---
title: "8 Small git tips"
date: '2015-04-01T10:59:05-03:00'
category: webclip
summary: 'The post collects eight practical Git tips: partial staging, interactive rebase, stashing, a global ignore file, whitespace warnings, autosetuprebase, clearer logs, and amending commit messages.'
tags: ["git", "version-control", "command-line", "productivity"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "8 Small git tips · Rodrigo Flores's Corner"
    url: "http://blog.rlmflores.me/git/2015/03/31/8-small-git-tips/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-04/blog-rlmflores-me--8-small-git-tips.md"
    kind: repo
---

The post gathers eight short Git tips the author uses almost every day. It focuses on ways to stage only part of a file, reorganize commit history, keep temporary changes out of the way, reduce noise from local generated files, and inspect history more clearly.

## Reading notes

- `git add -p` lets you interactively choose which chunks of a file go into a commit, and `git checkout -p` does the same for changes you want to revert.
- `git diff --cached` shows what has been selected after partial staging.
- `git rebase -i <commit>` lets you pick, squash, reword, edit, or remove commits, but it changes history and should not be used on shared or already pushed branches.
- `git stash` stores work in progress when you need to switch contexts, and the author prefers to keep the stash empty by checking it with `git stash show -p`, then popping or clearing it.
- A global ignore file can be configured with `git config --global core.excludesfile=/Users/flores/.gitignore` for files generated locally, such as editor backup files or `.DS_Store`.
- `apply.whitespace=warn` makes Git warn about trailing whitespace when staging chunks with `git add -p`.
- `branch.autosetuprebase=always` makes pulls try to reapply local commits instead of creating a merge commit.
- `git log --graph --decorate --pretty=oneline --abbrev-commit` gives a more useful view of branch history and commit points.
- `git commit --amend` rewrites the last commit message and can include newly staged changes, but it also changes history and may require a force push.
