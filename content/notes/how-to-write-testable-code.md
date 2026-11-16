---
title: "How to write testable code"
date: '2026-11-16T19:06:55+00:00'
category: webclip
summary: 'The page shows how injecting dependencies makes a class easier to unit test, more loosely coupled, and easier to extend, using a PHP account state transition example.'
tags: ["unit-testing", "dependency-injection", "loosely-coupled-code", "mockery"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to write testable code"
    url: "https://dev.to/ddarrko/how-to-write-more-testable-code-oi7"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--how-to-write-testable-code.md"
    kind: repo
---

The page explains unit testing as testing the smallest possible unit of software without relying on dependencies. It argues that testable code supports maintainable, extensible software and usually aligns better with SOLID design.

## Reading notes

- Unit tests should run against an individual class or method and avoid dependencies such as other classes, libraries, or the database.
- The goal of software is a maintainable and extensible codebase that meets business requirements, and effective unit tests help encourage SOLID code.
- A class that creates its own dependencies inside methods is hard to unit test because those dependencies will be called during the test.
- Moving Account and validator dependencies into the constructor makes the class depend on interfaces rather than concrete implementations.
- With dependency injection, the class becomes more loosely coupled and easier to change if validator behavior changes later.
- Private methods are implementation details and should not be the focus of unit tests.
- The public transition method has two paths: validation passes and the account transitions, or validation fails and the account is not saved.
- The tests use Mockery to mock the account and validator, define expected calls, and assert how many times each method is called.
- In the passing case, the account is expected to set its state to active and save once, while the validator returns true.
- In the failing case, the validator returns false and the account methods are expected never to be called.
- The refactor makes the code both more testable and more flexible.
