---
title: "Developing Backbone.js Applications"
date: '2013-05-24T15:21:08-03:00'
category: webclip
summary: 'A guide to building client-side apps with Backbone.js, covering MVC and MV*, models, views, collections, routers, REST sync, modular development, testing, and common patterns.'
tags: ["backbonejs", "mvc", "single-page-apps", "javascript"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Developing Backbone.js Applications -"
    url: "http://addyosmani.github.io/backbone-fundamentals/"
    kind: repo
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-05/addyosmani-github-io--developing-backbone-js-applications.md"
    kind: repo
---

The book argues that Backbone.js helps structure client-side code for data-rich web applications. It explains MVC and MV* ideas, shows how Backbone models, views, collections, routers, events, and sync work, and then applies them in Todo and book library examples.

## Reading notes

- Client-side apps increasingly pull raw data from the server and render it in the browser when needed.
- Backbone is presented as a lightweight library for organizing code and separating responsibilities.
- The book targets novice to intermediate developers who want better-structured client-side code.
- It frames Backbone as MV* rather than strict MVC.
- Models hold application data and support defaults, getters, setters, validation, and change events.
- Views render model data into the DOM and handle user interaction through delegated events.
- Collections group models, support add, remove, reset, set, fetch, and utility methods from Underscore.
- REST persistence is handled through fetch, save, create, and destroy, all backed by Backbone.sync.
- Events are a central part of Backbone and are mixed into models, collections, views, routers, and Backbone itself.
- Routers map URLs to application states and work with Backbone.history.
- The Todo app example uses localStorage, filtering, and view updates driven by model and collection events.
- The book library example shows a REST API, server-side persistence, and date and keyword handling.
- Marionette and Thorax are presented as extensions for larger or more opinionated architectures.
- Common problems cover nested views, nested models, validation, inheritance, and event aggregation.
- Modular development is covered through RequireJS, AMD, and related build tooling.
- Backbone Boilerplate and Grunt-BBB are shown as scaffolding and build helpers.
- The mobile chapter shows how Backbone can be combined with jQuery Mobile while delegating navigation and page enhancement carefully.
- Pagination is handled with Backbone.Paginator for both request-side and client-side paging.
- Jasmine, QUnit, and SinonJS are introduced for testing Backbone apps.
- The appendix sketches a small MVC implementation and compares MVC, MVP, and Backbone’s approach.
