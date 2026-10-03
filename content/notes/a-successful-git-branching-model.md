---
title: "A successful Git branching model"
date: '2017-06-12T11:26:11-03:00'
category: webclip
summary: 'The post presents a Git workflow built around two long-lived branches, master and develop, plus temporary feature, release, and hotfix branches to manage parallel work and production releases.'
tags: ["git", "branching-model", "release-management"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "A successful Git branching model"
    url: "http://nvie.com/posts/a-successful-git-branching-model/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2017-06/nvie-com--a-successful-git-branching-model.md"
    kind: repo
---

The post describes a development model built around Git, with a central origin repo used by developers who may also pull from each other when working in subteams. It argues that branching and merging should be part of daily work because Git makes them cheap and simple.

## Reading notes

- The model uses two long-lived main branches: master for production-ready code and develop for the latest integrated changes for the next release.
- Supporting branches are temporary and serve feature work, release preparation, and urgent production fixes.
- Feature branches branch off develop, merge back into develop, and may be discarded if the experiment is not kept.
- Using --no-ff on feature merges preserves the history of the feature branch and makes it easier to identify or revert the whole feature later.
- Release branches branch off develop when the code is ready for a new production release, allow final bug fixes and metadata changes, and then merge back into develop and master.
- A release branch is named with the target version, and the version number is bumped when the branch is created.
- Hotfix branches branch off master to fix an urgent production problem while develop can keep moving.
- Hotfix branches merge back into master and develop, except that if a release branch exists, the hotfix goes into that release branch first.
- Each merge into master is treated as a new production release and tagged with a release number.
- The post says the model gives the team a shared mental picture of branching and releasing, and it provides a PDF of the diagram for reference.
