---
title: "How to Design a Notification System: Frontend + Backend"
date: '2026-08-24T17:50:15+01:00'
category: webclip
summary: 'The post maps a notification system as a five-layer pipeline with backend fan-out, priority handling, idempotency, rate limiting, capacity estimates, and frontend delivery concerns tied to trust and scale.'
tags: ["notification-systems", "kafka", "idempotency", "frontend-architecture"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to Design a Notification System: Frontend + Backend"
    url: "https://betterengineers.substack.com/p/how-to-design-a-notification-system"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-08/betterengineers-substack-com--how-to-design-a-notification-system-frontend-backend.md"
    kind: repo
---

The post says notification systems are harder than they look because they sit on real-time infrastructure, fan-out at scale, mobile OS internals, user preferences, and delivery guarantees. It frames the system as a backend and frontend design problem, with reliability and trust as central concerns.

It defines functional requirements such as multi-channel delivery, bulk and individual sends, user preferences, retries and fallback channels, scheduled notifications, delivery logs, and a split between critical and promotional messages. It also sets non-functional targets for scale, latency, availability, durability, and idempotency, then begins the architecture with capacity estimates, a five-layer pipeline, producer services that call a Notification API, 202 Accepted responses, Redis-based idempotency, rate limiting, and Kafka priority topics.

## Reading notes

- Notification systems can fail in ways users notice immediately, such as duplicate alerts, delayed fraud messages, or delayed OTPs during traffic spikes.
- The system should support push, email, SMS, and in-app delivery, for both one user and very large batches.
- User preferences must cover opt-in or opt-out per channel, quiet hours, and frequency caps.
- Delivery failures need retries and fallback channels, and future-dated notifications must be supported.
- Critical notifications and promotional notifications must be treated differently.
- The scale target is 1M+ notifications per second at peak, with transactional notifications under 1 second and promotional notifications within minutes.
- Availability should be 99.9%+, and transactional notifications should not be lost.
- Critical alerts need exactly-once delivery.
- Capacity is estimated backward from worker throughput per channel, with batching reducing push worker count.
- The architecture is described as five layers, each independently scalable and independently failing.
- Producer services publish events to the Notification API instead of calling FCM or Twilio directly.
- The API returns 202 Accepted immediately so the triggering service is not blocked by the notification pipeline.
- Idempotency on the write path uses a SHA256 key built from userId, eventId, and type, stored in Redis with a 24-hour TTL.
- Redis token buckets are used to rate-limit producers and keep one service from flooding the queue.
- Kafka should use separate priority topics so marketing traffic does not delay OTPs.
