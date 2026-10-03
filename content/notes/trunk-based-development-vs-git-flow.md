---
title: "Trunk-based Development vs. Git Flow"
date: '2017-10-06T11:24:01-03:00'
category: webclip
summary: 'The article compares Git flow and trunk-based development, showing how each workflow shapes branching, review, speed, and control, and when each fits open source, junior teams, startups, or senior teams.'
tags: ["git-flow", "trunk-based-development", "version-control", "software-development"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Trunk-based Development vs. Git Flow"
    url: "https://www.toptal.com/software/trunk-based-development-git-flow"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2017-10/toptal-com--trunk-based-development-vs-git-flow.md"
    kind: repo
---

The article contrasts two ways of using Git: Git flow, with strict review and separate branches, and trunk-based development, with direct commits to a shared main branch and less process. It argues that the better choice depends on team experience, trust, project maturity, and the need for speed or control.

## Reading notes

- Version control systems track project history, make it possible to reverse changes, and help merge work from multiple people.
- Git is presented as a distributed system that made parallel work easier and helped open source grow.
- Pull requests are described as a review process where developers comment on changes before they are merged.
- Git flow uses a main development branch, feature branches, pull requests, and a release branch before publishing to users.
- Git flow is said to work well for open source projects, junior teams, and established products that need close control.
- Git flow can slow development, create long-lived branches, encourage micromanagement, and cause office politics.
- Trunk-based development keeps developers on one shared branch, with only short-lived feature branches when needed.
- Trunk-based development relies on full source code review, enforceable code style, and experienced developers.
- Trunk-based development is presented as a better fit for startups, quick iteration, and teams of senior developers.
- The article says trunk-based development is a poor fit for open source projects, junior teams, and large established products that need strict control.
- The final advice is to choose Git flow or trunk-based development according to the project, the team, and the level of trust required.
