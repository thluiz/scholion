---
url: "https://papers.vincy.dev/distributed-pubsub-in-elixir?utm_medium=email&utm_source=elixir-radar"
captured_at: "2026-09-25T18:40:12+01:00"
title: "Distributed PubSub in Elixir"
domain: "papers-vincy-dev"
---

In this article, we’ll be exploring on building a distributed PubSub in Elixir. First, we’ll be building a local PubSub which will allow a process to broadcast a message to all local subscribers. Then, we’ll see how we can make it work on a distributed environment, taking inspiration from the battle-tested [Phoenix.PubSub](https://hexdocs.pm/phoenix_pubsub/Phoenix.PubSub.html) — which you should definitely use if you’re planning to use PubSub in your production app. We’ll be using concepts like Registry, Process Groups, Clusters, etc.

## What is PubSub?

PubSub (Publish/Subscribe) is a design pattern used for asynchronous communication between services. Instead of a process sending a message directly to another process, the **publisher** broadcasts a message with a topic and let **susbcribers** of that topic consume the message. This allows us to build loosely coupled services. To visualize this, let’s take a look at a real-world example, _radio stations_.

In this example, a radio station is considered a **publisher**. It broadcasts music, podcasts, or whatever through its assigned frequency. When we want to listen to a banger music, we tune in to our favorite radio station’s frequency. The radio station is not directly playing the music to us. It’s just **publishing** (broadcasting) to its assigned frequency, and us, being avid listeners, are **subscribed** (tuned in) to that frequency.

## Local PubSub

Now, let us build our local PubSub. In this article, we’ll be naming our PubSub system [**Hermes**](https://en.wikipedia.org/wiki/Hermes), for obvious reasons.

```
mix new hermes --sup
```

In a PubSub pattern, we need a mechanism where we could determine which processes are subscribed to which topics. In other words, we need to have a key-value storage for our processes. Fortunately, Elixir already provides this under the [Registry](https://hexdocs.pm/elixir/1.12/Registry.html) module.

## Registry

Registry is a local key-value process storage. It allows you to register the current process under a given key. To understand it better, let’s play with it.

First, let’s start the `Registry` process.

```
iex(1)> Registry.start_link(keys: :duplicate, name: MyPubSub)
{:ok, #PID<0.105.0>}
```

`keys: :duplicate` just means that we allow multiple processes to be registered under a single key. This is exactly what we need for a PubSub, one key/topic for multiple processes.

Now, let’s create a bunch of _subscribers_ and register them to our `MyPubSub` process registry. These processes would be registered under the key/topic, `:event_topic`. You can use any Elixir term as a topic. Depending on your use case, it’s usually an action that happened. For example, `:"user.updated"`.

```
iex(2)> for _i <- 1..3 do
...(2)>     spawn(fn ->
...(2)>       Registry.register(MyPubSub, :event_topic, nil)
...(2)>
...(2)>       receive do
...(2)>         message ->
...(2)>           IO.puts("#{inspect(self())} received: #{inspect(message)}")
...(2)>       end
...(2)>     end)
...(2)>   end
[#PID<0.107.0>, #PID<0.108.0>, #PID<0.109.0>]
```

Now that we have subscribers, we can try and broadcast a message to them. The Registry module has a function called [`dispatch/4`](https://hexdocs.pm/elixir/1.12/Registry.html#dispatch/4) which we could definitely use in this scenario. `dispatch/4` will iterate over the entries (in our case, subscribers) and do what we asked it to do.

```
iex(3)> Registry.dispatch(MyPubSub, :event_topic, fn entries ->
...(3)>   for {pid, _} <- entries, do: send(pid, {:hello, "world"})
...(3)> end)
:ok
#PID<0.109.0> received: {:hello, "world"}
#PID<0.108.0> received: {:hello, "world"}
#PID<0.107.0> received: {:hello, "world"}
```

Voila! We were able to broadcast a message to all registered process under the key/topic. We just demoed PubSub in our `iex` shell. Now let’s make it pretty and put it in our app, Hermes.

We want the `Registry` to start as soon as we start our app. So let’s put it in our app’s supervisor.

```
# lib/hermes/application.ex
...
def start(_type, _args) do
  children = [
    {Registry, keys: :duplicate, name: Hermes.Registry}
  ]

  opts = [strategy: :one_for_one, name: Hermes.Supervisor]
  Supervisor.start_link(children, opts)
end
...
```

Our Hermes module should have two functions, `subscribe/1` and `publish/2`. `subscribe/1` will subscribe the process to the topic while `publish/2` will broadcast a message to all subscribers of that topic.

```
# lib/hermes.ex
defmodule Hermes do
  @registry Hermes.Registry

  def subscribe(topic) do
    Registry.register(@registry, topic, nil)
  end

  def publish(topic, message) do
    Registry.dispatch(@registry, topic, fn entries ->
      for {pid, _} <- entries, do: send(pid, message)
    end)
  end
end
```

Let’s see if our local PubSub still works as expected.

```
iex -S mix

iex(1)> spawn(fn ->
...(1)>   Hermes.subscribe(:"user.updated")
...(1)>
...(1)>   receive do
...(1)>     message ->
...(1)>       IO.puts("#{inspect(self())} received: #{inspect(message)}")
...(1)>   end
...(1)> end)
#PID<0.167.0>
iex(2)> Hermes.publish(:"user.updated", {:user, %{id: 1, name: "John"}})
:ok
#PID<0.167.0> received: {:user, %{id: 1, name: "John"}}
```

## Distributed PubSub

Our current version of Hermes is already good enough… but only for single-node apps. This won’t suffice for a clustered app.

To fact-check this, spin up two instances of the app. For easy identification, we’ll just name our nodes Alice and Bob.

```
# Node: Alice
iex --sname alice -S mix
iex(alice@Zeus)1>

# Node: Bob
➜ iex --sname bob -S mix
iex(bob@Zeus)1>
```

Connect the two nodes.

```
# Node: Alice
iex(alice@Zeus)1> Node.connect(:"bob@Zeus")
:ok
```

Verify that they are connected and then subscribe to the `:"user.updated"` topic.

```
# Node: Bob
iex(bob@Zeus)1> Node.list()
[:alice@Zeus]
iex(bob@Zeus)2> Hermes.subscribe(:"user.updated")
{:ok, #PID<0.136.0>}
```

From Alice’s shell, broadcast a PubSub message.

```
# Node: Alice
iex(alice@Zeus)2> Hermes.publish(:"user.updated", {:user, %{id: 1, name: "John"}})
:ok
```

Observe Bob’s shell. You’ll notice that nothing happened. Even though they are connected, they don’t share the registry. Yes, they are connected, but it just means they can send and receive messages from other nodes in the cluster.

## Process Groups

This is where Erlang’s [pg](https://www.erlang.org/doc/apps/kernel/pg.html) module would come in. In its simplest definition, it enables processes in the cluster to be a member of a named group, thus the name `pg` (process group).

Just like how we started using `Registry`, let’s play with `pg` on our `iex` shell. Spin up two nodes and connect them.

```
# Node: Alice
iex --sname alice
iex(alice@Zeus)1>

# Node: Bob
➜ iex --sname bob
iex(bob@Zeus)1> Node.connect :"alice@Zeus"
true
iex(bob@Zeus)2> Node.list()
[:alice@Zeus]
```

Just like the `Registry`, we need to to start a `pg` process on both nodes before we can group processes.

```
# Node: Alice
iex(alice@Zeus)1> :pg.start_link()
{:ok, #PID<0.114.0>}

# Node: Bob
iex(bob@Zeus)3> :pg.start_link()
{:ok, #PID<0.116.0>}
```

Then on Bob’s shell, join a process group called `:my_group`.

```
# Node: Bob
iex(bob@Zeus)4> :pg.join(:my_group, self())
:ok
```

Bob’s iex shell is now part of the `:my_group` process group. Go back to Alice’s shell and see all the members of the group.

```
# Node: Alice
iex(alice@Zeus)2> [pid] = :pg.get_members(:my_group)
[#PID<13033.110.0>]
iex(alice@Zeus)3> send(pid, {:hello, "world"})
{:hello, "world"}

# Node: Bob
iex(bob@Zeus)6> flush
{:hello, "world"}
:ok
```

You will see the group’s member process from the remote node. Using the `send/1` function, you’ll be able to send a message to a process on a remote node.

We can use this for our distributed PubSub, right? Every subscriber process on each node can just join a `pg` group under the same key. Well, yes… but maybe not so efficient? If there are thousands of subscribers on a remote node, then we will be sending thousands of messages to a remote node. `Phoenix.PubSub` tackled this by having a designated local server process per node that is responsible for broadcasting to its local subscribers, kind of like a message coordinator. Only the local server processes are added in the `pg` group. So, in our case, if there are 3 nodes running, there will just be 3 members of the process group.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1727438463439/a4fc720f-b73c-49f3-99e4-1b7cd9e49ea7.png)

To ease up our life, let’s just use [`libcluster`](https://hexdocs.pm/libcluster/readme.html) for clustering.

```
# mix.exs
...
{:libcluster, "~> 3.4"}
...
```

Since we are just running our nodes on localhost, we can use the [`LocalEpmd`](https://hexdocs.pm/libcluster/Cluster.Strategy.LocalEpmd.html) strategy.

```
# lib/hermes/application.ex
...
def start(_type, _args) do
  ...
  topologies = [
    hermes_local: [
      strategy: Cluster.Strategy.LocalEpmd
    ]
  ]

  children = [
    {Cluster.Supervisor, [topologies, [name: Hermes.ClusterSupervisor]]},
    {Registry, keys: :duplicate, name: Hermes.Registry}
  ]
  ...
end
...
```

Once you start the app for Alice and Bob, you should see that they are connected automatically.

```
# Node: Bob

➜ iex --sname bob -S mix

18:30:17.705 [info] [libcluster:hermes_local] connected to :alice@Zeus
Interactive Elixir (1.17.2) - press Ctrl+C to exit (type h() ENTER for help)
iex(bob@Zeus)1> Node.list()
[:alice@Zeus]
```

Now that they are connected automatically, we can focus on building our distributed PubSub.

Let’s implement our local server process as a GenServer and add it to our app’s supervision tree.

```
# lib/hermes/pg_server.ex
defmodule Hermes.PGServer do
  use GenServer

  def start_link(_) do
    GenServer.start_link(Hermes.PGServer, [], name: Hermes.PGServer)
  end

  @impl GenServer
  def init(_args) do
    :pg.start_link()
    :pg.join({:hermes, Hermes.PubSub}, self())

    {:ok, []}
  end
end

# lib/hermes/application.ex
...
children = [
  {Cluster.Supervisor, [topologies, [name: Hermes.ClusterSupervisor]]},
  {Registry, keys: :duplicate, name: Hermes.Registry},
  Hermes.PGServer
]
...
```

Upon the GenServer’s initialization, it will also start the `pg` process on its default scope. Then, it will join the process group called `{:hermes, Hermes.PubSub}`. A process group’s name can be any Erlang term. Recompile both and verify that both Alice’s and Bob’s `pg` server are members of the `{:hermes, Hermes.PubSub}` process group.

```
# Node: Alice
iex(alice@Zeus)1> :pg.get_members({:hermes, Hermes.PubSub})
[#PID<22764.190.0>, #PID<0.208.0>]
```

Currently, `Hermes.publish/2` broadcasts only to local subscribers. Instead of broadcasting to registry entries, we need it to send messages to all the other nodes’ `Hermes.PGServer` process, which are members of the `{:hermes, Hermes.PubSub}` process group. Here’s the updated `Hermes.PGServer` module:

```
# lib/hermes.ex
defmodule Hermes do
  @registry Hermes.Registry
  @pg_group {:hermes, Hermes.PubSub}

  def subscribe(topic) do
    Registry.register(@registry, topic, nil)
  end

  def publish(topic, message) do
    for pid <- :pg.get_members(@pg_group), node(pid) != node() do
      send(pid, {:broadcast_to_local, topic, message})
    end

    broadcast_local(topic, message)
  end

  def broadcast_local(topic, message) do
    Registry.dispatch(@registry, topic, fn entries ->
      for {pid, _} <- entries, do: send(pid, message)
    end)
  end
end
```

`Hermes.publish/2` will now send a message to all the clustered nodes’ `Hermes.PGServer`. That module should be broadcasting it to its local subscribers.

```
# lib/hermes/pg_server.ex

...
@impl GenServer
def handle_info({:broadcast_to_local, topic, message}, state) do
  Hermes.broadcast_local(topic, message)
  {:noreply, state}
end
...
```

Once the node’s `Hermes.PGServer` process receives a message, it should broadcast it locally.

That should be it! You now have a PubSub that could broadcast to remote nodes… a distributed PubSub! 🎉

Before taking it out for a spin, let’s create a very basic client module so we can easily test that our PubSub works. This `Client` module just starts a GenServer process that subscribes to a specified topic. It will also just print out any messages it receive.

```
# lib/hermes/support/client.ex
defmodule Client do
  use GenServer

  def start_link(topic) do
    GenServer.start_link(__MODULE__, topic)
  end

  def init(topic) do
    Hermes.subscribe(topic)
    {:ok, topic}
  end

  def handle_info(msg, state) do
    IO.puts("Received: #{inspect(msg)}")
    {:noreply, state}
  end
end
```

Now that we have it in place, we can start testing it. I’m feeling a bit adventurous today so we’ll be connecting 3 nodes namely, `Alice`, `Bob`, and `Carol`.

```
# Node: Alice
iex --sname alice -S mix

# Node: Bob
iex --sname bob -S mix

# Node: Carol
iex --sname carol -S mix
```

Since we have configured `libcluster`, they should automatically discover and connect to each other.

For this test, we’ll have the following:

*   Alice:
    
    *   1 client subscribed to `:"user.created"`
        
    *   1 client subscribed to `:"user.updated"`
        
*   Bob:
    
    *   5 clients subscribed to `:"user.created"`
        
    *   0 clients subscribed to `:"user.updated"`
        
*   Carol:
    
    *   0 clients subscribed to `:"user.created"`
        
    *   2 clients subscribed to `:"user.updated"`
        

```
# Node: Alice
iex(alice@Zeus)1> Client.start_link(:"user.created")
{:ok, #PID<0.214.0>}
iex(alice@Zeus)2> Client.start_link(:"user.updated")
{:ok, #PID<0.215.0>}

# Node: Bob
iex(bob@Zeus)1> for _i <- 1..5, do: Client.start_link(:"user.created")
[
  ok: #PID<0.201.0>,
  ok: #PID<0.202.0>,
  ok: #PID<0.203.0>,
  ok: #PID<0.204.0>,
  ok: #PID<0.205.0>
]

# Node: Carol
iex(carol@Zeus)1> for _i <- 1..2, do: Client.start_link(:"user.updated")
[ok: #PID<0.197.0>, ok: #PID<0.198.0>]
```

Let’s try publishing a `:"user.created"` message from `Alice`.

```
# Node: Alice
iex(alice@Zeus)3> Hermes.publish(:"user.created", %{name: "Jade"})
:ok
Received: %{name: "Jade"}

# Node: Bob
Received: %{name: "Jade"}
Received: %{name: "Jade"}
Received: %{name: "Jade"}
Received: %{name: "Jade"}
Received: %{name: "Jade"}

# Node: Carol
# ** nothing new **
```

Since no clients in `Carol` are interested when users are created, nothing was broadcasted to its local subscribers.

Cool. Now, let’s try publishing a `:"user.updated"` message from Bob.

```
# Node: Alice
Received: %{id: 1, name: "Jadyline"}

# Node: Bob
iex(bob@Zeus)2> Hermes.publish(:"user.updated", %{id: 1, name: "Jadyline"})
:ok

# Node: Carol
Received: %{id: 1, name: "Jadyline"}
Received: %{id: 1, name: "Jadyline"}
```

Awesome! Our distributed PubSub seems to be working fine!

I would like to reiterate that what we built here is a simple toy example **solely for learning purposes and not meant to be used in production**. If you need a distributed PubSub for production, **just use the already battle-tested** [`Phoenix.PubSub`](https://hexdocs.pm/phoenix_pubsub/Phoenix.PubSub.html).

Link to full source code: [https://github.com/vinceurag/hermes](https://github.com/vinceurag/hermes)

See you on the next one!
