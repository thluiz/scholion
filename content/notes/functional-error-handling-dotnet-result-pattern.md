---
title: "Functional Error Handling in .NET With the Result Pattern"
date: '2023-12-04T10:03:55+00:00'
category: webclip
summary: 'Explains using a Result/Error type for functional error handling in .NET, reserving exceptions for truly exceptional cases and making expected failures explicit and testable.'
tags: ["dotnet", "error-handling", "functional-programming"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Functional Error Handling in .NET With the Result Pattern"
    url: "https://www.milanjovanovic.tech/blog/functional-error-handling-in-dotnet-with-the-result-pattern/?utm_source=Twitter&utm_campaign=27.11.2023"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/milanjovanovic-tech--functional-error-handling-dotnet-result-pattern.md"
    kind: repo
---

The article argues that exceptions should be used only for exceptional situations and unknown errors, not for regular control flow or validation. For expected, handleable errors, it proposes the Result pattern: methods return a Result object that explicitly signals success or failure and carries an Error value with a code and description. This makes failure modes visible in method signatures, simplifies testing, and allows consistent conversion to HTTP responses in ASP.NET Core.

A minimal Error record holds a unique Code and a developer‑oriented Description, with a special None instance. A corresponding Result class exposes IsSuccess, IsFailure, and Error, and can only be created via static Success and Failure methods so that its state remains consistent. The pattern can be extended with a generic Result<T> and there are libraries like FluentResults if you do not want to roll your own. A refactored FollowerService shows replacing thrown DomainException validation errors with Result.Failure values based on a FollowerErrors helper class that centralizes possible errors for the follower domain. At the API boundary, you can map Result values to HTTP responses either by checking IsFailure directly or through a Match extension method that routes to onSuccess or onFailure callbacks. Collecting Error instances in static classes also doubles as documentation, and the author mentions generating tables for Confluence by scanning these definitions.

## Reading notes

- Using exceptions for flow control enforces a fail‑fast style but hides possible failures from the method signature and forces callers to know implementation details and specific exceptions.
- The article recommends reserving exceptions for errors that cannot be handled and catching them as low in the call stack as possible.
- Expected, handleable errors should be modeled functionally with the Result pattern so that the method’s ability to fail is explicit.
- An Error record encapsulates application errors via a Code and a developer‑friendly Description, plus a special None value for the success case.
- The bare‑bones Result class stores IsSuccess and Error, exposes IsFailure as the negation of IsSuccess, and validates in its constructor that success pairs only with Error.None.
- Static factory methods Success and Failure are the only way to create Result instances, enforcing a valid combination of success flag and error value.
- In the FollowerService example, thrown DomainException cases for self‑follow, non‑public profile, and already following are replaced with Result.Failure calls.
- Returning Task<Result> from StartFollowingAsync makes all possible errors explicit and removes the need to throw for validation and business rule violations.
- A FollowerErrors static class groups follower‑related Error instances like SameUser, NonPublicProfile, and AlreadyFollowing under descriptive codes and messages.
- FollowerErrors can also expose factory methods (for example NotFound(Guid id)) that construct Error instances with interpolated values.
- Grouping errors via dedicated classes or a nested Errors hierarchy documents the possible errors for each entity or area of the application.
- In ASP.NET Core Minimal APIs, a straightforward mapping checks result.IsFailure to return a BadRequest with the error or a NoContent success response.
- A ResultExtensions.Match method provides a more functional mapping from Result to API responses, taking onSuccess and onFailure delegates and invoking the appropriate one.
- Using Match in the Minimal API endpoint leads to a concise expression of the success and failure branches without explicit if checks.
- The author highlights that the Result pattern improves testability because callers can verify specific failure values instead of catching exceptions.
- The frequently asked questions restate that exceptions for flow control are hard to reason about and that the Result pattern makes potential failures visible in return types.
- The FAQ also emphasizes grouping errors into those you know how to handle and those you do not, applying exceptions only to the latter.
- Error instances collected in code can be turned into human‑readable documentation, such as a generated table uploaded to Confluence.
- The article encourages readers to adopt the Result pattern to clarify error semantics and improve code quality in .NET applications.
