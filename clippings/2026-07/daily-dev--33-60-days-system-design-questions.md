---
url: "https://daily.dev/posts/EMnXrcVUC?utm_source=notification&utm_medium=email&utm_campaign=digest"
captured_at: "2026-07-06T12:26:38+01:00"
title: "33/60 Days System Design Questions"
domain: "daily.dev"
---

# 33/60 Days System Design Questions | daily.dev

> ## Excerpt
> A practical system design scenario where an order service using Postgres with mutable state loses the ability to reconstruct order history, leading to a...

---
[

![Post cover image](https://media.daily.dev/image/upload/s--g15AMGc6--/f_auto/v1780933918/posts/EMnXrcVUC?_a=BAMAMiWQ0)

](https://media.daily.dev/image/upload/s--g15AMGc6--/f_auto/v1780933918/posts/EMnXrcVUC?_a=BAMAMiWQ0)

Your order service takes 200 writes/sec at peak.

You audit 6 months of data. Something's off — two orders show the same ID, different totals.

You have the current state. You don't have how it got there.

Your DB is a graveyard of overwritten rows.

Here's the system:

• OrderService → Postgres (current state only)

• Events: placed, updated, cancelled, refunded

• Every UPDATE overwrites the previous row

• No audit log. No event history. No replay.

A billing dispute just landed. You need to reconstruct exactly what happened to Order #8471. You can't.

Instead of storing the current state, you store the sequence of events that produced it.

What's your approach when redesigning this service?

A) Event Sourcing — append-only event log as the source of truth, current state derived from replaying events.

B) Change Data Capture (CDC) — keep Postgres as-is, but stream all row changes to Kafka for an audit trail.

C) Add an audit_log table — trigger-based shadow writes on every INSERT/UPDATE/DELETE.

D) Dual-write — write to both the current-state table and a separate events table on every operation.

One of these gives you full replay, projection flexibility, and a real source of truth. The others are patches.

Pick one — A, B, C, or D — and tell me why. I'll drop the full breakdown in the comments.

If your team is arguing about audit trails or event-driven redesigns, tag someone who needs to see this.

Drop your answer 👇

#30DaysOfSystemDesign #SystemDesign #EventSourcing #SoftwareArchitecture

41 Comments

Sort:
