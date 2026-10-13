---
title: "Porting from C# to F#: Introduction"
date: '2013-05-24T10:43:17-03:00'
category: webclip
summary: 'The series says a direct port from C# to F# is often not the best way to write F# code, and it lays out three levels of porting, from direct translation to type-driven design.'
tags: ["fsharp", "csharp", "porting", "functional-programming"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Porting from C# to F#: Introduction | F# for fun and profit"
    url: "http://fsharpforfunandprofit.com/posts/porting-to-csharp-intro/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-05/fsharpforfunandprofit-com--porting-from-csharp-to-fsharp-introduction.md"
    kind: repo
---

The post introduces a series on porting C# code to F# and says the goal is to compare approaches, not to assume a direct translation is the best result. It frames porting as a way to see the differences between imperative and functional code, then organizes the work into three levels of sophistication.

## Reading notes

- A direct port keeps the original shape where possible, using classes and methods and often mutating values.
- The functional level replaces classes and methods with modules and functions, favors immutability, uses higher-order functions, pattern matching, and list functions or recursion.
- One path to functional code is to port first and refactor later; another is to make the C# code functional before moving it to F#.
- The advanced level changes the design to use algebraic data types, especially union types, so the domain is encoded in types and illegal states are not representable.
- The series will apply these levels to a bowling game, a shopping cart, and a subway turnstile example.
