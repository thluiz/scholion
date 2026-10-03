---
title: "Here are all the Git commands I used last week, and what they do."
date: '2017-06-26T09:30:01-03:00'
category: webclip
summary: 'The page lists common Git commands for initializing, cloning, branching, merging, pulling, inspecting changes, and reviewing history, then adds cautions about force pushes, rebasing, and commit message cleanup.'
tags: ["git", "version-control", "branches", "commit-history"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Here are all the Git commands I used last week, and what they do."
    url: "https://medium.freecodecamp.com/git-cheat-sheet-and-best-practices-c6ce5321f52#.7j376qy8l"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2017-06/medium-freecodecamp-com--git-commands-used-last-week-and-what-they-do.md"
    kind: repo
---

The page groups the Git commands it uses most often into routine work and more advanced cleanup. It explains how to initialize a repository, connect it to a remote named origin, clone a repo, create and switch branches, merge work back into master, pull updates, and inspect status, diffs, and logs.

It also covers history editing and maintenance. It shows how to check out an older commit by hash, warns that force pushing overwrites history, describes interactive rebase as a way to combine commits, and recommends consistent commit messages and amend for renaming the latest commit. It adds that rebasing and squashing are best avoided on shared code.

## Reading notes

- `git init` starts Git in a repository, and no other Git commands can run there before initialization.
- `git remote -v` shows the URL of the remote repository.
- `git remote add origin <url>` connects a local repo to a GitHub repo, and `git remote set-url origin <url>` changes that remote.
- `git clone <url>` copies a repository, but pushing later depends on whether the remote origin points to an account you can write to.
- `git branch`, `git branch <name>`, `git checkout <name>`, and `git checkout -b <name>` list, create, switch, or create-and-switch branches.
- `git merge <branch>` brings one branch into another after checking out the target branch.
- `git pull origin <branch>` brings the newest remote changes into the local branch.
- `git status` shows changed and tracked files, and `git diff --stat` shows how many lines changed.
- `git log` shows commit history and the hashes attached to commits.
- Checking out an old commit by hash detaches the app from the current version.
- `git push -f origin master` force pushes, which overwrites history and is described as dangerous.
- `git rebase -i HEAD~4` can combine several local commits into one by changing `pick` to `fixup`.
- `git commit --amend` changes the latest commit message.
- The page recommends a consistent commit message pattern and notes that rebasing and squashing should be avoided on shared work.
