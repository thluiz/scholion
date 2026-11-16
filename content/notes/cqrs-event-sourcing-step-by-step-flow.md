---
title: "CQRS + Event Sourcing – Step by Step | Learn CQRS and Event Sourcing"
date: '2020-04-20T21:22:46+00:00'
category: webclip
summary: 'The post explains how commands, events, and queries flow in a CQRS and Event Sourcing system, from a task-based UI through handlers, event storage, projections, and the read model.'
tags: ["cqrs", "event-sourcing", "command-handler", "read-model"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "CQRS + Event Sourcing – Step by Step | Learn CQRS and Event Sourcing"
    url: "https://danielwhittaker.me/2020/02/20/cqrs-step-step-guide-flow-typical-application"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/danielwhittaker-me--cqrs-event-sourcing-step-by-step-flow.md"
    kind: repo
---

The post walks through the flow of a typical CQRS and Event Sourcing application. It explains how the write side handles commands, stores events in order, and then uses those events to build optimized read models for queries.

## Reading notes

- CQRS means Command Query Responsibility Segregation and separates the write side from the read side of an application.
- Event sourcing stores the order and timing of changes as an append-only log instead of only storing the final state.
- The approach is presented as a good fit for more complex domains, especially business-critical applications with a clear domain model.
- The author says CQRS and event sourcing are well suited to microservices because both use domain events and event streams.
- A command starts from the UI, which is described as task-based rather than CRUD-based.
- The message bus routes each command to a single handler, usually inside a transaction.
- The handler prepares the aggregate root and replays prior events from the event store to bring it to the latest state.
- The aggregate root decides whether the command can run and creates the events that would change its state.
- The handler then asks for the uncommitted changes before any persistence happens.
- The event store persists the events in order and must handle concurrency safely.
- The event store is described as the source of truth, and temporal queries are possible because events are stored in strict order.
- Published events can be routed to multiple projectors, which de-normalize data into read models.
- The read side stores simple DTOs in an optimized read database, which can support fast queries and different database types.
- The event stream can be used to rebuild the read model, either fully or in part.
- The read side is independent from the command side, and this separation is presented as the main benefit of CQRS.
