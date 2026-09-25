---
title: "Out-of-the-box Elixir telemetry with Phoenix"
date: '2026-09-25T22:13:14+01:00'
category: webclip
summary: 'The article explains Phoenix’s built-in telemetry, how metrics are defined in telemetry.ex, how events feed multiple metrics, and how clustered Elixir lets the dashboard attach to other nodes.'
tags: ["phoenix", "elixir", "telemetry", "distributed-systems"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Out-of-the-box Elixir telemetry with Phoenix"
    url: "https://www.honeybadger.io/blog/phoenix-telemetry/?utm_medium=email&utm_source=elixir-radar"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/honeybadger-io--out-of-the-box-elixir-telemetry-with-phoenix.md"
    kind: repo
---

Phoenix ships with telemetry, metrics, and dashboard support that expose Phoenix, Ecto, and BEAM activity by default. The article shows how the dashboard aggregates these measurements, how custom metrics can be added in `telemetry.ex`, and how telemetry events can carry metadata for tagging and splitting data.

It also shows that Elixir nodes can be clustered and observed through the same dashboard, even when the target node is not running Phoenix. The final point is that telemetry is useful only when it is connected to alerts and operational action.

## Reading notes

- Telemetry is presented as instrumentation that makes internal system operations visible so people can act on the data.
- Raw actions from the system are events; aggregated events become metrics.
- Phoenix includes telemetry poller and telemetry metrics dependencies, and starts the telemetry supervisor by default.
- The generated `telemetry.ex` module defines metrics for Phoenix, the repo, and the VM.
- `summary` is already configured, and the article names `counter`, `sum`, `last_value`, and `distribution` as other metric types.
- The tutorial adds `:os_mon` so the dashboard can receive operating-system-related events.
- The dashboard shows metrics for the OS, BEAM memory, the atom table, supervision trees, running applications, and custom application metrics.
- Custom metrics are added by editing `telemetry.ex` and defining new metric entries.
- The article demonstrates emitting telemetry events from `iex` with `:telemetry.execute/2`.
- One event can feed multiple metrics.
- Event metadata can be used to tag metrics and compare different user or process categories.
- Elixir clustering is shown by starting two Phoenix nodes with the same cookie and connecting them with `:net_adm.ping/1`.
- The dashboard can detach from one node and attach to another node in the cluster.
- A node not running Phoenix can still appear in the dashboard once it is joined to the cluster.
- The article argues that telemetry becomes useful when it drives alerts and operational response, not when it stays as instrumentation alone.
