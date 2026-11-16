---
title: "Elixir: a few things about GenStage I wish I knew some time ago"
date: '2020-07-05T14:10:34+00:00'
category: webclip
summary: 'The article separates GenStage use into owned sources, where demand is fetched and controlled upstream, and pushed sources, where backpressure matters because event volume is unpredictable.'
tags: ["elixir", "genstage", "backpressure", "demand-handling"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Elixir: a few things about GenStage I wish I knew some time ago | by Andrey Chernykh | Medium"
    url: "https://medium.com/@andreichernykh/elixir-a-few-things-about-genstage-id-wish-to-knew-some-time-ago-b826ca7d48ba"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/medium-com--elixir-a-few-things-about-genstage-i-wish-i-knew-some-time-a.md"
    kind: repo
---

The article groups GenStage use into two cases. When you own the event source, the producer fetches only what consumers demand, which helps with load control and parallel or distributed processing. When you do not own the source, the producer receives an unpredictable stream and the buffer becomes the backpressure mechanism.

It also warns that consumer demand is tied to `max_demand - min_demand`, so a consumer may wait with partial batches before it processes anything. Because of that, a producer should keep track of unmet demand and pending events, or some events can remain hanging. It also mentions dynamic consumer spawning and the built-in dispatcher options.

## Reading notes

- GenStage stages exchange data, acting as producers when sending and consumers when receiving.
- One usage pattern is when you own the event source and fetch events only to satisfy consumer demand.
- In that pattern, GenStage can help with parallel or distributed data handling.
- Another usage pattern is when you do not own the source and must handle unpredictable incoming events.
- In that pattern, the producer uses its buffer as a backpressure mechanism.
- In the demand-handling case, the producer should store unsatisfied demand and leftover events from earlier handling.
- A consumer asks for more work when its queue reaches `max_demand - min_demand`, not at `min_demand` itself.
- A consumer may wait for more events before it starts processing a partial batch.
- If the producer only listens for incoming demand, some events can remain hanging in a consumer.
- Consumers can be started dynamically from a producer setup.
- The article mentions three predefined dispatchers: `DemandDispatcher`, `BroadcastDispatcher`, and `PartitionDispatcher`.
