---
title: "3 Git Commands I Use Every Day"
date: '2017-03-06T09:37:02-03:00'
category: webclip
summary: 'The author favors `git add -p` for reviewing changes before staging, `git commit --amend --no-edit` for keeping sequential work in one commit, and `git reset --hard` for discarding unwanted changes.'
tags: ["git", "git-workflow", "git-commands"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "3 Git Commands I Use Every Day"
    url: "https://dev.to/gonedark/3-git-commands-i-use-every-day"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2017-03/dev-to--3-git-commands-i-use-every-day.md"
    kind: repo
---

The post describes three Git commands the author uses in everyday work. `git add -p` helps review changes interactively before staging, `git commit --amend --no-edit` keeps sequential work attached to the previous commit without changing the message, and `git reset --hard` removes changes that were not meant to be kept.

## Reading notes

- `git add -p` lets the author inspect each change and decide whether to stage it.
- The command is slower than `git add .`, but it serves as a final review and often catches comments or debug statements that should stay out of a commit.
- `git commit --amend --no-edit` is used for small incremental commits during longer stretches of work.
- The author prefers that approach to rebasing when work is being done sequentially.
- Keeping a clean state makes it easier to run other Git commands and track changes over time.
- `git reset --hard` is used to discard changes that were not staged or changes from exploratory work that should not be committed.
- The author says the command should be used carefully, but argues that `git reflog` and `git fsck` make Git less frightening.
