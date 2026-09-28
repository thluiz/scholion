---
title: "Patterns That Every Developer Should Know"
date: '2022-07-01T17:35:36-03:00'
category: webclip
summary: 'The post presents four design patterns every developer should know—Singleton, Builder, Factory, and Facade—showing how each one simplifies a common problem and when it becomes useful.'
tags: ["design-patterns", "singleton", "builder", "factory", "facade"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Patterns That Every Developer Should Know"
    url: "https://blog.upperdine.dev/patterns-that-every-developer-should-know"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-07/blog-upperdine-dev--patterns-that-every-developer-should-know.md"
    kind: repo
---

The post argues that developers meet recurring problems across domains, and design patterns name common solutions to those problems. It uses TypeScript examples and focuses on patterns that may be worth recognizing even when they are not used every day.

## Reading notes

- Singleton is described as a class that exposes one instance and a global reference to it; the example is app configuration loaded once instead of read from disk on every instantiation.
- The author notes that Singleton is often called an anti-pattern because it violates Single Responsibility and adds global state, but says it still fits components that should have only one instance.
- Builder is recommended for highly customizable objects; the example turns logger configuration into a dedicated builder with chained methods and a build step.
- The Builder example is used to keep configuration readable when an options object grows in scope.
- Factory is presented as a way to centralize object creation when construction logic becomes complex; the tax example shows subclass selection based on item state.
- The post links Factory to the problem of scattering creation checks across the codebase and says a factory keeps the creation logic in one place.
- Facade is described as a simplified interface for third-party libraries, services, or databases; the user service example extracts email sending into an EmailSender class.
- The Facade example is tied to Single Responsibility and Dependency Inversion because the consuming class only depends on what it needs.
- The closing advice says design patterns are easy to overuse and should be applied only when they simplify code rather than make it more complex.
- The post ends by preferring readability over cleverness and recommending Head First Design Patterns and refactoring.guru for further reading.
