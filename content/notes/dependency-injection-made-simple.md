---
title: "Dependency Injection made simple"
date: '2026-09-24T23:58:50+01:00'
category: webclip
summary: 'The page explains dependency injection as passing an object to the constructor or setter of a dependent class, which decouples the code, makes testing easier, and uses interfaces in strongly typed languages.'
tags: ["dependency-injection","javascript","csharp","interfaces"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Dependency Injection made simple."
    url: "https://dev.to/emanuelgustafzon/dependency-injection-made-simple-3d4c?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--dependency-injection-made-simple.md"
    kind: repo
---

A page defines dependency injection as a simple way to deal with objects that depend on other objects. It first shows a coupled example in JavaScript and then replaces direct connection creation with injection in the constructor, to allow using different connections without changing the route.

## Reading notes

- Dependency injection is presented as the act of passing an object to the constructor or setter of a class that depends on it.
- The initial example shows a posts route that directly creates a DatabaseConnection, which leaves the code coupled and not very flexible.
- The alternative with SQLiteConnection and MySqlConnection passes the connection to the PostsRouter constructor, allowing the implementation used to be changed.
- The text says that this approach decouples the objects and makes code management easier.
- It also states that dependency injection helps with tests, because it is possible to pass a mock object to the post router.
- In strongly typed languages, the text says that it is necessary to define a type for the object passed.
- For this, the page introduces interfaces as a type structure without implementation of methods or properties.
- In the C# example, the SQLiteConnection and MySqlConnection classes implement IDb.
- PostsRouter receives IDb in the constructor and uses the connection through the interface.
- The text ends with a complete example in C# using SQLiteConnection and MySqlConnection in two different PostsRouter objects.
