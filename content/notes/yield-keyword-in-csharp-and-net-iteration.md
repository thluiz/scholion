---
title: "Muhammad Waseem (@mwaseemzakir) on X"
date: '2023-12-18T05:36:27+00:00'
category: webclip
summary: 'Explains the C# yield keyword as a way to support custom stateful iteration over .NET collections, returning IEnumerable lazily and noting basic restrictions on where yield can be used.'
tags: ["csharp", "dot-net", "yield", "iteration"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Muhammad Waseem (@mwaseemzakir) on X"
    url: "https://x.com/mwaseemzakir/status/1736621427900436567?s=20"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2023-12/x-com--yield-keyword-in-csharp-and-net-iteration.md"
    kind: repo
---

The post explains that `yield` is used for custom stateful iteration over .NET collections. It contrasts building a full list and returning it with letting the caller consume values during iteration, and says `yield` basically returns an `IEnumerable`. It also notes that C# 8 adds `IAsyncEnumerable` and that `yield` works lazily, so values are not retrieved until the collection is iterated or materialized with `ToList()`.

## Reading notes

- `yield return` and `yield break` are presented as the key forms of the keyword.
- The example focuses on checking even numbers between 1 and 1000.
- One approach stores all results in a list before returning them.
- Another approach keeps iterating and reports numbers to the caller as it goes.
- `yield` is described as useful for that second approach.
- Methods with `ref`, `in`, or `out` parameters are said not to allow `yield`.
- Lambda expressions and anonymous methods are said not to contain `yield`.
- The post says the sequence is only retrieved when iterated with a `for` loop or when `ToList()` is used.
