---
title: "Git helpers - Simplify your git workflow"
date: '2017-08-15T14:18:47-03:00'
category: webclip
summary: 'The page shares Git aliases the author uses to reduce repetitive typing, speed up branch and fork maintenance, and simplify common tasks like committing, pulling, rebasing, pushing, and status checks.'
tags: ["git", "command-aliases", "workflow", "shell"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Git helpers - Simplify your git workflow"
    url: "https://dev.to/gyandeeps/git-helpers---simplify-your-git-workflow"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2017-08/dev-to--git-helpers-simplify-your-git-workflow.md"
    kind: repo
---

The page presents a set of Git aliases the author uses every day to avoid repeating the same commands. It groups them around common tasks such as starting work on an issue, updating a branch, cleaning up finished work, pushing changes, syncing a fork, and checking commit history or branch status.

## Reading notes

- The aliases were created because the author got tired of typing the same Git commands repeatedly.
- Some of the alias definitions were inherited from Nicholas C. Zakas’s gist.
- `ws 34` updates `master` from remote and creates a new branch named `issue34`.
- `wd 34` deletes a finished branch from both local and remote Git.
- `update` rebases a branch on the latest `master` when changes are already committed.
- `updateD` stashes uncommitted changes, updates from `master`, and reapplies the stash.
- `rebase 4` squashes commits by rebasing the last four commits from `HEAD`; the default is two.
- `push` sends branch changes to remote, but not to `master`.
- `fpush` force-pushes with `--force-with-lease` and also avoids pushing to `master`.
- `pull` pulls from upstream and merges into the current branch with `--rebase --prune`.
- `uf` updates a fork by syncing upstream `master` into local `master` and pushing it to origin.
- `c "<message>"` creates a quick commit with the given message and uses `-a`.
- `log` shows commits in one-line format with message, date, author, and other info.
- `s` shows the current branch status.
- The setup instructions say to add the gist content to `.bashrc`, reopen Bash, and run `alias` to see the defined commands.
