---
url: "https://antondevtips.com/blog/building-high-performance-dotnet-apps-with-csharp-channels"
captured_at: "2025-08-11T13:58:21+01:00"
title: "Building High-Performance .NET Apps With C# Channels"
domain: "antondevtips.com"
---

# Building High-Performance .NET Apps With C# Channels

> ## Excerpt
> Learn how to build concurrent applications in .NET and ASP.NET Core with C# Channels. Learn the differences between bounded and unbounded channels in C#, create robust background processing. Implement Write Back Caching Strategy with Channels.

---
Building reliable, scalable, and high-performance .NET applications often comes down to how you handle concurrency and data processing. C# Channels bring a new, modern approach for building safe, asynchronous, and high-throughput pipelines in .NET.

Channels allow you to create in-memory producer-consumer queues that scale naturally across async workflows and background services. However, a crucial architectural decision is choosing between bounded and unbounded channels.

## What are C# Channels?

Before Channels, developers used constructs such as `Queue<T>`, `ConcurrentQueue<T>`, or `BlockingCollection<T>`, encapsulated into classes to manage data flows — with a significant drawback: tight code coupling. C# Channels implement a producer-consumer pattern instead: one class produces data and the other consumes it, without knowing about each other.

Channels come from the `System.Threading.Channels` namespace. A channel has two parts: a Writer, which pushes data into the channel, and a Reader, which pulls data out. Both reading and writing can occur on different threads, and channels ensure thread safety, letting you use async code everywhere without blocking threads or locking.

## Bounded vs. Unbounded Channels

A **bounded** channel has a fixed maximum capacity set at creation. If the producer tries to add more items after the channel is full, it waits until there is space. Use it when you want to limit memory usage and prevent overload, when the consumer is sometimes slower than the producer, or when you need backpressure to avoid flooding the system.

An **unbounded** channel has no fixed limit — the producer can keep adding items as fast as it wants, and the channel grows until memory runs out. Use it only when the producer will never outpace the consumer for long, for simple cases where flow control isn't a problem, or when the stream is small and steady.

Unbounded channels are simple but risky under high load — if the producer writes faster than the consumer reads, memory can run out. In most real-world .NET services, bounded channels are the safer default.

## Background Processor with a Bounded Channel

A common pattern registers a bounded channel as a singleton (e.g. `Channel.CreateBounded<string>(new BoundedChannelOptions(100) { FullMode = BoundedChannelFullMode.Wait })`) and a `BackgroundService` that reads from `channel.Reader.ReadAllAsync(stoppingToken)` in a loop, processing each message. `ReadAllAsync` waits for new messages and ends once the writer calls `.Writer.Complete()`. Because the channel is bounded to 100, a producer writing faster than the consumer can process pauses until a slot frees up, keeping memory usage under control.

`BoundedChannelFullMode` options when the channel is full: `Wait` (the writer waits until space is available — most common, safest), `DropWrite` (new items are dropped), `DropOldest` (the oldest item is removed to make space), `DropNewest` (the newest item is dropped instead). Use `Wait` for most background tasks; use `DropWrite`/`DropOldest` when losing a few messages is acceptable, and `DropOldest` specifically when the latest event matters more than older ones.

## Real-World Application with Channels

Channels can implement a Write-Back Caching Strategy: data is written to the cache first, and the cache asynchronously writes back to the database after a condition or interval — useful in write-intensive scenarios like an online shopping cart, where only the final state at checkout really matters. A `WriteBackCacheProductCartService.AddAsync` method builds the cart, writes it to a `HybridCache`, and publishes a `ProductCartDispatchEvent` onto a bounded channel. A `WriteBackCacheBackgroundService` reads dispatch events from the channel and persists the cart to the database (insert if new, update if it already exists). The pattern speeds up writes significantly but requires robust conflict resolution and failure handling — and reliable replication or backup — to guarantee the cart state is never lost if the cache fails.

## Best Practices and Tips for Working with Channels

1. Prefer bounded channels for safety — set the capacity to cover typical bursts without being oversized; use unbounded only when the data rate is reliably low.
2. Always call `.Writer.Complete()` when the producer is done — without it, the consumer's `ReadAllAsync` loop never ends.
3. Always `await` write and read operations to avoid blocking threads and keep the app responsive.
4. Pass a `CancellationToken` to reads and writes so processing can stop cleanly on shutdown or cancellation.
5. Avoid too many producers or consumers on the same channel — stick to a single producer and consumer where possible for easier reasoning, even though channels do support multiple readers and writers.
6. Monitor channel usage in production — a channel that's frequently full signals consumers that are too slow, calling for faster processing or a larger capacity.
7. Choose the right `FullMode` deliberately for bounded channels, based on whether dropped messages are acceptable.
