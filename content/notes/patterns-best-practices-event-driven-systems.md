---
title: "Patterns & Best Practices in Event-Driven Systems — Kogan.com Dev Blog"
date: '2026-09-25T07:54:20+01:00'
category: webclip
summary: 'The text presents EDA patterns such as event notification, ECST, event sourcing, choreography, and orchestration, as well as practices for idempotency, versioning, schema management, and correlation IDs.'
tags: ["event-driven-architecture","event-sourcing","microservices","correlation-ids"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Patterns & Best Practices in Event-Driven Systems — Kogan.com Dev Blog"
    url: "https://devblog.kogan.com/blog/patterns-amp-best-practices-in-event-driven-systems?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/devblog-kogan-com--patterns-best-practices-event-driven-systems.md"
    kind: repo
---

Event-driven architecture is presented as a way to build decoupled, scalable systems that can evolve independently. The post walks through core patterns, compares choreography with orchestration, and adds practices for replay, versioning, schema management, idempotency, and tracing.

## Reading notes

- Event-driven architecture lets teams build decoupled systems that scale and evolve independently.
- Event notification is a small message that only says something happened, which is useful when consumers can fetch the details they need.
- Event-Carried State Transfer sends the data needed by consumers inside the event, reducing back-calls and improving resilience.
- Event Sourcing stores every change as an immutable event and rebuilds state by replaying events; it is often paired with CQRS.
- Choreography lets services react to events without a central coordinator, while orchestration uses a central service to coordinate steps in a workflow.
- Idempotency is necessary because events can be delivered more than once, so consumers must safely ignore duplicates.
- Durable, replayable streams are recommended, with examples including Kafka, AWS EventBridge + SQS, Pulsar, and EventStoreDB.
- Events should be explicitly versioned, and schema evolution can be managed with schema registries, Avro or Protobuf compatibility modes, and consumer-driven contract tests.
- Events should use domain-driven names, such as OrderPaid, ShipmentDispatched, and StockShortageDetected.
- Correlation IDs are described as essential for tracing a request across services, logs, and monitoring tools.
