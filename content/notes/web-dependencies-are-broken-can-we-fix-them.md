---
title: "Web dependencies are broken. Can we fix them?"
date: '2026-09-25T17:15:02+01:00'
category: webclip
summary: 'The web makes basic dependency management depend on bundlers, import maps, or fragile workarounds. The post argues that dependencies should be first-class and mapped more natively.'
tags: ["web-dependencies", "import-maps", "bundlers", "web-platform"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Web dependencies are broken. Can we fix them? • Lea Verou"
    url: "https://lea.verou.me/blog/2026/web-deps/?utm_source=substack&utm_medium=email"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/lea-verou-me--web-dependencies-are-broken-can-we-fix-them.md"
    kind: repo
---

The post argues that the web platform has outsourced basic dependency management to third-party tooling, which turns a normal task into a usability cliff. Bundlers are acceptable for optimization, but they should not be required just to use a dependency.

It reviews the main workarounds for using dependencies without bundlers, including raw node_modules imports, CDN imports, local copies, browser bundles, and import maps. Each approach is shown to trade away encapsulation, reliability, locality, or scalability, especially once dependencies themselves depend on other packages.

## Reading notes

- Dependency management should be first-class in the platform, not something handled only by bundlers.
- Bundlers are fine for performance optimization, but not as the default answer for basic dependency use.
- Raw node_modules imports are wasteful, fragile, and break package encapsulation.
- CDN imports add security risk, failure points, and local-development friction.
- Copying packages or exports locally still breaks encapsulation and does not handle transitive dependencies.
- Browser bundles avoid specifiers but just move bundling into the library itself.
- Import maps currently require awkward HTML-level management and do not compose well across dependencies.
- The post suggests improving import maps, making them external or injectable, and exploring server-side handling of specifier resolution.
- It also sketches a broader idea: treating specifiers as a URL-like primitive that the server can resolve.
