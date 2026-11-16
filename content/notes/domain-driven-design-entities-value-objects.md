---
title: "Domain-Driven Design: Entities, Value Objects, and How To Distinguish Them"
date: '2026-11-16T04:45:10+00:00'
category: webclip
summary: 'Explains DDD tactical design through entities and value objects, focusing on identity, equality, mutability, and when each model fits. It also shows how aggregates relate to entities and VOs.'
tags: ["domain-driven-design", "entities", "value-objects", "aggregates"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Domain-Driven Design: Entities, Value Objects, and How To Distinguish Them"
    url: "https://blog.jannikwempe.com/domain-driven-design-entities-value-objects"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/blog-jannikwempe-com--domain-driven-design-entities-value-objects.md"
    kind: repo
---

Entities and value objects are presented as basic building blocks of tactical DDD. The post explains that entities are defined by continuity and identity, while value objects have no conceptual identity and are defined by their attributes. It also argues that the choice depends on the domain.

## Reading notes

- Entities are for objects that need to be tracked over time and recognized as the same object even when attributes change.
- A strong sign of an entity is a status-like attribute or a domain rule that requires matching by identity rather than by attributes.
- Value objects describe characteristics of something and have no conceptual identity.
- Value objects are treated as complex attributes of entities or other value objects.
- Value objects should be immutable, so changing one attribute means creating a new instance.
- The post recommends using value objects by default and assigning identity only when the domain requires it.
- Entities use identity equality, while value objects use structural equality.
- The example compares a `Student` entity by matriculation number and an `Address` value object by its fields.
- Whether something is an entity or a value object depends on the domain, so the same concept can play different roles in different contexts.
- An aggregate is a cluster of entities and value objects treated as one unit for changes, with one entity as the aggregate root.
