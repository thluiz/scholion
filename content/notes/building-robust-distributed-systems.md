---
title: "Building robust distributed systems"
date: '2022-04-12T15:01:57-03:00'
category: webclip
summary: 'The article argues that resilient distributed systems reduce inter-component coupling, isolate errors with SLAs and fallbacks, and add buffers such as asynchronous communication and extra capacity.'
tags: ["distributed-systems", "fault-tolerance", "sla", "backpressure"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Building robust distributed systems | Kislay Verma"
    url: "https://kislayverma.com/software-architecture/building-robust-distributed-systems/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-04/kislayverma-com--building-robust-distributed-systems.md"
    kind: repo
---

The article says robust distributed systems come from limiting connections between components, assuming every component can fail, and leaving slack in the system. It groups the approach into three parts: minimize dependencies, isolate errors, and add buffers.

## Reading notes

- Reduce connections by moving data or functionality into the calling component when possible.
- Duplicate frequently used data locally, cache data that changes over time, and store rarely changing data directly in the component.
- Denormalize data inside a component to avoid looking across multiple entities.
- Package remote functionality as a library when it is critical and heavily used, even if that brings upgrade tradeoffs.
- Use SLAs so each component declares latency, error-rate, and concurrency limits.
- Let callers time out, retry idempotent operations, and open circuit breakers when failures continue.
- Add random backoff to retries so callers do not retry all at once and overload a recovering component.
- Use backpressure to drop new requests when a component is close to breaching its SLA.
- Use asynchronous communication such as message buses so callers do not depend on a tight SLA.
- Add hardware capacity as a buffer when load grows and cost allows it.
