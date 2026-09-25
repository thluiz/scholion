---
title: "Elixir's Secret Weapon"
date: "2026-09-23T18:54:06+01:00"
category: webclip
has_commentary: false
summary: "Explains Elixir's with special form as the fix for nested case statements when chaining dependent operations that each return a tagged {:ok, _} / {:error, _} tuple."
tags:
  - elixir
  - error-handling
  - erlang
sources:
  - title: "Elixir's Secret Weapon"
    url: "https://blog.drewolson.org/elixirs-secret-weapon/?utm_campaign=elixir_radar_96&utm_medium=email&utm_source=RD+Station"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/blog-drewolson-org--elixirs-secret-weapon.md"
    kind: repo
---

Drew Olson starts from the Erlang-borrowed idiom of tagged tuples: functions return {:ok, value} on success or {:error, reason} on failure, so errors become values a caller pattern-matches on explicitly instead of exceptions that interrupt control flow. The idiom holds up for a single call, but chaining several dependent operations that can each fail forces a case statement nested inside a case statement, one level per operation.

The with special form fixes that. It runs a list of operations against <- patterns, carrying forward each successful match's bindings into the next operation, and stops at the first operation whose result doesn't match, returning that unmatched value directly. An optional else clause intercepts that unmatched value and pattern-matches on it explicitly, instead of just passing it through as the form's return value.

## Reading notes

- Tagged tuples ({:ok, value} / {:error, reason}) turn errors into values a function always returns, letting the caller pattern-match on success and failure explicitly rather than relying on exceptions.
- Chaining several tagged-tuple operations that each depend on the last one's result forces nested case statements, one level of nesting per operation.
- The with form lists operations against <- patterns; each operation can use the bindings from the ones before it, and the do block runs only once every operation has matched.
- with stops at the first operation whose result fails to match its pattern and returns that unmatched value as the whole form's result.
- An optional else clause pattern-matches on that unmatched value directly, instead of leaving the caller to handle whatever with returns.
- with also supports guard clauses on each operation, beyond the plain pattern match.
