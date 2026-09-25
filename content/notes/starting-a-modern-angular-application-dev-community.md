---
title: "Starting a Modern Angular Application"
date: '2025-04-02T11:06:05-03:00'
category: webclip
summary: 'The article recommends Nx monorepos, Tailwind CSS, SSR-ready code, standalone components, zoneless reactivity, strict linting, immutable data, and avoiding aging Angular features.'
tags: ["angular", "nx", "tailwind-css", "zoneless"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Starting a Modern Angular Application - DEV Community"
    url: "https://dev.to/oz/starting-a-modern-angular-application-34h6?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-04/dev-to--starting-a-modern-angular-application-dev-community.md"
    kind: repo
---

The article argues that the first architecture choices in an Angular app shape maintenance, performance, and user experience for years. It recommends Nx for new workspaces, Tailwind CSS for styling, SSR-compatible code from the start, standalone components, zoneless change detection, strict TypeScript and linting, immutable data, and Playwright or Vitest for testing.

## Reading notes

- The initial app structure affects development, user experience, bundle size, lazy loading, code reuse, and onboarding.
- A plain Angular CLI single-project setup is easy to start, but it is fragile, encourages relative imports, circular dependencies, and weak lazy loading.
- An Angular CLI monorepo with libraries gives modularity and reusable code, but path management and boundary tracking are manual.
- Nx adds module-boundary enforcement, cache, parallel runs, incremental test and build execution, Playwright support, and config migration.
- The author recommends Nx, or a multi-project workspace if Nx feels too costly, and advises against the single-project option.
- Tailwind CSS is recommended for styling, and CSS is preferred over Sass for modern browser features and easier integration.
- For UI components, the article mentions PrimeNG, Angular Material, spartan/ui, and daisyUI, and prefers libraries that use CSS variables, avoid extra maintenance burden, stay Angular-focused, and remain active.
- SSR should be enabled during setup even if the app does not plan to use it, so the code stays reusable and compatible later.
- Standalone components, directives, pipes, and libraries should be used by default instead of creating new NgModules.
- New apps should be zoneless and use `provideExperimentalZonelessChangeDetection()`, with `OnPush` and signals for best performance.
- For state management, the article points to signals and `SignalStore`, and links to the author’s own helpers for collections and reactive storage.
- For testing, Playwright is recommended for e2e, Storybook as an extra option, and Vitest for unit tests in a real browser.
- The article recommends strict TypeScript and ESLint settings, including strong Angular, RxJS, and unused-code checks.
- Data structures should be immutable by default because Signals compare by reference and Angular change detection works better that way.
- Helpful extras include `mat-icon` with an SVG icon registry, type-fest, and `tailwindcss-safe-area`.
- The author advises avoiding Angular Animations, legacy control-flow directives, and CSS selectors based on Angular Material class names.
