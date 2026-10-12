---
title: "Creating Reusable Pagination Controls for Ember.js"
date: '2014-06-30T10:02:03-03:00'
category: webclip
summary: 'The post shows how to build an Ember component for pagination using Foundation markup, computed properties, and actions, then extend it with previous/next arrows and truncated page lists.'
tags: ["ember-js", "pagination", "foundation", "components"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Creating Reusable Pagination Controls for Ember.js"
    url: "http://spin.atomicobject.com/2014/06/27/pagination-emberjs-foundation/?utm_source=Ember+Weekly&utm_campaign=963a48fa79-Ember_Weekly_Issue_64&utm_medium=email&utm_term=0_e96229d21d-963a48fa79-99490097"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-06/spin-atomicobject-com--creating-reusable-pagination-controls-for-ember-js.md"
    kind: repo
---

The post describes a reusable Ember component for pagination. It starts with currentPage and totalPages, uses a computed pageItems list to drive the template, and keeps the UI simple by letting the component update currentPage directly.

## Reading notes

- The component is built on Foundation’s pagination markup and CSS.
- It starts with currentPage and totalPages as the core properties.
- A computed pageItems property generates the page objects used by the template.
- Clicking a page updates currentPage through an action handler.
- The template iterates over pageItems to render clickable page numbers.
- The page objects are plain JavaScript objects because they are recomputed when dependent keys change.
- Previous and next arrow controls are added with canStepForward and canStepBackward computed properties.
- The arrows are shown as unavailable when movement is not possible.
- When the page count is large, the component adds maxPagesToDisplay to truncate the list.
- The truncation logic inserts ellipses and tries to keep pages near the current page visible.
- The author notes that the implementation could be more efficient but is good enough in practice.
- The wrap-up credits Ember’s computed properties and bindings for making the component easy to build.
