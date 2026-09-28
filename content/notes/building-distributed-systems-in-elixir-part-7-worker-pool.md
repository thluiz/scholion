---
title: "Building Distributed Systems in Elixir: Part 7 — Worker Pool"
date: '2026-09-28T15:12:26+01:00'
category: webclip
summary: 'The article builds a worker pool from raw Elixir process primitives to keep concurrency bounded, queue excess jobs, and let workers pull new work only when they become available.'
tags: ["elixir", "worker-pool", "bounded-concurrency", "backpressure"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Building Distributed Systems in Elixir: Part 7 — Worker Pool"
    url: "https://dev.to/pckrishnadas88/building-distributed-systems-in-elixir-part-7-worker-pool-f23"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--building-distributed-systems-in-elixir-part-7-worker-pool.md"
    kind: repo
---

The article builds a worker pool from scratch with `spawn/1`, `send/2`, and `receive/1`. A coordinator process keeps the pool state, tracks idle workers, buffers waiting jobs, and stops the workers when all jobs are done. The design is meant to show bounded concurrency and backpressure before using higher-level abstractions.

## Reading notes

- A single registered process name points to one running process, so the article turns to a pool when many jobs must run without sending everything to one worker or spawning an unbounded number of processes.
- The pool has three parts: a parent that starts it and waits, a coordinator that manages state, and worker processes that execute jobs and report back.
- Each worker announces that it is available when it starts, then waits for work, processes a job, sends the result together with renewed availability, and stops when it receives `:stop`.
- The coordinator keeps `workers`, `available_workers`, `waiting_jobs`, `completed_jobs`, and `total_jobs` in its recursive loop.
- Job distribution is demand-driven: the coordinator assigns work only to workers that have explicitly sent `:available`.
- The article says this model lets fast workers handle more jobs, slow workers handle fewer, and keeps concurrency within the worker count.
- When `completed_jobs == total_jobs`, the coordinator sends `:stop` to every worker and notifies the parent that the pool has finished.
- The article notes limits of the raw version: no failure handling or supervision, in-memory buffering only, and static sizing.
- It points to OTP libraries such as `NimblePool`, `Poolboy`, and `Broadway` for production use.

## Series

*Building Distributed Systems in Elixir*, by krishnadaspc. Research: [Distributed Systems Patterns](/research/distributed-systems-patterns).

- [Part 1 — Stateful Process Without GenServer](/notes/building-a-stateful-process-in-elixir-without-genserver)
- [Part 2 — Correlated Request–Reply](/notes/building-distributed-systems-with-elixir-02-correlated-reque)
- [Part 3 — Process Monitoring](/notes/building-distributed-systems-in-elixir-part-3-process-monito)
- [Part 4 — Process Linking](/notes/building-distributed-systems-in-elixir-part-4-process-linkin)
- [Part 5 — Supervisor From Scratch](/notes/building-distributed-systems-in-elixir-part-5-supervisor-fro)
- [Part 6 — Named Processes](/notes/building-distributed-systems-in-elixir-part-6-named-processe)
- **Part 7 — Worker Pool**
- [Part 8 — Publish / Subscribe](/notes/building-distributed-systems-in-elixir-part-8-publish-subscr)
- [Part 9 — Backpressure](/notes/building-distributed-systems-in-elixir-part-9-backpressure)
