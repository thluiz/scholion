---
url: "https://poeticoding.com/distributed-phoenix-chat-with-pubsub-pg2-adapter"
captured_at: "2026-11-16T03:43:59+00:00"
title: "Distributed Phoenix Chat with PubSub PG2 adapter · Poeticoding"
domain: "poeticoding-com"
---

In this article we’ll see how to cluster the Phoenix Chat nodes, using a really powerful functionality embedded in BEAM (the Elixir/Erlang VM), for easily communicate between Elixir nodes. We’ll then see how `pg2` works and inspect how Phoenix efficiently broadcasts the messages in a distributed chat app.

We previously saw, in [Distributed Phoenix Chat using Redis PubSub](https://poeticoding.com/distributed-phoenix-chat-using-redis-pubsub/), how to distribute multiple Phoenix Chat nodes and broadcast the messages using Redis. It worked well and it’s really easy to setup, especially in a Kubernetes cluster. Each single Chat node just needs to know the internet Redis server DNS and port to connect to.

This approach is easy but has some **drawbacks**:

The Redis server acts as a single point of failure: if Redis goes down, the whole service goes down. There is no way for the nodes to broadcast messages to clients in other nodes.

We also need then to maintain a Redis server, or a new cluster of Redis servers. With Docker and Kubernetes it’s really easy to spawn new services in the cluster. But we need to keep in mind that maintaining a new server in production doesn’t come for free, especially under heavy loads.

## Clustering Elixir nodes

At first we need to fully connect each node to the other nodes, using the communication protocol embedded in the Erlang VM. I’ve briefly shown in [Running Elixir in Docker Containers](https://poeticoding.com/running-elixir-in-docker-containers/) how to connect multiple Elixir nodes using Docker.

Let’s quickly see how to manually connect two Elixir nodes using `iex` in two separate terminals. We need to start the two `iex` sessions setting the node name and IP with the `--name`

```
# Terminal 1
$ iex --name a@127.0.0.1
iex(a@127.0.0.1)>

# Terminal 2
$ iex --name b@127.0.0.1
iex(b@127.0.0.1)> Node.connect :"a@127.0.0.1"
true
iex(b@127.0.0.1)> Node.list
[":a@127.0.0.1"]
```

Using the function `Node.connect/1` we’ve created a cluster made by two nodes: `a@127.0.0.1` and `b@127.0.0.1`. Once the nodes are connected we can start sending messages to remote processes, like when we are on a single node.

```
# Terminal 1
iex(a@127.0.0.1)> Agent.start(
  fn -> %{hello: "world"} end, 
  name: {:global, GlobalAgent}
)
{:ok, #PID<0.116.0>} 


# Terminal 2
iex(b@127.0.0.1)> Agent.get {:global,GlobalAgent}, &(&1)
%{hello: "world"}
```

In `a@127.0.0.1` we start an `Agent` process, registering it under the `GlobalAgent` name in the global registry. The node `b@127.0.0.1` then sends a message to `GlobalAgent`, **running on** `a@127.0.0.1`, and get its state.

We can easily configure Phoenix to leverage this powerful functionality to broadcast messages to remote nodes.

## PG2 Module

Before configuring our Phoenix Chat with the PG2 PubSub adapter, let’s dig a bit into understanding what PG2 is and how it works.

`pg2` [is an Erlang module](http://erlang.org/doc/man/pg2.html) which implements _process grouping_. Process groups can be useful when we need to group processes distributed over multiple nodes, so we can easily monitor and message them.

> This module implements process groups. Each message can be sent to one, some, or all group members.\\
> 
> — [http://erlang.org/doc/man/pg2.html](http://erlang.org/doc/man/pg2.html)

Let’s see in practice how PG2 works, starting _three_ different Elixir nodes: `a@127.0.0.1`, `b@127.0.0.1` and `c@127.0.0.1`.

```
#Terminal 3
iex(c@127.0.0.1)> Node.connect :"a@127.0.0.1"
iex(c@127.0.0.1)> Node.connect :"b@127.0.0.1"

iex(c@127.0.0.1)> Node.list
[:"a@127.0.0.1", :"b@127.0.0.1"]

iex(c@127.0.0.1)> :pg2.create :agents_group
```

In the `c@127.0.0.1` node, we form the cluster connecting `c` to the other two nodes. We then create the `:agents_group` process group with the `:pg2.create/1` function.

Each node runs a local `pg2` process, which **monitors** the processes in the group and holding their `PID` in the local `:pg2_table` `ETS` table.  
Without going deeper into the pg2 implementation itself, let’s start an agent for each node and add it to the `:agents_group` we have just created.  
\\

```
# TERMINAL 1
iex(a@127.0.0.1)> {:ok, a_pid} = Agent.start fn -> :agent_a end
{:ok, #PID<0.121.0>}
iex(a@127.0.0.1)> :pg2.join :agents_group, a_pid

iex(a@127.0.0.1)> :pg2.get_members :agents_group
[#PID<0.121.0>]


# TERMINAL 2
iex(b@127.0.0.1)> {:ok, b_pid} = Agent.start fn -> :agent_b end
{:ok, #PID<0.126.0>}
iex(b@127.0.0.1)> :pg2.join :agents_group, b_pid

iex(b@127.0.0.1)> :pg2.get_members :agents_group
[#PID<10547.121.0>, #PID<0.126.0>]



# TERMINAL 3
iex(c@127.0.0.1)> {:ok, c_pid} = Agent.start fn -> :agent_c end
{:ok, #PID<0.126.0>}
iex(c@127.0.0.1)> :pg2.join :agents_group, c_pid

iex(c@127.0.0.1)> :pg2.get_members :agents_group
[#PID<10631.121.0>, #PID<10715.126.0>, #PID<0.126.0>]
```

![pg2 monitors the processes in the group](https://poeticoding.com/distributed-phoenix-chat-with-pubsub-pg2-adapter/pg2_monitors_agents.png)

pg2 monitors the processes in the group

We start an `Agent` process in each node, each one holding its own state. We add them to the `:agents_group` with the function `:pg2.join(:agents_group, agent_pid)`.

Once the agents are added to the group, pg2 starts to monitor them. If a process exits it will be immediately removed from the group. We’ve seen that’s quite easy to make multiple processes part of a group, but how can we send a message to the so-called group’s **members**?

```
iex(c)> :pg2.get_members(:agents_group) \
      |>  Enum.map( &Agent.get(&1,fn s-> s end) )

[:agent_a, :agent_b, :agent_c]
```

The `pg2` module doesn’t offer a `broadcast` or a `send` function to send a message to all the members. We need to enumerate the PIDs given by the `:pg2.get_members(:agents_group)` function and send them a message one by one. This actually gives us the freedom to selectively send a message to just a subset of the group’s members. We’ll see later how this freedom becomes handy.

```
# TERMINAL 1
iex(a)> Process.exit a_pid, :halt
iex(a)> :pg2.get_members :agents_group
[#PID<10547.126.0>, #PID<10546.126.0>]

# TERMINAL 2
iex(b)> :pg2.get_members :agents_group
[#PID<0.126.0>, #PID<10546.126.0>]
```

`pg2` monitors the processes joined in the group. When we halt one agent, we see how the process is immediately removed from the group.

Now I’m going to use the code in the [poeticoding/phoenix\_chat\_example](https://github.com/poeticoding/phoenix_chat_example) GitHub repository, under `pubsub_pg2` branch.

When we create a new Phoenix app, it comes with a PubSub PG2 adapter configured by default. \\

```
#config/config.exs
config :chat, ChatWeb.Endpoint,
  ...
  pubsub: [name: Chat.PubSub, adapter: Phoenix.PubSub.PG2]
```

So, coming from the previous version in the `pubsub_redis` branch, we just need to change the pubsub configuration in the `config/config.exs` file. Let’s open two `iex` nodes running each one a chat server on port `4000` and on port `4001`.\\

```
# NODE a
$ PORT=4000 iex --name a@127.0.0.1 -S mix phx.server
iex(a@127.0.0.1)>

# NODE b
$ PORT=4001 iex --name b@127.0.0.1 -S mix phx.server
iex(b@127.0.0.1)>
```

If we try to connect a browser to `4000` and another browser to `4001` we see that the messages are not propagated. The two nodes are not connected, we need to cluster them.

```
# NODE a
iex(a@127.0.0.1)> Node.connect :"b@127.0.0.1"
```

Once the nodes are connected, we see that the messages are correctly broadcasted from one browser to the other one. It works and we don’t need any other configuration. I find interesting to hack a bit around though, inspecting the `Phoenix.PubSub.PG2` adapter to understand how it works under the hood.

Each Phoenix node starts its own **local** `PubSub.PG2Server` and registers it in a `pg2` group with name `{:phx, Chat.PubSub}`. \\

```
iex(a)> :pg2.which_groups
[phx: Chat.PubSub]

iex(a)> :pg2.get_members {:phx, Chat.PubSub}
[#PID<25838.1566.0>, #PID<0.1820.0>]
```

The important thing to see here is that the **members** of the pg2 group are the PIDs of `PubSub.PG2Server` running in each node. If we spawn and connect another phoenix node in the cluster, we would see its `PubSub.PG2Server` PID as third member.

The members **are not** the users connection processes, this would be highly inefficient for how pg2 is built and because one single node would have to broadcast a single message to **each** **user** over multiple nodes.

![How Phoenix uses PubSub with pg2](https://poeticoding.com/distributed-phoenix-chat-with-pubsub-pg2-adapter/pg2.png)

How Phoenix uses PubSub with pg2

Let’s see **instead** how Phoenix handles a broadcast over multiple nodes.

*   We connect a browser to the http server on `b@127.0.0.1` node, port `4001`
*   We send a message to the chat room. This message is sent to the node `b`, via the WebSocket connection. The `PubSub.PG2Server`, running locally in the node, broadcasts the message to all the browsers connected to the same node.
*   The `PubSub.PG2Server` in `b` then forwards the message to the remote `PubSub.PG2Server` running in `a@127.0.0.1`.
*   `PubSub.PG2Server` in the `a` node then broadcasts the message to all the browser connected to the node.

In this way the message is replicated over the cluster network just one time!

Let’s try to manually send the broadcast message from the node `b` to the `PubSub.PG2Server` running in node `a`. The message looks like this.

```
#{:forward_to_local, fastlane, from_pid, topic, msg}
forward_msg = {
  :forward_to_local, Phoenix.Channel.Server, 
  :none, "rooms:lobby",
  %Phoenix.Socket.Broadcast{
    event: "new:msg",
    payload: %{body: "message from node b", user: "user_b"},
    topic: "rooms:lobby"
  }
}
```

We need at first to get the PIDs of the remote `PubSub.PG2Server`, which is part of the `{:phx, Chat.PubSub}` pg2 group.

```
iex(b@127.0.0.1)> [a_server_pid] = \
   :pg2.get_members({:phx, Chat.PubSub}) -- \ 
   :pg2.get_local_members({:phx, Chat.PubSub})
```

With `:pg2.get_members` we get all the members part of the group, which are the `PubSub.PG2Server` running locally in `b`, and the remote one running in `a`. `:pg2.get_local_members` returns only the processes running locally, in this case in node `b`.

Let’s connect a browser to the node `a` http server (port `4000`) and see what happens when forwarding a message to the `PG2Server` running in `a`.

```
iex(b@127.0.0.1)> send a_server_pid, forward_msg
```

![](https://poeticoding.com/distributed-phoenix-chat-with-pubsub-pg2-adapter/manually_send_a_msg-1.png)

We see how the message is correctly broadcasted, by the `PubSub.PG2Server` process, to the open connections.

## Wrap Up

We’ve seen how `pg2` works and how Phoenix conscientiously handles messages in a distributed PubSub. So far, we’ve always manually connected the nodes, which is an issue when we want to deploy our app into production and on a Kubernetes cluster.

In the screencast [Connecting Elixir Nodes with libcluster, locally and on Kubernetes](https://poeticoding.com/connecting-elixir-nodes-with-libcluster-locally-and-on-kubernetes/), you can see how to automatically cluster nodes and easily scale out using Kubernetes DNS for nodes auto-discovery.
