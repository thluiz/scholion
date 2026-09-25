---
title: "Opportunistic Refactoring"
date: '2026-09-25T17:53:08+01:00'
category: webclip
summary: 'Refactoring should happen continuously and opportunistically, whenever code needs cleanup, while tests are green. Small changes done now keep the codebase healthier and reduce slower progress later.'
tags: ["refactoring", "codebase-health", "technical-debt"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "bliki: Opportunistic Refactoring"
    url: "https://martinfowler.com/bliki/OpportunisticRefactoring.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/martinfowler-com--opportunistic-refactoring.md"
    kind: repo
---

Refactoring works best as a continuous habit rather than a separate phase. When code looks unclear, duplicated, or awkward to extend, the right move is usually to fix it right away or soon after, as long as the tests stay green. Small changes made in the moment keep the codebase easier to work with and help the team move faster over time.

## Reading notes

- Refactoring should be opportunistic, done whenever and wherever code needs to be cleaned up, by whoever notices it.
- The camp site rule is to leave code in a better state than you found it.
- Refactoring can happen before implementation, while adding functionality, or after finding a better interaction with existing classes.
- If you spot a refactoring while doing something else, note it and return to it the same day.
- Refactoring should not be separated from the work of adding value, because it keeps the codebase easier to change.
- Good judgment matters, since opportunistic refactoring can turn into a rabbit hole if you keep expanding the scope.
- A refactoring can apply to any part of the codebase, even outside the class you are currently working on.
- A good regression suite is important, and extra tests can be added when a part of the system feels weak.
- Development practices that make refactoring harder, such as strong code ownership or feature branches, should be treated as a problem.
- If a small refactoring feels discouraged, that friction should be raised with the team and discussed in a retrospective.
- Planned refactoring can still make sense for a difficult area, but teams should usually see refactoring as a constant stream of small adjustments.
