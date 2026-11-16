---
title: "Refactoring for Tests in Elixir"
date: '2026-11-16T20:10:05+00:00'
category: webclip
summary: 'Author explores how to test Elixir code that calls System.cmd/2, weighing testing private functions, extracting logic, and making a function public to inject a test double.'
tags: ["elixir", "testing", "refactoring"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Refactoring for Tests in Elixir"
    url: "https://devonestes.com/refactoring-for-tests-in-elixir"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/devonestes-com--refactoring-for-tests-in-elixir-system-cmd.md"
    kind: repo
---

The text reflects on how to structure and test Elixir code that interacts with system commands, based on work adding cross-platform system information to Benchee. The author questions whether private functions, especially those using pattern matching for OS-specific behavior, should be tested, and ultimately decides they are implementation details whose tests are not worth maintaining. Faced with testing error handling around `System.cmd/2`, they compare making a function public to inject a test double versus extracting branching logic into a separate, pattern-matched function, and choose the first option for readability and more direct unit testing.

## Reading notes

- The author is returning to open source work and is contributing a cross-platform system information feature to the Benchee benchmarking tool.
- Implementing this feature raises questions about testing private functions in Elixir, especially compared to the author’s Ruby background where private methods were not tested.
- An example shows `cpu_speed/0` delegating to multiple private `cpu_speed/1` clauses that depend on the OS and further delegate to `parse_cpu_for/2` with platform-specific handling.
- Pattern matching in these private functions makes it easy to test each branch of the logic in isolation if they were exposed to tests.
- The author wonders whether private functions in Elixir should be treated as untested implementation details, similar to OOP, or as part of a narrower interface that could merit tests.
- Because the code queries system information, testing the public function directly would require running tests separately on macOS, Linux, and Windows.
- The author decides not to test the private functions, viewing them as implementation details that do not describe public behavior and whose development-time tests should be removed before deployment if they exist.
- A key factor in that decision is that the ongoing maintenance cost of tests for these private functions is judged higher than the benefit.
- Another challenge is testing a helper that wraps `System.cmd/2`, since its behavior depends on the underlying system and can’t be controlled easily in tests.
- The `system_cmd/2` helper handles errors by checking the exit code, printing messages when something goes wrong, and returning "N/A" instead of the raw output.
- Because it is difficult to force predictable system failures, the author looks for ways to test the error handling without relying on actual system behavior.
- One proposed solution is to make the helper function public and take the system call (`System.cmd/2`) as an argument, allowing injection of a test double with predictable behavior.
- The alternative is to keep `System.cmd/2` inside a private helper but extract the branching logic into a separate function that uses pattern matching on the `{output, exit_code}` tuple.
- In the first option, a default argument points to `&System.cmd/2`, but tests can pass a different function to simulate success or failure cases.
- In the second option, the main helper pipes the `System.cmd/2` result into a `handle_errors/1` function that has pattern-matched clauses for success and failure.
- After comparing the two approaches, the author chooses the first option and updates the code accordingly.
- One reason for preferring the first approach is the perceived readability of keeping all relevant logic together in a single function using `if/else` for control flow.
- Another reason is the preference for directly unit testing the `system_cmd/2` behavior, not just the extracted error-handling logic.
- The author notes that this preference may be influenced by prior object-oriented experience but still guides the final decision.
- The text closes by stating that both refactoring options are valid and there is no definitive correct answer between them.
