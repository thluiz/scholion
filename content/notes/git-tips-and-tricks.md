---
title: "Git Tips & Tricks"
date: '2016-12-19T09:42:19-03:00'
category: webclip
summary: 'The post gathers Git commands, config tweaks, aliases, and plugins that GitLab uses to make daily work faster, from built-in help to branch cleanup and merge request checkout.'
tags: ["git", "git-config", "aliases", "gitlab"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Git Tips & Tricks"
    url: "https://about.gitlab.com/2016/12/08/git-tips-and-tricks/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-12/about-gitlab-com--git-tips-and-tricks.md"
    kind: repo
---

The page collects Git tips GitLab uses in everyday work. It points readers to built-in help, prompt status, autocompletion, plugins, `.gitconfig` options, aliases, and command-line shortcuts that make common tasks faster.

## Reading notes

- Git includes built-in help for commands, guides, and tutorials, so users do not need to rely only on external sites.
- A prompt script can show repository status in the terminal, and completion scripts can autocomplete Git commands.
- Plugins such as `git-extras` and `git-open` add commands for repository information and opening the hosted project in a browser.
- `.gitconfig` can set a global ignore file, prune removed remote branches on fetch or pull, enable autosquash, show submodule summaries, and change the editor or diff and merge tools.
- Aliases can shorten long commands, including pretty log graphs and a command to fetch and check out a merge request locally.
- Command-line tips include using `@` for `HEAD`, switching back to the previous branch with `-`, deleting merged local branches, pruning remote-tracking branches, and creating a new branch from a base branch in one step.
