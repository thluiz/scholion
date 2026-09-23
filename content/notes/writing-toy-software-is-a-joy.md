---
title: "Writing Toy Software Is A Joy"
date: "2026-09-23T19:06:49+01:00"
category: webclip
has_commentary: false
summary: "Argues for building toy programs (regex engines, OS kernels, chess AIs) as the fastest route to real understanding, and against outsourcing that struggle to an LLM."
tags:
  - programming
  - learning
  - side-projects
sources:
  - title: "Writing Toy Software Is A Joy"
    url: "https://blog.jsbarretto.com/post/software-is-joy"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/blog-jsbarretto-com--writing-toy-software-is-a-joy.md"
    kind: repo
---

Joshua Barretto opens with Feynman's line, "what I cannot create, I do not understand," and builds the post on it: reinventing the wheel teaches more about wheels than any book does. His target is 2025's version of software development, increasingly commodified and now threatened by AI on the exact parts of the craft he finds joyful. His answer is toy programs: small, deliberately unpolished projects built to the 80:20 rule, where the only goal is to hit the constraints of a problem head-on rather than read about them.

A toy program stays useful by staying underbuilt. Crash on unimplemented paths instead of handling them, skip anything not required to reach the goal, and resist the instinct to make it production-ready.

## Fichamento

- The post lists 21 toy projects he's built over 15 years, each rated for difficulty and time: a regex engine, an x86 kernel, a GameBoy/NES emulator, a physics engine, a tree-walking interpreter, a C-like compiler, a text editor, an async runtime, a hash map, a software rasteriser, an SDF renderer, a voxel engine, a threaded VM, a GUI toolkit, an orbital mechanics simulator, a 64-bit-state game jam constraint, an ECS framework, a CHIP-8 emulator, a chess engine, and a POSIX shell.
- Knowledge from these projects transfers sideways into paid work, most often as a head start diagnosing a bug in a tool or library he wouldn't otherwise understand from the inside.
- He argues LLMs undercut the exercise's whole point. The value is in exploring the unknown without an existing solution polluting the search, and he recommends a book over an LLM for that kind of learning.
- Modern hardware, in his view, doesn't make toy software any easier or harder to justify than it used to be. Toy software was the default before frameworks got heavy, and performance mostly didn't suffer for it.
- His diagnosis for slow software isn't usually the developer's own code. It's reaching for pre-built frameworks and toolkits sized for heavy-duty use on problems that never needed them.
