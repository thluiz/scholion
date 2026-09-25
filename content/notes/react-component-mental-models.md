---
title: "React Component Mental Models"
date: '2026-09-25T21:34:49+01:00'
category: webclip
summary: 'The article contrasts Container/Presentational components with Stateful/Stateless components and argues that hooks make the older split less necessary by keeping state and business logic closer to where they are used.'
tags: ["react", "hooks", "component-design", "state-management"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "React Component Mental Models"
    url: "https://thetshaped.dev/p/react-component-mental-models"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/thetshaped-dev--react-component-mental-models.md"
    kind: repo
---

The article explains two ways of thinking about React components. The older model separates container components, which handle state and data fetching, from presentational components, which handle how data is displayed. It then argues that hooks make this split less useful in modern UI applications because state and business logic can live closer to the components that use them.

## Reading notes

- Container components handle state and data fetching, while presentational components focus on how data looks to the user.
- The article says this pattern can become hard to manage, extend, and test as applications grow.
- Hooks let developers add statefulness without wrapping components in a container just to provide state.
- A custom hook such as `useUsers` can hold business and application logic while `UserList` stays focused on display.
- The Stateful and Stateless model spreads responsibility through the application instead of concentrating complexity in a few components.
- The state and business logic should live as close as possible to where they are used.
- In the form example, the `Form` component keeps business logic, while the `Input` component stays stateless and only shows validation errors.
- Even a `ToggleButton` fits better in the Stateful and Stateless model because its active or inactive state lives inside the component.
- The article recommends preferring the Stateful and Stateless components model for code that is easier to manage, extend, maintain, and test.
