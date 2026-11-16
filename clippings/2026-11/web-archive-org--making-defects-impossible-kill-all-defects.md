---
url: "https://web.archive.org/web/20191206190723id_/https://killalldefects.com/2019/08/29/making-defects-impossible/"
captured_at: "2026-11-16T07:56:33+00:00"
title: "Making Defects Impossible - Kill All Defects"
domain: "web-archive-org"
---

Software bugs are bad, but repeated bugs of the same type can be beyond frustrating. How many times have we seen error messages containing strings like “Object reference not set to an instance of an object”? As software engineers, we can fight one-off occurrences as we find them, or we can aggressively look to eliminate common causes of defects as we identify them.

![A pair of microchips with two legs bent up to look like bugs or defects](https://i0.wp.com/cdn-images-1.medium.com/max/600/0*mUfTyVY7uQYD1aUv.jpg?resize=600%2C450&ssl=1)

Whenever you see a defect, ask yourself how it was possible for that defect to exist, for it to remain undetected for however long it did, and what you can do to either eliminate the possibility of future defects like it or make it impossible for them to hide

Certainly we can’t eliminate all types of issues, but the types of issues we can strategically address at the design or language level is growing every year.

This article is written from the perspective of a .NET and JavaScript development manager, but the techniques may also be more broadly applicable to other languages.

Bear in mind that many of these techniques have tradeoffs in readability or other facets (particularly those related to functional programming), so choosing to go with them should not be automatic, but rather a careful decision made based on the skill level and familiarity of your team members, the state of the codebase, and the nature of the types of problems you’re trying to solve.

## Identifying Run-Time Errors at Compile Time

Starting with an easy and fairly obvious one, compiled languages give you the ability to catch what would be a run-time error at compile time. In JavaScript, you can easily write a function like this:

`function myMethod(a, b, c) {}`

And try to invoke it via:

`my**m**ethod(1, 2, 3);`

The JavaScript will parse fine but create a runtime exception when `mymethod` cannot be found.

TypeScript will catch this at time of compilation (transpilation, rather) preventing you from making this mistake. Additionally, TypeScript gives you static type checking via syntax like

`public myMethod(a: number, b: number, c: number): void {}`

This will catch issues where you try to invoke it like `myMethod(1, 2, '3');`

Of course, this takes away some of the advantages of dynamically typed languages, but you can mix strongly typed definitions and more generic JavaScript in TypeScript. Additionally, even statically typed compiled languages have dynamic language capabilities, such as the`dynamic` keyword in .NET.

## **Ensuring Validity with Immutability**

In programming immutability refers to an object’s state being unchangeable. This restriction can have some performance benefits, but the quality benefits it offers are sometimes overlooked.

Take the .NET DateTime object, for example. If you try to create a new DateTime instance representing January 35th or some other invalid date, the constructor will throw an exception. The DateTime object is designed in such a way that if you have an instance, you know it represents a valid date and have no need to do any verification to it.

The tradeoff of this, is that you can’t take an instance representing January 28th and modify the Day property to be the 35th since the date it represents is immutable. If you do want to advance a day, for example, you call a method to add a TimeSpan to the DateTime instance and this creates a new DateTime instance that is also known to be in a good state (advancing the month and year as needed).

By adopting this technique in your own classes, you can offer the same sort of quality benefits to your code. This is an approach commonly supported by functional languages such as F#.

[ImmutableJS](https://github.com/immutable-js/immutable-js) is a very well known library that offers immutability in JavaScript.

## **Baking Validation into Types with Discriminated Unions**

Both F# and TypeScript have a concept called a Discriminated Union. A Discriminated Union is essentially the concept of an “or” type saying that something is one of a number of different possibilities.

The classical example in TypeScript of this reads as follows:

`Type User = AnonymousUser | AuthenticatedUser;`

This lets you declare return types, properties, and parameters as `User` meaning that they can either be an `AnonymousUser` or an `AuthenticatedUser`. If you have some logic that explicitly requires an `AuthenticatedUser` you can call a method with a signature similar to `authenticate(user: AnonymousUser): AuthenticatedUser` to convert the user to an `AuthenticatedUser` and then require certain methods take in an `AuthenticatedUser` instance. This bakes validation into your typing system.

The downside of this approach is that you can have an explosion of nearly identical types and need to maintain more code for type transitions.

In the .NET ecosystem, you can use [F#’s Discriminated Union](https://fsharpforfunandprofit.com/posts/discriminated-unions/) feature support or use a library like [OneOf](https://killalldefects.com/2019/09/22/oneof-discriminated-unions-in-c/) to introduce the capability using .NET Generics syntax.

## **Null Reference Exceptions**

Ask almost anyone in a .NET development shop (or potentially their customers) and they’ve seen the dreaded “Object reference not set to an instance of an object” error message.

This is a common problem in object oriented languages. By defining reference variables, it’s possible to set the reference to null.

Take the following example:

`var myObject = someList.FirstOrDefault(o => o.Id == 42);`

If an object with an Id property of 42 is in `someList`, `myObject` will now hold a reference to it and calling `myObject.DoSomething();` will work, but if no object exists in `someList` with an Id of 42, then `myObject` will be `null` and you can’t invoke a method on a null instance so a null reference exception is thrown.

Functional Programming languages get around this via a concept of Options. Options can either be of `Some` and `None` with `Some` representing a non-null entity and `None` representing a null entity.

So, what’s the difference between this and standard references in object oriented languages, or even nullable types with `HasValue` and `Value` methods? The key difference is that you can do things like this:

This makes interacting with null values explicit and forces the developer to consider null and non-null scenarios.

The above sample uses the .NET [Language-Ext](https://github.com/louthy/language-ext) library for functional programming. In TypeScript you could use the [fp-ts](https://github.com/gcanti/fp-ts) library which offers a simple set of functional programming constructs including Options.

See [my article on Eliminating Nulls in C# with Functional Programming](https://killalldefects.com/2019/09/11/eliminating-nulls-in-c-with-functional-programming/) for more information on Option classes.

* * *

Ultimately, there are a number of ways to attack common programming problems. This list barely scratches the surface and I could write another article entirely on Reactive Programming and the problems it can solve, but hopefully this gives you a tip of the iceberg insight into the types of problems you can eliminate via carefully applying tools, languages, and libraries.
