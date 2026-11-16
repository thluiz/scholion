---
title: "Why Development Teams are Slow"
date: '2026-11-16T06:18:04+00:00'
category: webclip
summary: 'The article argues that slow teams usually reflect management problems: unrealistic expectations, too many open issues, oversized tasks, review bottlenecks, weak training, burnout, poor retention, and bugs.'
tags: ["software-management", "developer-productivity", "code-review", "ci-cd"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Why Development Teams are Slow. Common Software Jams and Solutions | by Eric Elliott | JavaScript Scene | Medium"
    url: "https://medium.com/javascript-scene/why-development-teams-are-slow-89107985c75c"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/medium-com--why-development-teams-are-slow.md"
    kind: repo
---

The article says that “developers are too slow” is a symptom, not a cause. It ties slow delivery to management choices, especially bad expectations, too much backlog, large tasks, delayed code review, weak training, burnout, retention problems, and bugs.

## Reading notes

- Unrealistic expectations are the most common cause of perceived slowness, and software schedules are hard to predict because scope and complexity are discovered during development.
- Predictive burndown charts and closed-ticket counts are criticized as misleading metrics, especially when they become targets.
- Too many open issues create rework because each ticket must be triaged, prioritized, assigned, and understood before work starts.
- Task size should be small enough to finish in about a day, with large features split into independently testable pieces and safer shipped with feature toggles.
- Large pull requests create code review pileups, merge conflicts, and churn, while small PRs reduce rework and keep integration moving.
- Poor training slows teams because many developers lack guidance on software foundations, so managers should support mentoring, pairing, and code review learning.
- Burnout is treated as a management failure and a health risk, and the article recommends better prioritization, scope cuts, and reducing churn instead of pushing harder.
- Poor retention is costly because recruiting, onboarding, and ramp-up add large expense and delay, so the article recommends fair pay, raises, vacation, remote work, training, benefits, and reasonable hours.
- Bugs slow teams because fixing production defects causes interruptions, extra process steps, customer support load, and additional rework.
- The article recommends design review, code review, TDD, CI/CD, and stronger test coverage to reduce defects and speed delivery over time.
