---
title: "Building Resilient Payment Systems"
date: '2023-10-24T14:26:38+00:00'
category: webclip
summary: 'Thread summarizes Shopify Engineering’s ten recommendations for resilient payment systems, covering timeouts, circuit breakers, monitoring, idempotency, testing, and incident handling.'
tags: ["payment-systems", "resilience", "software-engineering", "distributed-systems"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Thread by @milan_milanovic: 𝗕𝘂𝗶𝗹𝗱𝗶𝗻𝗴 𝗥𝗲𝘀𝗶𝗹𝗶𝗲𝗻𝘁 𝗣𝗮𝘆𝗺𝗲𝗻𝘁 𝗦𝘆𝘀𝘁𝗲𝗺𝘀 The recent article by Shopify Engineering explained the…"
    url: "https://x.com/milan_milanovic/status/1683357943037657090"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2023-10/x-com--building-resilient-payment-systems-top-10-tips.md"
    kind: repo
---

Dr Milan Milanović summarizes Shopify Engineering’s ten main tips for building resilient payment systems, from tuning timeouts and adding circuit breakers to structured logging, reconciliation, and incident retrospectives. He also points readers to his newsletter for more details.

## Reading notes

- The thread presents Shopify Engineering’s list of ten useful tips and tricks for resilient payment systems.
- Lower timeouts are recommended, with an example that Ruby’s Net::HTTP 60s default is too slow when users are waiting in online applications.
- Circuit breakers such as Shopify’s Semian are suggested to detect when a service is down and fail fast instead of waiting for timeouts.
- Little’s Law is highlighted to relate queue size, arrival rate, and time, helping to design systems that handle load efficiently.
- Monitoring and alerting should cover the four golden signals from Google SRE: latency, traffic, errors, and saturation, to detect overload risk.
- Structured logging in a machine-readable format is recommended for better observability.
- Idempotency keys are advised so payments or refunds are executed exactly once while tracking attempts toward financial partners.
- Consistent reconciliation with financial partners’ records is emphasized, including recording mismatches and remediating them automatically when possible.
- Regular load testing is encouraged to probe system limits and safeguards, including simulating large flash sales; Shopify uses scriptable load balancers to throttle checkouts.
- Incident management at Shopify uses a Slack bot and defined roles for coordination, external communication, and restoring stability, triggered by alerts or manual reports.
- Incident retrospectives occur within a week to review what happened, adjust incorrect assumptions, and reduce the chance of recurrence.
- The author ends by inviting readers to subscribe to his "Techworld with Milan" newsletter for more information and provides related links and a card.
