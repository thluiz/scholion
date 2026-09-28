---
title: "Implementing & Testing Repository Pattern using Entity Framework"
date: '2022-07-13T09:45:13-03:00'
category: webclip
summary: 'The article explains why Repository Pattern can still help with Entity Framework by reducing duplicate query logic, separating persistence concerns, and making business logic easier to unit test through mocking.'
tags: ["repository-pattern", "entity-framework", "unit-testing", "mocking"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Implementing & Testing Repository Pattern using Entity Framework"
    url: "https://rubikscode.net/2022/07/11/implementing-and-testing-repository-pattern-using-entity-framework/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-07/rubikscode-net--implementing-testing-repository-pattern-entity-framework.md"
    kind: repo
---

The article argues that Repository Pattern remains useful with Entity Framework when you want to avoid repeated query code, keep persistence details out of application code, and make business logic easier to test. It also notes that DbContext and DbSet do not remove the need for abstraction in every case.

## Reading notes

- The definition used is that a repository mediates between the domain and data mapping layers and behaves like an in-memory collection.
- One benefit is reducing duplicate query logic, especially when the same query appears in multiple places.
- Another benefit is separating application code from the persistence framework and the database behind it.
- The article says the pattern helps unit testing mainly by making repository behavior easier to mock in business logic tests.
- The repository interface is described as generic and exposing Add, Remove, Get, GetAll, and Find.
- Save is left out because the article assigns saving responsibility to Unit of Work.
- Entity Framework is described as an object-relational mapper that maps code objects to database tables and back.
- The article distinguishes database-first and code-first approaches and uses code-first for the example.
- DbContext and DbSet are the key Entity Framework classes used in the implementation.
- Tests are written with xUnit and Moq, following a test-first approach.
- The Add test verifies that Repository calls DbContext.Set and then DbSet.Add.
- The Remove test follows the same pattern and verifies DbSet.Remove.
- The Get test verifies DbSet.Find.
- The GetAll and Find tests require mocking IQueryable behavior on DbSet, including Provider, Expression, ElementType, and GetEnumerator.
- The final repository implementation uses Context.Set<TEntity>() in the constructor and delegates each method to the DbSet.
- The conclusion says the value of Repository and Unit of Work depends on the problem, but mocking DbContext and DbSet can still be useful.
