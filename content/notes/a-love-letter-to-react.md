---
title: "A love letter to React"
date: '2026-09-25T08:46:40+01:00'
category: webclip
summary: 'The text says that React influenced LiveView and Phoenix by showing a model of reactive components, colocation between markup and code, HTML-aware components, and diff optimizations on the server and the client.'
tags: ["react","phoenix","liveview","frontend"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "A love letter to React"
    url: "https://fly.io/blog/love-letter-react/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/fly-io--a-love-letter-to-react.md"
    kind: repo
---

React is presented as the basis for several Phoenix and LiveView choices. The text highlights the reactive component model, the joint placement of markup and code, and the adoption of HTML-aware components and slots to build more extensible interfaces.

## Reading notes

- React showed a simple-to-understand component model, with state and rendering that is redone when state changes.
- LiveView brought this model into a process with state on the server.
- Placing HTML together with application code is described as the correct decision because it brings together tightly coupled parts.
- The text argues that if two parts of the code change together, they should live together.
- HTML-aware components and JSX are presented as a way to keep the markup structure readable and to allow natural composition between static tags and dynamic components.
- Slots and functional components in Phoenix are used as a response to the problem of creating reusable and extensible components without hiding the HTML structure.
- The text states that Phoenix adopts efficient diffs on the server, sending only the dynamic parts that changed.
- On the client, the text mentions the use of morphdom to apply only the minimum patches to the DOM.
- The influence of React also appears in the backend, with frameworks like Blade being cited as examples of HTML-aware engines.
- The text ends by arguing that, in 2022, backend frameworks should follow this direction.
