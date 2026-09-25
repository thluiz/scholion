---
title: "O(n) Solution to the Multiply Others Problem in F#"
date: "2026-09-23T17:11:13+01:00"
category: webclip
has_commentary: false
summary: "Yan Cui walks through a division-free, O(n) F# solution to the classic interview question of multiplying every array element except itself."
tags:
  - fsharp
  - algorithms
  - interview-questions
sources:
  - title: "O(n) solution to Multiply Others problem in F# | theburningmonk.com"
    url: "http://theburningmonk.com/2016/12/o-n-solution-to-multiply-others-problem-in-f/?utm_content=42278278&utm_medium=social&utm_source=twitter"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/theburningmonk-com--o-n-solution-to-multiply-others-problem-in-f.md"
    kind: repo
---

The problem is a Facebook interview classic: given an array, produce a new array where each position holds the product of every other element, without using division and in O(n) time. Yan Cui shares an F# implementation of a solution built on two auxiliary arrays.

## Reading notes

- One array accumulates products left to right, the other right to left. Position i in the first array holds the product of everything before it; position i in the second holds the product of everything after it.
- Multiplying the two arrays position by position gives the final answer, computed with one forward pass and one backward pass.
- The approach avoids division entirely and runs in O(n) time and O(n) space.
- Cui includes the full F# code, a GitHub-hosted snippet, and links to the original CareerCup question plus his own Project Euler and Advent of Code solutions in F#.
