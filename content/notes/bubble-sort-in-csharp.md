---
title: "Bubble Sort In C#"
date: '2022-03-27T18:58:03-03:00'
category: webclip
summary: 'The article explains how bubble sort works in C#, shows a basic implementation and an optimized version with early exit, and compares their O(N²) behavior with benchmark results.'
tags: ["csharp", "bubble-sort", "sorting-algorithms"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Bubble Sort In C# - Code Maze"
    url: "https://code-maze.com/csharp-bubble-sort/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-03/code-maze-com--bubble-sort-in-csharp.md"
    kind: repo
---

Bubble sort is presented as a simple way to sort arrays by comparing adjacent elements and swapping them when they are out of order. The article walks through an example array, then shows a C# implementation that uses nested loops and a temporary variable to swap values in place.

It also adds an optimized version that tracks whether any swap occurred and breaks early when the array is already ordered. The article reviews space complexity as O(1), time complexity as O(N²) in general, and shows benchmark results where the optimized version is faster, especially on already sorted input.

## Reading notes

- Bubble sort compares neighboring elements and swaps them when they are in the wrong order.
- The example array is sorted step by step until it becomes `1, 20, 49, 57, 73, 99, 133`.
- The basic C# implementation uses two nested loops and a temporary variable to swap adjacent values.
- The algorithm sorts the array in place, with space complexity O(1).
- The article states best case time complexity as O(N) when the array is already ordered.
- The article states average and worst case time complexity as O(N²).
- The optimized version uses a boolean `swapRequired` to stop early when no swaps happen in a pass.
- The benchmark compares the normal and optimized versions on random arrays and already sorted arrays of different sizes.
- The optimized version is faster in every benchmark shown.
- The article concludes that bubble sort is easy to implement but inefficient compared with other sorting algorithms.
