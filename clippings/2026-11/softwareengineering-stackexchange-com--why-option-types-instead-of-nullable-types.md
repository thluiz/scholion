---
url: "https://softwareengineering.stackexchange.com/questions/410724/why-f-rust-and-others-use-option-type-instead-of-nullable-types-like-c-8-or-t"
captured_at: "2026-11-16T05:28:34+00:00"
title: "language design - Why F#, Rust and others use Option type instead of nullable types like C# 8 or TypeScript? - Software Engineering Stack Exchange"
domain: "softwareengineering-stackexchange-com"
---

AFAIK, Option type will have runtime overhead, while nullable types won't, because Option time is an enum (consuming memory).

Why not just mark optional references as optional, then the compiler can follow code execution and find whenever it can't more be null?

Edit: I see I was misunderstood. I understand and agree with the advantages of avoiding null pointers. I'm not talking about arbitrary pointers that accept null. I'm only asking why not use compile-time metadata, like C# 8's nullable reference types and TypeScript with strict null checks, where default pointers can't be null and there's a special syntax (mostly ?) to indicate a pointer that can accept null.

Edit 2:

Also, Some is strange, in my opinion. Implicit conversion would be better. But that a language feature and not relevant.

language-designnull
asked May 27, 2020 at 23:18
Chayim Friedman

Answer by Jörg W Mittag:

The purpose of Null Tracking in general (of which Nullable Types are only one of many different forms), is to somehow regain a modicum of safety (and sanity) in languages that have null references.

If you have the chance to eliminate null references altogether, that is a much better solution since the problems that null references cause simply will not exist in the first place. Sir Tony Hoare has famously said that he considers inventing the Null Reference his "Billion Dollar Mistake", which is actually a quite conservative estimate on the total costs that null references have caused until today. If even the person who invented them considers them a mistake, why would you willingly put them in a language?

C# has them because, well, they probably didn't know any better, and now they can't get rid of them because of backwards-compatibility. TypeScript has them because its semantics are based on ECMAScript's, which has them.

The real beauty of an Option type, though, is that it is isomorphic to a collection that can only hold from zero to one elements. Dealing with collections is one of the most important parts of programming, and thus every language in the world has powerful collections libraries. And you can apply all of the work that has gone into collections also to Option types.

For example, if you want to execute an action with an option, you don't need to check whether it is defined! Every collection library on the planet has a way of iterating over a collection and executing an action for each element. Now, what does "executing an action for each element" mean for an Option? Well, if there is no element, then no action is executed. And if there is one element, then the action is executed once with that element.

In other words, foreach acts exactly like a NULL check! You can just blindly do

mightExistOrMightNot.foreach(println)

and it will print out the value contained in the Option if it exists and do nothing if it doesn't exist. The same applies when you want to perform a computation with the value. Every collections library on the planet has a way of iteration over a collection and transforming each element. Again, for an Option "transforming each element" translates to "transform the value or do nothing". So you can just do

val squared: Option[Int] = mightExistOrMightNot.map(_ ** 2)

Also, collections libraries have ways to flatten nested collections. Imagine you have a long chain of references, each of which could be NULL, and you wanted to access the last reference in that chain. With nested Options, you just write

longListOfReferences.flatten

And if you want to get a value out of an Option, then you can simply write

mightExistOrMightNot.getOrElse(42)

and you will either get the value inside the option if it exists, or a default value of your choosing if it doesn't.

The only reason, really, for you to explicitly check for the existence of an Option is if you want to do something completely different in case the value is missing.

It turns out that Option is actually even more than "just" a collection. It is a monad. Languages like C#, Scala, and Haskell have built in syntax sugar for working with monads, and they have powerful libraries for working with monads. I will not go into details about what it means to be a monad, but e.g. one of the advantages is that there are some specific mathematical laws and properties associated with monads, and one can exploit those properties.

The fact that Java's Optional is not implemented as a monad, not even as a collection, is a significant design flaw, and I think is partially to blame for people not understanding the advantages of Options, simply because some of those advantages cannot be realized with Java's Optional.

There is also a more philosophical reason for choosing an Option type over NULL references. We can call this "language democracy". There is a major difference between those two: NULL references are a language feature whereas Option is a library type.

Everybody can write a library type, but only the language designer can write a language feature. That means that if for my code, I need to handle the absence of values in a slightly different manner, I can write a MyOption. But I cannot write a MYNULL reference without changing the language semantics and thus the compiler (or, for a language like C, C++, Java, Go, ECMAScript, Python, Ruby, PHP with multiple implementations, every single compiler and interpreter that exists, has existed, and will ever exist).

The more the language designer moves out of the language into libraries, the more the programmers can tailor the language (really, the library) to their needs.

Also, the more the language designer moves out of the language into libraries, the more the compiler writers are forced to make library code fast. If a compiler writer figures out some clever trick to make NULL references fast, that doesn't help our hypothetical programmer who has written their own abstraction. But if a compiler writer figures out some clever trick to make Option fast, it is highly likely the same trick will also apply to MyOption (and Try, Either, Result, and possibly even every collection).

Take Scala, for example. Unfortunately, because it is designed to interoperate and integrate deeply with the host environment (the Java platform, the ECMAScript platform, there is also an abandoned CLI implementation), it has null references and exceptions. But, it also has the Option type which replaces the former and Try which replaces the latter. And Try first appeared in a library of helpers released by Twitter. It was only later added to the standard library. Such innovation is much harder to do with language features.

I can write my own Scala Option type, and I don't need to change the compiler for it:

sealed trait Option[+A] extends IterableOnce[A]:
override def iterator: Iterator[A]
override def knownSize: Int

def isEmpty: Boolean
def getOrElse[B >: A](default: => B): B
def foreach[U](f: A => U): Unit
def map[B](f: A => B): Option[B]
// … and so on

final case class Some[+A](value: A) extends Option[A]:
override def iterator = collection.Iterator.single(value)
override val isEmpty = false

override val knownSize = 1
override def getOrElse[B >: A](default: => B) = value
override def foreach[U](f: A => U) = f(value)
override def map[B](f: A => B) = Some(f(value))
// … and so on

case object None extends Option[Nothing]:
override def iterator = collection.Iterator.empty
override val isEmpty = true

override val knownSize = 0
override def getOrElse[B](default: => B) = default
override def foreach[U](f: Nothing => U) = ()
override def map[B](f: Nothing => B) = None
// … and so on

@main def test = Some(23).foreach(println)

Try it out here.

Answer by Kain0_0:

NULL is Overloaded.

NULL simultaneously means:

This variable has not been initialised
This variable has been initialised, but does not point to a valid object, and as such is invalid
This variable has been initialised, but does not point to a valid object, and this is perfectly valid
This variable has been cleared and should never be used again
This is the magic third logic value

I'm quite likely missing a few definitions.

So which meaning does this NULL represent?

The Solution

Well that depends on the meaning being ascribed to NULL.

Optional works in the sense of knowing the state of initialisation, and that not being initialised is valid.

A NullObject works in that it conforms to an interface a can be used anywhere the normal object can be while doing some sort of default "nullish" behaviour.

A Trinary Logic Value works best when NULL is the third wheel in a logic system.

There are other solutions, but there isn't any reason to favour one solution over another across the board.

Language Support

At this level it boils down to how the type system is formulated.

Some systems prefer to have some relatively complex primitives. Usually these primitives are reflections of either an historical implementation, or of some underlying platform constraint. In the case of C# it inherited much of is syntax and semantic style from C/C++/Java. This is reflected in the fact that all object references are default nullable, and all values are default non-nullable.

In the case of C# the language, the type system is sufficiently complex to support an Optional type allowing value types to gain a nullable state, but there isn't a trivial way to remove nullability from the object references.

Some systems prefer to have very simple primitive types, and rely on a powerful type composition system to create the desired behaviours. In these languages a C# nullable Reference might look like def cs_reference(T) => NULL | T. The Optional pattern makes more sense though in these languages: def Option(T) => T[0..1]. Its an array/list/sequence of 0 or 1 element.

Using a sequence/array concept leverages our understanding of empty, and has one element. Its directly compatible with anything that accepts the sequence/array concept. And its recomposable within the type system T[0..1][0..1]. Where as cs_reference isn't cs_reference(cs_reference(T)) == NULL | T.

Answer by JacquesB:

Much of the angst over nulls are due to languages where every reference type is nullable by default. But this is not an issue for Typescript or C# 8 so lets disregard that.

There are two basic approaches to how to optional values are represented:

A distinct container type (the Option type) which contain zero or one instances of the actual value.

A union type of the original type with a "sentinel" value, null, which indicate the lack of a value. In Typescript it would be declared as a (actualType | null) type union. (Or shortened as actualType?, but the the explicit union makes it clearer what is going on.)

On the face of it they seem similar, but a significant difference is that containers nest but type unions don't. An option can contain another option as its value, but ((actualType | null) | null) is just the same as (actualType | null).

For example consider a dictionary. The lookup function could return an option: Nothing if the key does not exist, otherwise Some value. This will work with any type of value. If the values in the dictionary are themselves options, the lookup will just return an option where the value (if any) is itself an option.

But what if we instead use null to represent a missing value? Then the lookup function can return a value or a null, but there is no way to distinguish between if the null means the key did not exist or the key did exist but the associated value was null. You lose what could be important information.

Dictionaries are just an example, the problem arise anywhere you have a data-structure with multiple levels of optional elements. Nullable types prevent polymorphism: code can't manipulate data of an unknown type generically, it has to treat nullable and non-nullable types differently.

You can see how C# has to use awkward workarounds in the Dictionary interface. Either it throws an Exception (eww!) if the key is not found, or with TryGetValue() it returns a boolean indicating if the key is found and then the value (or null) on an out parameter. This is pretty ugly and it doesn't scale and is not composable. Option types solves this elegantly, and in a way that is consistent with the rest of the language.

Answer by Karl Bielefeldt:

Nullable types need 3 states in order to be safe and useful:

Null.
Unknown if it is null or not.
Definitely not null. Safe to assign to a non-nullable.

You can only encode two of those states at runtime in a memory pointer. The third state is determined statically at compile time. The compiler determines from the context that you have done a null check, so you can safely treat it as non-nullable inside that context.

Those types of static checks are a relatively recent invention. They were invented in response to options, as a way to pull in the benefits of options without the memory overhead and with a more familiar syntax. So a big part of the reason why more languages don't use statically-checked nullables is because options were invented first.

I think more languages will drift to the statically-checked nullable model over time, but more languages will also drift to the option model, because it has its own advantages.

Options are only one of many types that encode an error/empty state. There is Either, Try, IO, Future, Task, Observable, Validation, and many more, all with their own use cases. It seems very odd to me to give options special treatment in the compiler and leave all the rest in libraries, especially given how common it is to do things like change Option code to Either code when requirements change.

Answer by candied_orange:

Pass me a null and I have to check for null to avoid throwing an exception.

Pass me an option, or an empty collection, or a null object, and I can avoid needing the check. I can use it the same as the other valid values and watch it quietly do nothing.

Use this wisely and it makes code easier to read.

Insist on checking for null and checks clutter code and confusion is caused because now some nulls are meant to cause exceptions and other aren’t.

Some might argue to fail early, but that could have happened before the null even got here. Pass me a null and you have to hope I know what you wanted done with it.

If you believe in fail early and want a process halting exception thrown just throw it. If you don’t need anything cleaned up don’t throw exceptions at me expecting me to silence them and don’t pass me nulls expecting me to check them.

It is possible to design complex systems that don’t even permit the use of null. Instead we design objects that do nothing. If that means consuming a little memory so I can point at the kind of nothing I need then so be it. It’s not like there are that many kinds.

Answer by Manishearth:

AFAIK, Option type will have runtime overhead, while nullable types won't, because Option time is an enum (consuming memory).

This is incorrect. Nullables have exactly the same overhead as option types in Rust, and overall the overhead can go either way depending on the language design. You can have option types with no overhead over nullables, and you can have nullables with overhead over option types.

In Rust, Option<Box<T>> is represented by a nullable pointer. If anything, Option is more efficient than some languages with null because Option lets you represent optionals as stack based value types, whereas in languages with null these optionals need to be heap-allocated so that null can be used.

C# and Typescript are garbage collected and almost everything is on the heap. In that sense, null exists as a state anyway. On the other hand, Rust is not: most values in Rust are not on the heap, so if you wanted to represent a null state you need an additional bit anyway. Which is what Option does, and it optimizes the heap case to use null pointers.

Answer by gnasher729:

Swift has a clever feature in the compiler: If “all bits zero” is not a valid value for type T, then the type optional uses all bits zero to represent nil. The most common use case are optional pointers, of course, followed by optional enums, where no case has all bits zero.

So no space overhead where it isn’t needed. And for something like optional, that cannot be done without overhead.

Answer by Beefster:

In short: Language Pedigree

These languages draw inspiration from Haskell, which is a language built on principles of pure functional design and category theory. Haskell never had null in the first place, with that idea being represented with the Maybe type from the very beginning.

Scala in particular draws a lot of inspiration from Haskell while keeping null purely for interoperability with Java. It uses Option by convention rather than by design. It's a similar story for F#.

Although Rust has null pointers under the hood for bare metal work and foreign function interoperability, it opted to consider working with pointers unsafe, providing the Option type for that purpose in safe contexts. It's nothing more than a design choice that draws inspiration from Haskell. It happens to fit well with Rust's model of integrating lifetimes into its type system, so it seems like a natural design choice.

Reminder: which approach is better varies by situation and preference

Whether Nullables or Options are better is a hotly debated issue among programming language enthusiasts. There is nothing objectively superior about Option types, just certain use cases it happens to excel at. Likewise for nullables; it's situational.

Both Options and Nullable types (with static analysis) solve the same problem, each with their own tradeoffs. In the best case, the two are identical in core function and performance. Options have the benefit of nesting, whereas Nullables are less verbose, have stronger performance guarantees, and tend to come with less complex type systems (potentially saving compilation time).

Answer by Winston Ewert:

Semantically, Options and nullable types are pretty similar. Option<T> and T? work pretty much the same. There are some differences like explicit Some and methods that operate on options. But you indicate that's not what you are interested in. Rather, you seem more interested in the implementation detail of using null pointers rather then some sort of enum.

In a language like Rust, nullable pointers wouldn't work, because Rust doesn't have the indirection of a language like Java.

In Java, an ArrayList<String> is actually a pointer to an ArrayList object which contains a pointer to a String[] which is a pointer to an array of pointers to String objects each of which contains a char[] which is a pointer to an array of chars.

In Rust, a Vec<String> contains a pointer to an array of String each of which contains a pointer to a u8 array.

Consequently, in Rust, it is relatively rare that I want an Option<&T>. Most of the things that I want to have optional aren't references. For example, I often have an Option<String> but unlike in Java, String isn't a pointer to a String, it is a String.

Another way of looking at this, most types in Rust are value types not reference types. Thus nullable versions of those types couldn't be implemented as null pointers. They'd have to implemented as a value with a flag, which is how enums are implemented.

But the Rust compiler does have an optimization on this point. The easy case is Option<&T>, which can be implemented as a null pointer. But as noted, that's not actually very common. But the Rust compiler also looks inside the type to see if there is a non-nullable pointer inside. If compiling Option<String>, it see that String contains Vec<u8> which contains RawVec<u8> which contains Unique<u8> which contains NonZero<*u8>. The compiler knows that NonZero can never contain a null pointer, so it sets that field deep inside the String to null to indicate that the Option is None.

The consequence is that nullable pointer types wouldn't work for a language like Rust. Optional types with compiler optimization does.

Furthermore, this is a relatively obvious optimization. I suspect that all languages with optional types that care about performance will ensure it gets implemented as a null pointer when that is suitable. So, there is no performance reason to shy away from Optional types in favor of nullables.

Answer by gnasher729:

Nullable/nonnull pointers have very complicated semantics.

Let's say function f receives a nullable pointer as an argument, and wants to pass it to a function g which has a nonnull pointer. Obviously only if the pointer is not null. So g(p) gives a compile time error. What about "if (p != nil) g(p)"? That should work, but what is the difference? p is still a nullable pointer. So we need the compiler to be clever enough to know that after the if-statement, p cannot be null. So either you make massive changes in the compiler, or the feature is quite useless.

Now take optionals in Swift. How are they created?

First, there is a very general and very useful feature in Swift: enums with associated values. That means, for every case of an enum the programmer can define what values are stored in the enum value for that case. That feature is used to implement optionals: Optionals are just enums with two cases "none" and "some", where the "none" case has no associated data, and the "some" case does. Optionals are not even part of the language, they are implemented in the standard library.

What about "nil"? nil is a literal, similar to numeric or string literals. So nil is implemented in the compiler. nil is translated to a "NilConvertibleLiteral" (I'm probably spelling this wrong). In the standard library, where Optionals are implemented, the assignment operator and the equality / inequality operators are overloaded for the case that an operand is a "NilConvertibleLiteral" so optional == nil is implemented as "optional case is "none". It's all implemented in the Standard Library, except for the tiny bit in the compiler that knows how to compile "nil" just like it knows how to compile "13" or "3.1415e-20". And comparisons are defined in the standard library for all combinations of optionals and non-optionals: nil optionals are equal to nil optionals and not-equal to non-nil optionals, and two non-nil optionals compare their values. Nothing here in the compiler.

There are two bits of syntactic sugar: First, the ? and ! operators. Declaring a variable as T? or T! makes it an optional T. T?.x returns x if T is not nil, and nil if T is nil. T!.x returns x if T is not nil, and is guaranteed to crash if T is nil. In the example above, "g(p)" wouldn't compile because you can't use an optional where a non-optional is needed, "g(p!)" would compile and crash if p is nil, "if p != nil { g(p!) } cannot crash.

The other bit of syntactic sugar makes all the difference: "if let x = expression { ... } else { ... }. expression must be an optional value. If it is not nil, then the non-optional value is extracted and assigned to x, and the first list of statements is executed; if the expression is nil, the second list of statements is executed (optional). This combines checking whether an optional is nil with creating a non-optional value.

The advantages to nullable and non-null pointers: 1. It can be used for everything. Like a function converting a string to an integer returns an optional Int, so you write "if let i = Int(string) { success } else { failure }, and you can't avoid the test. 2. It has a very clean semantics. 3. It is not possible to avoid nil tests unless you use ! which can lead to a guaranteed crash (and ! means you're asking for it). 4. You actually cannot perform nil tests for non-optional values. Converting Objective-C to Swift I found lots of paranoid nil tests just disappearing.

Answer by Matt Wonlaw:

I'm late to the party here (and everyone is glowingly praising Option) but I'd like to point out that Option comes with significant downsides for maintainability.

This is a re-hash of Clojure author Rich Hickey's discussion of maybe types here: https://www.youtube.com/watch?v=YR5WdGrpoug

While not as bad a untyped null references,

Option types are a 500 million dollar mistake
Starting at the beginning

There are 3 ways of handling nullability:

First: the billion dollar mistake. A reference can be null but this fact is not encoded in the type system.

This is what Java does. Anytime you receive a pointer to something you don't know whether or not it is pointing to an actual object or null.

string foo(String x) {
// this might work or it might throw a null pointer exception
return x.substring(0, 1);
}

// both of these invocations are allowed by the compiler
// however one will fail at runtime.
foo(null);
foo("xyz");

Second: Null references exist but the type system understands that fact and forces the programmer to specify when null is expected and when it is not expected.

This is how TypeScript handles null.

function foo(x: string): string {
return x.substr(0, 2);
}

foo(null); // You cannot write this in TypeScript as x was not declared as being nullable.
foo("sdf"); // works fine

function relaxedFoo(x?: string): string {
if (x != null) // compiler forces you to check for null
return x.substr(0, 1);
return '';
}

relaxedFoo(null); // works fine. We indicated to the compiler that relaxedFoo can handle null references

Third:

The Option/ Maybe type. This "removes" null altogether. The easiest way to think about this is that rather than having a thing that is null or not null, now you have a collection that is empty or not empty. Option has already been discussed at great length in the other answers here.

Option -- the 500 million dollar mistake

So what is so bad about Option that I'd spend an hour on Sunday morning writing about it?

It has to do with program maintenance.

Relaxing Requirements

Take a look at the following code:

function foo(x: string): string {...}

foo requires all callers to always pass a string. But what if tomorrow I want to relax that constraint? Callers can call me with a string or without.

If I used Option I'd end up here:

function foo(x: Option<string>): string {...}

which breaks all callers as Option<string> in not compatible with string.

Callers doing foo('sdf'); must be updated to foo(Option('sdf'));. Pretty problematic if this is a library released publicly.

However, this isn't an issue in TypeScript and other languages that understand null references. In those languages I would do:

function foo(x: ?string): string {...}

?string is a union type of string and null, thus no existing callers break. I can release an update to my library and not break any of its consumers.

foo('sdf'); // requires no change as 'sdf' is allowed in the type union of `null | string`

The same problem with Option also exists in the reverse -- when making return types provide stronger guarantees.

I.e.,

Changing foo(): Option<string> to foo(): string shouldn't be considered a breaking change.

Of course foo(): string to foo(): Option<string> is breaking (and should be breaking) since a new type is added.
