---
title: "Functionally Solving Problems"
date: "2026-09-23T16:53:13+01:00"
category: webclip
has_commentary: false
summary: "A Learn You Some Erlang chapter that solves an RPN calculator and a shortest-path puzzle with folds and pattern matching instead of hand-rolled recursion."
tags:
  - erlang
  - functional-programming
  - algorithms
sources:
  - title: "Functionally Solving Problems | Learn You Some Erlang for Great Good!"
    url: "http://learnyousomeerlang.com/functionally-solving-problems"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/learnyousomeerlang-com--functionally-solving-problems.md"
    kind: repo
---

This chapter of Learn You Some Erlang takes two problems borrowed from Learn You a Haskell and works through Erlang solutions for both, on the premise that once you understand functional concepts, the same shape of solution carries across languages with very different syntax.

## Reading notes

- The reverse Polish notation calculator tokenizes an expression, then folds over the tokens treating Erlang's list as a stack: numbers get pushed, operators pop two values and push the result back.
- Reading a string as a number needs a small wrapper, since Erlang has no single built-in that parses both integers and floats.
- The Heathrow-to-London problem models the road as a list of {A,B,X} triples, one per stretch, with X the cost of crossing between the two roads.
- The accumulator for that fold is found by imagining standing in the middle of the algorithm: at each step, the shortest distance and path known so far for each side of the road.
- Both solutions favor lists:foldl over hand-rolled recursion once the recursive logic has been worked out on paper first.
- The chapter closes on breaking a problem into small solvable parts before coding it, and testing once it's done, over any specific language trick.
