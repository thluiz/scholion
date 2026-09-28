---
url: "https://dev.to/pckrishnadas88/building-a-stateful-process-in-elixir-without-genserver-58eb"
captured_at: "2026-09-28T15:10:00+01:00"
title: "Building Distributed Systems in Elixir: Part 1 - Building a Stateful Process in Elixir Without GenServer"
domain: "dev-to"
---

> **Series:** Distributed Systems from First Principles — Part 1

`GenServer` is one of the most widely used OTP behaviours in Elixir. It provides a convenient abstraction for building long-running stateful processes, but behind the abstraction lies a surprisingly small set of ideas.

At its core, a stateful server is simply:

*   A process
*   That owns private state
*   Receives messages
*   Updates its state
*   Sends replies
*   Waits for the next message

This article builds a minimal stateful counter using only:

*   `spawn/1`
*   `send/2`
*   `receive`
*   recursion

No `GenServer`, `Agent`, or other OTP behaviours are used.

The objective is not to replace OTP, but to understand the message-passing model it builds upon.

* * *

## [](#the-problem)The Problem

Imagine multiple clients need access to a shared counter.

In many programming languages, the counter might simply be a mutable object.  

```
Counter
-------
value = 0
```

Enter fullscreen mode Exit fullscreen mode

Multiple threads can read or modify this value directly.

The BEAM follows a completely different design.

Processes never share memory.

Each process owns its own private state, and the only way to interact with another process is by sending it a message.

Instead of representing the counter as a shared variable, the counter itself becomes a process.

* * *

## [](#highlevel-design)High-Level Design

The counter process owns the state.

Clients never access that state directly.

Instead, they communicate using a simple protocol.  

```
                    +---------------------------+
                    |     Counter Process       |
                    |---------------------------|
                    | value = 0                 |
                    |                           |
                    | Mailbox                  |
                    +---------------------------+
                             ▲
                             │
                  Requests   │   Replies
                             │
                    +--------------------------+
                    |      Client Process      |
                    +--------------------------+
```

Enter fullscreen mode Exit fullscreen mode

The communication protocol consists of three request messages.  

```
{:get, caller_pid}
{:increment, caller_pid}
:stop
```

Enter fullscreen mode Exit fullscreen mode

The counter responds with:  

```
{:counter_value, value}
```

Enter fullscreen mode Exit fullscreen mode

Notice that clients never call functions inside the counter process.

Instead, they exchange messages.

* * *

## [](#complete-implementation)Complete Implementation

```
defmodule Counter do
  def start(initial_value \\ 0) do
    spawn(fn ->
      loop(initial_value)
    end)
  end

  def get(counter_pid) do
    send(counter_pid, {:get, self()})

    receive do
      {:counter_value, value} ->
        {:ok, value}
    after
      1000 ->
        {:error, :timeout}
    end
  end

  def increment(counter_pid) do
    send(counter_pid, {:increment, self()})

    receive do
      {:counter_value, value} ->
        {:ok, value}
    after
      1000 ->
        {:error, :timeout}
    end
  end

  def stop(counter_pid) do
    send(counter_pid, :stop)
  end

  defp loop(value) do
    receive do
      {:get, from_pid} ->
        send(from_pid, {:counter_value, value})
        loop(value)

      {:increment, from_pid} ->
        new_value = value + 1
        send(from_pid, {:counter_value, new_value})
        loop(new_value)

      :stop ->
        IO.puts("Counter stopped")

      unknown ->
        IO.inspect(unknown, label: "Unknown message")
        loop(value)
    end
  end
end

counter = Counter.start()

IO.inspect(Counter.get(counter), label: "Initial value")
IO.inspect(Counter.increment(counter), label: "After increment")
IO.inspect(Counter.increment(counter), label: "After second increment")
IO.inspect(Counter.get(counter), label: "Current value")

Counter.stop(counter)
```

Enter fullscreen mode Exit fullscreen mode

Expected output:  

```
Initial value: {:ok, 0}
After increment: {:ok, 1}
After second increment: {:ok, 2}
Current value: {:ok, 2}
Counter stopped
```

Enter fullscreen mode Exit fullscreen mode

* * *

## [](#understanding-the-implementation)Understanding the Implementation

## [](#1-starting-the-server)1\. Starting the Server

```
def start(initial_value \\ 0) do
  spawn(fn ->
    loop(initial_value)
  end)
end
```

Enter fullscreen mode Exit fullscreen mode

`spawn/1` creates a new lightweight BEAM process.

That process immediately starts executing `loop/1`.

The value passed to `loop/1` becomes the process's private state.

The returned PID is **not** the counter value.

It is simply the address used to communicate with the counter process.

* * *

## [](#2-reading-the-counter)2\. Reading the Counter

The implementation of `get/1` surprises many developers.  

```
send(counter_pid, {:get, self()})
```

Enter fullscreen mode Exit fullscreen mode

At first glance, it feels strange that a function called `get()` sends a message.

The reason is simple.

The client cannot access another process's memory.

Instead of reading a variable, it asks the process that owns the state.

The message  

```
{:get, self()}
```

Enter fullscreen mode Exit fullscreen mode

contains two pieces of information:

*   `:get` → the requested operation
*   `self()` → the PID of the caller

The caller PID is included because the counter needs to know where to send the reply.

Immediately after sending the request, the client waits.  

```
receive do
  {:counter_value, value} ->
    {:ok, value}
end
```

Enter fullscreen mode Exit fullscreen mode

This `receive` does **not** read the message that was just sent.

Instead, it waits for a **new message** created by the counter process.

* * *

## [](#3-updating-the-counter)3\. Updating the Counter

Incrementing the value follows exactly the same request–reply pattern.

The client sends:  

```
{:increment, caller_pid}
```

Enter fullscreen mode Exit fullscreen mode

The counter updates its private state and sends the updated value back.

Notice that the client never performs the increment itself.

Only the counter process can modify its own state.

* * *

## [](#4-the-receive-loop)4\. The Receive Loop

The receive loop is the heart of the server.  

```
receive do
  {:get, from_pid} ->
    ...

  {:increment, from_pid} ->
    ...

  :stop ->
    ...
end
```

Enter fullscreen mode Exit fullscreen mode

Each incoming message is pattern matched.

The atom (`:get`, `:increment`, `:stop`) identifies which operation should be performed.

Once the operation completes, the process calls `loop/1` again.  

```
loop(0)

↓

loop(1)

↓

loop(2)
```

Enter fullscreen mode Exit fullscreen mode

The state is never mutated.

Instead, every new state is passed into the next iteration of the loop.

* * *

## [](#message-flow)Message Flow

The interaction between the client and the counter looks like this.  

```
Client Process                     Counter Process

{:get, caller_pid}
-------------------------------------->

                           Reads current value

                           {:counter_value, 0}

<--------------------------------------

{:increment, caller_pid}
-------------------------------------->

                           value = value + 1

                           {:counter_value, 1}

<--------------------------------------
```

Enter fullscreen mode Exit fullscreen mode

Two messages are exchanged.

The client sends a request.

The counter sends a reply.

The client never reads the message it originally sent.

* * *

## [](#why-this-design)Why This Design?

Using message passing instead of shared memory provides an important guarantee.

Every request enters the process mailbox.  

```
Mailbox

1. {:increment, pid1}
2. {:increment, pid2}
3. {:get, pid3}
```

Enter fullscreen mode Exit fullscreen mode

The counter processes one message at a time.

No two clients can modify the state simultaneously.

The process itself serializes access to its private state.

This model avoids many of the synchronization problems commonly associated with shared mutable memory.

* * *

## [](#what-does-genserver-add)What Does GenServer Add?

This implementation already demonstrates the core behaviour of a stateful server.

`GenServer` builds on the same ideas while providing:

*   Standard request handling
*   Request correlation
*   Timeouts
*   Monitoring
*   Supervision
*   Debugging support
*   System messages
*   Consistent APIs

Understanding the raw implementation makes these abstractions much easier to appreciate.

* * *

## [](#summary)Summary

This small example demonstrates several fundamental ideas behind the BEAM.

*   Processes own private state.
*   Processes communicate only through messages.
*   State is maintained through recursive receive loops.
*   A `get()` operation is a request–reply conversation, not a memory read.
*   A stateful server is simply a process implementing a message protocol.

Although intentionally minimal, this example forms the foundation for understanding `GenServer`, supervision trees, distributed messaging, and many other OTP concepts explored in later articles.

* * *

**Source Code**

The complete runnable example is available on GitHub:

**Repository:** _[https://github.com/pckrishnadas88/elixir-distributed-systems-lab/tree/main/01-process-mailbox](https://github.com/pckrishnadas88/elixir-distributed-systems-lab/tree/main/01-process-mailbox)_

## [](#series)Series

1.  **Building a Stateful Process in Elixir Without GenServer**
2.  [Correlated Request/Reply](https://dev.to/pckrishnadas88/building-distributed-systems-with-elixir-02-correlated-request-reply-4b2a)
3.  [Process Monitoring](https://dev.to/pckrishnadas88/building-distributed-systems-in-elixir-part-3-process-monitoring-5b5p)
4.  [Process Linking](https://dev.to/pckrishnadas88/building-distributed-systems-in-elixir-part-4-process-linking-okb)

* * *

Next: [Part 2 — Correlated Request/Reply](https://dev.to/pckrishnadas88/building-distributed-systems-with-elixir-02-correlated-request-reply-4b2a) →

* * *

## [](#content-license)Content License

This article is licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). You may share and adapt it with attribution for non-commercial purposes. The accompanying source code remains licensed under the MIT License.
