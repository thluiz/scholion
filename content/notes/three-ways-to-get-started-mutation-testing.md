---
title: "Three Ways To Get Started With Mutation Testing"
date: '2026-11-16T20:08:26+00:00'
category: webclip
summary: 'Article describes three easy approaches to start using Muzak for mutation testing: focus on critical files, run only on changed lines in CI, or run the full suite occasionally.'
tags: ["mutation-testing", "elixir", "testing-strategy"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Three Ways To Get Started With Mutation Testing"
    url: "https://devonestes.com/three-ways-to-get-started-with-mutation-testing"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/devonestes-com--three-ways-to-get-started-mutation-testing.md"
    kind: repo
---

The text presents three simple ways to start using Muzak for mutation testing after functionality from Muzak Pro was added to Muzak. It explains how to focus on a small set of critical modules, how to integrate mutation testing into CI on only recently changed lines, and how to occasionally run a full mutation pass to build a backlog of improvements.

## Reading notes

- Muzak has gained significant features from Muzak Pro, making it easier to integrate mutation testing into regular workflows.
- The author outlines three easy entry points for teams, each with different tradeoffs so that different needs can be met.

- One approach is to run mutation testing only on the most important modules in an application.
- Examples of critical behavior include authorization to prevent data leaks, billing logic to ensure correct payments, and complex code for key third-party integrations.
- Restricting mutations to these files helps reduce runtime while focusing on areas where regressions would be most damaging.
- A `critical` profile in `.muzak.exs` can use `mutation_filter` to target specific file paths and set `min_coverage` for strict expectations.
- The `mutation_filter/1` function can return a list indicating that all possible mutations should be generated for all lines in specified files.
- Setting `min_coverage` to a high value like 98.0 means the process exits with failure if more than 2% of mutations are not caught by tests.
- Teams can trigger `mix muzak --profile critical` manually to periodically assess test effectiveness in these important modules.
- This focused-profile idea can be combined later with continuous approaches to keep critical code checked regularly.

- Another option is to use mutation testing in CI only on lines changed since a prior git commit.
- A `ci` profile in `.muzak.exs` can define `mutation_filter` logic driven by `git log` and `git diff` output.
- The example `mutation_filter` uses a custom separator to parse recent commits and authors from `git log`.
- It identifies the last commit made by a different author to use as the comparison point in the diff.
- The function then obtains a diff with zero context lines from that commit using `git diff -U0`.
- Several regular expressions are used to parse the diff format and track current file names and line numbers.
- While reducing the diff, the code tracks only lines marked as added, using the plus sign indicator in the parsed output.
- The result is a map where keys are files and values are changed line numbers, derived from the diff.
- The function discards changes in test files by rejecting paths that start with `test/`.
- It also filters to only Elixir source files with the `.ex` extension.
- The author describes the `mutation_filter/1` function as complex but summarizes its intent as mutating only lines changed since the last commit by a different author.
- Teams can adjust the logic to match their workflow, such as using the last merge commit, while the example works even for workflows without merge commits.
- This CI approach is presented as a common pattern because it avoids wasting time running all mutations on every CI run.

- A third option is to run mutation testing across the whole codebase.
- The author notes that mutation testing can be slow but points out that computers often remain idle and can be used for these long runs.
- Running the full process once can produce a list of uncovered or weakly tested areas for teams to improve over time.
- As an example, a developer might start `mix muzak` before leaving for a long weekend and let it run without supervision.
- When the run completes, likely before the developer returns, it provides useful information on where tests can be strengthened.
- For very slow test suites, this full-run approach might still be impractical.
- Large applications may hit Muzak’s current limit of 1000 mutations.
- If the test suite runs under 220 seconds, the author suggests that 1000 mutations can realistically complete over a regular weekend.
- With a 275 second test suite, 1000 mutations are expected to finish over a three-day weekend.
- The text mentions that Muzak Pro offers more options for speeding up mutation testing.
- Muzak Pro also includes many additional mutators, giving more thorough insight into how well tests cover the application.
