---
title: "Introduction to Test-Driven-Development in React for Beginners"
date: '2022-04-14T09:15:49-03:00'
category: webclip
summary: 'The article shows TDD in React by first writing tests for a Counter component, then implementing the component and an Increase button in App.js until the tests pass.'
tags: ["react", "test-driven-development", "testing-library", "javascript"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Introduction to Test-Driven-Development in React for Beginners - DEV Community 👩‍💻👨‍💻"
    url: "https://dev.to/koladev/introduction-to-test-driven-development-in-react-for-beginners-260f"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-04/dev-to--introduction-to-test-driven-development-in-react-for-beginne.md"
    kind: repo
---

The article explains TDD in React through a simple counter. It starts with a test for a `Counter` component that receives a `value` prop and then moves to an `App` that renders the counter with a button that increases the count by one.

## Reading notes

- TDD is presented as writing a test before coding the feature.
- The example uses a simple counter instead of focusing on styling.
- The project is created with `yarn create react-app react-test-driven-development` and started with `yarn start`.
- A `components` directory is created inside `src`.
- `Counter.test.js` is written before `Counter.jsx`.
- The counter test checks that the component renders and shows the value `2`.
- The test uses `render`, `screen.getByTestId`, `toBeInTheDocument`, and `toHaveTextContent`.
- Running `yarn test` fails before the component exists, which matches the TDD flow.
- `Counter.jsx` renders a `<p>` with `data-testid="counter-test"` and displays `props.value`.
- The next step adds the counter to `App.js` with a button that changes state.
- `App.test.js` checks that `App` renders, the counter starts at `0`, the button exists, and clicking it changes the counter to `1`.
- The test uses `userEvent.click` to simulate the button press.
- `App.js` uses `React.useState(0)` and passes the state value to `Counter`.
- The button calls `setCount(count + 1)` when clicked.
- The article notes a React 18 warning about `ReactDOM.render` and points to a StackOverflow answer for fixing it.
- It ends by saying the next article will cover TDD with Redux and thunk.
