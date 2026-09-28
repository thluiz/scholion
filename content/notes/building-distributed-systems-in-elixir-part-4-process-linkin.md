---
title: "Building Distributed Systems in Elixir: Part 4 — Process Linking"
date: '2026-09-28T15:11:14+01:00'
category: webclip
summary: 'The article explains how `spawn_link/1` connects two BEAM processes so an abnormal exit in one can terminate the other, and how `Process.flag(:trap_exit, true)` turns that exit into a message.'
tags: ["elixir", "beam", "process-linking", "supervision"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Building Distributed Systems in Elixir: Part 4 — Process Linking"
    url: "https://dev.to/pckrishnadas88/building-distributed-systems-in-elixir-part-4-process-linking-okb"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--building-distributed-systems-in-elixir-part-4-process-linkin.md"
    kind: repo
---

The article shows that process links create a bidirectional failure relationship between BEAM processes. Unlike monitors, links are not just observation; an abnormal exit in a linked process can terminate the other process unless exits are trapped.

It also shows how `Process.flag(:trap_exit, true)` converts the exit signal into a regular `{:EXIT, from_pid, reason}` mailbox message. That lets the parent process receive and inspect the worker’s failure, while still leaving restart decisions for later supervisor logic.

## Reading notes

- `spawn_link/1` starts and links a process atomically, avoiding a gap where the child could crash before the link exists.
- A linked crash propagates as an exit signal, so an abnormal worker exit can terminate the parent.
- Normal exits do not ordinarily take down linked processes that are not trapping exits.
- `Process.flag(:trap_exit, true)` changes the incoming exit signal into a mailbox message.
- The trapped message has the shape `{:EXIT, from_pid, reason}`.
- `^worker` pins the receive pattern to the specific linked worker PID.
- Trapping exits lets the parent observe the failure and stay alive.
- Links and monitors are different: monitors are one-way and produce `{:DOWN, ...}`, while links are bidirectional and affect process lifecycles.
- The article treats links as a step before supervision, since restart policy still has to be decided separately.
- The next part will build a supervisor from scratch and use the trapped exit to start a replacement worker.

## Series

*Building Distributed Systems in Elixir*, by krishnadaspc. Research: [Distributed Systems Patterns](/research/distributed-systems-patterns).

- [Part 1 — Stateful Process Without GenServer](/notes/building-a-stateful-process-in-elixir-without-genserver)
- [Part 2 — Correlated Request–Reply](/notes/building-distributed-systems-with-elixir-02-correlated-reque)
- [Part 3 — Process Monitoring](/notes/building-distributed-systems-in-elixir-part-3-process-monito)
- **Part 4 — Process Linking**
- [Part 5 — Supervisor From Scratch](/notes/building-distributed-systems-in-elixir-part-5-supervisor-fro)
- [Part 6 — Named Processes](/notes/building-distributed-systems-in-elixir-part-6-named-processe)
- [Part 7 — Worker Pool](/notes/building-distributed-systems-in-elixir-part-7-worker-pool)
- [Part 8 — Publish / Subscribe](/notes/building-distributed-systems-in-elixir-part-8-publish-subscr)
- [Part 9 — Backpressure](/notes/building-distributed-systems-in-elixir-part-9-backpressure)
