---
title: "React code conventions and best practices"
date: '2022-08-05T10:28:58-03:00'
category: webclip
summary: 'The page lists React conventions focused on consistent formatting, explicit naming, smaller components, separation of logic from rendering, and preferring declarative code and abstractions over direct library use.'
tags: ["react", "code-conventions", "best-practices", "typescript"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "React code conventions and best practices | by Gaspar Nagy | Jul, 2022 | Level Up Coding"
    url: "https://levelup.gitconnected.com/react-code-conventions-and-best-practices-433e23ed69aa"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-08/levelup-gitconnected-com--react-code-conventions-and-best-practices.md"
    kind: repo
---

The page collects React code conventions that aim to keep codebase structure consistent and easier to maintain. It recommends linting and automatic formatting, ordering imports, using clear naming rules, and avoiding default exports. It also favors barrels, type aliases, and centralized re-exports for third-party libraries.

## Reading notes

- Use linting and automatic formatting with tools such as eslint and prettier.
- Enforce import order through eslint rules so imports stay grouped and alphabetized.
- Use PascalCase for components, interfaces, and type aliases, and camelCase for variables, functions, folders, and non-component files.
- Prefer TypeScript barrels for shared components, utils, and helper functions.
- Avoid default exports because named exports make imports explicit and reduce ambiguity.
- Keep component files consistent by using PropsWithChildren, separating function logic from JSX when it becomes longer, avoiding index keys, using fragments, and destructuring properties.
- Separate business logic from presentation, especially in page or container components that use multiple hooks or useEffects.
- Create custom hooks first, and move to component controllers when components become overloaded with state and hooks.
- Split large components into smaller pieces when conditional rendering, data grid columns, or heavy hook usage makes them harder to read.
- Group state when possible, use shorthand boolean props, avoid curly braces for string props, and avoid inline styles.
- Prefer conditional rendering with the ternary operator and use constants or enums for string values.
- Re-export third-party libraries from a centralized place instead of importing them directly throughout the codebase.
- Rely on abstractions rather than implementation details, prefer declarative programming, use descriptive variable names, avoid long argument lists, and use implicit returns in small functions.
