---
title: "Merge vs rebase"
date: '2021-06-22T10:35:29-03:00'
category: webclip
summary: 'The article compares merge and rebase in Git, showing merge as a way to join histories and preserve conflict-resolution history, while rebase rewrites history to keep branches linear and clean.'
tags: ["git", "merge", "rebase"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Merge vs rebase - DEV Community"
    url: "https://dev.to/emyller/merge-vs-rebase-63e"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2021-06/dev-to--merge-vs-rebase.md"
    kind: repo
---

Merge and rebase are both useful Git tools, but they serve different situations. Merge is presented as the option for joining histories while keeping the record of how branches converged. Rebase is presented as the option for cleaning up and rewriting history, especially on branches that are still not known to the remote.

## Reading notes

- Merge is described as joining two or more development histories and is used to update main with a feature branch or update a feature branch with the latest work from main.
- Merge commits preserve conflict resolution at the merge level, so once conflicts are resolved they are not revisited in that merge.
- A fast-forward merge can keep history linear, but it hides the fact that a merge happened because no merge commit is created.
- Rebase re-applies commits on top of another base tip and is used to update a topic branch by resetting it to main and replaying its history.
- Rebase rewrites history and can be used to move commits in history or fix, squash, or rename previous commits.
- Rebasing usually requires resolving conflicts at the commit level, and the same conflicts may appear again if the base branch changes.
- Rebase should not be used to rewrite commits that other people have already pushed, because it can discard or rewrite their work and may require a force-push.
- `git pull --rebase` helps avoid an unnecessary merge commit when pulling a more recent remote version onto a branch that was rebased or force-pushed.
- The choice between merge and rebase depends on the goal and on the team’s agreed workflow.
- Merge is best for joining histories with visible context, while rebase is best for cleanup and branch maintenance before a branch is shared.
