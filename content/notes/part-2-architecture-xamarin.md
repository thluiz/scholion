---
title: "Part 2 - Architecture | xamarin"
date: '2013-08-05T13:48:51-03:00'
category: webclip
summary: 'The page explains that cross-platform apps should maximize code sharing through encapsulation, separation of responsibilities, and polymorphism, then maps those ideas to common application layers and mobile software patterns.'
tags: ["architecture", "cross-platform", "mobile-patterns"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Part 2 - Architecture | xamarin"
    url: "http://docs.xamarin.com/guides/cross-platform/application_fundamentals/building_cross_platform_applications/part_2_-_architecture"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-08/docs-xamarin-com--part-2-architecture-xamarin.md"
    kind: repo
---

The page argues that cross-platform apps should be built around an architecture that maximizes code sharing. It ties that goal to encapsulation, separation of responsibilities, and polymorphism, then recommends keeping layers logically and physically separate so applications stay easier to understand, test, and maintain.

## Reading notes

- Encapsulation keeps classes and architectural layers exposing only a minimal API while hiding implementation details.
- UI code should display screens and accept input, but not talk to the database directly.
- Data-access code should read and write data, but not interact directly with UI controls.
- Separation of responsibilities gives each component a clear and well-defined purpose.
- Polymorphism lets core code work through interfaces or abstract classes while still using platform-specific implementations.
- Typical layers listed are Data Layer, Data Access Layer, Business Layer, Service Access Layer, Application Layer, and User Interface Layer.
- Not every application needs all layers; a simple app may merge the Data Layer and Data Access Layer.
- Common mobile patterns named on the page are MVC, Business Façade, Singleton, Provider, and Async.
- MVC separates View, Controller, and Model, and the text says the model is optional in this context.
- Business Façade gives a simplified entry point for complex work, such as a TaskManager with task retrieval and save methods.
- Singleton is described as a way to ensure only one instance of an object exists, such as a SQLite database.
- Provider supports code reuse by pairing shared interfaces or abstract classes with platform-specific implementations.
- Async is described as running long work on another thread or task so the UI or current processing can continue.
