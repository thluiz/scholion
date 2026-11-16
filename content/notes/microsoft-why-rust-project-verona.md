---
title: "Microsoft: Here’s why we love programming language Rust and kicked off Project Verona"
date: '2020-07-05T14:10:42+00:00'
category: webclip
summary: 'Microsoft says it is pursuing safe systems programming to reduce memory-related bugs in C++ software. Rust and Project Verona are part of that effort, along with Krustlet for Kubernetes and WebAssembly.'
tags: ["rust", "microsoft", "safe-systems-programming", "project-verona"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Microsoft: Here’s why we love programming language Rust and kicked off Project Verona"
    url: "https://zdnet.com/article/microsoft-heres-why-we-love-programming-language-rust-and-kicked-off-project-verona"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/zdnet-com--microsoft-why-rust-project-verona.md"
    kind: repo
---

Microsoft says it is pursuing safe systems programming to cut memory-related bugs in software written in C++ and other low-level languages. Ryan Levick says those bugs are costly to fix and make up a large share of Patch Tuesday issues.

## Reading notes

- Systems programming covers platforms such as Windows, Xbox, and Azure rather than applications that run on them.
- Microsoft writes much of its platform software in C++ and sometimes C, and says it has reached a wall in how much it can improve memory safety in those languages.
- Levick says 70% of Microsoft’s very serious, mission-critical bugs are memory safety issues.
- Project Verona is a Microsoft Research language aimed at safe infrastructure programming and is described as completely memory safe.
- Microsoft is also looking at Rust as the best alternative to C++ for making system software more safe and reliable.
- The Azure team used Rust for Krustlet because it could catch bugs that Go could not, even though Rust has a steep learning curve.
