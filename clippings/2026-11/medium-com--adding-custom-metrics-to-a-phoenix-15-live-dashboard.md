---
url: "https://medium.com/@marcdel/adding-custom-metrics-to-a-phoenix-1-5-live-dashboard-1b21a8df5cf1"
captured_at: "2026-11-16T05:59:01+00:00"
title: "Adding custom metrics to a Phoenix 1.5 live dashboard | by Marc Delagrammatikas | Medium"
domain: "medium-com"
---

Elixir
Phoenix Framework
Web Development
Programming
Adding custom metrics to a Phoenix 1.5 live dashboard
Marc Delagrammatikas
4 min read
·
Apr 22, 2020

Part 2: Sending Phoenix 1.5 metrics to InfluxDb

The code for this demo is available here

To get started, make sure you have the Phoenix 1.5 project generator:

mix archive.uninstall phx_new
mix archive.install hex phx_new 1.5.1

Create a new Phoenix 1.5 project:

mix phx.new metrics_demo
cd metrics_demo && mix ecto.create

Open metrics_demo/lib/metrics_demo_web/controllers/page_controller.ex and add the following line to emit a telemetry event:

:telemetry.execute([:metrics_demo, :render], %{controller: "PageController", action: "index"})

It should now look like this:

defmodule MetricsDemoWeb.PageController do
use MetricsDemoWeb, :controller

def index(conn, _params) do
:telemetry.execute([:metrics_demo, :render], %{controller: "PageController", action: "index"})
render(conn, "index.html")
end
end

Now open metrics_demo/lib/metrics_demo_web/telemetry.ex and add the following line anywhere in the metrics array:

counter("metrics_demo.render.controller"),

It should look something like this:

defmodule MetricsDemoWeb.Telemetry do
use Supervisor
import Telemetry.Metrics

def start_link(arg) do
Supervisor.start_link(__MODULE__, arg, name: __MODULE__)
end

@impl true
def init(_arg) do
children = [
{:telemetry_poller, measurements: periodic_measurements(), period: 10_000}
# Add reporters as children of your supervision tree.
# {Telemetry.Metrics.ConsoleReporter, metrics: metrics()}
]

Supervisor.init(children, strategy: :one_for_one)
end

def metrics do
[
# Phoenix Metrics
summary("phoenix.endpoint.stop.duration",
unit: {:native, :millisecond}
),
summary("phoenix.router_dispatch.stop.duration",
tags: [:route],
unit: {:native, :millisecond}
),

# App Metrics
counter("metrics_demo.render.controller"),

# Database Metrics
summary("metrics_demo.repo.query.total_time", unit: {:native, :millisecond}),
summary("metrics_demo.repo.query.decode_time", unit: {:native, :millisecond}),
summary("metrics_demo.repo.query.query_time", unit: {:native, :millisecond}),
summary("metrics_demo.repo.query.queue_time", unit: {:native, :millisecond}),
summary("metrics_demo.repo.query.idle_time", unit: {:native, :millisecond}),

# VM Metrics
summary("vm.memory.total", unit: {:byte, :kilobyte}),
summary("vm.total_run_queue_lengths.total"),
summary("vm.total_run_queue_lengths.cpu"),
summary("vm.total_run_queue_lengths.io")
]
end

defp periodic_measurements do
[
# A module, function and arguments to be invoked periodically.
# This function must call :telemetry.execute/3 and a metric must be added above.
# {MetricsDemoWeb, :count_users, []}
]
end
end

Note: the names and order of items in the array are significant. The part of the string before the first dot (.) determines which tab the graph for the metric appears in, and the graphs will appear in order on the page in relation to things with the same top level “namespace”.

We’re only counting calls to metrics.render here, the fact that we’re using the controller value and disregarding the action value doesn’t make a difference.

If you navigate to the metrics page of the dashboard, you should see our new “metrics_demo.render.controller” graph on the MetricsDemo tab:

Now if we visit the home page again in another tab/window, we should see a datapoint appear:

Cool! …kinda. Let’s mash the refresh button on our home page window.

Okay, that’s a little more interesting!

Note: the repo seems to be doing things even though we don’t have any queries on this page. I’d be interested to dig in and see why that is.

Let’s generate some more interesting data. We’re going to add a GenServer to periodically send telemetry events, let’s call it metrics_generator.ex.

defmodule MetricsDemo.MetricsGenerator do
use GenServer

def start_link(initial_state) do
GenServer.start_link(__MODULE__, initial_state, name: __MODULE__)
end

@impl GenServer
def init(state) do
schedule_work()

{:ok, state}
end

@impl GenServer
def handle_info(:work, state) do
:telemetry.execute([:metrics_demo, :work], %{
duration: Enum.random(0..10),
result_count: Enum.random(0..100)
})

schedule_work()

{:noreply, state}
end

defp schedule_work do
# 2 seconds
Process.send_after(self(), :work, 2 * 1000)
end
end

Every 2 seconds this will emit a work event with two metrics: duration and result_count with have a random value between 0 and 10 or 0 and 100.

We’ll need to add it to the children in metrics_demo/lib/metrics_demo/application.ex to start it when our application starts.

defmodule MetricsDemo.Application do
# See https://hexdocs.pm/elixir/Application.html
# for more information on OTP Applications
@moduledoc false

use Application

def start(_type, _args) do
children = [
# Start the Ecto repository
MetricsDemo.Repo,
# Start the Telemetry supervisor
MetricsDemoWeb.Telemetry,
# Start the PubSub system
{Phoenix.PubSub, name: MetricsDemo.PubSub},
# Start the Endpoint (http/https)
MetricsDemoWeb.Endpoint,
# Start a worker by calling: MetricsDemo.Worker.start_link(arg)
# {MetricsDemo.Worker, arg}
MetricsDemo.MetricsGenerator
]

# See https://hexdocs.pm/elixir/Supervisor.html
# for other strategies and supported options
opts = [strategy: :one_for_one, name: MetricsDemo.Supervisor]
Supervisor.start_link(children, opts)
end

# Tell Phoenix to update the endpoint configuration
# whenever the application is updated.
def config_change(changed, _new, removed) do
MetricsDemoWeb.Endpoint.config_change(changed, removed)
:ok
end
end

Now we can add some summary graphs of these metrics to our dashboard. Back in lib/metrics_demo_web/telemetry.ex add the following lines just below our count metric.

summary("metrics_demo.work.duration"),
summary("metrics_demo.work.result_count"),

The metrics function should now look like this:

def metrics do
[
# Phoenix Metrics
summary("phoenix.endpoint.stop.duration",
unit: {:native, :millisecond}
),
summary("phoenix.router_dispatch.stop.duration",
tags: [:route],
unit: {:native, :millisecond}
),

# App Metrics
counter("metrics_demo.render.controller"),
summary("metrics_demo.work.duration", unit: {:native, :millisecond}),
summary("metrics_demo.work.result_count"),

# Database Metrics
summary("metrics_demo.repo.query.total_time", unit: {:native, :millisecond}),
summary("metrics_demo.repo.query.decode_time", unit: {:native, :millisecond}),
summary("metrics_demo.repo.query.query_time", unit: {:native, :millisecond}),
summary("metrics_demo.repo.query.queue_time", unit: {:native, :millisecond}),
summary("metrics_demo.repo.query.idle_time", unit: {:native, :millisecond}),

# VM Metrics
summary("vm.memory.total", unit: {:byte, :kilobyte}),
summary("vm.total_run_queue_lengths.total"),
summary("vm.total_run_queue_lengths.cpu"),
summary("vm.total_run_queue_lengths.io")
]
end

If we stop and restart our app, we should see metrics starting to show up automatically. Because we used the summary instead of the counter, we can see the mix/max, average, and the count or duration.

Note: these dashboards are transient and refreshing the page will clear all of the data that was collected. If you want to be able to view historical data, you’ll need to have a persistent storage mechanism handle the events as well. Stay tuned for a follow up post on writing telemetry metrics to InfluxDB!

If you’d like to see the diff with all of these changes in one place, click here.
