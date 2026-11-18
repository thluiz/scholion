---
title: "10 Things NOT To Do When Building React Applications"
date: '2019-06-30T11:51:56+00:00'
category: webclip
summary: 'The post lists common React pitfalls, from inline functions and random keys to null defaults, prop drilling, and state mutation, and suggests safer patterns like stable keys, context, and explicit props.'
tags: ["react", "javascript", "best-practices", "state-management"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "10 Things NOT To Do When Building React Applications"
    url: "https://dev.to/jsmanifest/10-things-not-to-do-when-building-react-applications-58a7"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--10-things-not-to-do-when-building-react-applications.md"
    kind: repo
---

The post collects 10 React habits to avoid because they can lead to bugs, wasted renders, or harder maintenance. It focuses on practical mistakes around functions, keys, conditional rendering, state updates, and prop handling.

## Reading notes

- Spending too much time in your own private world can leave you behind on community-discovered bad practices, forcing late refactors.
- Defining inline functions in render, or using `bind` there, still creates new function instances on each render and can cause performance issues.
- Random keys solve uniqueness but break identity and make React recreate nodes on every render; keys should stay unique and stable.
- Default parameters only apply when a value is missing or `undefined`, not when it is `null`, which can crash code that expects an array.
- Repetitive components should be abstracted so shared structure changes in one place instead of many.
- Initializing state from props in a constructor does not keep it synced on later prop changes; updates need separate sync logic.
- `items.length && ...` can render `0` when the array is empty; double negation avoids that by turning the expression into a boolean.
- Copying state without deep care can still mutate nested data, as shown with `splice` on `items` inside a copied object.
- Passing props explicitly makes debugging easier, clarifies what a child uses, and can reduce re-render work.
- Prop drilling pushes data through intermediate components, creates tight coupling, and can be replaced with context or redux.
