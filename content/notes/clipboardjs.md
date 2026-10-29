---
title: "clipboard.js"
date: '2015-10-19T08:55:10-03:00'
category: webclip
summary: 'clipboard.js is a modern text-copy library that avoids Flash and heavy dependencies, uses event delegation and HTML5 data attributes, and exposes success, error, and cleanup hooks.'
tags: ["javascript", "clipboard", "html5-data-attributes", "event-delegation"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "clipboard.js"
    url: "https://zenorocha.github.io/clipboard.js/"
    kind: repo
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-10/zenorocha-github-io--clipboardjs.md"
    kind: repo
---

clipboard.js is presented as a small library for copying text to the clipboard without Flash or extra dependencies. It installs through npm, bower, a ZIP download, or a CDN, and it is initialized with a DOM selector that points to the trigger elements.

## Reading notes

- It is described as a modern way to copy text to the clipboard, with a 2kb footprint.
- The setup loads the script from the dist folder or from a CDN.
- The library is instantiated with a selector such as .btn.
- It uses event delegation so many matching elements do not need many listeners.
- It uses HTML5 data attributes for its main usage patterns.
- data-clipboard-target copies from another element.
- data-clipboard-action sets copy or cut, with copy as the default.
- cut works only on input or textarea elements.
- data-clipboard-text copies text directly from the trigger element.
- success and error events let the user add feedback or custom logic.
- The advanced API allows a target function that returns a Node.
- The advanced API allows a text function that returns a String.
- clipboard.destroy() removes the events and objects created by the library.
- Browser support depends on Selection and execCommand.
- On Safari, execCommand copy and cut are not supported, but Selection still works and the page can fall back to a selected text prompt.
