---
title: "In defense of TypeScript"
date: '2020-09-21T15:09:33-03:00'
category: webclip
summary: 'The article argues that TypeScript has practical value in team communication, refactoring, bug prevention, and scaling, and addresses common objections about difficulty, speed, readability, and Microsoft.'
tags: ["typescript", "javascript-ecosystem", "static-typing"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "In defense of TypeScript - DEV"
    url: "https://dev.to/stojakovic99/in-defense-of-typescript-13ci"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-09/dev-to--in-defense-of-typescript.md"
    kind: repo
---

The article argues that TypeScript matters because JavaScript has expanded into web, desktop, server-side, and IoT work, and because common objections about TypeScript often miss how it helps with collaboration, refactoring, and catching mistakes earlier. It also says that gradual typing makes adoption possible while keeping existing JavaScript code in place.

## Reading notes

- TypeScript is presented as useful even for people who could avoid it, because it helps teams communicate, makes refactoring safer, reduces simple type-related mistakes, and supports larger projects.
- The article says TypeScript is not hard for people who already know JavaScript well, and that gradual typing lets projects migrate by using `any` where types are still unclear.
- It explains that `strict` mode exposes implicit `any` values, which helps avoid leaving untyped parameters scattered through a growing codebase.
- It shows that explicit return and parameter types let TypeScript surface methods and properties while code is being written, such as when checking whether a user has badges.
- The article argues that type annotations slow initial writing but make debugging, navigation, bug detection, and self-documentation easier as projects grow.
- It says TypeScript is not worth forcing into every project, and gives a small weather app as an example where the overhead felt unnecessary.
- It rejects the idea that TypeScript is bad because Microsoft made it, and points to C#, VS Code, and TypeScript as examples of Microsoft products it sees as valuable.
- It says complaints that TypeScript is hard to read often reflect the complexity of the project rather than the language itself, especially when types become long.
- It closes by framing the piece as personal experience rather than empirical proof and says the goal is to question misconceptions about TypeScript, not attack JavaScript.
