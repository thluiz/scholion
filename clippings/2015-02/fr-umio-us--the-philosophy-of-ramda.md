---
url: "http://fr.umio.us/the-philosophy-of-ramda/"
captured_at: "2015-02-27T20:20:11-03:00"
title: "The Philosophy of Ramda"
domain: "fr-umio-us"
---

# The Philosophy of Ramda

## The Goal

We're writing [Ramda](https://github.com/ramda/ramda) so we could code in a manner not readily available in Javascript. Given data that looks like this:

```
1. // `projects` is an array of objects that look like this
2. //     {codename: 'atlas', due: '2013-09-30', budget: 300000,
3. //      completed: '2013-10-15', cost: 325000},
4. // `assignments` maps project codenames to employee names, with a
5. // list of objects like these:
6. //     {codename: 'atlas', name: 'abby'},
7. //     {codename: 'atlas', name: 'greg'},
```

we want to write code like this:

```
1. // :: ProjectName (String) -> [EmployeeName (String)]
2. employeesByProjectName
3. propEq'codename'
4. filterassignments
5. 'name'
6. // :: [Project] -> [Project] -- (completed on time)
7. onTime  filterfunction
8. returncompleted <=
9. // :: [Project] -> [Project] -- (completed withing budget)
10. withinBudget  filterfunction
11. return<=budget
12. // :: [Project] -> [Project] -- (on time and within budget)
13. topProjects  converge
14. intersection
15. onTime
16. withinBudget
17. // :: [Project] -> [EmployeeName (String)] -- (who worked on top projects?)
18. bonusEligible
19. topProjects
20. 'codename'
21. employeesByProjectName
22. flatten
23. bonusEligibleprojects//=> ["abby", "bob", "carol", "edie", "dave", "hannah"]
24. // Live version at http://jsbin.com/nekoxi/1/edit?js,console
```

This code is a a "functional pipeline." It is built of modular, composable functions, snapped together to form a long pipe into which we feed the data. Each of those `var` statements represents a function taking a single parameter and returning a result. Each result is passed down the pipeline.

These functions transform the data and pass it to the next one. It is important to notice that *none of the functions mutates its input.*

Ramda aims to make coding like this easier in Javascript. That's what it's for, and our design decisions are driven by that goal. There is only one other substantial concern: *simplicity*. We do mean *simple*, not *easy*. If you haven't seen Rich Hickey's talk "[Simple Made Easy](http://www.infoq.com/presentations/Simple-Made-Easy)", you owe it to yourself to spend the hour. "Simplicity" means that separate concerns are never allowed to become entangled. Ramda strives to hold to that ideal.

## The Mantra

Ramda bills itself as "A practical functional library for Javascript programmers." What does that mean?

In the rest of this essay we'll break that description into parts and discuss what each part means for Ramda.

## For Javascript Programmers

### Somewhat Surprising

Ramda is a library for programmers. It is not meant as an academic exercise. It's for those in the trenches building systems. It has to work, work well, and work efficiently.

We try to make it clear what our functions do, to ensure there are no surprises. Still, some things we do could surprise the more academic users. We're willing to risk that so long as day-to-day programmers understand us. For instance Ramda's `is` function is meant to take the place of functions like `isArray`, `isNumber`, `isFunction`, etc. Ramda's version accepts a constructor function and an object:

```
1. Number//=> true
2. Function//=> false
3. Object//=> true
```

This also works with custom constructor functions. If the prototype chain for `Square` contains `Rectangle`, you can do this:

```
1. RectangleSquare//=> true
```

But this might cause some interesting conniptions for academics:

```
1. Object//=> false
```

Real-world programmers know that this is exactly right. Strings, booleans, and numbers are primitives, but they're not objects. However, academics might insist, since the wrapper type `Number` extends `Object`, in parallel with `Square`/`Rectangle` this should really return `true`. Well, they're free to do so... in their own library. The functions are most useful to working programmers as they are.

### Imperative Implementation

We are not trying to *implement* Ramda functions in a functional manner. Many of the constructs we present, things like folds, maps, and filters can only be done functionally through recursion. But Javascript is not optimized for recursion; we cannot code these features with elegant recursive algorithms. Instead we resort to ugly, imperative `while` loops. We write the nasty code so that users can write the more elegant code. The *implementation* of Ramda should never be considered a guide for how to write functional code.

Although we take inspiration from functional languages such as Haskell and ML and from the functional parts of LISP and its many variants, Ramda is not trying to implement any particular parts of those languages.

Nor is Ramda trying to simply redo the native APIs in a functional manner. It's nothing so mechanical. When we write our [map function](https://github.com/ramda/ramda/blob/a277affd34160c1c4754baef9db4d616f32d9a3d/ramda.js#L1743), we feel no pressure to follow the [ECMAScript spec](http://www.ecma-international.org/ecma-262/5.1/#sec-15.4.4.19) for `Array.prototype.map` nor the precedents set by [existing implementations](http://mxr.mozilla.org/mozilla-central/source/js/src/builtin/Array.js#230). We feel free to define for our library what each function does, how it works, exactly what sorts of parameters it can take, how it does or doesn't modify its inputs (never!), what it returns, and what sorts of errors it might throw. In other words, the API is our own. We do feel constrained by traditions from the functional programming world, but when there are compromises to be made in getting things to work in Javascript, we feel free to make whatever choice seems pragmatic.

## A Library

Ramda is a library, a toolkit, or, in Underscore's phrase, a *toolbelt*. It's not a framework that dictates how you structure your application. Instead it's simply a collection of functions designed to make it easier to work in the composable-function style described earlier. The functions don't dictate your workflow. For instance, you don't have to pass the result of `where` in order to use `filter`.

### Why Not Just Use...

It's inevitable that Ramda will be compared to [Underscore](http://underscorejs.org/) and [lodash](http://lodash.com/); the functions supplied overlap in capability and function names. But Ramda will never be a drop-in replacement for those libraries. Even with a magical parameter-order adjustment mechanism, it would still not be a simple replacement. Ramda has different priorities and focuses on different capabilities. Remember, if those libraries had made it easy to code the way we wanted, there would have been no need for Ramda.

When we started, the main functional programming libraries were:

- Oliver Steele's *[Functional Javascript](http://osteele.com/sources/javascript/functional/)*, which was an incredible
  *tour de force* demonstrating for the first time that one could really
  write functional JS. But it was also a toy, pulling things off with tricks
  one would not want in production code.
- Reg Braithwaite's *[allong.es](https://github.com/raganwald/allong.es)*, the book, was out and the little-known
  library was available. But this library was self-described as a companion
  to Underscore or lodash, and, while it was well-done, it seemed the minimal
  set of code necessary to support the book, not a complete library.
- Michael Fogus's *[Lemonad](https://github.com/fogus/lemonad)* was experimental in outlook, perhaps the
  most interesting of the bunch, based around a number of functions not
  found elsewhere in the JS libraries. But it also seemed mostly a
  playground, and an abandoned one at that.
- And of course the big ones, Jeremy Ashkenas' *[Underscore](http://underscorejs.org/)*, and
  John-David Dalton's *[lodash](http://lodash.com/)*. These were the libraries that had
  shown a great number of Javascript developers not to be afraid of
  functional constructs. They were very popular, and already included many
  tools we wanted.

So why not just use Underscore/lodash? The answer is simple. For the sort of coding we want to do, they got something fundamental wrong: they put the parameters in the wrong order.

It sounds ridiculous, even petty, but it turns out to be *essential* to this style of coding. To build up our simple composable functions, we need tools that work together correctly. One of the most important of these is automatic currying. To curry properly, we must ensure that the parameters likely to change most often -- usually the data -- come last.

The difference is simple. Let's say we had this function available:

```
1. functionreturn
```

and we wanted a function that would give us the total cost of a basket of fruit such as this one:

```
1. basket
2. 'apples' count
3. 'peaches' count
4. 'plums' count
```

Our preference would be to write this:

```
1. reduce
```

And use it like this:

```
1. totalCost  compose pluck'cost'
```

This is what we would like. Note how simple both `sum` and `totalCost` are. With Underscore, writing a totalling function would not be difficult, but it would not be as simple as that.

```
1. function
2. returnreduce
3. totalCost functionbasket
4. returnpluckbasket'cost'
```

Another possibility available in lodash would be something like this:

```
1. function
2. returnreduce
3. getCosts partialRightpluck'cost'
4. totalCost compose getCosts
```

or, skipping the intermediate variable:

```
1. function
2. returnreduce
3. totalCost composepartialRightpluck'cost'
```

While that's closer to what we want, it's still pretty far from the Ramda version:

```
1. reduce
2. total composepluck'cost'
```

The secret sauce that went into Ramda to enable this style is very simple: we put the function parameters first and the data parameters last, and we curry every function.

Let's look at `pluck`. Ramda has a `pluck` function that does much the same thing as the `pluck` functions in Underscore and lodash. These functions accept a string property name and a list; they return a list representing the value of that property name for each item in the input list. But Underscore and lodash ask you to supply your list *first*. Ramda wants it *last*. The difference is significant when you add in currying:

```
1. pluck'cost'//=> function :: [Object] -> [costs]
```

By simply not supplying the list parameter to `pluck`, we get back a new function that accepts a list and `plucks` the `cost` from a newly-supplied list.

To reiterate, just that simple difference, autocurried functions with the data parameter last made the difference between this style:

```
1. function
2. returnreduce
3. total functionbasket
4. returnpluckbasket'cost'
```

and this one:

```
1. reduce
2. total composepluck'cost'
```

This was why we started writing a new library.

### Design Choices

The next question was what sort of library we wanted. We knew for certain that we wanted a simple and unsurprising API. But that still leaves open the question about how broad the API is and how deep.

By the breadth of an API we simply mean how many different sorts of functionality it tries to capture. An API with two hundred functions is much broader than one with only ten. As did most of the other libraries, we set no particular limits on our breadth. We add useful functions without concern that the increased size of the library will bring it crashing down.

The depth of a library measures how many different ways its various functions can be used *individually*. (How they can be combined is an entirely different question.) Here we went in a different direction than Underscore and lodash. Because Javascript does no checking of the number of arguments or of argument types, it's fairly easy to write single functions that have many different behaviors depending on the exact parameters passed. Underscore and lodash use this to make their functions more flexible. For instance, in lodash, `pluck` works not just on lists, but also on objects and on strings. In this sense, lodash is a fairly deep API. Ramda tries to remain an extremely shallow one. Here's why:

Lodash offers this:

```
1. pluck'abc' propertyName
```

This will split the string into an array of single-character strings, then return the array formed by retrieving the specified property from each of them. It's very hard to come up with a reasonable use for this:

```
1. pluck'abc''length'//=> [1, 1, 1]
```

I suppose if you really want an array of `1`'s, one for each character in your string, this code is slightly shorter than my Ramda solution:

```
1. always split'abc'
```

But it's pretty useless, as is the only other property that makes any sense at all:

```
1. pluck'abc'//=> ['a', 'b', 'c']
```

This would be fine if it didn't already exist:

```
1. 'abc'split//=> ['a', 'b', 'c']
```

So operating on strings is not particularly useful. It's probably included because all functions in lodash's "Collections" category should work on arrays, objects and strings ; it's just a matter of consistency. (Disappointingly, [lodash has no plans](https://github.com/lodash/lodash/issues/858#issuecomment-69999131) to expand to other actual collections such as `Map` or `Set`.) We already understand how `pluck` works on arrays. The other type it covers is objects, like this:

```
1. flintstones1
2. 'fred'
3. 'wilma'
4. 'pebbles'
5. pluckflintstones1'age'//=> [30, 28, 2]
```

But I can create an object, `flintstones2` such that this is true:

```
1. isEqualflintstones1 flintstones2//=> true
```

and yet this is false:

```
1. pluckflintstones1'age'pluckflintstones2'age'//=> false;
```

Here's one possibility:

```
1. flintstones2
2. 'wilma'
3. 'fred'
4. 'pebbles'
5. pluckflintstones2'age'//=> [28, 30, 2]
```

The problem is that [according to the spec](http://www.ecma-international.org/ecma-262/5.1/#sec-12.6.4) the iteration order of object keys is implementation-dependent; usually they're iterated in the order they were added to the object.

At the time of this writing, I'd [submitted an issue](https://github.com/lodash/lodash/issues/703) about this behavior. At the very best it will likely be fixed only by documenting the problem. But the problem really is profound. If you're trying to unify list and object behaviors, you are going to run into this sort of problem continually unless you implement a (slow!) uniform order to iterate object properties.

In Ramda, `pluck` works only on lists. It accepts a property name and a list and returns you a new list of the same length. That's it. The API is shallow.

You can see it as a feature or a drawback. Consider lodash's `filter`: It accepts an array, object, or string for its `collection`, a function, object, string, or nothing at all for its `callback`, and an object or nothing at all for its `thisArg`. You're getting 3 \* 4 \* 2 = 24 functions in one! That's either a great deal or it's a lot of complexity distracting you from the one case you really want. You decide.

In Ramda, we think of that style as unnecessary complexity. We find straightforward function signatures essential to the simplicity we maintain. If we need a function to operate on lists and also on objects, we create separate functions. If there is a parameter that we'd sometimes like available, we don't create an optional parameter; we create two functions. This broadens our API, but keeps it uniformly shallow.

### API Growth

There is a danger here we recognize quite well, a danger I can spell with three letters: "PHP". We don't want our API to grow into an unmaintainable monstrosity of inconsistent functions. That's a real threat without compelling guidelines to determine what we should and shouldn't include.

We are working on that; we do know that we wouldn't want to include a possibly useful function simply because it's easy to implement. But if a function seems widely useful, it's a likely candidate for inclusion.

To avoid turning into a PHP-style behemoth, we focus on a few things. First of all, the API is the king. Although we like our implementation to be as elegant as possible, we'll sacrifice a great deal of implementation elegance for even a slight API improvement. We try to adhere to rigid standards of consistency. One example: a Ramda function like `somethingBy` is different from one named `somethingWith` in a standard fashion. As described in [issue 65](https://github.com/ramda/ramda/issues/65), we

> use `*By` for single-property comparisons, whether a natural property
> of the object or a synthesized one, `*With` for a more general function.

Some examples that use these sorts of functions include `max` / `min` / `sort` / `uniq` / `difference`.

## Functional

Javascript is a multi-paradigm language. You can write simple imperative code, Object-Oriented code, or functional code. Plain imperative code is straightforward enough. And there are plenty of libraries to help you work with Javascript as an OO language. But there are far fewer libraries for using Javascript as a functional language. Ramda helps fill that gap.

As mentioned before, we are certainly not the first. Others have approached functional programming (FP) in Javascript with various approaches. To my mind, the most successful of these in terms of integrating the FP world with Javascript was probably [allong.es](https://github.com/raganwald/allong.es). But it is not a popular library, not nearly in the class of [Underscore](http://underscorejs.org/) or [lodash](http://lodash.com/). And it had a different purpose than Ramda; it was designed as a pedagogical tool, a companion to the book.

Ramda is trying something different. It aims to be an actual functional library that is practical for day-to-day work.

We are building this functional library from the ground up, using many of the techniques common to other functional languages, ported in ways that actually make sense for Javascript. We are not trying to bridge any gaps with the OO world, or to copy every feature of every functional language. Actually, we're not even trying to copy over every feature of a single functional language. It's still Javascript, and it inherits Javascript's warts.

### Functional Features

So, then, which parts of the broad world of Functional Programming are we trying to keep, and which ones are out of our scope? Here is an (incomplete) list of Functional Programming's major concerns:

- First-class functions
- Higher-order functions
- Lexical closures
- Referential transparency
- Immutable data
- Pattern matching
- Lazy evaluation
- Efficient recursion (TCO)
- Homoiconicity

The first few are built into Javascript. Functions in Javascript are *first-class* values, meaning that they are values we can reference and pass around just as we do strings, numbers or objects. We also can pass functions as parameters to other functions, and return brand new functions, so Javascript has *higher-order functions*. Because such returned functions have access to all variables that were in scope at the time they were created, we also have *lexical closures* built into the language.

None of the remaining items on the list are automatic in Javascript. Some can be achieved easily, some can be achieved only partially or only with great difficulty, and some are beyond the current abilities of the language.

Ramda tries to ensure that you can manage some of these other concerns by at least not causing problems in your library code. For instance, Ramda does not mutate your input data. Ever. If you use `append` to add an element to the end of a list, you get back a new list with the additional element included. Your original list is unaltered. So, while Ramda does not try to *enforce* immutable client data, it makes it easy to work with immutable data.

On the other hand, Ramda does enforce referential transparency. This is the notion that expressions can be replaced by their values without changing behavior. For Ramda, this means that Ramda stores no internal state from your application nor references any global variables or local state-changing closures. In short, when you call a Ramda function with the same values, you always get the same result.

*Lazy evaluation*, as of this writing, is under consideration for Ramda. Libraries like [Lazy.js](http://danieltao.com/lazy.js/) and [Lz.js](https://github.com/goatslacker/lz) have shown that this is possible; [Transducers](https://github.com/cognitect-labs/transducers-js) offer a way to emulate lazy evaluation. Ramda is working on adding such capacities of its own. But it's a big change and will not happen quickly.

Ramda will also consider adding some degree of *pattern matching*, but it will not be as powerful or as convenient as it is in languages like Erlang or Haskell. We're not looking at macros which would alter the syntax of the language, so at most we might do something like what [Reg Braithwaite described](http://raganwald.com/2014/06/23/multiple-dispatch.html#guarded-functions). But this would be at least some pattern-matching technique.

The other features are beyond the abilities of Ramda. While there are techniques such as trampolining that allow you to gain some of the benefits of recursion without tools that optimize tail-calls, they are too intrusive to be generally useful. So Ramda does not use much recursion internally nor does it offer any help in enforcing *efficient recursion*. The good news is that is scheduled for the next version of the language specification.

And *homoiconicity* -- the property of some languages (LISP, Prolog) that program syntax is expressed in a data structure easily understood and modified within the language -- is far beyond the current abilities of Javascript and well outside even the dreams of Ramda.

### Composability

The goal of Ramda, one of allowing the user to work with small composable functions, is key to all functional programming.

Functional programming is generally concerned with some common data structures, and a wealth of functions that operate upon them. This is how Ramda works.

In the abstract, Ramda works mostly on *lists*. But Javascript does not have a list implementation; the closest analog is the Array. That is the basic data structure Ramda uses. We don't concern ourselves with some of the esoteric possibilities of Javascript arrays. We ignore sparse arrays. If you pass one to Ramda, bad things could happen. You need to pass Ramda lists implemented as arrays. (If this doesn't make sense to you, don't worry; this is the standard way people use Javascript arrays. You have to work to create the the unusual cases.)

Many Ramda functions accept lists and return lists. Such functions compose easily.

```
1. // :: [Comment] -> [Number]
2. userRatingForComments compose
3. pluck'rating'// [User] -> [Number]
4. propOfusers// [String] -> [User]
5. pluck'username'// [Comment] -> [String]
```

Ramda includes also the function `pipe`, which does the same thing but inverts the order; I personally find it more readable:

```
1. // :: [Comment] -> [Number]
2. userRatingForComments
3. pluck'username'// [Comment] -> [String]
4. propOfusers// [String] -> [User]
5. pluck'rating'// [User] -> [Number]
```

But of course composition can be used for any types. If the next function accepts the type the current one returns, everything should be fine.

To make this work, Ramda functions need to be small in scope. It's similar to the [Unix Philosophy](http://en.wikipedia.org/wiki/Unix_philosophy): large tools should be built out of smaller tools, each doing one and only one thing. Ramda's functions are similar. Ideally, this means that the complexity in a system built on these functions is only the inherent complexity of the problem domain, not some incidental complexity added by the library.

### Immutability

It bears repeating that Ramda functions do not modify input data. This is a core tenet of functional programming, and it is central to the way Ramda works. While the functions may mutate internal local variables, Ramda does not mutate any data you pass to it.

This does not mean that everything you use will be cloned. Ramda does reuse what it can. So in functions like `assoc` and `assocPath`, which returns clones of an object with a specific property updated, all possible non-primitive properties of the original are used by reference in the new object. If instead you want a disassociated copy of an object, Ramda supplies `cloneDeep`.

This non-mutation is a hard-and-fast rule for Ramda. Any pull request that involves mutating user data is rejected out of hand. We see this as one of the key features of Ramda.

## Practical

Finally, Ramda aims to be a *practical* library. This is trickier to describe because practicality is like beauty: always in the eye of the beholder. There are forever requests for features that don't fit with Ramda's philosophy, features that are, in the minds of their proposers, clearly practical. Often these functions are useful in their own right, but they still get rejected for not fitting with the Ramda philosophy.

For Ramda *practical* means a few specific things.

### Imperative Implementation

First of all, Ramda's implementation does not follow the elegant coding techniques found in LISP, ML, or Haskell libraries. We use ugly imperative loops rather than graceful recursive blocks. Some of Ramda's authors went down that road once in an earlier library called [Eweda](https://github.com/CrossEye/eweda), and the code is very pretty, but it fails miserably at practical concerns. Many list functions could only handle a thousand or so entries and the performance was abysmal. Javascript is not designed to handle recursion well, and most current engines do not perform any tail call elimination.

The Ramda source code is instead littered with ugly `while` loops.

This means that the implementation of Ramda cannot serve as a model for how to write good functional Javascript. That's too bad. But it is the practical choice for the current crop of Javascript engines.

### Reasonable API

Ramda also attempts to make pragmatic choices about what to include in our API. There has been no attempt to port over any particular subsets of the functions in Clojure, Haskell, or any other functional language, nor do we try to mimic the API of more established Javascript libraries or specifications. We choose functions to use because they demonstrate reasonable utility. They of course also have to fit with our functional paradigm to even be considered, but that is not enough; we have to be convinced they will be used and that they offer value not easily achieved through current functions.

That latter is tricky. There is a balancing act to determine when syntactic sugar is acceptable. Above, we discussed that `compose` has an order-reversed twin named `pipe`. There is an argument to be made that this is wasteful, that we shouldn't clutter our API with such a redundant function. After all,

could be rewritten as

```
1. applycomposereverse
```

But we do choose to include `pipe` and other somewhat redundant functions when they seem

- reasonably likely to be used
- better able to express the users' intent
- simple enough to implement

### Clean and Consistent API

The desire for a consistent API might sound less like a practical consideration and more like a purist's goal. But in fact supplying a simple and consistent API makes Ramda significantly easier to use. For instance, once you're used to Ramda's preference regarding parameter order, you'll very rarely have to consult the documentation to determine how to structure your calls.

Also, Ramda's firm stand against optional parameters helps to make for a very clean API. It's generally quite straightforward what a function does and how to call it.

### Not "What Will Help Me"

Finally, it's often difficult to explain to someone with a suggestion that a user's notion of what is practical has only a little to do with what's practical for a library as a whole. Even if a proposed function would help solve a difficult problem, if the issue seems too narrowly focused or if the solution veers from our underlying philosophy, it's not going to get included in Ramda. While practical is in the eye of the beholder, those beholders looking at the entire library have a privileged point of view, and only those changes that will improve Ramda as a whole will be approved.

## Conclusion: Designed to be Different

Ramda was written because there was no other library that worked the way we wanted to work. We wanted to combine small composable functions on immutable data into simple functional pipelines. This has involved some decisions that seem fairly controversial when Ramda is compared to similar libraries. We're not worried by this. Ramda works well for us, and seems to be [meeting a need](https://github.com/ramda/ramda/stargazers) in the community as well.

We're no longer alone. Since we started, [FKit](https://github.com/nullobject/fkit) has come along with similar ideas. It's a less mature library, and it's still working the same way that [Eweda](https://github.com/CrossEye/eweda) did, attempting to maintain real elegance in the implementation as well as the API; it seems to me likely that they will hit a performance wall. However we can do nothing but wish them well.

Ramda is working hard to stick to it's mantra of being a practical functional library for Javascript developers. We think we're managing it. But we'd [love to hear](https://github.com/ramda/ramda/issues) what you think.
