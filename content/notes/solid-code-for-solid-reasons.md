---
title: "SOLID Code for SOLID Reasons"
date: '2012-05-24T11:02:19-03:00'
category: webclip
summary: 'The post argues that good code should be written for maintainability, with testability as a secondary benefit. It connects SOLID, bounded contexts, and anti-corruption layers to TDD and criticizes using moles or shims to justify weak design.'
tags: ["solid", "tdd", "bounded-context", "anti-corruption-layer"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "SOLID Code for SOLID Reasons | the pluralsight blog"
    url: "http://blog.pluralsight.com/2012/05/22/solid-code-for-solid-reasons/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-05/blog-pluralsight-com--solid-code-for-solid-reasons.md"
    kind: repo
---

Good code should be written because it is easy to maintain, not mainly because it is easy to unit test. The post treats testability as a helpful effect of good design, then links that design to SOLID principles, bounded contexts, and anti-corruption layers.

## Reading notes

- Good code is easy to maintain, and that is the main reason to write it.
- SOLID is presented as a useful starting point for OO code, along with bounded contexts and anti-corruption layers from Domain Driven Design.
- Bounded contexts separate the main code base from external systems, and anti-corruption layers keep one context from leaking into another.
- Small classes are justified by coupling and maintainability problems, not by isolated unit tests or private method testing.
- Dependencies should point to abstractions rather than concretions because this reduces coupling and makes change safer.
- Wrapping third-party dependencies in adapters isolates the code from external change and from mismatched principles.
- The post argues that “it makes it unit testable” should not be the main defense for design choices.
- TDD is described as a way to reveal violations of design principles.
- Moles or shims are criticized because they can hide poorly written code instead of exposing it.
- The author rejects using KISS and YAGNI to dismiss SOLID and context boundaries in legacy or complex cases.
