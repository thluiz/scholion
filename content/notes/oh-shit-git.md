---
title: "Oh shit, git!"
date: '2016-09-11T16:13:48-03:00'
category: webclip
summary: 'The page collects plain-English fixes for common Git messes, including reflog recovery, amending commits, moving commits to the right branch, checking staged diffs, and starting over by recloning.'
tags: ["git", "version-control", "reflog", "debugging"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Oh, shit, git!"
    url: "http://ohshitgit.com/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-09/ohshitgit-com--oh-shit-git.md"
    kind: repo
---

Git is hard because it is easy to make mistakes and hard to find the right fix when you are already stuck. The page offers practical recovery steps for common bad situations, written in plain English rather than as a complete reference or a beginner tutorial.

## Reading notes

- `git reflog` shows every Git action across branches and can be used to find the state before things broke, then `git reset HEAD@{index}` can return to it.
- `git commit --amend` lets you add a small fix to the last commit after making the change.
- `git commit --amend` also changes the message on the last commit.
- If a commit landed on `master` by mistake, create a branch from the current state, reset `master` back, and keep the commit on the new branch.
- If a commit was made on the wrong branch, you can reset softly, stash the changes, switch branches, pop the stash, and commit again on the right branch.
- `git diff --staged` shows a diff for files already added to the staging area.
- If you give up, delete the repo and clone it again.
