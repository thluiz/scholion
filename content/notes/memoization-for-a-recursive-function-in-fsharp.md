---
title: "Memoization for a recursive function in F#"
date: '2026-09-25T21:54:01+01:00'
category: webclip
summary: 'The post shows how to memoize a recursive F# solution for an Advent of Code puzzle, compares dictionary and map-based caches, and reports BenchmarkDotNet results.'
tags: ["fsharp", "memoization", "recursion", "benchmarkdotnet"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Memoization for a recursive function in F#"
    url: "https://www.damirscorner.com/blog/posts/20250110-MemoizationForARecursiveFunctionInFSharp.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/damirscorner-com--memoization-for-a-recursive-function-in-fsharp.md"
    kind: repo
---

The post explains why memoization fits a pure recursive solution for one Advent of Code puzzle in F#. The author first had a slow recursive function that repeated the same calculations, then explored ways to cache results in F#.

## Reading notes

- Memoization stores previous function results so the same pure call can skip recomputation.
- The first recursive solution was pure but too slow because it recalculated the same results many times.
- F# has no built-in memoization support, so the author implemented it manually.
- A wrapper that passes a memoized recursive function into the worker function is needed for recursive cases.
- One implementation uses a mutable `Dictionary` from .NET as the cache.
- Another implementation uses a mutable variable that holds an immutable F# `Map`.
- A third approach keeps the cache in the function state and uses `mapFold`.
- The `mapFold` version requires passing the cache in, returning it, and splitting the original `sumBy` step into preparation, recursion, and final summation.
- BenchmarkDotNet was used to compare the approaches at 25, 30, and 35 blinks.
- The version with a mutable dictionary was the fastest cached implementation.
- The two map-based versions performed similarly and were much slower than the dictionary version.
- The post concludes that F# supports mutable data structures, which can be useful for memoization.
