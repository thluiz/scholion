---
title: "Clean Architecture Essentials"
date: '2020-02-22T12:11:45+00:00'
category: webclip
summary: 'The article argues that software architecture should be described by use cases, not by frameworks. It presents Clean Architecture as a use-case-centered style with ports, adapters, fakes, and deferred technology choices.'
tags: ["clean-architecture", "use-cases", "ports-and-adapters", "evolutionary-architecture"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Clean Architecture Essentials"
    url: "https://paulovich.net/clean-architecture-essentials"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/paulovich-net--clean-architecture-essentials.md"
    kind: repo
---

Clean Architecture is presented as an architecture style organized around use cases rather than layers or frameworks. The article says software should reveal what it does at first glance, and that the user interface and persistence should be shaped to serve the core needs.

It also connects Clean Architecture with ports and adapters, fake implementations, TDD Outside-In, and stable versus unstable dependencies. The text shows how use cases, presenters, repositories, and controllers are separated, and how major technology decisions can be postponed.

## Reading notes

- Describe software by use cases instead of frameworks, layers, or technology details.
- Use cases are the central organizing structure in Clean Architecture.
- Use cases are algorithms that transform input into output and should stay close to business vocabulary.
- Primary actors start use cases, and secondary actors are affected by them.
- Ports and adapters separate application ports from technology-specific adapters.
- Fake implementations help the system run without I/O and support feedback early in development.
- TDD Outside-In starts from test cases, then use cases, then fakes, then real adapters, and only later the user interface.
- Interfaces such as repositories and account abstractions are stable and general.
- Concrete classes tied to Entity Framework or request models are specific and unstable.
- The dependency direction goes inward, and classes that change together should be packaged together.
- A good architecture defers major decisions and lets the simplest component come first.
- The presenter translates use case output into WebApi responses, while the controller stays away from output-message decisions.
