---
title: "Applying SOLID Principles in JavaScript and TypeScript Framework"
date: '2026-09-25T01:20:49+01:00'
category: webclip
summary: 'The article shows how SOLID principles apply in React and Angular with JS and TS examples, using refactors to separate responsibilities, ease extension, and reduce coupling.'
tags: ["solid","javascript","typescript","react","angular"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Applying SOLID Principles in JavaScript and TypeScript Framework"
    url: "https://dev.to/wafa_bergaoui/applying-solid-principles-in-javascript-and-typescript-framework-2d1d?context=digest"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--applying-solid-principles-in-javascript-and-typescript-frame.md"
    kind: repo
---

The article applies the SOLID principles to JavaScript and TypeScript frameworks such as React and Angular. It uses anti-patterns and refactors to show how code can be split by responsibility, extended without modifying core logic, and decoupled through abstractions.

## Reading notes

- SRP appears when components, services or classes accumulate UI, business logic, data updates and notifications; the solution presented separates these tasks into a hook, component and specific service.
- OCP is shown in validation functions and notification services, with the idea of adding rules or new types through new implementations without altering the central code.
- LSP is illustrated with button and link components in React and with Rectangle and Square in TypeScript; the proposal is to maintain safe substitution and consistent behavior among related types.
- ISP is applied when components receive too many props or when an interface forces a class to implement a method it does not use; the text proposes dividing interfaces and smaller components.
- DIP is presented as dependence on abstractions instead of concrete implementations, both by injecting functions in React and by interfaces in Angular.
- The closing encourages practice, team review and exploration of patterns such as MVC, MVVM and CQRS to carry these principles forward.
