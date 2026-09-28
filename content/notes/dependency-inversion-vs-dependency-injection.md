---
title: "Dependency Inversion vs. Dependency Injection"
date: '2022-05-27T17:18:29-03:00'
category: webclip
summary: 'The article distinguishes dependency inversion as a principle that favors abstractions over concrete implementations, and dependency injection as a pattern that supplies those dependencies at runtime.'
tags: ["dependency-inversion", "dependency-injection", "solid", "software-design"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Dependency Inversion vs. Dependency Injection | by Guy Erez | Better Programming"
    url: "https://betterprogramming.pub/straightforward-simple-dependency-inversion-vs-dependency-injection-7d8c0d0ed28e"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-05/betterprogramming-pub--dependency-inversion-vs-dependency-injection.md"
    kind: repo
---

The article separates dependency inversion from dependency injection. Dependency inversion is presented as a design principle that asks code to depend on high-level abstractions rather than low-level implementations. Dependency injection is presented as a pattern that creates a dependency outside the code that uses it and supplies it at runtime, which makes code more configurable and easier to test.

It also explains why the word inversion is used. In older layered architectures, higher-level components depended directly on lower-level components. The inverted approach reverses that direction by relying on abstractions instead of concrete details.

## Reading notes

- Dependency inversion is a design principle that favors high-level abstractions over low-level implementations.
- That approach keeps code agnostic to implementation details and easier to adapt when implementations change.
- Dependency injection is a design pattern that separates creation from use and provides objects at runtime.
- Injecting dependencies can make code more configurable and easier to test by allowing mocks.
- The article connects dependency injection to dependency inversion by saying injection helps code rely on abstractions.
- The term inversion refers to older layered architecture, where higher-level components depended directly on lower-level components.
- The inverted model shifts that dependence toward abstractions instead of concrete components.
