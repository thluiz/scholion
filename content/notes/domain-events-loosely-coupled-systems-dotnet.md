---
title: "How To Use Domain Events To Build Loosely Coupled Systems"
date: '2026-11-16T20:25:00+00:00'
category: webclip
summary: 'Explains how domain events in DDD help decouple core logic from side effects in .NET, comparing them to integration events and showing implementation with MediatR and EF Core.'
tags: ["domain-events", "ddd", "dotnet", "architectural-patterns"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "How To Use Domain Events To Build Loosely Coupled Systems"
    url: "https://www.milanjovanovic.tech/blog/how-to-use-domain-events-to-build-loosely-coupled-systems/?utm_source=Twitter&utm_campaign=04.12.2023"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/milanjovanovic-tech--domain-events-loosely-coupled-systems-dotnet.md"
    kind: repo
---

Domain events in Domain-Driven Design represent immutable facts that already happened in the domain and that other parts of the domain should react to. By raising domain events from entities and letting separate handlers respond, core domain logic stays decoupled from side effects while still coordinating behavior across aggregates. In .NET, you can model domain events as MediatR notifications, store them on entities, and publish them from EF Core's Unit of Work, choosing when to publish and which consistency tradeoffs to accept, often using the Outbox pattern for reliability.

## Reading notes

- Coupling in software describes how strongly different parts of a system depend on each other; loose coupling reduces the impact of changes across components.
- Domain events are a DDD tactical pattern that capture something that happened in the domain and that other domain parts should know about.
- Events represent past facts and are immutable, which shapes how domain events should be designed.
- Domain events make side effects explicit and improve separation of concerns, especially for behavior spanning multiple aggregates.
- The publisher of a domain event should remain decoupled from the side effects, which are moved into event handlers.
- Domain events and integration events are both representations of past occurrences but differ in intent and scope.
- Domain events are published and consumed inside a single domain, typically over an in-memory message bus, and may be handled synchronously or asynchronously.
- Integration events are consumed by other subsystems or bounded contexts, sent via a message broker and queues, and are processed fully asynchronously.
- Domain events inside a domain can be used as a source to generate integration events that cross domain boundaries.
- One implementation approach is defining an IDomainEvent abstraction that implements MediatR's INotification interface.
- Using MediatR allows leveraging its publish-subscribe mechanism so a single domain event can be routed to one or multiple handlers.
- When designing domain events, they should be immutable, carefully sized in terms of how much data they carry, and named in the past tense.
- An example event is CourseCompletedDomainEvent, carrying the CourseId as data.
- Only entities are allowed to raise domain events, which can be enforced with an Entity base class.
- The Entity base class keeps a private list of domain events, exposes read-only access via a snapshot, and provides a method to clear stored events.
- Raising domain events is encapsulated in a protected method that appends to the internal collection so external code cannot manipulate it directly.
- A concrete entity such as Course can inherit from Entity, update its state, and then raise a CourseCompletedDomainEvent when a course is completed.
- EF Core can act as a Unit of Work to collect and publish all domain events that occur within a transaction.
- One simple strategy is overriding SaveChangesAsync to publish domain events around the database call instead of building more complex infrastructure.
- There are two main timing options for publishing: before SaveChangesAsync or after it completes.
- Publishing before SaveChangesAsync keeps domain events in the same transaction and provides immediate consistency between data and handlers.
- Publishing after SaveChangesAsync runs handlers in a separate transaction, leading to eventual consistency and the possibility of handler failures.
- The author prefers publishing after saving changes to the database, accepting eventual consistency.
- Publishing after database persistence introduces a risk of inconsistency if event handling fails once data is already committed.
- The Outbox pattern mitigates inconsistency by persisting both domain data and domain events as outbox messages in a single atomic transaction.
- With the Outbox pattern, a background job processes stored outbox messages asynchronously, preserving reliability while accepting eventual consistency.
- Implementing PublishDomainEventsAsync involves scanning the EF Core ChangeTracker for entities of type Entity.
- For each tracked entity, the method retrieves its domain events, clears them from the entity, and aggregates them into a list.
- The accumulated domain events are then published one by one through an injected publisher component.
- Handling domain events with MediatR requires implementing INotificationHandler<T> for each specific domain event type.
- An example handler, CourseCompletedDomainEventHandler, receives the CourseCompletedDomainEvent and uses an IBus to publish a corresponding CourseCompletedIntegrationEvent.
- This pattern separates internal domain reactions from cross-system notifications, turning a domain event into an integration event when needed.
- Domain events can be processed asynchronously, helping to offload side effects and keep core domain operations focused.
- Implementing domain events with EF Core and MediatR avoids creating custom messaging infrastructure because existing libraries supply the necessary building blocks.
- Choosing when to publish domain events requires weighing immediate consistency against eventual consistency and reliability concerns.
- The author resolves the tradeoff by publishing events after saving changes while combining this with the Outbox pattern for stronger guarantees.
- A linked video further demonstrates how to implement domain events to create decoupled systems that can scale.
