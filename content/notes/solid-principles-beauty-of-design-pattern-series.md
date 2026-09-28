---
title: "SOLID Principles: The Beauty of Design Pattern Series"
date: '2022-08-03T10:06:08-03:00'
category: webclip
summary: 'The page presents SOLID as a set of OOP concepts for making software easier to change, and links poor design to rigidity, fragility, duplication, slow modules, and unnecessary complexity.'
tags: ["solid-principles", "object-oriented-programming", "design-patterns"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "SOLID Principles: The Beauty of Design Pattern Series"
    url: "https://towardsdev.com/solid-principles-19f5a8438638"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-08/towardsdev-com--solid-principles-beauty-of-design-pattern-series.md"
    kind: repo
---

The page argues that software design should make future change easier, because applications become difficult to develop when dependencies between modules are poorly managed. It introduces SOLID as five OOP concepts and frames design patterns as tools for building software that can adapt over time.

## Reading notes

- Software design is about placing source code well and managing how data flows between code.
- Good design from the start makes software easier to change later.
- When one module depends closely on others, a change in one part can force changes across several modules.
- SOLID is presented as five OOP concepts: Single Responsibility, Open-Closed, Liskov Substitution, Interface Segregation, and Dependency Inversion.
- Design patterns are described as a way to study recurring development problems.
- SOLID and design patterns are compared to tools used to make a wooden chair.
- Software built without design is described as fragile when change is requested.
- Software development should happen through iterative meetings with the client, not through a one-time big design phase.
- An initial prototype should be simple and flexible.
- Big Up Front Design is rejected because real conditions often differ from early plans.
- Delivery time cannot be predicted in advance because requests and business conditions change.
- Software built for one company cannot be assumed to fit another company in the same way, because the human factor differs.
- Design smells include rigidity, fragility, immobility, viscosity, and needless complexity.
- Rigidity means small changes are hard to make.
- Fragility means changing one part breaks others.
- Immobility refers to duplicated code that makes changes harder.
- Viscosity appears when modules are too large and slow to run.
- Needless complexity comes from code that is no longer needed but still remains in the system.
- Poor design can reduce competitiveness by slowing service, causing overdue receivables, and harming inventory flow.
