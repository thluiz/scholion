---
title: "Don't Amend, Fix"
date: '2017-04-11T11:15:08-03:00'
category: webclip
summary: 'The post argues that `git commit --amend` hides history and is too limited for many correction workflows, while `git commit --fixup` with `git rebase -i --autosquash` makes fixing commits easier and more flexible.'
tags: ["git", "rebase", "commit-fixup"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Don't Amend, Fix"
    url: "https://dev.to/tmr232/dont-amend-fix"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2017-04/dev-to--dont-amend-fix.md"
    kind: repo
---

The post recommends avoiding `git commit --amend` for routine fixes. It says amend hides history and breaks down when the fix belongs earlier in a branch, where `git rebase` is needed instead.

It then proposes `git commit --fixup` together with `git rebase -i --autosquash` as a lower-friction workflow. The suggested aliases are `ri`, `mri`, `fix`, and `squ`, and the author says this approach lets you keep making fixup commits until the rebase.

## Reading notes

- `git commit --amend` can hide the previous state and should stay a last resort.
- When a forgotten change belongs to an earlier commit, the workflow moves to `git rebase -i`.
- `git commit --fixup` and `git rebase -i --autosquash` remove the need to reorder commits and edit `pick` lines manually.
- The suggested aliases are `ri = rebase -i --autosquash`, `mri = rebase -i`, `fix = commit --fixup`, and `squ = commit --squash`.
- Multiple fixup commits can be stacked before rebasing, and autosquash still groups them correctly.
