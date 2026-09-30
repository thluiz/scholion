---
title: "Merge Sort"
date: '2021-02-13T08:45:19-03:00'
category: webclip
summary: 'The page explains merge sort as a divide-and-conquer method that splits an array into smaller subarrays until size 0 or 1, then rebuilds a sorted array by merging.'
tags: ["merge-sort", "divide-and-conquer", "recursion", "arrays"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Merge Sort - DEV Community 👩‍💻👨‍💻"
    url: "https://dev.to/code_regina/merge-sort-1boo"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2021-02/dev-to--merge-sort.md"
    kind: repo
---

Merge sort is presented as a combination of merging and sorting. The page says it works by splitting an array into smaller subarrays until they reach 0 or 1 element, then building a newly sorted array from those parts.

## Reading notes

- Merge sort is described as a divide-and-conquer strategy.
- The array is split into smaller subarrays all the way down to 0 or 1 element.
- The sorted array is built back up from the smaller parts.
- The example `merge` function compares two arrays with indices and pushes the smaller values into a results array.
- Remaining elements from either array are appended after one side is exhausted.
- The page says most merge sort implementations use recursion.
- The recursive `mergeSort` example returns the array when its length is 1 or less.
- The array is split with `slice`, the halves are sorted recursively, and then merged.
