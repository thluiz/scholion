---
url: "https://dev.to/canro91/this-is-why-we-dont-test-private-methods-28ef?context=digest"
captured_at: "2026-09-24T23:52:57+01:00"
title: "This Is Why We Don't Test Private Methods"
domain: "dev-to"
---

_I originally posted this post on [my blog](https://canro91.github.io/2024/11/30/TestingPrivateMethods/) a long time ago in a galaxy far, far away. It's part of an ongoing series I've been publishing, called [Unit Testing 101](https://canro91.github.io/UnitTesting)._

* * *

Trying to test private methods causes a lot of confusion.

That's a common question we all have made when finding unit testing for the first time. These days, I found that very same question on [Reddit](https://www.reddit.com/r/csharp/comments/1gf2r6s/trying_to_understand_why_we_dont_test_private/):

> Can someone explain to me why unit testing our private methods is bad?

And here's my full answer:

## [](#because-we-dont-want-to-break-encapsulation)Because we don't want to break encapsulation.

If you have a private method, how are you going to call it from a test class or method?

It's private. You can only access it from inside the same class. That's the whole point of access modifiers: restricting access to the fields and properties that hold the internal state of a class.

And please don't make your private methods public and static to call them directly inside unit tests. They're private for a reason, right? We don't want the rest of your code to use them directly.

Exposing internals is [the most common mistake when writing tests](https://canro91.github.io/2021/10/11/DontRepeatLogicInAssertions/). I've [seen it and fixed it before](https://canro91.github.io/2022/12/22/TestingDuplicatedEmails/).

Let's take the `HasAdmin()` method from the question as an example,  

```
private bool HasAdmin(List<string> relations, bool hasPermission)
{
    // Beep, beep, boop...
}
```

Enter fullscreen mode Exit fullscreen mode

Unless `HasAdmin()` has 0 references—if that's the case, you should remove it—another method from the same class is calling it. And you can trace the chain of method calls back to a public method.

`HasAdmin()`, or any other private method down in the chain of method calls, is changing something that you can observe from public methods. Probably it's affecting a return value or changing an internal state you can inspect with getters. That's what you should test instead.

To test `HasAdmin()`, create a `User` object with the right relations and permissions, call the public methods you have, and check what should change when your user is an admin or not. Maybe you return additional data only admins can access or finish an action without throwing a `UnauthorizedAccessException`.

You test private methods indirectly while testing the observable behavior exposed through public methods.

Et voilà!

Want to learn more about unit testing? Grab a copy of **[Start Testing](https://imcsarag.gumroad.com/l/unittesting101/?utm_source=devto&utm_medium=post&utm_campaign=this-is-why-we-dont-test-private-methods)**. A step-by-step guide to writing your first C# unit tests with confidence.
