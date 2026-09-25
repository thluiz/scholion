---
title: "Bytes #328 - Bloomberg's new TypeScript framework"
date: '2026-09-24T23:08:02+01:00'
category: webclip
summary: 'Issue highlights Stricli, a new TypeScript framework from Bloomberg for CLIs with full typing, zero dependencies, and support for ESM and CommonJS, along with several short links to tools and news.'
tags: ["typescript","cli","bloomberg","viteconf"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Bytes #328 - Bloomberg's new TypeScript framework"
    url: "https://bytes.dev/archives/328?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/bytes-dev--bytes-328-bloombergs-new-typescript-framework.md"
    kind: repo
---

The issue highlights Stricli, a new Bloomberg framework for building complex CLIs with TypeScript. It is presented as a way to keep type safety while avoiding extra dependencies and unnecessary complexity. The issue also notes that Stricli supports ESM and CommonJS, and that its scope is intentionally limited, so other packages are needed for prompts, terminal styling, and similar features.

## Reading notes

- Bloomberg launched Stricli, a framework for building complex CLIs with TypeScript, type safety, and zero dependencies.
- The text contrasts Stricli with tools like oclif and clipanion, saying that they can bring extra dependencies and complexity for some uses.
- The framework offers full TypeScript support, with types defined once for named flags and positional arguments that propagate through the application.
- It also supports ESM and CommonJS, and makes code splitting easier with ESM build tools and dynamic autocomplete.
- The project avoids runtime dependencies and centralizes access to the system in a context object, with optional dependency injection.
- The assumed limitation is that Stricli's scope is narrower, so interactive prompts, terminal styling, and similar features are handled by other packages.
- The rest of the issue mentions ViteConf live, Zod.fyi for viewing issues in `ZodError`, ESLint with official support for JSON and Markdown, Eleventy v3.0 with ESM and Deno, Tauri 2.0, and VoidZero.
