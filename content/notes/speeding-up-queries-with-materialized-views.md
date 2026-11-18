---
title: "Speeding up Queries with Materialized Views"
date: '2026-11-18T12:00:14+00:00'
category: webclip
summary: 'Explains how to speed up read-heavy systems by precomputing and persisting query-optimized materialized views, using CQRS, async updates, and event streams/projections.'
tags: ["materialized-views", "cqrs", "event-sourcing", "software-architecture"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Speeding up Queries with Materialized Views"
    url: "https://codeopinion.com/speeding-up-queries-with-materialized-views/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/codeopinion-com--speeding-up-queries-with-materialized-views.md"
    kind: repo
---

Many applications perform far more reads than writes, yet data is often stored in a way that favors writes and makes read-side composition expensive at runtime. The post describes using materialized views as precomputed, query-optimized data structures, often shaped exactly like UI or reporting needs, to reduce query complexity and improve performance in decomposed systems where data is spread across boundaries and databases.

Materialized views can be created directly on write, or asynchronously, and can reuse existing tables/columns or be separate read models. CQRS fits this approach by separating commands and queries so that read-side models can be independently optimized. Event sourcing and long-lived event streams support building and rebuilding projections that serve as materialized views, particularly for reporting and cross-boundary data composition.

## Reading notes

- Many systems are more read-intensive than write-intensive, but storage models are frequently optimized for writes rather than for queries.
- In large decomposed systems, data is split across many boundaries and databases, so UI queries often require composing data from multiple sources.
- UI/view composition in microservice-style systems tends to be a common and difficult performance challenge because of cross-database queries and required transformations.
- One way to improve performance is to move computation before the request, storing data already composed or transformed into the final shape needed by clients.
- The author compares this to caching but emphasizes that the cached structure is the final composed result, optimized for specific queries or use cases, not a direct mirror of the write-side schema.
- A sales order example shows precomputing values such as order total by denormalizing into a dedicated table so that later reads avoid joins and aggregations.
- Additional precomputation can include one-time calculations like tax when the order is placed, instead of recalculating during each query.
- Materialized views do not always require separate tables; sometimes calculated or specialized columns on existing tables can support query-optimized access.
- CQRS aligns well with this approach because it treats commands and queries as distinct operations that can use differently structured models.
- On command handling, the system can both persist the write model and perform precomputation to store query-specific data for later reads.
- Query handlers can then rely on tables or columns designed specifically for queries, which reduces runtime composition and improves read performance.
- Doing precomputation synchronously during writes can add latency to write operations, which may be acceptable in read-heavy systems but is a trade-off to consider.
- An alternative is to perform precomputation asynchronously by publishing an event after the write completes and letting a consumer update the read-optimized model.
- Asynchronous updates make the read database eventually consistent relative to the write side, so reads may not immediately see the latest state after a command.
- Eventual consistency affects user experience, and the author refers to separate guidance on how to handle UX issues when reads lag behind writes.
- The query and command models do not have to live in separate physical databases; they can share an instance while using different tables or columns.
- With event sourcing, events in the event store act as the source of truth from which different materialized views or projections can be derived.
- Projections read from event streams and perform the same kind of precomputation, persisting the results in whatever shape is needed for queries.
- Using event sourcing for projections generally avoids the need for a separate message broker, relying instead on event store subscriptions or polling.
- For reporting that must combine data from various logical boundaries, event streams of published events provide a source that can be consumed repeatedly.
- The author distinguishes event streams from queue-based brokers because events in streams are intended to be re-consumed and can remain in the log indefinitely.
- Persisting events long-term enables rebuilding materialized views at any time, which is useful for evolving reporting needs or recovering read models.
- Overall, applications can balance write-optimized storage with targeted read-optimized views, especially on query-heavy hot paths, to speed up queries.
