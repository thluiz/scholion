---
title: "4 Tips for Mastering Test-Driven Development"
date: '2020-07-11T21:38:32-03:00'
category: webclip
summary: 'The article explains TDD basics and four practical techniques: isolate external calls, test rollbackable migrations, watch code coverage, and use property-based testing to catch bugs earlier.'
tags: ["test-driven-development", "unit-testing", "code-coverage", "property-based-testing"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "4 tips for mastering test-driven development"
    url: "https://www.welcometothejungle.com/fr/articles/tips-test-driven-development"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-07/welcometothejungle-com--4-tips-for-mastering-test-driven-development.md"
    kind: repo
---

The article presents TDD as a short development cycle in which tests are written before code, then revisited requirement by requirement. It also notes trade-offs such as more test code, maintenance costs, and slower CI, while arguing that the approach can reduce overbuilding and make refactoring safer.

## Reading notes

- Write tests before code, one requirement at a time, and repeat the cycle until the feature is complete.
- TDD can limit unnecessary code, help avoid missed requirements, and make refactoring safer because loosely coupled code is easier to isolate.
- Test suites can grow quickly, become harder to maintain, and lengthen CI, so tests should stay small and the slow or less relevant ones should be reviewed.
- Keep modules isolated from external effects by replacing dependencies with a stub or test double, so unit tests do not trigger Slack calls or other outside behavior.
- For Ecto migrations, test rollback behavior too, because some migrations cannot be reversed automatically with `change/0`.
- Use `up/0` and `down/0` when a migration needs explicit rollback logic, such as removing and later restoring a column.
- Run a rollback test across all migrations to catch problems before a deployment rollback is needed.
- Use code coverage reports to spot relevant lines that were not exercised, while remembering that full coverage does not guarantee bug-free code.
- Property-based testing generates many inputs from declared properties and can reveal bugs that example-based tests miss.
- The article uses `Wttj.Math.sum/2` to show that a function can pass fixed examples while still failing on generated inputs.
- Property-based tests complement unit tests rather than replace them, and are presented as useful once the codebase has stabilized.
