---
title: "TypeScript Advanced Types — Nullable Types and Type Aliases"
date: '2020-02-22T12:11:43+00:00'
category: webclip
summary: 'The article explains how TypeScript’s strictNullChecks blocks null and undefined on non-nullable members, and how nullable types use a question mark to allow them. It also introduces type aliases.'
tags: ["typescript", "nullable-types", "type-aliases"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "TypeScript Advanced Types — Nullable Types and Type Aliases | by John Au-Yeung | Level Up Coding"
    url: "https://levelup.gitconnected.com/typescript-advanced-types-nullable-types-and-type-aliases-847f03b08fae"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/levelup-gitconnected-com--typescript-advanced-types-nullable-types-and-type-aliases.md"
    kind: repo
---

TypeScript supports nullable types so properties can accept undefined when strictNullChecks is enabled. Without the nullable operator, members cannot be assigned null or undefined under that flag.

## Reading notes

- With strictNullChecks on, TypeScript rejects null or undefined on type members that do not use the nullable operator.
- A question mark after a member name marks it as nullable.
- The example interface Person sets age to null and produces a type error because age is declared as number.
- The article says TypeScript also has other advanced types, including intersection types, union types, type guards, nullable types, and type aliases.
- This piece focuses on nullable types and type aliases.
