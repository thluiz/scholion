---
title: "Your job is to deliver code you have proven to work"
date: '2026-09-25T20:41:29+01:00'
category: webclip
summary: 'Simon Willison argues that AI-assisted development still requires proving changes work through manual testing and automated tests, with humans accountable for the result and coding agents helping only if they can verify their own output.'
tags: ["ai-assisted-development", "testing", "code-review", "coding-agents"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Your job is to deliver code you have proven to work"
    url: "https://simonwillison.net/2025/Dec/18/code-proven-to-work/?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/simonwillison-net--your-job-is-to-deliver-code-you-have-proven-to-work.md"
    kind: repo
---

The post argues that the point of software work is not just to produce code, but to deliver code that works and to show evidence that it works. Large untested pull requests shift the burden to reviewers and are presented as a poor use of other people’s time.

## Reading notes

- Manual testing is required first: the developer should see the code do the right thing, set up the right initial state, exercise the change, and show the result.
- When a change is hard to demonstrate directly, the post recommends recording a screen capture and attaching it to the pull request.
- Automated tests are the second required step, and they should fail if the implementation is reverted.
- The process for writing automated tests mirrors manual testing: prepare a known state, exercise the change, and assert the expected outcome.
- The post says manual testing should not be skipped just because automated tests exist.
- Coding agents like Claude Code and Codex CLI should also be made to prove their changes work.
- For coding agents, manual and automated tests are treated as effectively the same thing because they can run code themselves.
- The human’s role is accountability: a person can be held responsible, while a computer cannot.
- A valuable pull request includes evidence that the change works as intended.
