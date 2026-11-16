---
title: "The Bridge Pattern - Design Patterns meet the Frontend"
date: '2026-11-16T00:53:28+00:00'
category: webclip
summary: 'The article explains the Bridge Pattern as a way to separate abstraction from implementation, reduce coupling, and let both evolve independently, with examples in Angular and a frontend data access layer.'
tags: ["bridge-pattern", "frontend", "angular", "type-script"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "The Bridge Pattern - Design Patterns meet the Frontend"
    url: "https://dev.to/coly010/the-bridge-pattern-design-patterns-meet-the-frontend-46fc"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--the-bridge-pattern-design-patterns-meet-the-frontend.md"
    kind: repo
---

The article presents the Bridge Pattern as a way to separate abstraction from implementation so each can change on its own. It uses shapes and colors to show how a class can hold a reference to an implementation, improving loose coupling, maintainability, and testability.

## Reading notes

- The Bridge Pattern is framed as part of the composition over inheritance idea.
- The pattern separates an abstraction from an implementation.
- In the shape example, Shape is the abstraction and Color is the implementation.
- Multiple shapes and multiple colors can vary independently without affecting each other.
- The abstraction keeps a reference to the implementation through a property.
- The consumer of the abstraction does not need to know the underlying implementation.
- The article shows TypeScript examples with Color, Shape, Red, Blue, Circle, and Triangle.
- The pattern supports easier extension for new shapes and colors.
- The article says the pattern decouples abstraction and implementation so they can differ independently.
- Each side keeps its own inheritance hierarchy.
- The abstraction can be set or swapped at runtime.
- Angular's ControlValueAccessor is presented as an example where a framework abstraction can use external implementations.
- A frontend data access layer is proposed as another use case.
- In that example, EntityService is the abstraction and IApiService is the implementation.
- UserService refines the abstraction and uses the API service to add and update users.
- A custom API service can be swapped for another implementation such as MongoDBService without changing the rest of the usage.
