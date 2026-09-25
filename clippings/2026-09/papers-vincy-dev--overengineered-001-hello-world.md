---
url: "https://papers.vincy.dev/overengineered-001-hello-world"
captured_at: "2026-09-25T18:40:52+01:00"
title: "Overengineered #001: Hello World"
domain: "papers-vincy-dev"
---

👋

Welcome to the first episode of **Overengineered**, a blog series I’m starting where we take simple problems and **build ridiculously complex and unnecessary solutions** — all for the sake of learning and fun. Most of the solutions will be written in Elixir but feel free to join the fun using any other language!

Every journey into learning a programming language starts with a “Hello World.” I remember my first time compiling and executing my first program. It was exhilarating. It gave me a sense of accomplishment… even though it’s just a terminal that shows “Hello World.” Now, let’s revisit the same problem, equipped with the knowledge and experience we've gained along the way.

## The Problem

**Hello World** in programming is just printing the phrase “Hello World”. Here’s how to do it in some languages:

```
// Elixir
IO.puts("Hello World")

// Python
print("Hello World")

// Ruby
puts "Hello World"

// Java
System.out.println("Hello World");
```

But, where’s the fun in that? In this article, we’ll be building a **distributed Hello World system**:

*   multiple distributed nodes
    
*   auto-discovery of nodes
    
*   whenever a node joins, all the other nodes will send a “hello world” message to it
    

## Project Setup

To kick off, let’s create an Elixir project with a supervision tree and application callback:

```
➜ mix new distributed_hello_world --sup
```

We want to generate it like that since we will be creating **GenServers** that executes instructions on application boot up.

## Node Auto-discovery

One of our requirements is for nodes to automatically discover and connect to each other. There should be no manual `Node.connect/1` calls whenever there’s a new node. There are couple of libraries we could use for this like [`libcluster`](https://github.com/bitwalker/libcluster) which supports a bunch of strategies. If you’re looking for a robust and well-tested clustering mechanism, you should take a look at those. But since we are overengineering here, we would roll our own using the idea from libcluster’s [Gossip strategy](https://hexdocs.pm/libcluster/Cluster.Strategy.Gossip.html).

## How it works

For our clustering mechanism, we’ll use **UDP broadcast** for node discovery. We’ll use **UDP (User Datagram Protocol)** to send packets over the network without needing a connection. It’s perfect for fire-and-forget type of messages like “Hey, I’m here”.

When we use UDP broadcast, we send a packet to everyone on the local network by targeting the _limited broadcast address_ (255.255.255.255). All nodes that listen to the same UDP port will receive the message.

## NodeManager

Since we have our strategy laid out, let’s start building it. We’ll be dealing with UDP so we need to use Erlang’s [`gen_udp`](https://www.erlang.org/docs/26/man/gen_udp) module. To send and receive UDP packets, we need to call `:gen_udp.open/2` which opens a UDP socket bound to a port. We need to make sure that all the nodes send and listen to the same UDP port. For this example, we’ll use the port `45826`.

Once we have the socket, we would be able to broadcast messages via `:gen_udp.send/4`.

Let’s play with it a little bit. Fire up your IEx shell.

```
iex(1)> {:ok, socket} = :gen_udp.open(45826, [:binary, active: true, broadcast: true, reuseport: true])
{:ok, #Port<0.3>}
iex(2)> :gen_udp.send(socket, {255, 255, 255, 255}, 45826, "HELLO WORLD")
:ok
iex(3)> flush
{:udp, #Port<0.3>, {192, 168, 68, 61}, 45826, "HELLO WORLD"}
:ok
```

Once you open a UDP socket, it associates the port number to the calling process so all the packets will arrive in the calling process’ mailbox.

We want the node auto-discovery and connection to happen on application startup. To achieve this, we’ll create a **GenServer** that opens a UDP socket upon initialization.

```
defmodule DistributedHelloWorld.NodeManager do
  use GenServer

  @port 45826
  @heartbeat_interval 2_000

  def start_link(_) do
    GenServer.start_link(__MODULE__, %{}, name: __MODULE__)
  end

  def init(_) do
    {:ok, udp_socket} =
      :gen_udp.open(@port, [:binary, active: true, broadcast: true, reuseport: true])

    {:ok, %{socket: udp_socket}, {:continue, :heartbeat}}
  end
end
```

Now that the UDP socket is open, we can start sending and receiving packets. Since UDP messages arrive in the calling process’ mailbox, we can use `handle_info/2` to receive it. Let’s also create a catch-all `handle_info/2` and inspect its messages.

```
defmodule DistributedHelloWorld.NodeManager do
  ...

  def handle_continue(:heartbeat, state) do
    send(self(), :heartbeat)
    {:noreply, state}
  end

  def handle_info(:heartbeat, state) do
    :gen_udp.send(state.socket, {255, 255, 255, 255}, @port, :erlang.term_to_binary(node()))

    Process.send_after(self(), :heartbeat, @heartbeat_interval)

    {:noreply, state}
  end

  def handle_info(msg, state) do
    IO.inspect(msg)
    {:noreply, state}
  end

  ...
end
```

Run the app while providing a name:

```
➜ iex --sname alice -S mix

Erlang/OTP 27 [erts-15.0] [source] [64-bit] [smp:14:14] [ds:14:14:10] [async-threads:1] [jit]

Compiling 1 file (.ex)
Interactive Elixir (1.17.2) - press Ctrl+C to exit (type h() ENTER for help)
{:udp, #Port<0.5>, {192, 168, 68, 61}, 45826,
 <<131, 119, 10, 97, 108, 105, 99, 101, 64, 90, 101, 117, 115>>}
```

As you may have noticed, the calling node also received the UDP message. This is because we are broadcasting it to everyone on the local network… including us. Let’s handle the message. Since we now have the node name, we should be able to connect to it.

```
defmodule DistributedHelloWorld.NodeManager do
  use GenServer

  ...

  def handle_info({:udp, _, _, _, node_bin}, state) do
    node = :erlang.binary_to_term(node_bin)

    if node() != node && node not in Node.list() do
      Node.connect(node)
    end

    {:noreply, state}
  end

  ...
end
```

Make sure to add this **GenServer** to the supervision tree.

```
defmodule DistributedHelloWorld.Application do
  use Application

  @impl true
  def start(_type, _args) do
    children = [
      DistributedHelloWorld.NodeManager
    ]

    opts = [strategy: :one_for_one, name: DistributedHelloWorld.Supervisor]
    Supervisor.start_link(children, opts)
  end
end
```

Let’s test this out by spinning up two nodes, `alice` and `bob`. They should be connected automatically.

```
# Node: alice
➜ iex --sname alice -S mix
iex(alice@Zeus)1> Node.list()
[:bob@Zeus]

# Node: bob
➜ iex --sname bob -S mix
iex(bob@Zeus)1> Node.list()
[:alice@Zeus]
```

## A bit of a problem…

Run `alice` node again then open up another terminal. On this new terminal, issue this command:

```
➜ echo "Test" | nc -u 127.0.0.1 45826
```

You’ll see that there’s an error that happened in `alice` node.

```
➜ iex --sname alice -S mix
Erlang/OTP 27 [erts-15.0] [source] [64-bit] [smp:14:14] [ds:14:14:10] [async-threads:1] [jit]

Interactive Elixir (1.17.2) - press Ctrl+C to exit (type h() ENTER for help)

13:20:04.779 [error] GenServer DistributedHelloWorld.NodeManager terminating
** (ArgumentError) errors were found at the given arguments:

  * 1st argument: invalid external representation of a term

    :erlang.binary_to_term("Test\n")
    (distributed_hello_world 0.1.0) lib/distributed_hello_world/node_manager.ex:32: DistributedHelloWorld.NodeManager.handle_info/2
    (stdlib 6.0) gen_server.erl:2173: :gen_server.try_handle_info/3
    (stdlib 6.0) gen_server.erl:2261: :gen_server.handle_msg/6
    (stdlib 6.0) proc_lib.erl:329: :proc_lib.init_p_do_apply/3
Last message: {:udp, #Port<0.5>, {127, 0, 0, 1}, 62202, "Test\n"}
State: %{socket: #Port<0.5>}
```

This happens because our app listens to a specific UDP port. Our app will receive all the packets sent to that port. We can solve this by **scoping**. To scope the message, we’ll just prefix it with `node::`.

```
...
  def handle_info(:heartbeat, state) do
    :gen_udp.send(
      state.socket,
      {255, 255, 255, 255},
      @port,
      "node::" <> :erlang.term_to_binary(node())
    )

    Process.send_after(self(), :heartbeat, @heartbeat_interval)

    {:noreply, state}
  end

  def handle_info({:udp, _, _, _, <<"node::", node_bin::binary>>}, state) do
    node = :erlang.binary_to_term(node_bin)

    if node() != node && node not in Node.list() do
      Node.connect(node)
    end

    {:noreply, state}
  end

  def handle_info({:udp, _socket, _ip, _port, _}, state) do
    {:noreply, state}
  end
...
```

Now, our app only listens and reacts to packets that are prefixed with `node::` and ignores the others.

Here’s the full **NodeManager** code:

```
defmodule DistributedHelloWorld.NodeManager do
  use GenServer

  @port 45826
  @heartbeat_interval 2_000

  def start_link(_) do
    GenServer.start_link(__MODULE__, %{}, name: __MODULE__)
  end

  def init(_) do
    {:ok, udp_socket} =
      :gen_udp.open(@port, [:binary, active: true, broadcast: true, reuseport: true])

    {:ok, %{socket: udp_socket}, {:continue, :heartbeat}}
  end

  def handle_continue(:heartbeat, state) do
    send(self(), :heartbeat)
    {:noreply, state}
  end

  def handle_info(:heartbeat, state) do
    :gen_udp.send(
      state.socket,
      {255, 255, 255, 255},
      @port,
      "node::" <> :erlang.term_to_binary(node())
    )

    Process.send_after(self(), :heartbeat, @heartbeat_interval)

    {:noreply, state}
  end

  def handle_info({:udp, _, _, _, <<"node::", node_bin::binary>>}, state) do
    node = :erlang.binary_to_term(node_bin)

    if node() != node && node not in Node.list() do
      Node.connect(node)
    end

    {:noreply, state}
  end

  def handle_info({:udp, _socket, _ip, _port, _}, state) do
    {:noreply, state}
  end
end
```

Nice! All nodes automatically discover and connect to each other. Now let’s move on to the next part, the **Greeter**.

## Hello World, folks

Once a new node joins a cluster, it will greet all the nodes and get some greetings too. Just like the previous part, we’ll also be building a **GenServer**.

## The Greeter

For us to know when a node joins the cluster, we need to monitor the nodes. We can do this by using `:net_kernel.monitor_nodes(true)`.

```
defmodule DistributedHelloWorld.Greeter do
  use GenServer

  require Logger

  def start_link(_) do
    GenServer.start_link(__MODULE__, %{}, name: __MODULE__)
  end

  def init(_arg) do
    :net_kernel.monitor_nodes(true)

    {:ok, %{}}
  end

  def handle_info(msg, state) do
    IO.inspect(msg)

    {:noreply, state}
  end
end
```

Let’s see what messages we receive when we monitor the nodes.

```
# Node: alice
iex --sname alice -S mix
{:nodeup, :bob@Zeus}

# Node: bob
➜ iex --sname bob -S mix
{:nodeup, :alice@Zeus}

# alice disconnects...
{:nodedown, :alice@Zeus}
```

To fulfill the requirements, we just need to send a greeting message to the node when we receive the `:nodeup` message. And whenever we receive the `:greet` message, we print it via Logger along with the name of the node that sent it.

```
defmodule DistributedHelloWorld.Greeter do
  use GenServer

  ...

  def handle_info({:nodeup, node}, state) do
    GenServer.cast({__MODULE__, node}, {:greet, node()})

    {:noreply, state}
  end

  def handle_cast({:greet, node}, state) do
    Logger.info("Hello world from " <> inspect(node))

    {:noreply, state}
  end

  ...
end
```

Here’s the full code of the **Greeter** module.

```
defmodule DistributedHelloWorld.Greeter do
  use GenServer

  require Logger

  def start_link(_) do
    GenServer.start_link(__MODULE__, %{}, name: __MODULE__)
  end

  def init(_arg) do
    :net_kernel.monitor_nodes(true)

    {:ok, %{}}
  end

  def handle_info({:nodeup, node}, state) do
    GenServer.cast({__MODULE__, node}, {:greet, node()})

    {:noreply, state}
  end

  def handle_info({:nodedown, _}, state) do
    {:noreply, state}
  end

  def handle_cast({:greet, node}, state) do
    Logger.info("Hello world from " <> inspect(node))

    {:noreply, state}
  end
end
```

Just like the NodeManager, make sure to add it to the supervision tree.

```
defmodule DistributedHelloWorld.Application do
  ...

  def start(_type, _args) do
    children = [
      DistributedHelloWorld.Greeter,
      DistributedHelloWorld.NodeManager
    ]

    opts = [strategy: :one_for_one, name: DistributedHelloWorld.Supervisor]
    Supervisor.start_link(children, opts)
  end
end
```

Let’s test our Distributed Hello World app by spinning up nodes `alice` and `bob`.

```
➜ iex --sname alice -S mix
Erlang/OTP 27 [erts-15.0] [source] [64-bit] [smp:14:14] [ds:14:14:10] [async-threads:1] [jit]

Compiling 1 file (.ex)
Interactive Elixir (1.17.2) - press Ctrl+C to exit (type h() ENTER for help)
iex(alice@Zeus)1>
```

Nothing happened yet. Now let’s observe what happens when we run `bob`.

```
➜ iex --sname bob -S mix
Erlang/OTP 27 [erts-15.0] [source] [64-bit] [smp:14:14] [ds:14:14:10] [async-threads:1] [jit]

Interactive Elixir (1.17.2) - press Ctrl+C to exit (type h() ENTER for help)

00:59:02.539 [info] Hello world from :alice@Zeus
iex(bob@Zeus)1>
```

Go back to `alice` and you’ll notice that it also received a greeting from `bob`.

```
# Node: alice
00:59:02.538 [info] Hello world from :bob@Zeus
```

Now let’s see what happens when a third node joins the cluster. Enter `charlie`…

```
➜ iex --sname charlie -S mix
Erlang/OTP 27 [erts-15.0] [source] [64-bit] [smp:14:14] [ds:14:14:10] [async-threads:1] [jit]

Interactive Elixir (1.17.2) - press Ctrl+C to exit (type h() ENTER for help)

01:02:19.497 [info] Hello world from :alice@Zeus

01:02:19.498 [info] Hello world from :bob@Zeus
iex(charlie@Zeus)1>
```

It got greetings from both `alice` and `bob`. Go back to both `alice` and `bob` nodes and see how it reacted.

```
# Node: alice
01:02:19.494 [info] Hello world from :charlie@Zeus

# Node: bob
01:02:19.498 [info] Hello world from :charlie@Zeus
```

## Wrapping Up

So there you have it — a **multi-node Hello World**.

What did we actually do here?

*   built our own node-discovery mechanism via UDP broadcast
    
*   Node monitoring
    
*   an app that says hello to everyone in the cluster
    

Was it overkill? Absolutely — and that’s the point of this series!

Again, this is **just for fun and learning**. If you need a **robust node-discovery mechanism**, check out [`libcluster`](https://github.com/bitwalker/libcluster).

Link to full source code: [https://github.com/vinceurag/distributed\_hello\_world](https://github.com/vinceurag/distributed_hello_world)

Awesome! I hope you had fun reading and following along this first **Overengineered** post. I’ll be making more of this so if you want this kind of content, feel free to subscribe to my newsletter. For suggestions/feedback, please use this [form](https://vin.cy/overengineered-form). If you want to join the fun and take a jab at the problem yourself, please tag me — I'd love to see what you come up with!

Happy overengineering and see you on the next one!
