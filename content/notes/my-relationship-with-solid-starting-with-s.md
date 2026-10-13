---
title: "My relationship with SOLID - Starting with S"
date: '2013-09-27T10:16:33-03:00'
category: webclip
summary: 'The post argues that single responsibility works best as a vertical concern tied to feature behavior and state, not as a stack of horizontal layers. It warns that premature separation creates layer soup.'
tags: ["solid", "single-responsibility-principle", "layer-soup", "state"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "My relationship with SOLID - Starting with S"
    url: "http://codeofrob.com/entries/my-relationship-with-solid---starting-with-s.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-09/codeofrob-com--my-relationship-with-solid-starting-with-s.md"
    kind: repo
---

The post revisits the single responsibility principle as part of the author’s changing view of SOLID. It argues that the main mistake is treating responsibility as a set of horizontal layers, when the stronger idea is a vertical slice centered on a feature and the state it changes.

## Reading notes

- The author connects the topic to earlier experiences with SOLID, TDD, and GoF patterns, and says over-zealous readings of these ideas can damage codebases.
- The single responsibility principle is presented as a source of confusion because people split systems into controllers, services, data layers, and interfaces instead of focusing on one feature.
- The author contrasts horizontal abstractions with vertical work, such as writing a feature to manage book availability in a library.
- Mutable state is treated as a useful guide: cohesive classes should have methods that touch most of their state, while split responsibilities often show up as duplicated access, getters, visitors, or bags of state passed around.
- If behavior must jump through many classes to find or change the state it affects, the design has likely gone too far.
- State persistence is described as a poor candidate for a vague horizontal layer, while feature-specific objects that own state and persist it make the code easier to understand and trace.
- Logging and authentication can be orthogonal concerns, but the post warns that treating too many things as orthogonal leads to layer soup.
- The author prefers discovering reusable concerns over time rather than isolating them too early.
- At the module level, single responsibility matters when code can be treated as a disposable unit with clear boundaries, independent versioning, and an easy path to rewrite or refactor.
- The post closes by saying this is only the first and least controversial SOLID rule, and that the next entries will continue through the rest of the set.
