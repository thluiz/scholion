---
title: "3 Tips That Will Simplify Your Application State Management"
date: '2020-07-05T14:10:45+00:00'
category: webclip
summary: 'The post says state management gets hard because many state sources update together, and suggests three ways to keep it simpler: classify the state, keep it close to where it is used, and avoid putting everything in global state.'
tags: ["state-management", "application-state", "redux", "frontend"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "3 Tips That Will Simplify Your Application State Management"
    url: "https://dev.to/marinvirdol/3-tips-that-will-simplify-your-application-state-management-21e9"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--3-tips-that-will-simplify-your-application-state-management.md"
    kind: repo
---

The post argues that application state becomes difficult when many sources of state update at the same time, so state management should be planned early. It defines state as a representation of a system at a given time and separates it into persistent, navigation, local UI, and client state.

## Reading notes

- The post introduces three strategies for simplifying state management.
- First, identify what kind of state you are working with and decide whether it should be saved later or reflected in the URL.
- For shareable or restorable state, the URL can carry the needed information, as in a YouTube link that opens at a specific moment.
- Second, keep state data as close as possible to where it is needed.
- Keeping state near the component that uses it can reduce re-rendering and improve performance.
- For maintainability, start with internal component state, lift it up only when a parent or sibling needs access, and move it down when only one child uses it.
- Third, do not keep the entire state globally.
- In Redux, only global state should go there; local state should stay close to the components that need it.
- Putting every piece of state in Redux increases complexity because it spreads state handling across reducers, actions, and dispatch calls.
- The conclusion is that state strategy should be planned early because it can affect whether an application succeeds or fails.
