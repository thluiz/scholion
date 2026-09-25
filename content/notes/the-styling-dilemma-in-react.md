---
title: "The styling dilemma in React"
date: '2026-09-25T21:30:51+01:00'
category: webclip
summary: 'The article compares Vanilla CSS, preprocessors, Tailwind CSS, CSS Modules, and CSS-in-JS in React, weighing setup, scope, dynamic styling, and maintainability before preferring classless tools.'
tags: ["react", "styling", "css-in-js", "tailwind-css"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The styling dilemma in React"
    url: "https://thetshaped.dev/p/the-styling-dilemma-in-react"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/thetshaped-dev--the-styling-dilemma-in-react.md"
    kind: repo
---

The page compares common styling approaches in React and says the choice affects development experience, performance, and how easy a codebase is to manage and scale. It goes through plain CSS, preprocessors, Tailwind CSS, CSS Modules, and CSS-in-JS, then prefers classless tools such as Tailwind CSS or CSS-in-JS because they keep styles close to components and avoid class-name overhead.

## Reading notes

- Plain CSS is presented as simple and familiar, with no extra setup, but it brings global scope issues, class collisions, weak support for dynamic styling, and more context switching between files.
- CSS preprocessors such as SASS, SCSS, LESS, and Stylus add variables, nesting, and loops, and they can make styles more modular, but they also add setup complexity and still keep styles globally scoped.
- Tailwind CSS is described as a utility-based approach with many single-purpose classes, high customization, no custom CSS, and standardized design consistency, though components can become cluttered and the setup may need extra configuration.
- CSS Modules scope class names locally by default, which avoids global conflicts and supports modular styles, while still allowing Vanilla CSS or preprocessors.
- CSS-in-JS libraries such as styled-components and emotion keep styles inside JavaScript files, support dynamic styling with props, and reduce file switching, but they add dependencies, can affect performance, and may create server-side rendering issues.
- The author prefers Tailwind CSS or CSS-in-JS because styles stay within components, class names do not need to be invented, and maintenance becomes easier.
- If styled components grow too large, the article suggests extracting them into separate files while keeping localized styles.
- The article ends by saying there is no single right or wrong styling approach in React and that knowing the trade-offs is what matters.
