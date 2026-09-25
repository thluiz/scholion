---
title: "State Management & Data Fetching Libraries in React"
date: '2026-09-25T21:29:38+01:00'
category: webclip
summary: 'The article recommends starting with React’s built-in state tools for simple cases, adding state libraries only when complexity grows, and using data-fetching libraries to reduce boilerplate and improve loading and error handling.'
tags: ["react", "state-management", "data-fetching", "react-query"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "State Management & Data Fetching Libraries in React"
    url: "https://thetshaped.dev/p/state-management-and-data-fetching-libraries"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/thetshaped-dev--state-management-data-fetching-libraries-react.md"
    kind: repo
---

The article argues that React apps should begin with built-in state tools and only move to external state libraries when state becomes hard to manage, update, maintain, or follow. It also recommends data-fetching libraries because they reduce boilerplate and add loading, error handling, caching, and refetching support.

## Reading notes

- State management and data fetching are two of the main concerns in a React application, and they should be handled well from the start.
- External libraries should be used carefully because they can add complexity that is not needed.
- React’s built-in hooks such as useState, useReducer, and Context API are often enough for small to medium applications.
- Built-in tools are a good fit for simple UI logic and short-term projects or prototypes.
- A state management library becomes more useful when multiple components share and modify the same state.
- Large applications may benefit from a standard way of managing state across the team.
- The application’s structure and logic flow change once a state management library is introduced, so that choice should be made carefully.
- React-Toolkit and Zustand are presented as popular state management options.
- Built-in tools and a state management library can be combined, using built-in state for simpler components and a library for complex shared state.
- React does not provide a common way to fetch data, so teams often build their own implementation.
- A custom data-fetching solution can create extra boilerplate and maintenance work.
- Libraries like React-Query, SWR, Apollo Client, and urql provide hooks that fit the component lifecycle and help with loading and error states.
- Data-fetching libraries act as a thin layer over API calls and add features such as caching, automatic refetching, and background updates.
- The article recommends using data-fetching libraries.
