---
title: "Pesquisa Viva: Distributed Systems Patterns"
date: 2026-09-28T14:19:39+01:00
summary: "General patterns for building distributed systems, one pattern at a time, using krishnadaspc's Elixir series built on raw BEAM primitives as the main thread."
tags: ["pesquisa-viva", "distributed-systems", "elixir", "erlang", "beam", "software-architecture"]
status: "em andamento"
toc: true
---

## Method

(General rules: see `.claude/skills/research/SKILL.md`.)

- Organized by pattern, not by series part. Each pattern gathers the matching part of krishnadaspc's series and the related Scholion notes.
- The series builds each pattern from `spawn`, `send` and `receive`, without GenServer, GenStage or Broadway. When a direction reaches the OTP abstraction that formalizes the pattern, keep the two levels apart: what the series builds by hand vs. what the library provides.
- Most related notes are webclips (secondary summaries). Claims taken from them need the original article before getting ✓.

## Estado

- **Em foco**: none yet; the author will pick the first direction later.
- **Próximo**: choose which direction opens the research.

## Motivation

Starting point: the series *Building Distributed Systems in Elixir*, by krishnadaspc (pckrishnadas88) on dev.to, published between 2026-07-30 and 2026-09-22. Part 10 (Connecting Nodes) is announced but not yet published.

Links: [Part 9 — Backpressure](https://dev.to/pckrishnadas88/building-distributed-systems-in-elixir-part-9-backpressure-4o5i) · [author on dev.to](https://dev.to/pckrishnadas88)

## Open questions

## Directions / Readings

(To be confirmed with the author. Each one is exhausted before moving to the next.)

### 1. State in a process

Part 1: [Building a Stateful Process in Elixir Without GenServer](https://dev.to/pckrishnadas88/building-a-stateful-process-in-elixir-without-genserver-58eb) (2026-07-30). Related: [erlang](/notes/erlang), [elixir](/notes/elixir), [otp-open-telecom-platform](/notes/otp-open-telecom-platform), [thinking-in-actors-part-1](/notes/thinking-in-actors-part-1), [jonas-boner-actor-model-akka-reactive-programming-microservi](/notes/jonas-boner-actor-model-akka-reactive-programming-microservi). ?

### 2. Request–reply and service communication

Part 2: [Correlated Request–Reply](https://dev.to/pckrishnadas88/building-distributed-systems-with-elixir-02-correlated-request-reply-4b2a) (2026-08-06). Related: [must-know-service-communication-patterns](/notes/must-know-service-communication-patterns), [cross-app-communication-with-rpc-in-elixir](/notes/cross-app-communication-with-rpc-in-elixir), [retries-have-an-evil-twin-duplicates](/notes/retries-have-an-evil-twin-duplicates). ?

### 3. Failure detection

Part 3: [Process Monitoring](https://dev.to/pckrishnadas88/building-distributed-systems-in-elixir-part-3-process-monitoring-5b5p) (2026-08-13). Part 4: [Process Linking](https://dev.to/pckrishnadas88/building-distributed-systems-in-elixir-part-4-process-linking-okb) (2026-08-14). Related: [heartbeats-in-distributed-systems](/notes/heartbeats-in-distributed-systems). ?

### 4. Supervision and resiliency

Part 5: [Supervisor From Scratch](https://dev.to/pckrishnadas88/building-distributed-systems-in-elixir-part-5-supervisor-from-scratch-32mh) (2026-08-18). Related: [must-known-resiliency-patterns-for-distributed-systems](/notes/must-known-resiliency-patterns-for-distributed-systems), [building-robust-distributed-systems](/notes/building-robust-distributed-systems), [http-best-practices-using-asp-net-core-and-polly](/notes/http-best-practices-using-asp-net-core-and-polly). ?

### 5. Naming and discovery

Part 6: [Named Processes](https://dev.to/pckrishnadas88/building-distributed-systems-in-elixir-part-6-named-processes-l3) (2026-08-19). ?

### 6. Worker pools

Part 7: [Worker Pool](https://dev.to/pckrishnadas88/building-distributed-systems-in-elixir-part-7-worker-pool-f23) (2026-08-24). Related: [dont-ignore-thread-safety-design-for-concurrency-from-day-on](/notes/dont-ignore-thread-safety-design-for-concurrency-from-day-on). ?

### 7. Publish/subscribe and events

Part 8: [Publish / Subscribe](https://dev.to/pckrishnadas88/building-distributed-systems-in-elixir-part-8-publish-subscribe-cl3) (2026-09-14). Related: [distributed-pubsub-in-elixir](/notes/distributed-pubsub-in-elixir), [understanding-concepts-in-event-driven-architectures](/notes/understanding-concepts-in-event-driven-architectures), [the-dual-nature-of-events-in-event-driven-architecture](/notes/the-dual-nature-of-events-in-event-driven-architecture), [patterns-best-practices-event-driven-systems](/notes/patterns-best-practices-event-driven-systems), [serverless-event-driven-systems](/notes/serverless-event-driven-systems). ?

### 8. Backpressure

Part 9: [Backpressure](https://dev.to/pckrishnadas88/building-distributed-systems-in-elixir-part-9-backpressure-4o5i) (2026-09-22). ⚠ From a first read, not yet checked line by line: three experiments, going from uncoordinated push (the consumer's mailbox grows without bound), to stop-and-wait with acknowledgements, to a consumer-driven demand window; mentions GenStage and Broadway as the production form of the demand protocol. Scholion webclip: [building-distributed-systems-in-elixir-part-9-backpressure](/notes/building-distributed-systems-in-elixir-part-9-backpressure). Related: [elixir-makes-you-make-good-decisions](/notes/elixir-makes-you-make-good-decisions), [notes-on-distributed-systems-for-young-bloods](/notes/notes-on-distributed-systems-for-young-bloods), [high-performance-dotnet-apps-with-csharp-channels](/notes/high-performance-dotnet-apps-with-csharp-channels). ?

### 9. Clustering and consistency

Part 10 (Connecting Nodes), announced. Related: [cap-theorem-for-databases-consistency-availability-partition](/notes/cap-theorem-for-databases-consistency-availability-partition), [designing-data-intensive-applications-book](/notes/designing-data-intensive-applications-book), [rick-reed-whatsapp-scaling-erlang](/notes/rick-reed-whatsapp-scaling-erlang). ?

## Related Scholion notes

General overviews, not tied to a single direction:

- [8-must-know-distributed-system-design-patterns](/notes/8-must-know-distributed-system-design-patterns) — patterns for failure handling, read/write separation, partitioning and coordination.
- [15-must-know-elements-of-system-design](/notes/15-must-know-elements-of-system-design) — system design elements grouped by area.
- [system-design-tips](/notes/system-design-tips) — caches, queues, sharding and replication, with when to use each.
- [review-is-designing-data-intensive-applications-worth-it](/notes/review-is-designing-data-intensive-applications-worth-it) — review of Kleppmann's book.
- [death-by-a-thousand-microservices](/notes/death-by-a-thousand-microservices) — the cost of distributing without need.

Notes tied to a direction are listed inside it above.

## Extracted notes
