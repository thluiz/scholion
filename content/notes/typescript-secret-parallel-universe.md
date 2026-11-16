---
title: "TypeScript's Secret Parallel Universe"
date: '2020-02-22T12:11:48+00:00'
category: webclip
summary: 'The article explains that TypeScript keeps a type scope separate from JavaScript''s value scope, so a class name can exist as both a value and a type. That is why exporting both works in the same namespace.'
tags: ["typescript", "type-scope", "namespaces"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "TypeScript's Secret Parallel Universe"
    url: "https://dev.to/loilo/typescript-s-secret-parallel-universe-54i6"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--typescript-secret-parallel-universe.md"
    kind: repo
---

The article describes a TypeScript library API built as a nested object from classes spread across folders. Several attempts to re-export a class from inside a namespace fail because each attempt exports only the value side or only the type side.

The solution is to export both a value and a type under the same name. TypeScript keeps an independent type scope, separate from JavaScript's variable scope, so a class name can be used both as a constructor value and as an instance type.

## Reading notes

- The author wants classes from separate files to appear as a single nested public API such as `API.Output.Console`.
- `export Console` inside a namespace is invalid TypeScript.
- `export Console = ConsoleAlias` does not resolve the name.
- `export { ConsoleAlias as Console }` is not permitted inside a namespace.
- `export const Console = ConsoleAlias` compiles, but the type `API.Output.Console` is missing.
- `export type Console = ConsoleAlias` makes the type usable, but `new API.Output.Console()` fails.
- The working approach is to export both the value and the type.
- TypeScript maintains a type scope that is independent of JavaScript's value scope.
- A class declaration creates both a value and a type.
- When a class is imported, both the class object and the class type are imported.
- `export const` exports only the value side.
- `export type` exports only the type side.
