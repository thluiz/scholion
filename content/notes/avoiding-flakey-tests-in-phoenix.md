---
title: "Avoiding flaky tests in Phoenix"
date: '2026-11-16T20:09:28+00:00'
category: webclip
summary: 'Explains how list equality assertions cause flaky Phoenix tests due to unordered DB results and suggests using a helper to compare list contents without relying on order.'
tags: ["testing", "phoenix", "elixir"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Avoiding flaky tests in Phoenix"
    url: "https://devonestes.com/avoiding-flakey-tests"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/devonestes-com--avoiding-flakey-tests-in-phoenix.md"
    kind: repo
---

The text argues that direct list equality assertions are a major source of flaky tests in Phoenix applications. When tests compare lists coming from database queries without an explicit `ORDER BY`, they end up relying on an order that the database does not guarantee, causing intermittent failures. Instead, tests should check that two lists contain the same items without assuming a specific order.

To handle this, the author suggests defining a helper function, `contains_exactly/2`, that checks list contents irrespective of order by using list difference operations. This clarifies the intent of the test, avoids accidental ordering assertions, and suits typical test data sizes where performance is not a concern. Direct list equality should only be used when ordering is an intentional part of the behavior under test.

## Reading notes

- The author identifies direct list equality assertions as a leading cause of unnecessary test failures.
- An example is given where a test asserts that a list equals `[user_1, user_2, user_3]`, which assumes a specific order.
- A pattern-matching example with a list head and tail is shown as a related source of order-dependent flakiness.
- Phoenix applications often interact with a database, and queries without `ORDER BY` provide no guarantee of record order.
- Databases may appear to return records in creation order because they often read them in disk storage order, but this behavior is not guaranteed.
- Relying on default database ordering can cause tests to pass most of the time and fail intermittently.
- Such tests inadvertently check list ordering even when order is not relevant to the function's behavior.
- The proposed solution is a helper function `contains_exactly/2` that compares list contents without assuming order.
- This helper works by verifying that subtracting each list from the other yields an empty list, ensuring both contain the same elements.
- The helper is described as a light wrapper around two boolean checks that reads clearly in test code.
- The function is not optimized for high performance, but that is acceptable for typical test scenarios with small lists.
- The recommendation is to avoid direct list equality assertions unless list order is a deliberate and documented part of the tested behavior.
