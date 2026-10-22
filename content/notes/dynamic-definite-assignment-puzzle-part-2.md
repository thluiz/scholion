---
title: "A dynamic definite assignment puzzle, part 2"
date: '2020-12-31T09:12:28-03:00'
category: webclip
summary: 'Eric Lippert shows why the C# compiler is right to report a definite assignment error for a dynamic expression, using strange operator overloads to demonstrate that control flow can skip an out variable assignment.'
tags: ["csharp", "compiler", "dynamic", "definite-assignment"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "A dynamic definite assignment puzzle, part 2 | Fabulous adventures in coding"
    url: "https://ericlippert.com/2018/11/19/a-dynamic-definite-assignment-puzzle-part-2/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-12/ericlippert-com--dynamic-definite-assignment-puzzle-part-2.md"
    kind: repo
---

Eric Lippert argues that the C# compiler is correct to flag the earlier program as a definite assignment problem. The key point is that `dynamic` forces the compiler to consider any runtime behavior that a legal but unusual type might produce, including odd operator overloads.

He builds the case with two contrived types. One makes `&&` behave in a way that can skip evaluating the right-hand side, and another overloads equality so that `obj != null` can produce a non-bool result that still leads to a true `if` condition. That combination shows how `GetString(out str)` might never run even though the program later uses `str`. The practical fix is to cast `dynamic` to `object` before comparing with `null`, so the compiler can emit a normal null check.

## Reading notes

- The C# compiler is correct to report a definite assignment error for the original program.
- `dynamic` makes the compiler account for any valid runtime control flow, including very strange operator overloads.
- The example uses a `Crazy` type whose `operator true`, `operator false`, and `operator &` behave in unnatural ways.
- A second `Weird` type overloads equality so that `obj != null` can return `Crazy` instead of `bool`.
- With these overloads, `GetString(out str)` can be skipped while the `if` condition still evaluates as true.
- The safe pattern is `(object)obj != null && GetString(out str)`.
- The post also treats this as a lesson for language designers and compiler writers about operator overloading and adversarial test cases.
