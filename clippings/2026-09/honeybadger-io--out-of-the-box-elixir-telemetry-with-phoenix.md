---
url: "https://www.honeybadger.io/blog/phoenix-telemetry/?utm_medium=email&utm_source=elixir-radar"
captured_at: "2026-09-25T22:13:14+01:00"
title: "Out-of-the-box Elixir telemetry with Phoenix"
domain: "honeybadger-io"
---

Knowledge is power, and this is especially true for software. Telemetry puts software engineers in the driver's seat by exposing the underlying performance of a system. Identifying possible problems before they occur and proactively fixing them is better than waiting for users to point them out for you.

Telemetry refers to the instrumentation of a system. When you use your web application and take action, you emit events. These events can be aggregated to calculate statistics—which we call metrics—or written to logs. Later, they can be decorated with information that links them together.

This article will start by examining the built-in telemetry and metrics that come for free with the Phoenix framework in Elixir. Elixir is built on the BEAM virtual machine, which is cluster-friendly, so distributed telemetry works out of the box.

## What is telemetry?

The dictionary definition of telemetry is:

> The process of practice of obtaining measurements for recording or display to a point at a distance. The transmission of measurements by the apparatus making them. Also apparatus used for this; information so transmitted.

In short - _tele-_ - at a distance, _\-metry_ - of or pertaining to metrics.

At the heart of telemetry is designing software systems to **make their internal operations visible externally** - so that someone can take action based on that data. Those actions might be backward looking - _how did this happen?_ They might also be forward-looking - _if we don't address this, then bad things might happen_.

### The relationship between a telemetry event and metrics

We call the raw actions coming out of a system **events**. A properly tagged set of continuous events is a critical resource in backward-looking telemetry, helping developers figure out what happened inside a system.

For forward-looking telemetry, an aggregated view of events is more useful. We call these events **metrics**.

The metrics reported might be operationally related - _"the Dilithum Crystals cannae handle it Captain"_ or they might be business focused - _"aggregated sales volume is 20% below trend"_.

Starting a tech company in Linlithgow, where Engineer Scottie from Star Trek will be born in 2222, I obviously have Dilithium Crystals hanging about, but don't worry young 'un, keep at it and the good tech will come your way - if you focus on the business side and get the money in.

Telemetry is a holistic game. The customer doesn't care if they didn't get your order because of a bug in your application software, or your server ran out of memory or rain came through the roof and fried all the electronics in the data center.

Before we start digging into it, let's start looking at what telemetry comes out of the box with Phoenix.

## Quick start for telemetry with Phoenix

We'll start by creating a dummy Phoenix application called `Brock`, a guid Scots word for badger. Be sure to [install Elixir and Phoenix](https://hexdocs.pm/phoenix/installation.html) before continuing.

For this tutorial, we'll be using Phoenix with Elixir 1.17.3, and assume that you already also have [Postgres](https://www.postgresql.org/download/).

Building `Brock` will show us Phoenix's telemetry tooling. (For readers for whom English is a 2nd language that's _good Scots_, for all you native speakers, _Saor Alba!_ \[strikes Mel Gibson in _Braveheart_ pose\])

```
mix phx.new brock
```

You will notice as the terminal scrolls past that it has created a telemetry module in `brock/lib/brock_web`. Perhaps not surprisingly it is called `telemetry.ex`.

Next, do the rest of the setup:

```
cd brock
mix ecto.create
```

Depending on your setup you might need to fiddle with database passwords and hostnames that Phoenix uses to connect to Postgres. These configuration settings are usually in `config/dev.exs`

### Looking for the telemetry module

Before we start the application, let's poke around the existing code and see what we see.

In `mix.exs` we can see that Phoenix is pulling in the dependencies [telemetry\_poller](https://hexdocs.pm/telemetry_poller/readme.html) and [telemetry\_metrics](https://hexdocs.pm/telemetry_metrics/Telemetry.Metrics.html) and they, in turn, pull in the base Erlang telemetry package [telemetry](https://hexdocs.pm/telemetry/readme.html). By default, Phoenix starts the telemetry supervisor and we are good to go.

The poller is a library that collects metrics from the underlying virtual machine - the BEAM. Remember that the customer doesn't care what caused the problem - but for programmers understanding the behavior of the underlying BEAM or the operating systems or hardware is also important in telematics.

Skimming the code in `telemetry.ex` we can see that there are a load of metrics defined, for example:

```
summary("phoenix.endpoint.start.system_time", unit: {:native, :millisecond}),
# …
summary("brock.repo.query.total_time", unit: {:native, :millisecond}, description: "The sum of the other measurements"),
# …
summary("vm.memory.total", unit: {:byte, :kilobyte}),
```

Phoenix is collecting metrics from the Phoenix application itself, the Ecto repo instantiated inside the new Brock app, and the Erlang virtual machine. Later on, we will see how these are presented to the user.

This module is where you would add your custom **metrics**. In your code, you would write emitters for the telemetry **events**.

The only metric type already configured is `summary`, but there are another 4 available; `counter`, `sum`, `last_value` and `distribution`. You can read about them in [the telemetry metrics documentation](https://hexdocs.pm/telemetry_metrics/Telemetry.Metrics.html#module-vm-metrics).

One last thing before we fire up Phoenix - let's add operating system monitoring to receive VM-related events. We do this by editing the `application` function in `mix.exs` to add a new parameter `:os_mon`:

```
# Type `mix help compile.app` for more information.
def application do
  [
    mod: {Brock.Application, []},
    extra_applications: [:logger, :runtime_tools, :os_mon]
  ]
end
```

Now let's see Phoenix telemetry in action! Start your Phoenix app in a shell:

```
iex -S mix phx.server
```

If we head over to the browser at [http://localhost:4000/dev/dashboard](http://localhost:4000/dev/dashboard), we can see the dashboard in action:

![Phoenix Dashboard showing the out-of-the-box Elixir telemetry](https://www-files.honeybadger.io/posts/phoenix-telemetry/phoenix-dashboard.png)

The built-in telemetry events are aggregated into metrics. The metrics collector is invoked periodically to collect them, and you can see that it does so on a 15-second cycle. It might appear that the telemetry poller is doing this, but it isn't, it's polling the OS and BEAM for you.

This is a presentation of holistic telemetry. Scan along the menu bar - you have tabs for metrics about the Operating System, the use of memory by the BEAM, the atom table, the supervision trees, details of running applications, and more - and a particular tab called Metrics - which displays the specific telemetry that we have looked at. Let's have a peek:

![Built-in Ecto repo metrics showing the performance of the database in our Phoenix app](https://www-files.honeybadger.io/posts/phoenix-telemetry/application-telemetry-dashboard.png)

A side-by-side comparison of the three tabs here (`Brock`, `Phoenix` and `VM`) will show that there is a graph generated for each metric defined in `telemetry.ex`. The Brock app is getting metrics from its Ecto repo which makes sense. Everybody needs to graph query execution time for their database, right?

You might have a single Phoenix app, starting multiple web applications with their own databases and Ecto repos. You'd probably want to see metrics from each one separately.

Phoenix is built on top of Elixir which is built on top of the BEAM and Erlang OTP. OTP is a very mature platform dating back to the 1990s with very strong operational support. You don't build systems with 99.9999999% uptime (31.56 milliseconds downtime **per year**) accidentally.

The entire stack is wired for telemetry with the veritable SASL (System Architecture Support Libraries) underpinning it all. OTP is instrumented, Phoenix is instrumented, and now it's up to you to live up to the great traditions of the BEAM community.

## Writing your own telemetry in Phoenix

Let's start by adding new metrics to our stack. We'll first add some new metrics for Brock in the `telemetry.ex` module. All the existing Phoenix/Repo metrics are `summary` so let's mix it up a bit and start by defining metrics of all the other varieties:

```
  def metrics do
    [
      # Phoenix Metrics
      # …
      # Database Metrics
      # …
      # VM Metrics
      # …
      summary("vm.total_run_queue_lengths.io"),

      # Brock metrics
      counter("brock.bingobongo"),
      sum("brock.bingobongo"),
      last_value("brock.bingobongo"),
      distribution("brock.bingobongo")
    ]
  end
```

Pop over to the dashboard and refresh and we can see that the graphs are all there:

![New custom telemetry metrics for Brock in the Phoenix dashboard](https://www-files.honeybadger.io/posts/phoenix-telemetry/new-custom-metrics.png)

### Adding our own telemetry events

Now let's populate those graphs. To do that we need to emit telemetry events. Rather than go through the whole faff of setting up a dummy app, let's just do it from the shell. It's how Joe Armstrong always worked, so you are in good company.

At the prompt, we can just fire off telemetry events:

```
iex(1)> :telemetry.execute([:brock], %{bingobongo: 9})
:ok
iex(2)> :telemetry.execute([:brock], %{bingobongo: 33})
:ok
iex(3)> :telemetry.execute([:brock], %{bingobongo: 5})
:ok
iex(4)> :telemetry.execute([:brock], %{bingobongo: 2.3})
:ok
```

And voila they appear in the dashboard:

![The new (fake) telemetry metrics we have created for Brock appear automatically](https://www-files.honeybadger.io/posts/phoenix-telemetry/fake-brock-metrics.png)

We are aggregating the same event in 4 different ways here. The telemetry library we are using is written in Erlang which is why you are specifying the module name as an atom - Erlang doesn't have a hierarchical module namespace like Elixir. There is a common open telemetry framework so that different monitoring solutions can be attached and this library is a key part of that.

Looking at the graphs, they don't make much sense, which does make sense as they are fake metrics. In your real app you will need to work out what you want to measure and how.

There are [various configuration options](https://hexdocs.pm/phoenix_live_dashboard/metrics_history.html) which you can explore and metrics data can be saved, although that is a bit more work.

### Driving multiple metrics with the same telemetry events

A single telemetry event can feed multiple metrics. Let's add a couple of new metrics in the `telemetry.ex` module:

```
  def metrics do
    [
      # Brock metrics
      # ...
      sum("brock.bingo.jammies"),
      sum("brock.bingo.jimmies")
    ]
  end
```

Let's get some telemetry events emitted:

```
iex(5)> :telemetry.execute([:brock, :bingo], %{jammies: 53, jimmies: 133})
:ok
iex(6)> :telemetry.execute([:brock, :bingo], %{jammies: 15, jimmies: 15})
:ok
```

We get both graphs populated:

![Multiple custom metrics from a single telemetry event](https://www-files.honeybadger.io/posts/phoenix-telemetry/multiple-custom-metrics-from-one-event.png)

The metrics come in a natural hierarchical namespace which you need to design, so `counter(“brock.bingo.bongo”)` would be invoked like `:telemetry.execute([:brock, :bingo], %{bongo: 11})`.

We can extend the model with event metadata. Event metadata allows you to slice and dice your metrics. Imagine you have a common registration process for developers, small companies, and enterprise users. Now imagine you have instrumented it! You want to understand its behaviour as a whole, but also be able to compare how different classes of users execute the process — tagging your events with event metadata is the how you would do that.

[Adding event metadata](https://hexdocs.pm/telemetry/telemetry.html#execute/3) is simple, and helps in extracting valuable data from all your metrics:

```
:telemetry.execute([:db, :query], %{duration: 198}, %{table: "users", operation: "insert"})
```

When the telemetry event arrives at the metrics engine, it sets about tagging metrics. The metrics definitions include tag values which are used to extract tagging from the metadata. You can read about tagging in [the documentation](https://hexdocs.pm/telemetry_metrics/Telemetry.Metrics.html#module-breaking-down-metric-values-by-tags).

We can also build spanning that runs across multiple telemetry events, providing a holistic view of a process across the HTTP request lifecycle and beyond.

## Distributed telemetry with Elixir clusters

So far we have looked at the _\-metry_ end of the telescope. Now it's time to look at the _tele-_ bit, getting data out of one system.

Leveraging the power of the BEAM we can start exploring telemetry. The first step is to build an Elixir cluster:

```
cd ./config
cp dev.exs dev2.exs
```

Let's edit `dev2.exs` so we can create a cluster. There are 2 settings we need to change. First up we rename the database:

```
config :brock, Brock.Repo,
  username: "postgres",
  password: "postgres",
  hostname: "db",
  database: "brock_dev2",
```

Next, we need to bind the webserver to a different port:

```
config :brock, BrockWeb.Endpoint,
  # Binding to loopback ipv4 address prevents access from other machines.
  # Change to `ip: {0, 0, 0, 0}` to allow access from other machines.
  http: [ip: {0, 0, 0, 0}, port: 4001],
```

We also need to enable `Phoenix.LiveReload` in `mix.exs`:

```
{:phoenix_live_reload, "~> 1.2"},
```

Now we are going to start two sessions in two different terminals. In one type:

```
iex --sname dev1 --cookie jerko -S mix phx.server
```

And in the other, type:

```
MIX_ENV=dev2 mix ecto.create
MIX_ENV=dev2 iex --sname dev2 --cookie jerko -S mix phx.server
```

We should now have two instances of Phoenix running on two Erlang VMs - one bound to port 4000 and the other to 4001.

These two have the same cookies - we can check with `:erlang.get_cookie()` and we can make them into a cluster simply by pinging one from the other. My nodes are called `dev1@gordon` and `dev2@gordon` ("gordon" is the hostname), so executing `:net_adm.ping(:'dev1@gordon')` on `dev2` will do the trick. You should get a `pong` back and not a `pang` (it's Swedish humor, that is).

If we now run `:erlang.nodes()` in one shell we should get back a list with the other node name in it.

### Clustered Elixir telemetry metrics

Now we'll power over to the browser and look at the dashboard:

![Clustered telemetry with elixir and phoenix](https://www-files.honeybadger.io/posts/phoenix-telemetry/clustered-telemetry-with-elixir-and-phoenix.png)

In the top right corner we can detach the dashboard and connect it to another node. Pretty neat, huh?

So how does Elixir do that? The best way to understand it is to compare the processes of the same BEAM from 2 dashboards:

First up is the view of `dev1` from `dev1`:

![Process view of dev1 from dev1](https://www-files.honeybadger.io/posts/phoenix-telemetry/process-view-of-dev1-from-dev1.png)

And then the same view from `dev2`:

![Process view of dev1 from dev2](https://www-files.honeybadger.io/posts/phoenix-telemetry/process-view-of-dev1-from-dev2.png)

The process with the PID `<0.50.0>` on `dev1` is `<29582.50.0>` on `dev2` and all the way down the list.

The PID (or process ID) is a fundamental element of the BEAM and it has 3 visible parts (and an invisible one). The middle number is the number of the process on the machine it is running one, the left number is the number of the machine on the physical host, and the right number is the number of the physical node in the cluster.

The BEAM implements an actor model - discrete processes that communicate by sending each other messages. The PID is the postal address of the system even if the process is on another VM on another machine.

Thanks to PIDs, the whole core of Erlang is network transparent, and building clusters and working across a cluster is super-easy, like impossibly easy. So the dashboard running on one server can simply swap over and attach to the telemetry supervision tree on the other server and show that instead.

(The invisible number is the generation number, if a process dies and then a new process gets its PID, it's a different PID. Generation numbers are a bit obscure, and you needn't normally worry about them, but it's the reason `:erlang.list_to_pid/1` has a [warning](https://www.erlang.org/doc/apps/erts/erlang.html#list_to_pid/1) not to be used in production.)

### Free distributed telemetry

But there's more. Let's start a new node with the command:

```
iex --sname nophoenix --cookie jerko
```

Now do the same `ping` trick (`:net_adm.ping(:'nophoenix@gordon')`) on another node. Joining this new node to one of the nodes in the cluster connects it to both. You can check by running `:erlang.nodes()` in both shells. This 3rd node, which is not running Phoenix, appears on our dashboard list and we can attach the dashboard to it:

![The miracle of distributed telemetry with Elixir - a node not running phoenix appearing in a dashboard anyway](https://www-files.honeybadger.io/posts/phoenix-telemetry/the-miracle-of-distributed-telemetry.png)

Obviously the dashboard has a few less elements. The node under observation isn't running Phoenix, so any of the Phoenix-specific bits aren't there. The `os_mon` application isn't started either so none of that, and telemetry is missing. But you can see how distributed telematics really can work in Elixir, with or without Phoenix.

### Show this to your ops team

Often times a software shop will switch to Elixir and Phoenix for concurrency and performance reasons. The developers will often be excited but the ops teams are not as excited. This simple cluster trick is a good way to persuade your ops teams that they really need to understand how different working with the BEAM and OTP is to working with the JVM or PHP or Ruby or anything else.

It's a best practice to take the live dashboard out of your non-development environments but the network transparency allows you to build a separate jump server inside your secure DMZ with monitored access. You can connect that to a production machine _round the back_ securely and use your dashboard for diagnostics.

### Show this to your security team

Once upon a time, when I was a BEAM guru at a big company, I tried and tried to persuade them to manage their cookies properly and have cluster separation across the piece. “Pfft” they said.

We later accidentally clustered the testing and production clusters while deploying a new system that was literally catching money falling from the sky. Then other words were said - words I blush at the memory of.

After that cookies and clustering were taken seriously. For a bit of fun, show your security team this command and watch them sweat `:kernel.call(SomeNode, System, :cmd, \[“rm”, “-rf”, “/\*”\])`. (**Hint**: is letting somebody on another machine in the cluster wipe your file system a good thing or a bad thing?)

When clustered Elixir is good, its very, very good—and when it's bad, it's horrid!

### Use this trick for developing instrumented libraries

Imagine you are writing a library and you want it to emit telemetry events to be a good citizen. You can add the telemetry library to your application, then in development, you can just fire up an empty Phoenix app and attach it to the node you are running your library in. You'll get a free dashboard!

## Take telemetry to the next level in your Elixir and Phoenix apps

Phoenix telemetry out of the box gives you a great start on managing and inspecting your application. Phoenix's telemetry events take you a long way, but your app is unique to you and your company, so you should add custom events relevant to your business model.

The Phoenix dashboard also brings in native BEAM telemetry by reporting the underlying metrics. However, the value of telemetry lies not in a particular measurement but upon _acting_ on the measurement. It is mapping an event emitted to a metric on which there is a threshold. That threshold should alert a person to take action.

Telemetry without alerts and user actions is just vanity programming. You need to wire your instrumentation up to your operational processes, and Honeybadger can help with that. Honeybadger's [full-stack Phoenix monitoring platform](https://www.honeybadger.io/for/phoenix/) allows you to graph, query, and alert on your Phoenix telemetry data.

In addition to Honeybadger's Elixir error tracking, logging, and uptime monitoring tools, it's the best way to gain real-time insights into your application's health and performance.
