---
title: "3 Interview Questions on Event-Driven Patterns"
date: '2026-09-25T18:09:45+01:00'
category: webclip
summary: 'The post reviews three interview-ready event-driven patterns: competing consumers, queue-based retries with a DLQ, and async request-response using correlation IDs.'
tags: ["event-driven-systems", "message-queues", "competing-consumers", "correlation-id"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "3 Interview Questions on Event-Driven Patterns"
    url: "https://newsletter.systemdesigncodex.com/p/3-interview-questions-on-event-driven?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/newsletter-systemdesigncodex-com--3-interview-questions-on-event-driven-patterns.md"
    kind: repo
---

The post frames three event-driven patterns as common system design interview topics and useful ideas for project work. It focuses on how queues distribute work, how failed messages are retried, and how async request-response stays traceable across multiple service instances.

## Reading notes

- Competing Consumers lets one or more producers send messages to a queue while multiple consumer instances compete to process them.
- A message should be claimed by only one consumer, and different platforms enforce this with prefetch counts, in-flight delivery, peek-lock, or visibility timeout.
- For retrying failed transactions, the post describes a setup with a main queue, an optional retry queue, and a dead letter queue.
- The retry flow checks a retry count in message metadata, re-queues messages until the max retry limit, and then moves them to the DLQ.
- The post recommends exponential backoff, idempotency, message TTL, retry limits, and separating transient from permanent errors.
- In async request-response, the requester and responder may be different ephemeral instances, so the response may not return to the same instance that sent the request.
- A correlation ID is used to match the response message to the original request across services.
- The post says the correlation ID can be stored in a database, distributed cache, or local HashMap, and it travels with the request and response messages.
- It also notes that correlation IDs can help with multiple requests for the same order and make tracing easier across services.
