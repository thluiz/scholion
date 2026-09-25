---
title: "99% of frontend devs don't use this"
date: 2026-09-23T15:10:45+01:00
category: webclip
summary: "Antonio Moruno Gracia argues data-* attributes beat closures inside React's .map() when React.memo or useCallback need a stable function reference to actually work."
tags: ["react", "javascript", "frontend", "performance"]
has_commentary: false
sources:
  - title: "99% of frontend devs don't use this - DEV Community"
    url: "https://dev.to/moruno21/99-of-frontend-devs-dont-use-this-1g44?context=digest"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-07/dev-to--99-of-frontend-devs-dont-use-this.md"
    kind: repo
---

In a list rendered with `.map()`, Antonio Moruno Gracia contrasts `onClick={() => handleClick(item.id)}`, a closure recreated for every item on every render, with `data-id={item.id}` read back out in a single shared handler through `e.currentTarget.dataset.id`. HTML's `data-*` attributes attach the item's id straight to the DOM element instead of capturing it in a new function each time.

With `React.memo` or `useCallback` in place, recreating the closure on every render changes the function reference and invalidates the memoization those tools depend on.

## Reading notes

- With `data-*`, metadata attaches straight to the DOM element. A single stable `handleClick` function reads the id back out through `e.currentTarget.dataset` instead of a new closure getting created for each item in the list.
- Since the function reference stays the same across renders, memoization actually prevents the re-render it's supposed to prevent. A fresh closure defeats that every time, regardless of `React.memo` or `useCallback` being in place.
- Moruno frames `data-*` as underused because closures are simpler to write and perform fine in most apps, not because `data-*` is objectively better. It becomes worth the extra step in large or re-render-sensitive lists specifically.
- [Should Junior Developers Still Learn JavaScript the Hard Way?](/notes/should-junior-devs-still-learn-javascript-hard-way/) treats closures as one of the core fundamentals worth understanding deeply. This post makes the sharper case for knowing exactly what a closure costs, not just what it is.
