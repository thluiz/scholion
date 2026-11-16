---
title: "Adding custom metrics to a Phoenix 1.5 live dashboard"
date: '2026-11-16T05:59:01+00:00'
category: webclip
summary: 'The post shows how to emit a custom telemetry counter from a Phoenix controller, register it in the Telemetry metrics list, add a GenServer that sends periodic work events, and display the new graphs on the live dashboard.'
tags: ["elixir", "phoenix-framework", "telemetry", "live-dashboard"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Adding custom metrics to a Phoenix 1.5 live dashboard | by Marc Delagrammatikas | Medium"
    url: "https://medium.com/@marcdel/adding-custom-metrics-to-a-phoenix-1-5-live-dashboard-1b21a8df5cf1"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/medium-com--adding-custom-metrics-to-a-phoenix-15-live-dashboard.md"
    kind: repo
---

The article adds custom metrics to a Phoenix 1.5 live dashboard by emitting telemetry from a controller, registering the counter in the Telemetry metrics list, and then adding a GenServer that periodically sends work events. It shows how those metrics appear on the dashboard and notes that summary metrics expose mix, max, average, count, or duration.

## Reading notes

- It starts by installing Phoenix 1.5 project generator, creating a new project, and adding a `:telemetry.execute/2` call in `PageController.index/2`.
- The custom counter is added in `metrics_demo_web/telemetry.ex` as `counter("metrics_demo.render.controller")`.
- The metric name prefix determines the dashboard tab, and the order of metrics in the array affects their order on the page.
- The article explains that only the controller value is counted in the example, even though the action value is also present in the emitted event.
- It then adds a `MetricsDemo.MetricsGenerator` GenServer that sends a `:work` telemetry event every 2 seconds with random `duration` and `result_count` values.
- The GenServer is added to `application.ex` so it starts with the app.
- Two summary metrics, `metrics_demo.work.duration` and `metrics_demo.work.result_count`, are added to the Telemetry metrics list.
- After restarting the app, the dashboard shows the new metrics automatically.
- The post notes that summary graphs show mix, max, average, and count or duration.
- It also says the dashboard data is transient and refreshing the page clears collected data.
