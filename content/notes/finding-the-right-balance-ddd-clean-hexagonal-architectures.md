---
title: "Finding the Right Balance Between DDD, Clean and Hexagonal Architectures"
date: '2026-09-25T01:24:34+01:00'
category: webclip
summary: 'The article argues for a practical mix of Clean Architecture, DDD and Hexagonal Architecture, keeping domain logic isolated, favoring immutable domain objects, and avoiding boilerplate that adds little value.'
tags: ["clean-architecture", "ddd", "hexagonal-architecture", "kotlin"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Finding the Right Balance Between DDD, Clean and Hexagonal Architectures"
    url: "https://dev.to/y9vad9/digging-deep-to-find-the-right-balance-between-ddd-clean-and-hexagonal-architectures-4dnn?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--finding-the-right-balance-ddd-clean-hexagonal-architectures.md"
    kind: repo
---

The article says architectural choices should balance theory with practical implementation. It describes how the author combines Clean Architecture, DDD, and Hexagonal Architecture in TimeMates, while avoiding strict rules that create unnecessary boilerplate.

## Fichamento

- Clean Architecture is presented as a separation of presentation, domain, and data layers, with business logic kept out of the presentation layer.
- The domain layer should hold business rules, and the presentation layer should focus on UI and platform-specific work.
- DDD is framed around modeling the application after the business domain through domain objects.
- Value objects are immutable, identity-less domain concepts whose equality depends on their values.
- Semantic value objects are recommended instead of raw primitives when the domain needs validation and clearer meaning.
- Domain entities are defined by stable identity over time, even when their attributes change.
- The article prefers immutable entities, including versions that return new instances after a change.
- Aggregates are described as consistency boundaries that enforce invariants across related domain objects.
- Aggregate creation and updates should go through controlled factories or commands so invariants are not bypassed.
- Aggregates should reference other aggregates by ID rather than embedding them directly.
- Domain services are mentioned as a place for business logic that does not fit inside an aggregate.
- Anemic domain entities are criticized because they spread logic across controllers or use cases, weaken encapsulation, and make testing harder.
- The TimerState example is used to show how state objects can hold behavior instead of being passive containers.
- The article says not to force behavior into objects when there is nothing meaningful to aggregate, and to keep KISS in mind.
- Ubiquitous Language is presented as using names that match the business domain and are understandable to non-programmers.
- Hexagonal Architecture is described as isolating the core domain from frameworks, databases, and other external systems.
- Inbound ports are the operations the outside world uses to reach the domain, and outbound ports are the services the domain needs from outside.
- The author prefers to use repositories or use cases directly instead of introducing extra port terminology in every case.
- Adapters implement ports and connect the domain to external systems.
- The article warns against tying repositories and use cases to data sources in the mental model, since the domain should stay agnostic about where data comes from.
- The author’s TimeMates structure uses domain, data, dependencies, and presentation, with data split into database and network concerns.
- Common core types are reused only when they are broadly shared, avoid duplicate validation, and are not overly complex.
- The author replaces inbound ports with use cases in practice, while keeping outbound ports as interfaces needed by the domain.
