---
title: "Dependency injection in Ember.js - Going deeper"
date: '2026-09-27T00:30:58+01:00'
category: webclip
summary: 'The post explains how Ember sets up container dependencies, how `register` and `inject` work, why components and views default to new instances, and how `container.lookup` ties caching and instantiation together.'
tags: ["ember-js", "dependency-injection", "container", "singleton"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Dependency injection in Ember.js - Going deeper"
    url: "http://balinterdi.com/2014/05/16/dependency-injection-in-ember-dot-js-going-deeper.html?utm_source=Ember+Weekly&utm_campaign=92cbf50a88-Ember_Weekly_Issue_58&utm_medium=email&utm_term=0_e96229d21d-92cbf50a88-99490097"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/balinterdi-com--dependency-injection-in-ember-js-going-deeper.md"
    kind: repo
---

The post expands on Ember's internal dependency injection setup. It shows where the app container is created, how objects from the container can access it, and how public APIs can replace direct use of the private `__container__` property.

## Reading notes

- Ember creates an internal container when an app starts, and that container is the basis for its dependency setup.
- `optionsForType` can define lookup behavior for a type, such as making components and views non-singletons.
- The default for singleton behavior is `true`, so `container.register('store:main', Store, { singleton: true })` matches `application.register('store', Store)`.
- Objects created by the container have a `container` property, which lets routes call `this.container.lookup` without relying on `__container__`.
- `instantiate: false` is used for templates and helpers, since they are functions and do not need instantiation.
- `container.lookup` first returns a cached singleton if one exists, then instantiates the requested full name, caches it if needed, and finally returns the result.
- `container.lookup` also checks that the full name follows the `type:name` syntax before doing the lookup.
