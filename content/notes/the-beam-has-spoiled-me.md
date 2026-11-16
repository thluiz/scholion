---
title: "The BEAM has Spoiled Me"
date: '2026-11-16T02:12:09+00:00'
category: webclip
summary: 'Greg Vaughn says BEAM-style fault tolerance reduced his fear of crashes, made processes and idempotency part of his default Elixir practice, and led him to think in systems rather than web apps.'
tags: ["beam", "elixir", "fault-tolerance", "distributed-systems"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The BEAM has Spoiled Me"
    url: "https://gvaughn.github.io/2020/08/08/beam_spoiled_me.html"
    kind: repo
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/gvaughn-github-io--the-beam-has-spoiled-me.md"
    kind: repo
---

Greg Vaughn says focusing his career on Elixir changed how he wants to build software. BEAM-style fault tolerance lowers friction and fear, so he now thinks in systems, not just web applications.

## Reading notes

- BEAM fault tolerance comes from isolated processes and supervisory processes that are told when a process dies.
- Concurrency is presented as a consequence of fault tolerance, not the main point.
- “Let It Crash” means accepting that errors will happen and containing their impact.
- He uses processes to contain possible damage even when he does not need concurrency.
- He uses supervision trees and durable work queues to recover from small process crashes.
- He prefers upserts over inserts so logic can be retried safely and stay idempotent.
- Fault tolerance changes how he thinks about test coverage enforcement, static types, and code reviews because those tools also add friction.
- BEAM and Elixir renewed his interest in software development through distributed systems ideas.
- He sees BEAM processes as lightweight building blocks for larger systems.
- He argues that teams can think of each process as a logical microservice without separate deployment, JSON serialization, containers, orchestration, or distributed logging.
- He describes Elixir and BEAM as a game changer that made him more fearless about building systems.
