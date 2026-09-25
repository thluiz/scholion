---
title: "Let’s learn how modern JavaScript frameworks work by building one"
date: '2026-09-25T18:24:52+01:00'
category: webclip
summary: 'The post explains how post-React frameworks converge on reactivity, cloned templates, and newer web APIs, then builds a small framework step by step to show how those pieces fit together.'
tags: ["javascript-frameworks", "reactivity", "templates", "proxy"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Let’s learn how modern JavaScript frameworks work by building one"
    url: "https://nolanlawson.com/2023/12/02/lets-learn-how-modern-javascript-frameworks-work-by-building-one/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/nolanlawson-com--lets-learn-how-modern-javascript-frameworks-work-by-building.md"
    kind: repo
---

The post argues that modern JavaScript frameworks are easiest to understand by building one. It treats post-React frameworks as a family that relies on reactivity, cloned templates, and APIs like `<template>` and `Proxy`, then sketches a toy framework around those ideas.

## Reading notes

- Modern frameworks are described as post-React client-side frameworks such as Lit, Solid, Svelte, and Vue.
- The author groups them around three shared ideas: reactivity for DOM updates, cloned templates for rendering, and newer web APIs like `<template>` and `Proxy`.
- React is presented as more pull-based, while modern frameworks push updates only to the parts of the component tree that depend on changed state.
- A small reactivity system is built with a `Proxy`, `createEffect`, `onGet`, `onSet`, a dependency map, and microtask batching.
- DOM rendering is built around tagged template literals, parsing HTML once into a `<template>`, and cloning the template for later renders.
- The template parsing step is cached with a `WeakMap` keyed by the `tokens` array from the tagged template literal.
- Dynamic values are handled with stub placeholders that are replaced in attributes and text content.
- The reactive system and renderer are combined so state changes update the DOM through effects.
- The post notes missing pieces such as deep tree updates, repeated lists, key handling, and more efficient binding lookup.
- The conclusion says the exercise helped explain framework internals and mentions a smaller custom framework for an emoji picker component.
- It also points to browser APIs such as the DOM Part API proposal and possible extensions to `Proxy` as future improvements.
