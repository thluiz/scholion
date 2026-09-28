---
url: "https://dev.to/pckrishnadas88/building-distributed-systems-in-elixir-part-5-supervisor-from-scratch-32mh"
captured_at: "2026-09-28T15:11:39+01:00"
title: "Building Distributed Systems in Elixir: Part 5 — Supervisor From Scratch"
domain: "dev-to"
---

In the previous part of this series, we explored process links.

A linked worker that crashes sends an exit signal to the process linked to it. By default, that failure propagates and can terminate both processes.

We also saw that a process can trap exits:  

```
Process.flag(:trap_exit, true)
```

Enter fullscreen mode Exit fullscreen mode

Once exit trapping is enabled, an incoming exit signal becomes a mailbox message:  

```
{:EXIT, pid, reason}
```

Enter fullscreen mode Exit fullscreen mode

Receiving that message tells us that a linked process terminated, but detection is only the beginning.

What should happen next?

If the failed process was performing essential work, we may need to start a replacement.

In this part, we'll build a small supervisor from scratch using:  

```
spawn/1
spawn_link/1
Process.flag(:trap_exit, true)
send/2
receive/1
```

Enter fullscreen mode Exit fullscreen mode

Our supervisor will manage two workers. When one crashes, it will restart only that worker while leaving the healthy sibling unchanged.

No `GenServer`.

No OTP `Supervisor`.

The goal is not to replace OTP. The goal is to understand the mechanism and policy that an OTP supervisor provides.

* * *

## [](#the-problem)The Problem

Imagine a long-running worker process:  

```
worker =
  spawn(fn ->
    worker_loop()
  end)
```

Enter fullscreen mode Exit fullscreen mode

The worker receives jobs and keeps private state in its recursive loop.

If it crashes, the process disappears:  

```
Client                       Worker

  |                            |
  | {:work, value}             |
  |--------------------------->|
  |                            |
  |                         crash
  |                            X
  |
  | {:work, another_value}
  |---------------------------> no process
```

Enter fullscreen mode Exit fullscreen mode

Messages sent to a dead local PID do not bring that process back. The application needs another process responsible for detecting the failure and deciding whether to start a replacement.

We could periodically call:  

```
Process.alive?(worker)
```

Enter fullscreen mode Exit fullscreen mode

But polling has several problems:

*   failure detection is delayed until the next check
*   restart logic becomes scattered through the application
*   the code must repeatedly check every worker
*   a liveness check does not tell us why the worker stopped

The BEAM already gives us event-driven failure detection through links and exit signals.

We need a process that uses those primitives to apply a restart policy.

* * *

## [](#the-design)The Design

We will create one manual supervisor and two workers:  

```
                 +------------------------+
                 |   Manual Supervisor    |
                 |------------------------|
                 | trap_exit = true       |
                 | child PID -> name map  |
                 | restart loop           |
                 +------------------------+
                    /                  \
              link /                    \ link
                  v                      v
        +------------------+    +------------------+
        |     worker_1     |    |     worker_2     |
        |------------------|    |------------------|
        | receive loop     |    | receive loop     |
        | private state    |    | private state    |
        +------------------+    +------------------+
```

Enter fullscreen mode Exit fullscreen mode

The supervisor will:

1.  enable exit trapping
2.  start and link both workers
3.  record the relationship between each PID and logical worker name
4.  wait for messages
5.  restart a worker after an abnormal exit
6.  leave healthy siblings running
7.  avoid restarting a worker after a normal exit

This is a minimal **one-for-one restart strategy**.

* * *

## [](#the-worker)The Worker

Our worker starts with a logical name and a processed-job count:  

```
defmodule Worker do
  def start(name) do
    spawn_link(fn -> loop(name, 0) end)
  end
end
```

Enter fullscreen mode Exit fullscreen mode

The call to `spawn_link/1` does two things atomically:  

```
start process + create link
```

Enter fullscreen mode Exit fullscreen mode

The link connects the worker's failure lifecycle to the process that starts it. In this example, that process is our manual supervisor.

The worker then enters a receive loop:  

```
defp loop(name, count) do
  receive do
    {:work, caller, value} ->
      new_count = count + 1
      send(caller, {:done, name, value, new_count})
      loop(name, new_count)

    :crash ->
      raise "#{name} crashed"

    :stop ->
      IO.puts("#{name} stopping normally")
      :ok
  end
end
```

Enter fullscreen mode Exit fullscreen mode

The worker supports three messages.

### [](#processing-work)Processing Work

```
{:work, caller, value}
```

Enter fullscreen mode Exit fullscreen mode

For each job, the worker increments its private counter and replies:  

```
{:done, name, value, new_count}
```

Enter fullscreen mode Exit fullscreen mode

The recursive call carries the new state into the next loop:  

```
loop(name, new_count)
```

Enter fullscreen mode Exit fullscreen mode

### [](#crashing-intentionally)Crashing Intentionally

```
:crash
```

Enter fullscreen mode Exit fullscreen mode

This branch raises an exception:  

```
raise "#{name} crashed"
```

Enter fullscreen mode Exit fullscreen mode

The exception terminates the worker with an abnormal exit reason. Because the worker is linked to the supervisor, an exit signal travels across that link.

### [](#stopping-normally)Stopping Normally

```
:stop
```

Enter fullscreen mode Exit fullscreen mode

Returning `:ok` lets the worker function finish normally. The worker exits with reason:  

```
:normal
```

Enter fullscreen mode Exit fullscreen mode

That distinction will determine whether our supervisor restarts it.

* * *

## [](#starting-the-manual-supervisor)Starting the Manual Supervisor

The public `start/1` function creates the supervisor process:  

```
defmodule ManualSupervisor do
  def start(worker_names) do
    spawn(fn -> init(worker_names) end)
  end
end
```

Enter fullscreen mode Exit fullscreen mode

We use `spawn/1`, rather than `spawn_link/1`, here because this example focuses on links between the supervisor and its children. The caller running the demonstration is not part of that supervision relationship.

The new supervisor begins in `init/1`:  

```
defp init(worker_names) do
  Process.flag(:trap_exit, true)

  children =
    Map.new(worker_names, fn name ->
      pid = start_child(name)
      {pid, name}
    end)

  loop(children)
end
```

Enter fullscreen mode Exit fullscreen mode

The order here matters.

The supervisor enables exit trapping **before** it starts linked children:  

```
Process.flag(:trap_exit, true)
```

Enter fullscreen mode Exit fullscreen mode

If a child crashes immediately after it starts, the supervisor is already prepared to receive the exit as a message instead of being terminated by it.

* * *

## [](#tracking-child-identity)Tracking Child Identity

A restarted process receives a new PID.

That means a PID cannot be the permanent identity of a logical worker:  

```
worker_1 before crash -> #PID<0.102.0>
worker_1 after crash  -> #PID<0.104.0>
```

Enter fullscreen mode Exit fullscreen mode

The name remains `:worker_1`, but the process incarnation changes.

Our supervisor stores its children in a map:  

```
%{
  worker_1_pid => :worker_1,
  worker_2_pid => :worker_2
}
```

Enter fullscreen mode Exit fullscreen mode

The PID is the key because the exit message identifies the terminated process by PID:  

```
{:EXIT, pid, reason}
```

Enter fullscreen mode Exit fullscreen mode

With the map, the supervisor can recover the logical name:  

```
name = Map.fetch!(children, pid)
```

Enter fullscreen mode Exit fullscreen mode

It can then start a replacement using that name.

* * *

## [](#starting-children)Starting Children

Child creation is kept in one helper:  

```
defp start_child(name) do
  pid = Worker.start(name)
  IO.puts("supervisor: started #{name} as #{inspect(pid)}")
  pid
end
```

Enter fullscreen mode Exit fullscreen mode

`Worker.start/1` uses `spawn_link/1`, so the calling supervisor becomes linked to the new worker.

After initialization, the relationship looks like this:  

```
ManualSupervisor
    |
    +---- link ---- worker_1
    |
    +---- link ---- worker_2
```

Enter fullscreen mode Exit fullscreen mode

The supervisor then carries the child map into its recursive message loop:  

```
loop(children)
```

Enter fullscreen mode Exit fullscreen mode

* * *

## [](#detecting-an-abnormal-exit)Detecting an Abnormal Exit

Suppose the demonstration sends this message:  

```
send(worker_1, :crash)
```

Enter fullscreen mode Exit fullscreen mode

The worker raises an exception and terminates.

Because the supervisor traps exits, it receives:  

```
{:EXIT, worker_1_pid, reason}
```

Enter fullscreen mode Exit fullscreen mode

The abnormal-exit branch handles that message:  

```
{:EXIT, pid, reason} ->
  name = Map.fetch!(children, pid)
  IO.puts("supervisor: #{name} exited with #{inspect(reason)}")

  children = Map.delete(children, pid)
  new_pid = start_child(name)
  IO.puts("supervisor: restarted #{name} as #{inspect(new_pid)}")

  loop(Map.put(children, new_pid, name))
```

Enter fullscreen mode Exit fullscreen mode

There are four important steps here.

### [](#1-identify-the-logical-worker)1\. Identify the Logical Worker

```
name = Map.fetch!(children, pid)
```

Enter fullscreen mode Exit fullscreen mode

The exit message contains the old PID. The child map tells us that this PID belonged to `:worker_1`.

### [](#2-remove-the-dead-pid)2\. Remove the Dead PID

```
children = Map.delete(children, pid)
```

Enter fullscreen mode Exit fullscreen mode

The old PID will never become alive again, so it must not remain in the supervisor's state.

### [](#3-start-a-replacement)3\. Start a Replacement

```
new_pid = start_child(name)
```

Enter fullscreen mode Exit fullscreen mode

This creates another linked process with the same logical name and a new PID.

### [](#4-store-the-replacement)4\. Store the Replacement

```
loop(Map.put(children, new_pid, name))
```

Enter fullscreen mode Exit fullscreen mode

The recursive loop continues with the updated child map.

* * *

## [](#the-restart-message-flow)The Restart Message Flow

The complete interaction looks like this:  

```
Demo                  Supervisor                 worker_1

send(worker_1, :crash)
----------------------------------------------->

                                               raises
                                               exits

                      {:EXIT, pid, reason}
                      <-------------------------- BEAM

                      find name for old PID
                      remove old PID
                      spawn_link replacement

children(supervisor)
--------------------->

{:children, ref,
 %{worker_1: new_pid,
   worker_2: same_pid}}
<---------------------
```

Enter fullscreen mode Exit fullscreen mode

The important result is:  

```
worker_1 crashes -> worker_1 is replaced
worker_2 survives -> worker_2 keeps the same PID
```

Enter fullscreen mode Exit fullscreen mode

That is the meaning of one-for-one supervision in this small example.

* * *

## [](#healthy-siblings-stay-alive)Healthy Siblings Stay Alive

When `worker_1` crashes, the supervisor does not rebuild its entire child set.

It removes and replaces only the matching PID:  

```
children = Map.delete(children, worker_1_pid)
children = Map.put(children, new_worker_1_pid, :worker_1)
```

Enter fullscreen mode Exit fullscreen mode

The `worker_2` entry is untouched.  

```
Before

worker_1 -> #PID<0.102.0>
worker_2 -> #PID<0.103.0>

After worker_1 crashes

worker_1 -> #PID<0.104.0>  changed
worker_2 -> #PID<0.103.0>  unchanged
```

Enter fullscreen mode Exit fullscreen mode

This matters because a healthy worker may contain useful in-memory state. Restarting it unnecessarily would discard that state and interrupt work it could have continued performing.

OTP also provides other restart strategies for cases where child lifecycles are related, but our implementation supports only one-for-one replacement.

* * *

## [](#normal-exit-is-not-a-failure)Normal Exit Is Not a Failure

Our supervisor has a separate pattern for a normal exit:  

```
{:EXIT, pid, :normal} ->
  name = Map.fetch!(children, pid)
  IO.puts("supervisor: #{name} stopped normally; not restarting")
  loop(Map.delete(children, pid))
```

Enter fullscreen mode Exit fullscreen mode

When a worker receives `:stop`, it finishes normally:  

```
:stop ->
  IO.puts("#{name} stopping normally")
  :ok
```

Enter fullscreen mode Exit fullscreen mode

The supervisor removes that child but does not replace it.

This gives our restart policy a simple rule:  

```
reason == :normal -> do not restart
reason != :normal -> restart
```

Enter fullscreen mode Exit fullscreen mode

This is closest to OTP's `:transient` restart policy, which restarts a child only after an abnormal exit. It is still deliberately simplified. OTP child specifications provide explicit `:permanent`, `:transient`, and `:temporary` policies instead of forcing every application to encode the decision directly in a receive loop.

* * *

## [](#asking-the-supervisor-for-its-children)Asking the Supervisor for Its Children

The demonstration needs a safe way to discover current child PIDs, including a replacement PID after a crash.

The public function uses a correlated request-reply protocol:  

```
def children(supervisor) do
  ref = make_ref()
  send(supervisor, {:children, self(), ref})

  receive do
    {:children, ^ref, children} -> children
  after
    1_000 -> {:error, :timeout}
  end
end
```

Enter fullscreen mode Exit fullscreen mode

This reuses an idea from Part 2.

The request includes:  

```
{:children, caller_pid, reference}
```

Enter fullscreen mode Exit fullscreen mode

The supervisor transforms its internal PID-to-name map into a caller-friendly name-to-PID map:  

```
{:children, caller, ref} ->
  by_name = Map.new(children, fn {pid, name} -> {name, pid} end)
  send(caller, {:children, ref, by_name})
  loop(children)
```

Enter fullscreen mode Exit fullscreen mode

The reply is:  

```
{:children, reference, %{
  worker_1: worker_1_pid,
  worker_2: worker_2_pid
}}
```

Enter fullscreen mode Exit fullscreen mode

The pinned reference ensures that the caller accepts only the response belonging to its request:  

```
{:children, ^ref, children}
```

Enter fullscreen mode Exit fullscreen mode

Our supervisor is already combining several earlier primitives:  

```
mailbox loop
    +
request/reply correlation
    +
process links
    +
trapped exits
    +
restart policy
```

Enter fullscreen mode Exit fullscreen mode

* * *

## [](#replacement-means-fresh-state)Replacement Means Fresh State

Each worker begins with a count of zero:  

```
spawn_link(fn -> loop(name, 0) end)
```

Enter fullscreen mode Exit fullscreen mode

Suppose `worker_1` processes three jobs and then crashes:  

```
old worker_1 count = 3
```

Enter fullscreen mode Exit fullscreen mode

The replacement is a completely new process:  

```
new worker_1 count = 0
```

Enter fullscreen mode Exit fullscreen mode

Supervision restores the **process**, not its private memory.

That distinction is fundamental:

> Restarting a worker restores availability only if the worker can begin again from valid initial state or reconstruct its state from somewhere durable.

Real applications may rebuild state from a database, an event log, another process, a cache, or the arguments in a child specification.

Our worker intentionally starts from zero so that this behavior is visible. After restart, its first completed job replies with a count of `1`:  

```
{:done, :worker_1, :job_after_restart, 1}
```

Enter fullscreen mode Exit fullscreen mode

* * *

## [](#stopping-the-supervisor)Stopping the Supervisor

The supervisor also handles its own `:stop` message:  

```
:stop ->
  Enum.each(Map.keys(children), &send(&1, :stop))
  wait_for_children(Map.keys(children))
```

Enter fullscreen mode Exit fullscreen mode

It asks each current child to stop normally, then waits for all corresponding exit messages:  

```
defp wait_for_children([]), do: :ok

defp wait_for_children(children) do
  receive do
    {:EXIT, pid, _reason} ->
      wait_for_children(List.delete(children, pid))
  end
end
```

Enter fullscreen mode Exit fullscreen mode

Because exit trapping remains enabled, normal child exits arrive as `:EXIT` messages. Waiting for them ensures that the supervisor does not finish before its children have processed the shutdown request.

This is only a minimal shutdown protocol. It has no timeout and cannot force a child that ignores `:stop` to terminate.

OTP supervisors implement more complete shutdown behavior.

* * *

## [](#the-complete-example)The Complete Example

```
defmodule Worker do
  def start(name) do
    spawn_link(fn -> loop(name, 0) end)
  end

  defp loop(name, count) do
    receive do
      {:work, caller, value} ->
        new_count = count + 1
        send(caller, {:done, name, value, new_count})
        loop(name, new_count)

      :crash ->
        raise "#{name} crashed"

      :stop ->
        IO.puts("#{name} stopping normally")
        :ok
    end
  end
end

defmodule ManualSupervisor do
  def start(worker_names) do
    spawn(fn -> init(worker_names) end)
  end

  def children(supervisor) do
    ref = make_ref()
    send(supervisor, {:children, self(), ref})

    receive do
      {:children, ^ref, children} -> children
    after
      1_000 -> {:error, :timeout}
    end
  end

  defp init(worker_names) do
    Process.flag(:trap_exit, true)

    children =
      Map.new(worker_names, fn name ->
        pid = start_child(name)
        {pid, name}
      end)

    loop(children)
  end

  defp loop(children) do
    receive do
      {:EXIT, pid, :normal} ->
        name = Map.fetch!(children, pid)
        IO.puts("supervisor: #{name} stopped normally; not restarting")
        loop(Map.delete(children, pid))

      {:EXIT, pid, reason} ->
        name = Map.fetch!(children, pid)
        IO.puts("supervisor: #{name} exited with #{inspect(reason)}")

        children = Map.delete(children, pid)
        new_pid = start_child(name)
        IO.puts("supervisor: restarted #{name} as #{inspect(new_pid)}")

        loop(Map.put(children, new_pid, name))

      {:children, caller, ref} ->
        by_name = Map.new(children, fn {pid, name} -> {name, pid} end)
        send(caller, {:children, ref, by_name})
        loop(children)

      :stop ->
        Enum.each(Map.keys(children), &send(&1, :stop))
        wait_for_children(Map.keys(children))
    end
  end

  defp start_child(name) do
    pid = Worker.start(name)
    IO.puts("supervisor: started #{name} as #{inspect(pid)}")
    pid
  end

  defp wait_for_children([]), do: :ok

  defp wait_for_children(children) do
    receive do
      {:EXIT, pid, _reason} ->
        wait_for_children(List.delete(children, pid))
    end
  end
end

defmodule SupervisorDemo do
  def run do
    supervisor = ManualSupervisor.start([:worker_1, :worker_2])
    children_before = ManualSupervisor.children(supervisor)

    worker_1_before = children_before.worker_1
    worker_2_before = children_before.worker_2

    send(worker_1_before, :crash)

    children_after =
      wait_for_restart(supervisor, :worker_1, worker_1_before)

    IO.puts(
      "worker_1 restarted: #{children_after.worker_1 != worker_1_before}"
    )

    IO.puts(
      "worker_2 unchanged: #{children_after.worker_2 == worker_2_before}"
    )

    send(
      children_after.worker_1,
      {:work, self(), :job_after_restart}
    )

    receive do
      message -> IO.inspect(message, label: "reply")
    after
      1_000 -> IO.puts("reply timed out")
    end

    send(supervisor, :stop)
  end

  defp wait_for_restart(supervisor, name, old_pid, attempts \\ 50)

  defp wait_for_restart(_supervisor, _name, _old_pid, 0) do
    raise "worker was not restarted"
  end

  defp wait_for_restart(supervisor, name, old_pid, attempts) do
    children = ManualSupervisor.children(supervisor)

    case Map.get(children, name) do
      pid when is_pid(pid) and pid != old_pid ->
        children

      _ ->
        Process.sleep(10)
        wait_for_restart(supervisor, name, old_pid, attempts - 1)
    end
  end
end

SupervisorDemo.run()
```

Enter fullscreen mode Exit fullscreen mode

* * *

## [](#running-the-example)Running the Example

From the `05-supervisor-from-scratch` directory, run:  

```
elixir supervisor.exs
```

Enter fullscreen mode Exit fullscreen mode

Example output:  

```
supervisor: started worker_1 as #PID<0.102.0>
supervisor: started worker_2 as #PID<0.103.0>

10:30:00.000 [error] Process #PID<0.102.0> raised an exception
** (RuntimeError) worker_1 crashed

supervisor: worker_1 exited with {%RuntimeError{message: "worker_1 crashed"}, ...}
supervisor: started worker_1 as #PID<0.104.0>
supervisor: restarted worker_1 as #PID<0.104.0>
worker_1 restarted: true
worker_2 unchanged: true
reply: {:done, :worker_1, :job_after_restart, 1}
worker_1 stopping normally
worker_2 stopping normally
```

Enter fullscreen mode Exit fullscreen mode

The exact PIDs, timestamps, stack trace, and output order may vary because the processes execute concurrently.

The exception report is expected. We deliberately crash `worker_1` to exercise the restart path.

The important observations are:  

```
worker_1 has a new PID
worker_2 has its original PID
replacement worker_1 accepts work
replacement worker_1 begins with fresh state
```

Enter fullscreen mode Exit fullscreen mode

* * *

## [](#why-the-demo-polls-for-the-new-pid)Why the Demo Polls for the New PID

After sending `:crash`, the caller cannot assume that the supervisor has already processed the resulting exit signal.

These operations are concurrent:  

```
caller sends :crash
worker receives :crash
worker exits
supervisor receives :EXIT
supervisor starts replacement
```

Enter fullscreen mode Exit fullscreen mode

The caller therefore asks for the children repeatedly until `worker_1` has a different PID:  

```
case Map.get(children, name) do
  pid when is_pid(pid) and pid != old_pid ->
    children

  _ ->
    Process.sleep(10)
    wait_for_restart(supervisor, name, old_pid, attempts - 1)
end
```

Enter fullscreen mode Exit fullscreen mode

This polling exists only in the demonstration code so it can verify the asynchronous restart. The supervisor itself does not poll for failures; it reacts to linked exit messages.

* * *

## [](#what-makes-this-a-supervisor)What Makes This a Supervisor?

Our process performs the smallest useful form of supervision:  

```
start children
      |
link to children
      |
observe exits
      |
apply restart policy
      |
start replacements
```

Enter fullscreen mode Exit fullscreen mode

The mechanism comes from BEAM primitives:

*   links connect process lifecycles
*   exit trapping converts exit signals into messages
*   the mailbox delivers failure information
*   recursion preserves the current child set

The policy comes from our own code:

*   normal exits are not restarted
*   abnormal exits are restarted
*   only the failed child is restarted
*   replacements begin with the same logical name

OTP's `Supervisor` separates and formalizes these responsibilities through child specifications and restart strategies.

* * *

## [](#the-restart-loop-is-not-enough)The Restart Loop Is Not Enough

It is tempting to look at this example and conclude that supervision is simply:  

```
receive do
  {:EXIT, pid, reason} ->
    start_replacement(pid)
end
```

Enter fullscreen mode Exit fullscreen mode

But production supervision must answer many more questions.

### [](#what-if-a-worker-crashes-forever)What If a Worker Crashes Forever?

Our supervisor restarts every abnormal exit without a limit:  

```
start -> crash -> restart -> crash -> restart -> crash -> ...
```

Enter fullscreen mode Exit fullscreen mode

That loop can consume CPU, flood logs, and hide a persistent configuration or programming error.

A real supervisor needs restart intensity limits, such as a maximum number of restarts within a time window.

### [](#what-if-children-depend-on-each-other)What If Children Depend on Each Other?

One-for-one is not always correct.

If a producer and consumer share a protocol state, restarting only one could leave them inconsistent. Other strategies may restart multiple children together or restart children in a defined order.

### [](#what-if-shutdown-hangs)What If Shutdown Hangs?

Our supervisor waits forever if a worker ignores `:stop`:  

```
wait_for_children(children)
```

Enter fullscreen mode Exit fullscreen mode

Production shutdown needs timeouts and a way to force termination after the grace period expires.

### [](#what-if-child-startup-fails)What If Child Startup Fails?

Our `start_child/1` assumes that starting a worker succeeds immediately.

Real child startup may need to validate configuration, open resources, or return an error. The supervisor must handle partial initialization and report why startup failed.

### [](#in-what-order-should-processes-start-and-stop)In What Order Should Processes Start and Stop?

Applications often require dependencies to start before their consumers and stop after them. A plain map does not represent that ordering.

### [](#how-should-children-be-configured)How Should Children Be Configured?

Our child configuration is only a list of names:  

```
[:worker_1, :worker_2]
```

Enter fullscreen mode Exit fullscreen mode

Real supervision needs structured information about how to start, restart, identify, and shut down each child.

These requirements are why OTP supervisors exist.

* * *

## [](#why-use-otp-supervisor-in-real-applications)Why Use OTP Supervisor in Real Applications?

Our manual supervisor is a learning exercise. It makes the underlying process model visible, but it is not production-ready.

OTP's `Supervisor` provides tested implementations of concerns including:

*   child specifications
*   one-for-one and other restart strategies
*   restart intensity and period limits
*   deterministic startup and shutdown behavior
*   configurable shutdown timeouts
*   supervisor initialization guarantees
*   child introspection
*   structured error reporting
*   supervision trees

The value of OTP is not that these behaviors are impossible to write ourselves.

The value is that failure handling contains subtle edge cases, and OTP provides a standard implementation that has been exercised across decades of BEAM systems.

Understanding the raw primitives helps us use that abstraction deliberately.

* * *

## [](#limitations-of-our-implementation)Limitations of Our Implementation

Our manual supervisor intentionally leaves out many production requirements:

*   a repeatedly crashing worker is restarted forever
*   there is no restart delay or exponential backoff
*   there is no restart-frequency limit
*   only one-for-one replacement is supported
*   restarted workers lose all private in-memory state
*   child startup cannot return a structured error
*   shutdown has no timeout
*   an unresponsive child can block supervisor shutdown forever
*   there is no nested supervision tree
*   the child registry is a private map
*   unknown linked exit messages would crash `Map.fetch!/2`
*   the supervisor is not linked to the process that starts it

These are not reasons to keep expanding the custom implementation until it becomes a second supervisor library.

They are evidence for using OTP's existing one.

* * *

## [](#what-we-built)What We Built

Without using `GenServer` or OTP `Supervisor`, we now have:  

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
   +
Process Linking
   +
Trapped Exits
   +
Child Tracking
   +
One-for-One Restart
```

Enter fullscreen mode Exit fullscreen mode

The central idea from this part is:

> **A supervisor combines failure detection with a restart policy.**

Links and trapped exits tell the supervisor that a child terminated.

The supervisor's policy decides whether to restart it, which process to replace, and what happens to the remaining children.

Our one-for-one policy replaces only the failed worker and preserves its healthy sibling.

* * *

## [](#whats-next)What's Next?

Our caller currently discovers workers by asking the supervisor for its private child map.

That works inside this small example, but passing and refreshing PIDs becomes awkward as a system grows.

In Part 6, we'll explore **named processes** and process registration:  

```
logical name
     |
     v
current process PID
```

Enter fullscreen mode Exit fullscreen mode

This will let processes find one another through stable names instead of sharing raw PIDs everywhere.

* * *

Source code link: [https://github.com/pckrishnadas88/elixir-distributed-systems-lab/tree/main/05-supervisor-from-scratch](https://github.com/pckrishnadas88/elixir-distributed-systems-lab/tree/main/05-supervisor-from-scratch)

* * *

## [](#series)Series

1.  [Process Mailbox](https://dev.to/pckrishnadas88/building-a-stateful-process-in-elixir-without-genserver-58eb)
2.  [Correlated Request/Reply](https://dev.to/pckrishnadas88/building-distributed-systems-with-elixir-02-correlated-request-reply-4b2a)
3.  [Process Monitoring](https://dev.to/pckrishnadas88/building-distributed-systems-in-elixir-part-3-process-monitoring-5b5p)
4.  [Process Linking](https://dev.to/pckrishnadas88/building-distributed-systems-in-elixir-part-4-process-linking-okb)
5.  **Supervisor From Scratch**
6.  [Named processes](https://dev.to/pckrishnadas88/building-distributed-systems-in-elixir-part-6-named-processes-l3)

* * *

← Previous: [Part 4 — Process Linking](https://dev.to/pckrishnadas88/building-distributed-systems-in-elixir-part-4-process-linking-okb)

Next: [Part 6 - Named processes](https://dev.to/pckrishnadas88/building-distributed-systems-in-elixir-part-6-named-processes-l3) →

## [](#content-license)Content License

This article is licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). You may share and adapt it with attribution for non-commercial purposes. The accompanying source code remains licensed under the MIT License.
