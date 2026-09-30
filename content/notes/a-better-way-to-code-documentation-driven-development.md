---
title: "A Better Way To Code: Documentation Driven Development"
date: '2022-04-09T17:03:15-03:00'
category: webclip
summary: 'The article argues that writing documentation first can clarify API shape and project scope before code is implemented, often reducing later refactors and helping teams communicate requirements more clearly.'
tags: ["documentation-driven-development", "api-design", "software-development"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "A Better Way To Code: Documentation Driven Development"
    url: "https://dev.to/this-is-learning/a-better-way-to-code-documentation-driven-development-1kem"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-04/dev-to--a-better-way-to-code-documentation-driven-development.md"
    kind: repo
---

The article argues that starting with documentation can help clarify API shape and project scope before implementation begins. It uses `calculateUserScore` to show how requirements can shift when details like assists or bonus points appear, and how those changes affect the function design.

It presents documentation-driven development as a way to create a self-feedback cycle around APIs and scope. The author also notes that documentation can take many forms, including design mockups, tickets, future plans, examples, and tests, and says the idea is close to BDD and ATDD.

## Reading notes

- TDD asks you to write tests before implementation, but tests are still code and can be hard to keep aligned with changing implementation details.
- Starting with implementation and adding tests later can weaken the early pressure to define the API.
- A function like `calculateUserScore` can change as requirements expand, for example when assists and bonus points are added.
- Those changes can force refactors in multiple parts of the codebase if the API was not thought through early.
- Miscommunication of scope can happen between teams, between individuals, or inside one person's own thinking.
- TDD can push you to address the API ahead of time, but it does not solve scope confusion by itself.
- Writing documentation first can surface API decisions before code is written.
- The article shows a doc-first sketch for `calculateUserScore`, including a signature, usage examples, and a possible future shape.
- The author argues that docs can lead to a better choice for the `kills` property before implementation locks it in.
- Documentation is described broadly, including mockups, reference docs, well-formed tickets, future plans, and other ways of communicating ideas.
- Tests are also presented as a form of documentation, especially when they show usage examples.
- The article says documentation-driven development is not a one-time write-and-forget process; docs and code can influence each other.
- In interviews, writing comments before the solution is presented as a way to show workflow and clarify goals.
- The term DDD is linked to Behavioral Driven Development and Acceptance Test-Driven Development, which also validate behavior through stronger communication.
- The author says the approach helped refine goals in the CLI Testing Library project and related documentation work.
