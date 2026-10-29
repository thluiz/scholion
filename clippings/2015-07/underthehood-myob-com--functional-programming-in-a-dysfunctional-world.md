---
url: "https://underthehood.myob.com/functional-programming-in-a-dysfunctional-world/"
captured_at: "2015-07-24T08:45:59-03:00"
title: "Functional Programming in a Dysfunctional World"
domain: "underthehood-myob-com"
---

# Functional Programming in a Dysfunctional World

Much has been said about the virtues of functional programming (FP) - conciseness, laziness, and concurrency, just to name a few. While it’s certainly still worth rehashing these areas of discourse, in this article I intend to focus on what I think are two of the most compelling benefits of functional programming: correctness and testability.

The idea that FP facilitates correctness and testability does not, by any means, come as a surprise to any reader who is a seasoned functional programmer, so feel free to skip this article if you can code ADTs and applicative functors to get out of a wet paper bag. But if you are an FP skeptic or a closet functional programmer who is struggling to convince your boss and colleagues that your team should adopt FP, then this article is for you.

### Let it be immutable

Have you ever struggled with debugging or extending a codebase where the value of a variable can be modified anywhere in the 500-line class, or worse yet, any of the several super classes that make up the class hierarchy? Did you ever attempt to get to the bottom of an intermittent error that was driving you insane, only to discover much later that a private variable wasn’t synchronized properly? Have you ever spent hours stepping through the lifecycle of an object, going through many different components spread out across the codebase and wished that you had spent all that time solving new problems instead? I know I have, and every time it happens my hair turns a bit more gray.

> Every time it happens my hair turns a bit more gray.

Dealing with mutation is hard. When I constantly grappled with these issues early on in my career, I thought I had serious issues. Perhaps I wasn’t cut out to be a developer. Maybe I should seriously consider a different career. It didn’t help that other developers breezed through similar assignments as if mutation and them were one (don't get any ideas). But then I started reading about functional programming and how everyone was endlessly whining about “side effects”. I thought, hey, maybe it’s not just me. If these intelligent people are also struggling with it, then perhaps it’s a real problem after all.

In functional languages, all variables are immutable. That means once a variable is assigned you can’t modify it. Which is kind of funny because you would think a variable isn’t really *variable* if you can’t change its value. But if you think about it, in algebra and calculus that’s exactly what a variable is: you don’t say `x = 42` and then change your mind and say `x = 43` later on.

If everything is immutable, how do you deal with changing state like database updates and a constant stream of data? After all, software is only interesting and useful if things are dynamic; imagine refreshing a website only to see the same content over and over. The answer is, you copy data. Instead of mutating an object’s attributes in place, you call a function that creates a new object with the updated attributes. This makes the code much easier to reason about since you don’t need to worry about variables mutating in unintended and unexpected ways.

Take for instance the following Ruby code that uses [Virtus](https://github.com/solnic/virtus).

```
class Events < Array  
  <<(event)
    super(event.is_a?() ? construct_event(event)  event)
  

  construct_event(hash)
    hash.key?(:emails) ? EmailEvent.new(hash)  Event.new(hash)
```

Recently I spent hours debugging this code where the *append* (`<<`) method was called with a Virtus object (unexpected) instead of a hash (expected). After consulting a seasoned Ruby developer, I learned that this is a so-called known behavior in which Virtus would perform its ‘magic’ under the hood (no pun intended) when an object is initialized. Because of this unexpected behavior, we had to compensate for it by putting in place a conditional so it would handle an object or a hash accordingly. It’s exactly this kind of *magic* that FP tries to avoid, as demonstrated by the following equivalent Haskell code.

```
data Event = Event String | EmailEvent Event [String] deriving 

appendEvent :: String -> [Event] -> [Event]  
appendEvent status events = events ++ [(Event status)]

appendEmailEvent :: Event -> [String] -> [Event] -> [Event]  
appendEmailEvent event emails events = events ++ [(EmailEvent event emails)]
```

Notice how the *append* functions return a new list that includes the new *Event* instead of mutating the events argument in place. In FP, what you see is exactly what you get.

> Goodbye buggy side effect, hello immutability.

### Performance: the price of immutability?

But if everything has to be copied, doesn’t the performance suck? The short answer is as always, it depends. Even if it were true, I would argue that most software can cope with the additional memory overhead just fine. I would be more wary of introducing bugs because the code is hard to read than get bogged down by micro-optimizations. Moreover, performance bottlenecks are usually caused by blocking network calls and slow database queries anyway, so memory overhead is the least of our concerns. And it goes without saying it’s imperative that we measure things before attempting any optimization as no two systems are created equal.

What’s more, since variables are immutable, it also means they are thread-safe. And thread safety is a godsend if you deal with parallel computations. That entails being able to aggregate large datasets and run calculations in parallel instead of waiting for each chunk of work to complete before running the next. Don’t take my word for it, just ask Guy Blelloch if [functional parallel algorithms](http://www.cs.cmu.edu/~guyb/papers/ICFP10.pdf) are on to something.

But surely the benefits of parallelism are negated by memory inefficiencies caused by all that unnecessary copying? One would be forgiven for buying that, but Chris Okasaki has demonstrated how lazy evaluation in [functional data structures](http://www.cs.cmu.edu/~rwh/theses/okasaki.pdf) can actually yield performance comparable to that of their imperative counterparts. As a matter of fact, many high performance systems used in telecommunications and financial trading are written in functional languages like Erlang, Scala and Haskell, which suggests that concerns about memory overhead due to excessive copying are probably overblown after all.

### Your rights end where lack of proper typing begins

Correctness in functional languages isn’t merely a function of immutability, it also has to do with the fact that most of them support algebraic data types (ADT) and advanced type systems.

Let’s start with ADT. In a typical type system found in mainstream languages like Java, C# and Objective-C, you can easily create types that combine other types either via composition (C is composed of A and B) or inheritance (B:A and C:A). This is called *conjunction*. Where it falls short is a succinct way of expressing *disjunction*, e.g. A = B | C where B <> C. That’s where ADT comes in handy.

For instance, the *Maybe* type in Haskell allows you to express a type that may or may not have a value.

```
Maybe a = Nothing | Just a
```

where *a* can be any valid Haskell type.

(Sure, you can probably use *enums* in mainstream languages to achieve something similar, but enums are ‘dumb’ values and not first-class types. On the other hand, ADT types are rich types with type constructors that can further be composed and decomposed.)

One implication of using *Maybe* is you can bid farewell to the [billion dollar problem](https://en.wikipedia.org/wiki/Tony_Hoare#Apologies_and_retractions) - the dreaded and much maligned null pointer exception (NPE) - forever. Really, it’s just not possible to get an NPE in Haskell, unless of course the program interfaces with C or C++. The compiler forces you to acknowledge that a function may or may not have a value, and you *have* to pattern match it accordingly.

Take for instance a built-in Haskell function to look up a key in a dictionary with the following type signature.

```
lookup :: Eq a => a  -> [(a, b)] -> Maybe b
```

The following is a very contrived example of how you can use it to determine whether a key exists.

```
isKey :: Eq a => a -> [(a, b)] -> Bool  
isKey a b =  (lookup a b) of  
                Nothing -> False
                Just x  -> True
```

The same applies to Scala and F# *Options*, although you have to be wary of using Java and .NET types which are still prone to NPEs. As long as you stick to types defined in those languages, you’re safe.

Another enviable property of ADT is it allows you to define data structures in a more expressive and granular fashion. An oft-repeated example is a tree structure, e.g.

```
 Tree = Empty | Leaf Int | Node Tree Tree
```

which also happens to be recursive: a Node is composed of two Trees!

ADT by itself is extremely useful, but the real jewel of functional languages is the type system. The ML, Haskell and F# type systems are all based on the Hindley–Milner type inference algorithm which uses lambda calculus to intelligently infer types based on usage. Consider the following Haskell code

```
getLength s = length s

foo x y = getLength(x) + y
```

Just by looking at the two methods, we can, without much fuss, figure out that

1. *getLength* takes a *Foldable* (a value that can be ‘reduced’ to a summary value, e.g. a list) and returns an *Int*
2. *foo* takes a *Foldable* and an *Int* and returns an *Int*

The Haskell compiler uses the same heuristics to infer types and impose type constraints on usages of these methods. This is more remarkable when you consider the fact that most type systems rely on type annotations to achieve this, while Hindley-Milner does the same (and more) in the absence of type metadata.

Of course you can take this further by explicitly specifying type metadata so the compiler can less ambiguously impose constraints. In fact, you can often figure out what a method does simply by looking at the type annotation. Consider the following Haskell code for instance.

```
treeElem :: (Ord a) => a -> Tree a -> Bool  
treeElem x EmptyTree = False  
treeElem x (Node a left right)  
   | x == a = True
   | x < a  = treeElem x left
   | x > a  = treeElem x right
```

Looking at the first line, you can easily see that the method takes an ‘orderable’ value and a tree of such values and returns whether the value exists in the tree. Not only does the type metadata imposes type constraints (in the form of *Ord*), it also serves as documentation for the method.

So, what does this all mean? Well for one, the expressiveness of ADT enables simpler data structures that do more with much less code. Simpler code often translates to less bugs as there’s less code to read, modify, test and execute. What’s more, the use of advanced type systems allows you to take full advantage of intelligent type inference and constraints to catch errors and verify program correctness at compile time. You can essentially just compile the code and go home. Gone are the days when you needed to summon and appease the gods of TDD just to write tests whose sole purpose is to verify whether your code is correct (as in runtime and type correctness).

> As the saying goes - why write tests when you can just use the type system.

### Any friend of testability is a friend of mine

A nice side effect (hmm) of immutability is you end up with pure functions. A pure function is one whose output depends entirely on its input and nothing else. That means for the same input you always end up with the same output. No amount of foreign state or mutable variable can change that.

Having lots of pure functions is a boon to testing. Since the expected result relies completely on the arguments, there’s nothing to mock - no private or global variable, no hidden state, just pure values or functions that get passed into the function.

You might be wondering, what about impure functions? Surely there’s code that feeds on a database or a microservice (you know it), assuming the software actually does something useful. That’s why Haskell has these things called *monads* that, among other things, allow you to separate I/O (impure) functions from pure ones. By leveraging monads, you can easily test pure functions as usual and either mock the component that handles I/O computation or rely on property-based testing.

Which brings me to another killer feature of many functional languages: property-based testing (PBT). While PBT is by no means an exclusive domain of functional languages, it does have deep roots in Haskell in the form of QuickCheck. What sets PBT apart from its traditional unit and integration brethren is its emphasis on defining a set of properties that describe a function and ability to generate a lot of random test cases to attempt to falsify these specifications. This is especially useful if you are concerned about test coverage and effectiveness as PBT allows you to focus on what requirements a function should fulfil while leaving the test cases that cover different permutations and edge cases to the framework.

As an example (taken from Real World Haskell), imagine you have a quicksort function with the following signature.

```
qsort :: Ord a => [a] -> [a]
```

This is how you can go about writing the QuickCheck properties.

```
prop_idempotent xs = qsort (qsort xs) == qsort xs

prop_minimum xs = head (qsort xs) == minimum xs

prop_ordered xs = ordered (qsort xs)  
    where ordered []       = True
          ordered [x]      = True
          ordered (x:y:xs) = x <= y && ordered (y:xs)

prop_permutation xs = permutation  (qsort xs)  
    where permutation xs ys =  (xs \\ ys) &&  (ys \\ xs)

prop_maximum xs =  
    not ( xs) ==>
        last (qsort xs) == maximum xs

prop_append xs ys =  
    not ( xs) ==>
    not ( ys) ==>
        head (qsort (xs ++ ys)) == min (minimum xs) (minimum ys)
```

As you can see, thinking about properties of quicksort not only allows you to exhaustively test the code, it also helps to design and document it in terms of its characteristics: sorting it once should yield the same result as sorting it twice, the head should be the minimum, the tail should be the maximum, and so on.

### Correctness and testability are not an option

To summarize, if your manager or development lead has doubts about going functional, just tell them that not only does FP allow you to do more with less code, it also significantly improves quality by promoting software correctness and aiding testability. Tell them how you can save the organization [one billion dollars](http://memecrunch.com/meme/1JQEN/one-billion-dollars/image.jpg) by ridding your codebase of null pointer exceptions. And when you consider 80% of development effort is spent on maintenance, the benefit that you reap for adopting a functional language becomes exceedingly apparent. In fact, one would be hard-pressed to argue against it. I know I would.

If you would like to experiment with FP in your day-to-day work but reckon that going the whole nine yards by adopting a functional language is too radical, you can start by writing functional-style code and start thinking functionally. For instance, you can try making as many variables as possible immutable. In fact, many mainstream languages have a way of creating immutable variables: *readonly* in C#, *final* in Java, *let* in Swift, *@Immutable* in Groovy, etc. Another thing you can try is create a clear separation between pure and side effecting code. Depending on the type of software you’re developing, you can implement the [ECS](https://en.wikipedia.org/wiki/Entity_component_system), [CQS/CQRS](https://en.wikipedia.org/wiki/Command%E2%80%93query_separation) or [anemic domain model](https://en.wikipedia.org/wiki/Anemic_domain_model) patterns. Once you’ve done that, you can decide for yourself if going functional actually improves the readability, testability and quality of your code.

Here's a related article on [Functional Programming in Groovy for Android](https://underthehood.myob.com/is-your-android-code-groovy-baby/)

###### References

Real World Haskell - <http://book.realworldhaskell.org/read/>   
Learn You A Haskell - <http://learnyouahaskell.com/chapters>

Cover image by [woodleywonderworks](https://www.flickr.com/photos/wwworks/), via [Wikimedia Commons](http://commons.wikimedia.org/wiki/File%3AUnofficial_JavaScript_logo_2.svg)
