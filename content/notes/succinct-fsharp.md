---
title: "Succinct FSharp"
date: '2022-06-28T11:18:15-03:00'
category: webclip
summary: 'An overview of F# basics through F# Interactive, covering bindings, types, collections, control flow, functions, pattern matching, records, unions, exceptions, classes, interfaces, and compiler directives.'
tags: ["fsharp", "fsharp-interactive", "types", "pattern-matching"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "DasDocs"
    url: "https://dasdocs.com/fsharp/1-succinct-fsharp.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-06/dasdocs-com--succinct-fsharp.md"
    kind: repo
---

Page walks through F# through examples and explanations, starting with F# Interactive and basic evaluation in `fsi`. It then covers immutable bindings, `let`, mutable values, whitespace sensitivity, primitive types, strings, tuples, collections, slices, comments, conditionals, loops, functions, currying, pipelines, recursion, and pattern matching.

## Reading notes

- `fsi` is presented as a practical way to learn F#, started with `dotnet fsi` and controlled with `#help;;`, `#quit;;`, and `;;` to end input.
- Expression results are stored in `it`, which has a type, and `it` is not mutable.
- `let` creates bindings, `let mutable` creates variables that can be updated with `<-`, and `=` is used for comparison.
- `let..in` is shown as equivalent to `let`, and lambda functions are introduced through that equivalence.
- Double-backtick identifiers allow names with spaces and symbols.
- F# is whitespace sensitive and uses indentation instead of braces.
- Primitive types listed include `bool`, `byte`, `int`, `float`, `double`, `float32`, `single`, `char`, `string`, and `unit`.
- Strings can be concatenated, written as verbatim strings with `@`, written as multiline strings with triple quotes, or interpolated with `$`.
- Tuples can hold values of different types, be deconstructed, and be accessed with `fst` and `snd`.
- Lists are immutable, arrays are fixed-size and mutable, sequences are lazy, and slices work on lists, arrays, and 2-D arrays.
- Comments can be block, line, or XML doc comments.
- `if..then..else`, `for..in`, `for..to`, and `while..do` are presented as expressions.
- Functions are defined with `let`, can have explicit types, can be anonymous, can capture outer bindings, and can be curried.
- Pipe `|>` and composition `>>` are shown for chaining functions.
- Recursive functions use `rec`, and mutual recursion uses `and`.
- Pattern matching uses `match`, with `_` as wildcard and `when` as a guard.
- `function` is presented as shorthand for `fun x -> match x with`.
- Cons patterns, active patterns, parameterized active patterns, and partial active patterns are included.
- Records, anonymous records, discriminated unions, `option`, and `Result` are covered as data modeling tools.
- Generic type inference and automatic generalization are shown with generic list functions.
- Exceptions are handled with `failwith`, `try/with`, custom exceptions, and `try/finally`.
- Classes, inheritance, interfaces, object expressions, and compiler directives such as `#load`, `#r`, `#I`, and `#if INTERACTIVE` close the page.
