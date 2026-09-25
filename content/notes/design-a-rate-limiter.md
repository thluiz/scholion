---
title: "Design a Rate Limiter"
date: "2026-09-23T18:19:00+01:00"
category: webclip
has_commentary: false
summary: "Hello Interview's breakdown walks a system-design rate limiter from placement decisions through four limiting algorithms, landing on Token Bucket over Redis with a Lua script to close the race condition."
tags:
  - system-design
  - rate-limiting
  - redis
sources:
  - title: "Design a Rate Limiter - by Hello Interview"
    url: "https://hellointerview.substack.com/p/design-a-rate-limiter?utm_source=substack&utm_medium=email"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-08/hellointerview-substack-com--design-a-rate-limiter.md"
    kind: repo
---

The breakdown targets a request-level rate limiter for a social platform's API at a stated scale of 1 million requests per second across 100 million daily users, under 5ms latency overhead. Placement (gateway, microservice, or in-process) and client identification (user ID, IP, API key) get decided first. The comparison across four limiting algorithms is where the real design decisions happen, along with keeping that algorithm's state consistent across every gateway instance without adding a coordination bottleneck of its own.

## Reading notes

- Three placement options compared: in-process (fast, but each server only sees its own slice of traffic, so a 100/minute limit becomes 500/minute effective across 5 servers); dedicated microservice (global state and rich business context, at the cost of a network round trip on every request and a new point of failure); API gateway/load balancer, the pick, centralized and with no added service call per request, but limited to whatever context lives in the HTTP request itself, like headers and IP.
- Client identification layers three keys: user ID (from a JWT), IP address (from X-Forwarded-For, unreliable behind NATs), API key. The piece notes production systems often layer per-user, per-IP, global and endpoint-specific rules at once, enforcing whichever is most restrictive.
- Fixed Window Counter: simplest to implement (a hash table of counter + window-start per client), but has a boundary bug. A user can get 200 requests in 2 seconds by hitting the limit right at a window edge twice.
- Sliding Window Log: perfectly accurate by keeping every request timestamp per user and discarding old ones, but memory cost scales directly with request volume, which breaks down at millions of users.
- Sliding Window Counter: a hybrid that weighs the previous and current fixed windows by how far into the current window a request arrives, trading some accuracy for just two counters per client.
- Token Bucket: the algorithm chosen. Each client holds tokens refilled at a steady rate, consumed one per request; it naturally handles both sustained load and bursts, and the piece notes Stripe uses this approach in production for exactly that bursty-traffic reason.
- Implementation detail: state has to live in Redis, not gateway memory, or the same per-gateway blind spot from in-process limiting reappears. The naive HMGET-then-MULTI/EXEC flow still has a race condition because the read happens outside the transaction; the fix is a single atomic Lua script that reads, recalculates and writes the bucket in one step.
- On rejection: fail fast with HTTP 429 rather than queueing, since queued requests cost memory, invite retries that add more load, and make response times unpredictable. Queueing is reserved for batch systems that can tolerate delay. A complete 429 response carries X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset and often Retry-After so well-behaved clients can back off correctly.
