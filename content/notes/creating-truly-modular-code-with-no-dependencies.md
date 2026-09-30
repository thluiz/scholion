---
title: "Creating Truly Modular Code with No Dependencies"
date: '2017-09-21T15:06:44-03:00'
category: webclip
summary: 'The article argues that rising software complexity comes from dependencies between components, and proposes an element architecture that isolates logic through interfaces and listeners.'
tags: ["software-architecture", "modularity", "dependency-injection", "element-architecture"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Creating Truly Modular Code with No Dependencies"
    url: "https://www.toptal.com/software/creating-modular-code-with-no-dependencies"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2017-09/toptal-com--creating-truly-modular-code-with-no-dependencies.md"
    kind: repo
---

The article says software slows down over time because components become tightly connected, so a change in one place can create bugs somewhere else. It contrasts the big ball of mud with an element architecture that separates complexity into independent parts.

## Reading notes

- Software development often starts fast, then slows as dependency chains grow and changes become harder to predict.
- The “big ball of mud” is described as an anti-pattern where classes depend on each other throughout the codebase.
- Interfaces and inversion of control are presented as a way to separate components without making them aware of each other.
- The article argues that dependency injection still leaves components linked through interfaces and does not remove the core dependency problem.
- The proposed element pattern uses a main class and a listener interface, with the element allowed to call outward only through the listener.
- In the example, the element stays independent of how output is implemented, so the same element can be reused in different applications.
- For larger applications, the suggested structure splits code into client and server, then into app and elements folders.
- The app folder wires components together and holds business logic, while the elements folder contains reusable independent pieces.
- The article presents this separation as a way to keep code maintainable and reusable across projects.
