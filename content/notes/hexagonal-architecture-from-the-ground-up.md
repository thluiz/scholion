---
title: "Hexagonal Architecture from the Ground Up"
date: '2022-05-18T15:36:11-03:00'
category: webclip
summary: 'The article contrasts layered architecture with hexagonal architecture and argues that ports and adapters keep domain logic at the center, make boundaries cleaner, and support easier testing and change.'
tags: ["hexagonal-architecture", "ports-and-adapters", "layered-architecture", "domain-driven-design"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Hexagonal Architecture from the Ground Up | by Matthew Lucas | May, 2022 | Level Up Coding"
    url: "https://levelup.gitconnected.com/hexagonal-architecture-from-the-ground-up-28f2a1097063"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-05/levelup-gitconnected-com--hexagonal-architecture-from-the-ground-up.md"
    kind: repo
---

Hexagonal architecture is presented as a way to keep the valuable center of a system, its domain and application services, separated from user interfaces, databases, and other outside concerns. The article starts from layered architecture, shows how its boundaries can blur, and then turns the model so dependencies point inward.

Ports are described as interfaces for both driving and driven interactions, and adapters are the concrete pieces that connect external systems to those ports. The article says this structure helps maintain clean boundaries and easier testing, while also adding interface and adapter overhead that may be too much for simple software.

## Reading notes

- A farm is used as the opening analogy for separating functional areas so they do not interfere with one another.
- In software, the goal is to tame complexity and keep systems easy to change.
- The Single Responsibility Principle is used to group things that change for the same reasons and separate things that change for different reasons.
- Layered architecture keeps related parts together and depends only on the same or lower layers.
- The article says layer boundaries can blur over time, especially when developers use shortcuts to ship features.
- A layered model also fits only one dimension well, which makes adding inputs like a CLI, REST API, or event stream awkward.
- In the hexagonal model, the user interface drives the application, while the domain and application services sit in the center.
- The driving and driven sides are both outside the core and do not provide value by themselves.
- Dependencies point inward to the domain, following the Dependency Inversion Principle.
- Ports are interfaces on both the driving side and the driven side.
- Adapters implement those ports and translate between external systems and the application.
- Multiple systems can connect to the same port, including test harnesses and different database technologies.
- The article closes by saying the approach improves boundaries and evolution, but adds boilerplate and is usually better suited to more complex applications.
