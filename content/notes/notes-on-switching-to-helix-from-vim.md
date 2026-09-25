---
title: "Notes on switching to Helix from Vim"
date: '2025-10-28T22:12:08+00:00'
category: webclip
summary: 'After three months with Helix, the author says built-in language servers, search, and simple configuration made the switch easier than expected, despite Markdown and reflow annoyances.'
tags: ["helix", "vim", "language-servers", "text-editor"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Notes on switching to Helix from vim"
    url: "https://jvns.ca/blog/2025/10/10/notes-on-switching-to-helix-from-vim/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-10/jvns-ca--notes-on-switching-to-helix-from-vim.md"
    kind: repo
---

The author tried Helix after hearing from a friend that it offers the same kind of low-configuration experience they liked in fish. After three months, Helix stood out for built-in language server support, strong search, a helpful quick reference, and a much simpler setup than Vim or Neovim.

## Reading notes

- Helix appealed because getting language servers working in Vim or Neovim felt like too much work.
- Built-in language server support makes actions like go to definition and rename symbol work across languages.
- Search in Helix shows matching files with full context, unlike the Vim ripgrep plugin the author used before.
- Pressing `g` opens a help popup with navigation options, which helps when shortcuts are easy to forget.
- Instead of Vim marks, the author uses `Ctrl+O` and `Ctrl+I` to move back and forward through cursor locations.
- For many edits that would have used macros, the author prefers multiple cursors and regex selection.
- Helix uses a buffer switcher instead of Neovim-style tabs, though there is a setting that can behave a bit like tabs.
- Reflowing text with `:reflow` works worse than Vim’s `gq`, especially for lists.
- Markdown lists do not continue automatically when pressing Enter at the end of a list item.
- Helix does not yet have persistent undo, so undo history does not survive quitting.
- Files do not auto-reload after on-disk changes, so `:reload-all` is needed.
- The editor sometimes crashes, roughly weekly.
- Switching was easier than expected after using Helix on a vacation coding project for a week or two.
- Trying to force Vim-like keybindings did not work well; learning the Helix way was easier.
- Vim and Helix differ on the meaning of `w`, especially around spaces after words.
- Moving from GUI Vim to a terminal editor required a workflow adjustment.
- The author now gives each project its own terminal window and puts the Helix tab first.
- The Helix configuration is much smaller than the author’s Neovim setup.
- The config remaps comment toggling, line-start and line-end movement, and reflow.
- Language-specific settings live in `languages.toml`, including turning off autoformatting for Python.
- After three months, the author still thinks they may switch back to Vim later.
