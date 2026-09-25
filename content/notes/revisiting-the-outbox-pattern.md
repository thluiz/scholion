---
title: "Revisiting the Outbox Pattern"
date: '2026-09-25T21:55:24+01:00'
category: webclip
summary: 'The article revisits the outbox pattern for microservices, explains how it keeps database updates and event publication atomic, and compares it with polling, CDC, 2PC, and other alternatives.'
tags: ["outbox-pattern", "microservices", "change-data-capture", "kafka"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Revisiting the Outbox Pattern"
    url: "https://www.decodable.co/blog/revisiting-the-outbox-pattern?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/decodable-co--revisiting-the-outbox-pattern.md"
    kind: repo
---

The outbox pattern is presented as a way to update a service’s local database and notify other services without distributed transactions. The article argues that log-based CDC is the preferred relay mechanism, and that a log-only implementation can reduce database overhead while preserving ordering and consistency.

It also reviews implementation details such as the outbox table structure, housekeeping, backfills, and consumer idempotency. The later sections compare the pattern with Dapr, read-yourself, raw change streams, 2PC, and durable execution, and conclude that the outbox pattern remains a central tool for reliable microservice communication.

## Reading notes

- A service can persist its own data and emit a notification in one local transaction, so both actions succeed or fail together.
- The pattern gives eventual consistency, not full ACID guarantees across services.
- Polling the outbox table can create database load and ordering problems under concurrency.
- Log-based CDC preserves commit order, avoids polling overhead, and usually gives lower latency.
- An outbox table is append-only, with fields such as id, aggregate type, aggregate id, event type, and payload.
- With log-based CDC, housekeeping can remove outbox rows immediately after insert because the transaction log still contains the event.
- Postgres can write outbox messages directly to the WAL with pg_logical_emit_message().
- The payload format is a data contract that should evolve in a forward-compatible way.
- Backfills can be handled with incremental snapshotting and chunk markers so live updates take precedence.
- Consumers should guard against duplicates, for example by using a monotonically increasing offset from the transaction log.
- The main criticisms discussed are database overhead, complexity, and latency.
- The article compares the pattern with Dapr, read-yourself, raw change-event streams, 2PC, and durable execution frameworks.
- The conclusion is that the outbox pattern is still highly relevant, especially when implemented through log-based CDC.
