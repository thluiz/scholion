---
title: "A huge productivity boost in git with a single alias"
date: '2020-09-12T19:01:02-03:00'
category: webclip
summary: 'The post suggests using a shell alias so `g` runs `git`, then shares a few Git config tweaks: global ignore files, `pull --rebase`, autocorrect, and reusable aliases.'
tags: ["git", "command-line", "productivity"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "A huge productivity boost in git with a single alias - DEV Community 👩‍💻👨‍💻"
    url: "https://dev.to/xoubaman/a-huge-productivity-boost-in-git-with-a-singe-alias-3pij"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-09/dev-to--a-huge-productivity-boost-in-git-with-a-single-alias.md"
    kind: repo
---

The post recommends adding a shell alias so `g` expands to `git`, which reduces repeated typing in daily use. It also shares a few personal Git configuration choices kept in `~/.gitconfig`, including a global ignore file, default rebase on pull, and autocorrect for mistyped commands.

## Reading notes

- Add `alias g='git'` in `.bashrc` or a similar shell file so `g pull` can replace `git pull`.
- Use a global ignore file through `core.excludesfile` for common files such as `.DS_Store` and `Thumbs.db`.
- Enable `pull.rebase = true` to make `git pull` use rebase by default.
- Turn on `help.autocorrect = 5` so Git can correct mistyped commands after a short delay.
- Keep custom Git aliases that print the full command before running it, including shortcuts for status, add, commit, checkout, amend, sync with rebase, and a colored log view.
- The closing advice is to optimize repeated tasks during the day.
