---
title: "Building Distributed Systems in Elixir: Part 9 — Backpressure"
date: '2026-09-28T15:00:02+01:00'
category: webclip
summary: 'Explains how unbounded BEAM mailboxes can grow into memory and GC problems, then shows stop-and-wait and demand-driven windowing as two ways to keep producers and consumers in balance.'
tags: ["elixir", "backpressure", "genstage", "distributed-systems"]
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

The article shows how an eager producer can overwhelm a slower consumer because BEAM mailboxes are unbounded and `send/2` does not wait for feedback. It uses small Elixir scripts to observe mailbox growth, memory use, and the risk of OOM crashes.

It then presents two flow-control strategies. Stop-and-wait keeps the mailbox at zero by making the producer wait for an acknowledgment after each item. Demand-driven windowing lets the consumer request batches, keeping memory bounded while preserving higher throughput. The article closes by tying this pattern to `GenStage`, `Broadway`, and Erlang socket backpressure.

## Reading notes

- The previous part built a publish/subscribe broker that decouples publishers from subscribers.
- `send/2` is non-blocking, so a fast producer can outpace a slow consumer without feedback.
- BEAM process mailboxes are private and unbounded FIFO queues by default.
- If messages pile up, memory grows, garbage collection gets heavier, and the VM can be killed by the OOM killer.
- `Process.info(pid, :message_queue_len)` and `Process.info(pid, :memory)` are used to inspect a process from outside it.
- In the first experiment, a producer sends 100 items quickly while a slow consumer processes them with `Process.sleep(15)`.
- After the producer finishes, the consumer still has a large backlog in its mailbox.
- Stop-and-wait uses a correlation reference and an acknowledgment message for each item.
- This keeps the consumer mailbox at zero, but the producer stays idle between items.
- Demand-driven flow control uses a consumer window and `{:ask, count}` messages to request work in batches.
- The producer tracks demand, dispatches batches up to the current credit, and sends `:stream_done` when its buffer is empty.
- The article compares uncoordinated push, stop-and-wait, and demand-driven windowing by control, mailbox risk, throughput, and use case.
- When upstream cannot be throttled, the article recommends bounded buffer policies such as dropping newest, dropping oldest, or rejecting at the boundary.
- It connects the hand-built demand pattern to `GenStage`, `Broadway`, and Erlang sockets with `{active, N}`.
