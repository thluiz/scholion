---
title: "Mistakes I Made in My First Ember Project"
date: '2014-09-26T18:19:46-03:00'
category: webclip
summary: 'The author reflects on an early Ember project and says the main problems came from starting before understanding Ember conventions, Ember Data, and the framework’s way of handling state.'
tags: ["ember", "ember-data", "javascript-frameworks", "single-page-apps"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Mistakes I Made in My First Ember Project - Press Up"
    url: "http://pressupinc.com/blog/2014/09/mistakes-made-first-ember-project/?utm_source=javascriptweekly&utm_medium=email"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-09/pressupinc-com--mistakes-i-made-in-my-first-ember-project.md"
    kind: repo
---

The author describes a greenfield CRUD app built with Ember and says the hardest parts came from not learning Ember’s core conventions early enough. The project worked, but the process led to confusion, brittle code, and repeated debugging because the framework’s model did not yet feel clear.

## Reading notes

- The project was a simple CRUD app, but it also needed some richer JavaScript-driven interactions.
- The author chose Ember because they wanted to try a single-page JavaScript application and thought Ember’s strengths would fit the project.
- A major mistake was diving in before learning Ember’s core features, values, and conventions.
- Ember’s “magic” and convention-over-configuration style made it easy to get started but hard to understand where new code should go.
- The author says they did not fully use Ember conventions like `.get()` and `.set()` early on.
- Using Ember’s object model matters because it supports computed properties working like regular properties.
- The author says they did not read the documentation deeply enough at the start.
- For Ember docs, the author suggests clearer distinctions between Ember behavior and what an average JavaScript programmer would expect.
- Ember Data simplified working with the server-side API by abstracting it away from the JavaScript code.
- The author did not know the default Ember Data serialization format and chose to use ActiveModel serialization on the server instead.
- That choice led to brittle data handlers on both ends.
- The author says it would have been simpler to adapt the Ember Data serializer to the server’s default rendering.
- The core pattern of the mistakes was fighting “the Ember way” without understanding it.
- Ember is described as a philosophy of work, not just a set of libraries.
- Mixing jQuery and non-Ember state with Ember Table caused DOM state problems.
- The author says Ember should be left in charge of all state in that setup.
- Using native JavaScript methods like `.push()` instead of Ember’s `.pushObject()` caused problems with Ember’s recomputation.
- The author concludes that Ember is powerful and a good place to start for rich single-page applications, but only after learning its conventions more deeply.
