---
title: "2015: The End of the Monolithic JavaScript Framework"
date: '2015-01-16T09:54:57-03:00'
category: webclip
summary: 'The post argues that front-end development should move away from monolithic JavaScript frameworks toward smaller libraries and components, with less abstraction, more reuse, and stronger shared standards.'
tags: ["javascript", "front-end-frameworks", "component-based-development", "open-source"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "2015: The End of the Monolithic JavaScript Framework / blog unblock"
    url: "https://andywalpole.me/#!/blog/142134/2015-the-end-the-monolithic-javascript-framework"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-01/andywalpole-me--2015-the-end-of-the-monolithic-javascript-framework.md"
    kind: repo
---

Andy Walpole argues that the front-end is changing faster than the rest of the web stack and that large frameworks create risk when their roadmaps shift, especially in corporate settings. He presents AngularJS 2.0 as an example of the costs of investing heavily in one framework, then points toward a component- and library-based approach as a more stable alternative.

## Reading notes

- The front-end layer has changed rapidly in recent years, driven by browser competition and new JavaScript and HTML5 capabilities.
- MVC-style JavaScript frameworks rose to help manage contemporary JavaScript, with Backbone.js first and AngularJS gaining the widest adoption.
- AngularJS 2.0 is described as a complete rewrite with no backwards compatibility, which the author treats as a warning about dependency on one monolithic framework.
- A single framework can become a weak point when its direction changes, its stewardship is corporate, and teams have to relearn it from scratch.
- The author cites a view that dedicated libraries are preferable because they let teams replace one part of the front end without replacing everything.
- A component-based approach also brings risks, including fragmentation, over-abstraction, and harder recruitment and maintenance.
- The proposed manifesto says corporations should contribute back to the projects they use, instead of only taking from permissively licensed software.
- The manifesto also calls for avoiding over-abstraction, staying close to the JavaScript specification, and being cautious about transpiled subset languages.
- The post recommends isomorphic JavaScript, separation of concerns, no unnecessary dependencies, and using an ES6 compiler when appropriate.
- The article ends with a set of library suggestions across helpers, routing, promises, client-server communication, animation, development support, flow control, templating, and micro-frameworks.
- The final checklist asks readers to judge maintainability, performance, accessibility, and openness to contribution when choosing libraries.
