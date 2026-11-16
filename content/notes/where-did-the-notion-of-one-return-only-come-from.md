---
title: "Where did the notion of \"one return only\" come from?"
date: '2026-11-16T08:11:49+00:00'
category: webclip
summary: 'The notion of Single Entry, Single Exit came from languages with explicit manual resource management, where early returns could leak resources. In languages with exceptions or automatic cleanup, that original argument largely disappears.'
tags: ["single-entry-single-exit", "early-return", "resource-management", "java"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Where did the notion of \"one return only\" come from?"
    url: "https://web.archive.org/web/20200607181758id_/https://softwareengineering.stackexchange.com/questions/118703/where-did-the-notion-of-one-return-only-come-from"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/web-archive-org--where-did-the-notion-of-one-return-only-come-from.md"
    kind: repo
---

The post says the Single Entry, Single Exit idea came from languages with explicit resource management, such as C and assembly. In those languages, an early return can skip cleanup code and leak resources, so programmers used one of three patterns to keep cleanup reliable.

It argues that exceptions, finally blocks, using, and RAII changed that situation by making premature exits something a language already has to handle. With cleanup covered, SESE loses its strongest justification, and in many modern languages it can make code more complex instead of clearer.

## Reading notes

- SESE is presented as coming from languages with explicit resource management, especially C and assembly.
- In C, an early return can skip release code and leak a resource.
- The text lists three responses: duplicate cleanup, jump to cleanup with goto, or control flow through a local variable.
- In assembly, functions can be entered at multiple addresses, which makes SESE-style discipline attractive for reducing complexity and bugs.
- With exceptions, functions may exit early anyway, so cleanup has to be prepared in advance.
- The post mentions finally in Java, using in C#, and RAII in C++ as ways to handle cleanup.
- It says readability is the remaining argument for SESE, but a function with many scattered returns is already hard to follow.
- The author argues that SESE often makes code more complex and fits C better than most modern languages.
- The post ends by suggesting that Java kept many C-era conventions even when they do not help much in an OO setting.
