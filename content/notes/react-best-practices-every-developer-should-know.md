---
title: "React Best Practices Ever Developer Should Know"
date: '2026-09-25T22:07:46+01:00'
category: webclip
summary: 'The guide recommends keeping React state immutable, avoiding useState for everything, deriving and computing values during render when possible, using unique keys, and leaving useEffect for real side effects.'
tags: ["react", "react-hooks", "state-management", "useeffect"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "React Best Practices Ever Developer Should Know"
    url: "https://www.freecodecamp.org/news/react-best-practices-ever-developer-should-know/?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/freecodecamp-org--react-best-practices-every-developer-should-know.md"
    kind: repo
---

The article presents React practices aimed at simpler code and better performance. It argues that state should stay immutable, that not every value belongs in useState, and that derived or computed values should usually be created during render instead of stored in state or moved into effects.

## Reading notes

- State should be treated as immutable so React can detect changes reliably and re-render correctly.
- Adding data to arrays should be done by creating a new array instead of mutating the existing one.
- useState should not be used for every value, especially when server state, URL state, or local storage already fit better.
- Values that can be derived from props or existing state should be calculated during render.
- Simple computations should not be moved into useEffect, and expensive ones can use useMemo.
- List items should have unique keys, and array indexes can cause bugs.
- Dependencies in useEffect should be complete to avoid stale closures and missed updates.
- useEffect should be a last resort when side effects are not handled more cleanly by derived values, event handlers, server-side fetching, or dedicated libraries.
