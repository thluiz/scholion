---
title: "Using git hooks to improve your day-to-day workflow"
date: '2018-02-26T10:24:00-03:00'
category: webclip
summary: 'The post shows how client-side git hooks can block bad commits, enforce linting, warn on WIP messages, and confirm pushes to protected branches before code leaves a developer’s machine.'
tags: ["git-hooks", "workflow", "linting", "continuous-integration"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Using git hooks to improve your day-to-day workflow"
    url: "https://dev.to/fedekau/using-git-hooks-to-improve-your-day-to-day-workflow-4nl5"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2018-02/dev-to--using-git-hooks-to-improve-your-day-to-day-workflow.md"
    kind: repo
---

The post explains how client-side git hooks can catch problems before they leave a developer’s machine. It focuses on three uses: running lint checks before commit, reacting to commit messages that look like work in progress, and asking for confirmation before pushing to a protected branch.

## Reading notes

- Git hooks are custom scripts triggered by Git actions, and client-side hooks run on operations like committing and pushing.
- The post focuses on client-side hooks to execute custom scripts for linting, tests, and commit formatting.
- `pre-commit` can inspect the snapshot about to be committed and abort the commit if checks fail.
- The example uses RuboCop to detect code issues and stop the commit when problems are found.
- `commit-msg` receives the commit message file and can validate or modify the message before Git accepts the commit.
- In the example, the hook looks for “WIP” or “work in progress” and, if the developer declines to run CI, appends `[skip ci]` to the commit message.
- `pre-push` runs during `git push` and can abort the push with a non-zero exit code.
- The example asks for confirmation before pushing to `master` and blocks the push if the developer does not confirm.
- Hooks inside `.git/hooks` are local to the repository copy, so they are not automatically shared with other developers.
- Using `git config core.hooksPath <path-to-hooks-folder>` lets a project store hooks under version control and make them available on install.
- The conclusion says these hooks can prevent failing or unnecessary CI runs and avoid unwanted pushes to protected branches.
