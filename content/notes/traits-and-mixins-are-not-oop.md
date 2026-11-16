---
title: "Traits and Mixins Are Not OOP"
date: '2020-02-22T12:11:52+00:00'
category: webclip
summary: 'The article argues that traits and mixins inject code into classes, expose private structure, and weaken encapsulation, making objects harder to understand and maintain than composable decorators.'
tags: ["traits", "mixins", "encapsulation", "decorators"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Traits and Mixins Are Not OOP"
    url: "https://yegor256.com/2017/03/07/traits-and-mixins.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/yegor256-com--traits-and-mixins-are-not-oop.md"
    kind: repo
---

The article treats traits and mixins as code that is injected into a class and that can reach private state directly. In the Ruby examples, a book class can pull behavior from modules, change how its title is printed, and combine several modules to alter the result.

## Reading notes

- Traits and mixins are described as features that were brought into object-oriented programming and are presented as harmful rather than useful.
- A module can be extended into a class so its methods are called directly, but the article says this is less readable because it hides where a method comes from.
- Mixins become more relevant when included in a class, where they can override behavior such as `to_s`.
- Several mixins can be combined to change output, including capitalization and abbreviation of a book title.
- The article says mixins have full access to the class, including private attributes like `@title`.
- It argues that mixins assume knowledge of a class’s internal structure and therefore violate encapsulation.
- The text compares mixins with annotations, DTOs, getters, and utility classes, saying they split object functionality into places where the object does not see it.
- As an alternative, it points to composable decorators, which keep objects small and cohesive while layering behavior on top.
- The conclusion is that mixins make objects more complex, less readable, and harder to maintain.
