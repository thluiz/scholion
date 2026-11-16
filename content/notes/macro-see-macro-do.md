---
title: "Macro See, Macro Do"
date: '2026-11-16T01:42:59+00:00'
category: webclip
summary: 'The post shows how `quote/2` turns Elixir code into AST, how `use` calls `__using__/1`, and how Phoenix injects shared imports and aliases through macros.'
tags: ["elixir", "macros", "abstract-syntax-tree"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Macro See, Macro Do"
    url: "https://dev.to/hint/macro-see-macro-do-2985"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--macro-see-macro-do.md"
    kind: repo
---

The post traces how Phoenix uses `quote/2` to package code as AST and how `use` expands into a call to `__using__/1`. It uses a small example to show that the shared `import` and `alias` setup can be generated instead of written by hand.

## Reading notes

- `quote/2` appears in Phoenix code that sets up controllers with shared imports and aliases.
- A simple `Bar.AllTheThings` example reproduces that pattern with `quote do ... end`.
- `use Bar.AllTheThings, :things` fails until `__using__/1` is defined.
- `__using__/1` calls the named function through `apply/3`.
- `quote do sum(2, 2) end` returns AST as a three-element tuple.
- `import Bar.Math` also has an AST form with `:import` and alias metadata.
- The same AST can be written directly without `quote/2`.
- `use Bar.AllTheThings, :things` expands to `Bar.AllTheThings.__using__(:things)`.
- The post concludes that `quote` converts Elixir code to AST and supports dependency injection through macros.
