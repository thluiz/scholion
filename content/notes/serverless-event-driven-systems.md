---
title: "Serverless Event-Driven Systems"
date: '2022-04-12T15:18:06-03:00'
category: webclip
summary: 'The article argues for event-driven-first serverless architectures around Amazon EventBridge, showing how loose coupling, async flow, schemas, and retries improve resilience and deployability.'
tags: ["serverless", "event-driven-architecture", "amazon-eventbridge", "aws"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Serverless Event-Driven Systems 🚀 | by Lee James Gilmore | Level Up Coding"
    url: "https://levelup.gitconnected.com/serverless-event-driven-systems-9617c6406064"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-04/levelup-gitconnected-com--serverless-event-driven-systems.md"
    kind: repo
---

The article argues that serverless systems should be designed event-driven first, with Amazon EventBridge as the default event bus. It contrasts synchronous service calls with loosely coupled async events, then walks through benefits such as independent testing, deployment, scaling, versioned schemas, and separate data stores.

It also covers practical pitfalls and mitigations, including idempotency, FIFO deduplication behavior, batch failures in SQS, schema versioning, event size limits, dead-letter queues, SNS for low-latency cases, and the difference between synchronous and asynchronous Lambda invocations.

## Reading notes

- Build serverless architectures around events first, rather than chaining services together through synchronous HTTPS calls.
- Synchronous service-to-service calls increase latency and make failures spread across tightly coupled domain services.
- Event-driven services stay loosely coupled, so one failing service can recover later without bringing down the others.
- Dead letter queues can hold unprocessed records for later reprocessing after a downstream service returns.
- Event-driven systems are presented as individually testable, individually deployable, versioned through shared schemas, and able to scale independently.
- An event is described as a past state change in a domain, while a command is an intent for another domain to do work in the future.
- EventBridge is framed as the default serverless event bus because it is serverless, supports schema discovery and code generation, filters by content, transforms inputs, archives and replays events, and encrypts data in transit and at rest.
- The example solution deploys a payslip upload flow where one service receives the upload and another generates PDF files into S3.
- Idempotency is required because EventBridge delivers at least once, so the same event can be seen more than once.
- The article suggests idempotency keys, UUID v5, and control databases as ways to avoid duplicate side effects.
- With EventBridge to SQS FIFO, content-based deduplication can be undermined because EventBridge adds a unique EventID, so identical payloads may not deduplicate as expected.
- Input transformations can remove the Event ID so FIFO deduplication works on the remaining body.
- When Lambda processes batched SQS messages, one failed record can send the whole batch back, so processing should be idempotent and partial batch failure handling is useful.
- The schema registry should be used carefully, with auto discovery in development only, and schemas can also be added manually as OpenAPI 3.0 definitions.
- For payloads larger than EventBridge’s 256 kb limit, the article uses S3 for the large object and passes the bucket and key in the event.
- If EventBridge cannot route to a target, a standard SQS queue can be used as a dead letter queue.
- SNS is suggested only for cases that need very low latency or very high message throughput.
- Lambda invoked from SQS is handled synchronously, while Lambda targets from EventBridge are asynchronous and need explicit failure handling such as Lambda Destinations or other error targets.
