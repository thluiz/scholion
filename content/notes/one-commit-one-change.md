---
title: "One Commit. One Change."
date: '2016-05-19T14:06:56-03:00'
category: webclip
summary: 'The post argues that commits should be atomic: one change only, so they can be reverted cleanly, keep builds consistent, and make history easier to trace.'
tags: ["git", "atomic-commit", "version-control", "software-engineering"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "One Commit. One Change. — Medium"
    url: "https://medium.com/@fagnerbrack/one-commit-one-change-3d10b10cebbf?ct=t(BrazilJS_Weekly_468_9_2013)"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-05/medium-com--one-commit-one-change.md"
    kind: repo
---

The post links Event Sourcing and Git to argue that history works best when each change is isolated. A commit should represent one change only, so it can be replayed, reverted, and understood later without relying on the original author.

## Reading notes

- Git is presented as a system where replaying committed changes in order reproduces the current state.
- The author connects that idea to Event Sourcing, where state comes from a sequence of stored events.
- A commit should reflect one change only, also called an atomic change.
- An atomic change is indivisible: it either succeeds fully or fails fully.
- In Git, an atomic change should be revertible without side effects in other parts of the system.
- A commit should not break the normal build flow and should work against a specific required state of the codebase.
- This matters especially on the master branch, whose history should remain consistent and immutable.
- Atomicity helps reset the application to earlier states and use tools like git bisect to find bugs in history.
- Traceability matters because future readers should be able to understand the source and purpose of a change from the commit history.
- If a commit does more than one thing, it becomes harder to locate when a bug or feature was introduced and harder to revert safely.
- The article closes by saying this is a principle, not a law, and the best choice depends on the circumstances.
