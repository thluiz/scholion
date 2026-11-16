---
url: "https://dashbit.co/blog/homemade-analytics-with-ecto-and-elixir"
captured_at: "2026-11-16T04:40:33+00:00"
title: "Homemade analytics with Ecto and Elixir"
domain: "dashbit-co"
---

*   José Valim
*   July 16th, 2020
*   [ecto](https://dashbit.co/blog/tags/ecto) , [processes](https://dashbit.co/blog/tags/processes) , [elixir](https://dashbit.co/blog/tags/elixir)

For the Dashbit website, we wanted to avoid tracking users as much as possible. This means no cookies and unfortunately most analytics use cookies for tracking and/or fingerprinting. However, we still want to see which pages on our website are being frequently accessed. For this purpose, we have decided to roll our own analytics system.

In this article, we will cover how we implemented the analytics system with Ecto upserts and how we have used the Elixir registry and Elixir processes to reduce the pressure on the database.

## Tracking with upserts

The idea is very simple: every time someone accesses a page, we will store this information in the database. However, we don’t need to track each access at the instant they happen. For us, tracking how many accesses a page had in a day is completely fine. Therefore, every time a page is accessed on a given date, we will attempt to insert an entry in the database. If an entry already exists, we update its counter instead.

Luckily, this can be done with an upsert in Ecto. Let’s first define the schema for the database resource:

```
defmodule MyApp.Metrics.Metric do
  use Ecto.Schema

  @primary_key false
  schema "metrics" do
    field :date, :date, primary_key: true
    field :path, :string, primary_key: true
    field :counter, :integer, default: 0
  end
end
```

It has three fields: a date, the page path, and the counter (number of accesses). The date and path make a composite primary key. Our migration looks like this:

```
defmodule Dashbit.Repo.Migrations.CreateMetrics do
  use Ecto.Migration

  def change do
    create table(:metrics, primary_key: false) do
      add :date, :date, primary_key: true
      add :path, :string, primary_key: true
      add :counter, :integer, default: 0
    end
  end
end
```

Now we execute the following command whenever we want to count one page access:

```
defp upsert!(path, counter) do
  import Ecto.Query
  date = Date.utc_today()
  query = from(m in Dashbit.Metrics.Metric, update: [inc: [counter: ^counter]])

  Dashbit.Repo.insert!(
    %Dashbit.Metrics.Metric{date: date, path: path, counter: counter},
    on_conflict: query,
    conflict_target: [:date, :path]
  )
end
```

The code above performs an upsert, incrementing the number of accesses in a page by the value of `counter`, which is typically 1. If an entry does not exist, one is immediately created.

This is the core of our analytics. It is a very straight-forward solution, but it does have a strong requirement on the database accepting all of our writes. While most applications heavily rely on a database, the analytics system is the only place in our website that uses a database, so we believe it is important to show an article, such as this blog post, even if there is an error when talking to the storage layer. To address this, we have decided to move the upserts to separate processes.

## Async and batched writes with processes

As laid out in the previous section, we want to move all the database writes done by our analytics code to a separate process. Another concern we have with our solution so far is how it will handle overloads. If there is a huge spike in traffic, could we end up putting too much pressure in the database? In this sense, would it be a good idea to batch our writes?

To be honest, our application will be just fine with spikes. Most of our page loads are within hundreds of microseconds, thanks to Phoenix, and our database usage is minimal. On the other hand, such a small project is a perfect opportunity to experiment, so we decided to explore how our analytics solution would look like if we performed writes asynchronously and in batches.

Here is what we came up with. Every time a user accesses a page, we will spawn an Elixir process that tracks all accesses to that page. If a process already exists for said page, we will message the existing process instead. The goal of this process is to collect all accesses within a time interval, writing to the database after X seconds.

We are going to call this the `Worker` process and it starts like this:

```
defmodule Dashbit.Metrics.Worker do
  use GenServer, restart: :temporary
```

We define a module for the process and declare it as a [`GenServer`](https://hexdocs.pm/elixir/GenServer.html). We also say that this process is `:temporary`. I.e. if it dies, we don’t want the supervisor to restart it. That’s because we are assuming that, if the process dies, our logic that dynamically spawns processes for each page will eventually start a new one anyway.

Next we define the `init` callback of the process:

```
  @impl true
  def init(path) do
    Process.flag(:trap_exit, true)
    {:ok, {path, _counter = 0}}
  end
```

The `init` callback traps exits and sets the process state to `{path, 0}`. The first element is the page path, the second element is the number of page visits.

Our process should be able to receive a `:bump` message. This message is sent whenever we need to bump the counter and is handled by the `handle_info` callback:

```
  @impl true
  def handle_info(:bump, {path, 0}) do
    schedule_upsert()
    {:noreply, {path, 1}}
  end

  @impl true
  def handle_info(:bump, {path, counter}) do
    {:noreply, {path, counter + 1}}
  end
```

If we receive the `:bump` when the page had no access (i.e. counter is zero), we will bump the counter to 1 and we will also schedule an upsert event, so we eventually write those accesses to the database. If the counter is more than 0, we simply bump it and return an updated state.

The scheduling and upsert code will look like this:

```
  defp schedule_upsert() do
    Process.send_after(self(), :upsert, Enum.random(10..20) * 1_000)
  end

  @impl true
  def handle_info(:upsert, {path, counter}) do
    upsert!(path, counter)
    {:noreply, {path, 0}}
  end

  defp upsert!(path, counter) do
    # same function as the previous section
  end
```

The `schedule_upsert()` function schedules a message to the current process (`self()`). The message will be named `:upsert` and it will be delivered in a random value between 10s to 20s. The reason we picked a random value is to avoid a scenario where multiple processes for different pages are spawned at the same time and they all write to the database at the same time.

Next we define another `handle_info` clause, this time to handle the scheduled `:upsert` message. This clause simply invokes the `upsert!` function, defined in the previous section, and resets the state back to `{path, 0}`. This makes it so that, once there is a new bump, we will schedule a new upsert.

Finally, we implement the `terminate` callback, which will be invoked whenever our application is shutting down:

```
  @impl true
  def terminate(_, {_path, 0}), do: :ok
  def terminate(_, {path, counter}), do: upsert!(path, counter)
end
```

If our application is shutting down, we may have pending writes in our worker, so we want to send them to the database as part of our termination logic. One important thing to remember is that the `terminate` callback is not called by default when shutting down, unless you are trapping exits. That’s why we called `Process.flag(:trap_exit, true)` in the `init` function.

The process we just implemented delivers all of the requirements we have so far: writes are now asynchronous, as they happen in a separate process, and they are also batched, using intervals between 10s and 20s. The last step we need to implement is to actually spawn those processes on the fly as users navigate through the website.

## Dynamic processes with the Elixir registry

In order to spawn and find processes for each page, we are going to use [Elixir’s `Registry`](https://hexdocs.pm/elixir/Registry.html). We also need a dynamic supervisor which is going to be the parent of all worker processes. Let’s implement this logic in the overaching `Metrics` module, alongside our `bump(page)` function.

Let’s get started with the basics:

```
defmodule Dashbit.Metrics do
  use Supervisor

  @worker Dashbit.Metrics.Worker
  @registry Dashbit.Metrics.Registry
  @supervisor Dashbit.Metrics.WorkerSupervisor
```

Our `Dashbit.Metrics` module is a [`Supervisor`](https://hexdocs.pm/elixir/Supervisor.html), which will have two children: the registry and the supervisor of all workers. Since the workers are started dynamically, as requests come, we will use a `DynamicSupervisor`. We store the names of the worker, registry and dynamic supervisor processes in module attributes for convenience.

Next we will define how our supervisor is started and its `init` callback:

```
  def start_link(_opts) do
    Supervisor.start_link(__MODULE__, :ok, name: __MODULE__)
  end

  @impl true
  def init(:ok) do
    children = [
      {Registry, keys: :unique, name: @registry},
      {DynamicSupervisor, name: @supervisor, strategy: :one_for_one}
    ]

    Supervisor.init(children, strategy: :one_for_all)
  end
```

With the registry and dynamic supervisor in place, we can write the bump function:

```
  def bump(path) when is_binary(path) do
    pid =
      case Registry.lookup(@registry, path) do
        [{pid, _}] ->
          pid

        [] ->
          case DynamicSupervisor.start_child(@supervisor, {@worker, path}) do
            {:ok, pid} -> pid
            {:error, {:already_started, pid}} -> pid
          end
      end

    send(pid, :bump)
  end
end
```

The `bump` function looks up in the registry if there is a process for the given path and returns its process identifier (`pid`). If one does not exist, we ask the worker supervisor to start a worker dynamically. We expect two possible outcomes from `start_child`:

*   `{:ok, pid}` - the worker was started
    
*   `{:error, {:already_started, pid}}` - a worker for the given `path` already exists
    

We need the second branch to address a potential race condition where two users may access a page for the first time at the same time. In this scenario, the `Registry.lookup/2` will fail for both them, and both will attempt to spawn the worker. One of them will succeed and the other will return the “already started” error. Once we find the `pid`, we send it the `:bump` message.

We are almost there. There are just two steps left. First, we need to configure the worker to register itself whenever it is started. This is done via the `start_link` function. Let’s go back to the worker and add this:

```
  @registry Dashbit.Metrics.Registry

  def start_link(path) do
    GenServer.start_link(__MODULE__, path, name: {:via, Registry, {@registry, path}})
  end
```

Now we just need to start the `Dashbit.Metrics` supervision tree. This is typically done in your application supervision tree, typically located in “lib/my\_app/application.ex”:

```
  children = [
    Dashbit.Repo,
    Dashbit.Metrics,
    Dashbit.Endpoint
  ]
```

And that’s it. Now whenever a user accesses a page, we just need to call `Dashbit.Metrics.bump(path)` where `path` is the current page address. In our case, we store just the path, without host and without the query string). If you are using [Plug](https://hexdocs.pm/plug), it can be built from the `conn.path_info` field. We also only perform writes if the page was successfully rendered with 200 status. Overall, our bumping code looks like this:

```
plug :bump_metric

defp bump_metric(conn, _opts) do
  register_before_send(conn, fn conn ->
    if conn.status == 200 do
      path = "/" <> Enum.join(conn.path_info, "/")
      Dashbit.Metrics.bump(path)
    end

    conn
  end)
end
```

## Summary

In this article we have covered a minimal analytics system, using Ecto, GenServer and Elixir’s Registry, that performs writes asynchronously and in batches. The usage of the Registry to dynamically spawn processes that map to different resources, each with their own life-cycle, can be used in many different scenarios.

One important aspect in our solution is that, after a process for a page is created, it stays alive until there is a new deployment. This works for us because we have less than 100 pages, so we know the maximum number of processes is bound to a very low value.

Although Elixir process are lightweight thanks to the Erlang VM, if we had a large number of pages, such as millions of pages, we could potentially end-up with hundreds of thousands of unused processes. In this case, we would slightly change our solution to terminate the process after every upsert. Something along these lines:

```
  @impl true
  def handle_info(:upsert, {path, counter}) do
    # We first unregister ourselves so we stop receiving new messages.
    Registry.unregister(@registry, path)

    # Schedule to stop in 2 seconds, this will give us time to process
    # any late messages.
    Process.send_after(self(), :stop, 2_000)
    {:noreply, {path, counter}}
  end

  @impl true
  def handle_info(:stop, {path, counter})
    # Now we just stop. The terminate callback will write all pending writes.
    {:stop, :shutdown, {path, counter}}
  end
```

That’s it, we hope you have enjoyed the article and learned a thing or two that could be useful in your next project!
