---
title: "A simple explanation of functional pipe in JavaScript"
date: '2019-07-07T09:34:38+00:00'
category: webclip
summary: 'The article explains why pipe helps JavaScript keep APIs broad while preserving tree-shaking and smaller bundles, and shows how left-to-right composition improves readability over prototype methods.'
tags: ["javascript", "functional-programming", "pipe", "rxjs"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "A simple explanation of functional pipe in JavaScript"
    url: "https://dev.to/benlesh/a-simple-explanation-of-functional-pipe-in-javascript-2hbj"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--a-simple-explanation-of-functional-pipe-in-javascript.md"
    kind: repo
---

The article argues that `pipe` helps balance two pressures in JavaScript: keeping APIs broad for common types and keeping shipped code small. It shows that prototype augmentation makes methods hard to tree-shake and can create global mutation problems, while functional composition avoids both.

## Reading notes

- JavaScript apps are shipped over a network, so smaller bundles matter because download and parse time affect responsiveness.
- Tree-shaking can remove unused code only when the bundler can statically prove it is unused.
- Attaching methods to a type’s prototype gives that type a broader API, but it mutates global objects and can be overwritten by other code.
- Prototype methods are not good candidates for tree-shaking because bundlers cannot know whether third-party code depends on them.
- Rewriting prototype methods as standalone functions makes them easier to remove when unused.
- The downside of standalone function calls is that they read from right to left when nested.
- A `pipe` function restores left-to-right readability by passing a value through a sequence of functions.
- `pipeWith` accepts the initial value first, then the functions to apply.
- Higher-order functions let piped functions accept extra arguments, as in `multiplyBy(2)`.
- `pipe` can be used to build reusable composed functions such as `tripleTheOdds`.
- The pattern is similar to RxJS’s `pipe` and the article connects it to the pipeline operator proposal in JavaScript.
