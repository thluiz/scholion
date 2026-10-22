---
title: "How To: Use LocalStorage with React"
date: '2021-02-25T08:39:24-03:00'
category: webclip
summary: 'The article shows how to use localStorage in a React app to remember a first visit, switch the message on later visits, and notes that localStorage stores values as strings.'
tags: ["react", "localstorage", "useeffect", "usestate"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How To: Use LocalStorage with React - DEV Community"
    url: "https://dev.to/antdp425/how-to-use-localstorage-with-react-2cpn"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2021-02/dev-to--how-to-use-localstorage-with-react.md"
    kind: repo
---

The page shows a simple React example that changes its welcome message after the user has visited once. It uses localStorage to remember the visit on the device or browser, and it notes that localStorage is only suitable for simple data and should not hold sensitive information.

## Reading notes

- The example starts with a component that always shows a first-time welcome message.
- `useEffect` runs after the first render and checks whether `localStorage` already has a `hasVisited` key.
- If the key exists, the component sets the message to "Welcome back!".
- If the key does not exist, the code creates the `hasVisited` key in `localStorage` with the value `true`.
- The message changes on refresh or when the page is visited again.
- `localStorage` stores and retrieves values as strings, so numbers, arrays, and objects must be stringified and parsed.
