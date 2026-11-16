---
url: "https://patrykbak.com/2020/07/07/handling-failures-in-background-workers-with-elixir-and-supervisors.html"
captured_at: "2026-11-16T04:41:29+00:00"
title: "Handling failures in background workers with Elixir and supervisors"
domain: "patrykbak-com"
---

Elixir is built on the top of the Erlang Virtual Machine. It allows us to write highly available systems that can run practically forever. Does that mean that we don’t have to do anything to make our systems reliable?

In our system, we have a worker which pays drivers money for their job.

```
defmodule Payment.Worker do
  use GenServer

  @interval 10 * 6000

  def start_link() do
    ...
  end

  def init(_) do
    Process.send_after(self(), :work, @interval)
    {:ok, %{interval: @interval}}
  end

  def handle_info(:work, state) do
    Repo.transaction(fn ->
      Job.Completed.fetch()
      |> Enum.map(fn %{job_id: job_id} ->
        :ok = Payment.pay_the_driver(job_id)

        job_id
      end)
      |> Job.Completed.delete_paid()
    end)

    Process.send_afer(self(), :work, state.interval)

    {:noreply, state}
  end
end
```

Let’s take a closer look at our **Payment.pay\_the\_driver/1** function to see what it does.

```
defmodule Payment do
  def pay_the_driver(%{id: job_id}) do
    :ok = pay(job_id)
    :ok = verify_payment(job_id)
  end

  defp verify_payment(job_id) do
    ...

    if over_the_limit?(to_be_paid, already_paid) do
      raise "Invalid payment for job #{job_id}"
    end
  end
end
```

The system compares money already paid with the amount which a driver should receive. It guarantees that a driver won’t receive more than they should.

Unfortunately, developers make mistakes and there’s a chance that an incorrect code is released. Luckily, the **verify\_payment/1** function prevents incorrect payments. But what happens to our application if such a scenario occurs and the function raises the error?

To understand consequences, let’s see how the supervision tree works.

![supervision-tree](https://patrykbak.com/assets/images/supervision_tree.png)

In the picture above, the main process supervises its child process - the **Worker** module.

Starting a supervisor, you can set what happens when one of the children gets crashed. [By default, a supervisor crashes when a child is restarted 3 times in 5 seconds](https://hexdocs.pm/elixir/Supervisor.html#module-start_link-2-init-2-and-strategies).

Our supervisor is configured with all these default values above:

```
defmodule Application do
  use Application
  import Supervisor.Spec

  def start(_type, _args) do
    children = [
      worker(Payment.Worker, []),
      ...
    ]
		
    opts = [strategy: :one_for_one, name: Supervisor]

    Supervisor.start_link(children, otps)
  end
end
```

It means that each time the **verify\_payment/1** function raises an error, our worker will be restarted.

```
defmodule Payment.Worker do
  use GenServer

  @interval 10 * 6000

  def start_link() do
    ...
  end

  def init(_) do
    Process.send_after(self(), :work, @interval)
    {:ok, %{interval: @interval}}
  end

  def handle_info(:work, state) do
     ...
  end
end
```

If it happens more than 3 times in 5 seconds, the main supervisor will also crash. As we can see, our worker handles its first message every second. If the logic within it raises an error, it will be able to reach more than 3 restarts within 5 seconds and consequently, our application will crash.

## So what’s now?

Even if there’s a problem with that part of the code, we still want the rest of the application to be up while we’re investigating the issue.

That’s why we can add a separate supervisor just for our worker:

![improved-supervision-tree](https://patrykbak.com/assets/images/supervision_tree_improved.png)

```
defmodule Payment.Supervisor do
  import Supervisor.Spec

  def start_link() do
    children = [
      worker(Payment.Worker, [])
    ]

    restart_interval = Payment.Worker.interval() / 1000
    default_max_seconds = 5
    max_restarts = ceil(default_max_seconds / restart_interval) + 1

    opts = [
      max_restarts: max_restarts,
      name: __MODULE__,
      strategy: :one_for_one
    ]

    Supervisor.start_link(children, opts)
  end
end
```

The supervisor needs to know the worker interval, so we have to replace the **@interval** attribute in the worker with the **interval()** public function.

```
defmodule Payment.Worker do
  use GenServer

  def start_link() do
    ...
  end

  def init(_) do
    Process.send_after(self(), :work, interval())
    {:ok, %{interval: interval()}}
  end

  ...

  def interval(), do: :timer.seconds(1)
end
```

Now our supervisor will crash if the child is restarted within 5 seconds more times than the value of **max\_restarts**.

The worker executes its function every second. Setting the limit to 6 restarts in 5 seconds guarantees that the supervisor will never crash.

It’s time to modify the main supervisor to look after the worker supervisor instead of the worker itself.

```
defmodule Application do
  use Application
  import Supervisor.Spec

  def start(_type, _args) do
    children = [
      supervisor(Payment.Supervisor, []),
      ...
    ]
		
    opts = [strategy: :one_for_one, name: Supervisor]

    Supervisor.start_link(children, otps)
  end
end
```

## Summing up

It’s sometimes hard to avoid temporary failures. You have to make sure that you have a plan for what happens if some parts of the system stop working correctly.

Originally published at [https://appunite.com](https://appunite.com/blog/handling-failures-in-background-workers-with-Elixir-and-supervisors) on Jul 7, 2020.
