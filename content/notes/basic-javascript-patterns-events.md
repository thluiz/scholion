---
title: "Basic JavaScript Patterns — Events"
date: '2020-07-05T14:11:17+00:00'
category: webclip
summary: 'The article says event handling in JavaScript should stay clean and separate from HTML markup. It shows moving click handling into JavaScript and gaining access to the event object.'
tags: ["javascript", "events", "separation-of-concerns"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Basic JavaScript Patterns — Events"
    url: "https://javascript.plainenglish.io/basic-javascript-patterns-events-b1795db01f26"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/javascript-plainenglish-io--basic-javascript-patterns-events.md"
    kind: repo
---

The article argues that JavaScript can be too forgiving in its syntax, so basic design patterns help organize code. In this part, it focuses on events and says user-event handling should be done cleanly and without putting handlers in HTML.

## Reading notes

- JavaScript can be too forgiving in its syntax, so basic design patterns help organize code.
- The article looks at events, HTTP requests, and background tasks.
- User-event handling should be done in a clean way.
- Event handling should not violate separation of concerns.
- A click handler should stay in JavaScript instead of being placed in HTML markup.
- Keeping click handling in JavaScript makes later changes easier.
- Handling events requires access to the event object.
