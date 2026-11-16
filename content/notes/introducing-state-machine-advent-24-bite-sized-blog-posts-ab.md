---
title: "Introducing state machine advent: 24 bite-sized blog posts about state machines and statecharts"
date: '2020-02-22T12:11:59+00:00'
category: webclip
summary: 'The author introduces a 24-day series on state machines and statecharts, motivated by Redux limitations and a need to model application states and transitions more strictly.'
tags: ["state-machines", "statecharts", "xstate", "redux"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Introducing state machine advent: 24 bite-sized blog posts about state machines and statecharts"
    url: "https://dev.to/codingdive/introducing-state-machine-advent-24-bite-sized-blog-posts-about-state-machines-and-statecharts-2ce0"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--introducing-state-machine-advent-24-bite-sized-blog-posts-ab.md"
    kind: repo
---

The post explains why the author turned to state machines after running into Redux problems with invalid application states and awkward handling of transitions. It frames XState as a JavaScript-based way to model states and transitions more explicitly and with fewer bugs.

## Reading notes

- The series will publish one piece of content each day until Christmas to explain the theory and application of state machines and statecharts.
- The author started looking for a state management library that could scale well and offer a good developer experience.
- A todo MVC example ended up in an invalid state, with loading still true after todos had resolved.
- That bug showed that Redux did not make it easy to model state transitions.
- The author wanted a paradigm that could strictly model all possible states and transitions of an application.
- After studying finite state machines and JavaScript implementations, the author chose XState.
- XState state machines and statecharts can be defined with plain JavaScript objects.
- The author says they are still learning XState and have not gone back to other state management libraries.
- The series claims state machines and statecharts can make apps more resilient and code easier to reason about.
