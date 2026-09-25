---
title: "Write broken commits for better review"
date: '2026-04-17T15:51:15+01:00'
category: webclip
summary: 'The article argues that intentionally broken commits can make code review easier when they separate mechanical changes from real ones, especially under squash merges and AI-assisted development.'
tags: ["code-review", "git", "squash-merge", "ai"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Write broken commits for better review | Huon on the internet"
    url: "https://huonw.github.io/blog/2026/04/broken-commits/?utm_source=tldrnewsletter"
    kind: repo
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-04/huonw-github-io--write-broken-commits-for-better-review.md"
    kind: repo
---

The article argues that some changes are easier to review when they are split into commits that tell a clearer story, even if an intermediate commit breaks tests or does not compile. Mechanical changes such as formatting, renaming, re-indenting, and moving code are easier to verify when they are separated from the substantive change.

It recommends using broken commits as a review tool, especially with squash merges, where commits can serve as units of review while the merged result remains a single unit of persistence. The article gives examples like adding formatters, lint rules, renames, file moves, and large re-indents, and says AI-generated code makes this discipline more important because the reviewer remains accountable for what is shipped.

## Reading notes

- Commits should tell a story about a change, and that story is easier to review when mechanical edits are separated from real code changes.
- A commit can be intentionally broken if that helps keep a mechanical transformation clearly isolated.
- Squash merges let commits be units of review without needing them to be the final persisted history.
- The article lists formatters, lint rules, renames, file renames, large re-indents, and moved code chunks as cases where broken commits are useful.
- The author says the method helps when reviewing AI-assisted code because the reviewer is still accountable for what gets shipped.
- The advice depends on judgment: it should be used when it helps, but not pushed to the point of meaningless micro-commits.
