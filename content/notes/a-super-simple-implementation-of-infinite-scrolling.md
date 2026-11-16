---
title: "A super simple implementation of Infinite Scrolling"
date: '2026-11-16T00:54:29+00:00'
category: webclip
summary: 'The post shows a jQuery scroll handler that clicks a “load more” button when the page reaches the bottom, then adjusts the check to fire 300 pixels before the end for better mobile behavior.'
tags: ["infinite-scrolling", "jquery", "pagination"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "A super simple implementation of Infinite Scrolling"
    url: "https://dev.to/sakun/a-super-simple-implementation-of-infinite-scrolling-3pnd"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--a-super-simple-implementation-of-infinite-scrolling.md"
    kind: repo
---

The post explains how to turn a “load more” pagination pattern into infinite scrolling with jQuery. It starts with a window scroll event that compares document height and scroll position, then triggers the pagination button when the user reaches the bottom.

## Reading notes

- The setup assumes a site with pagination and jQuery already added.
- The scroll handler uses `scrollHeight` and `scrollPos` to detect when the page bottom is reached.
- When the condition is met, it clicks `.load-more-days-button`.
- The author says the exact bottom check works, but it feels too strict and is unreliable on mobile.
- The revised check fires when the user is 300 pixels above the bottom of the page.
- The post ends with a complete example that combines the scroll handler, the height check, and the button click.
