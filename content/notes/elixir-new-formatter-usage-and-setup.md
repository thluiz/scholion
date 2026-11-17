---
title: "Everything you need to know about Elixir's new formatter"
date: '2026-11-17T15:04:03+00:00'
category: webclip
summary: 'Explains how to install Elixir with the new formatter, run mix format on files, configure .formatter.exs, use CI checks, and auto‑format Elixir code on save in vim.'
tags: ["elixir", "code-formatter", "mix", "vim"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Everything you need to know about Elixir's new formatter"
    url: "https://devonestes.com/everything-you-need-to-know-about-elixirs-new-formatter"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/devonestes-com--elixir-new-formatter-usage-and-setup.md"
    kind: repo
---

The text introduces Elixir's new code formatter, explaining that it has landed in the Elixir repository and can already be explored. It walks through installing the development version of Elixir that includes the formatter, then shows how to run `mix format` on individual files or file patterns, and how to centralize those patterns in a `.formatter.exs` file. It also covers optional configuration for macros that should not use parentheses, how to integrate formatting checks into a CI pipeline, and a simple way to trigger `mix format` automatically on save when using vim.

## Reading notes

- The new formatter mentioned in a previous ElixirConf talk has been merged into the Elixir repository and is available for use.
- To try it, you clone the Elixir repo from GitHub with `git clone https://github.com/elixir-lang/elixir.git`.
- After cloning, you should first run `make clean test` to compile and run the test suite on your machine.
- Once tests pass, you install Elixir with `make install`.
- Running `elixir -v` should now show a development version like `Elixir 1.6.0-dev (9b5af3303)`, with the SHA varying.
- With this dev version installed, you can start using the formatter.
- To format a single file in a standard mix project, you can run `mix format mix.exs`, where the extra argument is the target file.
- The `mix format` task formats only the files and patterns explicitly passed to it.
- To format many files at once, you can pass glob patterns, for example `mix format mix.exs "lib/**/*.{ex,exs}" "test/**/*.{ex,exs}"`.
- `mix format` accepts any number of specific files or glob patterns as arguments.
- Repeatedly passing long lists of patterns on the command line can be inconvenient.
- A `.formatter.exs` file lets you configure which files should be formatted by default.
- A basic `.formatter.exs` example sets `inputs` to include `lib/**/*.{ex,exs}`, `test/**/*.{ex,exs}`, and `mix.exs`.
- With that configuration, running `mix format` with no extra arguments will format all `.ex` and `.exs` files under those paths.
- The formatter also supports configuration for macros that should not be forced to use parentheses.
- In `.formatter.exs`, the `locals_without_parens` option lists macros by name and arity to exempt them from the parentheses rule.
- An example `locals_without_parens` configuration lists `my_macro: 2` and `my_other_macro: 3` as macros that should not require parentheses.
- The key in that keyword list is the macro name, and the value is its arity.
- For CI integration, you can add a formatting check command to the pipeline.
- The suggested command is `mix format --check-formatted --dry-run` so CI fails if files are not formatted.
- Because the formatter may change while still in development, the text suggests being cautious about wiring this up immediately.
- For vim users, you can trigger the formatter automatically when saving Elixir files.
- Adding `autocmd BufWritePost *.exs silent :!mix format %` and `autocmd BufWritePost *.ex silent :!mix format %` to `.vimrc` formats `.ex` and `.exs` files on write.
- Enabling `set autoread` in vim helps reload files after external formatting.
- The author expects more advanced vim integrations to appear later, possibly using tools like neomake, but the provided commands already allow basic on-save formatting.
