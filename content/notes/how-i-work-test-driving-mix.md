---
title: "How I Work (Test-Driving Mix)"
date: '2020-02-22T12:11:44+00:00'
category: webclip
summary: 'GeePawHill says he does not separate testing from coding. He uses fast, precise microtests as an interactive way to steer small production changes and catch simple mistakes before shipping.'
tags: ["test-driven-development", "microtests", "programming-practice"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Thread by @GeePawHill: How I Work (Test-Driving Mix) A while back, I wrote a muse about how I work focused just on the coding I do. Today I want to talk about how…"
    url: "https://threadreaderapp.com/thread/1217120556098752512.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/threadreaderapp-com--how-i-work-test-driving-mix.md"
    kind: repo
---

GeePawHill describes testing as part of coding, not a separate activity. He works by moving back and forth between production code and test code, using an IDE and a dedicated test runner to keep tests fast, easy to switch, and easy to rerun. He writes microtests for small changes, keeps them all passing, and uses them to guide code changes one step at a time.

## Reading notes

- He says this is a description of what he does, not a prescription for others.
- He treats himself as the customer of his tests and uses them when the cost-benefit tradeoff is good for him.
- He coined “microtest” for tests that are short, precise, descriptive, fast, easy to grasp, executable, and persistent.
- He sometimes uses the test kit for code that is not a test, or for tests that are not microtests when debugging or when the code is not yet easy to microtest.
- He thinks of code as a directed acyclic graph of dependencies, with entry points and exit points.
- His basic workflow is to find a minimal part of a path, write a microtest that fails, change the code until it passes, then make sure the existing microtests still pass before pushing.
- He says the value of tests is not only the test artifact itself, but also the way TDD helps him reshape code so it can be tested.
- He uses tests mainly for branching logic in code he owns, not to prove that customer understanding is correct or that external systems behave properly.
- He says most bugs he ships are simple mistakes such as off-by-one errors, inverted conditions, incomplete case splits, unhandled edge cases, literal spelling mistakes, ordering assumptions, and external configuration issues.
