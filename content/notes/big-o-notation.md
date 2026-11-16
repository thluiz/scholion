---
title: "Big O Notation"
date: '2020-08-26T19:31:13+00:00'
category: webclip
summary: 'The post defines Big O Notation as a way to classify algorithms by runtime and space use, then compares constant and linear examples and introduces logarithmic growth.'
tags: ["big-o-notation", "time-complexity", "space-complexity", "logarithms"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Big O Notation"
    url: "https://dev.to/adafia/big-o-notation-3oi6"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--big-o-notation.md"
    kind: repo
---

Big O Notation is presented as a standard way to classify algorithms by their runtime and memory requirements. The post uses simple code examples to show how performance is compared by general growth trends rather than exact timing, since hardware differences change raw execution time.

It separates time complexity from space complexity, treats auxiliary space as the relevant measure for memory, and gives examples of O(1) and O(n) for time and space. It also notes that logarithmic expressions such as O(log n) and O(n log n) are used for algorithms that do not fit the simpler cases.

## Reading notes

- Big O Notation classifies algorithms by runtime and memory use.
- It gives a vocabulary for comparing algorithm performance and trade-offs.
- Measuring seconds is unreliable because hardware changes execution time.
- Time complexity is based on how runtime grows as input grows.
- The first sum function always takes three simple operations, so its time complexity is O(1).
- The loop-based sum function grows with n, so its time complexity is O(n).
- Space complexity here is auxiliary space, without counting the input itself.
- Primitives are described as O(1) space, strings as O(n), and reference types as generally O(n).
- The sum function uses constant auxiliary space, so its space complexity is O(1).
- The double function creates a new array whose size grows with the input, so its space complexity is O(n).
- Logarithms are described as the inverse of exponentiation.
- Logarithmic complexities are given as O(log n) and O(nlog n).
- Big O focuses on general trends, not exact precision.
- The complexity depends on the algorithm, not on the hardware used to run it.
