---
title: "Building Distributed Systems in Elixir: Part 6 — Named Processes"
date: '2026-09-28T15:11:59+01:00'
category: webclip
summary: 'The article shows how named processes give a worker a stable, discoverable address with local registration or `:global`, while supervisors still handle restarts and replacement PIDs.'
tags: ["elixir", "named-processes", "process-registration", "distributed-systems"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Building Distributed Systems in Elixir: Part 6 — Named Processes"
    url: "https://dev.to/pckrishnadas88/building-distributed-systems-in-elixir-part-6-named-processes-l3"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--building-distributed-systems-in-elixir-part-6-named-processe.md"
    kind: repo
---

The article explains why sharing a PID is fragile: a PID points to one running incarnation, so it works for replies, monitors, and links, but not as a stable service address after a crash and restart. It then introduces named processes as a way for callers to depend on a service role instead of a temporary PID.

## Reading notes

- A worker can be registered locally with `Process.register/2`, then found with `Process.whereis/1` or addressed directly with `send/2` using the name.
- Local registration belongs to one BEAM node, so the same name can exist on different disconnected nodes without conflict.
- `:global.register_name/2` and `:global.whereis_name/1` provide node-wide lookup for connected nodes, but the article notes that global coordination has operational trade-offs.
- The worker can register itself and return `:worker` instead of its PID, so clients send requests to the name and keep the caller PID only for the reply path.
- Names do not replace supervision: when a registered process exits, its name is removed and a replacement still needs to be started and registered.
- One local name maps to one owner, so this simple mechanism fits a singleton service but not a worker pool.
- For reply correlation, the article shows matching on the request value and suggests `make_ref()` when several requests may be in flight with the same value.
- The closing point is that naming helps discovery, while supervisors handle lifecycle, and distributed systems still need decisions about partitions, duplicate claims, and dead PIDs.

## Series

*Building Distributed Systems in Elixir*, by krishnadaspc. Research: [Distributed Systems Patterns](/research/distributed-systems-patterns).

- [Part 1 — Stateful Process Without GenServer](/notes/building-a-stateful-process-in-elixir-without-genserver)
- [Part 2 — Correlated Request–Reply](/notes/building-distributed-systems-with-elixir-02-correlated-reque)
- [Part 3 — Process Monitoring](/notes/building-distributed-systems-in-elixir-part-3-process-monito)
- [Part 4 — Process Linking](/notes/building-distributed-systems-in-elixir-part-4-process-linkin)
- [Part 5 — Supervisor From Scratch](/notes/building-distributed-systems-in-elixir-part-5-supervisor-fro)
- **Part 6 — Named Processes**
- [Part 7 — Worker Pool](/notes/building-distributed-systems-in-elixir-part-7-worker-pool)
- [Part 8 — Publish / Subscribe](/notes/building-distributed-systems-in-elixir-part-8-publish-subscr)
- [Part 9 — Backpressure](/notes/building-distributed-systems-in-elixir-part-9-backpressure)
