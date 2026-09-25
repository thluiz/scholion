---
title: "Software Architecture and the Art of Experimentation"
date: '2026-09-25T22:28:48+01:00'
category: webclip
summary: 'The article argues that architectural decisions should be treated as experiments. Minimum Viable Architectures test viability, supportability, and future change so teams can catch wrong assumptions before costs grow.'
tags: ["software-architecture", "experimentation", "minimum-viable-architecture", "mvp"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Software Architecture and the Art of Experimentation"
    url: "https://www.infoq.com/articles/architecture-experimentation/?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/infoq-com--software-architecture-and-the-art-of-experimentation.md"
    kind: repo
---

Software architecture is presented as a set of decisions that should be tested through small experiments, because wrong assumptions are inevitable and costly to reverse. The article ties Minimum Viable Architecture to the MVP, saying each release should gather data about value, technical viability, supportability, and the cost of change.

## Reading notes

- Architectural work should use experiments to test decisions that matter most, especially the ones that would be most damaging if wrong.
- A Minimum Viable Architecture is the set of decisions that lets an MVP deliver value over time in a sustainable way.
- If the team does not run architectural experiments, its decisions remain assumptions and guesses.
- A product release can be treated as a set of experiments about value and supportability.
- Effective experiments are atomic, timely, and unambiguous.
- An experiment needs a clear hypothesis, a measurable goal, a method for measuring success or failure, a rollback plan when needed, and a timeline that fits the release timebox.
- If an experiment fails, extending it should count as a new experiment rather than a continuation of the old one.
- Architectural work also needs experiments about support and future change, including how hard it is to add new kinds of assets, events, or rules.
- Systems should be designed to fail gracefully and give support staff enough information to diagnose problems.
