---
url: "https://betterengineers.substack.com/p/how-to-design-a-notification-system"
captured_at: "2026-08-24T17:50:15+01:00"
title: "How to Design a Notification System: Frontend + Backend"
domain: "betterengineers-substack-com"
---

---
Every production app has one. Most engineers underestimate it.

A notification system looks simple from the outside: a little bell icon, a red badge, maybe a push to your phone. But underneath that bell is one of the most technically challenging systems you’ll build — touching real-time infrastructure, fan-out at scale, mobile OS internals, user preference management, and delivery guarantees that directly affect user trust.

Get it wrong and you send the same “order shipped” push three times. Or a fraud alert arrives 45 minutes late. Or your Kafka queue backs up during a marketing blast and your transactional OTPs get delayed.

This post covers the complete system — **backend pipeline and frontend architecture** — with exact design decisions, capacity estimation, and the traps that break production systems.

## Functional Requirements

Before designing anything, clarify scope. A notification system must:

-   Send notifications through multiple channels: **push, email, SMS, in-app**
    
-   Support both individual and bulk sends (1 user vs 10M users)
    
-   Respect user preferences — opt-in/out per channel, quiet hours, frequency caps
    
-   Handle delivery failures with retries and fallback channels
    
-   Support scheduled future-dated notifications
    
-   Log delivery status for auditing and debugging
    
-   Distinguish between critical (OTP, fraud) and promotional (campaigns) notifications
    

## Non-Functional Requirements

-   **Scale:** 1M+ notifications/second at peak (marketing blasts)
    
-   **Latency:** Transactional notifications delivered in < 1s; promotional within minutes
    
-   **Availability:** 99.9%+ — a notification system outage is a trust outage
    
-   **Durability:** No message loss for transactional notifications
    
-   **Idempotency:** Exactly-once delivery for critical alerts
    

## Capacity Estimation

Working backward from requirements helps size every component:

Workers per channel at 100 notifications/sec per worker:

-   Push: ~150 workers
    
-   Email: ~87 workers
    
-   SMS: ~29 workers
    

With batching (FCM supports 500 tokens/batch), push workers drop to ~30.

## The Full Architecture

-   _**The complete pipeline.**_
    
-   _**Producer services publish events →**_
    
-   _**Kafka decouples ingestion from processing →**_
    
-   _**Router resolves preferences and fans out →**_
    
-   _**Channel dispatchers deliver →**_
    
-   _**DLQ catches failures.**_
    

The architecture has five distinct layers. Each is independently scalable. Each fails independently.

## Backend: Layer by Layer

### Layer 1 — Producer Services

Any service that triggers a user-facing event publishes to the Notification API. It never calls FCM or Twilio directly — it only says _what happened_:

The API returns **202 Accepted** immediately. The order service’s job is done. If the notification pipeline goes down, the order service is unaffected.

**Idempotency on the write path:** Before publishing to Kafka, generate a key: **SHA256(userId + eventId + type)** and write to Redis with a 24h TTL. If the same event arrives again (network retry, at-least-once producer), the duplicate is dropped silently. This is the only reliable way to prevent “order shipped” from arriving twice.

**Rate limiting at the API:** Protect the Notification API from runaway producers using Redis token buckets. Per-service limits (e.g. Marketing Service: 10,000 req/min) prevent a campaign bug from flooding the queue and delaying OTPs.

### Layer 2 — Kafka Priority Topics

Never use a single Kafka topic for all notifications. A marketing blast to 10M users on the same topic as an OTP will delay the OTP.

[Get 30% off forever](https://betterengineers.substack.com/subscribe?coupon=f7039f8a&utm_content=201093592)
