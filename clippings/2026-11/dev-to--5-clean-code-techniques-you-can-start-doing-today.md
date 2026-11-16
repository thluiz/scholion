---
url: "https://dev.to/patferraggi/5-clean-code-techniques-you-can-start-doing-today-2ifh"
captured_at: "2026-11-16T01:52:46+00:00"
title: "5 clean code techniques you can start doing today"
domain: "dev-to"
---

If you are interested in reading this article in Spanish, check out my blog [The Developer's Dungeon](https://www.patferraggi.dev/blog/2020/mar/5-clean-code-tecnicas/)

Two years ago I started looking for ways to improve my coding skills, until that moment I was all on board with learning the next big thing, experimenting with new technologies constantly, and don't get me wrong, I still do, I am a big believer that you should keep your skills updated, but two years ago I read [Clean Code: A Handbook of Agile Software Craftsmanship](https://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882/ref=sr_1_1?keywords=clean+code&qid=1583780721&sr=8-1) and my career changed forever, I would even dare to say that my view on software changed forever.

After that book, I started really thinking about the code I was producing, how it was an expression of my own self and how important it was for me to take into consideration the quality of the software I was creating.

I am not gonna lecture you on our responsibilities as developers, I will do that on the following article, so let's begin with a little introduction.

* * *

### [](#what-is-clean-code)What is Clean Code?

There isn't only one definition, there are probably as many definitions as developers in the world but a few key personalities in our industry have their own opinion and I am gonna list here the ones I like the most:

> "Clean code always looks like it was written by someone who cares. There is nothing obvious you can do to make it better."  
> \-- Michael Feathers

Michael Feathers is right on point, when you see clean code is code that it has been written by someone who deeply cares about his craft, he/she has considered every possibility, written tests for it and made it easier for the next person working on it.

> Clean code is simple and direct. Clean code  
> reads like well-written prose.  
> \-- Grady Booch

Grady Booch focuses on readability, reading clean code is very easy, expressive and even beautiful. Notice how he didn't mention the writing of code.

> You know you are working on clean code when each  
> routine you read turns out to be pretty much what  
> you expected. You can call it beautiful code when  
> the code also makes it look like the language was  
> made for the problem.  
> \-- Ward Cunningham

This is a great definition, when was the last time you looked inside a method or module and the code was "pretty much what you expected"? it is usually the other way around, weird names, old comments, hidden responsibilities.

> Clean code can be easily read and enhanced by a  
> developer other than its original author. It has  
> unit and acceptance tests. It has meaningful  
> names. It provides one way rather than many  
> ways of doing one thing. It has minimal dependencies, which are explicitly defined, and provides a clear and minimal API. Code should be  
> literate since depending on the language, not all  
> necessary information can be expressed clearly  
> in code alone.  
> \-- Dave Thomas

Dave in comparison with the other authors is much more pragmatic, it clearly states that clean code should be easy to read, should have tests, a good naming strategy among other things.

* * *

This article relates more to the last definition, I am gonna give 5 things you can start doing today to improve your code and start walking the path of "Clean Code"

## [](#1-write-meaningful-names)1\. Write Meaningful Names

> There are only two hard things in Computer Science: cache invalidation and naming things.  
> \-- Phil Karlton

You might be thinking, naming things hard? what is this guy talking about, well naming things is actually pretty hard if put some thought into it, remember what Grady Booch said, "Clean code reads like well-written prose" if you want to achieve that you will have to follow certain constraints and try to name variables, methods, and classes as expressive as you can.

*   Classes and objects should have noun or noun phrase names like Customer, WikiPage, Account, and AddressParser. Avoid words like _Manager_, _Processor_, _Data_, or _Info_ in the name of a class. A class name should not be a verb
*   Methods should have verb or verb phrase names like "postPayment", "deletePage", or "save". Accessors, mutators, and predicates should be named for their value and prefixed with "get", "set"
*   Don't abbreviate names
*   Don't use magic numbers
*   Pick one word for one abstract concept and stick with it. For instance, it’s confusing to have "fetch", "retrieve", and get as equivalent methods of different classes. How do you remember which method name goes with which class? Likewise, it’s confusing to have a controller and a manager and a driver in the same code base. What is the essential difference between a DeviceManager and a Protocol- Controller?
    
*   Use variables or methods to describe expressions  
    

```
if (person.age < 18 || person.driverLicense == null) {
arrest(person);
}

// OR
const isUnderAgeOrNoDriverLicense = pperson.age < 18 || person.driverLicense == null

if (isUnderAgeOrNoDriverLicense) {
arrest(person);
}
```

Enter fullscreen mode Exit fullscreen mode

## [](#2-write-small-functions-classes-and-modules)2\. Write Small Functions, Classes, and Modules

> FUNCTIONS SHOULD DO ONE THING. THEY SHOULD DO IT WELL.  
> THEY SHOULD DO IT ONLY.

I know what you are asking yourself, what do you consider "one thing", generally I consider one thing as Uncle Bob explains it, "One reason to change", if the code inside that function, class or module can change for different reasons, then it is doing more than one thing. The reason we write functions is to decompose a larger concept into a set of smaller steps. If a function is retrieving data, mapping it, composing a different object then all those different responsibilities should be separated into different abstractions.

Doing this also will help to separate the logic for unit testing does components.

This concept is deeply related to the "Single Responsibility Principle" which I will probably look further into in another post 😃

## [](#3-avoid-side-effects)3\. Avoid Side Effects

This is a concept that I am very fan of lately since I have been studying functional programming but basically means that your code should not modify or depend on state outside of its control.

Your function promises to do one thing, but it also does other hidden  
things. Sometimes it will make unexpected changes to the variables of its own class.  
Sometimes it will turn the parameters passed into system globals. In either case, they are devious and damaging mistruths that often result in strange temporal couplings and order dependencies.

As I explained in my article about functional programming that you can read [here](https://dev.to/patferraggi/functional-programming-for-the-object-oriented-developer-part-0-1bgj) you should try to stick as much as possible to "Pure functions", functions that for the same input, always produce the same result, by doing this you will isolate the behavior that produces side effects (because we will want to save to database or call an API eventually) from the code that is "Pure".

## [](#4-dont-repeat-yourself)4\. Don't Repeat Yourself

Also known as the DRY principle, it basically explains that you should avoid duplication.

Duplication may be the root of all evil in software. Many principles and practices have been created for the purpose of controlling or eliminating it. Consider how object-oriented programming serves to concentrate code into base classes that would otherwise be redundant. It would appear that since the invention of the subroutine, innovations in software development have been an ongoing attempt to eliminate duplication from our source code.

I know it pretty obvious but sometimes we don't realize that duplication also comes in the sense of information, not only duplicated code but also by providing multiple ways of doing the same thing.

Without use giving some conscious thought into the ways of implementation we provide, we can very quickly have a class with multiple methods all for similar purposes, all with different implementations where bugs can hide, bugs we will have to fix and code we will have to maintain.

## [](#5-comments-are-lies)5\. Comments Are Lies

This is a controversial one, I usually say that you should not write comments at all. Every time I mention this, people love to criticize me.  
Before you jump to my neck, hear me out.

In general, I believe that comments are unnecessary, we developers use comments as an excuse for not properly making our code understandable. We create a big mess with dirty abstractions, bad names and hidden responsibilities and we try to compensate by writing a code comment.

> A common fallacy is to assume authors of incomprehensible code will somehow be able to express themselves lucidly and clearly in comments.  
> \-- Kevlin Henney

Worst, in some cases comments are indeed lies, they were written ages ago by a developer that no longers works in the team, but no one dares to delete the comment in case it is still important, this way the comment actually gives wrong information about the current implementation of the method.

So I have the following recommendation instead of using comments:

> Explain yourself in code  

```

// Check to see if the employee is eligible for full benefits
if ((employee.flags & HOURLY_FLAG) &&
 (employee.age > 65))


Or this?
if (employee.isEligibleForFullBenefits())

```

Enter fullscreen mode Exit fullscreen mode

Again, in most cases, if you write a comment, that is a signal that you should be focusing on extracting that function, giving it a proper name or using some other refactoring techniques.

But as always, there are some exceptions:

*   If you are writing a public API, code comments could express intent and documentation for some automated tools like [Swagger](https://swagger.io/)
*   If you are writing code that needs to be extremely performant, usually means handling very low-level stuff and using little abstractions, in that case, a code comment can be useful
*   Sometimes there are legal reasons to include comments in our code

## [](#6-write-tests)6\. Write Tests

Wait, didn't you say five? sue me. This one is so important that I am gonna give it to you for free. Still, even though it is key for our industry I am still surprised when people ask me what is the purpose of writing tests.

They tell me stories of how they work on a greenfield project where the code is great so they don't see the benefit. If you don't have tests, then is not a greenfield project anymore my friend, or as Michael Feathers puts it:

> Legacy code is code without tests

Tests will just slow me down, they say.  
I have even worked with people that they decided to comment out all the failing tests in the project so they could meet a deadline with a redesign.

Let me be clear about this, if you don't have tests, you don't know if your code works. If you are pretending you know your code, you are assuming you are delivering the specified product. There is a lot of fear right now in the world because of "Corona Virus", would you use a new vaccine if it hasn't been tested yet? I bet you wouldn't, but you are very comfortable delivering software that it hasn't been properly tested.

That behavior and recklessness had lead to lives and millions of dollars lost. Some examples are:

*   [Knight Capital](https://en.wikipedia.org/wiki/Knight_Capital_Group)
*   [Boeing 737 MAX crashes](https://en.wikipedia.org/wiki/Boeing_737_MAX_groundings)

* * *

This is a topic that is very dear to my heart. Since I read the book, a book I recommend every developer should read, in case you are interested you can read my full list of books [here](https://dev.to/patferraggi/5-books-every-developer-should-read-and-some-extras-377n), I have started looking at my career in a very different way.

> I am a Software Craftsman and I will try to show the love for my craft with every single line of code I write.

It is not an easy task, but I actually have a picture of uncle bob pasted to my monitor judging if I don't write clean code.

[![Uncle Bob](https://res.cloudinary.com/practicaldev/image/fetch/s--8nyi0EC0--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/cz0mxe9v9szchl6baqjj.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--8nyi0EC0--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/cz0mxe9v9szchl6baqjj.png)

If you liked or didn't like my article please let me know in the comments below, if you have any questions you can also comment or contact me on twitter, I would very happy to help you 😃

Lastly, if you really really liked it please share it with others.
