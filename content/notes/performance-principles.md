---
title: "Performance Principles"
date: '2026-09-25T21:37:41+01:00'
category: webclip
summary: 'The page frames performance as reducing unnecessary work, shortening paths, caching repeated computations, and moving loading earlier with prefetching or preloading, including mobile-specific timing.'
tags: ["performance", "caching", "prefetching", "preloading"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Performance Principles"
    url: "https://tigerabrodi.blog/performance-principles?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/tigerabrodi-blog--performance-principles.md"
    kind: repo
---

The page treats performance as a set of practical questions: can you do less work, take a shorter route, avoid repeating work, or do some work ahead of time. It uses examples from programming and frontend work to show how those choices reduce cost or make navigation feel instant.

## Reading notes

- If only part of a dataset is needed, stop processing early instead of looping through everything.
- For nested lookups, build a map or a Set so lookups are O(1) after an O(n) setup cost.
- Caching avoids recalculating expensive results by storing them in a map and checking it first.
- Prefetching page data and resources before navigation can make the next page load feel instant.
- On mobile, where hover does not exist, prefetching can wait until the browser is idle with `requestIdleCallback`, with `setTimeout` as a fallback.
- For image carousels, swiping the first image can trigger preloading of the remaining images.
