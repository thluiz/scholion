---
title: "17 Tips from a Senior React Developer"
date: '2026-09-24T23:33:53+01:00'
category: webclip
summary: 'The text gathers 17 tips for learning React more clearly: mastering JavaScript, using the documentation, building projects, avoiding too many libraries, abstractions too early, and frameworks without need.'
tags: ["react","javascript","typescript","frontend"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "17 Tips from a Senior React Developer"
    url: "https://dev.to/_ndeyefatoudiop/17-tips-from-a-senior-react-developer-2249?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--17-tips-from-a-senior-react-developer.md"
    kind: repo
---

The article collects 17 tips for learning and working with React, based on the author's experience at Palantir. It argues for building projects early, reading the docs and other code, keeping components simple, using TypeScript, refactoring regularly, and choosing libraries or frameworks only when they are actually needed.

## Reading notes

- Learning JavaScript before React avoids confusion between what belongs to the language and what is specific to the framework.
- The official React documentation, including the Quick Start and the learning chapters, is enough to get started.
- Watching tutorials and buying courses does not replace building projects from the beginning.
- Libraries should come from trusted authors, with a good number of downloads and regular updates.
- Whenever possible, the text recommends solving problems with native JavaScript to reduce dependencies, bundle size, build time, and maintenance.
- Bundle size should be monitored, and lazy loading is suggested to avoid slow loading.
- Code and assets related to a component should stay together to make reading easier and avoid forgotten files.
- Components that try to do everything tend to be hard to read, maintain, and change without side effects.
- Solving varied problems with React helps identify patterns, anti-patterns, and new approaches.
- In addition to React, the text argues for studying data structures, algorithms, and general programming principles.
- Reading a lot of React code, from open source projects and from colleagues, is also presented as an important way of learning.
- TypeScript is shown as a big change in the workflow, with fewer prop errors and fewer bugs reaching production.
- Abstractions too early can create wrong solutions and generate refactoring later or bad code that is hard to evolve.
- For simple apps, built-in React state management, such as useState, useReducer, and useContext, is usually enough.
- The text warns against following online advice without evaluating one's own context, citing the case of memoization and React 19.
- Short and frequent refactorings help when components become too large, confusing, or complex.
- A simple setup with React, Vite, and react-router may be enough; frameworks like Next.js and Remix should only be added when their features are actually needed.
