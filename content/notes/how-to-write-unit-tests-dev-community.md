---
title: "How to write unit tests"
date: '2022-04-14T09:17:31-03:00'
category: webclip
summary: 'The article explains what unit tests are, how they help with validation, refactoring, modularity, and speed, and suggests starting with scaffolding, mocking, structure, and test-driven development.'
tags: ["unit-tests", "testing", "javascript", "test-driven-development"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to write unit tests - DEV Community 👩‍💻👨‍💻"
    url: "https://dev.to/marcinwosinek/how-to-write-unit-tests-52dl"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-04/dev-to--how-to-write-unit-tests-dev-community.md"
    kind: repo
---

The article defines unit tests as a way to set expectations about code so a machine can verify whether the code meets them. It also says the specific testing library matters less than having a way to automatically validate an application.

It presents unit tests as useful for checking code quickly and reliably, giving confidence during refactoring, encouraging clearer responsibility between parts of the code, and speeding up development after the initial test is written. It recommends first setting up testing scaffolding, then using mocks for dependencies, keeping tests in three phases, and using test-driven development when it fits the problem.

## Reading notes

- Unit tests set explicit expectations about code so the machine can verify them.
- In JavaScript projects, libraries such as Jest, Jasmine, and Chai are examples of tools for testing.
- The article treats automatic validation as the main point, not the specific library.
- Writing tests helps check behavior quickly and reliably.
- Good test coverage makes refactoring safer.
- Unit tests push you to think about units and the division of responsibility between them.
- Tests can make coding faster once the initial test case exists.
- The suggested starting point is to install the testing library and set up the testing script.
- A naming convention helps organize test files, such as `plane-ticket.spec.js`.
- The article suggests checking simple things first, like whether an object is an object or a function is a function.
- Mocks replace dependencies of the unit being tested.
- Dependency injection makes mocking easier.
- The article separates a test into setting up mocks, running the code, and checking expectations.
- Test-driven development starts with a failing test before the implementation exists.
- If exploration is needed, the article recommends delaying tests until the path is clearer.
- For legacy code without tests, it suggests starting to add tests while working on the codebase.
