---
title: "Building Distributed Systems in Elixir: Part 5 — Supervisor From Scratch"
date: '2026-09-28T15:11:39+01:00'
category: webclip
summary: 'The article builds a manual one-for-one supervisor in Elixir using links, trapped exits, and message passing to restart only a crashed worker while leaving a healthy sibling running.'
tags: ["elixir", "supervision", "process-links", "distributed-systems"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Building Distributed Systems in Elixir: Part 5 — Supervisor From Scratch"
    url: "https://dev.to/pckrishnadas88/building-distributed-systems-in-elixir-part-5-supervisor-from-scratch-32mh"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--building-distributed-systems-in-elixir-part-5-supervisor-fro.md"
    kind: repo
---

The article shows how to build a small supervisor without GenServer or OTP Supervisor. It links two workers to a supervising process, traps exits, and uses a child map to identify which worker died so only that worker is restarted.

It also explains the difference between abnormal and normal exits, the fresh state of replacement processes, and the limits of the manual approach compared with OTP supervision.

## Reading notes

- The supervisor starts two linked workers and keeps a map from PID to logical worker name.
- `Process.flag(:trap_exit, true)` turns exit signals into `{:EXIT, pid, reason}` messages.
- An abnormal exit removes the dead PID, starts a replacement with the same name, and stores the new PID.
- A normal exit removes the worker without restarting it.
- The demo polls for a new PID only to verify the asynchronous restart.
- Restarting a worker restores the process, not its private in-memory state.
- The manual implementation does not cover restart limits, shutdown timeouts, structured child specs, or nested supervision.
- OTP Supervisor is presented as the production-ready version of these ideas.

## Series

*Building Distributed Systems in Elixir*, by krishnadaspc. Research: [Distributed Systems Patterns](/research/distributed-systems-patterns).

- [Part 1 — Stateful Process Without GenServer](/notes/building-a-stateful-process-in-elixir-without-genserver)
- [Part 2 — Correlated Request–Reply](/notes/building-distributed-systems-with-elixir-02-correlated-reque)
- [Part 3 — Process Monitoring](/notes/building-distributed-systems-in-elixir-part-3-process-monito)
- [Part 4 — Process Linking](/notes/building-distributed-systems-in-elixir-part-4-process-linkin)
- **Part 5 — Supervisor From Scratch**
- [Part 6 — Named Processes](/notes/building-distributed-systems-in-elixir-part-6-named-processe)
- [Part 7 — Worker Pool](/notes/building-distributed-systems-in-elixir-part-7-worker-pool)
- [Part 8 — Publish / Subscribe](/notes/building-distributed-systems-in-elixir-part-8-publish-subscr)
- [Part 9 — Backpressure](/notes/building-distributed-systems-in-elixir-part-9-backpressure)
