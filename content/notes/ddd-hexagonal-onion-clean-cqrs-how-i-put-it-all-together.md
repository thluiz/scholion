---
title: "DDD, Hexagonal, Onion, Clean, CQRS, … How I put it all together"
date: '2020-09-07T14:36:54-03:00'
category: webclip
summary: 'Herberto Graca explains how he combines Ports & Adapters, Onion, DDD layers, and CQRS into an explicit architecture with inward dependencies, ports, adapters, components, and buses.'
tags: ["software-architecture", "ddd", "cqrs", "ports-and-adapters"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "DDD, Hexagonal, Onion, Clean, CQRS, … How I put it all together – @hgraca"
    url: "https://herbertograca.com/2017/11/16/explicit-architecture-01-ddd-hexagonal-onion-clean-cqrs-how-i-put-it-all-together/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-09/herbertograca-com--ddd-hexagonal-onion-clean-cqrs-how-i-put-it-all-together.md"
    kind: repo
---

The post presents “Explicit Architecture” as a way to combine EBI, Ports & Adapters, Onion Architecture, DDD layers, and CQRS. It separates user interfaces, application core, and infrastructure, then places ports inside the core and adapters outside it.

It also describes application and domain layers, domain services, domain events, and component-level segregation by bounded context. For coordination across components, it uses events, a shared kernel, queries, or direct calls through a discovery service when needed.

## Reading notes

- The application core is the part that actually does the work, while user interfaces only trigger it.
- Ports define how tools use the application core or how the core uses tools, and they belong inside the business logic.
- Primary adapters translate delivery mechanisms into calls to the application core.
- Secondary adapters implement ports and connect the application core to tools such as databases or search engines.
- The direction of dependencies must point inward, which expresses inversion of control at the architectural level.
- The application layer contains use cases, application services, ports, and command or query handlers.
- Application services or command handlers typically load entities, trigger domain logic, and persist the changes again.
- Application events represent outcomes of a use case and can trigger side effects such as emails, notifications, or another use case.
- The domain layer contains domain services and the domain model, and it stays unaware of the application layer.
- Domain services hold domain logic that involves multiple entities but does not belong inside the entities themselves.
- The domain model contains entities, value objects, enums, and domain events.
- The coarse-grained code organization should follow components and bounded contexts, not only layers.
- Components should be decoupled from each other and can use events, a shared kernel, eventual consistency, or a discovery service.
- A component can query data owned by another component, but it should not change data it does not own.
- When components keep local copies of other components’ data, owner components publish domain events so copies can be updated.
- Without a command or query bus, controllers depend on an application service or a query object.
- Query objects return raw data in DTOs that are injected into view models.
- With a command or query bus, the controller depends on the bus and on a command or query, while handlers are wired by configuration.
- The article closes by stressing that these patterns are guidelines and that the actual architecture depends on the project context.
