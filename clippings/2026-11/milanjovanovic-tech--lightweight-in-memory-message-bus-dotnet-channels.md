---
url: "https://milanjovanovic.tech/blog/lightweight-in-memory-message-bus-using-dotnet-channels"
captured_at: "2026-11-18T11:03:21+00:00"
title: "Lightweight In-Memory Message Bus Using .NET Channels"
domain: "milanjovanovic-tech"
---

An in-memory message bus passes messages between loosely coupled components inside the same process, giving you low latency and non-blocking communication. You build one with `System.Threading.Channels`: an unbounded channel holds the integration events, an `IEventBus` writes to it, and a `BackgroundService` reads and dispatches them to handlers. Messages are lost if the process goes down.

Suppose you're building a [**modular monolith**](https://milanjovanovic.tech/blog/modular-monolith-architecture-dotnet), a type of software architecture where different components are organized into loosely coupled modules. Or you might need to process data asynchronously. You'll need a tool or service that allows you to implement this.

Messaging plays a crucial role in modern software architecture, enabling communication and coordination between loosely coupled components.

An in-memory message bus is particularly useful when high performance and low latency are critical requirements.

In today's issue, we will:

*   Create the required messaging abstractions
*   Build an in-memory message bus using channels
*   Implement an integration event processor background job
*   Demonstrate how to publish and consume messages asynchronously

Let's dive in.

## [When To Use an In-Memory Message Bus](#when-to-use-an-in-memory-message-bus)

I have to preface this by saying that an in-memory message bus is far from a silver bullet. There are many caveats to using it, as you will soon learn.

But first, let's start with the pros of using an in-memory message bus:

*   Because it works in memory, you have a very low-latency messaging system
*   You can implement asynchronous (non-blocking) communication between components

However, there are a few drawbacks to this approach:

*   Potential for losing messages if the application process goes down
*   It only works inside of a single process, so it's not useful in distributed systems

A practical use case for an in-memory message bus is when building a modular monolith. You can implement [communication between modules](https://milanjovanovic.tech/blog/modular-monolith-communication-patterns) using integration events. When you need to extract some modules into a separate service, you can replace the in-memory bus with a distributed one.

## [Defining The Messaging Abstractions](#defining-the-messaging-abstractions)

We will need a few abstractions to build our simple messaging system. From the client's perspective, we really only need two things. One abstraction is to publish messages, and another is to define a message handler.

The `IEventBus` interface exposes the `PublishAsync` method. This is what we will use to publish messages. There's also a generic constraint defined that only allows passing in an `IIntegrationEvent` instance.

C#

```
public interface IEventBus
{
    Task PublishAsync<T>(
        T integrationEvent,
        CancellationToken cancellationToken = default)
        where T : class, IIntegrationEvent;
}
```

I want to be practical with the `IIntegrationEvent` abstraction, so I'll use [MediatR](https://github.com/jbogard/MediatR) for the pub-sub support. The `IIntegrationEvent` interface will inherit from `INotification`. This allows us to easily define `IIntegrationEvent` handlers using `INotificationHandler<T>`. Also, the `IIntegrationEvent` has an identifier, so we can track its execution.

The abstract `IntegrationEvent` serves as a base class for concrete implementations.

C#

```
using MediatR;

public interface IIntegrationEvent : INotification
{
    Guid Id { get; init; }
}

public abstract record IntegrationEvent(Guid Id) : IIntegrationEvent;
```

## [Simple In-Memory Queue Using Channels](#simple-in-memory-queue-using-channels)

The `System.Threading.Channels` namespace provides data structures for asynchronously passing messages between producers and consumers. Channels implement the [producer/consumer pattern](https://en.wikipedia.org/wiki/Producer%E2%80%93consumer_problem). Producers asynchronously produce data, and consumers asynchronously consume that data. It's an essential pattern for building loosely coupled systems.

One of the primary motivations behind the adoption of [.NET Channels](https://learn.microsoft.com/en-us/dotnet/core/extensions/channels) is their exceptional performance characteristics. Unlike traditional message queues, Channels operate entirely in memory. This has the disadvantage of the potential for message loss if the application crashes.

The `InMemoryMessageQueue` creates an unbounded channel using the `Channel.CreateUnbounded` bounded. This means the channel can have any number of readers and writers. It also exposes a `ChannelReader` and `ChannelWriter`, which allow consumers to publish and consume messages.

C#

```
internal sealed class InMemoryMessageQueue
{
    private readonly Channel<IIntegrationEvent> _channel =
        Channel.CreateUnbounded<IIntegrationEvent>();

    public ChannelReader<IIntegrationEvent> Reader => _channel.Reader;

    public ChannelWriter<IIntegrationEvent> Writer => _channel.Writer;
}
```

You also need to register the `InMemoryMessageQueue` as a singleton with dependency injection:

C#

```
builder.Services.AddSingleton<InMemoryMessageQueue>();
```

## [Implementing The Event Bus](#implementing-the-event-bus)

The `IEventBus` implementation is now straightforward with the use of channels. The `EventBus` class uses the `InMemoryMessageQueue` to access the `ChannelWriter` and write an event to the channel.

C#

```
internal sealed class EventBus(InMemoryMessageQueue queue) : IEventBus
{
    public async Task PublishAsync<T>(
        T integrationEvent,
        CancellationToken cancellationToken = default)
        where T : class, IIntegrationEvent
    {
        await queue.Writer.WriteAsync(integrationEvent, cancellationToken);
    }
}
```

We will register the `EventBus` as a singleton service with dependency injection because it's stateless:

C#

```
builder.Services.AddSingleton<IEventBus, EventBus>();
```

## [Consuming Integration Events](#consuming-integration-events)

With the `EventBus` implementing the producer, we need a way to consume the published `IIntegrationEvent`. We can implement a simple [background service](https://milanjovanovic.tech/blog/running-background-tasks-in-asp-net-core) using the built-in `IHostedService` abstraction.

The `IntegrationEventProcessorJob` depends on the `InMemoryMessageQueue`, but this time for reading (consuming) messages. We'll use the `ChannelReader.ReadAllAsync` method to get back an `IAsyncEnumerable`. This allows us to consume all the messages in the `Channel` asynchronously.

The `IPublisher` from MediatR helps us connect the `IIntegrationEvent` with the respective handlers. It's important to resolve it from a [**custom scope**](https://milanjovanovic.tech/blog/using-scoped-services-from-singletons-in-aspnetcore) if you want to inject scoped services into the event handlers.

C#

```
internal sealed class IntegrationEventProcessorJob(
    InMemoryMessageQueue queue,
    IServiceScopeFactory serviceScopeFactory,
    ILogger<IntegrationEventProcessorJob> logger)
    : BackgroundService
{
    protected override async Task ExecuteAsync(CancellationToken stoppingToken)
    {
        await foreach (IIntegrationEvent integrationEvent in
            queue.Reader.ReadAllAsync(stoppingToken))
        {
            try
            {
                using IServiceScope scope = serviceScopeFactory.CreateScope();

                IPublisher publisher = scope.ServiceProvider
                    .GetRequiredService<IPublisher>();

                await publisher.Publish(integrationEvent, stoppingToken);
            }
            catch (Exception ex)
            {
                logger.LogError(
                    ex,
                    "Something went wrong! {IntegrationEventId}",
                    integrationEvent.Id);
            }
        }
    }
}
```

Don't forget to register the hosted service:

C#

```
builder.Services.AddHostedService<IntegrationEventProcessorJob>();
```

## [Using The In-Memory Message Bus](#using-the-in-memory-message-bus)

With all of the necessary abstractions in place, we can finally use the in-memory message bus.

The `IEventBus` service will write the message to the `Channel` and immediately return. This allows you to publish messages in a non-blocking way, which can improve performance.

C#

```
internal sealed class RegisterUserCommandHandler(
    IUserRepository userRepository,
    IEventBus eventBus)
    : ICommandHandler<RegisterUserCommand>
{
    public async Task<User> Handle(
        RegisterUserCommand command,
        CancellationToken cancellationToken)
    {
        // First, register the user.
        User user = CreateFromCommand(command);

        userRepository.Insert(user);

        // Now we can publish the event.
        await eventBus.PublishAsync(
            new UserRegisteredIntegrationEvent(user.Id),
            cancellationToken);

        return user;
    }
}
```

This solves the producer side, but we also need to create a consumer for the `UserRegisteredIntegrationEvent` message. This part is greatly simplified because I'm using MediatR in this implementation.

We need to define an `INotificationHandler` implementation handling the integration event `UserRegisteredIntegrationEvent`. This will be the `UserRegisteredIntegrationEventHandler`.

When the background job reads the `UserRegisteredIntegrationEvent` from the `Channel`, it will publish the message and execute the handler.

C#

```
internal sealed class UserRegisteredIntegrationEventHandler
    : INotificationHandler<UserRegisteredIntegrationEvent>
{
    public async Task Handle(
        UserRegisteredIntegrationEvent event,
        CancellationToken cancellationToken)
    {
        // Asynchronously handle the event.
    }
}
```

## [Improvement Points](#improvement-points)

While our basic in-memory message bus is functional, there are several areas we can improve:

*   **Resilience** - We can introduce retries when we run into exceptions, which will improve the reliability of the message bus.
*   **Idempotency** - Ask yourself if you want to handle the same message twice. The [idempotent consumer pattern](https://milanjovanovic.tech/blog/idempotent-consumer-handling-duplicate-messages) elegantly solves this problem.
*   **Dead Letter Queue** - Sometimes, we won't be able to handle a message correctly. It's a good idea to introduce a persistent storage for these messages. This is called a [Dead Letter Queue](https://aws.amazon.com/what-is/dead-letter-queue/), and it allows for troubleshooting at a later time.

We've covered the key aspects of building an in-memory message bus using .NET Channels. You can extend this further by implementing the improvements for a more robust solution.

Remember that this implementation only works inside of one process. Consider using a real message broker if you need a more reliable solution.

That's all for today. I'll see you next week.

* * *

## Frequently Asked Questions

What is an in-memory message bus?

A messaging component that passes messages between loosely coupled parts of the same process, entirely in memory. It gives you very low latency and non-blocking asynchronous communication, at the cost of losing messages if the process goes down and only working inside a single process.

When should you use an in-memory message bus?

It is particularly useful when high performance and low latency are critical requirements. A practical use case is a modular monolith, where modules communicate through integration events. When you later extract a module into a separate service, you can replace the in-memory bus with a distributed one.

What are .NET Channels?

The System.Threading.Channels namespace provides data structures for asynchronously passing messages between producers and consumers, implementing the producer/consumer pattern. Channels operate entirely in memory, which gives them exceptional performance but also means messages are lost if the application crashes.

How do you consume messages from a .NET Channel in a background service?

Implement a BackgroundService that iterates ChannelReader.ReadAllAsync as an IAsyncEnumerable. For each message, create a service scope and use MediatR's IPublisher to dispatch the event to its INotificationHandler implementations. The custom scope lets you inject scoped services into the handlers.

What are the drawbacks of an in-memory message bus?

Messages can be lost if the application process goes down, and it only works inside one process, so it is not useful in distributed systems. Improvements include retries for resilience, the idempotent consumer pattern for duplicate messages, and a dead letter queue for messages that repeatedly fail.
