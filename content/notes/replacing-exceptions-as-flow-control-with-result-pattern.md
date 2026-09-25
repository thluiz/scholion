---
title: "Replacing Exceptions-as-flow-control with the Result Pattern"
date: "2026-09-23T17:41:55+01:00"
category: webclip
has_commentary: false
summary: "Andrew Lock walks a C# service through three stages — exceptions for flow control, a basic Result<T>, and a safer Switch()-based Result<T> — showing why each trade-off matters."
tags:
  - csharp
  - dotnet
  - result-pattern
  - error-handling
sources:
  - title: "Replacing Exceptions-as-flow-control with the result pattern"
    url: "https://andrewlock.net/working-with-the-result-pattern-part-1-replacing-exceptions-as-control-flow/?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/andrewlock-net--replacing-exceptions-as-flow-control-with-the-result-pattern.md"
    kind: repo
---

Andrew Lock opens the first post of a series on the result pattern by responding to a public complaint from Jeremy Miller, who has been recommending people rip the pattern out of their codebases. Lock's counter isn't a full defense: he grants that Result<T> objects threaded back through mediator handlers into MVC can pile on abstraction, but argues the core benefits still hold. Exceptions are expensive to throw in .NET, so using them for routine control flow is costly, and a method that returns Result<T> instead of T makes its failure conditions visible in the signature instead of hidden in undocumented throws.

The post is a worked refactor of a hypothetical UserProvisioningService, walked through three stages to make the trade-offs concrete. The happy-path version hides its failure modes entirely: nothing signals what happens if claim validation comes back empty or tenant lookup fails. Adding exceptions for each failure case fixes that but introduces its own cost, verbose try/catch wrapping and exception types the caller has no way to discover from the method signature alone. Replacing those exceptions with a basic Result<T> class (an IsSuccess flag plus Value or Error) makes failure explicit, but Lock's first version still lets you access Value or Error incorrectly, and only avoids that at the cost of a Switch()-based version whose nested callbacks produce a "pyramid of doom" that's harder to read than either of the two versions it replaced.

## Reading notes

- Lock's stated case for the result pattern: exceptions are performance-expensive as ordinary control flow in .NET, and returning Result<T> instead of T makes failure conditions explicit in the method signature rather than hidden in undocumented throws.
- He acknowledges Miller's specific complaint (Result<T> objects threaded through mediator handlers into MVC, adding abstraction) without disputing it directly, framing his own argument as about the pattern's core benefit rather than every implementation of it.
- Stage 1 (happy path only): the example service assumes every step succeeds; nothing in the code signals what should happen if claim validation returns nothing or tenant lookup fails.
- Stage 2 (exceptions for flow control): throwing typed exceptions (ValidationException, UnknownTenantException) at each failure point works but is expensive at runtime, requires the caller to know which exceptions to catch since the method signature doesn't declare them, and gets verbose fast if you need to wrap each call to produce a "correct" semantic exception type.
- Stage 3 (basic Result<T>): a class with IsSuccess, Value, and Error properties removes the exception cost and makes failure visible in the return type, but nothing stops calling code from reading Value or Error on the wrong branch, a bug that surfaces as a real NullReferenceException.
- Stage 4 (safer Result<T> via Switch()): hiding Value/Error as private fields and forcing access through a Switch(onSuccess, onFailure) method closes that hole, but chaining several Switch() calls produces deeply nested callbacks, the "pyramid of doom", that Lock calls "kind of horrible" to read.
- Lock's own conclusion for this post: none of the three stages shown is the version he'd recommend using. The safer Result<T> fixes the type-safety problem but at a verbosity cost he flags as unsustainable, deferring the actual fix (LINQ-based extensions on Result<T>) to the next post in the series.
