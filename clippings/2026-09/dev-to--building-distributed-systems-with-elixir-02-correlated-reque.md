---
url: "https://dev.to/pckrishnadas88/building-distributed-systems-with-elixir-02-correlated-request-reply-4b2a"
captured_at: "2026-09-28T15:10:20+01:00"
title: "Building Distributed Systems with Elixir — 02: Correlated Request–Reply"
domain: "dev-to"
---

In the previous example, we built a minimal stateful process using `spawn`, `send`, and `receive`.

A client could send a request:  

```
{:get, self()}
```

Enter fullscreen mode Exit fullscreen mode

and the server could reply:  

```
{:counter_value, value}
```

Enter fullscreen mode Exit fullscreen mode

That gives us basic request–reply communication.

But there is an important question we haven't answered yet:

**If a process makes multiple requests, how do we know which reply belongs to which request?**

This is the problem we'll explore in this example.

We will continue using raw Elixir process primitives without `GenServer`, `Task`, or other OTP abstractions.

* * *

## [](#the-problem)The Problem

Every Elixir process has a PID.

A client can include its PID in a request:  

```
send(server, {:request, self(), value})
```

Enter fullscreen mode Exit fullscreen mode

The server can then use that PID to send the response:  

```
send(from, {:reply, result})
```

Enter fullscreen mode Exit fullscreen mode

For a simple request this works.

But a PID identifies a **process**, not an individual request.

The same process can make many requests during its lifetime.  

```
Client #PID<0.95.0>

    request 10
    request 20
    request 30
```

Enter fullscreen mode Exit fullscreen mode

All three requests come from the same process.

So we have two separate questions:  

```
Where should the reply go?

Which request does the reply belong to?
```

Enter fullscreen mode Exit fullscreen mode

A PID answers the first question.

We need something else to answer the second.

* * *

## [](#creating-a-request-id)Creating a Request ID

Elixir provides `make_ref/0`.  

```
ref = make_ref()
```

Enter fullscreen mode Exit fullscreen mode

It creates a unique reference.

For example:  

```
#Reference<0.2323213673.1614020613.213691>
```

Enter fullscreen mode Exit fullscreen mode

Calling it again produces another reference.  

```
ref1 = make_ref()
ref2 = make_ref()
```

Enter fullscreen mode Exit fullscreen mode

These references can be used as request identifiers.

So instead of sending:  

```
{:request, self(), value}
```

Enter fullscreen mode Exit fullscreen mode

we send:  

```
{:request, self(), ref, value}
```

Enter fullscreen mode Exit fullscreen mode

Our protocol now contains both pieces of information:  

```
self() -> where should the response go?

ref    -> which request is this?
```

Enter fullscreen mode Exit fullscreen mode

* * *

## [](#the-server)The Server

The server is intentionally small.  

```
defmodule Server do
  def start do
    spawn(fn -> loop() end)
  end

  defp loop do
    receive do
      {:request, from, ref, value} ->
        IO.puts("Server received request: #{value}")

        result = value * 2

        send(from, {:reply, ref, result})

        loop()

      :stop ->
        IO.puts("Server stopped")
        :ok
    end
  end
end
```

Enter fullscreen mode Exit fullscreen mode

The important part is the protocol.

The server receives:  

```
{:request, from, ref, value}
```

Enter fullscreen mode Exit fullscreen mode

It processes the request:  

```
result = value * 2
```

Enter fullscreen mode Exit fullscreen mode

and returns the **same reference**:  

```
send(from, {:reply, ref, result})
```

Enter fullscreen mode Exit fullscreen mode

The server doesn't generate a new reference.

It simply returns the request identifier supplied by the client.

Conceptually:  

```
Client                              Server

       {:request, pid, ref1, 10}
---------------------------------->

                                  10 * 2

          {:reply, ref1, 20}
<----------------------------------
```

Enter fullscreen mode Exit fullscreen mode

The request and response are now correlated by `ref1`.

* * *

## [](#the-client)The Client

The client creates the reference.  

```
defmodule Client do
  def request(server, value) do
    ref = make_ref()

    IO.puts("Client #{inspect(self())} sending #{value}")
    IO.puts("Request ref: #{inspect(ref)}")

    send(server, {:request, self(), ref, value})

    receive do
      {:reply, ^ref, result} ->
        IO.puts(
          "Client #{inspect(self())} received matching reply :#{result}"
        )

        {:ok, result}
    end
  end
end
```

Enter fullscreen mode Exit fullscreen mode

There is one particularly important line here:  

```
{:reply, ^ref, result}
```

Enter fullscreen mode Exit fullscreen mode

Why `^ref` instead of just `ref`?

* * *

## [](#matching-the-correct-reply)Matching the Correct Reply

Before entering `receive`, the client already created a reference:  

```
ref = make_ref()
```

Enter fullscreen mode Exit fullscreen mode

Suppose conceptually its value is:  

```
ref2
```

Enter fullscreen mode Exit fullscreen mode

Now imagine the mailbox contains:  

```
{:reply, ref1, 20}
{:reply, ref2, 40}
{:reply, ref3, 60}
```

Enter fullscreen mode Exit fullscreen mode

The client is interested only in the response for `ref2`.

That's what the pin operator does:  

```
receive do
  {:reply, ^ref, result} ->
    {:ok, result}
end
```

Enter fullscreen mode Exit fullscreen mode

`^ref` means:

> Match against the value already stored in `ref`.

So:  

```
{:reply, ref1, 20}  -> doesn't match
{:reply, ref2, 40}  -> matches
{:reply, ref3, 60}  -> doesn't match
```

Enter fullscreen mode Exit fullscreen mode

The process can select the matching message while unmatched messages remain in its mailbox.

This is **selective receive**.

* * *

## [](#pid-vs-request-reference)PID vs Request Reference

This distinction was the most useful part of this example for me.

Consider three requests made by the same process:  

```
Client #PID<0.95.0>

request 10 -> ref1
request 20 -> ref2
request 30 -> ref3
```

Enter fullscreen mode Exit fullscreen mode

The PID doesn't change.

The request reference does.

So they represent different things:  

```
PID = process identity

REF = request identity
```

Enter fullscreen mode Exit fullscreen mode

Or from the server's perspective:  

```
PID -> where do I send the reply?

REF -> which request am I replying to?
```

Enter fullscreen mode Exit fullscreen mode

A process and an operation are not the same thing.

* * *

## [](#running-the-example)Running the Example

The project is kept deliberately small:  

```
02-correlated-request-reply/
├── client.ex
├── server.ex
├── example.exs
└── README.md
```

Enter fullscreen mode Exit fullscreen mode

The example starts the server and makes several requests.  

```
server = Server.start()

IO.inspect(Client.request(server, 10))
IO.inspect(Client.request(server, 20))
IO.inspect(Client.request(server, 30))

send(server, :stop)
```

Enter fullscreen mode Exit fullscreen mode

Run:  

```
elixir example.exs
```

Enter fullscreen mode Exit fullscreen mode

Example output:  

```
Client #PID<0.95.0> sending 10
Request ref: #Reference<...>
Server received request: 10
Client #PID<0.95.0> received matching reply :20
{:ok, 20}

Client #PID<0.95.0> sending 20
Request ref: #Reference<...>
Server received request: 20
Client #PID<0.95.0> received matching reply :40
{:ok, 40}

Client #PID<0.95.0> sending 30
Request ref: #Reference<...>
Server received request: 30
Client #PID<0.95.0> received matching reply :60
{:ok, 60}

Server stopped
```

Enter fullscreen mode Exit fullscreen mode

Something interesting is visible in this output.

The PID remains:  

```
#PID<0.95.0>
```

Enter fullscreen mode Exit fullscreen mode

while every request gets a different reference.

That's exactly what we wanted.

* * *

## [](#what-about-multiple-client-processes)What About Multiple Client Processes?

BEAM processes are lightweight, so we can also have multiple clients communicating with the same server.  

```
for value <- [40, 50, 60] do
  spawn(fn ->
    IO.inspect(Client.request(server, value))
  end)
end
```

Enter fullscreen mode Exit fullscreen mode

Now the architecture looks more like:  

```
Client A #PID<0.101.0> ---- refA ----\
                                      \
Client B #PID<0.102.0> ---- refB -----> Server
                                      /
Client C #PID<0.103.0> ---- refC ----/
```

Enter fullscreen mode Exit fullscreen mode

Each client has its own PID.

Each request also has its own reference.

The server doesn't need to know anything about how those clients were created.

It understands only the protocol:  

```
{:request, from, ref, value}
```

Enter fullscreen mode Exit fullscreen mode

and:  

```
{:reply, ref, result}
```

Enter fullscreen mode Exit fullscreen mode

* * *

## [](#if-every-request-has-its-own-process-do-we-still-need-a-request-id)If Every Request Has Its Own Process, Do We Still Need a Request ID?

This was a question I had while building the example.

Suppose we create one process for every request.

Each process has a unique PID.

Couldn't the PID itself identify the request?

For a very simple one-request-per-process design, it sometimes could.

But that mixes two different concepts.

A process represents a unit of execution and isolation.

A reference identifies an operation.  

```
Process   = WHO

Reference = WHICH REQUEST
```

Enter fullscreen mode Exit fullscreen mode

A process may eventually have several operations in flight:  

```
One Client Process

    ├── request ref1
    ├── request ref2
    ├── request ref3
    └── request ref4
```

Enter fullscreen mode Exit fullscreen mode

If our protocol already contains request identifiers, it doesn't depend on the assumption that every request needs a new process.

Processes should be created when we want concurrency or isolation, not merely as a substitute for request IDs.

* * *

## [](#why-this-pattern-matters)Why This Pattern Matters

The idea itself isn't specific to Elixir.

The general pattern is:  

```
Request
   |
   +---- request_id
   |
   v
Server
   |
   +---- same request_id
   |
   v
Response
```

Enter fullscreen mode Exit fullscreen mode

Whenever requests and responses are asynchronous, some form of correlation can be useful.

The identifier might be:

*   a BEAM reference
*   a UUID
*   an integer
*   a protocol-specific request ID

The implementation changes, but the underlying problem is the same:

**Which response belongs to which request?**

* * *

## [](#what-we-have-so-far)What We Have So Far

After the first two examples, our tiny protocol has evolved from:  

```
Client
   |
   | message
   v
Process
```

Enter fullscreen mode Exit fullscreen mode

into:  

```
Client
   |
   | request + PID + request ID
   v
Server
   |
   | response + request ID
   v
Client
```

Enter fullscreen mode Exit fullscreen mode

We now understand:

*   process mailboxes
*   `send`
*   `receive`
*   request–reply communication
*   `make_ref/0`
*   request IDs
*   matching replies
*   selective receive
*   concurrent clients

But there is still a much bigger problem.

What happens if the process we're communicating with dies?  

```
Client
   |
   | request
   v
Server
   |
   X
```

Enter fullscreen mode Exit fullscreen mode

How does another process know that it terminated?

That's where process monitoring comes in.

* * *

## [](#next-process-monitoring)Next: Process Monitoring

In the next example I'll explore:  

```
Process.monitor(pid)
```

Enter fullscreen mode Exit fullscreen mode

and the `:DOWN` messages delivered when a monitored process terminates.

That will be the first step from basic message passing toward understanding how the BEAM detects and reacts to process failures.

The full source for this example is available in the repository: [https://github.com/pckrishnadas88/elixir-distributed-systems-lab/tree/main/02-correlated-request-reply](https://github.com/pckrishnadas88/elixir-distributed-systems-lab/tree/main/02-correlated-request-reply)

## [](#series)Series

1.  [Building a Stateful Process in Elixir Without GenServer](https://dev.to/pckrishnadas88/building-a-stateful-process-in-elixir-without-genserver-58eb)
2.  **Correlated Request/Reply**
3.  [Process Monitoring](https://dev.to/pckrishnadas88/building-distributed-systems-in-elixir-part-3-process-monitoring-5b5p)
4.  [Process Linking](https://dev.to/pckrishnadas88/building-distributed-systems-in-elixir-part-4-process-linking-okb)

* * *

← Previous: [Building a Stateful Process in Elixir Without GenServer](https://dev.to/pckrishnadas88/building-a-stateful-process-in-elixir-without-genserver-58eb)

Next: [Part 3 — Process Monitoring](https://dev.to/pckrishnadas88/building-distributed-systems-in-elixir-part-3-process-monitoring-5b5p) →

* * *

## [](#content-license)Content License

This article is licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). You may share and adapt it with attribution for non-commercial purposes. The accompanying source code remains licensed under the MIT License.
