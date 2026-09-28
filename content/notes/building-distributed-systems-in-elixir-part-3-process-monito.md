---
title: "Building Distributed Systems in Elixir: Part 3 — Process Monitoring"
date: '2026-09-28T15:10:45+01:00'
category: webclip
summary: 'Shows how BEAM process monitoring uses Process.monitor/1 to receive :DOWN messages when a worker stops or crashes, without polling, GenServer, or Supervisor.'
tags: ["elixir", "beam", "process-monitoring", "distributed-systems"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Building Distributed Systems in Elixir: Part 3 — Process Monitoring"
    url: "https://dev.to/pckrishnadas88/building-distributed-systems-in-elixir-part-3-process-monitoring-5b5p"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--building-distributed-systems-in-elixir-part-3-process-monito.md"
    kind: repo
---

The article explains process monitoring as the BEAM primitive for learning when a process terminates. Instead of repeatedly checking Process.alive?/1, a monitoring process calls Process.monitor/1 and receives a {:DOWN, ref, :process, pid, reason} message when the worker exits normally or crashes. The examples show how to match the monitor reference and worker PID, how to track several workers at once, and how to remove finished monitors from a map until all workers have terminated.

## Reading notes

- The series has already built a stateful process and correlated request–reply using references.
- The problem is knowing when a communicating process dies, whether it stops normally, crashes, or terminates for another reason.
- Polling with Process.alive?/1 is presented as the wrong approach.
- Process.monitor/1 makes the calling process the monitoring process and returns a unique reference.
- When the monitored process terminates, the BEAM sends {:DOWN, ref, :process, pid, reason} to the monitoring process.
- The worker example handles :work, :stop, and :crash messages.
- :stop ends the function without another loop call, so the process terminates normally.
- A normal exit produces a :DOWN message with reason :normal.
- A crash also produces a :DOWN message, and the monitoring process stays alive.
- The pin operator ^ is used to match the specific reference and worker being watched.
- Multiple workers can be monitored at the same time by storing references in a map.
- A recursive wait_for_workers/1 function receives :DOWN messages, logs each termination, and removes the corresponding monitor until none remain.
- The order of termination is not guaranteed because the workers run concurrently.
- The article contrasts monitoring with polling and says monitoring fits the BEAM message-passing model.
- The next part will cover spawn_link/1 and failure propagation between linked processes.

## Series

*Building Distributed Systems in Elixir*, by krishnadaspc. Research: [Distributed Systems Patterns](/research/distributed-systems-patterns).

- [Part 1 — Stateful Process Without GenServer](/notes/building-a-stateful-process-in-elixir-without-genserver)
- [Part 2 — Correlated Request–Reply](/notes/building-distributed-systems-with-elixir-02-correlated-reque)
- **Part 3 — Process Monitoring**
- [Part 4 — Process Linking](/notes/building-distributed-systems-in-elixir-part-4-process-linkin)
- [Part 5 — Supervisor From Scratch](/notes/building-distributed-systems-in-elixir-part-5-supervisor-fro)
- [Part 6 — Named Processes](/notes/building-distributed-systems-in-elixir-part-6-named-processe)
- [Part 7 — Worker Pool](/notes/building-distributed-systems-in-elixir-part-7-worker-pool)
- [Part 8 — Publish / Subscribe](/notes/building-distributed-systems-in-elixir-part-8-publish-subscr)
- [Part 9 — Backpressure](/notes/building-distributed-systems-in-elixir-part-9-backpressure)
