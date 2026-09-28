---
title: "Building Distributed Systems in Elixir: Part 1 - Building a Stateful Process in Elixir Without GenServer"
date: '2026-09-28T15:10:00+01:00'
category: webclip
summary: 'The article shows how a counter can be built as a BEAM process with private state, message passing, and a recursive receive loop, then contrasts that core model with what GenServer adds.'
tags: ["elixir", "beam", "genserver", "message-passing"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Building Distributed Systems in Elixir: Part 1 - Building a Stateful Process in Elixir Without GenServer"
    url: "https://dev.to/pckrishnadas88/building-a-stateful-process-in-elixir-without-genserver-58eb"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--building-a-stateful-process-in-elixir-without-genserver.md"
    kind: repo
---

The article explains a minimal stateful server in Elixir by turning a counter into a process that owns its private state. Clients do not read that state directly; they send requests with `send/2`, wait for replies with `receive`, and rely on the process to update and return values.

## Reading notes

- A stateful server is described as a process with private state that receives messages, updates state, sends replies, and waits for the next message.
- The example uses only `spawn/1`, `send/2`, `receive`, and recursion, without `GenServer`, `Agent`, or other OTP behaviours.
- The counter is modeled as a process because BEAM processes do not share memory.
- The protocol uses `{:get, caller_pid}`, `{:increment, caller_pid}`, and `:stop`, and replies with `{:counter_value, value}`.
- `start/1` calls `spawn/1` and begins the recursive `loop/1` with the initial value as private state.
- `get/1` sends a request and then waits for a new reply message; it does not read the message it sent.
- `increment/1` follows the same request-reply pattern, but the counter process performs the state update.
- The receive loop matches incoming messages, handles each operation, and calls `loop/1` again with the next state.
- Because the process handles one mailbox message at a time, requests are serialized and clients do not modify the state concurrently.
- `GenServer` is presented as a higher-level abstraction that adds request handling, correlation, timeouts, monitoring, supervision, debugging support, system messages, and consistent APIs.

## Series

*Building Distributed Systems in Elixir*, by krishnadaspc. Research: [Distributed Systems Patterns](/research/distributed-systems-patterns).

- **Part 1 — Stateful Process Without GenServer**
- [Part 2 — Correlated Request–Reply](/notes/building-distributed-systems-with-elixir-02-correlated-reque)
- [Part 3 — Process Monitoring](/notes/building-distributed-systems-in-elixir-part-3-process-monito)
- [Part 4 — Process Linking](/notes/building-distributed-systems-in-elixir-part-4-process-linkin)
- [Part 5 — Supervisor From Scratch](/notes/building-distributed-systems-in-elixir-part-5-supervisor-fro)
- [Part 6 — Named Processes](/notes/building-distributed-systems-in-elixir-part-6-named-processe)
- [Part 7 — Worker Pool](/notes/building-distributed-systems-in-elixir-part-7-worker-pool)
- [Part 8 — Publish / Subscribe](/notes/building-distributed-systems-in-elixir-part-8-publish-subscr)
- [Part 9 — Backpressure](/notes/building-distributed-systems-in-elixir-part-9-backpressure)
