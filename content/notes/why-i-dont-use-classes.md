---
title: "Why I Don’t Use Classes"
date: '2020-04-20T21:22:38+00:00'
category: webclip
summary: 'The author prefers functional solutions in full-stack TypeScript because classes make abstractions harder to name, tend to grow large, and complicate state management, especially in React.'
tags: ["typescript", "functional-programming", "classes", "state-management"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Why I Don’t Use Classes"
    url: "https://spin.atomicobject.com/2020/03/12/why-i-dont-use-classes"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/spin-atomicobject-com--why-i-dont-use-classes.md"
    kind: repo
---

The author says he does not actively avoid classes, but usually leans toward functional solutions in full-stack TypeScript. His preference comes from how classes often make abstractions harder to manage, especially when inheritance and polymorphism cause methods to take on extra responsibilities and when class-based state becomes harder to control.

## Reading notes

- He is reflecting on a team codebase that does not use many classes, and he wants that observation to prompt self-reflection rather than persuade others.
- His recent projects have been in full-stack TypeScript, and that ecosystem has shaped what he values in software.
- He prefers functional solutions over object-oriented ones when solving problems in TypeScript.
- He finds it hard to make good abstractions with classes, especially when inheritance and polymorphism turn code into a mess.
- He says overriding base class methods can lead to terrible method names, because methods end up doing more than their names suggest.
- He gives the example of database table classes whose update method may also need to insert a log into a side table.
- He says classes tend to grow large because they collect functionality tied to internal state.
- He finds groups of functions in modules easier to split into smaller pieces when needed.
- He says class-managed state has led to buggy behavior in his work.
- He gives class-based React components as a concrete example of state-related bugs.
- He says React hooks for functional components have not produced the same kind of bugs in his UI code.
- He prefers modules that expose groups of functions taking state and other dependencies, similar to the functional module pattern.
- He leaves open the idea that classes might feel more natural in other ecosystems, but he has not found a strong reason to switch on his current projects.
