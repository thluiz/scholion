---
title: "Learn elixir in Y Minutes"
date: '2015-02-15T11:23:48-03:00'
category: webclip
summary: 'The page introduces Elixir as a functional language on the Erlang VM and walks through its core syntax, pattern matching, control flow, modules, structs, exceptions, and message-based concurrency.'
tags: ["elixir", "functional-language", "pattern-matching", "concurrency"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Learn elixir in Y Minutes"
    url: "http://learnxinyminutes.com/docs/elixir/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-02/learnxinyminutes-com--learn-elixir-in-y-minutes.md"
    kind: repo
---

Elixir is presented as a modern functional language built on the Erlang VM, compatible with Erlang but using a more standard syntax and offering more features. The page sketches the core data types, operators, control flow forms, module and function definitions, structs, exceptions, and concurrency through processes and message passing.

## Reading notes

- Elixir runs on the Erlang VM and stays compatible with Erlang while using a more standard syntax.
- Comments are single-line only, and the shell uses `iex` while compilation uses `elixirc`.
- Basic types include numbers, atoms, tuples, lists, binaries, strings, char lists, and ranges.
- `=` means pattern matching, not assignment, and many examples depend on matching values against patterns.
- Strings are UTF-8 encoded, while char lists are lists.
- `/` returns a float, while `div` and `rem` handle integer division and remainders.
- Boolean operators `or`, `and`, and `not` require boolean inputs, while `||`, `&&`, and `!` accept any type.
- Comparisons include strict variants such as `===` and `!==`, and Elixir defines a total ordering across data types.
- Control flow uses `if`, `unless`, `case`, `cond`, and `try/catch`, with `after` available in `try/catch`.
- Anonymous functions can have multiple clauses and guards.
- Functions can be grouped into modules, with `def` for public functions and `defp` for private ones.
- Modules may use attributes, including built-in attributes like `@moduledoc` and custom attributes.
- Structs extend maps with default values, compile-time guarantees, and polymorphism.
- `try/rescue` handles exceptions, and exceptions expose a message.
- Concurrency is based on the actor model, using spawning, sending, and receiving messages.
- The shell itself is a process, and `self` returns its pid.
