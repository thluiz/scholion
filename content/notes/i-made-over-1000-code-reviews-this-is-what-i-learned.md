---
title: "I made over 1,000 code reviews - this is what I learned"
date: '2020-07-05T14:10:38+00:00'
category: webclip
summary: 'The author says code reviews go better when each pull request solves one thing, checks are automated in CI, reviewers talk with the author, feedback stays considerate, and local runs are required.'
tags: ["code-reviews", "pull-requests", "ci", "teamwork"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "I made over 1,000 code reviews - this is what I learned"
    url: "https://dev.to/mjuraj/i-made-over-1-000-code-reviews-this-is-what-i-learned-4e9e"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--i-made-over-1000-code-reviews-this-is-what-i-learned.md"
    kind: repo
---

The article argues that code review works better when pull requests stay focused, automated checks handle routine verification, and reviewers keep the conversation constructive. It also says some reviews are faster and clearer when the author sits with the reviewer.

## Reading notes

- A pull request should solve one problem, because focused changes are easier to review and large requests take much longer.
- Bigger pull requests tend to contain more mistakes, take longer to approve, and can wait long enough to create merge conflicts.
- Common side changes like renamings and generalizations can distract from the main review.
- Formatting, documentation, tests, linting, type checking, and similar checks should be moved into CI when possible.
- Automated tests help confirm that the change did not break existing behavior.
- Automated formatting removes arguments about style details and makes review less noisy.
- A lint checker is especially important in languages like Python, where formatting can affect logic.
- Reviewing code with the author can make iteration faster and can help explain the reasoning behind the change.
- Sitting with the author can also strengthen communication and connection within the team.
- Review comments should be considerate, and open-ended questions can be better than direct criticism.
- The author recommends asking how to reduce complexity instead of just pointing out a mistake.
- A checklist item for running the code locally helps prevent reviewers from finding basic failures in small pull requests.
- The post includes a pull request template with checklist items for local runs, tests, type hints, changelog updates, and deployment notes.
