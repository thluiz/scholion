---
title: "Code Smell 149 — Optional Chaining"
date: '2022-07-21T13:05:55-03:00'
category: webclip
summary: 'The page argues that optional chaining hides null and undefined instead of removing them, and says cleaner code should eliminate nulls and explicit undefined checks.'
tags: ["null", "optional-chaining", "undefined"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Code Smell 149 — Optional Chaining | by Maximiliano Contieri | Jul, 2022 | Level Up Coding"
    url: "https://levelup.gitconnected.com/code-smell-149-optional-chaining-b8830d7206ae"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-07/levelup-gitconnected-com--code-smell-149-optional-chaining.md"
    kind: repo
---

The page treats optional chaining as a code smell because it keeps nulls and undefined in the code path. Its position is that mature, robust code should remove nulls and avoid the need for optional access or explicit undefined checks.

## Reading notes

- Optional chaining is presented as a way to hide null under the rug rather than solve the underlying problem.
- The page says nulls and undefined should be removed, and then optionals are no longer needed.
- It groups optional chaining with other ways of dealing with nullish values, such as optionals and coalescence.
- In the sample code, `user?.credentials?.notExpired` is marked wrong because it depends on potential nulls and undefined.
- The right example uses a real user object or a polymorphic `NullUser`, with credentials always defined.
- An explicit `!== undefined` check is also labeled wrong, because explicit undefined checks are another code smell.
- The page says this is an automatic, language-feature-level smell that can be detected and removed.
- It also connects the topic to null, short circuit hacks, big bang castings, and the broader issue of nullish values.
