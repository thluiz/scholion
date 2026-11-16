---
title: "Variables? We Don’t Need No Stinking Variables | C# Discards"
date: '2026-11-16T08:15:16+00:00'
category: webclip
summary: 'C# 7.0 discards let you ignore values you do not need, from unused results and out parameters to tuples, null checks, tasks, and switch patterns.'
tags: ["csharp", "discards", "out-parameters", "pattern-matching"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Don't Code Tired | Variables? We Don’t Need No Stinking Variables"
    url: "https://web.archive.org/web/20200516032544id_/https://dontcodetired.com/blog/post/Variables-We-Dont-Need-No-Stinking-Variables-C-Discards"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/web-archive-org--variables-we-dont-need-no-stinking-variables-csharp-discards.md"
    kind: repo
---

C# 7.0 introduced discards as intentionally unused temporary values. The page shows how `_` can stand in for results you do not care about, including ignored method results, `out` parameters, tuple elements, null-check expressions, tasks, and switch patterns.

## Reading notes

- `_ = 1 + 1;` discards the result of an addition, and the discarded value cannot be accessed later.
- When calling `int.TryParse`, `_` can replace an `out` variable that is never used.
- An expression-bodied method can return `int.TryParse(@int, out _)` when only the boolean result matters.
- In a method with several `out` values, the unused ones can be written as `_` while keeping the one needed value.
- Tuple deconstruction can ignore fields with `(_, age) = GenerateDefaultPerson();` when only one element matters.
- A null check can be written as `_ = message ?? throw new ArgumentNullException(nameof(message));` to avoid a redundant temporary variable.
- `_ = Task.Run(() => SayHello());` discards the task result, but the page notes that exceptions are suppressed in this form.
- A `switch` can use `case var _:` to catch unsupported types after the more specific cases.
