---
title: "The beauty of recursion and pattern matching in functional programming languages"
date: '2026-11-16T01:25:38+00:00'
category: webclip
summary: 'The post explains an Erlang lookup function for a binary tree and shows how recursion plus pattern matching let the code express what it does without stating each control step explicitly.'
tags: ["erlang", "recursion", "pattern-matching", "functional-programming"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The beauty of recursion and pattern matching in functional programming languages"
    url: "https://dev.to/ericdouglas/the-beauty-of-recursion-and-pattern-matching-in-functional-programming-languages-hmn"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--the-beauty-of-recursion-and-pattern-matching-in-functional-p.md"
    kind: repo
---

The post uses an Erlang `lookup/2` function to show how recursion and pattern matching can make a binary-tree search concise and declarative. The function returns `{ok, Val}` when the key matches, `undefined` for an empty node, and otherwise recurses into `Smaller` or `Larger` depending on the key.

## Reading notes

- The function searches a binary tree for a passed `Key` and returns the associated `Val` or `undefined`.
- Erlang allows multiple cases for the same function by changing the pattern in the parameters.
- The cases are checked from top to bottom, so more specific patterns should come first.
- `lookup(_, {node, 'nil'})` ignores the first argument and returns `undefined` for an empty node.
- `lookup(Key, {node, {Key, Val, _, _}})` matches when the key in the node is the same as the requested key and returns `{ok, Val}`.
- `lookup(Key, {node, {NodeKey, _, Smaller, _}}) when Key < NodeKey` uses a guard to decide to continue the search in `Smaller`.
- `lookup(Key, {node, {_, _, _, Larger}})` handles the remaining case and continues the search in `Larger`.
- The post presents this as a functional way to express what the algorithm does instead of spelling out every step.
