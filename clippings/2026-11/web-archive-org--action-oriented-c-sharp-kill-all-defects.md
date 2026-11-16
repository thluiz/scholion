---
url: "https://web.archive.org/web/20191206183600id_/https://killalldefects.com/2019/09/15/action-oriented-c/"
captured_at: "2026-11-16T07:57:05+00:00"
title: "Action-Oriented C# - Kill All Defects"
domain: "web-archive-org"
---

Five years ago I hit a plateau. My code hit a certain level of quality and flexibility and stopped improving. Here’s how I used aspects of functional programming to keep climbing.

My code was pretty [SOLID](https://en.wikipedia.org/wiki/SOLID), but there was still a lot of very similar code, despite actively trying to remove duplication whenever possible. It wasn’t exact duplication, but it was clear patterns throughout code that made maintenance more trouble than it should have been.

Then I discovered how to apply `Actions` and `Funcs` to further improve my code.

Let’s look at a hypothetical example:

While this is a contrived example, this illustrates the problem. In this scenario you have a repetitive pattern of checking a property, then doing some custom logic that should not be invoked if the property was false, then storing the result in a custom property on the object.

It’s a simple little routine, but the duplication is obvious and it resists extracting methods out because the `CalculateX` methods cannot be called if the resume doesn’t have the related degree.

Additionally, let’s say that a bug occurred and a code change was needed. You now need to make the same change in 3 places. If you miss one, it’s likely going to cause bugs. Additionally, the similarities tempt you to do _copy / paste driven development_ which is an anti-pattern and a potential source for bugs if not all lines that needed to be modified were modified.

* * *

What I learned that changed my approach is that passing around [Action](https://docs.microsoft.com/en-us/dotnet/api/system.action-1?view=netframework-4.8) and [Func](https://docs.microsoft.com/en-us/dotnet/api/system.func-2?view=netframework-4.8) types lets you get a lot more flexibility out of your methods by giving them configurable behavior.

`Action` is a generic signature of a method to invoke without a return type.

For example, a signature of something that takes in a boolean and integer parameter would look like this: `Action<bool, int> myAction;`

`Func` is very similar to an `Action` except it returns a value. The type of the value returned is the last generic type argument. For example, a `Func<bool, int>` would take in a boolean and return an integer.

So, we can use a `Func` in our example to extract a method with some configurable behavior:

This improves our calling code to the following brief segment:

This is much simpler, though the syntax is a little harder to read. What we’re doing in the third parameter to the method is declaring a _lambda expression_ similar to those you use for LINQ queries.

If you needed to work with a Func that uses parameters (say, you had a `Func<int, decimal>` signature, you could change your logic to the following:  
`(myInt) => myInt + CalculateMastersDegreeScore();`

While this was a fairly contrived example, hopefully it illustrates the power of passing around `Func` and `Action` to various methods. This is the foundation that _functional programming_ is built upon, but in small doses this can be extremely helpful in object-oriented programming as well.

* * *

While this syntax makes the code a little harder to read, the benefits in maintainability are real and the odds of introducing duplication-related defects is much lower.

Give it a try on a side project or particular area of duplication and let me know what you think.
