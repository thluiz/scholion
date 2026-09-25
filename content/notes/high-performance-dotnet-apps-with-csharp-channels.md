---
title: "Building High-Performance .NET Apps With C# Channels"
date: "2026-09-23T17:37:15+01:00"
category: webclip
has_commentary: false
summary: "A practical rundown of bounded vs. unbounded C# Channels, a bounded-channel background processor, and a write-back caching pattern for a shopping cart."
tags:
  - csharp
  - dotnet
  - concurrency
sources:
  - title: "Building High-Performance .NET Apps With C# Channels"
    url: "https://antondevtips.com/blog/building-high-performance-dotnet-apps-with-csharp-channels"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-08/antondevtips-com--high-performance-dotnet-apps-with-csharp-channels.md"
    kind: repo
---

C# Channels, from `System.Threading.Channels`, connect a Writer and a Reader across async threads without the coupling of wrapping a `Queue<T>` in a class. The article's central recommendation: default to a bounded channel, with a fixed capacity that makes the producer wait once full, and reach for unbounded only when the data rate is reliably low, since an unbounded channel can exhaust memory if the producer consistently outpaces the consumer.

A background processor pattern reads from `channel.Reader.ReadAllAsync()` in a loop inside a `BackgroundService`, which ends once the producer calls `.Writer.Complete()`. The post applies this to a write-back caching strategy for a shopping cart: writes land in the cache immediately and get pushed as an event onto a bounded channel, while a separate background service drains that channel and persists the cart to the database, giving fast writes during traffic spikes while the database catches up asynchronously.

## Reading notes

- Bounded channels make the producer wait once the channel is full, useful for backpressure when a consumer might lag behind a bursty producer.
- Unbounded channels never block the producer, which only makes sense when the data rate is reliably low; otherwise memory can run out.
- `BoundedChannelFullMode` controls what happens at capacity: `Wait` (the default and safest), `DropWrite`, `DropOldest`, or `DropNewest`. `DropOldest` fits cases where the newest event matters more than older ones.
- A `BackgroundService` reading `channel.Reader.ReadAllAsync(stoppingToken)` in a loop stops naturally once the producer calls `.Writer.Complete()`. Skipping that call leaves the consumer waiting forever.
- The write-back cache example writes a shopping cart to `HybridCache` immediately, then pushes a `ProductCartDispatchEvent` onto a bounded channel for a background service to persist to the database later, useful because only the state at checkout really matters.
- In production, a channel that's frequently full signals a consumer falling behind. The article's advice is to speed up processing, not simply raise the capacity.
