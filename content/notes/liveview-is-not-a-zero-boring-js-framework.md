---
title: "LiveView Is Not a Zero-JS Framework, It’s a Zero-Boring-JS Framework"
date: '2026-09-25T21:42:35+01:00'
category: webclip
summary: 'The post argues that LiveView can cover most app needs without much JavaScript, while still leaving client-side code for richer browser-only features and hooks.'
tags: ["phoenix-liveview", "javascript", "client-hooks", "typescript"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "LiveView Is Not a Zero-JS Framework, It’s a Zero-Boring-JS Framework - Tyler Barker"
    url: "https://tylerbarker.com/posts/liveview-is-not-a-zero-js-framework-it-s-a-zero-boring-js-framework?utm_medium=email&utm_source=elixir-radar"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/tylerbarker-com--liveview-is-not-a-zero-boring-js-framework.md"
    kind: repo
---

LiveView can handle most of the JavaScript that other frameworks usually require, including routing, auth, and other app logic, while leaving only the client-side parts that are actually needed for richer browser interactions. The post frames this as a way to avoid boring JavaScript, not all JavaScript.

## Reading notes

- LiveView can take over much of the JS that would otherwise be written for routing, auth, and similar app behavior.
- The client-side code that remains is presented as the fun part, such as data visualization, Web Audio, Gamepad API work, and WebGL.
- The author says client hooks make LiveView a strong fit for complex browser behavior.
- A client hook is a JavaScript object with lifecycle methods like `mounted()`, `updated()`, `destroyed()`, and `reconnected()`.
- Hooks are registered in `app.js` and then used from HEEX templates through `phx-hook`.
- The post shows a hook that listens for scroll events and pushes a `load-more` event to LiveView.
- The hook keeps its own state on the object and updates it when the DOM changes.
- The author also shows a closured hook pattern, where a function returns the hook object so the hook can use variables from the function closure.
- A custom `hookState` helper is used to store and update state in that closure.
- The author defines a narrower `StatefulViewHook` type because the community LiveView types do not fit this pattern well.
- In the Prototape example, the hook reads browser media devices, filters audio devices, and pushes them to LiveView with `pushEvent`.
- The hook tracks known device IDs so it only pushes updates when the list changes.
- The hook resets state on `destroyed()` and re-runs the device push on `reconnected()`.
- The post also shows server replies to `pushEvent`, and server-to-client messages handled with `hook.handleEvent`.
- For immediate client-side actions, the post uses `LiveView.JS.dispatch` to trigger browser events without a server round trip.
- A drawback of closured hooks is that state in the function closure is shared if the same hook is used more than once on a page.
- The author notes that integrating React, Svelte, Vue, or Solid is still an option when client-side state heavily shapes the markup.
- The post ends by mentioning an effort to port Phoenix and LiveView JavaScript to TypeScript.
