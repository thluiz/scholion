---
title: "Z-Shell Frequently-Asked Questions"
date: '2015-04-03T19:29:05-03:00'
category: webclip
summary: 'Explains how to make zsh your login shell without root access by using exec in a login file, with examples for Bourne-like and csh-like shells and cautions about .cshrc and SHELL.'
tags: ["zsh", "login-shell", "shell-configuration"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Z-Shell Frequently-Asked Questions"
    url: "http://zsh.sourceforge.net/FAQ/zshfaq01.html#l3"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-04/zsh-sourceforge-net--z-shell-frequently-asked-questions-1-7-login-shell-root-acce.md"
    kind: repo
---

The page explains that, when `chsh` is unavailable because the shell is not listed in `/etc/shells`, a personal copy of zsh can still be used at login by replacing the current shell with `exec <zsh-path>`. It recommends placing that command in a login file such as `.profile` for sh or ksh, or `.login` for csh, and warns that `exec` is unforgiving, so the file should be editable by some other means first.

It gives example snippets for `~/bin/zsh`, including optional confirmation prompts before calling `exec`. It also warns against putting this in `.cshrc` without checks, because every csh session would become zsh and csh scripts could fail. If zsh is launched from `.cshrc`, it suggests a minimal safety check with `if ($?prompt) exec zsh`, and notes that changing `SHELL` at the same time is sensible. If the user wants the process list to show `-zsh`, the page suggests linking `zsh` to `-zsh` and running `exec -zsh`, which has the same effect as `-l`.

## Reading notes

- Use `exec <zsh-path>` to replace the current shell with zsh at login.
- Put the command in `.profile` for sh or ksh, or in `.login` for csh.
- Keep a way to edit the login file before testing, because `exec` is unforgiving.
- A check before `exec` can ask the user to type Y.
- Avoid putting this in `.cshrc` without checks, because it affects every csh session and can break csh scripts.
- When launching zsh, update the `SHELL` environment variable to the full zsh path.
- To have the shell appear as `-zsh`, link `zsh` to `-zsh` and run `exec -zsh`.
- If root access exists, zsh should be added to `/etc/shells`, including on NIS clients, to avoid FTP problems.
