---
title: "What Makes a Good Check-in?"
date: '2014-07-19T02:39:15-03:00'
category: webclip
summary: 'The article argues that a good check-in should have one intent, a tight scope, a clear description, build and test consistency, completeness, review, traceability, and reversibility.'
tags: ["version-control", "code-review", "software-development"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "What Makes a Good Check-in? | Dr Dobb's"
    url: "http://www.drdobbs.com/architecture-and-design/what-makes-a-good-check-in/240168601"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-07/drdobbs-com--what-makes-a-good-check-in.md"
    kind: repo
---

A good check-in is presented as the basic unit of work in a version-control system. It should move a project from one buildable and tested state to the next, preserve history, and include enough information for review, debugging, and later backout.

## Reading notes

- A check-in should have one purpose, not serve as a backup for unrelated local changes.
- Small scope makes changes easier to review, verify, undo, and move to another branch.
- The description should explain the intent and scope, with a short first line that gives an overview.
- A good check-in keeps the project buildable and tested, and includes tests with the change.
- It should also include all changes needed to build, test, and update related documentation.
- Pre-check-in review helps catch mistakes, enforce standards, and check for side effects before committing to the shared repository.
- Traceability matters in regulated settings, where authorship, date, authorization, and issue links may be required.
- Reversibility is important because later testing can still expose unwanted side effects.
- The article recommends check-ins that are small, well described, and complete enough to make review and maintenance easier.
