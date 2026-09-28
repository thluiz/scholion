---
title: "Speed up your daily work with Elixir console tricks"
date: '2022-03-27T19:08:40-03:00'
category: webclip
summary: 'The post collects IEx habits that make Elixir work faster: use built-in help, autocomplete, history, multiline input, previous results, recompile, and .iex.exs setup.'
tags: ["elixir", "iex", "developer-tools"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Speed up your daily work with Elixir console tricks | Bartosz Górka"
    url: "https://bartoszgorka.com/speed-up-your-daily-work-with-elixir-console-tricks"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-03/bartoszgorka-com--speed-up-your-daily-work-with-elixir-console-tricks.md"
    kind: repo
---

The article lists IEx tricks meant to make daily Elixir work smoother. It points to built-in help, autocomplete, shell history, multiline input, previous results, faster recompilation, and a local .iex.exs file for imports, aliases, variables, and IEx configuration.

## Reading notes

- Use `h` in IEx to check documentation for built-in modules instead of switching to a browser.
- `iex -S mix` gives access to project modules and their docs, including `@doc` and `@moduledoc`.
- Tab completion helps with module and function names, and it only shows public functions.
- Shell history can be enabled with `iex --erl "-kernel shell_history enabled"` or by setting `ERL_AFLAGS`.
- IEx supports multiline pasting and can reuse the previous result with `v()` when a pasted expression starts with a binary operator.
- Previous results can be reused for debugging or for computations that are expensive to run again.
- `recompile` lets you test code changes without restarting the console.
- A local `.iex.exs` can import modules, add aliases, set variables, and configure IEx on startup.
