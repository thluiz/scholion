---
url: "https://hellointerview.substack.com/p/design-a-rate-limiter?utm_source=substack&utm_medium=email"
captured_at: "2025-08-11T22:17:32+01:00"
title: "Design a Rate Limiter - by Hello Interview"
domain: "hellointerview.substack.com"
---
## Understanding the Problem

A rate limiter controls how many requests a client can make within a specific timeframe. It acts like a traffic controller for an API - allowing, for example, 100 requests per minute from a user, then rejecting excess requests with an HTTP 429 "Too Many Requests" response. Rate limiters prevent abuse, protect servers from being overwhelmed by bursts of traffic, and ensure fair usage across all users.

The breakdown designs a request-level rate limiter for a social media platform's API, focusing on server-side implementation, at a scale of 1 million requests per second across 100 million daily active users, targeting under 5ms latency overhead and high availability with eventual consistency across nodes.

## Core Entities

**Rules**: the rate limiting policies that define limits for different scenarios - requests per time window, which clients it applies to, which endpoints it covers.

**Clients**: the entities being rate limited (users, IP addresses, API keys), each with associated rate limiting state.

**Requests**: the incoming API requests evaluated against rate limiting rules, carrying client identity, endpoint, and timestamp.

## Where to Place the Rate Limiter

Three options, with different trade-offs:

**In-Process** (bad): rate limiting built into each application server's code, checking local in-memory counters. Fast, but each server only knows its own traffic - with 5 servers behind a load balancer, a 100 requests/minute limit becomes effectively 500 requests/minute globally, and gets worse if the load balancer's routing is uneven.

**Dedicated Service** (good): the rate limiter becomes its own microservice that application servers call before processing a request. Gives rich context (subscription tier, account status, business logic) and precise global limits, but adds a network round trip to every request, a new point of failure (fail open vs fail closed), and operational complexity (the service itself needs high availability).

**API Gateway/Load Balancer** (great): the rate limiter runs at the edge, examining every incoming request before it reaches application servers. Most popular in production because it's conceptually simple and application servers never see blocked requests. The limitation is context - the gateway only sees what's in the HTTP request itself (headers, URL, IP), so rules like "premium users get 10x higher limits" require that status to be encoded in a JWT or similar. State storage (an in-memory store like Redis) becomes an external dependency.

The breakdown picks the API Gateway approach: centralized control without adding network calls to every request.

## Identifying Clients

Three keys: **User ID** (best for authenticated APIs, typically from a JWT in the Authorization header), **IP Address** (for public APIs without accounts, from X-Forwarded-For, but unreliable behind NATs/corporate firewalls), **API Key** (for developer APIs, from X-API-Key). Real systems layer multiple rules simultaneously - per-user, per-IP, global, and endpoint-specific limits - and enforce the most restrictive one that applies.

## Rate Limiting Algorithms

**Fixed Window Counter**: divides time into fixed windows (e.g. 1-minute buckets) and counts requests per window, resetting to zero at each new window. Simple (a hash table of client ID to counter/window-start pairs), but has boundary effects - a user can make 100 requests at 12:00:59 and another 100 at 12:01:00, getting 200 requests in 2 seconds.

**Sliding Window Log**: keeps a log of individual request timestamps per user, discarding anything older than the window and counting what remains. Perfectly accurate, no boundary effects, but memory-heavy - a user making 1000 requests/minute needs 1000 stored timestamps, which doesn't scale to millions of users.

**Sliding Window Counter**: a hybrid that approximates sliding windows using two fixed-window counters (current and previous), weighted by how far into the current window the request arrives (e.g. 30% into the window → 70% of the previous window's count + 100% of the current). Much better accuracy than fixed windows, minimal memory (two counters per client), but it's an approximation that assumes even traffic distribution within windows.

**Token Bucket**: each client has a bucket holding a certain number of tokens (burst capacity), refilled at a steady rate. Each request consumes one token; no tokens means rejection. Handles both sustained load (refill rate) and bursts (bucket capacity), and is simple to implement (tracking tokens and last_refill_time per client). Companies like Stripe use this because it accommodates bursty API traffic while still enforcing overall limits. This is the algorithm chosen for the design.

## Implementing Token Bucket with Redis

Each gateway instance can't keep bucket state in its own memory - that reproduces the same coordination problem as in-process rate limiting, since a load balancer splits a user's traffic across gateways. Redis becomes the central source of truth.

The flow: a request arrives at a gateway; it fetches the client's bucket state from Redis via HMGET (tokens, last_refill); it calculates how many tokens to add based on elapsed time since the last refill (capped at bucket capacity); it updates the bucket atomically via a Redis MULTI/EXEC transaction (HSET tokens, HSET last_refill, EXPIRE to clean up inactive buckets after an hour); then it allows or rejects based on the updated token count.

There's still a race condition: the read (HMGET) happens outside the transaction, so two simultaneous requests for the same user could both read the same initial count and both get allowed, granting 2 requests when only 1 token was available. The fix is to move the entire read-calculate-update logic into a single atomic operation using a Redis Lua script, which reads, calculates, and updates the bucket in one atomic step.

Why Redis fits: sub-millisecond responses, automatic cleanup via EXPIRE, high availability through replication, and atomic operations that eliminate race conditions between gateways.

## Handling Rejected Requests

Most rate limiters fail fast: immediately return HTTP 429 rather than queueing excess requests. Queueing sounds user-friendly but consumes memory and processing resources, encourages users to retry (adding more load), and makes API response times unpredictable. It only makes sense for batch processing systems that can afford to wait - for interactive APIs, fast failure is almost always right.

A well-formed 429 response includes X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset (a Unix timestamp), and often Retry-After, letting well-behaved clients implement proper backoff instead of hammering the API with failed retries.
