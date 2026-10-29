---
title: "Converting a DSL to Executable F# Code On-the-Fly, Part 1"
date: '2016-02-29T10:49:36-03:00'
category: webclip
summary: 'The post shows how to move from a hard-coded function to a replaceable F# function by modeling expressions with a discriminated union and interpreting them into executable code.'
tags: ["fsharp", "dsl", "interpreter", "functional-programming"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Converting a DSL to Executable F# Code On-the-Fly, Part 1 ·"
    url: "http://brandewinder.com/2016/02/20/converting-dsl-to-fsharp-code-part-1/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-02/brandewinder-com--converting-a-dsl-to-executable-fsharp-code-on-the-fly-part-1.md"
    kind: repo
---

The post starts from a hard-coded F# function and moves toward a design where the application can receive behavior at run time. The stated goal is to let a user provide a function as a string, using a small domain-specific language, and turn that input into an executable function without changing the application code.

## Reading notes

- The application begins with a fixed function `f (x:float) = 2.0 * x + 1.0` inside a `Program` class.
- The long-term goal is to call the program with a string such as `add(1,mul(2,x))` and have it produce the same result.
- The approach is broken into four steps: write code in an external DSL, parse it into an intermediate F# representation with FParsec, interpret it into a runnable F# function, and run it.
- The first refactoring extracts the function so `Run` can receive any `float -> float` function as an argument.
- The next step models the function body with a discriminated union called `Expression`, with cases `X`, `Constant`, `Add`, and `Mul`.
- The `Expression` type is used as an internal DSL that keeps valid constructions type-safe.
- An `interpret` function recursively converts an `Expression` into a function of type `float -> float`.
- `Constant(value)` becomes a function that always returns `value`, and `X` becomes a function that returns its input.
- `Add` and `Mul` are handled by interpreting both sides and combining their results.
- `Program.Run` is then changed to accept an `Expression`, interpret it, and execute the resulting function.
- The post closes by saying that the next step will be to map user input to the four shapes of the internal DSL.
