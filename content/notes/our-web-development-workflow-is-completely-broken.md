---
title: "Our web development workflow is completely broken"
date: '2013-09-27T10:22:29-03:00'
category: webclip
summary: 'The post argues that browser developer tools still assume simple documents, while web apps and frontend workflows have become far more complex. It calls for deeper editor-browser integration and a unified remote debugging protocol.'
tags: ["web-development", "developer-tools", "remote-debugging", "browser-editors"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Our web development workflow is completely broken. — Kenneth Auchenberg"
    url: "http://kenneth.io/blog/2013/05/21/our-web-development-workflow-is-completely-broken/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-09/kenneth-io--our-web-development-workflow-is-completely-broken.md"
    kind: repo
---

The post argues that web development has changed faster than the tools around it. Browsers now run complex applications, but developer tools still mostly treat pages as documents, and that mismatch makes the workflow feel broken. The proposed direction is to keep editors as editors and connect them directly to browsers through deeper integration.

## Reading notes

- The author says his work at Podio, where most frontend code is now JavaScript, changed the tooling needs of frontend development.
- He traces browser developer tools from IE Developer Toolbar to Firebug to Chrome DevTools and notes that they still share the same document-inspection model.
- He says the current workflow is broken because browser tools and editors remain separate and loosely integrated.
- He argues that extra tools such as LiveReload and CSS Reloader only patch symptoms and add more complexity.
- He questions the browser becoming the editor, since browsers are built around a read-only and execute-only model and already need extensions to cover editing needs.
- He says editors should stay the main editing environment, while browsers and editors communicate with each other.
- He points to remote-debugging protocols in Chrome, Firefox, and Safari as the existing path for integration, but says the protocols are incompatible.
- He supports efforts like RemoteDebug that aim to provide one consistent debugging interface across browsers.
- He says deep editor-browser integration also needs platform support for replaying page-load steps, reloading assets precisely, editing JavaScript in place, and keeping DOM state in sync.
- He asks browser vendors to focus on the platform and collaborate with editor vendors instead of reimplementing editors.
- He cites Brackets as an example of contextual editing and imagines browsers feeding computed styles, dimensions, and previews back into the editor.
