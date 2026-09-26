---
title: "My Laws of Test Driven Development"
date: '2024-09-07T15:31:59+00:00'
category: webclip
summary: 'Dennis Doomen lists 19 heuristics for TDD-focused tests, emphasizing practical test scope, functional names, clear arrange-act-assert structure, restrained mocking, and readable failures.'
tags: ["test-driven-development", "unit-tests", "test-design", "bdd"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "My Laws of Test Driven Development"
    url: "https://www.continuousimprover.com/2021/10/laws-test-driven-development.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2024-09/continuousimprover-com--my-laws-of-test-driven-development.md"
    kind: repo
---

Dennis Doomen presents 19 practical heuristics for writing tests in a way that supports design, readability, and maintenance. He frames them as laws only loosely, saying they are really principles that helped him avoid common mistakes while practicing Test Driven Development.

## Reading notes

- TDD should not be followed exactly as books describe it; when designing new code, it can make sense to sketch responsibilities, fill in details, and then move back to test-first work.
- Different test levels matter, including class, component, module, API, and UI tests, and arguing over a strict boundary between unit and integration tests is not useful.
- Test scope should match how classes work together, which parts are used directly, and which parts are implementation details.
- Test names should describe the scenario being validated, not the names of classes, methods, or UI buttons.
- Naming should stay functional and consistent within the code base, even if frameworks like JEST or Jasmine need a slightly different shape.
- Tests should make the starting state, the action, and the assertion easy to see without digging through helper methods or base classes.
- Each test should cover one scenario only.
- Test code should be treated as part of the code base and should be reviewed, refactored, and evolved like production code.
- DRY can go too far in tests when it hides important details inside base classes or fixtures.
- Unimportant setup should be hidden, while the relevant parts of a test should stay visible, using tools like Object Mothers or Test Data Builders.
- Assertions should stay focused on what matters in that test, including only the message fragment or object properties that are relevant.
- Inline literal strings and numbers can be clearer in tests than shared constants.
- A test framework that runs tests in parallel can expose concurrency issues and race conditions early.
- Tests should target observable behavior rather than private members or direct database access.
- Production code should generally not be used on the expectation side of an assertion.
- Test classes should end with `Specs` to emphasize their role as specifications.
- Mocking should be used sparingly, especially when a test uses many mocks or starts to mock the subject under test itself.
- When a test fails, the expected and actual outcomes should be clear without needing a debugger, and a good assertion library can improve that.
- Some tests are state-based and fit Arrange-Act-Assert, while others are more orchestrational and fit a BDD style with multiple outcomes.
