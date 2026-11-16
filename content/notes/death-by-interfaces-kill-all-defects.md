---
title: "Death by Interfaces?"
date: '2026-11-16T07:57:20+00:00'
category: webclip
summary: 'The post argues that interfaces can add navigation friction, hide runtime specifics, and make maintenance harder. It also warns that large interfaces often violate ISP and suggests base classes can be a better fit in some cases.'
tags: ["interfaces", "software-maintenance", "solid", "inheritance"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Death by Interfaces? - Kill All Defects"
    url: "https://web.archive.org/web/20200923061658id_/https://killalldefects.com/2020/01/19/death-by-interfaces/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/web-archive-org--death-by-interfaces-kill-all-defects.md"
    kind: repo
---

The post argues that interfaces in object-oriented code are useful for decoupling, but their tradeoffs are often underestimated. It says they can make code harder to navigate, obscure the concrete implementation in use, and add small maintenance costs that accumulate over time.

It also warns that large interfaces often violate the Interface Segregation Principle and can encourage classes with too many responsibilities. As an alternative, it suggests considering base classes when a system needs only limited flexibility, while still weighing the limits of inheritance.

## Reading notes

- Interfaces are presented as contracts that enable decoupling, such as depending on an abstraction instead of a specific data provider.
- Using interfaces can make navigation slower because the jump from a type usually lands on the interface definition rather than the concrete implementation.
- Interfaces can hide runtime specifics, making it easier to lose track of the actual implementation used in production.
- Refactoring can become more cumbersome because changes often have to be made in the interface and in every implementation.
- Dead members inside an interface are harder to detect, so unused parts of the contract can remain longer.
- Large interfaces are described as a common violation of the Interface Segregation Principle.
- Broad interfaces can be harder to implement, often end up with only one concrete implementation, and can encourage classes that violate single responsibility.
- The post suggests that base classes can sometimes be a better fit when the goal is limited flexibility, reuse, or dependency injection support.
- Base classes also have tradeoffs, including constrained implementations and the risk of increasing inheritance depth.
- The overall recommendation is to choose between interfaces, base classes, and concrete classes according to the needs of the codebase, not by default.
