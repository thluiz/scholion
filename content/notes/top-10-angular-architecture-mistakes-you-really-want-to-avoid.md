---
title: "Top 10 Angular Architecture Mistakes You Really Want To Avoid"
date: "2026-09-23T17:42:20+01:00"
category: webclip
has_commentary: false
summary: "Tomas Trajan catalogs ten recurring Angular architecture mistakes, from missing eager/lazy boundaries and duplicated routing patterns to skipping dependency-graph tooling and standalone components."
tags:
  - angular
  - architecture
  - dependency-graph
  - standalone-components
sources:
  - title: "Top 10 Angular Architecture Mistakes You Really Want To Avoid - Angular Experts"
    url: "https://angularexperts.ch/blog/top-10-angular-architecture-mistakes?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/angularexperts-ch--top-10-angular-architecture-mistakes-you-really-want-to-avoid.md"
    kind: repo
---

Tomas Trajan, a Google Developer Expert for Angular, argues that architecture know-how in Angular has stayed stable since Angular 4 introduced lazy-loaded routing, even as newer APIs like signals, standalone components, and zoneless change detection keep reshaping the syntax layer. He lists ten recurring mistakes that tangle a codebase's dependency graph and erode the eager/lazy split that keeps initial JavaScript bundles small.

The mistakes cluster around two failures: not enforcing boundaries between lazy features, or between lazy features and the eager core, and not using available tooling to catch violations before they compound. Trajan pairs each mistake with a concrete fix, from picking one routing style to scoping services to specific lazy routes.

## Fichamento

- Skipping architecture planning entirely produces a tangled dependency graph, visualized as an "overconnected ball of mud" with circular imports, that turns "move fast and break things" into "change one thing, break everything."
- Not separating eager (core) from lazy (feature) code lets a single import, such as a core service reaching into a feature service, pull that feature and everything it imports into the eager bundle, hurting both performance and architecture.
- Forgetting to lazy-load some features (commonly login/signup, the error/404 page, or whichever feature was implemented first, before routing existed) leaves inconsistent patterns; his fix is to implement even a single-page app's first feature as a lazy route from the start.
- Using more than one way to do the same thing (he counts four ways to configure Angular routing) adds cognitive load; he recommends standardizing on feature-based routes with `loadChildren`, extended with `loadComponent` for sub-navigation.
- Optimizing for DRY over isolation backfires in frontend code: he argues isolation between lazy features is worth 3 to 10 times more than removing duplication, since ad-hoc, per-flow requirements are common and isolated code evolves independently.
- Analyzing architecture by hand, manually grepping for cross-feature imports, doesn't scale; he recommends `madge` for visualizing the dependency graph and `eslint-plugin-boundaries` for encoding allowed import rules between folder-based "core" and "feature" types, enforced automatically on every pull request.
- Losing track of the dependency graph's three properties, one-way direction (lazy sub-features can depend on parents, not the reverse), isolation between sibling branches, and absence of cycles, is what the other mistakes ultimately damage.
- Reusing a component across features by importing it directly instead of extracting it creates invisible coupling; his fix is a generic `ui/` folder holding components stripped of feature-specific logic.
- Not understanding Angular's two governing systems, template context and injector hierarchy, leads to accidental cross-feature service consumption; scoping a service through a lazy route's `providers` array, instead of `providedIn: 'root'`, keeps it from being reachable by features it wasn't meant for.
- Skipping standalone components, available since Angular 14, keeps the dependency graph coarser and forces features to depend on a shared module's full component set instead of cherry-picking only what they use.
