---
title: "You Don't Hate Mocks; You Hate Side-Effects"
date: '2026-11-16T03:07:48+00:00'
category: webclip
summary: 'The article argues that excessive mock expectations are a signal of side-effects in the design. Refactoring away from those side-effects often removes the mock and leads to simpler, more focused tests.'
tags: ["test-doubles", "side-effects", "tdd", "simple-design"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "You Don't Hate Mocks; You Hate Side-Effects"
    url: "https://blog.thecodewhisperer.com/permalink/you-dont-hate-mocks-you-hate-side-effects"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/blog-thecodewhisperer-com--you-dont-hate-mocks-you-hate-side-effects.md"
    kind: repo
---

The article argues that mocks are not the problem. Excessive expectations expose side-effects that make code harder to test. When the design changes, the mock often disappears as a consequence.

## Reading notes

- Here, mock means an expectation such as verify(), expect().toHaveBeenCalled(), or should_receive.
- Test doubles are treated as a design tool, not as something to avoid or keep for its own sake.
- Integrated tests are described as harder for isolating the cause of behavior problems and less suited to detecting specific side-effects.
- Replacing side-effects with return values can remove the need for test doubles and make tests simpler and more focused.
- Relying on integrated tests can create a feedback loop with tangled code and lower value from the tests.
- Excessive expectations often show that the programmer is not using the feedback from the test doubles.
- Refactoring away from side-effects can make expectations feel odd in tests, which signals a design issue worth addressing.
- One refactoring strategy is to replace an effect with a return value.
- Another strategy is to replace a group of related side-effects with a single event and subscribers.
- Excessive expectations are presented as a warning signal for design problems.
