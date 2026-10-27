---
title: "Preparing Yourself for Modern JavaScript Development"
date: '2012-07-09T11:11:30-03:00'
category: webclip
summary: 'The post introduces older JavaScript practices that help prepare for newer tools: using IIFEs and namespaces to avoid global pollution, the revealing module pattern, and constructors with prototypes and inheritance.'
tags: ["javascript", "modules", "prototypes"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Preparing Yourself for Modern JavaScript Development | CodeThinked"
    url: "http://www.codethinked.com/preparing-yourself-for-modern-javascript-development"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-07/codethinked-com--preparing-yourself-for-modern-javascript-development.md"
    kind: repo
---

The post argues that developers who know JavaScript basics can prepare for newer libraries by first understanding scope, modules, namespaces, and constructor functions. It presents these ideas as practical building blocks before moving on to tools like Backbone.js or Ember.js.

## Reading notes

- Code that places variables and functions directly in the global namespace creates pollution and raises the chance of collisions with other scripts.
- An IIFE creates scope by wrapping code in a function that is called immediately, so variables and functions stay out of the global namespace.
- Passing `window`, `jQuery`, and `undefined` into an IIFE gives the code safer local references and avoids relying on possibly changed global values.
- A namespace can be created with an object on `window`, using `window.myApp = window.myApp || {}` so the same object is reused across files.
- A module can combine with a namespace by taking the namespace object as an argument and returning it after adding members.
- The revealing module pattern keeps variables private inside the module and returns an object that exposes only selected functions and values.
- JavaScript constructors use function calls with `new` to create objects, and public instance data is assigned with `this` inside the constructor.
- Methods placed on a constructor’s `prototype` are shared by all instances instead of being duplicated on every object.
- A `Spy` constructor can inherit from `Person` by setting its prototype to `new Person()`, which lets instances use inherited methods such as `fullName()`.
- After splitting code into modules, the next step is to look into combination and minification, with Rails asset pipeline, SquishIt, and ASP.NET MVC 4 mentioned as examples.
