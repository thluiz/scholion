---
title: "If at first you don't get an answer..."
date: '2020-05-15T23:42:55+00:00'
category: webclip
summary: 'The post argues that poor timeout and retry settings can break distributed systems, and that fixing them is often a configuration change. It explains connection versus request timeouts, retry limits, backoff, and latency-aware settings.'
tags: ["microservices", "timeouts", "retries", "distributed-systems"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "If at first you don't get an answer..."
    url: "https://dev.to/aws/if-at-first-you-don-t-get-an-answer-3e85"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--if-at-first-you-dont-get-an-answer.md"
    kind: repo
---

The post says that bad timeout and retry policies can break a distributed systems architecture, but are often easy to fix with configuration changes. It warns against using the same default settings everywhere, because that can trigger work amplification when one slow dependency causes retries to pile up.

## Reading notes

- Timeout and retry settings are often copied from framework defaults or sample code, which makes failures more likely across a whole microservice system.
- Limiting retries to zero or one helps reduce work amplification, especially in deeper parts of the service chain.
- It is useful to document current timeout settings and how they can be changed, since some are dynamic and others are hard coded or hidden in libraries.
- The text distinguishes connection timeouts from request timeouts, using letters and phone calls as analogies.
- Connection timeouts cover the time to establish a connection, while request timeouts cover the full flow after the connection is made.
- Timeouts should be telescoped through the system, with longer limits at the edge and shorter limits deeper in the backend.
- For human-facing interactions, the post suggests giving up after about 10 seconds and aiming for web page loads below 4 seconds.
- Fallback code is often poorly tested, so slow or failed dependency responses are a better target for chaos testing.
- When requests build up during timeouts, old queued requests can clog the system, so dropping a full timeout queue can be better than processing it in order.
- If there is only one endpoint or database instance, retries should use bounded exponential backoff with jitter to avoid thundering herd behavior.
- In deeply nested flows, the best timeout may depend on the specific request path, so dynamic timeout policies may be needed.
- Connection timeouts should be short for co-located microservices and longer for AWS regions or third-party APIs.
- The post recommends setting connection timeouts to about 10x round trip latency when possible.
- For horizontally scaled services, retries should move to a different instance instead of repeating the same connection to one failed instance.
- Fast failures are preferred, because retrying the same failed instance immediately is usually pointless.
