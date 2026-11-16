---
title: "Elixir: The power of truly distributed systems"
date: '2020-08-26T19:31:10+00:00'
category: webclip
summary: 'The text argues that Elixir fits a concurrent, process-based approach to scaling because it supports low-latency, fault-tolerant, distributed apps with simple supervision and visible runtime behavior.'
tags: ["elixir", "distributed-systems", "concurrency", "scalability"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Elixir: The power of truly distributed systems | by Eduardo Pereira | Medium"
    url: "https://medium.com/unbabel/elixir-the-power-of-truly-distributed-systems-c4c79ed9f97d"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/medium-com--elixir-the-power-of-truly-distributed-systems.md"
    kind: repo
---

The text presents Elixir as a language and mindset for building scalable systems. It ties scaling problems to process-based design, message passing, immutability, supervision, and runtime visibility, then links those ideas to stable memory use, low latency, and fault tolerance.

## Reading notes

- Most startups begin by focusing on product-market fit and a first version, but growth eventually makes scaling unavoidable.
- Small scaling steps can be handled by adding infrastructure, tuning queries, and optimizing algorithms, but that stops being enough when demand grows.
- The text frames Elixir as a fit for this stage because it supports low-latency, scalable, fault-tolerant, and distributed applications.
- OTP is described as a set of building blocks and design principles, including a process-based architecture.
- In Elixir, code runs inside lightweight BEAM processes that can exist in very large numbers and use little CPU and memory.
- Processes are isolated, do not share state, and communicate through messages, which supports concurrency.
- Immutability is presented as another reason Elixir avoids awkward state handling.
- Supervisors monitor processes, terminate failed ones, and restart them to restore initial state.
- The text argues that concurrent thinking changes how problems are approached, favoring many small workers instead of one large server.
- In the example, one process monitors a table and launches many processes, each responsible for one row.
- A GenServer is used as a simple micro web server that initializes state, handles work messages, updates a record, and schedules itself again.
- The code is described as clean, simple, functional, and suitable for thousands of processes.
- The runtime can be monitored through process trees, memory usage, IO, and telemetry, which makes behavior visible during development.
- The stated result is boring telemetry: 20 ms average response time, stable low memory usage, and 2% peak CPU use.
- The author presents this as a move from reactive fixing to proactive building.
