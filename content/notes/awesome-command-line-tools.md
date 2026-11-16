---
title: "Awesome Command-Line Tools"
date: '2026-11-16T00:52:59+00:00'
category: webclip
summary: 'The page recommends CLI tools for common shell tasks: quick usage lookups, directory jumping, prettier diffs, syntax-highlighted file viewing, faster search, colorful listing, and fuzzy finding.'
tags: ["cli-tools", "shell", "fuzzy-search"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Awesome Command-Line Tools"
    url: "https://dev.to/janis_t/awesome-command-line-tools-204n"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--awesome-command-line-tools.md"
    kind: repo
---

The page collects command-line tools the author uses regularly in the terminal. It presents each one as a replacement or upgrade for a familiar utility, with examples of how to wire it into the shell through aliases or config.

## Reading notes

- tldr gives short usage descriptions and common examples when man pages feel too long for a quick lookup.
- rupa/z tracks frequently used directories and lets the user jump to them with a partial path, with j suggested as an easier command name.
- diff-so-fancy replaces diff or git diff and shows changes with improved colors and intra-line highlighting.
- bat replaces cat with syntax highlighting for many languages and Git integration that shows file changes.
- ripgrep is presented as a faster alternative to ag and respects .gitignore by default.
- exa is a colorful replacement for ls that keeps ls-like compatibility and offers friendlier defaults.
- fd is described as a faster alternative to find with simpler usage and colorized output.
- fzf provides fuzzy search over lines, files, and command history, and it can preview files and work with z.
- The author’s setup uses iTerm2, Menlo, Afterglow, zsh with oh-my-zsh, and a custom theme.
