---
title: "Dependency inversion in architectural patterns"
date: '2024-11-22T13:27:56+00:00'
category: webclip
summary: 'The article says dependency inversion is common in architectural patterns because it protects a core from change through interfaces or adapters. It distinguishes cases where suppliers follow a defined SPI from cases where adapters translate between incompatible APIs.'
tags: ["dependency-inversion", "architectural-patterns", "adapters", "interfaces"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Dependency inversion in architectural patterns | ITNEXT"
    url: "https://itnext.io/dependency-inversion-in-architectural-patterns-aab2323f4118"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2024-11/itnext-io--dependency-inversion-in-architectural-patterns.md"
    kind: repo
---

Dependency inversion appears in several architectural patterns because it lets a core depend on interfaces instead of concrete external components. The article says this is more general than OOP and shows two main ways it is used: defining an SPI or inserting adapters.

## Reading notes

- Plugins and Hexagonal Architecture both use dependency inversion to protect the core from variability in external components.
- In Plugins, small pieces of code contribute customizable parts of algorithms and decision making, and the core team may not know how many plugins will exist.
- In Hexagonal Architecture, adapters break the core’s dependency on external libraries or services.
- Each adapter depends on the core’s SPI and on the API of the adapted component.
- Adapters make components look identical to the core when interfaces and contracts vary across vendors or versions.
- Stub adapters help develop and test the core in isolation.
- Microkernel, top-down Hierarchy, Cell-Based Architecture, Layers, and Services may also use similar ideas to decouple their parts.
- A higher layer can depend on a lower layer that implements a standardized interface such as POSIX or SQL.
- A service can use an anti-corruption layer or CQRS views as adapters to protect itself from changes in other components.
- If suppliers can follow your rules, the article says to define an SPI.
- If suppliers are independent, the article says to add adapters that translate between your SPI and their APIs.
