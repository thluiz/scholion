---
title: "A Dark Mode Toggle with React and ThemeProvider"
date: '2021-08-08T15:19:43-03:00'
category: webclip
summary: 'The tutorial shows how to build a React dark mode toggle with styled-components, persist the chosen theme in localStorage, and default to the user’s OS color scheme when available.'
tags: ["react", "styled-components", "dark-mode", "localstorage"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "A Dark Mode Toggle with React and ThemeProvider | CSS-Tricks"
    url: "https://css-tricks.com/a-dark-mode-toggle-with-react-and-themeprovider/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2021-08/css-tricks-com--dark-mode-toggle-react-themeprovider.md"
    kind: repo
---

The page explains how to build a light and dark theme switch in React with styled-components. It starts with ThemeProvider and GlobalStyles, then moves the toggle logic into a reusable useDarkMode hook that stores the choice in localStorage and can respect prefers-color-scheme.

## Reading notes

- It uses ThemeProvider from styled-components to pass either lightTheme or darkTheme into the app.
- GlobalStyles reads background and text colors from the current theme and adds a short transition for smoother switching.
- The initial toggle can be handled with React state and a click handler that swaps between light and dark.
- A custom Toggle component makes the switch reusable and uses SVG icons for sun and moon.
- The useDarkMode hook stores the selected theme in localStorage so the choice persists between sessions.
- The hook also checks for a saved theme on mount and can return a componentMounted flag to avoid showing the wrong icon before the theme is ready.
- If the browser supports prefers-color-scheme and there is no saved theme, the hook can default to dark mode when the OS prefers it.
