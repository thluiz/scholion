---
url: "http://blogs.perl.org/users/rafael_garcia-suarez/2011/10/why-dart-is-not-the-language-of-the-future.html"
captured_at: "2014-05-01T21:40:44-03:00"
title: "Why Dart is not the language of the future | Rafaël Garcia-Suarez [blogs.perl.org]"
domain: "blogs-perl-org"
---

## Why Dart is not the language of the future

By [Rafaël Garcia-Suarez](http://blogs.perl.org/users/rafael_garcia-suarez/)
on October 11, 2011 11:10 AM

So I've been looking at the Dart language specification recently published by Google (draft version 0.01). So far, I'm not really enthusiastic. Here's my reading notes.

## Class-based OO and Interfaces

At first glance Dart code looks like Java (and nothing's wrong with that, I'm not going to criticize a language based on my idiomatic preferences). The syntax is very similar, with the dot to invoke methods, the curly braces for blocks, the required semicolon to terminate statements, the main() function, the general feeling of verbosity. The familiar classes and interfaces are here. There is only single-inheritance, abstract interfaces being provided instead of full multiple inheritance to solve the diamond inheritance problem.

The spec has even a chapter on factories (static constructors). (Oh my, factories? it's like 1997 and design patterns all over again!) I should note that the integration of popular design patterns at the syntax level is disappointing: design patterns tend to emerge to work around a language design's weaknesses. Embracing them is a bit like admitting a design failure up front.

Let us just regret for the moment that more modern and useful OO paradigms, like roles, are not used here; as we have learned, interfaces are limited, since they do not allow sharing of code, only of method prototypes. But there are much more problems with Dart.

## Feeble Typing

The spec says: *Dart programs may be statically checked. The static checker will report some violations of the type rules, but such violations do not abort compilation or preclude execution.*

Ah; OK. In other words the "static checker" is a lint-type development aid, not a language feature. Worse, that means you can write functioning programs with wrong (and misleading) type declarations, and still run them. Types have no effect whatsoever on your program's semantics.

The lack of type enforcement also implies that the runtime cannot take advantage of the typing information to optimize a running program (for example by pre-resolving method calls). Via some type decoration mechanism, one could have mixed weak and strong typing; instead, it looks like the Dart designers found that type inference was too hard to implement, so they completely gave up on the advantages that typing could have brought to the runtime.

Finally, this weak typing design removes the point of using interfaces at all. Interfaces don't allow to share code; so what's the point in adding them (and having them parsed and compiled in a browser at page loading time) if they are nothing more than a fancy documentation format? Interfaces make sense only in strongly typed languages (like Java), or else you're just doing duck typing like basically every dynamic language, but without the advantages of dynamic languages (runtime addition of new methods, or calling of methods by name, for example).

The design of Dart's OO system is not consistent. I'm calling it feeble typing. It's an unassuming weak typing that can't afford to be strong but does not want to be seen with the weak typing boys.

I understand that Dart is designed to be compiled to fast Javascript. The absence of type checking, in that context, feels like a premature optimisation, and we all know what it is the root of.

I note that Dart also supports function types (describing the whole function prototype, like in C). Their purpose is not clear, since there is apparently no way to manipulate function pointers; the interface Function (apparently used for anonymous functions) does not provide any method at this point. What is the point of function types if they have no runtime existence? Moreover, the fact that named functions and anonymous ("literal") functions are different entities is disturbing.

There are generics, too. Well, I guess that the example of C++ and Java hasn't discouraged the Dart designers. Again I don't see the point of generics without type checking.

## Booleans

Here's a strange thing: the one and only true value is the boolean literal boolean true. Everything else is false. That means that code in if (1) { ... } will never execute, because 1 is a number, not a boolean, and there is no implicit conversion to boolean. You'll need to write if (1==1) instead.

The spec hints that it's because the boolean literals true and false can be autoboxed into objects, and as objects, they would be non-null, thus defined, thus true, if any non-zero value could be true. Looks like a lot of trouble imposed on the programmer for a very minor problem that could have been fixed at the language level by allowing boolean coercion overload, or by disallowing boolean autoboxing. (It is notable that Dart allows operator overloading, but not boolean, string or numeric coercion overloading.)

Another word of warning; the operators === (reference equality), != and !== (inequalities) all return a boolean; but == is not required to do so, because it can be overloaded, and (once again) there is no runtime type enforcement on its return value. Which means that the expression (a==a) might be, in some pathological cases, false. In my opinion, this is not something that should be allowed to happen in a well-designed language.

## Type conversion

There is no implicit type conversion between numeric, string or boolean types. Integers and floating point numbers are distinct types. Objects that provide a toString() method (that should return a string!) can be converted into a string by interpolating them, as in int foo = 42; String bar = "${foo)";. The Math class provides methods to extract numbers from strings (parseInt and parseDouble).

The distinction between string and numbers allows to re-use the addition operator + both for addition and concatenation. However, without strong typing, this will almost certainly prove to be a bad idea. From the specs, it looks like "2" + 2 will be a concatenation, and 2 + "2" a run-time exception (in the absence of implicit conversion from string to number), but experience infirms this: string concatenation happens in both cases (although with a warning in the second one).

## Exceptions

Speaking about exceptions. If we look at the list of standard exceptions, we see a proliferation of classes encouraging exception-based control flow. The programmers, being lazy, will naturally prefer writing catch-all NullPointerException handlers instead of testing whether their objects are null -- because the syntax makes it easier for them. (Constructs like if (a) a.foo(); will not work in Dart, see above.)

Another example: [Ovid](http://blogs.perl.org/users/ovid/) pointed me at the [NoMoreElementsException](http://www.dartlang.org/docs/api/NoMoreElementsException.html), and added: "didn't Java programmers learn years ago that you throw exceptions for exceptional things and not for expected things?"

## Isolates and heavy thread model

From the spec: *Dart code is always single threaded. There is no shared-state concurrency in Dart. Concurrency is supported via actor-like entities called isolates.*

Thus, isolates are a heavyweight thread control model very much like Perl 5's ithreads. That means that they are good for data isolation, but heavy to use and hungry in memory, because spawning a new isolate will imply cloning all the objects and data structures of the running libraries. (By the way, there is no word in the spec on cloning. Apparently Dart does not have the equivalent of Perl's CLONE() method.) There are also "light" isolates, which means that they run in the same thread than the object that created them.

(Isolates are probably good for browser-side security, although the spec do not talk much about that point -- disappointing again, security should have been in mind of the designers from the start, for a JS replacement.)

However, running in a browser is not like running in a server thread, and where Perl 5's ithreads might do their job, isolates are not adapted to web-page programming. Controlling the UI of the browser, with its high level of interactivity, requires a good concurrency implementation for event processing, lazy loading of resources, and animations. Dart is weak on that point: if you want to animate multiple widgets at once in the same HTML page, you'll need one isolate for each one, with all the implied overhead. Likewise if you want to do something while an ajax call is completing, etc.

Isolates communicate via message passing. It's not clear if there is some synchronisation method available in the standard libraries, semaphore-based or other. It's not clear either how the browser events are passed to the program. I need to look at the code examples; the spec is very much formal and not practical at all.

## Security

*Dart is lexically scoped and uses a single namespace for variables, functions and types.* Dart provides private names, which are simply those beginning with an underscore; those names are not accessible outside the library where they are declared.

Dart provides library imports and source file includes. Not much more about it, the spec does not mention any kind of restriction about the places where code can be loaded. I suppose it will be in a future version. When importing a library, one can specify a namespace (or prefix) in which the imported names will be found, to avoid name clashes. It is not clear how Dart deals with second-level imports or recursive imports in this case. However the naming rules are clear and the removal of a global namespace was a good idea.

## Conclusion

The worst of both worlds: Dart fails to provides the advantages of static languages, without compensating by the flexibility of dynamic languages. Nothing has been learned from the dynamic language renaissance of the last ten years; nothing from the functional world; nothing even from the slick concurrency model of Go and its goroutines, also from Google.

So I think it's a step backwards in language design. With Node.js and Coffeescript around, and the programming paradigms they allow, Dart looks already obsolete and inadapted.

- [9 comments](http://blogs.perl.org/users/rafael_garcia-suarez/2011/10/why-dart-is-not-the-language-of-the-future.html#comments)

#### Tagged as:

[dart language design](http://blogs.perl.org/users/rafael_garcia-suarez/2011/10/why-dart-is-not-the-language-of-the-future.htmljavascript:void(0))

## 9 Comments

[![53773d25985c30aa17c4cd84fa0b9e9b.png](blogs-perl-org--why-dart-is-not-the-language-of-the-future/53773d25985c30aa17c4cd84fa0b9e9b.png)](http://robsimmons.myopenid.com/)
[robsimmons.myopenid.com](http://robsimmons.myopenid.com/ "http://robsimmons.myopenid.com/")
| [October 11, 2011 4:27 PM](http://blogs.perl.org/users/rafael_garcia-suarez/2011/10/why-dart-is-not-the-language-of-the-future.html#comment-58945)
| [Reply](http://blogs.perl.org/users/rafael_garcia-suarez/2011/10/why-dart-is-not-the-language-of-the-future.htmljavascript:void(0); "Reply")

I enjoyed your take. I liked the term “feeble typing” so much I renamed [my Dart blog post](http://requestforlogic.blogspot.com/2011/10/incomplete-by-design-thought-on-dart.html), which tries to make many of the same points your “Feeble Typing” section makes X - citing you of course.

[![54974d1b040b5a2191e7c7a9ff6c0347.png](blogs-perl-org--why-dart-is-not-the-language-of-the-future/54974d1b040b5a2191e7c7a9ff6c0347.png)](http://was.id.ly/)
[gizzlon](http://was.id.ly/ "http://was.id.ly")
| [October 11, 2011 6:06 PM](http://blogs.perl.org/users/rafael_garcia-suarez/2011/10/why-dart-is-not-the-language-of-the-future.html#comment-59033)
| [Reply](http://blogs.perl.org/users/rafael_garcia-suarez/2011/10/why-dart-is-not-the-language-of-the-future.htmljavascript:void(0); "Reply")

FYI there's more discussion here:  
<http://news.ycombinator.com/item?id=3098435>

![54974d1b040b5a2191e7c7a9ff6c0347.png](blogs-perl-org--why-dart-is-not-the-language-of-the-future/54974d1b040b5a2191e7c7a9ff6c0347.png)
frenchy
| [October 12, 2011 2:58 AM](http://blogs.perl.org/users/rafael_garcia-suarez/2011/10/why-dart-is-not-the-language-of-the-future.html#comment-59329)
| [Reply](http://blogs.perl.org/users/rafael_garcia-suarez/2011/10/why-dart-is-not-the-language-of-the-future.htmljavascript:void(0); "Reply")

This is a good point of view.

Although I don't agree with everything you say, you are right one point: a PL should be either dynamic and untyped, or fully statically typed.

In the sphere of web programming language, that means either JS and NodeJS (http://nodejs.org) or Opa (http://opalang.org).

[![54974d1b040b5a2191e7c7a9ff6c0347.png](blogs-perl-org--why-dart-is-not-the-language-of-the-future/54974d1b040b5a2191e7c7a9ff6c0347.png)](http://gorwits.me.uk/)
[Oliver Gorwits](http://gorwits.me.uk/ "http://gorwits.me.uk/")
| [October 12, 2011 4:28 PM](http://blogs.perl.org/users/rafael_garcia-suarez/2011/10/why-dart-is-not-the-language-of-the-future.html#comment-60099)
| [Reply](http://blogs.perl.org/users/rafael_garcia-suarez/2011/10/why-dart-is-not-the-language-of-the-future.htmljavascript:void(0); "Reply")

[Programming Language Checklist](http://colinm.org/language_checklist.html)

[![53773d25985c30aa17c4cd84fa0b9e9b.png](blogs-perl-org--why-dart-is-not-the-language-of-the-future/53773d25985c30aa17c4cd84fa0b9e9b.png)](http://robsimmons.myopenid.com/)
[robsimmons.myopenid.com](http://robsimmons.myopenid.com/ "http://robsimmons.myopenid.com/")
| [October 13, 2011 3:50 PM](http://blogs.perl.org/users/rafael_garcia-suarez/2011/10/why-dart-is-not-the-language-of-the-future.html#comment-61382)
| [Reply](http://blogs.perl.org/users/rafael_garcia-suarez/2011/10/why-dart-is-not-the-language-of-the-future.htmljavascript:void(0); "Reply")

Oliver: I don't think "a PL should be either dynamic and untyped, or fully statically typed" is the right lesson to be drawn from this. There's a lot of interesting research that has been done or is being done on languages that integrate static and dynamic type systems, going by names like "gradual typing" or "hybrid typing." This work both shows a lot of promise and is mature enough that ideas could really be incorporated into a production language.

Here, the issue is that they add something which has superficial resemblance to this work but then, because the "type" stuff doesn't actually work right, keeps the *core* language 100% dynamic. Among many other things, this means they "completely gave up on the advantages that typing could have brought to the runtime."

That's not an indictment of languages that mix static typing and flexible, tagged-at-runtime dynamic typing, and in my opinion it would be a real pity if Dart, which is doing something altogether different, discredits the idea of hybrid or gradual type systems prematurely.

[![53773d25985c30aa17c4cd84fa0b9e9b.png](blogs-perl-org--why-dart-is-not-the-language-of-the-future/53773d25985c30aa17c4cd84fa0b9e9b.png)](http://robsimmons.myopenid.com/)
[robsimmons.myopenid.com](http://robsimmons.myopenid.com/ "http://robsimmons.myopenid.com/")
| [October 13, 2011 3:50 PM](http://blogs.perl.org/users/rafael_garcia-suarez/2011/10/why-dart-is-not-the-language-of-the-future.html#comment-61383)
| [Reply](http://blogs.perl.org/users/rafael_garcia-suarez/2011/10/why-dart-is-not-the-language-of-the-future.htmljavascript:void(0); "Reply")

Oops, that was a reply to frenchy, not Oliver.

![54974d1b040b5a2191e7c7a9ff6c0347.png](blogs-perl-org--why-dart-is-not-the-language-of-the-future/54974d1b040b5a2191e7c7a9ff6c0347.png)
Dennis
| [October 26, 2011 3:27 PM](http://blogs.perl.org/users/rafael_garcia-suarez/2011/10/why-dart-is-not-the-language-of-the-future.html#comment-73533)
| [Reply](http://blogs.perl.org/users/rafael_garcia-suarez/2011/10/why-dart-is-not-the-language-of-the-future.htmljavascript:void(0); "Reply")

"Oh my, factories? it's like 1997 and design patterns all over again!)"

and then

"Via some type decoration mechanism, one could have mixed weak and strong typing..."

You mock the use of design patterns then you recommend one - "decoration mechanism"

Which is it - they're useful or they're not ??

![f16417039c430ac3d3bce64823553a1e.png](blogs-perl-org--why-dart-is-not-the-language-of-the-future/f16417039c430ac3d3bce64823553a1e.png)
moru0011
| [December 18, 2013 8:24 AM](http://blogs.perl.org/users/rafael_garcia-suarez/2011/10/why-dart-is-not-the-language-of-the-future.html#comment-1304700)
| [Reply](http://blogs.perl.org/users/rafael_garcia-suarez/2011/10/why-dart-is-not-the-language-of-the-future.htmljavascript:void(0); "Reply")

This post is full of wrong assumptions and misunderstandings.

1. Dart has mix-ins not interfaces
2. Factory constructors. Construction of objects is more than a design pattern, object construction is a core element of a language. Factory methods are a great improvement over the limited “new” statement. Nothing wrong with introducing this at lang level, as it does not prevent other patterns.
3. Concurrency model: is actor-alike. This model is also favoured by many in the Java-VM language camp. A big advantage is that Garbage Collection (a big problem for large enterprise apps) can be done per Isolate separately. It also shines with upcoming 32+ core hardware. Additionally this way applications can be run distributed naturally (just run isolates on different machines). Cloning is missing indeed.
4. Regarding typing: You miss the point that Dart has to compile efficiently to JavaScript, so there are some serious technical limits for the language designers

![54974d1b040b5a2191e7c7a9ff6c0347.png](blogs-perl-org--why-dart-is-not-the-language-of-the-future/54974d1b040b5a2191e7c7a9ff6c0347.png)
Malaidas
| [February 26, 2014 3:40 PM](http://blogs.perl.org/users/rafael_garcia-suarez/2011/10/why-dart-is-not-the-language-of-the-future.html#comment-1325938)
| [Reply](http://blogs.perl.org/users/rafael_garcia-suarez/2011/10/why-dart-is-not-the-language-of-the-future.htmljavascript:void(0); "Reply")

I strongly feel you are missing the pint somewhat here.

the primary use of dart is to bring sanity to scripting web applications, specifically those of moderate to large size and in this it achieves its aims from what I can see. Would I choose it for a desktop application, no, there are a plethora of languages better suited to this. For use in the browser though its a good choice in my opinion. Certainly better than plugins such as Java Applets or Flash etc.

the main stopping point with creating sensible we applications is JavaScript's stupidities. Which are caused of course by its lack of proper OOP support and at an enterprise level its purely prototype approach. Both of which are properly addressed by DART.

Now I take your point about the mixing of static and dynamic types. Personally I prefer (most of the time) to develop with proper static classes, they implement the idea that it is one of the compilers job's to catch static errors such type mistakes, not detailed testing which is for the most part insufficient to catch them all.

however there are many cases where dynamic typing can be easier or more flexible I admit. I'm just not sure that the advantages mitigate the severe risks they bring in a large project. However yes a hybrid approach is even more dangerous I think.

Concurrency and Security: again we come back to tool for purpose. Whatever DART does has to be implementable in pure Javascript. Better Solutions exist but not in a form that can be easily supported within the confines of a browser.

Dart provides proper classes and interfaces etc by their proper definition. This is needed for sanity. It compiles to efficient (runtime wise) code that runs natively within all HTML5 compliant browsers regardless of platform, because it compiles to industry standard JS.

Is it a long term language for the future, probably not yet in its current form, but neither was Java when it first came out. Like all program languages, so long as Google continue to develop it, which is of course an important consideration for choosing it, it will evolve.

I think you are being overly harsh at this point.

Also may I point out that   
1) mix ins and interfaces are completely separate concepts at a conceptual level. An interface is the black box, the point of interaction. The interface should never be related to the code that implements it directly.

2) Design Patterns are a lot more than you are implying. They are a very good idea, regardless of language weakness/strength. They are not patches over this. A Design Pattern facilitates understanding of your code to others, especially when as is the case 90% of the time the coder insufficiently, or ambiguously comments the code and the reader doesn't have a fully detailed design document. Standardisation yes limits creativity but most of the time this is a good thing. Standard ways of doing things also allow for 4th generation tools to be better used which is also a good thing.
