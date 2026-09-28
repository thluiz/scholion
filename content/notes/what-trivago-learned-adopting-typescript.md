---
title: "What Trivago Learned Adopting TypeScript"
date: '2022-08-04T09:06:02-03:00'
category: webclip
summary: 'Trivago says the TypeScript migration slowed coding at first, but improved discipline and confidence. The team leaned on GraphQL schema types and warned that loose type casting can hide runtime bugs.'
tags: ["typescript", "graphql", "trivago", "type-safety"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "What Trivago Learned Adopting TypeScript – The New Stack"
    url: "https://thenewstack.io/what-trivago-learned-adopting-typescript/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-08/thenewstack-io--what-trivago-learned-adopting-typescript.md"
    kind: repo
---

Trivago’s migration from PHP/JavaScript to TypeScript covered its core website and more than 50 domains. The team says the switch required more thought about data flow and type definitions, but it also made code easier to reason about and safer to maintain.

## Reading notes

- The migration ended with 200,000 lines in 2,600 .ts files and 115,000 lines in 1,500 .tsx files.
- The team had limited prior TypeScript experience and found the learning curve slowed day-to-day coding.
- Bartel says the extra time spent defining types improves discipline and confidence in the code.
- Trivago auto-generated TypeScript types from existing GraphQL schemas with `apollo client:codegen`.
- The generated types were kept separate from hand-written code to avoid file conflicts.
- Bartel recommends connected types whenever possible instead of type casting unrelated hand-written types.
- He warns that manual casting can hide missing fields and null or non-null mismatches.
- Those mistakes can produce runtime errors in production and are hard to catch with testing.
- Bartel recommends TypeScript for both new projects and existing ones because gradual migration is possible.
