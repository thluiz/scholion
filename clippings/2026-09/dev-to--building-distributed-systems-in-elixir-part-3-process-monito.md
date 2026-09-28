---
url: "https://dev.to/pckrishnadas88/building-distributed-systems-in-elixir-part-3-process-monitoring-5b5p"
captured_at: "2026-09-28T15:10:45+01:00"
title: "Building Distributed Systems in Elixir: Part 3 — Process Monitoring"
domain: "dev-to"
---

In the previous parts of this series, we built a stateful process using a mailbox and then added correlated request–reply using references.

Now we have another problem.

**What happens when the process we are communicating with dies?**

A worker might finish normally, crash because of an exception, or terminate for some other reason.

Instead of repeatedly checking whether a process is alive, the BEAM provides **process monitoring**.

In this part, we'll build process monitoring directly using:  

```
Process.monitor/1
```

Enter fullscreen mode Exit fullscreen mode

No `GenServer`.

No `Supervisor`.

The goal is to understand the primitive underneath OTP's failure-handling mechanisms.

* * *

## [](#the-problem)The Problem

Imagine we start a worker:  

```
worker = Worker.start("worker-1")
```

Enter fullscreen mode Exit fullscreen mode

That worker is an independent BEAM process.

At some point it could stop:  

```
send(worker, :stop)
```

Enter fullscreen mode Exit fullscreen mode

or crash:  

```
send(worker, :crash)
```

Enter fullscreen mode Exit fullscreen mode

Another process may need to know that the worker is gone.

One option would be repeatedly checking:  

```
Process.alive?(worker)
```

Enter fullscreen mode Exit fullscreen mode

But polling isn't what we want.

Instead, we can ask the BEAM to notify us when the process terminates.

* * *

## [](#monitoring-a-process)Monitoring a Process

Monitoring starts with one line:  

```
ref = Process.monitor(worker)
```

Enter fullscreen mode Exit fullscreen mode

The important detail is:

> The process calling `Process.monitor/1` becomes the monitoring process.

`Process.monitor/1` returns a unique reference.

If the worker later terminates, the BEAM sends the monitoring process a message:  

```
{:DOWN, ref, :process, worker, reason}
```

Enter fullscreen mode Exit fullscreen mode

This is just a message.

That means we can handle it using the same `receive` primitive we've already been using.

* * *

## [](#a-simple-worker)A Simple Worker

Let's create a worker that understands three messages:  

```
defmodule Worker do
  def start(name) do
    spawn(fn -> loop(name) end)
  end

  defp loop(name) do
    receive do
      {:work, from, value} ->
        IO.puts("#{name} received #{value}")
        send(from, {:done, name, value})
        loop(name)

      :stop ->
        IO.puts("#{name} stopping normally")
        :ok

      :crash ->
        raise "#{name} crashed"
    end
  end
end
```

Enter fullscreen mode Exit fullscreen mode

The process starts here:  

```
spawn(fn -> loop(name) end)
```

Enter fullscreen mode Exit fullscreen mode

The newly spawned process executes `loop/1` and waits at:  

```
receive do
```

Enter fullscreen mode Exit fullscreen mode

If it receives work:  

```
{:work, from, value}
```

Enter fullscreen mode Exit fullscreen mode

it handles the message and calls:  

```
loop(name)
```

Enter fullscreen mode Exit fullscreen mode

again.

That keeps the process alive.

But look at `:stop`:  

```
:stop ->
  IO.puts("#{name} stopping normally")
  :ok
```

Enter fullscreen mode Exit fullscreen mode

There is no call to `loop/1`.

The function finishes, so the process terminates normally.

* * *

## [](#detecting-a-normal-exit)Detecting a Normal Exit

Now let's monitor the worker:  

```
def normal_exit do
  worker = Worker.start("worker-1")

  ref = Process.monitor(worker)

  send(worker, :stop)

  receive do
    {:DOWN, ^ref, :process, ^worker, reason} ->
      IO.puts("worker-1 terminated")
      IO.puts("reason: #{inspect(reason)}")
  end
end
```

Enter fullscreen mode Exit fullscreen mode

The execution flow looks like this:  

```
Monitoring Process                 Worker Process

       |                                |
       | -------- spawn ------------->  |
       |                                |
       |                             receive
       |                             waiting
       |
       | Process.monitor(worker)
       |
       | -------- :stop ------------->  |
       |                                |
       |                         receives :stop
       |                                |
       |                          returns :ok
       |                                |
       |                           terminates
       |                                X
       |
       |      BEAM detects termination
       |
       | <---- {:DOWN, ..., :normal}
       |
    receive
       |
       v
 reason = :normal
```

Enter fullscreen mode Exit fullscreen mode

There are two separate messages here.

First:  

```
:stop
```

Enter fullscreen mode Exit fullscreen mode

is sent to the **worker's mailbox**.

Later:  

```
{:DOWN, ref, :process, worker, :normal}
```

Enter fullscreen mode Exit fullscreen mode

is sent by the BEAM to the **monitoring process's mailbox**.

This distinction is important.

* * *

## [](#understanding-the-raw-down-endraw-message)Understanding the `:DOWN` Message

The notification has this shape:  

```
{:DOWN, ref, :process, pid, reason}
```

Enter fullscreen mode Exit fullscreen mode

Let's break it down.

### [](#-raw-down-endraw-)`:DOWN`

Identifies the message as a monitor notification.

### [](#-raw-ref-endraw-)`ref`

The unique monitor reference returned by:  

```
Process.monitor(worker)
```

Enter fullscreen mode Exit fullscreen mode

### [](#-raw-process-endraw-)`:process`

Indicates that the monitored entity was a process.

### [](#-raw-pid-endraw-)`pid`

The PID of the process that terminated.

### [](#-raw-reason-endraw-)`reason`

Describes why the process terminated.

For a normal exit:  

```
:normal
```

Enter fullscreen mode Exit fullscreen mode

For a crash, it contains information about the failure.

* * *

## [](#why-use-raw-ref-endraw-)Why Use `^ref`?

Our receive pattern contains:  

```
{:DOWN, ^ref, :process, ^worker, reason}
```

Enter fullscreen mode Exit fullscreen mode

The pin operator `^` tells Elixir to match against an existing value.

We already have:  

```
ref = Process.monitor(worker)
```

Enter fullscreen mode Exit fullscreen mode

So:  

```
^ref
```

Enter fullscreen mode Exit fullscreen mode

means:

> Match the `:DOWN` message belonging to this particular monitor.

Likewise:  

```
^worker
```

Enter fullscreen mode Exit fullscreen mode

means:

> Match the PID of this particular worker.

This lets us precisely identify the termination notification we're waiting for.

* * *

## [](#detecting-a-crash)Detecting a Crash

Monitoring also works when a worker crashes.  

```
def crash_exit do
  worker = Worker.start("worker-2")

  ref = Process.monitor(worker)

  send(worker, :crash)

  receive do
    {:DOWN, ^ref, :process, ^worker, reason} ->
      IO.puts("worker-2 terminated")
      IO.puts("reason: #{inspect(reason)}")
  end
end
```

Enter fullscreen mode Exit fullscreen mode

The worker receives:  

```
:crash
```

Enter fullscreen mode Exit fullscreen mode

and executes:  

```
raise "#{name} crashed"
```

Enter fullscreen mode Exit fullscreen mode

The worker dies.

But the monitoring process does **not** die with it.

Instead, the BEAM sends it a `:DOWN` message containing the failure reason.

This gives us an important property:

> Monitoring lets one process observe another process's failure without automatically propagating that failure.

* * *

## [](#monitoring-multiple-workers)Monitoring Multiple Workers

Real systems usually have more than one worker.

Let's start three:  

```
worker1 = Worker.start("worker-1")
worker2 = Worker.start("worker-2")
worker3 = Worker.start("worker-3")
```

Enter fullscreen mode Exit fullscreen mode

Then monitor each one:  

```
ref1 = Process.monitor(worker1)
ref2 = Process.monitor(worker2)
ref3 = Process.monitor(worker3)
```

Enter fullscreen mode Exit fullscreen mode

Each monitor gets a different reference.

We can keep track of them using a map:  

```
%{
  ref1 => "worker-1",
  ref2 => "worker-2",
  ref3 => "worker-3"
}
```

Enter fullscreen mode Exit fullscreen mode

Think of this map as:  

```
workers whose termination we are still waiting for

ref1 -> worker-1
ref2 -> worker-2
ref3 -> worker-3
```

Enter fullscreen mode Exit fullscreen mode

Now send different termination messages:  

```
send(worker1, :stop)
send(worker2, :crash)
send(worker3, :stop)
```

Enter fullscreen mode Exit fullscreen mode

One worker crashes while the other two stop normally.

* * *

## [](#waiting-for-all-workers)Waiting for All Workers

We can write a small recursive function to collect the monitor notifications:  

```
defp wait_for_workers(monitors) when map_size(monitors) == 0 do
  IO.puts("all workers terminated")
end

defp wait_for_workers(monitors) do
  receive do
    {:DOWN, ref, :process, pid, reason} ->
      case Map.pop(monitors, ref) do
        {nil, monitors} ->
          wait_for_workers(monitors)

        {name, remaining} ->
          IO.puts("#{name} terminated")
          IO.puts("pid: #{inspect(pid)}")
          IO.puts("reason: #{inspect(reason)}")
          IO.puts("")

          wait_for_workers(remaining)
      end
  end
end
```

Enter fullscreen mode Exit fullscreen mode

The function has a simple purpose:

> Wait for each worker to terminate and log what happened.

Conceptually:  

```
3 workers
    |
    | worker terminates
    v
receive :DOWN
    |
    v
log termination
    |
    v
remove monitor
    |
    v
2 workers
    |
    | worker terminates
    v
receive :DOWN
    |
    v
1 worker
    |
    | worker terminates
    v
receive :DOWN
    |
    v
0 workers
    |
    v
finished
```

Enter fullscreen mode Exit fullscreen mode

The order is not guaranteed.

Even though we send:  

```
send(worker1, :stop)
send(worker2, :crash)
send(worker3, :stop)
```

Enter fullscreen mode Exit fullscreen mode

the workers execute concurrently.

Any of them may terminate first.

* * *

## [](#the-complete-example)The Complete Example

```
defmodule Worker do
  def start(name) do
    spawn(fn -> loop(name) end)
  end

  defp loop(name) do
    receive do
      {:work, from, value} ->
        IO.puts("#{name} received #{value}")
        send(from, {:done, name, value})
        loop(name)

      :stop ->
        IO.puts("#{name} stopping normally")
        :ok

      :crash ->
        raise "#{name} crashed"
    end
  end
end

defmodule MonitorDemo do
  def normal_exit do
    worker = Worker.start("worker-1")
    ref = Process.monitor(worker)

    send(worker, :stop)

    receive do
      {:DOWN, ^ref, :process, ^worker, reason} ->
        IO.puts("worker-1 terminated")
        IO.puts("reason: #{inspect(reason)}")
    end
  end

  def crash_exit do
    worker = Worker.start("worker-2")
    ref = Process.monitor(worker)

    send(worker, :crash)

    receive do
      {:DOWN, ^ref, :process, ^worker, reason} ->
        IO.puts("worker-2 terminated")
        IO.puts("reason: #{inspect(reason)}")
    end
  end

  def multiple_workers do
    worker1 = Worker.start("worker-1")
    worker2 = Worker.start("worker-2")
    worker3 = Worker.start("worker-3")

    ref1 = Process.monitor(worker1)
    ref2 = Process.monitor(worker2)
    ref3 = Process.monitor(worker3)

    send(worker1, :stop)
    send(worker2, :crash)
    send(worker3, :stop)

    wait_for_workers(%{
      ref1 => "worker-1",
      ref2 => "worker-2",
      ref3 => "worker-3"
    })
  end

  defp wait_for_workers(monitors) when map_size(monitors) == 0 do
    IO.puts("all workers terminated")
  end

  defp wait_for_workers(monitors) do
    receive do
      {:DOWN, ref, :process, pid, reason} ->
        case Map.pop(monitors, ref) do
          {nil, monitors} ->
            wait_for_workers(monitors)

          {name, remaining} ->
            IO.puts("#{name} terminated")
            IO.puts("pid: #{inspect(pid)}")
            IO.puts("reason: #{inspect(reason)}")
            IO.puts("")

            wait_for_workers(remaining)
        end
    end
  end
end

MonitorDemo.normal_exit()
MonitorDemo.crash_exit()
MonitorDemo.multiple_workers()
```

Enter fullscreen mode Exit fullscreen mode

Run it with:  

```
elixir monitor.exs
```

Enter fullscreen mode Exit fullscreen mode

* * *

## [](#monitor-vs-polling)Monitor vs Polling

We could ask:  

```
Process.alive?(worker)
```

Enter fullscreen mode Exit fullscreen mode

But that only tells us whether the process was alive at that particular moment.

The process could terminate immediately afterward.

With monitoring:  

```
Process.monitor(worker)
```

Enter fullscreen mode Exit fullscreen mode

we instead ask the BEAM to notify us about termination.  

```
monitor worker
      |
      v
worker runs independently
      |
      v
worker terminates
      |
      v
BEAM detects termination
      |
      v
{:DOWN, ...}
      |
      v
monitoring process
```

Enter fullscreen mode Exit fullscreen mode

This fits naturally with the BEAM's message-passing model.

* * *

## [](#what-we-built)What We Built

Without using `GenServer` or `Supervisor`, we now have:  

```
Process
   +
Mailbox
   +
Request / Reply
   +
Request References
   +
Process Monitoring
```

Enter fullscreen mode Exit fullscreen mode

We're gradually building the primitives needed for fault-tolerant process systems.

The important idea from this part is:

> **Failure detection itself can be represented as message passing.**

A worker terminates, and the monitoring process receives a message describing what happened.

* * *

## [](#whats-next)What's Next?

Monitoring lets us **observe** another process's failure.

But sometimes processes need a stronger relationship.

What if the failure of one process should affect another process?

That's where **process links** come in.

In Part 4, we'll explore:  

```
spawn_link/1
```

Enter fullscreen mode Exit fullscreen mode

and see how failures propagate between linked processes.

* * *

The examples intentionally use low-level process primitives first so we can understand what OTP abstractions are solving before using them.

Source code of the same can be found at: [https://github.com/pckrishnadas88/elixir-distributed-systems-lab](https://github.com/pckrishnadas88/elixir-distributed-systems-lab)

## [](#series)Series

1.  [Building a Stateful Process in Elixir Without GenServer](https://dev.to/pckrishnadas88/building-a-stateful-process-in-elixir-without-genserver-58eb)
2.  [Correlated Request/Reply](https://dev.to/pckrishnadas88/building-distributed-systems-with-elixir-02-correlated-request-reply-4b2a)
3.  **Process Monitoring**
4.  [Process Linking](https://dev.to/pckrishnadas88/building-distributed-systems-in-elixir-part-4-process-linking-okb)
5.  [Supervisor from scratch](https://dev.to/pckrishnadas88/building-distributed-systems-in-elixir-part-5-supervisor-from-scratch-32mh)

The examples intentionally use low-level process primitives first so we can understand what OTP abstractions are solving before using them.

* * *

← Previous: [Part 2 — Correlated Request/Reply](https://dev.to/pckrishnadas88/building-distributed-systems-with-elixir-02-correlated-request-reply-4b2a)

Next: [Part 4 — Process Linking](https://dev.to/pckrishnadas88/building-distributed-systems-in-elixir-part-4-process-linking-okb) →

* * *

## [](#content-license)Content License

This article is licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). You may share and adapt it with attribution for non-commercial purposes. The accompanying source code remains licensed under the MIT License.
