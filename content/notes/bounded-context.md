---
title: "Bounded Context"
date: '2015-05-14T21:02:30-03:00'
category: webclip
summary: 'Bounded Context is a central DDD pattern for splitting large systems into separate models, each internally consistent, while making relationships between contexts explicit.'
tags: ["domain-driven-design", "strategic-design", "context-map"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "BoundedContext"
    url: "http://martinfowler.com/bliki/BoundedContext.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-05/martinfowler-com--bounded-context.md"
    kind: repo
---

Bounded Context is presented as a central pattern in Domain-Driven Design, especially in strategic design for dealing with large models and teams. Instead of trying to unify a whole domain model, DDD divides a large system into separate contexts with their own unified models and explicit relationships.

## Reading notes

- A model supports communication through a Ubiquitous Language and also serves as the conceptual basis for software design.
- A single unified model becomes harder to maintain as the domain grows and different groups use subtly different vocabularies.
- DDD recognizes that total unification of a large domain model is not feasible or cost-effective.
- Bounded Contexts can contain unrelated concepts and also different models of shared concepts such as products and customers.
- Different contexts may require mapping between polysemic concepts for integration.
- Cultural differences are a common reason for drawing boundaries between contexts.
- Boundaries can also appear within a single application, such as between in-memory and relational database models.
- Relationships between Bounded Contexts are usually shown with a context map.
- Eric Evans’s book and Vaughn Vernon’s book are listed as further reading, along with an example of a bubble context in legacy systems.
