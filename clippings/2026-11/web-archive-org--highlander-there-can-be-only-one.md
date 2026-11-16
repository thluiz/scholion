---
url: "https://web.archive.org/web/20200808150316id_/https://moosecode.nl/blog/highlander_there_can_be_only_one"
captured_at: "2026-11-16T08:07:41+00:00"
title: "Highlander, there can be only one"
domain: "web-archive-org"
---

![Photo by Mick Haupt on Unsplash](https://web.archive.org/blog/highlander_there_can_be_only_one/highlander.jpg "Photo by Mick Haupt on Unsplash")

By: Derek Kraan / 2020-04-23

> How can I start a globally unique process in my Erlang cluster?

It is one of the questions I see the most often: how can I start a globally unique process in my Erlang cluster? A lot of people end up using Horde for this purpose, but Horde was not really meant for this use case, so the result ends up looking odd, like trying to shove a square into a round hole.

In this blog post, I will present a small, clean solution to this problem. We will use Erlang’s `:global` library, and about 50 lines of code to get this done. I have also released the code from this blog post as a library, [called Highlander](https://github.com/derekkraan/highlander).

## The goal

Ideally we would like to be able to take an existing supervision tree and modify it easily to make one or more processes globally unique.

```
children = [  child_1,  child_2,  child_3]Supervisor.init(children, strategy: :one_for_one)
```

To make `child_2` globally unique, it would be nice to be able to just do this:

```
children = [  child_1,  {Highlander, child_2},  child_3]Supervisor.init(children, strategy: :one_for_one)
```

Highlander should then use `child_2.id` to determine whether `child_2` is already running in the cluster, and if not, start `child_2`.

## Using `:global`

`:global` is a global process registry. It has two functions that we will be using here:

`:global.register_name(name, pid)` - register `pid` under `name`. Returns `:yes` or `:no`, indicating whether the registration was successful.

`:global.whereis_name(name)` - returns the pid registered to the name, or `:undefined`.

## Implementation

When we put `{Highlander, child_spec}` in the children list, `Supervisor` will call `Highlander.child_spec(child_spec)` in order to get the standard child spec that it needs in order to run it. This will be the only public function in Highlander:

```
defmodule Highlander do  def child_spec(child_child_spec) do    child_child_spec = Supervisor.child_spec(child_child_spec, [])%{      id: child_child_spec.id,      start: {GenServer, :start_link, [__MODULE__, child_child_spec, []]}    }  endend
```

This module converts `child_child_spec` into a regular child\_spec (if it is of the form `{Module, arg}`), so that we can access the `id` of it later, and then returns a child spec that will start Highlander with `GenServer.start_link(Highlander, child_child_spec, [])`.

The entrypoint of our process will be the `init` callback, so let’s define that:

```
  @impl true  def init(child_spec) do    Process.flag(:trap_exit, true)    {:ok, register(%{child_spec: child_spec})}  enddefp register(state) do    case :global.register_name(name(state), self()) do      :yes -> start(state)      :no -> monitor(state)    end  enddefp start(state) do    {:ok, pid} = Supervisor.start_link([state.child_spec], strategy: :one_for_one)    %{child_spec: state.child_spec, pid: pid}  enddefp monitor(state) do    case :global.whereis_name(name(state)) do      :undefined ->        register(state)pid ->        ref = Process.monitor(pid)        %{child_spec: state.child_spec, ref: ref}    end  enddefp name(%{child_spec: %{id: global_name}}) do    {__MODULE__, global_name}  end
```

This is the meat of the module. In `init/1`, we call `register(%{child_spec: child_spec})`, which eventually sets the state for our process. In `register/1`, we ask `:global` to register the name for us. If the name has not been registered, then it will register the name and return `:yes`, and otherwise it will return `:no`. If it returns `:yes`, then we know that this process is the only one in the cluster with the name defined by `child_spec.id`, and we can start the child.

If, it returns `:no`, then we know that there is already another process that has been registered with this name. If this happens, then we want to monitor this other process, so that we know when it goes down, and can try to register the name again.

In `monitor/1`, we ask `:global` where the process is that is defined by `child_spec.id`. If it returns a pid, then we monitor the pid. If it returns `:undefined`, then perhaps the other process has already died, and we should attempt to register the name again.

We also need to handle the case that the other process goes down:

```
  @impl true  def handle_info({:DOWN, ref, :process, _, _}, %{ref: ref} = state) do    {:noreply, register(state)}  end
```

This is a fairly simple call to `register/1`, to attempt to register the name again.

Finally, we cannot forget that Highlander is running in a supervision tree, and should be a well-behaved child process. If the supervision tree is shutting down, we should ask the child process to also shut down in a civilized way:

```
  @impl true  def terminate(reason, %{pid: pid}) do    Supervisor.stop(pid, reason)  enddef terminate(_, _), do: nil
```

If the child process stops for any reason, then Highlander will also stop, and will be restarted by the parent process as usual. There is no special handling necessary for this.

## Supervisor.child\_spec/1

Because Highlander accepts a child spec, it’s naturally possible to have it start _any_ process, even another supervisor. See the [documentation for Supervisor.child\_spec/1](https://hexdocs.pm/elixir/Supervisor.html#module-child_spec-1) for more information.

## Highlander library

Highlander could really be best described as a micro-library. It consists of [a single module](https://github.com/derekkraan/highlander/blob/master/lib/highlander.ex), and all the code fits comfortably on a single screen. I hope this blog post has helped explain how it works, and hopefully it has answered the question of how you can run a globally unique process in a cluster!
