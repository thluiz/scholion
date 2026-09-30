---
title: "How to write unit tests"
date: '2022-04-07T20:26:20-03:00'
category: webclip
summary: 'The page defines unit tests as automatic checks against expectations, explains their value for safety, modularity, and speed, and outlines scaffolding, mocking, structure, and TDD.'
tags: ["unit-tests", "testing", "test-driven-development", "mocking"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to write unit tests"
    url: "https://how-to.dev/how-to-write-unit-tests"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-04/how-to-dev--how-to-write-unit-tests.md"
    kind: repo
---

The page presents unit tests as a way to set explicit expectations about code and let a machine verify whether the code meets them. It says testing libraries such as Jest, Jasmine, and Chai are just tools, and the key point is having automatic validation.

It also describes how tests help: they give fast and reliable checks, support refactoring, push you to think about responsibilities between units, and can make coding faster once the test exists. The page recommends building test scaffolding first, using mocks for dependencies, keeping setup, execution, and assertions separate, and using test-driven development when appropriate. It also notes that when exploring solutions, you may delay tests, and that legacy code without tests can still be improved by adding tests while working on it.

## Reading notes

- Unit tests set expectations about code so a machine can check whether the code meets them.
- In JavaScript projects, testing libraries such as Jest, Jasmine, and Chai are examples of tools for automatic validation.
- Tests can make code easier to check, safer to refactor, more modular, and faster to work with over time.
- Before testing real behavior, it helps to set up scaffolding and confirm that the test setup works at all.
- Mocks replace dependencies, and dependency injection can make mocking easier.
- A clear test structure separates mocks, execution, and expectation checks.
- In test-driven development, you write the test first, let it fail, add the implementation, and then improve code and tests without changing the logic.
- When exploring solutions, it can make sense to postpone tests for a while.
- Legacy code without tests can still be improved by adding tests gradually while working on it.
