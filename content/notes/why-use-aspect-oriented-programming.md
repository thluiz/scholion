---
title: "Why use aspect-oriented programming"
date: '2026-09-25T22:33:55+01:00'
category: webclip
summary: 'The article explains how aspect-oriented programming helps manage cross-cutting concerns like logging and authentication, reducing duplication and improving modularity, readability, and maintainability without replacing OOP.'
tags: ["aspect-oriented-programming", "cross-cutting-concerns", "code-maintenance"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Why use aspect-oriented programming"
    url: "https://www.infoworld.com/article/2245539/why-use-aspect-oriented-programming.html?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/infoworld-com--why-use-aspect-oriented-programming.md"
    kind: repo
---

Aspect-oriented programming is presented as a way to handle cross-cutting concerns such as authentication and logging across many parts of an application. The text says it helps avoid duplicated code, keeps applications adaptable, and improves modularity by separating concerns. It also says AOP complements object-oriented programming rather than replacing it.

## Reading notes

- AOP is described as a programming style for managing concerns that cut across many parts of an app, such as authentication and logging.
- It is said to reduce code duplication and help applications stay adaptable to changes.
- The text says AOP increases modularity by separating concerns and reduces clutter in the code.
- AOP is presented as a complement to OOP, offering another way to achieve modularity and reduce duplication.
- An aspect is defined as the modularization of a concern, with logging and authentication given as examples.
- The goal is to handle common functionalities in one place, including logging, authentication, notifications, transaction management, and exception management.
- The article lists key AOP concepts such as aspect, introduction, join point, advice, weaving, target object, and pointcut.
- The benefits named include reduced code clutter, reduced redundancy, easier maintenance, faster development, and improved readability.
- Implementing AOP is described as a two-step process: isolate aspects from business logic, then weave them into the source code where needed.
- The text gives C# attributes as one way to implement AOP and shows a custom attribute applied to a method.
