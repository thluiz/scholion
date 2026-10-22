---
title: "A productive command-line Git workflow for indie app developers"
date: '2020-11-13T10:01:15-03:00'
category: webclip
summary: 'The article shows a terminal-first Git workflow built around aliases, commitizen, tig, and vim-fugitive to speed up everyday Git tasks and review history.'
tags: ["git", "command-line", "vim", "developer-workflow"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "A productive command-line Git workflow for indie app developers - DEV Community 👩‍💻👨‍💻"
    url: "https://dev.to/craftzdog/a-productive-command-line-git-workflow-for-indie-app-developers-k7d?utm_source=digest_mailer&utm_medium=email&utm_campaign=digest_email"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-11/dev-to--productive-command-line-git-workflow-indie-app-developers.md"
    kind: repo
---

The article describes a solo developer’s Git workflow centered on the terminal. It uses short aliases to reduce typing, commitizen for structured commit messages, tig for browsing history, and vim-fugitive to work with Git inside Vim. It also shows how the same setup helps with release notes and quick inspection of older changes.

## Reading notes

- Git is used from the terminal rather than GUI clients, with aliases such as `g`, `st`, `ps`, `pl`, `br`, `hist`, `llog`, `df`, and `open` to shorten repeated commands.
- `commitizen` is used through `g cz` to create consistent commit messages with type, scope, summary, and optional details.
- The `hist` and `llog` aliases format commit logs so they are easier to read, and `df` combines `hist`, `peco`, `awk`, and `git diff` to inspect an arbitrary commit from history.
- `tig` is used as a TUI for selecting commits and viewing diffs with vim-like keybindings.
- `ps` and `pl` push and pull against the remote branch with the same name as the current local branch.
- `open` uses `hub browse` to open the GitHub repository page from the terminal.
- `vim-fugitive` is used to check diffs, blame lines, and open related GitHub pages directly from Vim.
- The workflow is presented as useful for a solo developer, while the author notes that some parts may also help in team work.
