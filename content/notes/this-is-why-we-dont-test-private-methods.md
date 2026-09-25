---
title: "This Is Why We Don't Test Private Methods"
date: '2026-09-24T23:52:57+01:00'
category: webclip
summary: 'The post argues that private methods should be tested indirectly through public behavior, because direct tests break encapsulation and expose internals that other code should not use.'
tags: ["unit-testing","encapsulation","private-methods","csharp"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "This Is Why We Don't Test Private Methods"
    url: "https://dev.to/canro91/this-is-why-we-dont-test-private-methods-28ef?context=digest"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dev-to--this-is-why-we-dont-test-private-methods.md"
    kind: repo
---

Trying to test private methods creates confusion, especially for people who are new to unit testing. The post answers that the reason to avoid it is encapsulation. Private methods are only accessible inside the same class, and access modifiers exist to restrict access to a class’s internal state.

Instead of making private methods public just for tests, the post says to test what they affect through public methods. If a private method changes a return value or internal state, create the object with the right data, call the public method, and check the observable result. In the example, `HasAdmin()` should be covered by testing whether a user with certain relations and permissions gets admin-only behavior or a blocked action.

## Reading notes

- Test private methods often causes confusion for people who are starting out in unit testing.
- The justification for not testing them directly is to preserve encapsulation.
- Private methods can only be accessed within the same class, and that is precisely the role of access modifiers.
- It is not a good idea to make private methods public or static just to call them in tests.
- Exposing internals is pointed out as a common mistake when writing tests.
- If a private method has no references, it should be removed.
- A private method in the call chain changes something observable by public methods.
- The test should cover that observable behavior, whether by return value or by internal state visible through getters.
- In the `HasAdmin()` example, the test should create a `User` with appropriate relations and permissions and verify what changes when the user is admin or not.
- The private method is tested indirectly by testing the behavior exposed by public methods.
