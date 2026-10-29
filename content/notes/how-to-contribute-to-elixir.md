---
title: "How to contribute to Elixir"
date: '2016-02-29T11:03:31-03:00'
category: webclip
summary: 'The page explains how to build, test, and verify Elixir changes locally, from running make compile and make test to targeting single packages, using a custom build in an app, and cleaning bad builds.'
tags: ["elixir", "testing", "contributing", "build-tools"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to contribute to Elixir"
    url: "https://dockyard.com/blog/2016/02/02/how-to-contribute-to-elixir?utm_campaign=elixir_radar_36&utm_medium=email&utm_source=RD+Station"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-02/dockyard-com--how-to-contribute-to-elixir.md"
    kind: repo
---

The post outlines a practical workflow for contributing to Elixir. It starts with cloning the repository, checking that the code compiles, and running the full test suite before making changes. After editing, it suggests recompiling, narrowing tests to a package or a single test file when needed, and using a custom build in a real application to confirm the changes behave as expected.

## Reading notes

- Clone Elixir, run `make compile`, and then `make test` to confirm the project builds and the tests pass.
- If either step fails, the author recommends asking for help in the `#elixir-lang` IRC channel on Freenode.
- After making changes, recompile and test again from the project root.
- Elixir is split into packages under `lib/`, including `eex`, `elixir`, `ex_unit`, `iex`, `logger`, and `mix`.
- For package-level work, the Makefile includes commands such as `make test_ex_unit`.
- To run one test file, compile first and then run `bin/elixir -r` with the test helper and the chosen test file.
- For real-world testing, prepend the custom build’s `bin/` directory to `$PATH` so it is used first.
- Check the active binaries with `which elixir` and `which mix`.
- Recompile dependencies for the custom build with `mix do deps.clean, deps.get, deps.install`.
- If compilation produces a bad build, run `make clean` and try again.
- The post also notes that changes may need documentation, and points to Elixir’s writing documentation guide.
