---
title: "let, const, and my view"
date: '2020-02-22T12:11:53+00:00'
category: webclip
summary: 'The post argues that `const` should be the default for variable bindings, while `let` should signal an expected change. It also says `const` teaches constant bindings, not immutable values.'
tags: ["javascript", "let", "const", "readability"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "let, const, and my view"
    url: "https://dev.to/emnudge/let-const-and-my-view-3aa"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--let-const-and-my-view.md"
    kind: repo
---

The post responds to the debate around `let` and `const` by arguing for `const` as the default choice. It distinguishes constant bindings from immutable values, says `var` is mostly avoided because of hoisting and block-scope issues, and claims `let` should be used when mutation is expected.

## Reading notes

- `var` is described as largely out of use because it hoists to the top of the current function or file scope and is not limited to block scope.
- `let` is presented as `var` without those two issues, while `const` is presented as `let` with constant bindings.
- `const` does not make objects immutable; it only prevents reassignment of the binding.
- The post says beginners often confuse `const` with immutability, and that this should be taught as a binding rule instead.
- Dan Abramov’s reasons for preferring `let` are summarized as loss of intent, confusion, pressure to avoid redeclaring, and little practical benefit from `const`.
- The author argues that `const` is useful as a default because it makes the unusual case stand out when `let` is used.
- The post says intent is not lost, but moved, and that `let` can signal that a value will change.
- It compares this idea with Rust, where immutability is default and mutation is marked with `mut`.
- It also says screaming case can already be used when something needs to be marked as constant.
- The conclusion says it is usually better to follow a project’s conventions and keep code consistent.
