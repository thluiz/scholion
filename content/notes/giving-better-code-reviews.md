---
title: "Giving better code reviews"
date: '2016-02-07T22:54:23-03:00'
category: webclip
summary: 'The article argues that code reviews should go beyond a quick approval. Reviewers need a light pass and a deeper contextual pass, keep diffs small, and ask questions that improve code quality and team understanding.'
tags: ["code-reviews", "code-quality", "testing", "pull-requests"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Giving better code reviews — Medium"
    url: "https://medium.com/@mrjoelkemp/giving-better-code-reviews-16109e0fdd36"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-02/medium-com--giving-better-code-reviews.md"
    kind: repo
---

Code reviews are presented as a key process for spreading knowledge and best practices across a development team. The text argues that review quality is often inconsistent because teams leave improvement to individual reviewers, and that weak reviewers set the ceiling for the whole team.

## Reading notes

- The review process has at least two phases, and many people stop at the first one.
- The light pass looks for obvious mistakes, at least one test, deleted commented-out code, and styleguide violations that linters do not catch.
- The contextual pass goes deeper and checks idiomatic framework use, test coverage, meaningful test behavior, stronger tests, refactors, edge cases, logical omissions, and missing spec details.
- Reviewers should question code kindly, assume mistakes may exist, and ask about specific lines when needed.
- Pull requests should be small, because large diffs reduce review quality and force repeated reviews after changes.
- When a reviewer lacks context, the author should look for another reviewer or walk through the diff step by step.
- Blocking and non-blocking comments can help separate essential issues from optional ones.
- Reviewing code is described as a craft that should improve code understanding, review criteria, and the team’s ability to write correct diffs.
