---
title: "Handling Dependency Injection in Inherited Classes"
date: '2021-06-21T10:30:00-03:00'
category: webclip
summary: 'The post shows that constructor injection in a base class becomes tedious when new shared dependencies are added to every subclass, and proposes a dependency aggregate to centralize them.'
tags: ["dependency-injection", "inheritance", "mediatr", "dotnet"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Handling Dependency Injection in Inherited Classes"
    url: "https://samwalpole.com/handling-dependency-injection-in-inherited-classes?utm_source=csharpdigest&utm_medium=email&utm_campaign=359"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2021-06/samwalpole-com--handling-dependency-injection-in-inherited-classes.md"
    kind: repo
---

The post explains that dependency injection works well for testability, maintainability, and reusability, but inheritance makes it awkward when a base class gains more shared dependencies. Every concrete handler then needs its constructor updated to pass the new arguments through to the base class.

## Reading notes

- Dependency injection is presented as a useful pattern because it improves testability, maintainability, and reusability.
- In inherited classes, adding a new dependency to the base class forces changes in every concrete subclass constructor.
- Large constructor signatures make the class intent harder to read.
- The proposed fix is to create a dependency aggregate that groups the shared dependencies.
- The base handler receives the aggregate instead of individual dependencies.
- Concrete handlers then depend on the aggregate, so adding a new shared dependency only requires changes in the aggregate class and the base class.
