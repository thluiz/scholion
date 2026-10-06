---
url: "http://www.reactive.io/tips/2015/02/07/introduction-to-distributed-messaging-with-elixir/"
captured_at: "2015-05-25T21:39:32-03:00"
title: "Introduction to Distributed Messaging with Elixir - Reactive.TIPS - The Official Blog of Reactive.IO"
domain: "reactive-io"
---

# [Introduction to Distributed Messaging with Elixir](http://www.reactive.io/tips/2015/02/07/introduction-to-distributed-messaging-with-elixir)

Sooner or later, applications grow to the point that multiple computers, and often multiple data centers, are needed to host them. Many times, these systems are architected using databases to connect multiple nodes, often causing points of contention. Elixir however, has distributed messaging built right in thanks to its Erlang heritage, and offers many ways to connect nodes across racks, data centers, and even oceans. By using these messaging patterns, your real-time software can continue growing past the boundaries of hardware, while managing the latency and failure inherent in physical separation.

### Prerequisites

[Introduction to Parallel Computing with Elixir](http://www.reactive.io/tips/2015/02/03/introduction-to-parallel-computing-with-elixir/)

### Connecting Two Nodes

Let’s start off by connecting two nodes and running some distributed code. In your terminal, start two `iex` sessions with an `sname`. In Erlang, the `sname`, or Short Name, is the unique name for this node across the connected network. Start one node with the `sname` of “alice”, and another with the `sname` of “bob”. We’ll also make a small module called `Greet` with a function called `say` in the `bob` node.

**alice node**

```
$ iex --sname alice
iex(alice@MacBook-Pro)1>
```

**bob node**

```
$ iex --sname bob
iex(bob@MacBook-Pro)1> defmodule Greet do
...(bob@MacBook-Pro)1>   def say(name), do: "Hello #{name}, nice to meet you"
...(bob@MacBook-Pro)1> end
```

Notice the full name of the node, as the part after the `@` sign will most likely be different on your computer. For example, the “alice” node has the full name of `alice@MacBook-Pro` on my computer.

Now that these node are ready to go, let’s connect them. On the “alice” node, run the following.

```
iex(alice@MacBook-Pro)1> Node.ping(:"bob@MacBook-Pro")
:pong
iex(alice@MacBook-Pro)2> Node.ping(:"charlie@MacBook-Pro")
:pang
iex(alice@MacBook-Pro)3> Node.list
[:"bob@MacBook-Pro"]
iex(alice@MacBook-Pro)4>
```

Notice when we pinged the “bob” node, we got back a `:pong` response, but instead got a `:pang` response from the nonexistent “charlie” node. Also, after pinging an available node, we can see we’re connected by running the `Node.list` function. As the “alice” and “bob” node are hooked up, we can get right to running some remote calls.

```
iex(alice@MacBook-Pro)4> :rpc.call(:"bob@MacBook-Pro", Greet, :say, ["alice"])
"Hello alice, nice to meet you"
iex(alice@MacBook-Pro)5>
```

It might not seem like much, but notice how we ran the `Greet.say` function on the “alice” node while the code was only compiled on the “bob” node. We did this with the `:rpc` (Remote Procedure Call) module built into Erlang. Using is one way to handle distributed messaging, but things get really interesting when you realize that processes work across distributed nodes as well. Let’s check that out.

> **Why is the module called :rpc and not ?**
>
> As Elixir runs on top of the Erlang VM, it has access to all of the modules that come along with it. One convention for Elixir is that any module or library that was written in Erlang and not Elixir should be called with its original `:lowercase.function` syntax instead of Elixir’s `Uppercase.function` syntax. As the `:rpc` module is a trusty Erlang built-it, we’re going to use it here.

### Building Our Server

We’re going to have two different projects as part of this tutorial; a `Client` and `Server` application that will talk to each other natively. For the `Server` project, run `mix new server` and put the following into the `Server` module.

**server: /lib/server.ex**

```
require Logger

defmodule Server 
  @name :stack

   start 
      spawn __MODULE__ :loop HashDict 
    :globalregister_name@name 
  

    stack 
    receive 
      :subscribe   ->
        Logger subscribed"
        HashDict   stack
      :unsubscribe  ->
        Logger unsubscribed"
        HashDictdelete  stack
      :push   ->
        Logger gave: '
        notify:push   
            stack
        ->
         lengthstack   
          Logger"whoops, stack is empty"
          HashDict  :notify :empty
           
        
               stack
          Logger took: '
          notify   
           stack
        
        ->
        Logger requested stack"
         HashDict  :notify  stack
         stack
       ->
         stack
    
  

   notifyaction    
     _name  <-  
        :notify action
```

The server is really a simple receive loop that keeps track of subscribers with a `HashDict`, and the stack contents with a list. Subscribers are a HashDict entry with the name as the key and Client as a value. The stack is a list of tuples of who added an item, and what the item is. From there, we can use list comprehension to notify all subscribers in the `subs` variable. The really interesting part is in the `start` function where we register the server’s with `:global.register_name(@name, pid)`. This Erlang built-in ensures that `:stack` is a global identifier so other nodes across the network can find its .

When you’re done typing, run the program with `iex --sname server -S mix` and start the server in IEx with `Server.start`. You should get a `:yes` atom returned if everything kicked off correctly.

### Now Time For The Client

The `Client` is going to connect to the `Server` and subscribe to any updates that change the stack. This way, everyone knows who is pushing and popping what. Generate this project with `mix new client` and put the following into the `Client` module.

**client: /lib/client.ex**

```
require Logger

defmodule Client 
  defstruct    

  @name :stack

   connect 
    connect:"server@MacBook-Pro"
  

   subscribe 
      spawn__MODULE__ :notify 

     server :subscribe  

    Client   
  

   unsubscribeClient    
     server :unsubscribe 
      :stop
  

   Client   
     server :push  
  

   Client  
     server  
  

   Client  
     server  
  

   notify 
    receive 
      :notify :push   ->
        Logger gave: '
        notify
      :notify     ->
        Logger took: '' from: 
        notify
      :notify  stack ->
        Logger"current stack: inspectstack
        notify
      :notify :empty ->
        Logger"nothing left to pop"
        notify
      :stop ->
        Logger"stopping"
       ->
        notify
    
  

   server 
    :globalwhereis_name@name
```

In this module we are spawning a process that will log changes to the stack, and passing it to the `Server` along with the client’s name. We are also using a struct to package our client name and for an easier interface. The `:global` module comes back when we trade the `:stack` identifier for the `Server` pid with `:global.whereis_name(@name)`. With this module, we can now subscribe to the server and modify the stack remotely.

### Off To The Races

Kick off two client IEx sessions, one with `iex --sname alice -S mix` and another with `iex --sname bob -S mix`. Make sure the two previous “alice” and “bob” sessions are terminated, or you will get a sname collision error. Once they are running, it’s time to send some messages.

**alice node**

```
iex(alice@MacBook-Pro)1> Client.connect
true
iex(alice@MacBook-Pro)2> alice = Client.subscribe("alice")
%Client{name: "alice", pid: #PID<0.91.0>}
```

**bob node**

```
iex(bob@MacBook-Pro)1> Client.connect
true
iex(bob@MacBook-Pro)2> bob = Client.subscribe("bob")
%Client{name: "bob", pid: #PID<0.96.0>}
iex(bob@MacBook-Pro)3> Node.list
[:"server@MacBook-Pro", :"alice@MacBook-Pro"]
```

Now that all nodes are connected, we’re ready to roll. Have both clients push and pop messages on the stack and notice how all three nodes are getting real-time updates on what is going on.

**alice node**

```
iex(alice@MacBook-Pro)3> Client.push(alice, "Howdy Partner!")
{:push, "alice", "Howdy Partner!"}
04:43:13.563 [info]  alice gave: 'Howdy Partner!'
iex(alice@MacBook-Pro)4>
04:43:50.830 [info]  bob gave: 'Hey There!'
iex(alice@MacBook-Pro)5> Client.get(alice)
{:get, "alice"}
04:44:04.661 [info]  current stack: [{"bob", "Hey There!"}, {"alice", "Howdy Partner!"}]
iex(alice@MacBook-Pro)6> Client.pop(alice)
{:pop, "alice"}
04:44:14.245 [info]  alice took: 'Hey There!' from: bob
iex(alice@MacBook-Pro)7>
04:44:21.620 [info]  bob took: 'Howdy Partner!' from: alice
iex(alice@MacBook-Pro)8>
iex(alice@MacBook-Pro)9> Client.unsubscribe(alice)
:stop
04:46:24.352 [info]  stopping
iex(alice@MacBook-Pro)10>
```

**bob node**

```
iex(bob@MacBook-Pro)4>
04:43:13.563 [info]  alice gave: 'Howdy Partner!'
iex(bob@MacBook-Pro)5> Client.push(bob, "Hey There!")
04:43:50.830 [info]  bob gave: 'Hey There!'
{:push, "bob", "Hey There!"}
iex(bob@MacBook-Pro)6>
04:44:14.245 [info]  alice took: 'Hey There!' from: bob
iex(bob@MacBook-Pro)7> Client.pop(bob)
{:pop, "bob"}
04:44:21.620 [info]  bob took: 'Howdy Partner!' from: alice
iex(bob@MacBook-Pro)8> Client.pop(bob)
{:pop, "bob"}
04:44:23.884 [info]  nothing left to pop
iex(bob@MacBook-Pro)9>
```

**server node**

```
04:40:06.776 [info]  alice subscribed
04:40:57.371 [info]  bob subscribed
04:43:13.559 [info]  alice gave: 'Howdy Partner!'
04:43:50.829 [info]  bob gave: 'Hey There!'
04:44:04.661 [info]  alice requested stack
04:44:14.244 [info]  alice took: 'Hey There!'
04:44:21.620 [info]  bob took: 'Howdy Partner!'
04:44:23.884 [info]  whoops, stack is empty
04:46:24.352 [info]  alice unsubscribed
```

As you send a few messages to the server and see it pop up on all three clients in real-time, you start understanding how easy it can be to make a distributed system using Elixir. What makes Elixir so powerful is that these nodes would work the same way if they were on two different cities, or even two different continents.

### Summary

By using the same data types and process spawning we’re used to, along with some handy built-in modules, we were able to quickly build a distributed system with relative ease. We also learned a bit more about Elixir’s relationship with Erlang, how we can use Erlang functions with no penalty, and pass messages to and from different nodes as easily as if they were sharing the same runtime. These very benefits are why Erlang is commonly used to build large messaging systems and also why Elixir can help make such development even easier.
