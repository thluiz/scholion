---
title: "Building Distributed Systems in Elixir: Part 9 — Backpressure"
date: '2026-09-28T15:13:04+01:00'
category: webclip
summary: 'The article shows how unbounded BEAM mailboxes can grow into OOM risk, then compares stop-and-wait acknowledgment with demand-driven windowing as two ways to keep producer and consumer in balance.'
tags: ["backpressure", "elixir", "beam-mailbox", "distributed-systems-patterns"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Building Distributed Systems in Elixir: Part 9 — Backpressure"
    url: "https://dev.to/pckrishnadas88/building-distributed-systems-in-elixir-part-9-backpressure-4o5i"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--building-distributed-systems-in-elixir-part-9-backpressure.md"
    kind: repo
---

The article explains backpressure as the missing control mechanism when a fast Elixir producer outpaces a slower consumer. It uses raw process primitives to show how unbounded mailboxes grow, why that can lead to memory blowups, and how flow control keeps systems from crashing.

## Reading notes

- Every process has a private heap and mailbox, and `send/2` does not wait for the receiver, so messages can accumulate faster than they are processed.
- The first experiment shows a slow consumer with `Process.sleep(15)` and a fast producer filling the mailbox, with `Process.info/2` used to inspect queue length and memory.
- The article links sustained mailbox growth to heap expansion, garbage collection overhead, and eventual OOM termination of the BEAM process.
- Stop-and-wait flow control uses a correlation reference and an acknowledgment message so the producer sends one item at a time and waits for `{:ack, ref}` before continuing.
- This keeps the consumer mailbox at zero or near zero, but it also reduces concurrency and adds round-trip latency.
- Demand-driven windowing shifts control to the consumer, which asks for a fixed number of items and replenishes demand after each batch.
- The producer keeps a demand counter, sends batches up to the available demand, and the consumer processes each batch before asking for more.
- The demand model keeps mailbox size bounded by the window and preserves throughput by pipelining work in batches.
- The article compares uncoordinated push, stop-and-wait, and demand-driven flow control in terms of control, mailbox risk, throughput, and use case.
- When upstream sources cannot be throttled, the article says a bounded buffer policy is needed, such as dropping newest, dropping oldest, or rejecting at the boundary.
- It identifies `GenStage`, `Broadway`, and Erlang socket active modes as production equivalents of the demand-driven pattern.
- The key takeaways are that the BEAM mailbox is unbounded, `Process.info/2` can monitor queue length externally, stop-and-wait protects memory but hurts latency, and demand windows keep throughput high while bounding backlog.

## Series

*Building Distributed Systems in Elixir*, by krishnadaspc. Research: [Distributed Systems Patterns](/research/distributed-systems-patterns).

- [Part 1 — Stateful Process Without GenServer](/notes/building-a-stateful-process-in-elixir-without-genserver)
- [Part 2 — Correlated Request–Reply](/notes/building-distributed-systems-with-elixir-02-correlated-reque)
- [Part 3 — Process Monitoring](/notes/building-distributed-systems-in-elixir-part-3-process-monito)
- [Part 4 — Process Linking](/notes/building-distributed-systems-in-elixir-part-4-process-linkin)
- [Part 5 — Supervisor From Scratch](/notes/building-distributed-systems-in-elixir-part-5-supervisor-fro)
- [Part 6 — Named Processes](/notes/building-distributed-systems-in-elixir-part-6-named-processe)
- [Part 7 — Worker Pool](/notes/building-distributed-systems-in-elixir-part-7-worker-pool)
- [Part 8 — Publish / Subscribe](/notes/building-distributed-systems-in-elixir-part-8-publish-subscr)
- **Part 9 — Backpressure**
