---
title: "How To Implement a TypeScript Web App With Clean Architecture"
date: '2022-08-14T17:45:55-03:00'
category: webclip
summary: 'The article explains how to structure a TypeScript web app with core, data, presentation, and DI layers so logic stays independent of frameworks, storage, and other details.'
tags: ["clean-architecture", "typescript", "dependency-injection", "testing"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How To Implement a TypeScript Web App With Clean Architecture | by Aziz Nal | Aug, 2022 | Better Programming"
    url: "https://betterprogramming.pub/how-to-implement-a-typescript-web-app-with-clean-architecture-27c7eb745ab4"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-08/betterprogramming-pub--how-to-implement-a-typescript-web-app-with-clean-architectur.md"
    kind: repo
---

The guide shows a layered setup for a TypeScript web app built around clean architecture. Core holds entities, use cases, and repository interfaces. Data implements repositories and storage details. Presentation uses the use cases, while a DI layer connects the pieces and keeps dependencies pointing back to Core.

It walks through a counter app example, from defining the Counter entity and a create-counter use case to wiring local storage through a repository implementation, a factory, and Angular dependency injection. It also shows how the same structure makes testing easier by letting repository dependencies be mocked.

## Reading notes

- Core contains the app logic, entities, use cases, and repository interfaces.
- Data implements the repositories and handles local or remote storage details.
- Presentation only talks to use cases and does not depend on Data directly.
- A DI layer connects Core, Data, and Presentation without reversing the dependency direction.
- The example app uses a Counter entity with create, delete, increment, decrement, label, and filter requirements.
- The author creates a use case interface so each use case defines its own return type.
- The create-counter use case depends on a repository interface defined in Core.
- Index files are used to re-export modules from Core and Data.
- The repository implementation in Data depends on a local-storage service interface instead of the browser storage API.
- The local-storage service interface is implemented in Presentation, where browser access exists.
- A CounterFactory in DI instantiates the repository and use case with their dependencies.
- Angular providers expose the factory output to the app module.
- The UI component injects the use case and calls it when the user adds a counter.
- A get-all-counters use case is added so counters can be loaded again on page refresh.
- The repository test uses a mock local-storage service and checks that a created counter can be retrieved.
