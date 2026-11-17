---
title: "Writing (and testing) a custom Credo check"
date: '2026-11-17T15:00:13+00:00'
category: webclip
summary: 'Article explains a workflow for implementing and testing a custom Credo check in Elixir using Credo helpers, mocked source files, and an example check for consistent function definitions.'
tags: ["elixir", "credo", "static-analysis"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Writing (and testing) a custom Credo check"
    url: "https://devonestes.com/writing-and-testing-a-custom-credo-check"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/devonestes-com--writing-testing-custom-credo-check.md"
    kind: repo
---

The text describes a practical workflow for writing and testing custom Credo checks in Elixir. It demonstrates how to test checks using mocked source files and Credo’s helpers, then walks through the implementation of a specific check that enforces consistent function definition styles within a module.

## Reading notes

- The author focuses on the process of writing custom Credo checks and emphasizes that testing is a key part of that workflow.
- Tests use a heredoc with Elixir source code that represents a mocked file to be parsed and checked.
- `Credo.SourceFile.parse/2` is used with the heredoc and a file path string, where the actual path value does not matter for the presented check.
- The custom check is run against the parsed source file, and the test asserts that it returns specific `%Credo.Issue{}` structs.
- The tests rely on helper functions from the `Assertions` library, using tools like `assert_lists_equal` and `assert_structs_equal` to compare actual and expected issues.
- This testing setup allows simple tests over mocked source files and makes inspecting parsed ASTs straightforward when needed.
- The basic skeleton of a custom Credo check defines a module that `use`s `Credo.Check` with options such as `base_priority: :high`, `category: :readability`, and `exit_status: 1`.
- The `run/2` callback receives a `source_file` and optional params, builds `issue_meta` via `IssueMeta.for/2`, and must return a list of `%Credo.Issue{}` structs.
- A helper function like `issue_for/2` is introduced to build issues using `format_issue/2` with a standard message and line number, based on `issue_meta`.
- For the example check, the first step is to collect all function definitions in the module by walking the AST.
- `Credo.Code.prewalk/3` is used to traverse the AST and accumulate data about functions; it behaves similarly to `Enum.reduce/2` while recursing through all nodes.
- Pattern matching in `get_funs/2` targets function definitions (`def` and `defp`), including those with guards (`when`), extracting the function name and its line number.
- The traversal builds a collection (initially shown as a map, then as a list of `{name, line_no}` pairs) that associates function names with the lines where they are defined.
- After collecting function definitions from the AST, the implementation switches to working with the original source lines because the exact syntax of definitions matters for this check.
- `SourceFile.lines/1` returns all lines of the file along with their line numbers, enabling a line-by-line pass over the source.
- In `process_line/3`, when a line number corresponds to a known function definition, a regular expression is used to classify the definition as `:single_line` or `:multiline`.
- The classification logic looks for `def` or `defp` with a function name followed by arguments and either a trailing comma at the end of the line or a `do:` inline form to decide if it is a single-line definition.
- The accumulator built in `process_line/3` groups definition entries by function name, storing lists of `{line_no, def_type}` tuples for each function.
- Lines that are not function definitions, or whose line numbers are not in the functions collection, are ignored and passed through unchanged in `process_line/3`.
- In `process_fun/3`, the first recorded definition for each function serves as the reference style, and subsequent definitions for that function are compared against it.
- For each definition whose style differs from the initial one for that function, a new issue is created with `issue_for/2` and added to the issues list.
- `run/2` ultimately reduces over the collected function definition data to build and return a list of issues describing inconsistent function definition styles.
- When the check implementation is complete, the earlier test passes, confirming that the check correctly identifies inconsistent function definitions on the expected lines.
- The author notes that this particular check could be implemented more simply, but the chosen approach helps showcase the range of Credo helpers available for custom checks.
- According to the text, combining `Credo.Code.prewalk/3`, `SourceFile.lines/1`, `Enum.map/2`, and `Enum.reduce/3` is enough to implement the majority of custom Credo checks a developer might want.
- The author briefly mentions that consistency checks of another kind are more complex and that teams do not typically write those themselves, so they are not addressed in this explanation.
