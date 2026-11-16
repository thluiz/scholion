---
title: "Technical ergonomics for the efficient developer"
date: '2020-07-05T14:10:31+00:00'
category: webclip
summary: 'The article argues that developers can reduce mental strain by using technical ergonomics tools such as stronger syntax highlighting, Git hooks, and static type systems.'
tags: ["developer-tools", "git-hooks", "static-types", "syntax-highlighting"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Technical ergonomics for the efficient developer"
    url: "https://dev.to/victoria/technical-ergonomics-for-the-efficient-developer-47i3"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--technical-ergonomics-for-the-efficient-developer.md"
    kind: repo
---

The article frames technical ergonomics as a way to save brainpower, not just physical comfort. It says programming is mentally demanding, but tools can make the hard parts of working with computers easier and reduce day-to-day stress.

## Reading notes

- Stronger syntax highlighting can make it easier to spot the current line, code block boundaries, matching brackets, and TODO or FIXME comments.
- The author lists Visual Studio Code extensions for bracket pair coloring, TODO highlighting, indented block highlighting, and line highlighting.
- The pictured Visual Studio Code theme is Kabukichō, which the author says they made.
- Git hooks can run automatically at specific points in the workflow and can handle linting, formatting, and local tests before code is pushed.
- The pre-commit framework is presented as a way to share hook configuration across a repository.
- The author shows a Python-focused `.pre-commit-config.yaml` using hooks such as detect-aws-credentials, end-of-file-fixer, trailing-whitespace, black, blacken-docs, mypy, and local isort and black hooks.
- The article recommends using a static type system for Python and JavaScript to improve thinking about code and catch type errors before running code.
- For Python, the author prefers mypy and notes that it can be used with pre-commit and Visual Studio Code.
- For JavaScript, the author prefers TypeScript and notes that it works from the command line and integrates with Visual Studio Code.
- The closing point compares ignoring these tools to unnecessary inversion and asks why work without them if they are available.
