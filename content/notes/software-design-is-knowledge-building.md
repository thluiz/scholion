---
title: "Software Design is Knowledge Building"
date: '2026-09-25T18:33:59+01:00'
category: webclip
summary: 'The article argues that software design is about building a shared theory of the system. When the original designer leaves, the team loses the mental model needed to modify the code safely.'
tags: ["software-design", "knowledge-building", "legacy-software", "maintenance"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Software Design is Knowledge Building"
    url: "https://olano.dev/blog/software-design-is-knowledge-building/?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/olano-dev--software-design-is-knowledge-building.md"
    kind: repo
---

The article uses the story of `SVC` to show how a system can work fine at first and still become hard to change after the original engineer leaves. The code preserves what the system does, but not why it was built that way, so new teams have to reverse engineer the model from incomplete clues.

It connects this to Parnas and Naur: software ages when changes are made by people who do not understand the original design concept, and programming is better understood as building the knowledge needed to explain, justify, and adapt the system. From that view, design succeeds when it helps future teams rebuild the system’s mental model.

## Reading notes

- `SVC` was built in-house to replace `SaaS`, delivered on time by X10, and then handed to `TEAM` after X10 left.
- Once business needs changed, `TEAM` could not make small changes without getting stuck in bugs and outages.
- The code showed the what and the how, but not the why, so the team had to guess, reverse engineer, and extrapolate.
- The article uses David Parnas to argue that changes made without understanding the original design degrade the structure of the program.
- It uses Peter Naur to frame programming as theory building, where the theory is the knowledge needed to explain and modify the program.
- In this view, the main product of software design is the mental model that links the domain and the system.
- Software design is also described in terms of reducing ambiguity, obscurity, unknown unknowns, and cognitive load.
- When X10 left, the program was still running but, in Naur’s terms, it was dead because the team that held its theory was gone.
- The author argues that future revival depends on code style, structure, comments, docstrings, READMEs, pull requests, commit messages, Jira tickets, and Confluence pages.
- The closing claim is that software design should aim at organizational knowledge building.
