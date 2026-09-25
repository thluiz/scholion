---
title: "Web Components Are Not the Future"
date: '2026-09-25T00:51:57+01:00'
category: webclip
summary: 'The text argues that Web Components offer some ergonomics, but they impose a broad cost in abstractions, compatibility, and evolution, which can block better choices for the future of the web.'
tags: ["web-components","javascript-frameworks","front-end"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Web Components Are Not the Future"
    url: "https://dev.to/ryansolid/web-components-are-not-the-future-48bh?context=digest"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--web-components-are-not-the-future.md"
    kind: repo
---

The author revisits a position he had already defended before and says the situation has gotten worse. He sees Web Components as a promise of portability and interoperability that seems attractive, but that brings a high cost to the ecosystem because it forces the web to organize itself around a rigid abstraction.

## Reading notes

- The text says that Web Components were designed to work as native elements, independent of tooling, with the promise of protecting sites and applications against future migration.
- The author argues that the existence of an ambitious standard favors some choices and makes it harder to explore alternatives, because a standard ends up influencing the way the entire platform is thought about.
- He uses JSX as an example of a technology whose standardization would have created problems, since different frameworks and tools treat its semantics in different ways.
- The text states that opportunity cost appears before the code itself, because architecture and abstraction decisions end up requiring limits that are later hard to undo.
- According to the author, Web Components start from Custom Elements, but elements and components are not the same thing, so every interface has to go through the DOM, even when that is not the ideal fit.
- He observes that attributes and properties, boolean rules, reflection between attributes and properties, and extensions used by templating libraries make support for custom elements more complex.
- The text cites that some libraries use prefixes like `attr:`, `prop:` and `bool:` and that this forces runtimes and compilers to know more special cases.
- The author states that clone behavior, upgrade, lifecycle in the DOM, and reactive context create friction for systems such as reactivity and context APIs.
- He also mentions that the Shadow DOM changes event routing and that this affects cases such as event composition and `focusin`.
- The text says that there is a performance cost and that, on the server, Web Components still require specific solutions because there is no DOM, so SSR and hydration need wrappers and extra overhead.
- The author maintains that the extra complexity is not limited to those who use Web Components, because it also weighs on the tools that need to support them.
- He states that advances such as resumability, partial hydration, and selective hydration depend on event delegation, and that this is in tension with the Shadow DOM.
- The text says that components tend to be more a matter of developer experience than something that should remain in the final output.
- In the comparison with micro-frontends and microservices, the author sees value in portability, but says that the cost of mixing versions, libraries, and frameworks increases, especially on the front end, where JS bytes matter a lot.
- He concludes that the most convincing uses are specific cases, such as a third-party widget or a microfrontend container, but in those cases the friction is already low enough that the gain does not justify the general promise.
- The text ends by saying that Web Components can be useful in some scenarios, but that the problem lies in the promise of being more than they are, because this distorts the rest of the web and shifts the cost to everyone.
