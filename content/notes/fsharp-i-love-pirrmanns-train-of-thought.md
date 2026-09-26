---
title: "F# |> I <3 | Pirrmann's train of thought"
date: '2026-09-27T00:48:23+01:00'
category: webclip
summary: 'The author says F# has changed how he writes C# and that he has now moved to F# at work. He then shows an F# solution for uncertain numbers using a wrapped type, tests, a generic combine function, and operator overloading.'
tags: ["f-sharp", "kata", "operator-overloading"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "F# |> I <3 | Pirrmann's train of thought"
    url: "http://www.pirrmann.net/f-sharp-i-love/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/pirrmann-net--fsharp-i-love-pirrmanns-train-of-thought.md"
    kind: repo
---

The post says F# has shaped the author’s everyday C# coding for years, and that a recent work project let him use F# for real. He also says the open-sourcing of Roslyn was welcome, but the bigger news for him was that Visual F# now accepts contributions, which makes him expect more from the language.

## Reading notes

- The author says he has been writing about F# for a while and has now gone “totally” over to F#.
- He presents a kata about values with uncertainty and operations that manipulate them.
- He models a value and its precision with a `Number` type holding two floats.
- He defines a `+-` operator to build values like `4.0 +- 1.0`.
- He uses FsUnit tests to check that a number equals itself and that addition combines values and accuracies.
- He writes a generic `combine` function that evaluates an operator on the boundary values, then rebuilds the result from the minimum and maximum.
- He adds operator overloading so `+`, `-`, `/`, and `Pow` all use the same combine logic.
- He thanks @luketopia for the Twitter exchange and for the trick that lets `**` be passed as an argument with spaces around the operator.
