---
title: "What is the right \"unit\" in unit testing and why it is not a class?"
date: '2026-09-25T23:01:01+01:00'
category: webclip
summary: 'The talk argues that the right unit for testing is defined by scope and functional boundaries, not by classes, and suggests using heuristics to keep tests focused, stable, and valuable.'
tags: ["unit-testing", "tdd", "testability"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "What is the right \"unit\" in unit testing and why it is not a class?"
    url: "https://www.slideshare.net/dennisdoomen/what-is-the-right-unit-in-unit-testing-and-why-it-is-not-a-class"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/slideshare-net--what-is-the-right-unit-in-unit-testing-and-why-it-is-not-a-c.md"
    kind: repo
---

Dennis Doomen presents unit testing as a question of scope rather than class boundaries. The slides use TDD in practice, heuristics for choosing what to test, and examples that show how tests stay useful when they target the real surface area of the code and align with functional boundaries.

## Reading notes

- In practice, TDD starts with class responsibilities, then a first unit test, stubs, a failure for the right reason, an implementation, a passing test, alternative scenarios, and refactoring.
- Code designed for reusability should be tested separately.
- Implementation details should not be tested directly.
- A good test should cover the real surface area.
- If refactoring requires rewriting the tests, the scope is likely off.
- Things in adjacent folders usually belong to separate scopes.
- Returning mocks from mocks often signals a scope issue.
- Testability improves when code is organized by functional boundaries.
- DRY should be applied within those boundaries.
- Dependencies outside the scope should be mocked.
- It is fine to include the database in tests.
- It is fine to test smaller when that adds value.
- The talk advises not to argue about “unit” versus “integration”.
- In the example architecture, command handlers, domain model, event store, projectors, HTTP API, and projections are shown as parts of the system under test with different test fixtures and test data.
