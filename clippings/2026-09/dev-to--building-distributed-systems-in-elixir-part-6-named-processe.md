---
url: "https://dev.to/pckrishnadas88/building-distributed-systems-in-elixir-part-6-named-processes-l3"
captured_at: "2026-09-28T15:11:59+01:00"
title: "Building Distributed Systems in Elixir: Part 6 — Named Processes"
domain: "dev-to"
---

In the previous part of this series, we built a tiny supervisor from scratch.

When a worker crashed, the supervisor started a replacement. That replacement had a new PID:  

```
old worker -> #PID<0.102.0>
new worker -> #PID<0.105.0>
```

Enter fullscreen mode Exit fullscreen mode

This reveals an important limitation of sharing PIDs as a public interface.

A PID identifies one running incarnation of a process. It is excellent for sending a reply, setting up a monitor, or creating a link. It is not a stable address for a service that may stop and later be replaced.

In this part, we'll use named processes to give a worker a discoverable address:  

```
:worker
```

Enter fullscreen mode Exit fullscreen mode

We'll build three small examples using:  

```
Process.register/2
Process.whereis/1
:global.register_name/2
:global.whereis_name/1
send/2
```

Enter fullscreen mode Exit fullscreen mode

No `GenServer`.

No OTP `Registry`.

The goal is to understand the lookup problem that registries solve before reaching for those abstractions.

* * *

## [](#the-pidsharing-problem)The PID-Sharing Problem

Suppose one process starts a worker and gives its PID to a client:  

```
worker = spawn(fn -> worker_loop() end)
send(client, {:worker_started, worker})
```

Enter fullscreen mode Exit fullscreen mode

The client can now send work directly:  

```
send(worker, {:work, self(), "hello"})
```

Enter fullscreen mode Exit fullscreen mode

This works while that particular worker process is alive.

But process IDs are temporary. If the worker exits, the PID is no longer a route to the service:  

```
Client                         Worker

holds #PID<0.102.0>            #PID<0.102.0>
     |                               |
     |                               X exits
     |
     | send(#PID<0.102.0>, work)
     |------------------------------> no worker receives it
```

Enter fullscreen mode Exit fullscreen mode

Sending to a dead local PID does not raise an error and does not restart a process. The message is simply not delivered to a living worker.

One answer is to tell every client about every new PID after a restart. That spreads lifecycle knowledge throughout the system.

Another answer is to make clients depend on a name and resolve that name when sending.

* * *

## [](#registering-a-local-name)Registering a Local Name

Our first worker waits for a stop message:  

```
defmodule Worker do
  def start do
    spawn(fn ->
      receive do
        :stop -> :ok
      end
    end)
  end
end
```

Enter fullscreen mode Exit fullscreen mode

Starting it gives us a PID:  

```
pid = Worker.start()
```

Enter fullscreen mode Exit fullscreen mode

We can associate that PID with a local name:  

```
Process.register(pid, :worker)
```

Enter fullscreen mode Exit fullscreen mode

The registration belongs to the current BEAM node.  

```
local process registry

:worker  ->  #PID<0.102.0>
```

Enter fullscreen mode Exit fullscreen mode

The atom `:worker` is now a registered local name. We can retrieve its current PID with:  

```
Process.whereis(:worker)
```

Enter fullscreen mode Exit fullscreen mode

In the example, the returned PID is the same PID that we registered:  

```
registered_pid = Process.whereis(:worker)
```

Enter fullscreen mode Exit fullscreen mode

`Process.whereis/1` returns `nil` if the name is not registered on this node.

* * *

## [](#sending-to-the-name)Sending to the Name

There is often no need to perform a lookup yourself. `send/2` accepts a local registered name:  

```
send(:worker, :stop)
```

Enter fullscreen mode Exit fullscreen mode

The runtime resolves the name and delivers the message to its current owner.  

```
Caller                         Local Registry                  Worker
  |                                  |                           |
  | send(:worker, :stop)             |                           |
  |--------------------------------->| :worker -> worker PID     |
  |                                  |-------------------------->|
  |                                  |                           | receives :stop
```

Enter fullscreen mode Exit fullscreen mode

This is the first benefit of a name: code that sends the message need not carry a PID around.

Run the local example:  

```
elixir 01-process-registration.exs
```

Enter fullscreen mode Exit fullscreen mode

Typical output is:  

```
Worker PID: #PID<...>
Registered as :worker
Lookup using name: #PID<...>
Stopping using name: #PID<...>
```

Enter fullscreen mode Exit fullscreen mode

The PID values vary from run to run. The name in the code does not.

* * *

## [](#name-scope-matters)Name Scope Matters

`Process.register/2` is local to one node.

If two disconnected nodes both run:  

```
Process.register(pid, :worker)
```

Enter fullscreen mode Exit fullscreen mode

there is no conflict:  

```
Node A: :worker -> #PID<...>
Node B: :worker -> #PID<...>
```

Enter fullscreen mode Exit fullscreen mode

Each node has its own local process registry. Therefore:  

```
Process.whereis(:worker)
```

Enter fullscreen mode Exit fullscreen mode

answers only the question:

> Which local process on this node is registered as `:worker`?

It does not discover a process on another BEAM node.

That is exactly right for many services. A local cache, a local connection manager, or a supervisor-owned worker usually needs only node-local lookup.

For cluster-wide lookup, the system needs a broader naming mechanism.

* * *

## [](#a-global-name)A Global Name

Erlang supplies the `:global` module for a namespace coordinated across connected nodes.

The second example registers the worker with:  

```
:global.register_name(:worker, pid)
```

Enter fullscreen mode Exit fullscreen mode

and looks it up with:  

```
:global.whereis_name(:worker)
```

Enter fullscreen mode Exit fullscreen mode

The example then sends a message to the PID returned by that lookup:  

```
send(:global.whereis_name(:worker), :stop)
```

Enter fullscreen mode Exit fullscreen mode

Run it with:  

```
elixir 02-global-lookup.exs
```

Enter fullscreen mode Exit fullscreen mode

The script itself runs on a single node, so its output looks much like the local case. The distinction becomes meaningful after nodes are named and connected.

Conceptually, a connected cluster can coordinate one name:  

```
                       connected Erlang nodes

Node A                                                Node B
 Client                                               Worker
   |                                                    |
   | :global.whereis_name(:worker)                      |
   |--------------------> global name coordination -----|
   |<-------------------- worker PID -------------------|
   |                                                    |
   | send(worker_pid, message)                          |
   |--------------------------------------------------->|
```

Enter fullscreen mode Exit fullscreen mode

`:global` (written as `:global` in code) provides a useful primitive, but global coordination is not free. It has failure behavior and operational trade-offs that matter in a real cluster.

* * *

## [](#hiding-the-pid-from-clients)Hiding the PID From Clients

The third example changes the startup API.

Instead of returning the spawned PID, the worker registers itself and returns its public name:  

```
def start do
  pid =
    spawn(fn ->
      receive do
        {:work, from, request} ->
          send(from, {:reply, request, "processed: #{request}"})
      end
    end)

  Process.register(pid, :worker)
  :worker
end
```

Enter fullscreen mode Exit fullscreen mode

The caller receives:  

```
worker = Worker.start()
# :worker
```

Enter fullscreen mode Exit fullscreen mode

It does not receive or retain the worker PID.

The client sends its request to the name:  

```
send(worker_name, {:work, self(), request})
```

Enter fullscreen mode Exit fullscreen mode

The message protocol is still explicit:  

```
{:work, caller_pid, request}
```

Enter fullscreen mode Exit fullscreen mode

The worker replies directly to the caller:  

```
send(from, {:reply, request, "processed: #{request}"})
```

Enter fullscreen mode Exit fullscreen mode

The name identifies the service endpoint. The caller PID identifies where that particular reply must go.  

```
Client                                          :worker
  |                                                 |
  | {:work, client_pid, "hello"}                    |
  |------------------------------------------------>|
  |                                                 |
  | {:reply, "hello", "processed: hello"}          |
  |<------------------------------------------------|
```

Enter fullscreen mode Exit fullscreen mode

Run it with:  

```
elixir 03-avoiding-pid-sharing.exs
```

Enter fullscreen mode Exit fullscreen mode

Expected output:  

```
Worker available as: :worker
Response: processed: hello
```

Enter fullscreen mode Exit fullscreen mode

* * *

## [](#names-are-not-supervision)Names Are Not Supervision

It is tempting to think that a name solves the worker-restart problem. It does not.

When a registered process terminates, its registration is removed:  

```
:worker -> #PID<0.102.0>

worker exits

:worker -> no registered process
```

Enter fullscreen mode Exit fullscreen mode

A replacement worker still must be started and registered:  

```
supervisor starts new worker
         |
         v
new worker registers :worker
         |
         v
:worker -> #PID<0.105.0>
```

Enter fullscreen mode Exit fullscreen mode

Names address **discovery**. Supervisors address **lifecycle**. They are complementary.

In an OTP application, a common pattern is to start a supervised process with a name, often using `:via` and `Registry`. The supervisor creates the current process; the registry lets callers find it without depending on its old PID.

* * *

## [](#one-name-means-one-owner)One Name Means One Owner

A local registered name has one owner on its node. This is useful for a singleton service, but it also means the simple mechanism does not describe a worker pool.

For example, this is a single endpoint:  

```
:worker -> one PID
```

Enter fullscreen mode Exit fullscreen mode

It cannot represent three workers under the same local atom without another routing process or a richer registry design:  

```
:workers -> router process -> worker_1, worker_2, worker_3
```

Enter fullscreen mode Exit fullscreen mode

That distinction will matter when we build a worker pool later in the series.

* * *

## [](#correlating-replies)Correlating Replies

The client waits for:  

```
{:reply, ^request, response} -> response
```

Enter fullscreen mode Exit fullscreen mode

Pinning `request` ensures it accepts a reply with the request value it sent.

For this small demonstration, the string itself is adequate. In a client that might have several requests in flight with the same value, use a unique reference instead:  

```
ref = make_ref()
send(:worker, {:work, self(), ref, request})

receive do
  {:reply, ^ref, response} -> response
end
```

Enter fullscreen mode Exit fullscreen mode

This combines named lookup from this lesson with the correlated request-reply technique from Part 2.

* * *

## [](#limits-of-global-registration)Limits of Global Registration

`:global` makes node-wide lookup possible, but it does not remove the hard parts of distributed systems.

A system still needs to decide what happens when:

*   nodes cannot communicate because of a network partition
*   a process dies and needs replacement
*   two nodes attempt to claim the same service role
*   clients have already looked up a PID that then exits

There is no universally correct answer. The appropriate naming and discovery strategy depends on whether the service must be local, replicated, partition-tolerant, or strongly coordinated.

For the small examples in this repository, the central idea is simpler:

> Use a process name when callers should depend on a service role rather than on one temporary PID.

That small separation between identity and process incarnation is one of the building blocks of a resilient BEAM system.

* * *

Source code link: [https://github.com/pckrishnadas88/elixir-distributed-systems-lab/tree/main/06-named-processes](https://github.com/pckrishnadas88/elixir-distributed-systems-lab/tree/main/06-named-processes)

* * *

## [](#series)Series

1.  [Process Mailbox](https://dev.to/pckrishnadas88/building-a-stateful-process-in-elixir-without-genserver-58eb)
2.  [Correlated Request/Reply](https://dev.to/pckrishnadas88/building-distributed-systems-with-elixir-02-correlated-request-reply-4b2a)
3.  [Process Monitoring](https://dev.to/pckrishnadas88/building-distributed-systems-in-elixir-part-3-process-monitoring-5b5p)
4.  [Process Linking](https://dev.to/pckrishnadas88/building-distributed-systems-in-elixir-part-4-process-linking-okb)
5.  [Supervisor From Scratch](https://dev.to/pckrishnadas88/building-distributed-systems-in-elixir-part-5-supervisor-from-scratch-32mh)
6.  **Named Processes**

* * *

← Previous: [Part 5 — Supervisor From Scratch](https://dev.to/pckrishnadas88/building-distributed-systems-in-elixir-part-5-supervisor-from-scratch-32mh)

Next: Part 7 — Worker Pool _(coming soon)_ →

* * *

## [](#content-license)Content License

This article is licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). You may share and adapt it with attribution for non-commercial purposes. The accompanying source code remains licensed under the MIT License.
