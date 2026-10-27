---
title: "Spine.js vs Backbone.js"
date: '2012-05-02T16:29:06-03:00'
category: webclip
summary: 'The page compares Spine and Backbone on basics, async UI behavior, models, attributes, identifiers, storage, helpers, views/controllers, architecture, and ends by recommending Spine for simplicity or CoffeeScript integration, Backbone otherwise.'
tags: ["javascript-mvc", "spine", "backbone", "coffeescript"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Constant Improvement"
    url: "http://hjortureh.tumblr.com/post/22117245794/spine-js-vs-backbone-js"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-05/hjortureh-tumblr-com--spine-js-vs-backbone-js.md"
    kind: repo
---

The page compares Spine and Backbone as two similar JavaScript MVC frameworks and goes through the main differences in their design and use. It covers how each handles models, collections, attributes, identifiers, record storage, helpers, controllers and views, then closes with a practical recommendation based on the kind of project.

## Reading notes

- Spine and Backbone look similar on the surface, but the article says they differ in important internal details.
- Backbone was created in 2010 by Jeremy Ashkenas and is written in JavaScript.
- Spine was created by Alex MacCaw, came later, and is written in CoffeeScript.
- Backbone became popular quickly and was used by companies such as 37signals, Fog Creek Software, and LinkedIn.
- Spine attracted attention, especially among CoffeeScript developers, but not as much as Backbone.
- Spine is described as 7k and as a framework that simplifies MVC and works well with CoffeeScript.
- Backbone is described as 5.6k and as depending on Underscore.js for missing JavaScript features.
- Spine introduced asynchronous user interfaces early, updating the UI when models are saved without waiting for the server response.
- Backbone adopted the same idea in version 0.9, with the option to disable it using `wait: true` in `save`, `create`, and `destroy`.
- Backbone has Models and Collections, while Spine has only Models.
- Spine uses static and instance methods in a way the article compares to Active Record.
- Spine requires attributes sent to the server to be configured ahead of time.
- Backbone stores attributes through `get` and `set`, which makes models more dynamic.
- Backbone’s setter also triggers both `change` and `change:attribute` events.
- Spine forces the unique identifier to be `id`.
- Backbone can change the unique identifier with `idAttribute`.
- Backbone also has a client-side `cid`, which the article links to asynchronous interfaces.
- Spine stores records in a hash keyed by `id`.
- Backbone uses both an array and a hash and keeps the records array sorted by default.
- Backbone benefits from Underscore helpers such as `map`, `filter`, and `pluck`.
- Spine has fewer helper methods, though CoffeeScript makes similar operations easier to write.
- Spine controllers and Backbone views both connect HTML markup with the model layer.
- Spine adds an `elements` list for naming controller elements.
- Spine is split into separate files such as core, ajax, local storage, and routes.
- The article recommends Spine when simplicity or CoffeeScript integration matters most, and Backbone with Underscore in most other cases.
