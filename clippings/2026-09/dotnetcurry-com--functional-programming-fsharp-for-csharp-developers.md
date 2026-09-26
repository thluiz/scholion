---
url: "http://www.dotnetcurry.com/csharp/1384/functional-programming-fsharp-for-csharp-developers"
captured_at: "2026-09-27T00:34:30+01:00"
title: "Functional Programming (F#) for C# Developers"
domain: "dotnetcurry-com"
---

Functional programming seems to be gaining popularity recently!

The functional programming language for .NET framework is F#. However, although C# is an object-oriented language at its core, it also has a lot of features that can be used with functional programming techniques.

![](https://www.dotnetcurry.com/images/csharp/fsharp/fsharp-csharp.png)

You might already be writing some functional code without realizing it!

> Are you keeping up with new developer technologies? Advance your IT career with our Free Developer magazines covering C#, Patterns, .NET Core, MVC, Azure, Angular, React, and more. [**Subscribe to the DotNetCurry (DNC) Magazine for FREE**](https://www.dotnetcurry.com/magazine/) and download all previous, current and upcoming editions.

## Functional Programming Paradigm

Functional programming is an alternative programming paradigm to the currently more popular and common, [object-oriented programming](https://www.dotnetcurry.com/software-gardening/1125/object-oriented-programming-oops).

There are several key concepts that differentiate it from the other programming paradigms. Let’s start by providing definitions for the most common ones, so that we will recognize them when we see them applied throughout the article.

The basic building blocks of functional programs are **pure functions**. They are defined by the following two properties:

*   Their result depends solely on the arguments passed to it. No internal or external state affects it.
*   They do not cause any side effects. The number of times they are called will not change the program behavior.

Because of these properties, a function call can be safely replaced with its result, e.g. to cache the results of computationally intensive functions for each combination of its arguments (technique known as memoization).

Pure functions lend themselves well to **function composition**.

This is a process of combining two or more functions into a new function, which returns the same result as if all its composing functions were called in a sequence. If ComposedFn is a function composition of Fn1 and Fn2, then the following assertion will always pass:

`Assert.That(ComposedFn(x), Is.EqualTo(Fn2(Fn1(x))));`

Composition is an important part of making functions reusable.

Having functions as arguments to other functions can further increase their reusability. Such **higher-order functions** can act as generic helpers, which apply another function passed as argument multiple times, e.g. on all items of an array:

`Array.Exists(persons, IsMinor);`

In the above code, IsMinor is a function, defined elsewhere. For this to work, the language must support **first-class functions**, i.e. allow functions to be used as first-class language constructs just like value literals.

Data is always represented with **immutable objects**, i.e. objects that cannot change their state after they have been initially created. Whenever a value changes, a new object must be created instead of modifying the existing one. Because all objects are guaranteed to not change, they are inherently thread-safe, i.e. they can be safely used in [multithreaded programs](https://www.dotnetcurry.com/dotnet/1360/concurrent-programming-dotnet-core) with no threat of race conditions.

As a direct consequence of functions being pure and objects being immutable, there is **no shared state** in functional programs.

Functions can act only based on their arguments, which they cannot change and therewith, affect other functions receiving the same arguments. The only way they can affect the rest of the program is through the result they return, which will be passed on as arguments to other functions.

This prevents any kind of hidden cross-interaction between the functions, making them safe to run in any order or even in parallel, unless one function directly depends on the result of the other.

With these basic building blocks, functional programs end up being more declarative than imperative, i.e. instead of describing _how_ to calculate the result, the programmer rather describes _what_ to calculate.

The following two functions that convert the _case_ of an array of strings to lower case, clearly demonstrate the difference between the two approaches:

`string``[] Imperative(``string``[] words)`

`{`

    `var lowerCaseWords =` `new` `string``[words.Length];`

    `for` `(``int` `i = 0; i < words.Length; i++)`

    `{`

        `lowerCaseWords[i] = words[i].ToLower();`

    `}`

    `return` `lowerCaseWords;`

`}`

`string``[] Declarative(``string``[] words)`

`{`

    `return` `words.Select(word => word.ToLower()).ToArray();`

`}`

Although you will hear about many other functional concepts, such as monads, functors, currying, referential transparency and others, these building blocks should suffice to give you a basic idea of what functional programming is and how it differs from object-oriented programming.

### Writing Functional Code in C#

You can implement many functional programming concepts in C#.

Since the language is primarily object-oriented, the defaults don’t always guide you towards such code, but with intent and enough self-discipline, your code can become much more functional.

#### Immutable Types

You most probably are used to writing mutable types in C#, but with very little effort, they can be made immutable:

`public` `class` `Person`

`{`

    `public` `string` `FirstName {` `get``;` `private` `set``; }`

    `public` `string` `LastName {` `get``;` `private` `set``; }`

    `public` `Person(``string` `firstName,` `string` `lastName)`

    `{`

        `FirstName = firstName;`

        `LastName = lastName;`

    `}`

`}`

Private property setters make it impossible to assign them a different value after the object has been initially created. For the object to be truly immutable, all the properties must also be of immutable types. Otherwise their values can be changed by mutating the properties, instead of assigning a new value to them.

The Person type above is immutable, because string is also an immutable type, i.e. its value cannot be changed as all its instance methods, return a new string instance. However this is an exception to the rule and most .NET framework classes are mutable.

If you want your type to be immutable, you should not use any other built-in type other than primitive types, and strings as public properties.

To change a property of the object, e.g. to change the person’s first name, a new object needs to be created:

`public` `static` `Person Rename(Person person,` `string` `firstName)`

`{`

    `return` `new` `Person(firstName, person.LastName);`

`}`

When a type has many properties, writing such functions can become quite tedious. Therefore, it is a good practice for immutable types to implement a With helper function for such scenarios:

`public` `Person With(``string` `firstName =` `null``,` `string` `lastName =` `null``)`

`{`

    `return` `new` `Person(firstName ??` `this``.FirstName, lastName ??` `this``.LastName);`

`}`

This function creates a copy of the object with any number of properties modified. Our Rename function can now simply call this helper to create the modified person:

`public` `static` `Person Rename(Person person,` `string` `firstName)`

`{`

    `return` `person.With(firstName: firstName);`

`}`

The advantages might not be obvious with only two properties, but no matter how many properties the type consists of, this syntax allows us to only list the properties we want to modify as _named_ arguments.

#### Pure Functions

Making functions ‘pure’ requires even more discipline than making objects immutable.

There are no language features available to help the programmer ensure that a particular function is pure. It is your own responsibility to not use any kind of internal or external state, to not cause side effects and to not call any other functions that are not pure.

Of course, there is also nothing stopping you from only using the function arguments and calling other pure functions, thus making the function pure. The Rename function above is an example of a pure function: it does not call any non-pure functions or use any other data than the arguments passed to it.

#### Function Composition

Multiple functions can be composed into one by defining a new function, which calls all the composed functions in its body (let us ignore the fact that there is no need to ever call Rename multiple times in a row):

`public` `static` `Person MultiRename(Person person)`

`{`

    `return` `Rename(Rename(person,` `"Jane"``),` `"Jack"``);`

`}`

The signature of Rename method forces us to nest the calls, which can become difficult to read and comprehend, as the number of function calls increases. If we use the With method instead, our intent becomes clearer:

`public` `static` `Person MultiRename(Person person)`

`{`

    `return` `person.With(firstName:` `"Jane"``).With(firstName:` `"Jack"``);`

`}`

To make the code even more readable, we can break the chain of calls into multiple lines, keeping it manageable, no matter how many functions we compose into one:

`public` `static` `Person MultiRename(Person person)`

`{`

    `return` `person`

        `.With(firstName:` `"Jane"``)`

        `.With(firstName:` `"Jack"``);`

`}`

There is no good way to split lines with Rename\-like nested calls. Of course, With method allows the chaining syntax due to the fact that it is an instance method.

However, in functional programming, functions should be declared separately from the data they act upon, like Rename function is.

While functional languages have a pipeline operator ([|> in F#](https://docs.microsoft.com/en-us/dotnet/articles/fsharp/language-reference/functions/index#function-composition-and-pipelining)) to allow chaining of such functions, we can take advantage of extension methods in C# instead:

`public` `static` `class` `PersonExtensions`

`{`

    `public` `static` `Person Rename(``this` `Person person,` `string` `firstName)`

    `{`

        `return` `person.With(firstName: firstName);`

    `}`

`}`

This allows us to chain non-instance method calls, the same way as we can instance method calls:

`public` `static` `Person MultiRename(Person person)`

`{`

    `return` `person.Rename(``"Jane"``).Rename(``"Jack"``);`

`}`

### Examples of Functional APIs in .NET Framework

To have a taste of functional programming in C#, you don’t need to write all the objects and functions yourself.

There are some readily available functional APIs in .NET framework for you to utilize.

#### Immutable Collections

We have already mentioned, string and primitive types are immutable types in .NET framework.

However, there is also a selection of immutable _collection_ types available. Technically, they are not really a part of the .NET framework, since they are distributed out-of-band as a stand-alone NuGet package **System.Collections.Immutable**.

On the other hand, they are an integral part of .NET Core, the new open-source cross-platform .NET runtime.

The namespace includes all the commonly used collection types: array, lists, sets, dictionaries, queue and stack.

As the name implies, all of them are immutable, i.e. they cannot be changed after they are created. Instead a new instance is created for every change. This makes the immutable collections completely thread-safe in a different way than the concurrent collections, which are also included in the .NET framework base class library.

With concurrent collections, multiple threads cannot modify the data simultaneously but they still have access to the modifications. With immutable collections, any changes are only visible to the thread that made them, as the original collection remains unmodified.

To keep the collections performant in spite of creating a new instance for every mutable operation, their implementation takes advantage of **structural sharing**.

This means that in the new modified instance of the collection, the unmodified parts from the previous instance are reused as much as possible, thus requiring less memory allocation and causing less work for the garbage collector.

This common technique in functional programming is made possible by the fact that objects cannot change and can therefore be safely reused.

The biggest difference between using immutable collections and regular collections, is in their creation.

Since a new instance is created on every change, you want to create the collection with all the initial items already in it. As a result, immutable collections don’t have public constructors, but offer three alternative ways of creating them:

\- Factory method Create accepts 0 or more items to initialize the collection with:

`var list = ImmutableList.Create(1, 2, 3, 4);`

\- Builder is an efficient mutable collection that can be easily converted to its immutable counterpart:

`var builder = ImmutableList.CreateBuilder<``int``>(); builder.Add(1); builder.AddRange(``new``[] { 2, 3, 4 }); var list = builder.ToImmutable();</``int``>`

\- Extension methods can be used to create immutable collections from an IEnumerable:

`var list =` `new``[] { 1, 2, 3, 4 }.ToImmutableList();`

Mutable operations of immutable collections are similar to the ones in regular collections, however they all return a new instance of the collection, representing the result of applying the operation to the original instance.

This new instance has to be used thereafter if you don’t want to lose the changes:

`var modifiedList = list.Add(5);`

After executing the above statement, the value of the list will still be { 1, 2, 3, 4 }. The resulting modifiedList will have the value of { 1, 2, 3, 4, 5 }.

No matter how unusual the immutable collections may seem to a non-functional programmer, they are a very important building block in writing functional code for .NET framework. Creating your own immutable collection types would be a significant effort.

#### LINQ – Language Integrated Query

A much better known functional API in .NET framework is LINQ.

Although it has never been advertised as being functional, it manifests many previously introduced functional properties.

If we take a closer look at LINQ extension methods, it quickly becomes obvious that almost all of them are **declarative** in nature: they allow us to specify _what_ we want to achieve, not _how_.

`var result = persons`

    `.Where(p => p.FirstName ==` `"John"``)`

    `.Select(p => p.LastName)`

    `.OrderBy(s => s.ToLower())`

    `.ToList();`

The above query returns an ordered list of last names of people named John. Instead of providing a detailed sequence of operations to perform, we only described the desired result. The available extension methods are also easy to compose using the chaining syntax.

Although LINQ functions are not acting on immutable types, they are still **pure functions**, unless abused by passing mutating functions as arguments.

They are implemented to act on IEnumerable collections which is a read-only interface. They don’t modify the items in the collection.

Their result only depends on the input arguments and they don’t create any global side effects, as long as the functions passed as arguments are also pure. In the example we just saw, neither the persons collection, nor any of the items in it will be modified.

Many LINQ functions are **higher-order functions**: they accept other functions as arguments. In the sample code above, lambda expressions are passed in as function arguments, but they could easily be defined elsewhere and passed in, instead of created inline:

`public` `bool` `FirstNameIsJohn(Person p)`

`{`

    `return` `p.FirstName ==` `"John"``;`

`}`

`public` `string` `PersonLastName(Person p)`

`{`

    `return` `p.LastName;`

`}`

`public` `string` `StringToLower(``string` `s)`

`{`

    `return` `s.ToLower();`

`}`

`var result = persons`

    `.Where(FirstNameIsJohn)`

    `.Select(PersonLastName)`

    `.OrderBy(StringToLower)`

    `.ToList();`

When function arguments are as simple as in our case, the code will usually be easier to comprehend with inline lambda expressions instead of separate functions. However, as the implemented logic becomes more complex and reusable, having them defined as standalone functions, starts to make more sense.

### Conclusion:

Functional programming paradigm certainly has some advantages, which has contributed to its increased popularity recently.

With no shared state, parallelizing and multithreading has become much easier, because we don’t have to deal with synchronization issues and race conditions. Pure functions and immutability can make code easier to comprehend.

Since functions only depend on their explicitly listed arguments, we can more easily recognize when one function requires a result of another function and when the two functions are independent and can therefore run in parallel. Individual pure functions are also easier to unit test, as all the test cases can be covered by passing different input arguments and validating return values. There are no other external dependencies to mock and inspect.

If all of these make you want to try out functional programming for yourself, doing it first in C# might be an easier option than learning a new language at the same time. You can start out slow by utilizing existing functional APIs more and continue by writing your code in a more declarative fashion.

If you see enough benefits to it, you can learn F# and go all in later, when you already become more familiar with the concepts.

_This article was technically reviewed by_ [_Yacoub Massad_](https://www.dotnetcurry.com/author/yacoub-massad)_._

_This article has been editorially reviewed by_ [_Suprotim Agarwal._](https://www.dotnetcurry.com/author/suprotim-agarwal)

[![Absolutely Awesome Book on C# and .NET](http://www.dotnetcurry.com/csharpbook/images/csharp-book-ad.jpg)](https://www.dotnetcurry.com/csharpbook)

C# and .NET have been around for a very long time, but their constant growth means there’s always more to learn.

We at DotNetCurry are very excited to announce **[The Absolutely Awesome Book on C# and .NET](https://www.dotnetcurry.com/csharpbook)**. This is a 500 pages concise technical eBook available in PDF, ePub (iPad), and Mobi (Kindle).

Organized around concepts, this Book aims to provide a concise, yet solid foundation in C# and .NET, covering **C# 6.0, C# 7.0 and .NET Core, with chapters on the latest .NET Core 3.0, .NET Standard and C# 8.0 (final release) too**. Use these concepts to deepen your existing knowledge of C# and .NET, to have a solid grasp of the latest in C# and .NET OR to crack your next .NET Interview.

**[Click here to Explore the Table of Contents or Download Sample Chapters!](https://www.dotnetcurry.com/csharpbook)**

  

![](http://www.dotnetcurry.com/images/authors/Damir%20Arh.jpg)

Damir Arh has many years of experience with software development and maintenance; from complex enterprise software projects to modern consumer-oriented mobile applications. Although he has worked with a wide spectrum of different languages, his favorite language remains C#. In his drive towards better development processes, he is a proponent of Test-driven development, Continuous Integration, and Continuous Deployment. He shares his knowledge by speaking at local user groups and conferences, blogging, and writing articles. He is an awarded Microsoft MVP for .NET since 2012.
