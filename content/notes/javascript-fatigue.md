---
title: "Javascript Fatigue"
date: '2016-01-02T15:04:45-03:00'
category: webclip
summary: 'The article argues that React and the surrounding JavaScript ecosystem overload beginners and teams with tooling, APIs, and configuration, and calls for simpler abstractions and faster prototyping setups.'
tags: ["javascript", "react", "tooling", "developer-experience"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Javascript Fatigue — Medium"
    url: "https://medium.com/@ericclemmons/javascript-fatigue-48d4011b6fc4#.rzwz221k3"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-01/medium-com--javascript-fatigue.md"
    kind: repo
---

The article says React and its ecosystem create fatigue because choosing them also means taking on build tools, boilerplates, linters, and other setup work before building anything. It argues that the developer experience gets worse when many small libraries push architectural decisions onto the user.

## Reading notes

- React is described as overwhelming for beginners because the surrounding ecosystem adds too many tools.
- Choosing React and JSX also means taking on build tools, boilerplate, linters, and other setup work.
- Generators such as Yeoman and Plop can reduce copying, but generated projects rarely match real needs exactly.
- Common code is harder to improve across projects when it is not abstracted into an independently updatable dependency.
- A generator can become its own complicated application when it must handle many permutations of use cases.
- Small modular APIs can still produce confusing code when combined across React, Redux, React Router, and Webpack.
- The article calls for an abstract middle ground between wiring dependencies and generating boilerplates.
- It suggests wrapper APIs, presets, file and folder conventions, and community RAD tooling as ways to reduce configuration and implementation details.
