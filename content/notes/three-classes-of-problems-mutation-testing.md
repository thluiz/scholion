---
title: "Three Classes of Problems Found by Mutation Testing"
date: '2026-11-16T20:08:26+00:00'
category: webclip
summary: 'Article shows three common bug types that escape line-based coverage but are exposed by mutation testing: multiple paths per line, untested side effects, and missing Elixir pin operator.'
tags: ["mutation-testing", "test-coverage", "elixir"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Three Classes of Problems Found by Mutation Testing"
    url: "https://devonestes.com/examples-of-mutation-testing"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/devonestes-com--three-classes-of-problems-mutation-testing.md"
    kind: repo
---

The article explains why mutation testing can reveal issues that traditional line-based code coverage misses, using Elixir examples. It walks through two functions with full coverage but real bugs, then categorizes the issues into three problem types and argues that mutation testing provides stronger feedback than relying on humans or simple coverage metrics.

## Reading notes

- Example module `CoverExample` has two functions: `write_json_to_file/2`, which encodes a map to JSON and writes it to a file, and `stringify_keys/1`, which converts map keys to strings with special handling for maps and tuples.
- The associated tests exercise both functions and `cover` reports 100% code coverage for the module.
- Despite full coverage, neither `write_json_to_file/2` nor `stringify_keys/1` behaves as intended, showing that coverage alone can give a false sense of safety.

- In `stringify_keys/1`, an `if` condition checks `is_map(k) or is_tuple(k)`, but the test data only includes a tuple key and never a map key.
- Because the test never uses a map key, changing the condition to `is_nil(k) or is_tuple(k)` would not break any tests, even though it likely introduces incorrect behavior for users.
- Line-based coverage counts that `if` line as covered, but it cannot tell that one logical branch involving map keys is never actually exercised.
- Mutation testing instead focuses on variations in the code’s logic, highlighting missing test cases when mutants affecting untested branches survive.

- In `write_json_to_file/2`, variable naming suggests the function should write JSON content to a file at a given path, then return the JSON string.
- Running the test reveals that the file system contains a file whose name is the JSON string and whose contents are the test’s temporary path, indicating the arguments to `File.write/2` are reversed.
- This bug persists while tests pass and coverage is 100% because the test only checks the return value, not the side effect on the file system.
- The article emphasizes that a large portion of meaningful application behavior consists of side effects, and untested side effects create a high chance of regressions.

- The third issue, called the “missing pin” problem, is specific to Elixir’s pattern matching in tests.
- The test for `stringify_keys/1` uses `assert expected = stringified`, which performs a pattern match and rebinds `expected` instead of comparing values.
- Because of this, the test passes even if `stringify_keys/1` returns an unexpected value, since the assertion treats that value as the new `expected`.
- Correcting the assertion to `assert ^expected = stringified` (using the pin operator) or `assert expected == stringified` would surface the failure the test author likely intended.
- The article notes that forgetting the pin operator or confusing `=` with `==` is easy and can silently produce passing tests where failures are expected.

- Without mutation testing, the only ways to uncover these issues are human-driven: the original developer noticing the problem, a reviewer catching it in a pull request, or a tester or user filing a bug report.
- For most teams, there is no automated, scalable mechanism to detect such subtle problems when relying solely on line-based code coverage.
- The article relates code coverage to the Pareto Principle: line-based coverage is relatively cheap to obtain and provides roughly 80% of the benefit.
- Teams that require higher assurance need tools like mutation testing to cover the remaining gap by finding logic-path gaps, untested side effects, and subtle test mistakes that simple coverage metrics miss.
