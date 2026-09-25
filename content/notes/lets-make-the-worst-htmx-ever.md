---
title: "Let's make the worst htmx ever!"
date: '2026-08-05T19:04:02+01:00'
category: webclip
summary: 'The article builds a tiny htmx clone in JavaScript, then adds triggers, targets, swapping, custom events, server headers, and plugins through a scan/send/swap loop.'
tags: ["htmx", "javascript", "frontend", "plugins"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Let's make the worst htmx ever!"
    url: "https://zserge.com/posts/worst-htmx-ever/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-08/zserge-com--lets-make-the-worst-htmx-ever.md"
    kind: repo
---

The article shows how to build a small htmx clone by wiring together triggers, targets, request sending, and DOM swapping. It starts from a simple click handler and grows into a scan/send/swap core that supports custom methods, swap modes, mutation-based rescanning, and richer trigger parsing.

## Reading notes

- The post is part of a series about tiny clones of popular web frameworks.
- htmx is presented as a frontend library for backend developers who prefer to avoid JavaScript.
- A button can declare a method, trigger, target, and swap mode, and the browser can then send a request and replace part of the DOM with the response.
- The first version of the clone uses a `fetch()` call on elements marked with a method attribute and replaces the element with the returned HTML.
- The core is expanded to sanitize responses, support separate targets, and let the user choose how content is swapped.
- A generic `send()` function handles method, URL, target resolution, swap mode, and form bodies.
- A `scan()` function binds events for supported methods and uses a default trigger based on the element type.
- A `MutationObserver` limits rescanning to newly added nodes after swaps.
- Trigger syntax is extended to support comma-separated events with modifiers such as `once`, `changed`, and `delay`.
- Target resolution is extended to support values like `this`, `next`, `previous`, `document`, `body`, `window`, `closest`, and `find`.
- The code emits custom events before and after requests and swaps, and it can react to server headers such as `HX-Trigger`, `HX-Redirect`, `HX-Refresh`, `HX-Retarget`, and `HX-Reswap`.
- The article treats the library’s core as `scan + send + swap`.
- Plugins are proposed for confirmation, indicators, disabling elements, custom headers, extra values, response selection, request synchronization, validation, URL history, server-sent events, and websockets.
- The author says the approach gets close to HTMX feature coverage, but that full compatibility would still need better error handling, exposed helpers, and asynchronous cancellation.
- The post ends by linking to the code on GitHub and inviting contributions.
