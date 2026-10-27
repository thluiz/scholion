---
title: "Create Keyboard Shortcuts with Mousetrap"
date: '2013-07-12T10:24:07-03:00'
category: webclip
summary: 'The page shows how Mousetrap binds single keys, combinations, sequences, aliases, unbinding, and triggering, framing it as a tiny utility for richer keyboard handling in web apps.'
tags: ["mousetrap", "keyboard-shortcuts", "javascript"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Create Keyboard Shortcuts with Mousetrap"
    url: "http://davidwalsh.name/keyboard-shortcuts?utm_source=javascriptweekly&utm_medium=email"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-07/davidwalsh-name--create-keyboard-shortcuts-with-mousetrap.md"
    kind: repo
---

Mousetrap is presented as a small library for adding keyboard shortcuts to web apps. The page emphasizes that keyboard shortcuts can make navigation faster, and shows how the library handles single keys, combinations, sequences, aliases, unbinding, and manual triggering.

## Reading notes

- The post treats keyboard shortcuts as one of the small details that can make web apps feel faster and more useful.
- Mousetrap’s `bind` method listens for a key or key pattern, a callback, and an optional event.
- Keys can be referenced by name instead of key code numbers.
- Multiple keys can be combined with `+`.
- Sequences can be written by separating keys with spaces.
- Alternative shortcuts can be passed as an array, such as `command+s` and `ctrl+s`.
- Modifier keys like `SHIFT` and `CONTROL` can be used.
- Keys that require `SHIFT` can also be bound without naming the shifted character separately.
- `unbind` removes listeners for given keys.
- `trigger` can fire a bound shortcut programmatically.
- The page says Mousetrap gives maximum control over key events and links to the official documentation for more advanced features.
- It describes Mousetrap as simple, useful, and tiny, and suggests it is best when advanced keyboard handling and navigation are needed.
