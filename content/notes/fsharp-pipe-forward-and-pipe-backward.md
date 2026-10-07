---
title: "Pipe Forward and Pipe Backward"
date: '2015-02-10T10:27:57-03:00'
category: webclip
summary: 'The post reviews F# pipe-forward and pipe-backward operators, shows how they pass values between functions, and explains how composition operators help when chaining functions or changing precedence.'
tags: ["fsharp", "functional-programming", "operators"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "F# - Pipe Forward and Pipe Backward | theburningmonk.com"
    url: "http://theburningmonk.com/2011/09/fsharp-pipe-forward-and-pipe-backward/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-02/theburningmonk-com--fsharp-pipe-forward-and-pipe-backward.md"
    kind: repo
---

The post revisits F# pipe operators and notes that pipe-forward is used more often than pipe-backward, even though both help make function application and chaining easier to read. It also relates pipe-forward to the way collections are used and says composition is especially useful when several functions are chained together.

## Reading notes

- Pipe-forward `|>` passes an intermediate result to the next function, using `let (|>) x f = f x`.
- It shows filtering even numbers from a list as an example of applying a function to a collection result.
- Forward composition `»` is defined as `let (») f g x = g (f x)`.
- The post says `»` is cleaner than writing the equivalent nested function calls, especially when many functions are chained.
- Pipe-backward `<|` applies the function on the left to the value on the right, using `let (<|) f x = f x`.
- The post says `<|` helps change operator precedence and avoid parentheses.
- Backward composition `«` is defined as `let («) f g x = f (g x)`.
- It gives finding odd numbers in a list as an example of where backward composition is useful.
