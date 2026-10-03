---
title: "Pull Requests: A Primer"
date: '2020-02-19T09:45:45-03:00'
category: webclip
summary: 'The article explains how to write effective pull requests by following contribution rules, keeping each PR to one scope, using clear commits and messages, and writing a concise title and body with enough context for reviewers.'
tags: ["pull-requests", "git", "open-source", "code-review"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Pull Requests: A Primer - DEV Community 👩‍💻👨‍💻"
    url: "https://dev.to/wes/opening-a-pr-a-primer-4kgc"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-02/dev-to--pull-requests-a-primer.md"
    kind: repo
---

The article says pull requests are the main way to add code to open source projects and many closed source ones. It recommends reading the project’s contribution rules first, keeping each PR focused on one scope of work, and using commits to separate changes when a PR is larger.

It also says commit messages should follow the project’s guidelines, usually staying short and in the present tense, and that the pull request title should state the main intent clearly. The body should explain the changes and reasoning, give enough context for reviewers, and can include steps taken, alternatives, and external links when relevant.

## Reading notes

- Pull requests are the main path for adding code to open source projects and many closed source ones.
- Read CONTRIBUTING.md, or the project’s root or docs folder, to learn the expected code style, merge strategy, and commit message format.
- Keep each pull request limited to one clear goal.
- Split larger changes into smaller commits so readers can follow each step separately.
- Follow the project’s rules for commit messages; they are often short, present tense, and without punctuation.
- Write the pull request title to express the main intent of the change.
- Use the pull request body to explain the change, the reasoning behind it, and the context reviewers need.
- The body can also include steps taken, alternatives considered, and linked external resources.
- Visual changes can benefit from screenshots or video.
- Reviewers need enough context to understand the change without assuming prior knowledge.
