---
title: "10 Refactorings to Boost your Clean Code Skills"
date: '2023-01-02T23:45:40+00:00'
category: webclip
summary: 'The article argues that clean code grows from small refactorings. It groups common changes into extract and move operations, then shows how each one helps make code clearer, safer to change, and easier to read.'
tags: ["refactoring", "clean-code", "javascript", "typescript"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "10 Refactorings to Boost your Clean Code Skills - ITNEXT"
    url: "https://itnext.io/10-refactorings-to-boost-your-clean-code-skills-3a1e142d63f3"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2023-01/itnext-io--10-refactorings-to-boost-your-clean-code-skills.md"
    kind: repo
---

The article presents refactoring as a gradual way to improve code: small changes make complicated code easier to understand, and repeated small steps can reveal better structure. It frames the main tools as ways to extract pieces, move them, rename them, or update signatures so the code matches what it does.

## Reading notes

- Extract Variable when an expression is too long or needs a concept with a name.
- Extract Function when a function grows too large or holds too many responsibilities.
- Extract Parameter when a value should be passed in instead of coming from internal state.
- Extract Type Definition when a props list becomes hard to read or needs reuse in TypeScript.
- Slide Statements to group related statements and make the file read more smoothly.
- Change Function Declaration when behavior changes and the name no longer matches what the function does.
- Change Variable when a placeholder name can be replaced by a clearer one after the code becomes more explicit.
- Move the Fields / Constants when moving code to another file makes the current file shorter and easier to read.
- Inline Variable when an extracted variable is no longer useful and the reverse change is better.
- Change Signature when parameters need to be reordered, added, removed, or retagged.
- Use IDE shortcuts to find available refactorings or search for actions when the right command is unclear.
- The summary says these refactorings are the most commonly used ones to master for restructuring complicated code.
