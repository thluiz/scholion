---
title: "Hacking Elixir's Syntax"
date: '2015-06-17T12:06:20-03:00'
category: webclip
summary: 'The author adds underscore support to Elixir binary literals by locating the tokenizer, adjusting its Erlang patterns, and verifying the change with tests before opening a pull request.'
tags: ["elixir", "hacking", "functional-programming"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Hacking Elixir's Syntax"
    url: "http://blog.heldscal.la/elixir-hacking.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-06/blog-heldscal-la--hacking-elixirs-syntax.md"
    kind: repo
---

The post shows a small Elixir language change: support for underscores in binary, hex, and octal literals. The author finds the tokenizer in the Erlang part of the codebase, updates its patterns to ignore underscores, and checks the result with tests.

## Reading notes

- Elixir already supported underscores in decimal numbers, but not in binary notation.
- The codebase was easy to build with `make clean test`.
- `grep` led to the tokenizer tests and then to `elixir_tokenizer.erl`.
- The tokenizer has separate paths for hex, binary, and octal numbers.
- The `is_hex`, `is_bin`, and `is_octal` checks are macros defined in `elixir.hrl`.
- The author first considered adding `_` to the character checks, but instead added a pattern that drops underscores while parsing.
- After the change, `make test_erlang` passed all tests.
- A full `make clean test` also passed.
- The author says the source layout was logical and the code was easy to understand.
- The post presents the existing test suite as what made it easy to find the relevant code.
- The change became a pull request, and a slightly different version was merged.
