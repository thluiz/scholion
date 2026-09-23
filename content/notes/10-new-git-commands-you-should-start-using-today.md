---
title: "10 new Git commands you should start using today"
date: "2026-09-23T17:39:29+01:00"
category: webclip
has_commentary: false
summary: "A round-up of ten Git commands added since version 2.23 that replace overloaded old ones, automate repo maintenance, and make merges, rebases and monorepos easier to handle."
tags:
  - git
  - version-control
  - developer-tools
  - cli
sources:
  - title: "10 new Git commands you should start using today · Appwrite"
    url: "https://appwrite.io/blog/post/10-git-commands-you-should-start-using"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/appwrite-io--10-new-git-commands-you-should-start-using-today.md"
    kind: repo
---

Ebenezer Don rounds up ten Git commands added since version 2.23, aimed at developers who know the basics but haven't tracked what Git shipped in the years after. The commands fall into four groups: safer replacements for `checkout`'s overloaded behavior, tools that automate repository maintenance, commands for inspecting merges and rewritten history, and features for working across branches without disrupting the current one.

## Fichamento

- `git switch` (Git 2.23) separates branch switching from `git checkout`, which used to also restore files and check out commits, so changing branches carries less risk of touching files by accident.
- `git restore` (Git 2.23) isolates undoing changes to files from branch operations that used to live inside `checkout` and `reset`, both of which could alter branch state if used carelessly.
- `git maintenance` (Git 2.29) automates garbage collection, packfile repacking and commit-graph updates that previously required running `git gc` and `git repack` by hand.
- `git sparse-checkout` (Git 2.25) lets a working directory include only the directories a developer needs, useful for large monorepos where a full clone is wasteful.
- `git log --remerge-diff` (Git 2.35) replays a merge's recorded strategy and shows the exact changes it introduced, which helps when reviewing how a conflict was resolved.
- `git blame --ignore-rev` (Git 2.23), backed by a persistent `.git-blame-ignore-revs` file, excludes a bulk formatting commit from blame so authorship stays meaningful.
- `git range-diff` compares two commit ranges and shows how a rebased or rewritten series of commits diverged from the original.
- `git worktree` creates additional working directories tied to the same repository, so multiple branches can be worked on at once without switching or stashing.
- `git rebase --update-refs` (Git 2.38) keeps branch pointers and tags referencing rewritten commits in sync automatically after a rebase.
- `git commit --fixup`, paired with `git rebase -i --autosquash` (fixup dates back to Git 1.7.4), marks a commit to be squashed automatically into an earlier target during an interactive rebase, keeping history clean without manual reordering.
