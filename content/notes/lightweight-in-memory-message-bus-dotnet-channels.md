---
title: "Lightweight In-Memory Message Bus Using .NET Channels"
date: '2025-04-21T15:43:24+00:00'
category: webclip
summary: 'Guide to building a lightweight in-memory message bus with .NET Channels and MediatR, covering abstractions, event bus, background processing, usage, and limitations.'
tags: ["dotnet", "messaging", "in-memory-bus", "architecture"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Lightweight In-Memory Message Bus Using .NET Channels"
    url: "https://milanjovanovic.tech/blog/lightweight-in-memory-message-bus-using-dotnet-channels"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/milanjovanovic-tech--lightweight-in-memory-message-bus-dotnet-channels.md"
    kind: repo
---

An in-memory message bus enables low-latency, non-blocking communication between loosely coupled components in the same process, at the risk of losing messages if the process crashes and without supporting distributed scenarios. The article shows how to build such a bus using System.Threading.Channels, MediatR, and ASP.NET Core background services, from defining abstractions to publishing and consuming integration events, and outlines possible robustness improvements.

## Reading notes

- An in-memory message bus passes messages entirely in memory between loosely coupled components within a single process, providing very low latency and asynchronous, non-blocking communication.
- It is useful when high performance and low latency are critical, for example in a modular monolith where modules communicate with integration events and can later switch to a distributed bus when extracting services.
- Main drawbacks are the potential loss of messages if the application process goes down and the fact that it only works inside one process, so it does not help in distributed systems.
- The design is based on two main abstractions from the client perspective: an `IEventBus` for publishing messages and a message handler abstraction based on MediatR notifications.
- `IEventBus` exposes a generic `PublishAsync` method constrained to `IIntegrationEvent`, which represents the integration events that can be published.
- `IIntegrationEvent` inherits from MediatR's `INotification` and includes an identifier, which makes it easy to define handlers via `INotificationHandler<T>` and to track event execution.
- The abstract `IntegrationEvent` record provides a base type for concrete integration events, encapsulating the event identifier.
- System.Threading.Channels is used to implement a producer/consumer pattern where producers and consumers asynchronously interact via channels in memory.
- A key motivation for using .NET Channels is their performance, since they are fully in-memory; the trade-off is that messages can be lost if the application crashes.
- `InMemoryMessageQueue` wraps an unbounded channel of `IIntegrationEvent` created via `Channel.CreateUnbounded<IIntegrationEvent>()`, allowing multiple readers and writers.
- This queue exposes `ChannelReader<IIntegrationEvent>` and `ChannelWriter<IIntegrationEvent>` properties for consuming and publishing messages.
- The `InMemoryMessageQueue` must be registered as a singleton in dependency injection so all producers and consumers share the same channel instance.
- `EventBus` implements `IEventBus` by taking an `InMemoryMessageQueue` dependency and using its `Writer` to write events asynchronously to the channel.
- `EventBus` is registered as a singleton because it is stateless and only writes messages to the underlying queue.
- To consume events, a background job is implemented by deriving from `BackgroundService` and using the channel reader to process messages continuously.
- `IntegrationEventProcessorJob` depends on `InMemoryMessageQueue` for reading, `IServiceScopeFactory` for creating scopes, and `ILogger` for logging errors.
- In `ExecuteAsync`, the job iterates `queue.Reader.ReadAllAsync(stoppingToken)` as an `IAsyncEnumerable`, consuming each `IIntegrationEvent` asynchronously.
- For each event, the job creates a new service scope, resolves MediatR's `IPublisher` from the scope, and calls `Publish` to dispatch the event to its handlers.
- A custom scope is required so that handlers can safely use scoped services while the background job itself is registered as a singleton hosted service.
- Exceptions during event processing are caught, and the logger records an error along with the integration event identifier.
- The background job is registered using `AddHostedService<IntegrationEventProcessorJob>()` so it starts with the application.
- Usage is illustrated with a `RegisterUserCommandHandler` that injects `IUserRepository` and `IEventBus` and first registers a user, then publishes a `UserRegisteredIntegrationEvent`.
- Publishing via `eventBus.PublishAsync` writes the integration event to the channel and returns immediately, which enables non-blocking publication and can improve performance.
- On the consumer side, a `UserRegisteredIntegrationEventHandler` implements `INotificationHandler<UserRegisteredIntegrationEvent>` to handle the event asynchronously when it is published by the background job.
- When the background processor reads `UserRegisteredIntegrationEvent` from the channel and publishes it via MediatR, the corresponding handler is executed.
- The article suggests resilience improvements such as adding retry logic when exceptions occur, to increase reliability of event processing.
- It also highlights the need to consider idempotency and references the idempotent consumer pattern to handle possible duplicate messages.
- A dead letter queue is proposed as a persistent store for messages that repeatedly fail, enabling later troubleshooting of problematic events.
- The implementation focuses on a single-process use case; for scenarios that require stronger reliability or cross-process communication, a dedicated message broker is recommended.
