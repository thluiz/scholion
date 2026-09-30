---
title: "Loop Optimizations in C# (and various other compilers)"
date: '2021-02-12T06:38:04-03:00'
category: webclip
summary: 'The post shows how C# loop optimizations depend on exact code patterns, with loop cloning, hoisting, Span<T> handling, and cases where try-catch or compound assignment block them.'
tags: ["csharp", "loop-optimizations", "jit", "compiler-behavior"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Loop Optimizations in C#"
    url: "https://leveluppp.ghost.io/loop-optimizations-in-various-compilers/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2021-02/leveluppp-ghost-io--loop-optimizations-in-csharp.md"
    kind: repo
---

This post uses infographics to show loop optimizations in C# and briefly compares them with Go and Rust. It focuses on how the compiler and JIT react to specific loop shapes, compiler versions, and code constructs.

## Reading notes

- C# loop cloning can remove array bounds checks in a fast path by cloning the loop into slow and fast paths.
- Loop hoisting moves expressions that can be computed once into a temporary variable or register.
- Compound assignment in C# emits a dup instruction in IL and can prevent loop cloning and hoisting in the JIT.
- Try-catch blocks block loop cloning and hoisting, even when part of the block is removed as empty.
- Loop optimizations are sensitive to the exact range expression; a slightly more complex loop condition can keep bounds checks on every iteration.
- With Span<T>, the compiler can remove bounds checks in the fast case, and working on a slice helps the compiler decide correctly.
- Prolog creates the stack frame and epilog cleans it up; too many returns from a function in a loop can turn optimizations off.
- Go shows few advanced optimizations in the author’s simple tests.
- Rust applies many optimizations, including bounds checks, loop unrolling, and hoisting, depending on the range construction and count.
