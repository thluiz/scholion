---
title: "20 ways to become a better Node.js developer in 2020"
date: '2026-11-16T17:51:05+00:00'
category: webclip
summary: 'The article gathers 20 ways to improve as a Node.js developer, from TypeScript, testing and ESM to deployment, security, observability, frameworks and architecture choices.'
tags: ["nodejs", "javascript", "testing", "architecture"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "20 ways to become a better Node.js developer in 2020"
    url: "https://yonigoldberg.medium.com/20-ways-to-become-a-better-node-js-developer-in-2020-d6bd73fcf424"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/yonigoldberg-medium-com--20-ways-to-become-a-better-nodejs-developer-in-2020.md"
    kind: repo
---

The article lists 20 areas a Node.js developer can study in 2020, including TypeScript, modern testing tools, ES modules, newer JavaScript features, architectural styles, Nest.js, gradual deployment, shift-left and shift-right testing, worker threads, Docker and Kubernetes, security, monitoring, machine learning basics, sleep, Fastify or Koa, CI quality tools, and starter projects. Its main point is to broaden the toolbox and choose tools with care instead of relying on one default approach.

## Reading notes

- Use TypeScript for type safety, but do not let its advanced constructs change code style for the wrong reasons.
- Prefer modern testing tools such as Jest and Ava, which improve speed and developer feedback.
- Plan ES modules adoption carefully because support gaps still affect tooling and mocking.
- Track new JavaScript features such as optional chaining, private fields, nullish coalescing, and Promise.any.
- Learn architectural styles beyond the default stack, including layered, hexagonal, clean, streaming, and GraphQL-based approaches.
- Consider Nest.js as a full-featured framework for teams that need more structure than Express provides.
- Use gradual deployment techniques such as feature flags, canary releases, and traffic shadowing.
- Shift testing left by running more tests earlier, and shift right by testing in production with monitoring and traffic-based techniques.
- Use worker threads for CPU-heavy work, while remembering they are not free or instant to start.
- Understand Docker and Kubernetes because they shape shutdowns, memory limits, signals, and runtime behavior.
- Build a security mindset by studying vulnerable code and practicing attack analysis.
- Learn Prometheus or ELK so you can define useful metrics and monitor application behavior.
- Treat machine learning tools as black-box products when the app does not rely on deep ML expertise.
- Sleep more than seven hours a night, because the author cites research and Hillel Wayne’s view that sleep and stress matter more than language or practice choices.
- Evaluate Fastify and Koa as alternatives to Express, which the article describes as old and poorly maintained.
- Use CI tools such as linters, scanners, lockfile checks, commitlint, and dependency rules to raise quality automatically.
- Diversify your toolbox by mixing ideas from different paradigms instead of adopting or rejecting them as a block.
- Study starter projects to borrow structure, architecture ideas, and library choices from real codebases.
