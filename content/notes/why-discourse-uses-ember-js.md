---
title: "Why Discourse uses Ember.js"
date: '2014-04-23T23:16:58-03:00'
category: webclip
summary: 'The author explains why Discourse chose Ember.js for a highly interactive app, arguing that client-side MVC fits richer interfaces, simplifies state handling, and supports an API-first workflow.'
tags: ["emberjs", "client-side-mvc", "discourse", "api-first-development"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Why Discourse uses Ember.js - Evil Trout's Blog"
    url: "http://eviltrout.com/2013/02/10/why-discourse-uses-emberjs.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-04/eviltrout-com--why-discourse-uses-ember-js.md"
    kind: repo
---

The post argues that client-side MVC frameworks are useful when an application becomes highly interactive. In Discourse, state such as whether a post is liked can live in a JavaScript object and template bindings can re-render the UI automatically, avoiding DOM traversal and brittle logic tied to HTML layout.

## Reading notes

- Client-side MVC makes more sense as interactivity increases, while simpler pages can stay server-rendered.
- Plain jQuery becomes awkward when application state grows and logic depends on DOM structure.
- Ember lets a Post be represented as a JavaScript object and bound to a template.
- When the liked state changes, the template updates without a separate render function.
- The app can update the UI optimistically and roll back if a request fails.
- The author says Discourse is fast and that its JavaScript payload works well with CDNs.
- A rich client-side app also gives the team a battle-tested API because the app uses its own API from the start.
- Ember is preferred over other frameworks because its documentation is clearer, it improved quickly, the team has an open-source track record, string templates fit the author’s preferences, and the run loop batches DOM updates.
