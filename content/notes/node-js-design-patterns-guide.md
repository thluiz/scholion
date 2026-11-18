---
title: "A guide to Node.js design patterns"
date: '2019-07-08T17:40:52+00:00'
category: webclip
summary: 'The article walks through common Node.js design patterns and shows how each one helps structure code, from IIFEs and factories to observers, dependency injection, middleware, and streams.'
tags: ["node-js", "design-patterns", "javascript", "software-design"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "A guide to Node.js design patterns - LogRocket Blog"
    url: "https://blog.logrocket.com/design-patterns-in-node-js/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/blog-logrocket-com--node-js-design-patterns-guide.md"
    kind: repo
---

The article surveys several design patterns used in Node.js and explains what each one is meant to solve. It starts with IIFEs for simulating static and private variables, then moves through factory, singleton, builder, prototype, observer, dependency injection, chain of responsibility, middleware, and streams.

## Reading notes

- Design patterns help structure code for benefits like faster development and code reuse, and they fit OOP well, though JavaScript can use them outside OOP projects too
- IIFEs execute immediately and can simulate static variables by keeping state in a closure
- IIFEs can also simulate private variables by exposing methods that share hidden state
- The factory method centralizes object creation logic so code can request objects without deciding how to create them each time
- A factory can be useful for creating different error objects from a single place instead of repeating error-object logic across endpoints
- The singleton pattern keeps object creation to one instance and can be implemented with a local module variable and a static getInstance method
- A singleton is presented as useful for keeping one active database connection accessible throughout the codebase
- The builder pattern separates construction from representation and creates complex objects step by step
- Builder methods set properties incrementally and a build method returns the final object
- The article uses House and Person examples to show how builders support different configurations without long constructor argument lists
- The prototype pattern creates new objects from a pre-existing object by cloning it
- A prototype can be used to create similar objects, reduce redundant code, improve performance, and support caching through cloned objects
- The observer pattern lets code react to events or inputs instead of checking for them constantly
- Node’s event-driven APIs, including HTTP server events, are presented as examples of the observer pattern
- EventEmitter is identified as Node’s own implementation of this pattern
- Dependency injection moves dependency creation outside the consuming object and passes dependencies in at runtime
- DI is presented as a way to improve testability, modularity, and scalability
- The article uses an email sender and email service example to show how a mock dependency can be injected during testing
- The chain of responsibility decouples request senders from request handlers by passing a request through a chain until one handler can process it
- Express middleware is described as a practical example of chain of responsibility
- Middleware functions receive request, response, and next, and use next() to pass control along the chain
- Streams are shown as a pipeline of readable, transform, and writable stages that process data chunk by chunk
- The stream example uses pipe() to chain stages and demonstrates the same stage-by-stage idea as chain of responsibility
