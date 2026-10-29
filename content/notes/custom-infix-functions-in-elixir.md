---
title: "Custom Infix Functions in Elixir"
date: '2016-03-05T09:10:36-03:00'
category: webclip
summary: 'The post shows that Elixir does not let you create new infix operators in regular code. The parser already knows a fixed set of operators, and only those can be implemented.'
tags: ["elixir", "infix-operators", "parser"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Custom Infix Functions in Elixir"
    url: "http://www.rodneyfolz.com/custom-infix-functions-in-elixir/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-03/rodneyfolz-com--custom-infix-functions-in-elixir.md"
    kind: repo
---

The post explains that the author needed a nearly-equal float test for an Elixir Math module and discovered that the apparent custom infix function was just a regular function definition using one of Elixir’s predefined infix operators. It then shows that Elixir’s parser recognizes a fixed set of operators, so new infix symbols cannot be added without changing and recompiling Elixir itself.

## Reading notes

- The author needed tests for floats that are very close to equal.
- The sample nearly-equal test is written as an ordinary function definition.
- Elixir 1.2.0 allows only a fixed set of infix operators such as `\`, `<-`, `|`, `~>>`, `<~>`, `|||`, `&&&`, and `^^^`.
- Attempts to define a new custom infix operator produce a syntax error.
- The parser, not Kernel, is where the operators are special-cased.
- The parser file `elixir_parser.yrl` lists operator precedence and the built-in infix forms.
- Because parsing happens before bootstrapping, new infix operators cannot be defined in user code.
- José Valim confirmed that the unused operators were included for this use case.
- Kernel operators can be redefined after unimporting them, but that can break expectations in other Elixir code.
- The `pipespect` library uses this technique to inspect each stage in a `|>` pipeline.
