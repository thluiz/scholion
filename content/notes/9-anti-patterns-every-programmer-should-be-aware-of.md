---
title: "9 Anti-Patterns Every Programmer Should Be Aware Of"
date: '2015-05-11T16:03:54-03:00'
category: webclip
summary: 'The article lists recurring programming anti-patterns and explains how to spot them, why they hurt design and progress, and when to prefer simpler, evidence-based choices instead.'
tags: ["anti-patterns", "software-design", "programming-practices"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "9 Anti-Patterns Every Programmer Should Be Aware Of"
    url: "http://sahandsaba.com/nine-anti-patterns-every-programmer-should-be-aware-of-with-examples.html?utm_content=buffer33a5d&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-05/sahandsaba-com--9-anti-patterns-every-programmer-should-be-aware-of.md"
    kind: repo
---

The article argues that programmers should cultivate self-criticism to spot unproductive patterns in design, code, process, and behavior. It treats anti-patterns as guidelines rather than fixed rules and warns against dogmatic thinking. Each section explains what the anti-pattern is, why it is harmful, how to avoid it, and when the boundary cases are hardest to judge.

## Reading notes

- Premature optimization means trying to optimize before there is enough data to know where the bottleneck is, which usually adds complexity and bugs for little gain.
- Bikeshedding is spending too much time debating trivial or subjective choices, such as UI colors or indentation style.
- Analysis paralysis happens when over-analysis delays or blocks action, and the article recommends iterating so decisions can be based on new feedback.
- God classes accumulate many dependencies and responsibilities, making them hard to test, debug, document, and maintain.
- Fear of adding classes can keep designs too tangled, even when breaking a large class into smaller ones would simplify the system.
- The inner-platform effect appears when software reimplements features already provided by the platform or language, often poorly.
- Magic numbers and strings hide meaning in unnamed literals, which makes code harder to understand and refactor.
- Management by numbers uses metrics too rigidly for decisions, even when the measurements no longer match reality or become easy to game.
- Useless classes add abstraction without responsibility, acting as pass-through wrappers that increase confusion and maintenance work.
