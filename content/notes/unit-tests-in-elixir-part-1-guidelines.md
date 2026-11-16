---
title: "Unit Tests in Elixir - Part 1"
date: '2026-11-16T20:09:24+00:00'
category: webclip
summary: 'Outlines practical guidelines for Elixir unit tests: parallel execution, single-process focus, behavior-oriented specs, not testing libraries, clear describe blocks, and careful setup use.'
tags: ["elixir", "unit-testing", "exunit"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Unit Tests in Elixir - Part 1"
    url: "https://devonestes.com/unit-tests-in-elixir-part-1"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/devonestes-com--unit-tests-in-elixir-part-1-guidelines.md"
    kind: repo
---

The author presents a personal philosophy of testing in Elixir, emphasizing the value of unit tests and end-to-end tests that reflect real user behavior, and downplaying the importance of intermediate layers in the traditional testing pyramid. They note that defining what counts as a unit test can be difficult, especially when functions call other functions, and introduce a set of guidelines for how they write unit tests in Elixir.

## Reading notes

- The author values unit tests and end-to-end tests that mimic real user behavior, considering other layers in the testing pyramid less important.
- They acknowledge that it can be tricky to define what a unit test is, especially when a function under test calls many other functions.
- The post focuses on basic beliefs about testing in Elixir, with future posts planned for trickier cases like GenServers, message-sending functions, filesystem access, and HTTP calls.
- The guidelines are presented as solid practices the author follows consistently, rather than strict rules.
- Guideline 1: all unit tests should run in parallel, which implies that tests must not rely on shared state.
- Each unit test should operate in its own isolated environment, making parallel execution acceptable.
- Guideline 2: unit tests should cover all behavior in a single function within a single process.
- If a test depends on changes outside a single process, it becomes an integration test because it involves asynchronous interaction between processes.
- It is acceptable for a function under unit test to call other functions, as long as the behavior being tested remains confined to a single process.
- The example `validate_parse_and_format_for_csv/1` shows a function that composes validation, parsing, and formatting functions into a single operation.
- In theory, one could only assert that the composed functions are called with correct data and rely on their own unit tests, but the author dislikes this approach in Elixir and does not elaborate on the reasons here.
- For the composed function, the author prefers tests that express expected outcomes, such as returning a CSV string for valid JSON or an error tuple for invalid JSON.
- They accept that these tests may duplicate coverage from the component functions but see unit tests as specifying desired behavior of a function rather than interactions between objects.
- The author notes a difference between functional programming and object-oriented programming in how tests are framed, and mentions that this took time to internalize.
- Guideline 3: do not test library code; there is no need to verify what a well-documented library already guarantees.
- Using Ecto as an example, the author argues there is no need to test the existence or behavior of associations provided by the library.
- When using a library, developers should trust its documented behavior; if the behavior is not documented, the author suggests the library should not be used.
- Guideline 4: each `describe` block in ExUnit should correspond to one function under test.
- Since ExUnit only allows one level of `describe` nesting, the author uses each block to group tests for a specific function, such as `find_with_posts/1` or `find_with_comments/1`.
- They recommend always including a `describe` block naming the function under test, even when there is currently only a single test, to improve readability and use tests as documentation.
- Guideline 5: use `setup` blocks sparingly, reserving them for cases where significant shared preparation is needed across multiple tests.
- A positive example of `setup` is initializing a `socket` for multiple Absinthe subscription tests.
- Overuse of `setup` can make individual tests harder to read, so it should be applied only when it removes many lines of duplicated code from several tests.
- For simpler shared data, the author prefers module attributes as a first option instead of introducing a `setup` block.
