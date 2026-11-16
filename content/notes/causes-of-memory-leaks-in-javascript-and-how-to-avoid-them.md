---
title: "Causes of Memory Leaks in JavaScript and How to Avoid Them"
date: '2026-11-16T03:53:13+00:00'
category: webclip
summary: 'The article explains how memory leaks happen in JavaScript, how to spot them with browser tools, and which coding patterns most often keep objects alive too long in SPAs.'
tags: ["javascript", "memory-leaks", "browser-tools", "single-page-applications"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Causes of Memory Leaks in JavaScript and How to Avoid Them"
    url: "https://ditdot.hr/en/causes-of-memory-leaks-in-javascript-and-how-to-avoid-them"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/ditdot-hr--causes-of-memory-leaks-in-javascript-and-how-to-avoid-them.md"
    kind: repo
---

The article says memory leaks matter more in SPAs because growing JavaScript memory use can hurt performance and even crash the browser tab. It defines a leak as an object that stays reachable through an unintended reference, and points to Task Manager, Performance, and Memory tools as ways to detect it.

## Reading notes

- In older page-based websites, memory is usually cleared as the user moves between pages, but SPAs need more care with JavaScript memory management.
- A memory leak happens when an object that should be collected stays reachable from the root through an unintended reference.
- Browser Task Managers can show the JavaScript memory footprint of each tab, and steady growth while the page is idle can signal a leak.
- Developer Tools can reveal leak patterns through performance recordings and heap snapshots.
- Accidental global variables stay reachable from the root and are not garbage collected; strict mode helps prevent this.
- Closures keep referenced variables alive after the outer function has finished, so their lifespan and retained objects need attention.
- Timers can keep objects in memory through callback references until the timer is cleared.
- Event listeners retain captured variables until they are removed or the DOM element is removed; anonymous listeners are harder to clean up.
- Using `{once: true}` makes an event listener remove itself after running once.
- A cache can grow without limit if unused entries are never removed; `WeakMap` can let entries disappear when the key is no longer referenced.
- A DOM node can remain in memory after removal from the document if JavaScript still holds a direct reference to it.
- Moving DOM references into local scope can help avoid detached elements lingering in memory.
