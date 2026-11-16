---
url: "https://dev.to/integerman/the-dream-of-c-9-0-5fc7"
captured_at: "2026-11-16T19:23:30+00:00"
title: "The Dream of C# 9.0"
domain: "dev-to"
---

As part of the final entry in the [C# Advent series of 2019](https://crosscuttingconcerns.com/The-Third-Annual-csharp-Advent), [Calvin Allen](https://twitter.com/_CalvinAllen) touched on some proposals in the C# 9 language that he was most excited about. It’s a quick, well-written, and exciting [article](https://www.calvinallen.net/csharp-8-is-old-news-onward-to-csharp-9/) you should check out and one I’ll expand on here.

Go ahead. I’ll wait.

Great! Now that you’re back, lets talk about the aspects of C# 9 that I’m really excited about as it supports more functional programming techniques.

So, with this preamble out of the way, what is it about C# 9 that gets me really excited?

**Note:** All items here are proposals and not final in syntax or in their inclusion in the next version of C#. Still, it’s good to look ahead at what may be coming. For full proposal details, see [the C# 9 Milestone on GitHub](https://github.com/dotnet/csharplang/milestone/15).

## [](#simplified-null-validation)Simplified Null Validation

Let’s start off with something simple.

C# 9’s proposal allows for the following syntax:

[![](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fqxv9jlezw0m5dqz08w7x.png)](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fqxv9jlezw0m5dqz08w7x.png)

Note the exclamation mark next to `brain`.

This is the equivalent of the following code:

[![](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fzddj27s29egy6eg4sqqc.png)](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fzddj27s29egy6eg4sqqc.png)

As you can see, this feature would simplify argument validation and potentially make the argument validation visible to upstream callers via IntelliSense.

My initial thoughts on this feature are that I like it and likely will use it, but prefer [C# 8’s existing null validation](https://killalldefects.com/2019/09/13/safer-code-with-c-8-non-null-reference-types/) to this. Combining the two would be fine, but more for readability and documentation.

Still, this is a feature that would help instrument legacy C# codebases.

## [](#primary-constructors)Primary Constructors

C# 9 has proposals that would allow you to simplify class constructors in the same way that you can in TypeScript.

Instead of writing the following code:

[![](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8e3uu2tsmnks9xocplot.png)](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8e3uu2tsmnks9xocplot.png)

You can instead use this code:

[![](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fw1m4ydzrba37x6242aj5.png)](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fw1m4ydzrba37x6242aj5.png)

As you can see, this is a significantly smaller amount of code. I frequently say that [code you don’t have to write won’t break](https://killalldefects.com/2019/08/29/making-defects-impossible/) and this is one of those cases.

By keeping your constructor logic minimal, you eliminate redundant boiler plate code that encourages skimming code files instead of doing a real code review. By having less code, we make it harder for bugs to hide by making our code more meaningful.

As an aside, this is one of the things I love about F#, so I am happy to see anything that helps C# have similar levels of conciseness.

## [](#record-classes)Record Classes

Records are so similar to primary constructors that I’d almost say they’re a minor syntax tweak variant of primary constructors.

Let’s say you need an object that holds a certain amount of information, yet has no need for methods. This is essentially a _record_ or a piece of data.

You can use primary constructors to declare the fields of the object, then end the class definition with a semicolon instead of declaring an empty body:

[![](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Ffz6yfwge1mqwjcfuhs9z.png)](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Ffz6yfwge1mqwjcfuhs9z.png)

In general I’m not in favor of record classes in object oriented programming, except as they apply to minimal functional programming languages like F#.

As we’ve seen in recent releases of C#, the language is supporting more and more aspects of functional programming and I view this feature as a stepping stone to enable and expand more advanced features like discriminated unions.

## [](#discriminated-unions-via-enum-classes)Discriminated Unions via Enum Classes

My number one wish for the C# language is support for Discriminated Unions and matching on various types. Incidentally, this is my number one favorite feature in F# as I’ve [written previously](https://killalldefects.com/2019/12/15/a-net-managers-perspective-on-f/).

If you’re not familiar with Discriminated Unions, they say that an object can be one of X different possibilities and your code can match off of these possibilities and take appropriate action based on which type it is.

C# currently has some support for this type of behavior via inheritance and overloading to some extent, but proper discriminated unions are concise and do not require object oriented features in order to work.

* * *

C# 9 has [a feature proposal](https://github.com/dotnet/csharplang/issues/113) to support Discriminated Unions in the language.

Take a look at the following class definition, noting the use of `enum class` syntax and the use of Records and primary constructors:

[![](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F9ave3o9l49y3dyxho61i.png)](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F9ave3o9l49y3dyxho61i.png)

You could then potentially match on a game card in code via a switch expression like the following:

[![](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fj7zwjr1r7rzd1a6qn3jw.png)](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fj7zwjr1r7rzd1a6qn3jw.png)

I should note that of the features I’ve discussed, this is likely the most volatile at the moment. There are a lot of different ideas being thrown around on how this should work and if it should even exist in the language.

My personal opinion is that it should exist. I’ve previously turned to libraries like OneOf to experiment with Discriminated Unions in C#, but was disappointed by some aspects of that library as [I discussed in a prior article](https://killalldefects.com/2019/09/22/oneof-discriminated-unions-in-c/).

Give us support for Discriminated Unions in C# and you’ll begin to see more possibilities emerging that offer a hybrid between functional programming and object oriented programming, as well as improved integration between F# and C#.

## [](#closing-thoughts)Closing Thoughts

As I mentioned earlier, C# is clearly trending towards supporting more functional programming techniques – for those who want to use them.

This trend something that may irritate some, but the ability of .NET and the C# language to adapt over the decades is one of the key reasons I love the language and framework, as [I wrote earlier this year](https://killalldefects.com/2019/09/23/a-love-letter-to-net/).

Again, these features are not guaranteed for C# 9 and are not necessarily in their final form. Stay tuned for more news on their development as we get closer to C# 9’s release.

And, once again, thanks to my friend Calvin Allen for highlighting these technologies in [his blog post](https://www.calvinallen.net/csharp-8-is-old-news-onward-to-csharp-9/) in the [collaborative C# Advent series](https://crosscuttingconcerns.com/The-Third-Annual-csharp-Advent).

I look forward to seeing how these features change over time and what C# 9 will fully bring to the table.

The post [The Dream of C# 9.0](https://killalldefects.com/2019/12/28/the-dream-of-csharp-9-0/) appeared first on [Kill All Defects](https://killalldefects.com/).
