---
title: "Building an Event Storage"
date: '2020-02-22T12:11:44+00:00'
category: webclip
summary: 'The chapter explains how to implement a basic event storage in an RDBMS, covering event and aggregate tables, ordered writes, optimistic concurrency, rolling snapshots, and using the event store as a queue.'
tags: ["event-storage", "cqrs", "rolling-snapshots", "optimistic-concurrency"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Building an Event Storage"
    url: "https://cqrs.wordpress.com/documents/building-event-storage"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/cqrs-wordpress-com--building-an-event-storage.md"
    kind: repo
---

The chapter describes a simple event storage implementation built on top of a relational database. It stores one row per event, keeps aggregate version numbers, and uses ordered reads and transactional writes with optimistic concurrency checks. It also notes that the design is meant as a discussion model rather than production-ready software.

## Reading notes

- A basic event storage can be represented with two tables, one for events and one for aggregates.
- Each event stores serialized data, a version number, and an aggregate identifier.
- The aggregates table keeps the current version for each aggregate and supports the concurrency check.
- The main read operation is to fetch all events for one aggregate in version order.
- The main write operation checks the expected version, inserts each event in sequence, and updates the aggregate version inside a transaction.
- Rolling snapshots are introduced to reduce the number of events needed to rebuild an aggregate.
- Snapshots are stored in a separate table with serialized aggregate data and the version they represent.
- A background snapshotter can create snapshots asynchronously when an aggregate passes a configured event count.
- The chapter warns that inline snapshots inside the event log can create ordering and concurrency problems.
- The event storage can also act as a queue by adding a sequence number and letting another process publish events asynchronously.
- Using the event store as a queue reduces latency on the initial write and avoids dual writes to storage and queue in the critical path.
