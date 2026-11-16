---
title: "The Third Age of JavaScript"
date: '2026-11-16T04:01:41+00:00'
category: webclip
summary: 'The essay argues that JavaScript entered a third era around 2020, defined by ESM replacing CommonJS, collapsing tooling layers, and more core tools being written in systems languages for speed and safety.'
tags: ["javascript", "esm", "tooling", "systems-languages"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The Third Age of JavaScript"
    url: "https://swyx.io/writing/js-third-age"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/swyx-io--the-third-age-of-javascript.md"
    kind: repo
---

The essay frames JavaScript history as three ages. The first ran from 1997 to 2007 and was about building the language. The second ran from 2009 to 2019 and was about users extending it through Node.js, npm, build tools, and new runtimes.

## Reading notes

- The Third Age begins around 2020, when the ecosystem starts clearing away legacy assumptions.
- CommonJS is described as a compromise that ES Modules has been waiting to replace.
- Browsers can handle small amounts of modules, while tooling and bundling details are still unresolved.
- Pika and Snowpack are presented as a bridge toward an ES Modules-first future.
- IE11 is expected to reach end of life over time.
- The essay says JavaScript tools no longer need to be built in JavaScript.
- TypeScript, Deno, Relay, Parcel, and Volta are used as examples of core tooling moving toward Rust or other strongly typed cores.
- The author describes this shift as moving from a "Functional Core, Imperative Shell" model to a "Systems Core, Scripting Shell" model.
- Deno is described as collapsing testing, formatting, linting, bundling, TypeScript support, and standard libraries into one runtime.
- Rome is described as collapsing those same layers on top of Node.js.
- Public cloud platforms have become central to JavaScript use, even if cloud platform developers often avoid the language.
- Cloud-based development environments such as Glitch, Repl.it, Codesandbox, GitHub Codespaces, and Stackblitz are presented as examples of cloud distros.
- JAMstack providers such as Netlify and Vercel are described as collapsing layers between CI/CD and CDN.
- Frontend frameworks also reflect the same pattern: Svelte moves animations and state management into a compiler, React explores metaframeworks and client-server integration, and Vue works on Vite.
- The essay summarizes Third Age tools as faster, ESM-first, more collapsed, more typesafe, more secure, polyglot, and more neo-isomorphic.
- The result is described as better developer experience and better user experience.
- The essay ends by raising the possibility that JavaScript’s Third Age may also be its last, with WebAssembly as the looming alternative.
