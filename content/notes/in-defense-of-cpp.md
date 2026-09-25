---
title: "In Defense of C++"
date: '2025-09-16T19:10:02+01:00'
category: webclip
summary: 'The post argues that C++’s complexity, age, and safety criticisms are overstated, and that readable code, modern features, and good practices matter more than the language’s reputation.'
tags: ["c-plus-plus", "systems-programming", "memory-safety", "rust"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "In Defense of C++ - DEV Community"
    url: "https://dev.to/dayvster/in-defense-of-c-1g7l?"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-09/dev-to--in-defense-of-cpp.md"
    kind: repo
---

The post argues that C++ is often criticized for being complex, outdated, unsafe, and hard to read, but says those complaints depend heavily on how the language is used. It claims C++ can be kept readable with simpler code, smart pointers, and the standard library, and that many supposed advantages of rewriting to Rust come from the rewrite itself rather than Rust alone.

## Reading notes

- C++ has many ways to solve the same problem, but the author says developers do not need to use the most advanced features to write maintainable code.
- The post argues that the best approach is usually a matter of personal or team preference, and that readability matters more than chasing an ideal solution.
- C++ is presented as old but still actively developed, with C++20 and C++23 bringing modules, concepts, ranges, and coroutines.
- The author says C++ remains widely used in games, high-performance computing, embedded systems, and other large applications.
- The discussion of Rust says code rewrites often improve security and bug counts because they also let teams redesign architecture and fix old issues.
- The post says unsafe code can be written in any language, and that memory safety is only one part of safety.
- C++ can be made safer with smart pointers, static analysis tools, memory sanitizers, and even garbage collection, though the author recommends smart pointers as the simplest path.
- For readability, the author recommends keeping C++ close to C when possible, using smart pointers, avoiding raw pointers, and relying on the standard library.
- The ecosystem is described as large and sometimes confusing, but the post says this is true of every language and recommends avoiding Boost unless its specific features are needed.
- For beginners, the author says C++ is hard but argues that systems programming and game development eventually require C or C++, while web or data work fits Python or JavaScript better.
- The post treats Rust and C++ as tools for different situations, with Rust favored for new safety-focused projects and C++ for legacy systems and performance-critical domains.
- It closes by saying C++ remains widely used in 2025 and still powers browsers, game engines, automotive systems, trading platforms, and AI frameworks.
