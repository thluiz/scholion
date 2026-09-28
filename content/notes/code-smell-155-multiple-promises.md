---
title: "Code Smell 155 — Multiple Promises"
date: '2022-08-05T10:27:57-03:00'
category: webclip
summary: 'Waiting for promises one by one creates indeterminism and a performance bottleneck. If all results are needed, they should be awaited together with Promise.all.'
tags: ["performance", "promises", "javascript"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Code Smell 155 — Multiple Promises | by Maximiliano Contieri | Aug, 2022 | Level Up Coding"
    url: "https://levelup.gitconnected.com/code-smell-155-multiple-promises-67cccd8795c"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-08/levelup-gitconnected-com--code-smell-155-multiple-promises.md"
    kind: repo
---

The page says that waiting for promises in a sorted order can block work unnecessarily. If the rule is to wait for all operations, the code should let them run in parallel and collect the results together.

## Reading notes

- The smell is described as indeterminism and a performance bottleneck.
- The suggested solution is to wait for all promises at once.
- The context compares this to semaphores and the need to wait until all conditions are met, regardless of ordering.
- The wrong example awaits fetchOne before fetchTwo, which prevents parallel execution.
- The right example uses Promise.all with fetchOne and fetchTwo together.
- The smell is marked as semi-automatic and semantic, with linters able to find related promise-waiting patterns.
- The conclusion says software should stay close to real-world business rules and avoid forcing a particular order when the rule only requires all operations to finish.
