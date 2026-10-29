---
title: "Comparing Elixir and Erlang variables"
date: '2016-01-25T08:48:13-03:00'
category: webclip
summary: 'The article compares Elixir rebinding and Erlang pattern matching, showing how both can cause hidden bugs when variables are added, removed, or reused in changing code.'
tags: ["elixir", "erlang", "variables", "pattern-matching"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Comparing Elixir and Erlang variables"
    url: "http://blog.plataformatec.com.br/2016/01/comparing-elixir-and-erlang-variables/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-01/blog-plataformatec-com-br--comparing-elixir-and-erlang-variables.md"
    kind: repo
---

The article argues that both Elixir and Erlang variables involve implicit behavior, so changing code around them can introduce hidden bugs. Elixir rebinding can silently change which value later code uses, while Erlang pattern matching can turn earlier or later code into a match and change runtime behavior.

## Reading notes

- Elixir uses rebinding, not mutable variables, and the stored values themselves do not change.
- Erlang and Elixir both rely on implicit behavior, which makes variable changes sensitive to context.
- In Elixir, adding a variable before or after existing code can change which value later calls receive.
- In Erlang, adding a variable before existing code can turn later assignments into matches and crash at runtime.
- In Erlang case expressions, introducing a variable before the case can silently change a clause from binding to matching.
- In Elixir, using `^` makes matching explicit, so removing a bound variable can fail at compile time.
- In Erlang, removing a variable used in a later match can silently change clause behavior.
- Numbered variables in Erlang can help track steps, but forgetting to update later uses can change semantics.
- The article says explicit names are better than versioned names when different values have different roles.
- It concludes that neither language guarantees safe code changes without context awareness, and that warnings, tests, types, and patterns like the Elixir pipe operator help reduce errors.
