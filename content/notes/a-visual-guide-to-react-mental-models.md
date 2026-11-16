---
title: "A visual guide to React mental models"
date: '2026-11-16T03:15:07+00:00'
category: webclip
summary: 'The article argues that React becomes easier to work with when you model components as boxes, props as arguments, closures as scoped access, and state as the part that persists across renders.'
tags: ["react", "mental-models", "javascript", "closures"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "A visual guide to React Mental models"
    url: "https://obedparla.com/code/a-visual-guide-to-react-mental-models"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/obedparla-com--a-visual-guide-to-react-mental-models.md"
    kind: repo
---

The article says that mental models are the fastest way to feel confident with React. It builds that idea from first principles and uses boxes, functions, closures, state, and rendering to explain how React works.

## Reading notes

- Mental models are ways of imagining how a system works, and they help people understand problems and solve them faster.
- A useful mental model is presented as the quickest way to feel confident with React.
- The article is the first part of a three-part series and points to a second part about `useState`, `useEffect`, and component lifecycles.
- React components are described as functions, with other components as functions calling functions and props as function arguments.
- JSX hides that function-based structure and makes nested components easier to read.
- A component is modeled as a box that runs logic, evaluates JSX, and produces HTML.
- Components can have many children but only one parent, matching the tree-like structure of HTML.
- Closures are described as a core JavaScript concept that lets a function use information from outside while keeping its own information contained.
- React components are treated as closures, with data flowing from parent to child through props.
- The example with `Parent` and `ChildButtons` shows a child triggering a parent state update through a function passed in props.
- State is described as a special part of the box that gets an initial value on first render and stays current across later renders.
- On each render, variables and functions are recreated, while state is preserved until a `set` method changes it.
- Rendering is modeled as the first creation of the box and later recycling of the box when props or state change.
- When props or state change, React re-renders the component and its children so the UI matches the latest data.
- The complete model brings these ideas together as nested boxes with downward data flow, props as shared information, and state as the value React keeps stable across renders.
