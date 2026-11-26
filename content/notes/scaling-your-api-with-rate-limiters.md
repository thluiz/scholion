---
title: "Scaling your API with rate limiters"
date: '2026-11-25T16:11:22+00:00'
category: webclip
summary: 'Stripe explains how different rate limiters and load shedders protect API availability, how they’re implemented with token buckets on Redis, and how to roll them out safely.'
tags: ["api-design", "rate-limiting", "reliability", "scalability"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Scaling your API with rate limiters"
    url: "https://stripe.com/blog/rate-limiters"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/stripe-com--scaling-your-api-with-rate-limiters.md"
    kind: repo
---

The text explains how rate limiting improves API availability beyond simply adding capacity. Stripe describes four mechanisms it uses in production: a per-user request rate limiter, a concurrent requests limiter, and two load shedders based on fleet usage and worker utilization. Together they protect critical traffic from spikes, misbehaving clients, and internal incidents. The post also outlines how Stripe implements rate limiting with the token bucket algorithm on Redis and how to deploy these controls safely using middleware integration, clear errors, safeguards, and dark launches.

## Reading notes

- Availability and reliability are described as central concerns for web applications and APIs, which can be disrupted by sudden traffic increases that degrade service or cause outages.
- Initially, adding more infrastructure capacity can handle growth, but a production API also needs robustness techniques like idempotency and protections so a single bad actor cannot affect overall availability.
- Rate limiting is positioned as a way to keep the API reliable when specific users cause traffic spikes, run buggy scripts, intentionally overload servers, or send large volumes of low-priority requests that could impact higher-priority traffic.
- Rate limiting also helps when internal problems reduce capacity and low-priority traffic must be dropped to preserve regular or critical requests.
- Stripe states that carefully chosen rate limiting strategies have helped keep its API available and that the post will focus on which strategies are most useful, how requests are prioritized, and how limiters were introduced without disrupting existing workflows.
- A rate limiter is defined as a control on traffic rate. It is appropriate when clients can slow down or spread out their calls without changing outcomes, but real-time cases that cannot be delayed generally require other capacity approaches.
- Stripe notes that users may generate sustained high traffic, for example during batch payment processing, yet in almost all cases clients can distribute their requests more and still operate within the rate limits.
- Load shedding is introduced as a complementary mechanism for incident situations, where low-priority requests are dropped to let more critical ones succeed when services are degraded.
- A load shedder is described as making decisions based on system-wide state rather than individual user behavior, helping keep core business functionality running during emergencies.
- Stripe runs four limiters in production, with the Request Rate Limiter called the most important and suggested as the starting point for improving API robustness.
- The Request Rate Limiter caps each user at N requests per second and is described as the primary, frequently used tool for handling high traffic volumes.
- Stripe reports that this limiter is constantly triggered and rejected millions of requests in a month, particularly in test mode when scripts run out of control.
- The same request rate limits apply in both test and live modes so that development and production behavior match and scripts do not see unexpected rate-related side effects when moving to production.
- After studying traffic patterns, Stripe added a brief burst ability that allows short-lived traffic spikes above the configured cap, such as those created by flash sales.
- The Concurrent Requests Limiter restricts the number of in-flight API requests per user rather than calls per second, shifting the model to “only X requests simultaneously.”
- Stripe notes that some endpoints are resource-intensive and can lead to slow responses and retries, which further overload those endpoints; the concurrent limiter helps reduce this feedback loop.
- The concurrent limiter is said to trigger much less often than the request rate limiter (about 12,000 rejections in a month) and is aimed at containing CPU-intensive endpoint usage.
- Before adopting concurrent limiting, Stripe experienced resource contention on expensive endpoints when users made too many parallel calls; the new limiter is credited with eliminating this recurring issue.
- Stripe observes that it can be acceptable to tune the concurrent limiter to reject more traffic than the request-based one because it encourages a different usage pattern based on a fixed number of workers rather than high-frequency retries.
- The Fleet Usage Load Shedder reserves a percentage of the infrastructure for critical API methods so that these calls keep working when capacity is constrained.
- Stripe categorizes requests into critical methods, such as creating charges, and non-critical methods, such as listing charges, and tracks counts of each using a Redis cluster.
- A fraction of infrastructure is always reserved for critical traffic; for example, if 20% is reserved, any non-critical traffic above its 80% share is rejected with HTTP 503.
- This fleet load shedder was only activated on a very small fraction of requests in a given month, yet Stripe notes that in other months it has helped prevent outages.
- The Worker Utilization Load Shedder operates at the worker level and is presented as the final safety layer when workers begin to back up with requests.
- Stripe divides incoming traffic into four categories for this shedder: critical methods, POSTs, GETs, and test mode traffic.
- The system continuously monitors workers with available capacity and, when a machine becomes too busy, it starts dropping lower-priority traffic, beginning with test mode.
- If shedding test mode requests restores the worker to a healthy state, traffic can be gradually reintroduced; if not, the shedder escalates and drops more categories.
- Stripe emphasizes that shedding and reintroducing traffic must happen slowly to avoid oscillations in system state, and describes tuning the rate through trial and error until it could shed a substantial fraction within a few minutes without flapping.
- The worker utilization shedder rejected around 100 requests in a month, but Stripe credits it with helping faster recovery during past load incidents and frames it as damage control compared to the more preventative earlier mechanisms.
- For implementation, Stripe uses the token bucket algorithm, where each user has a bucket that loses tokens on each request and refills at a steady rate, with requests rejected when the bucket is empty.
- Redis is used as the backing store for these token buckets, and Stripe notes that teams can either run Redis themselves or rely on managed services such as AWS ElastiCache.
- When integrating rate limiters, Stripe recommends wiring them into middleware in a way that prevents limiter bugs or Redis failures from blocking requests, which involves catching exceptions and failing open to keep the API functional.
- Stripe advises deciding upfront on appropriate HTTP status codes for rate limiting (such as 429 for too many requests or 503 for unavailable service) and returning actionable error messages to clients.
- Safeguards like kill switches and feature flags are recommended so that operators can quickly disable limiters if they misfire, along with alerts and metrics to monitor how often limiters fire.
- Stripe suggests dark launching each limiter first to observe what traffic would be blocked, then adjusting thresholds so that the API remains up without breaking existing user patterns, potentially coordinating with some users to adjust their code.
- In its conclusion, Stripe states that rate limiting is a powerful way to make APIs ready for scale and that not all strategies need to be present from the start; they can be added as needs arise.
- The recommended rollout sequence is to begin with the Request Rate Limiter to prevent abuse, then add the other three mechanisms over time to address distinct problem classes.
- Stripe also recommends following careful launch practices for new limiters, including safe error handling, feature flags, and strong observability to track trigger rates.
- To support implementation, Stripe links to a GitHub gist sharing production-based code details for rate limiters similar to those described.
