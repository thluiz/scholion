---
title: "Undoing changes in Git"
date: '2015-01-28T10:43:41-03:00'
category: note
summary: "Hand-drawn flowchart that tells which Git command undoes a change, depending on whether it was committed, is in the staging index, or is on a shared branch."
tags: ["www-gitforteams-com"]
has_commentary: false
sources:
  - title: "Undoing changes in Git"
    author: "www.gitforteams.com"
    kind: web
---

Hand-drawn flowchart from www.gitforteams.com for choosing the Git command that undoes a change.

![Black-and-white hand-drawn flowchart with ellipses, decision diamonds, curved arrows and command boxes. Top left, the title "Undoing Changes in Git" and "www.gitforteams.com". Start: "You want to remove changes to your file(s)." → "Has the change been committed?". "No" branch: "Is the change in the staging index?"; "No" → "checkout -- <filename>"; "Yes" → "Are there changed files you want to preserve in the working directory?"; "No" → "reset --hard"; "Yes" → "This is a multi-step sequence." → "first remove the file from staging index" → "reset <filename>" → "then" → "checkout -- <filename>". "Yes" branch: "Do you want to keep a reference to the committed change in your log?"; "Yes" → "revert"; "No" → "Is this a shared branch?"; "Yes" → "It is not appropriate to re-write history." → "revert"; "No" → "Is the change in the most recent commit(s)?"; "No" → "rebase --interactive"; "Yes" → "Are there changed files you want to preserve in the working directory?"; "No" → "reset --hard <commit_id>"; "Yes" → "reset <commit_id>".](undoing-changes-in-git.png)
