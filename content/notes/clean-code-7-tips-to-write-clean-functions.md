---
title: "Clean Code: 7 tips to write clean functions"
date: '2026-09-24T23:24:13+01:00'
category: webclip
summary: 'The post argues that clean functions are small, easy to understand, well named, limited in parameters, free of nested conditionals and booleans, and preferably pure.'
tags: ["clean-code","functions","refactoring","testing"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Clean Code: 7 tips to write clean functions"
    url: "https://craftbettersoftware.com/p/clean-code-7-tips-to-write-clean?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/craftbettersoftware-com--clean-code-7-tips-to-write-clean-functions.md"
    kind: repo
---

The post says functions should be easy to understand quickly, because complex code causes errors, slows changes, and makes onboarding harder. It recommends small functions, but also says size should depend on context and judgment.

It also suggests naming functions after the business domain, using verbs, keeping team naming conventions, and using one word per concept. For structure, it prefers few parameters, guard clauses instead of nested ifs, pure functions, enums instead of booleans, and descriptive names instead of comments.

## Reading notes

- Functions should be understandable in a few seconds; when that takes longer, the text argues for refactoring.
- Complex functions increase errors, make changes harder, and slow down onboarding for new developers.
- The ideal is to make functions small and pragmatic, without turning it into dogma or filling the code with too many functions.
- Function names should reflect the domain language and clearly say what the function does.
- The text recommends using verbs, following the team’s conventions, and keeping one term for each concept.
- The ideal number of arguments is zero, and the text suggests at most three parameters, grouping related data when necessary.
- Instead of nested IFs, the text proposes inverting conditions and using guard clauses.
- Pure functions have the same result for the same input and have no side effects; this makes them more predictable, easier to test, and parallelizable.
- Booleans as parameters make the call ambiguous; the text prefers enums to make the code self-explanatory.
- When a function is not clear, the text says to prioritize good names instead of resorting to comments, which age badly and often repeat the code.
