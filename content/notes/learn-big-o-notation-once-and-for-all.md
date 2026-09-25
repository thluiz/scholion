---
title: "Learn Big O Notation once and for all"
date: '2026-09-24T23:39:45+01:00'
category: webclip
summary: 'The post reviews Big O notation as a way to describe how runtime grows with input size and walks through common classes like O(1), O(n), O(n^2), O(log n), O(n log n), O(2^n) and O(n!).'
tags: ["big-o", "time-complexity", "algorithms", "sorting"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Learn Big O Notation once and for all"
    url: "https://dev.to/alvbarros/learn-big-o-notation-once-and-for-all-hm9?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--learn-big-o-notation-once-and-for-all.md"
    kind: repo
---

The post is a refresher on Big O notation for coding interviews. It explains that Big O describes how an algorithm's runtime grows as input size grows, then compares common cases through simple examples.

It covers O(1) for constant-time access, O(n) for scanning every item, O(n^2) for nested loops, O(log n) for binary search and tree traversal, O(n log n) for merge sort, O(2^n) for branching recursion like Fibonacci, and O(n!) for permutations and the Traveling Salesman Problem.

## Reading notes

- Big O notation classifies algorithms by how runtime or space requirements grow as input size grows.
- O(n) appears when the algorithm needs to inspect every element, such as finding the maximum in an unsorted array.
- O(2n) is simplified to O(n) because Big O keeps the growth shape, not constant multipliers.
- O(1) fits operations whose time does not grow with input, such as returning the first array element, appending, popping, or dictionary lookup by index.
- O(n^2) is associated with nested loops, like generating every pair of outcomes for two dice with the same number of sides.
- O(n*m) covers two loops that depend on different input sizes, like combinations from dice with different numbers of sides.
- O(log n) comes from repeatedly dividing the search space in half, as in binary search or tree traversal that goes left or right at each step.
- O(n log n) is common in sorting algorithms such as merge sort, where the array is split recursively and then merged in linear time.
- O(2^n) appears in recursion that branches in two directions, as in the Fibonacci example without memoization.
- O(n!) is linked to permutations and the Traveling Salesman Problem, and the post treats it as a sign that the algorithm is far from optimal.
- The post also points to a complexity chart and adds an edit mentioning a problem with an O(sqrt n) solution.
