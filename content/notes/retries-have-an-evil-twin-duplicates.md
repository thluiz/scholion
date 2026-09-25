---
title: "Retries Have an Evil Twin: Duplicates"
date: '2025-08-11T22:13:21+01:00'
category: webclip
summary: 'The post explains why at-least-once delivery leads to duplicate work and compares four application-level ways to stop it: database constraints, in-memory dedup, Redis, and broker support.'
tags: ["distributed-systems", "retries", "idempotency", "deduplication"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Retries Have an Evil Twin: Duplicates - by Raul Junco"
    url: "https://newsletter.systemdesignclassroom.com/p/retries-have-an-evil-twin-duplicates?utm_source=substack&utm_medium=email"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-08/newsletter-systemdesignclassroom-com--retries-have-an-evil-twin-duplicates.md"
    kind: repo
---

Duplication is presented as a normal outcome of retries in distributed systems, not an edge case. If the same payment, order, or message is replayed, the app can create corrupted data and repeated downstream effects unless it is built to handle at-least-once delivery.

The post compares four ways to handle duplicates at the application layer. A unique database constraint can block repeated inserts with an idempotency key. In-memory tracking is fast but only fits single-instance or short-lived processes. Redis offers shared deduplication across nodes with TTL-based cleanup, and broker-level duplicate detection can stop repeated delivery before the app sees it. The main takeaway is to combine layers where the flow is critical.

## Reading notes

- Retries and queues can make the same work arrive more than once.
- At-least-once delivery means messages and requests may be processed multiple times.
- Duplicate processing can charge users twice, create repeated records, and trigger repeated events.
- Without duplication control, data becomes unreliable and operations spend time fixing inconsistencies.
- A database `UNIQUE` constraint plus an idempotency key can stop repeated inserts and return the original result.
- In-memory deduplication is fast, but it only works safely in single-instance setups without frequent restarts.
- Redis can store request IDs with TTL and coordinate deduplication across nodes.
- Broker-side duplicate detection can discard repeated messages before they reach the application.
- The post recommends using the database for strong guarantees, Redis for coordination, and brokers for message-level protection.
- TTL-based deduplication is presented as a practical starting point for many systems.
