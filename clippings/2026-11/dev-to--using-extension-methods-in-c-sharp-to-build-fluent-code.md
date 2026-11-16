---
url: "https://dev.to/integerman/using-extension-methods-in-c-to-build-fluent-code-4b49"
captured_at: "2026-11-16T00:47:13+00:00"
title: "Using Extension Methods in C# to Build Fluent Code"
domain: "dev-to"
---

Extension methods are an integral part of modern .NET and some of .NET’s best features such as LINQ. Unfortunately, a lot of developers get intimidated by them and don’t understand what’s going on under the surface or how to build new ones. In this article I’ll attempt to demystify extension methods and illustrate how they can be used to build elegant and fluent code.

## [](#the-basics-static-methods)The Basics: Static Methods

In order to discuss extension methods, we have to first discuss static methods.

A static method is simply a method declared with a `static` keyword. This tells .NET that the method operates not on a specific instance basis, but is attached to the class as a whole. Since these methods are static, they do not have access to the state of any specific instance unless it is passed in as a parameter to the method (more on this later).

The `Integer.Parse` method is a fairly well-known static method as is `String.IsNullOrEmpty`.

Over the course of this article we’ll be building out a method for getting information on books, so let’s create a static method that builds a list of books.

[![](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fyuwa4a52o8hpz587zt1o.png)](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fyuwa4a52o8hpz587zt1o.png)

Now, to call out to get our books, we just do something like this:

`var books = Books.GetBooks();`

Pretty simple to use.

## [](#extension-methods)Extension Methods

Next let’s turn our attention to extension methods.

Put simply, extension methods are specially declared static methods that the compiler lets you call on objects matching their signature.

Let me show you what I mean.

Let’s say we have the following static method:

[![](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Ffoj8k8axnhh1z600ao2u.png)](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Ffoj8k8axnhh1z600ao2u.png)

Here we can take any `Book` instance and pass it in to `Books.IsBoring` and get a boolean response.

Let’s change this to be an extension method.

Since extension methods can only be declared in static classes (classes which cannot be instantiated and have only static members), we need to add the `static` keyword to our class.

Now, we declare our `IsBoring` method to be an extension method by adding the `this` keyword to the first parameter like so:

[![](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fa4bgudpvqb1pepjh32rh.png)](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fa4bgudpvqb1pepjh32rh.png)

What the `this` keyword is telling .NET is that `IsBoring` is an extension method and can either be invoked via the static method syntax like `Books.IsBoring(someBook)` or via an extension method syntax like `someBook.IsBoring()`.

Note that the `this` keyword in the extension method syntax can _only_ be used for the first parameter, which is the type or interface that the method extends.

Extension methods are syntactic sugar to have the compiler replace extension method style invocations to static method invocations.

The net result, however, is that extension methods let you _appear_ to bolt on new functionality to other classes or interfaces. This is their primary advantage as extension methods allow you to simplify calling syntax at the cost of obscuring exactly where the method is declared to the casual reader.

Now that we know what extension methods are, let’s look at using them to build a fluent syntax or domain specific language.

## [](#chaining-extension-methods-together)Chaining Extension Methods Together

Let’s say you want to create a book and need to perform a number of operations in order to create a valid book. If you wanted to offer a fairly flexible and readable API, you could use extension methods to create a mini domain specific language (DSL).

In this example, our end goal is to create a book object that is customized based on the values we’ve configured.

Let’s focus on the end result first:

[![](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fp81wquo6tsuqhg0cq1c4.png)](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fp81wquo6tsuqhg0cq1c4.png)

There’s a lot going on there, but maybe not as much as you think.

Let’s start with the `Books.CreateBook` call. This is a static method invocation that takes in a string representing a book’s title and return’s some mystery object.

Let’s call that object a `BookBuilder` and say that it looks something like this:

[![](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fxse4wr4wnvr8reexp32a.png)](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fxse4wr4wnvr8reexp32a.png)

Okay, now this is making maybe a little more sense. That’d mean that our `CreateBook` static method would look something like:

[![](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fb6j5ceoz8p9i7ua3s64r.png)](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fb6j5ceoz8p9i7ua3s64r.png)

Next our example has us calling `WrittenBy`. Well, the `BookBuilder` class doesn’t define that method. In a normal application we’d probably just add the method to `BookBuilder`, but that wouldn’t let us play with extension methods here, so let’s pretend that the `BookBuilder` class is defined by some code we don’t control and can’t modify.

We’ll handle the `WrittenBy` method by adding an extension method:

[![](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fthj7feynbx69bl7gwi3b.png)](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fthj7feynbx69bl7gwi3b.png)

This is a very simple method, but there’s some key things going on here.

First, the method acts as an extension method on `BookBuilder` instances due to the `this` keyword in the parameter signature.

Second, the method is invoked with only **one** parameter specified (e.g. `WrittenBy("Michael Crichton")` because the first parameter is inferred based on the `BookBuilder` you’re invoking the extension method on.

Third, we’re returning the same _builder_ instance we got back. The reason why we return this parameter is entirely to support fluent syntax like we saw in the example earlier, and allow invoking extension methods on the return result of prior extension methods.

The final static class might look something like this:

[![](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fnpa238cuwvq5blfpzcki.png)](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fnpa238cuwvq5blfpzcki.png)

That might not look like the prettiest code you’ve ever seen, but the type of syntax it can create can be incredibly powerful and beautiful.

## [](#lets-talk-about-linq)Let’s Talk about LINQ

Extension Methods were added to the C# language explicitly in order to support **L** anguage **In** tegrated **Q** uery (LINQ) in .NET Framework 3.5.

LINQ is one of my favorite features of C# in terms of developer productivity, and none of that would have been possible without extension methods.

LINQ lets you do things like:

[![](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fn5l5xo6ffmyrrl9vwa52.png)](https://media2.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fn5l5xo6ffmyrrl9vwa52.png)

Maybe this is a little bit of a silly example, but this all works by having extension methods that take in `IEnumerable<T>` or `IQueryable<T>` and use various `Func` signatures to filter, sort, or transform the collection.

Put another way, if you really wanted to, you could write your own version of LINQ with about the exact same syntax using extension methods. Please don’t do this – Microsoft did a great job already – but the capabilities of extension methods allow you to do this.

## [](#closing-thoughts)Closing Thoughts

Hopefully this demystifies some of the magic behind extension methods, LINQ, and static vs instance methods.

I am convinced that extension methods (and LINQ by extension) are one of the key productivity gains of .NET technologies, alongside things like the base class library, the common language runtime, Visual Studio, and generics.

While you may not create or even think about extension methods, they power a lot of what we do in modern .NET and the flexibilty they offer can be a tool for good.

The post [Using Extension Methods in C# to Build Fluent Code](https://killalldefects.com/2020/01/18/using-extension-methods-in-c-to-build-fluent-code/) appeared first on [Kill All Defects](https://killalldefects.com/).
