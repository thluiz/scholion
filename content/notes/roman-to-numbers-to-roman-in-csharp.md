---
title: "Roman To Numbers To Roman in C#"
date: '2022-03-27T18:56:47-03:00'
category: webclip
summary: 'The page explains how to convert Roman numerals to integers by comparing current and next symbols, then shows two ways to convert integers back to Roman numerals using a dictionary or arrays.'
tags: ["csharp", "roman-numerals", "leetcode", "algorithm"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Roman To Numbers To Roman in C#. Besides its very confusing title, I got… | by Rikam Palkar | Mar, 2022 | Level Up Coding"
    url: "https://levelup.gitconnected.com/roman-to-numbers-to-roman-in-c-12c6aa7e2ac7"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-03/levelup-gitconnected-com--roman-to-numbers-to-roman-in-csharp.md"
    kind: repo
---

The page covers Leetcode problems 13 and 12. For Roman to Integer, it uses a dictionary of Roman symbols and their values, then adds or subtracts based on whether the next symbol is larger than the current one. It notes the need to handle the last element to avoid an index error.

For Integer to Roman, it presents two approaches. The first uses a dictionary and handles the six subtractive cases, `IV, IX, XL, XC, CD, CM`, by traversing values from large to small and shrinking the number until it reaches zero. The second uses two arrays, one for Roman letters and one for numbers, with time complexity O(n) and space complexity O(n + m).

## Reading notes

- Roman to Integer converts a Roman numeral string into its corresponding integer value.
- The Roman to Integer logic compares each symbol with the next one and subtracts when the next value is greater.
- The example `MCMXCIV` converts to `1994`.
- A dictionary stores Roman symbols and their integer values.
- The code must handle the last element to avoid an Array IndexOutOfBoundsException.
- Integer to Roman is the reverse problem.
- One approach uses a dictionary and includes the subtractive pairs `IV, IX, XL, XC, CD, CM`.
- This approach traverses values from large to small and repeats each value while the number remains large enough.
- The example `350` becomes `CCCL`.
- The first Integer to Roman approach has time complexity O(n * m) and space complexity O(n).
- The second approach uses two arrays, one for Roman letters and one for numbers.
- The second approach has time complexity O(n) and space complexity O(n + m).
