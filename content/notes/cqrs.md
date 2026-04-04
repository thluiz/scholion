---
title: CQRS
date: '2026-04-04T08:16:25+01:00'
summary: CQRS — Command Query Responsibility Segregation — is a pattern first described by Greg Young. At its heart is the notion that you can use a different model to update information than the model you…
tags:
- software-engineering
- architecture
- design-patterns
has_commentary: true
sources:
- title: CQRS — Martin Fowler
  url: https://martinfowler.com/bliki/CQRS.html
  kind: article
---

CQRS — Command Query Responsibility Segregation — is a pattern first described by Greg Young. At its heart is the notion that you can use a different model to update information than the model you use to read information.

It extends the idea behind Bertrand Meyer's Command Query Separation (CQS) to the architectural level: queries retrieve data without modifying state, commands modify state without returning data. In CQRS, the read model and the write model become separate concerns — potentially separate services, separate databases, separate deployments.

CQRS fits naturally with event-based programming models and Event Sourcing, where state changes are stored as a sequence of events rather than as current state.

Important caveat: for most systems, CQRS adds risky complexity. It's a powerful pattern to have in the toolbox, but should be reserved for situations where the read and write sides have genuinely different requirements — not applied as a default architecture.
