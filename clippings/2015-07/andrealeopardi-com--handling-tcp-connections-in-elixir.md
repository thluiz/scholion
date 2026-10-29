---
url: "http://andrealeopardi.com/posts/handling-tcp-connections-in-elixir/?utm_campaign=elixir_radar_13&utm_medium=email&utm_source=RD+Station"
captured_at: "2015-07-19T10:40:45-03:00"
title: "Handling TCP connections in Elixir"
domain: "andrealeopardi-com"
---

# Handling TCP connections in Elixir

Elixir is frequently used in network-aware applications because of the core design of Erlang and the Erlang VM. In this context, there's often the need to connect to external services through the network: for example, a classic web application could connect to a relational database and a key-value store, while an application that runs on embedded systems could connect to other nodes on the network.

Many times, the connection with the network service will be transparent to the programmer thanks to external libraries (e.g., database drivers), but I think it's interesting to know how to handle such connections by hand. This turns out to be useful if there are no external libraries for a particular service but also if we want to understand how these libraries work.

In this article we will only talk about TCP connections since TCP is probably the most common protocol used in network applications. The principles we describe, however, are very similar for any other type of connection (for example, connections that use the UDP protocol).

## A semi-realistic example

For the sake of this article, we will build an *almost* working driver for the [Redis](http://redis.io/) key-value store. A Redis server is just a TCP server sends and receives messages. Redis uses its own protocol (more on this in a while) on top of TCP to exchange data, without relying on common protocols such as HTTP, but we will not focus on that: we will only deal with the TCP connection from Elixir to the Redis server.

A little side note: obviously, there are several Erlang and Elixir libraries for talking to Redis, but bear with me. Since there's no point in coming up with a clever name for the library we're going to write, we'll just call it `Redis`.

Let's get started!

## Brief overview of TCP connections in Erlang/Elixir

In Erlang and Elixir, TCP connections are handled using the [`:gen_tcp`](http://www.erlang.org/doc/man/gen_tcp.html) module. In this article we'll only set up clients that connect to an external TCP server, but the `:gen_tcp` module can also be used to set up TCP servers.

All messages to the server are sent using `:gen_tcp.send/2`. Messages sent from the server to the client are usually delivered to the client process as Erlang messages, so it's straightforward to work with them. As we will see later on, we can control how messages are delivered to the client process with the value of the `:active` option on the TCP socket.

To establish a connection with a TCP server we use `:gen_tcp.connect/3` passing the host (as a charlist, damn you Erlang!), the port and a list of options. By default, the process that calls `connect/3` is the "controlling process" of the TCP connection, which means that TCP messages from the socket will be delivered to it.

That's all we need to know about TCP connections for now, let's move on.

## First implementation

We'll use a `GenServer` as the only interface with the TCP connection. We need a GenServer so that we will be able to keep the TCP socket in the GenServer's state and reuse that socket for all commication.

### Establishing the connection

Since the GenServer will be the only interface to the TCP server and it will only hold a single TCP socket in its state, we want it to always be connected to the TCP server. The best strategy for this is establishing the connection when the GenServer is started, in the `init/1` callback. `init/1` is called when `GenServer.start_link/2` is used to start the process, and the GenServer doesn't start to do any work until `init/1` returns, so it's the perfect place for us.

```
defmodule Redis 
   GenServer

  @initial_state socket 

   start_link 
    GenServerstart_link__MODULE__ @initial_state
  

   state 
      :binary active false
     socket  :gen_tcpconnect'localhost'  
     state  socket socket
```

The options we pass to `:gen_tcp.connect/3` are straightforward. `:binary` instructs the socket to deliver messages from the TCP server to the GenServer as binaries instead of Erlang strings (charlists): in Elixir this is probably what we want, and it's probably the most efficient choice as well. `active: false` tells the socket to never deliver TCP messages as Erlang messages to the GenServer process; we will have to manually retrieve those messages using [`:gen_tcp.recv/2`](http://www.erlang.org/doc/man/gen_tcp.html#recv-2). We do this so that the GenServer isn't flooded with messages coming from the TCP server: we only retrieve messages when we're ready to process them.

### Sending messages

We now have a GenServer which is connected to a Redis server. Let's send commands to the Redis server now.

#### RESP protocol

At this point, I should mention the Redis binary protocol, RESP: this is the protocol that Redis uses to encode and decode commands and responses. The [specification for this protocol](http://redis.io/topics/protocol) is short and simple to understand, so I encourage you to go read it if you want to know more. For the purpose of this article, we'll assume we have a full RESP encoder/decoder (`Redis.RESP`) which provides two functions:

- `Redis.RESP.encode/1` which encodes a list into a Redis command, like this:

```
Redis.RESPencode"GET" "mykey" # <<...>>
```

- `Redis.RESP.decode/1` which decodes a binary into an Elixir term, like this:

```
resp_to_get_command  <<...>>
Redis.RESPdecoderesp_to_get_command #=> 1
```

#### `:gen_tcp.send/2`

As we mentioned at the beginning of the article, we use `:gen_tcp.send/2` to send messages through a TCP socket. Our `Redis` module will provide a single function to send commands to the Redis server: `Redis.command/2`. The implementation is straightforward:

```
defmodule Redis 
  # ...as before...

   command  
    GenServer :command 
  

   handle_call:command   socket socket  state 
      :gen_tcpsocket Redis.RESPencode

    # `0` means receive all available bytes on the socket.
       :gen_tcpsocket 
     Redis.RESPdecode state
```

This works fine...

```
   Redisstart_link
Rediscommand "SET" "mykey" 
Rediscommand "GET" "mykey" #=> 1
```

...but there's a big problem.

## What went wrong

Long story short: `:gen_tcp.recv/2` is blocking!

The code we wrote would work just fine if the GenServer would be used by just one Elixir process. This is what happens when an Elixir process wants to send a command to the Redis server:

1. the Elixir process calls `command/2` on the GenServer and *blocks*, waiting for the response
2. the GenServer sends the command to the Redis server and *blocks* on `:gen_tcp.recv/2`
3. the Redis server responds to the GenServer
4. the GenServer responds to the Elixir process

Can you spot the problem? The GenServer is blocked when it waits for the Redis server to respond. While this is fine when a single Elixir process talks to the GenServer, it instantly becomes terrible when more processes want to communicate with the Redis server through the GenServer. Luckily, we can implement a much better solution.

## Queuing for the win

As you probably know, the `handle_call/3` callback in a GenServer doesn't have to return a result to the client right away: it can return a `{:noreply, state}` tuple and then reply to the client using [`GenServer.reply/2`](http://elixir-lang.org/docs/stable/elixir/GenServer.html#reply/2).

This is exacly what we need here: a way for clients to call a function on the GenServer and block waiting for the response, but at the same time a way for the GenServer to keep doing work until it has a response **for that specific client**.

In order continue with this strategy, however, we need to ditch `:gen_tcp.recv/2` in favour of receiving TCP messages as Erlang messages. We can do that using the `active: true` instead of `active: false` when connecting to the Redis server: when `:active` is `true`, all messages from a TCP socket are delivered as Erlang messages in the form of `{:tcp, socket, message}`.

What will happen is this:

1. the Elixir process calls `command/2` on the GenServer and **blocks**, waiting for the response
2. the GenServer sends the command to the Redis server and returns `{:noreply, state}` so that it doesn't block
3. the Redis server responds to the GenServer, which receives a `{:tcp, socket, message}` message
4. the GenServer handles the message in the `handle_info/2` callback, responding to the appropriate client

As you can see, the main difference is that from the moment the GenServer sends a command to the Redis server to the moment it receives a response, the GenServer is not blocked and it can send other commands to the server. This is great!

The last thing we need to deal with is how the GenServer is supposed to respond to the **right** request: when it receives a `{:tcp, ...}` message, how does it know who to send it back with `GenServer.reply/2`? Since we're sure Redis responds to requests *sequentially* (first in, first out), we can use a simple queue to keep a list of Elixir processes waiting for a response. We'll keep this queue in the GenServer's state, enqueueing clients when they make a request and dequeueing them when a response is delivered.

```
defmodule Redis 
  @initial_state socket  queue :queue
  # ...as before...

   handle_call:command   queue   state 
    # We send the command...
      :gen_tcpstatesocket Redis.RESPencode

    # ...enqueue the client...
    state  state  queue :queue 

    # ...and we don't reply right away.
    :noreply state
  

   handle_info socket  socket socket  state 
    # We dequeue the next client
    :value client new_queue  :queuestatequeue

    # We can finally reply to the right client.
    GenServerreplyclient Redis.RESPdecode

    :noreply state  queue new_queue
```

## Messages on demand

In the sections above, we moved from an `active: false` socket to an `active: true` socket in order to receive TCP data as Erlang messages. This works fine, but can lead to problems if the TCP server sends the GenServer *a lot* of data: since Erlang has no limit on the message queue of a process, the GenServer can be easily flooded with messages; after all, we chose to use `active: false` for this reason in the first place. To avoid that, we can change `active: true` to the more conservative `active: :once`: this way, only one TCP messages is delivered as an Erlang message, and then the socket goes back to `active: false`. We can set `active: :once` again to receive the next message, and so on. We can process TCP data as Erlang messages but one at the time, so that we're sure we're able to process them.

We just have to remember to reactivate the socket when we receive a `{:tcp, ...}` message in the `handle_info/2` callback. We can do that using [`:inet.setopts/2`](http://www.erlang.org/doc/man/inet.html#setopts-2).

```
defmodule Redis 
  # ...as before...

   handle_call socket  socket socket  state 
    # Allow the socket to send us the next message
    :inetsetoptssocket active :once

    # exactly as before
```

## Plot twist

I didn't think of the pattern I wrote about. That's a shocker, right? The pattern I described here is very common and is shared by a number of Erlang and Elixir applications. This pattern applies nicely to any connection with a TCP server (or with anything similar for that matter), and it's often used in drivers for databases: that's why I went with Redis in the example.

Lots of real-world libraries use the pattern I talked about: for example, [eredis](https://github.com/wooga/eredis) (one of the most used Redis drivers for Erlang) is built very similarly to our example: just look at [this comment](https://github.com/wooga/eredis/blob/770f828918db710d0c0958c6df63e90a4d341ed7/src/eredis_client.erl#L1-L21) in the eredis source, which is basically a summary of this article (or is this article an expanded version of that comment? Who knows!). Other examples of libraries that roughly follow this pattern are the Elixir drivers for PostgreSQL ([postgrex](https://github.com/ericmj/postgrex)) and MongoDB ([mongodb](https://github.com/ericmj/mongodb)). Currently I'm working on an Elixir driver for [OrientDB](http://orientdb.com/orientdb/) (still not public) which uses this pattern as well. So, it must work right?

## Better handling of the TCP connection

We happily ignored an annoying thing to deal with throughout this article: error handling!

We'll keep happily ignoring a subset of the errors that can happen, e.g., an empty client queue (which fails the `{{:value, val}, new_queue}` pattern match) or an incomplete message from the TCP socket. However, a common set of errors that can happen when dealing with TCP connections are, well, TCP errors like dropped connections or timeouts.

We could try to handle this kind of errors ourselves, but, luckily for us, Elixir core team member James Fish (aka [fishcakez](https://github.com/fishcakez)) did most of the work in its awesome library [connection](https://github.com/fishcakez/connection). While this library is quite young at the time of writing, it's already being used in the [MongoDB driver](https://github.com/ericmj/mongodb) I mentioned before and in the OrientDB driver I'm working on.

### Handling connections with... Connection

The connection library defines the `Connection` behaviour: the API specified by this behaviour is a superset of the `GenServer` API, so it's easy to understand and integrate into existing projects.

The [docs](http://hexdocs.pm/connection) explain what `Connection` does in great detail, but the gist of it is this: it helps implement a process that has a peer it connects to and has to deal with that peer being possibly unavailable. To do this, the `Connection` behaviour defines two additional functions (other than the `GenServer` ones) and revises the return values of some `GenServer` callbacks.

We will only look at some of the functionality provided by `Connection` here, but make sure to read the docs if you want to know more.

### Connecting on startup

Our `Redis.init/1` callback implementation performs the connection to the Redis server, blocking the process that called `Redis.start_link/0` until it returns. This may be fine as we don't want our GenServer to be able to do anything before it's connected to the Redis server. However, `start_link/0` may be called by a supervisor or by a process specifically designed to just *start* the GenServer: in these cases, we'd like `start_link/0` to return `{:ok, pid}` as soon as possible, handling the process of establishing the TCP connection in the background. We'd also like the GenServer to queue messages until it's connected to the Redis server. This behaviour would enable us to start the GenServer without blocking the process that called `start_link/0`, but blocking all subsequent requests until the GenServer is connected to Redis.

With `Connection` we can do exactly this. Returning `{:connect, info, state}` from the `init/1` callback (instead of `{:ok, state}`) makes `init/1` return `{:ok, pid}` instantly, but also calls the `connect/2` callback on the GenServer and stops the GenServer from processing incoming messages until the connection is complete. The `info` element in the `{:connect, info, state}` tuple should contain any information needed to connect to the peer but that we don't want to keep in the GenServer's state.

Let's change our code to take advantage of this:

```
defmodule Redis 
   Connection
  @initial_state socket 

   start_link 
    # We need Connection.start_link/2 now,
    # not GenServer.start_link/2
    Connectionstart_link__MODULE__ @initial_state
  

   state 
    # We use `nil` as we don't need any additional info
    # to connect
    :connect  state
  

   connect_info state 
      :binary active :once
     socket  :gen_tcpconnect'localhost'  
     state  socket socket
```

This is a big improvement over what we had before, but `Connection` allows us to make our library even better.

### Backoff!

The line where we connect to the Redis server using `:gen_tcp.connect/3` should raise a loud alarm bell in your head: `{:ok, socket} = ...` is not very responsible. In case the connection fails for any reason, the pattern match will fail and, instead of handling the error, the whole GenServer blows up. The obvious thing to do is to handle the result of `:gen_tcp.connect/3` with a case statement:

```
 :gen_tcpconnect'localhost'   
   socket ->
     state  socket socket
  :error reason ->
    # now what?
```

Now we have to decide what we want to do in case there's an error. Blowing up the GenServer or returning the error to the client is trivial, but in real-world™ code we would probably want to try to reconnect to the TCP server. `Connection` to the rescue! We can make `connect/2` return a `{:backoff, timeout, state}` tuple: `connect/2` will be called again after `timeout` in an attempt to reconnect to the peer. Our `connect/2` would look like this:

```
 connect_info state 
    :binary active :once

   :gen_tcpconnect'localhost'   
     socket ->
       state  socket socket
    :error reason ->
       "TCP connection error: inspect reason
      :backoff  state # try again in one second
```

The great thing about `Connection` is that you can return `{:backoff, timeout, state}` from almost every callback function, so handling connection failures become straightforward.

When `{:backoff, timeout, state}` is returned, `connect/2` is called with `:backoff` as its first argument: this lets us easily detect **re**-connections (instead of first connections) and deal with them appropriately. For example, we may want to implement exponential backoff, i.e., we retry after one second, then after two seconds, then after four seconds and so on, possibly with a maximum number of retries.

## Pooling

Just one last tip: the GenServer we built can be used smoothly with pooling libraries like the famous [poolboy](https://github.com/devinus/poolboy). There's plenty of literature about poolboy around the web, so I'm not going to describe how it works here. I will just show you a small example.

First, we can can create a pool of a given number of our GenServers using `:poolboy.start_link/2`.

```
poolboy_opts  worker_module Redis  
redis_opts    
    :poolboystart_linkpoolboy_opts redis_opts
```

Then, we can just checkout worker processes (which are our `Redis` GenServers) out of the pool, perform operations on Redis through them, and then check them back in the pool.

```
worker  :poolboycheckout
Rediscommandworker "SET" "mykey" 
  :poolboycheckin worker
```

Nothing smoother than that!

## Conclusion

We saw how to implement a GenServer that works as an interface to a TCP server. We built a non-blocking GenServer that queues clients in order to send multiple commands to the TCP server while waiting for responses from the server. We used the [connection](https://github.com/fishcakez/connection) library to deal with TCP errors (e.g., the server being temporarely unavailable) by implementing a backoff strategy. Finally, we briefly looked at how [poolboy](https://github.com/devinus/poolboy) can be used to make a pool of our GenServers.

Thanks for reading!
