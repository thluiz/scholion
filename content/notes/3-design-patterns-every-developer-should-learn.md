---
title: "3 Design Patterns Every Developer Should Learn"
date: '2022-04-15T10:07:00-03:00'
category: webclip
summary: 'The article presents design patterns as reusable approaches to recurring software problems and recommends Strategy, Singleton, and Observer as patterns every developer should know, while warning against overusing them.'
tags: ["design-patterns", "strategy-pattern", "singleton-pattern", "observer-pattern"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "3 Design Patterns Every Developer Should Learn | Bits and Pieces"
    url: "https://blog.bitsrc.io/3-design-patterns-every-developer-should-learn-71a51568ac9d"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-04/blog-bitsrc-io--3-design-patterns-every-developer-should-learn.md"
    kind: repo
---

The article treats design patterns as high-level ways to approach recurring software problems, not as code itself. It says they help make code easier to adapt, create a shared vocabulary, and become more important as developers build larger systems and microservices.

## Reading notes

- Design patterns are described as recurring approaches to common problems in software engineering, not as code.
- They are presented as useful for making code more readable and adaptable.
- They also create a shared vocabulary, so teams can communicate with names like Singleton.
- The article recommends three patterns to learn: Strategy, Singleton, and Observer.
- Strategy is used to choose between algorithms at runtime and supports the open-closed principle.
- The delivery example shows separate strategies for bike, car, rail, air, and ship instead of one growing class.
- Singleton is used when only one instance of a class is needed and when shared resources must be controlled.
- The article mentions configuration settings, in-memory data, and comparators as examples of singleton use.
- Observer is presented as a one-to-many relationship where one object notifies others about changes.
- Examples given for Observer include Netflix subscriptions, email notifications, news alerts, Redux, CI builds, Kafka, RabbitMQ, Amazon SNS, and NATS.
- The article warns that design patterns can be overused and should be chosen only when they fit the project.
- It stresses that knowing a pattern’s name is not the same as understanding its constraints and tradeoffs.
- The origin of the idea is traced to Christopher Alexander and later to the 1994 book by the Gang of Four, which popularized design patterns in software development.
