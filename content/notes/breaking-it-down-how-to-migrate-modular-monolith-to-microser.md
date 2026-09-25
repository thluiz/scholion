---
title: "Breaking It Down: How to Migrate Your Modular Monolith to Microservices"
date: '2026-09-25T22:32:19+01:00'
category: webclip
summary: 'The article says to migrate one module at a time, first tightening boundaries and data ownership, then extracting a low-coupling module, switching communication to HTTP or messaging, and adding an API gateway and data migration plan.'
tags: ["microservices", "modular-monolith", "api-gateway", "data-migration"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Breaking It Down: How to Migrate Your Modular Monolith to Microservices"
    url: "https://www.milanjovanovic.tech/blog/breaking-it-down-how-to-migrate-your-modular-monolith-to-microservices"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/milanjovanovic-tech--breaking-it-down-how-to-migrate-modular-monolith-to-microser.md"
    kind: repo
---

The article argues that a modular monolith can become the starting point for microservices if its module boundaries, data ownership, and public APIs are already clear. It recommends extracting one module at a time, starting with a self-contained module that has low coupling and a distinct business role.

After extraction, the article says direct calls should be replaced with HTTP or messaging, resilience should be added for network failures, and an API gateway can provide one entry point for clients. For data, it presents two paths: copy everything and switch over, or synchronize data gradually while traffic moves to the new service.

## Reading notes

- Tighten module boundaries first, so each module has a distinct responsibility and minimal dependencies.
- Ensure each module owns its data exclusively, with no shared tables or cross-module database access.
- Define clean public APIs between modules instead of reaching into internals.
- Choose a first module that is low-coupling, high-cohesion, distinct in purpose, and likely to gain from separate scaling.
- Move that module into a new project and give it a separate database to enforce independence.
- Replace direct method calls with HTTP API calls after extraction.
- Use messaging for asynchronous communication, with tools such as RabbitMQ, Amazon SQS and SNS, or Azure Service Bus.
- Add retries and timeouts with resilience patterns because network communication introduces new failure modes.
- Use an API gateway as a single entry point when the number of services grows.
- Let the gateway route requests by path and handle concerns such as rate limiting, caching, and request or response transformation.
- For data migration, either copy schema and data to a new database and switch over, or synchronize data while traffic shifts gradually.
- Keep a backup and rollback plan for the migration.
- Separate database schemas in the monolith make the migration easier.
