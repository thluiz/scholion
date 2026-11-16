---
title: "The Performance Benefits of Final Classes"
date: '2020-04-20T21:22:44+00:00'
category: webclip
summary: 'The article explains that `final` in C++ prevents inheritance and can help the compiler devirtualize calls, which may reduce indirect-call overhead and improve optimization opportunities.'
tags: ["c++", "final", "devirtualization", "performance"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The Performance Benefits of Final Classes"
    url: "https://devblogs.microsoft.com/cppblog/the-performance-benefits-of-final-classes"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/devblogs-microsoft-com--the-performance-benefits-of-final-classes.md"
    kind: repo
---

The article says `final` marks a class or virtual member function as one that cannot be derived from or overridden. It argues that this helps the compiler enforce design intent and can also improve performance by enabling devirtualization.

## Reading notes

- `final` prevents further derivation from a class or overriding of a virtual member function.
- The compiler can use `final` to identify more virtual calls that can be resolved at compile time.
- Virtual calls use an indirect call through the vtable, which is more expensive than a direct call because of branch prediction, instruction cache, and missed inlining opportunities.
- Devirtualization resolves virtual calls at compile time instead of runtime.
- In the example with `dog::speak`, compilers inline the call into `main` because the only possible result is known.
- In the `derived final : base` example, a call to `d.f()` can be inlined because `derived` cannot be further derived.
- Without `final`, the assembly shown uses a vtable load and an indirect jump.
- The article says the compiler may optimize more aggressively when it can see the full code path that will execute.
- The conclusion recommends checking whether codebases have places where `final` could improve performance and measuring the impact.
