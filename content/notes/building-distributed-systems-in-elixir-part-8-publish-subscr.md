---
title: "Building Distributed Systems in Elixir: Part 8 — Publish / Subscribe"
date: '2026-09-28T15:12:45+01:00'
category: webclip
summary: 'The article builds a Pub/Sub broker in Elixir with raw processes, showing how topics, fan-out, subscriptions, and Process.monitor/1 avoid tight coupling and clean up dead subscribers.'
tags: ["elixir", "publish-subscribe", "distributed-systems", "process-monitoring"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Building Distributed Systems in Elixir: Part 8 — Publish / Subscribe"
    url: "https://dev.to/pckrishnadas88/building-distributed-systems-in-elixir-part-8-publish-subscribe-cl3"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--building-distributed-systems-in-elixir-part-8-publish-subscr.md"
    kind: repo
---

The article shows how point-to-point messaging becomes brittle when one event must reach several independent processes. It then builds a Pub/Sub broker from raw BEAM primitives, with a broker that routes messages by topic, subscribers that handle broadcasts in their own mailboxes, and monitoring to remove dead PIDs.

## Reading notes

- A worker-pool setup is contrasted with pub/sub to show that 1-to-1 coordination does not fit multi-recipient events.
- Directly looping over recipient PIDs creates spatial coupling, temporal coupling, and a wider failure radius.
- The broker keeps two pieces of state: topic-to-subscriber lists and PID-to-monitor references.
- `subscribe/3` and `unsubscribe/3` use correlated request-reply so the caller knows the broker has updated its state.
- `publish/3` is fire-and-forget, and fan-out uses `Enum.each/2` to send the broadcast to every PID for a topic.
- `Process.monitor/1` lets the broker receive `{:DOWN, ...}` messages and prune dead subscribers automatically.
- `Process.demonitor(ref, [:flush])` is used during unsubscribe so monitor references do not leak.
- The demo script registers Alice, Bob, and Charlie on overlapping topics, publishes to several topics, unsubscribes Bob, crashes Charlie, and shows the broker pruning him.
- The article notes that broadcasts to large binaries are memory-efficient on the BEAM because refc binaries are shared.
- It warns that unbounded mailboxes create a slow-consumer problem and lead to missing backpressure.
- Real-world Elixir alternatives mentioned are `Registry`, `Phoenix.PubSub`, and `:pg`.
- The next part of the series is Backpressure, focused on slow consumers and demand-driven flow control.

## Series

*Building Distributed Systems in Elixir*, by krishnadaspc. Research: [Distributed Systems Patterns](/research/distributed-systems-patterns).

- [Part 1 — Stateful Process Without GenServer](/notes/building-a-stateful-process-in-elixir-without-genserver)
- [Part 2 — Correlated Request–Reply](/notes/building-distributed-systems-with-elixir-02-correlated-reque)
- [Part 3 — Process Monitoring](/notes/building-distributed-systems-in-elixir-part-3-process-monito)
- [Part 4 — Process Linking](/notes/building-distributed-systems-in-elixir-part-4-process-linkin)
- [Part 5 — Supervisor From Scratch](/notes/building-distributed-systems-in-elixir-part-5-supervisor-fro)
- [Part 6 — Named Processes](/notes/building-distributed-systems-in-elixir-part-6-named-processe)
- [Part 7 — Worker Pool](/notes/building-distributed-systems-in-elixir-part-7-worker-pool)
- **Part 8 — Publish / Subscribe**
- [Part 9 — Backpressure](/notes/building-distributed-systems-in-elixir-part-9-backpressure)
