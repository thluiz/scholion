---
url: "https://devblog.kogan.com/blog/patterns-amp-best-practices-in-event-driven-systems?ref=dailydev"
captured_at: "2026-09-25T07:54:20+01:00"
title: "Patterns & Best Practices in Event-Driven Systems — Kogan.com Dev Blog"
domain: "devblog-kogan-com"
---

## Designing Robust, Scalable, Maintainable Event Architectures

Event-driven architecture (EDA) gives teams the ability to build decoupled, scalable systems that evolve independently. In the previous article, we introduced the idea using a restaurant analogy: instead of shouting instructions across the kitchen, teams place “dockets” on the rail and stations take what they need.

We’ll continue that analogy lightly in this post—sprinkling it here and there—while focusing on the engineering patterns that make event-driven systems work in practice.

## Core Patterns in Event-Driven Architecture

### Pattern 1: Event Notification

An **event notification** is a tiny message that simply declares **“something happened.”**

It doesn’t contain all the details—just enough for downstream systems to react. Think of it like a kitchen bell dinging: The bell doesn’t contain the meal. It’s just a signal. The cook still needs to check the ticket rail (the database) for the details of the order 12345. Example

```
{
  "eventName": "OrderCreated",
  "orderId": 12345,
  "createdAt": "2025-11-26T01:00:00Z"
}
```

*   Why it’s useful
    *   Extremely lightweight
    *   Easy to publish, easy to fan out
    *   Consumers decide how much extra data they need
*   Trade-offs
    *   Consumers must fetch details themselves
    *   More cross-service calls → more coupling
    *   Higher latency when many consumers query upstream systems

Use this pattern when the event is a simple trigger—like a bell, not a full meal.

### Pattern 2: Event-Carried State Transfer (ECST)

In **Event-Carried State Transfer**, the event carries all required data so consumers don’t need to make additional calls.

It’s the equivalent of the chef not only ringing the bell but also placing the complete **plated dish on the pass**. No one needs to ask questions—everything needed is right there.

```
{
  "eventName": "OrderPacked",
  "orderId": 12345,
  "items": [
    { "sku": "ABC123", "qty": 2 }
  ],
  "warehouseId": 19,
  "totalWeightGrams": 1850
}
```

*   Why it’s powerful
    *   Zero need for back-calls → full decoupling
    *   Highly resilient—consumers can process events even if upstream is down
    *   Faster pipelines, fewer moving parts
*   Trade-offs
    *   Larger event payloads → more bandwidth/storage
    *   More careful schema management
    *   Potential latency/throughput impact in high-volume streams

You’re essentially pre-plating the data, which costs more effort upfront, but saves everyone time downstream.

### Pattern 3: Event Sourcing

Instead of storing only the current state, **Event Sourcing** stores every change as an **immutable event**.

State is rebuilt by replaying the events.

Just like a kitchen’s order history tells the complete story of what happened throughout service, event sourcing gives you a full timeline of every change.

Example (C# Aggregate Rehydration)

```
var events = eventStore.LoadStream("Order-12345");
var order = OrderAggregate.Rehydrate(events);
```

*   Why it’s valuable
    *   Perfect audit trail
    *   Time-travel debugging
    *   Ability to replay events for recovery or analytics
*   Trade-offs
    *   Higher cognitive load for newcomers
    *   Requires rigorous versioning
    *   Requires maintaining projections/read models

**CQRS Note**

Event Sourcing often pairs with CQRS—splitting **commands** (writes) from **queries** (reads).

It’s like chefs cooking in the kitchen while waitstaff maintain menus, tables, and customer-facing views.

Each side does what it’s optimized for.

### Pattern 4: Choreography (Decentralised Workflow)

With choreography, services react to each other’s events without a central coordinator.

It’s like a well-trained kitchen crew: when the grill station finishes cooking a steak, the garnish station knows it’s their turn—without anyone shouting instructions.

*   Benefits
    *   Fully decoupled
    *   Naturally scalable
    *   Easy for new services to join by subscribing
*   Drawbacks
    *   Harder to visualize the full workflow
    *   Risk of event spaghetti
    *   Difficult to enforce global ordering or handle cross-service failures

Great for simple flows where each station knows what to do next.

### Pattern 5: Orchestration (Service Composer / Workflow Engine)

Orchestration introduces a conductor—a central service that coordinates each step of the workflow.

Think of it like a head chef calling out the steps during a complex dish:

“Start the sauce.”

“Grill the chicken.”

“Plate it.”

The orchestration engine takes responsibility for the ordering and coordination.

```
public class DispatchOrchestrator 
{
    public async Task Handle(OrderPaid evt)
        => await Send(new ReserveStock(evt.OrderId));

    public async Task Handle(StockReserved evt)
        => await Send(new BookShipment(evt.OrderId));

    public async Task Handle(ShipmentBooked evt)
        => await Send(new MarkOrderReady(evt.OrderId));
}
```

*   When orchestration is ideal
    *   Multi-step workflows
    *   Processes requiring retries and compensation
    *   Compliance requirements → clear traceability

Choreography scales. Orchestration brings order to complexity. Many systems end up using both.

### Idempotency Everywhere

Events may be delivered more than once.

Consumers must behave safely even if they “see the same order twice.”

Just like the kitchen must avoid making the same dish twice if the order docket is accidentally duplicated.

```
if (db.HasProcessed(evt.Id)) return;
Process(evt);
db.MarkProcessed(evt.Id);
```

In high-throughput, distributed systems, rely on **unique constraints** on the event ID (or a combination key) in the **MarkProcessed** step. This guarantees atomicity and prevents race conditions if two consumers attempt to process the event simultaneously.

### Durable, Replayable Streams

Use platforms that retain events reliably:

*   Kafka
*   AWS EventBridge + SQS
*   Pulsar
*   EventStoreDB

Replay is the equivalent of reviewing the order history after service to understand what happened.

### Explicit Event Versioning

Events evolve as the business evolves.

Always version your events.

```
{
  "eventName": "OrderCreated",
  "version": 3,
  "orderId": 12345
}
```

This is like updating the recipe book—you need to know which version was used.

### Event Contract Management (Schema Evolution)

Managing the schema itself is a real operational challenge.

Common solutions

*   Schema Registry (Confluent, AWS Glue)
*   Avro / Protobuf with compatibility modes
*   Automated consumer-driven contract tests

Just as a restaurant must keep recipes and menus consistent across teams, event schemas must stay compatible across services.

### Domain-Driven Event Naming

Good events describe meaningful business events—not technical state changes.

✔ OrderPaid

✔ ShipmentDispatched

✔ StockShortageDetected

These read like “kitchen tickets”—instantly meaningful across teams.

### Correlation IDs

Attach a correlation ID that follows the event across the system.

It’s your equivalent of an order number in a busy restaurant—the thing that ties together all actions associated with a single request.

```
x-correlation-id: d387f799e001-4a12-a3f1
```

**Why Correlation IDs are Essential**

In a decoupled EDA, the logical flow of a single business request is spread across multiple services, message queues, and logs. Without a correlation ID, this flow is almost impossible to trace.

1.  **Distributed Debugging**: If a customer reports a failure on order 12345, you can search your centralised logging system (like Splunk or ELK) using the correlation ID and instantly retrieve every log line, from every service, that contributed to that order's fulfillment.
2.  **Request Tracing**: They are the backbone of Application Performance Monitoring (APM) tools, which visualize the end-to-end path, latency, and dependencies of a request across your entire system.
3.  **Cross-System Auditing**: They provide the non-repudiable link between an incoming API call and the final persistent action (e.g., database write or shipment creation), fulfilling compliance needs.

A system without correlation IDs is a **black box**. They are the single most important tool for turning a distributed system into something observable and debuggable.

### Conclusion

Event-driven architecture unlocks scalability, resilience, and autonomy across teams. By understanding patterns like event notification, ECST, event sourcing, choreography, and orchestration, you can match your workflow’s needs to the right design.

The light kitchen analogy highlights what makes EDA so powerful: each station works independently, yet the whole system flows smoothly.

Combined with strong practices—idempotency, schema governance, replay, and correlation—these patterns help systems evolve with confidence even under rapid growth.
