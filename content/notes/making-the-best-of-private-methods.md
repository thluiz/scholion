---
title: "Making the best of private methods"
date: '2015-07-24T08:44:58-03:00'
category: webclip
summary: 'The post argues that private methods help narrow public promises, keep code stable, and make it easier to focus on what a class does rather than how it does it. It also treats private methods as a safe place to test abstractions before promoting them.'
tags: ["private-methods", "ruby", "rails"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Making the best of private methods - Firmafon Developers Blog"
    url: "https://dev.firmafon.dk/blog/making-the-best-of-private-methods/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-07/dev-firmafon-dk--making-the-best-of-private-methods.md"
    kind: repo
---

The post argues for splitting objects into a public part and a private part. Private methods reduce the surface that other code can depend on, which makes a system easier to keep stable and easier to change later. They also help shift attention from implementation steps to the result those steps produce.

It presents private methods as a place to start small, try an abstraction, and promote it only when there is real outside need. Rails methods marked `:nodoc:` are used as an example of keeping internal methods out of the public contract while still making them available inside the framework.

## Reading notes

- The author prefers objects with a public section for other objects and a private section for internal use.
- Exposing more public methods creates more promises that the code has to keep stable.
- Keeping methods private narrows the reach of code and reduces instability spreading through the rest of the app.
- Private methods help focus on what the code does instead of how it does it.
- Rails can keep internal methods in the public namespace and mark them `:nodoc:` so they do not appear in generated public documentation.
- Methods can start private and become public when there is frequent need outside the class.
- In one Rails app example, a private `before_save` callback was made public because it was useful in the console and avoided `send`.
- The author sees private methods as a way to test abstractions, keep boundaries clear, and let code evolve from actual needs.
