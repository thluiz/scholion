---
title: "Turbocharged JavaScript refactoring with codemods"
date: '2016-07-28T15:00:41-03:00'
category: webclip
summary: 'Airbnb describes codemods as a way to automate large JavaScript refactors, reduce manual cleanup, and bring old code closer to current style and lint rules with less effort.'
tags: ["codemods", "javascript-refactoring", "eslint", "airbnb"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Turbocharged JavaScript refactoring with codemods — Airbnb Engineering & Data Science — Medium"
    url: "https://medium.com/airbnb-engineering/turbocharged-javascript-refactoring-with-codemods-b0cae8b326b9#.gn2x6vaqf"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-07/medium-com--turbocharged-javascript-refactoring-with-codemods.md"
    kind: repo
---

The post argues that codemods help teams handle large-scale JavaScript cleanup without doing every change by hand. Airbnb uses them to bring older code toward its style guide, improve lint coverage, and speed up refactoring work that would otherwise be tedious and slow.

## Reading notes

- Codemods are presented as tools for partially automatable large refactors, built on AST transformations and written in JavaScript.
- They help apply style and syntax updates across many files while matching local coding style.
- The author links codemods to faster feedback loops, less communication overhead, and more time for meaningful work.
- Running a codemod still needs review and manual tweaking, so `git diff`, `git add --patch`, and `git checkout --patch` are useful afterward.
- Small commits and small pull requests make review and merge conflict handling easier.
- Splitting changes by file type or path can make large diffs easier to review.
- The post lists lighter codemods such as arrow functions, `var` to `const` or `let`, object shorthand, unchained variable declarations, and unquoted properties.
- It also lists heavier codemods such as converting `React.createClass` to ES6 classes, reordering React component methods, and changing string concatenation to template literals.
- The author says Airbnb modified 40,000 lines through codemods with little effort.
- The post ends by saying codemods can also support breaking API changes and are worth investing in.
