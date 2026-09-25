---
title: "No excuses, write unit tests"
date: '2026-09-25T00:12:27+01:00'
category: webclip
summary: 'The text argues that unit testing is worth the upfront time because it exposes how functions behave, makes API changes visible, and catches bugs before they reach production. It also says that writing tests often leads to clearer, smaller, easier-to-test code.'
tags: ["unit-testing","software-testing","code-quality"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "No excuses, write unit tests"
    url: "https://dev.to/jackmarchant/no-excuses-write-unit-tests"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--no-excuses-write-unit-tests.md"
    kind: repo
---

The text argues that unit testing is worth the upfront time because it exposes how functions behave, makes API changes visible, and catches bugs before they reach production. It also says that writing tests often leads to clearer, smaller, easier-to-test code.

## Reading notes

- Unit testing is presented as a useful practice even when teams worry about time, coverage disagreements, or broken tests.
- A unit can be any isolated block of code, including a function, though groups of functions are harder to test because they have more moving parts.
- Functions that always return the same output for the same inputs are easier to test because expectations can be set from their return values.
- Simple tests for `add` and `minus` are used to show that even basic functions can be checked with expected outputs.
- Testing simple functions can reveal how hard they are to use, what risks they carry in real use, and whether they do too much.
- The text says unit testing takes extra time upfront, but broken tests can be fixed earlier than bugs in production.
- If an API changes, tests should break; if they do not, code may reach production with other broken uses.
- Writing tests can improve code clarity because developers start thinking about testability while writing the code.
- The recommended flow is to make the code work, then write a test, then refactor.
- Broken tests are treated as useful because they force developers to understand inputs, outputs, and the impact of API changes.
- The author says there is no good reason to avoid at least some unit testing and recommends starting small and expanding from there.
