---
title: "Cure Impostor Syndrome with Functional Programming"
date: '2019-07-13T22:15:55+00:00'
category: webclip
summary: 'The author argues that web development’s churn and technical debt come from relying on ad hoc fixes instead of mathematical thinking, and says functional programming helps build smaller, more reliable, reusable code.'
tags: ["functional-programming", "javascript", "technical-debt", "software-engineering"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Cure Impostor Syndrome with Functional Programming"
    url: "https://dev.to/ltruchot/cure-impostor-syndrome-with-functional-programming-3ih6"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--cure-impostor-syndrome-with-functional-programming.md"
    kind: repo
---

The author says years of web development left him feeling like an impostor because his projects kept aging out, breaking down, and disappearing. He argues that common advice about tools, frameworks, and best practices still leaves codebases bloated and fragile, and that the missing piece is mathematics, especially functional programming.

## Reading notes

- He describes his move into teaching as a way to question his own skills and address impostor syndrome.
- He claims many web projects disappear or become too costly to maintain because they grow too large, too buggy, and too dependent on changing technology.
- He reverses the usual advice and says developers should stop adding code, stop patching endlessly, and stop changing frameworks every month.
- He presents functional programming as the missing foundation, tied to math topics like Boolean algebra, monoids, and composability.
- He argues that programs should use less code, rely on pure functions, and keep effects outside the core logic.
- He says the useful distinction is between what is already computed and what still needs a function to compute it.
- He recommends learning FP gradually through tools and functions such as map, filter, reduce, compose, and pipe.
- He proposes an onion-like architecture with layers for language, shared utilities, domain helpers, current services, and the top-level program.
- He says this approach makes refactoring easier, keeps codebases more reliable, and has helped reduce his own impostor syndrome.
- He ends by recommending FP languages and resources such as PureScript, ClojureScript, ReasonReact, fp-ts, Elm, SICP, and FP communities and podcasts.
