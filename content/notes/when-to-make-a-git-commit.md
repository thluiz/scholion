---
title: "When to make a Git Commit"
date: '2017-03-07T21:44:56-03:00'
category: webclip
summary: 'The post says to commit when you finish a unit of work or when you have changes you may want to undo. It argues that units of work should be defined by feature, not by time or file type.'
tags: ["git", "commits", "version-control", "feature-based-work"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "When to make a Git Commit"
    url: "https://dev.to/gonedark/when-to-make-a-git-commit"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2017-03/dev-to--when-to-make-a-git-commit.md"
    kind: repo
---

The post argues for two times to make a commit: when a unit of work is complete and when a change may need to be undone later. It says each commit should contain only that set of changes, and changes you may want to revert should be kept in their own commit so they are easy to find and use with `git revert`.

It rejects defining a unit of work by time or by type of change, such as new files versus modified files, code versus HTML, or client versus API. Instead, it treats feature as the better measure because it gives more context and helps commits tell a story while still leaving room to decide the size of the unit.

## Reading notes

- Commit when a unit of work is complete.
- Commit when a change may need to be undone later.
- Keep only one set of changes in each commit.
- Put changes you may want to revert in their own commit so they are easy to find with `git revert`.
- Do not define a unit of work by time.
- Do not define a unit of work by change type, such as file type, code layer, or location.
- Define a unit of work by feature because it gives more context and helps the history tell a story.
- A feature can vary in size, so the unit still needs judgment.
