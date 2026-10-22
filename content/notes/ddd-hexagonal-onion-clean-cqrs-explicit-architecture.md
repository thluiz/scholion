---
title: "DDD, Hexagonal, Onion, Clean, CQRS, … How I put it all together"
date: '2020-09-07T09:29:49-03:00'
category: webclip
summary: 'The post groups Ports & Adapters, Onion, DDD layers, and CQRS into an explicit architecture centered on the application core, with inward-pointing dependencies and decoupled components.'
tags: ["software-architecture", "ddd", "ports-and-adapters", "cqrs"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "DDD, Hexagonal, Onion, Clean, CQRS, … How I put it all together – @hgraca"
    url: "https://herbertograca.com/2017/11/16/explicit-architecture-01-ddd-hexagonal-onion-clean-cqrs-how-i-put-it-all-together/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-09/herbertograca-com--ddd-hexagonal-onion-clean-cqrs-explicit-architecture.md"
    kind: repo
---

The post presents “Explicit Architecture” as a way to combine DDD, Hexagonal, Onion, Clean Architecture, and CQRS. It centers the application core, separates internal code from external tools, and keeps dependencies pointing inward so the business logic stays isolated from user interfaces and infrastructure.

## Reading notes

- The system is split into user interface code, the application core, and infrastructure code.
- Ports belong inside the business logic, while adapters belong outside it.
- Primary adapters translate delivery mechanisms into application core calls.
- Secondary adapters implement ports and are injected where the application core needs them.
- The application layer contains use cases, application services, command handlers, ports, and application events.
- The domain layer contains entities, value objects, enums, domain services, and domain events.
- Components should be organized by domain or bounded context rather than by layer.
- Components should stay decoupled through architectural mechanisms such as events, a shared kernel, eventual consistency, or a discovery service.
- A component may query data from another component, but it should not change data it does not own.
- With a command bus, the controller depends on the bus and on a command or query, while handlers are configured separately.
- The overall goal is a codebase that is loosely coupled and highly cohesive, with architecture adapted to the actual needs of the application.
