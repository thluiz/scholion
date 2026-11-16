---
title: "How I Write Testable Code | Khalil's Simple Methodology | Khalil Stemmler"
date: '2026-11-16T02:26:18+00:00'
category: webclip
summary: 'The article argues that testability depends on how dependencies are introduced. Prefer abstractions, same-layer or inner-layer dependencies, or stable dependencies, and use dependency inversion when a dependency makes testing hard.'
tags: ["testable-code", "dependency-inversion", "software-design"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How I Write Testable Code | Khalil's Simple Methodology | Khalil Stemmler"
    url: "https://khalilstemmler.com/articles/software-design-architecture/write-testable-code"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/khalilstemmler-com--how-i-write-testable-code-khalil-stemmler.md"
    kind: repo
---

The article says testability starts with how a class depends on other code. If a dependency makes tests slow or hard, the code becomes harder to test, especially when it brings heavy collaborators like a database connection or network calls.

It presents a simple rule for deciding whether to import a dependency when testability matters, and shows how interfaces, abstract classes, dependency inversion, and HOCs can keep front-end and back-end code testable.

## Reading notes

- A source class becomes dependent on another class, function, or variable as soon as it imports or even names it.
- Directly creating a `UserRepo` inside `UserController` creates a hard source-code dependency.
- That direct dependency makes unit tests harder because `UserRepo` also brings the database connection.
- Dependency inversion inserts an abstraction between the source class and the dependency.
- Interfaces or abstract classes can serve as the abstraction.
- With an `IUserRepo` interface, `UserController` can accept any implementation that follows the contract, including a mock object.
- The methodology starts by asking whether future tests against the source class matter.
- If testability does matter, a dependency is acceptable only if it is an abstraction, comes from the same layer or an inner layer, or is a stable dependency.
- If a dependency breaks those rules, dependency inversion can fix the situation.
- The same idea applies on the front end.
- A `ProfileContainer` that depends directly on a `ProfileService` cannot be tested without making real API calls.
- The fix is to define an `IProfileService` interface and have `ProfileService` implement it.
- The container should receive `IProfileService` as a prop rather than create `ProfileService` itself.
- A HOC can supply either the real profile service or a mock profile service.
- The article ends by showing `ProfileContainer` composed with the real service or the mock service.
