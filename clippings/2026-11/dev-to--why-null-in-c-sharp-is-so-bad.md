---
url: "https://dev.to/mbernard/why-null-in-c-is-so-bad-cid"
captured_at: "2026-11-16T01:42:28+00:00"
title: "Why null in C# is so bad"
domain: "dev-to"
---

In my career, more than half of the bugs I encountered were related in a way or another to a null value being propagated where it shouldn't have been—therefore resulting in unexpected behaviors or a nasty `NullReferenceException`.

## [](#the-problem)The problem

Why is null such a problem in C#? Well... the null problem (a.k.a the billion-dollar mistake) breaks many assumptions you can make about the programming language.

In more theoretical terms, it breaks the Liskov substitution principle. (One of the famous [SOLID principles](https://en.wikipedia.org/wiki/SOLID))

> Let Φ(x) be a property provable about objects x of type T. Then Φ(y)should be true for objects y of type S where S is a subtype of T.

[![lB5wmMp-1](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fblog.miguelbernard.com%2Fcontent%2Fimages%2F2019%2F03%2FlB5wmMp-1.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fblog.miguelbernard.com%2Fcontent%2Fimages%2F2019%2F03%2FlB5wmMp-1.png)

#### [](#did-i-lose-you-great-now-lets-talk-plain-english)Did I lose you? Great! Now let's talk plain English.

It means that you should be able to use any subtype in place of its parent type without affecting the behavior of the application.

#### [](#what-does-that-have-to-do-with-null)What does that have to do with null?

In the C# compiler, there's a rule to enforce and prevent multiple inheritances... except... for null. Null is a special instruction in the language that can substitute any type. Put in another way; it means that null inherits from all reference types.

Because of that, you cannot think of your code logically anymore. You always have to check if the value is of subtype null or not. You have to check this because null behave in a very different way than any other type. It needs special processing and/or logic branching.

```


var customer = this._customerRepository.Get();
if (customer != null)
{
    // rest of the logic here.
}
else
{
    // logic for the null case here.
}


```

Enter fullscreen mode Exit fullscreen mode

This practice, often referenced as defensive programming, makes your code verbose and error-prone. It works fine-ishhh. To make it work, you need to do it everywhere in your system. It's really easy to forget one location and guess what? It's precisely where you're going to get a `NullReferenceException` popping up in production.

## [](#solutions)Solutions

Yes, of course, you can use the more beautiful Elvis operator `?.`, but it doesn't solve anything. It just makes the code more readable.

The only real solution is to get rid of all the `null`. That being said, unless you have very strict coding rules within your team, I doubt you'll be able to do it. It's always tempting as a developer to take a shortcut and return a null value on a function call.

### [](#c-80-to-the-rescue)C# 8.0 to the rescue

Fortunately, C# 8.0 adds a brand new [feature](https://blog.miguelbernard.com/c-8-0-nullable-reference-types-are-here/) to help us with the `null` witch hunt. That new option instructs the compiler to check for null values in all code paths. Simply add this line to your `.csproj` and voilà!

```


<Nullable>enable</Nullable>


```

Enter fullscreen mode Exit fullscreen mode

[![vs\_csharp\_null\_warning](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fblog.miguelbernard.com%2Fcontent%2Fimages%2F2019%2F03%2Fvs_csharp_null_warning.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fblog.miguelbernard.com%2Fcontent%2Fimages%2F2019%2F03%2Fvs_csharp_null_warning.png)

Then you can start getting rid of those null values and make sure nobody introduces new ones behind your back.

## [](#conclusion)Conclusion

Using that will most likely break everything on a brownfield project, but for greenfield projects, I highly recommend you enable it. It might seem more work at first, but writing code without passing null around will save you many long, painful debugging hours in production. Ask me how I know. For me, that upfront development cost is a no-brainer.

Good hunt!
