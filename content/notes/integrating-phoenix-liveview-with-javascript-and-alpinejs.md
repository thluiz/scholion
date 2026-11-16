---
title: "Integrating Phoenix LiveView with JavaScript and AlpineJS"
date: '2020-08-26T19:31:29+00:00'
category: webclip
summary: 'The article explains how LiveView hooks, AlpineJS, and Spruce let client-side code react to LiveView assigns, send events back to the server, and share state across components.'
tags: ["phoenix-liveview", "alpinejs", "javascript-hooks", "spruce"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Integrating Phoenix LiveView with JavaScript and AlpineJS • Patrick Thompson"
    url: "https://blog.pthompson.org/alpine-js-and-liveview"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/blog-pthompson-org--integrating-phoenix-liveview-with-javascript-and-alpinejs.md"
    kind: repo
---

The article argues that LiveView still benefits from some JavaScript for client-side reactions and transitions. It then shows how LiveView hooks, AlpineJS, and Spruce can be combined so hooks and Alpine components exchange events, track assigns, and share state across a page.

## Reading notes

- LiveView is presented as a way to build reactive apps without much JavaScript, but some JavaScript is still useful for client-side interactions and animations.
- LiveView JavaScript hooks register lifecycle callbacks on DOM nodes and can store state, access the element, and push events to LiveView or LiveComponents.
- The BeforeUnload hook uses a `beforeunload` handler to warn about unsaved changes and block navigation when needed.
- The BackHook uses an `updated` callback to trigger browser history navigation after an item is deleted.
- AlpineJS is described as a small companion to LiveView with syntax similar to Vue.js and support for client-side transitions.
- With the LiveView 0.13.3 integration, Alpine usually does not need `phx-update="ignore"` because Alpine can work with LiveView DOM updates.
- The article shows how to add the `dom.onBeforeElUpdated` callback in `LiveSocket` so Alpine state is cloned when LiveView patches the DOM.
- A counter example is used throughout the article to demonstrate increment and decrement events.
- Alpine components can call hook methods directly when the hook is attached to `window`, and those methods can use `pushEvent` and `pushEventTo`.
- Hooks can also relay custom browser events from Alpine to LiveView, though the article treats this as a more verbose alternative.
- Hooks can dispatch custom events back to Alpine, letting Alpine update local state when LiveView assigns change.
- LiveView assigns cannot be read directly inside Alpine markup, so the article shadows an assign inside `x-data` to keep Alpine state in sync.
- A watched shadowed assign can drive client-side behavior, such as opening or closing a modal and removing it after a delay.
- Alpine can add and remove DOM nodes with `x-for` while staying in sync with LiveView updates.
- Alpine custom events can publish a changed assign to sibling LiveViews and LiveComponents on the same page.
- Spruce is introduced as a global Alpine store that lets shadowed assigns be shared across multiple Alpine components and rendered LiveViews.
- The article closes by noting that global store data can also be accessed from hooks and other arbitrary JavaScript code.
