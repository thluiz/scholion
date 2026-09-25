---
url: "https://softwaremill.com/what-is-functional-programming/"
captured_at: "2026-09-25T20:43:30+01:00"
title: "What is Functional Programming?"
domain: "softwaremill-com"
---

An "orthodox" definition of functional programming (FP) states that it is programming with pure / mathematical / side-effect-free functions. But that's neither practical nor reflects how the term is used daily.

What is functional programming, then? And even if we accept the above definition, what does "programming with functions" actually mean? Let's try to answer.

## "You know it when you see it"

Before jumping to formal definitions, let's look at some code samples. We'll implement the same functionality, but using different styles: one "functional", one not. Based on these, we'll try to identify the traits of a functional programming language and style.

> Bonus: can you identify all the languages used?

### Collections

Let's start with one of the most popular use cases for functional programming, which is transforming collections:

```
const numbers = [1, 2, 3, 4, 5, 6];

const result = numbers
  .map((num) => num * 2)
  .filter((num) => num % 3 === 0)
  .reduce((acc, num) => acc + num, 0);
```

```
const numbers = [1, 2, 3, 4, 5, 6];

let result = 0;

for (let i = 0; i < numbers.length; i++) {
  const doubled = numbers[i] * 2;
  if (doubled % 3 === 0) {
    result += doubled;
  }
}
```

Same functionality, but completely different code! Right away, in the first example, we can see that FP is indeed a programming style on its own, radically different from an imperative or procedural approach.

As you might have guessed, the first snippet represents functional programming. What kind of properties make this code "functional"?

First, the collection is transformed in a **declarative** way, specifying what operations should be performed (`map`, `filter`, `reduce`), instead of how they should be done.

Secondly, the first snippet uses **function application** quite extensively: we apply `map`, `filter`, and `reduce` functions to some arguments. These arguments happen to be functions as well. Hence, we are using **higher-order functions**: functions, which are parameterized with other functions.

Finally, we use **function composition**. The result of `map` is used as an input for `filter`. The result of `filter` is, in turn, used as an input for `reduce`.

On the other hand, the imperative code snippet uses explicit **control flow** (`for` **loops**, `if` **conditionals**) and **mutable data** (`result`). Maybe more importantly (though this might be in the eye of the beholder), because of the procedural, not declarative nature, it's also not immediately obvious what the transformation applied to the incoming array is.

### Collections, continued

Our second example also concerns transforming collections. Let's take a look at the snippets:

```
val menu: List<Meal> = if (vegetarian) {
  entireMenu.filter { meal -> meal.ingredients.all { it.plant } }
} else {
  entireMenu.filter { meal -> meal.ingredients.any { it.meat } }
}
```

```
val dietaryRestriction: (Meal) -> Boolean = if (vegetarian) {
  { m -> m.ingredients.all { it.plant } }
} else {
  { m -> m.ingredients.any { it.meat } }
}

val menu = entireMenu.filter(dietaryRestriction)
```

In both cases, we use tools from the functional programming toolbox (as discussed above). However, the second snippet additionally defines `dietaryRestriction` as a value that is a function.

That is, in functional languages, functions are **first-class** values. Such values can be used as any other value: assigned to variables, passed as arguments, returned as a return value.

In the first snippet, we must write down the (simple, but still) `filter` invocation twice. This **code duplication** is avoided in the second snippet, thanks to functions-as-values.

### Data definition

Collection transformation is one thing, but we've got to define somehow the data structures we later transform. Let's look at a third example, where we create some data: a mapping from persons to addresses. The mapping is then updated, when one of the persons moves, on their birthday:

```
case class Person(name: String, age: Int)
case class Address(where: String, permanent: Boolean)

val chris = Person("Chris", 29)
val friends = Map(
  chris -> Address("Warsaw", permanent = true),
  Person("Nicole", 36) -> Address("Paris", permanent = false)
)

val updatedFriends = friends
  .removed(chris)
  .updated(chris.copy(age = 30),
    Address("Kraków", permanent = true))
```

```
class Person { String name; int age; }
class Address { String where; boolean permanent; }

Person chris = new Person("Chris", 29);
Map<Person, Address> friends = new HashMap<>();
friends.put(chris, new Address("Warsaw", true));
friends.put(new Person("Nicole", 36),
  new Address("Paris", false));

chris.setAge(30);
friends.put(chris, new Address("Kraków", true));
```

We don't have any higher-order functions or functions as first-class values. Still, the first snippet would be considered "functional", while the second—is "imperative". Why is that?

The key is the usage of **immutable** data structures in the 1st listing and of mutable data structures in the 2nd listing. In the first snippet, the `Map`, as well as the `Address` and `Person` classes are immutable. Their instances, once created, cannot be changed. We can only create updated copies of the data structures in question, using functions such as `removed`, `updated`, and `copy`.

Immutable data has a lot of benefits, especially when it comes to sharing data across functions and concurrently running processes. Knowing that a function is simply not able to change the arguments passed to it or that you can safely access some data without synchronization simplifies reasoning about code.

The imperative variant (second snippet) uses **mutable** data structures (`HashMap`, classes with mutable fields). We still call functions to update the data (`put`, `setAge`), but they typically don't return meaningful values (they are `void`, or return `()` / `Unit` values). That is, we call them only for their side effects.

When it comes to the programming style, the consequences of using immutable data structures go further. Because the `copy`, `removed`, and `updated` methods return updated values, we can (and have to) use **function composition** to define subsequent transformations of the `friends` map; e.g., the output of `removed` becomes the input of `updated`.

On the other hand, using side-effectful functions that don't return meaningful values inhibits the usage of function composition and functional programming, which, even if at all possible, is much harder. Instead, we have to resort to a sequence of effectful statements.

That way, we arrive at the next trait of a functional programming style: **limiting the effects** that functions have. Just as above, we have effect-free functions (the _only_ reason to call them, is to obtain their return value) on immutable collections vs. side-effectful functions on mutable collections. By minimizing the effects, we automatically increase the degree to which we can program in a functional style. How far should we take this observation?

### Effects

Talking of effects: they're all around us. Interacting with databases, sending HTTP requests, and launching rockets is a programmer's bread and butter. Let's take a look at code samples from that area:

```
public class RocketLauncher {
  public void launch() {
    checkFuelLevel();
    initializeNavigation();
    performSystemCheck();
    igniteEngine();
    System.out.println("Success!");
  }
}
```

```
launchRocket :: IO ()
launchRocket = do
  checkFuelLevel
  initializeNavigation
  performSystemCheck
  igniteEngine
  putStrLn "Success!"
```

```
launchRocket : '{IO}
launchRocket _ =
  checkFuelLevel
  initializeNavigation
  performSystemCheck
  igniteEngine
  printLine "Success!"
```

Once again, the functionality is the same. When we read all three snippets, we think about the code in a similar, imperative way: "To launch a rocket, I first need to check the fuel level, then initialize the navigation, check the systems, and finally ignite the engine. Then I can let the world know of yet another successful launch". So, on a meta-level, these all express the same line of thought. But on a programming level, they are entirely different!

The first snippet can be described as "plain old imperative programming". We call a function, it **immediately** performs a series of (side) effects, and we carry on.

The second snippet, however, represents **effects as values**. The `checkFuelLevel`, `initializeNavigation`, etc. functions only create & return values, which are **descriptions of computations**. Representing effects as values is used as a tool to create effect-free functions.

These values are then composed into a single larger description, which sequences the nested descriptions, using the `do`\-notation (a shorthand for invoking a series of `IO.flatMap` higher-order functions). The effects are only performed when a top-level interpreter evaluates this description (which might occur once, multiple times, or never). That way, the definition of effectful computations is separated from their evaluation.

We won't delve into a detailed discussion on the pros and cons of constraining effects that way, which would involve discussing control monads, laziness, etc.—that's already well covered by the Internet. It will suffice to say that (at least some) functional languages offer a way of representing effects as values and lazily evaluating them.

In the previous section, we stated that functional style benefits from minimizing the effects a function might have as much as possible, but we take this to the limit here. No effects are allowed at all. Such a radical approach has benefits: we can go 100% functional. However, it also has significant costs: runtime and cognitive and syntactical overheads due to the pervasiveness of side-effects in real-life codebases.

The third snippet demonstrates something of a middle-ground: running effectful computations requires an _ability_, which is part of the function's type. You can take an imperative perspective on such code, where effects are evaluated immediately if the ability is in scope. Alternatively, you can consider all functions requiring abilities as lazy and hence effect-free, as they require an ability for the effects to happen.

### Composing programs

Let's see how we can compose bigger programs from smaller pieces:

```
var order = Order.Parse(request); // might throw
order.Validate(); // might throw
order.CalculateTotal();

if (request.LoyalCustomer)
{
  order.SetLoyal(true);
  order.ApplyDiscount();
}

order.CalculateTax();

var invoice = new Invoice(order.Total, order.Tax);
```

```
parse_order request (* returns a Result *)
  |> Result.bind validate_order
  |> Result.map (fun order ->
    create_invoice
      (apply_discount (calculate_total order) request)
      (calculate_tax order))
```

We've got two examples of composition here. First, we want to compose the parsing and validation of an order, both of which might fail. The first example does it in an effectful way by throwing exceptions. The second is effect-free: it represents errors as values, using a `Result` data type (other languages also use `Either` for that purpose). In general, representing **concepts as values** is something that is commonly encountered in functional languages.

Secondly, we want to compose a number of functions to define the invoice-calculating logic. The first snippet performs this using imperative steps (a sequence of **statements**), mutable data, and **side-effecting functions**.

In the second snippet, the `apply_discount`, `calculate_total`, etc. functions don't mutate data or have other effects; they only perform calculations based on their inputs and return some values. We use **function composition** of **effect-free** functions, using **expressions** which yield **immutable data**. These are the same traits we identified when looking at data definition. Quite obviously, that corresponds to FP.

### Data & behavior

Finally, we'll (shallowly) examine the relationship between object-oriented and functional programming. They can co-exist (as exemplified by F# and Scala), but they do sometimes offer different answers to the same question.

```
interface Shape { double area(); }

class Square implements Shape {
  private double side;
  Square(double side) { this.side = side; }

  double area() { return side * side; }
}

class Circle implements Shape {
  private double radius;
  Circle(double radius) { this.radius = radius; }

  double area() { return Math.PI * radius * radius; }
}
```

```
enum Shape {
  Square { side: f64 },
  Circle { radius: f64 },
}

fn area(shape: &Shape) -> f64 {
  match shape {
    Shape::Square { side } => side * side,
    Shape::Circle { radius } => std::f64::consts::PI * radius * radius,
  }
}
```

The object-oriented answer to "how to handle code & data" is to **combine** them: that's what encapsulation is all about. The data is hidden from the users of abstractions and can only be manipulated by the methods available on the object. Often, this goes hand-in-hand with mutability. Encapsulating data might be the right thing to do, but it's not the only possibility.

The alternative FP answer is to **separate data and behavior**. We define the data structures without any behavior attached (which is specified using functions). Data is often immutable (as we mentioned earlier), and most, if not all, FP languages have built-in support for **algebraic data types** (ADTs) and **pattern matching**. In the second snippet above, `Shape` is an enum—a coproduct—with two variants—`Square` and `Circle`—both of which are structs (products) with a single field.

ADTs are a practical, flexible, and type-safe way of defining immutable data structures. Along with functions, they are the basic building blocks of functional programs.

### Traits and non-traits of functional programming languages

We might summarize what we've discovered so far with a "checklist" of traits that a programming language might have. Each such trait contributes to considering a language as functional or at least allowing programming in a functional style. This goes along a list of non-traits, which might help us identify imperative or procedural languages:

Traits of "functional" approach

Non-traits of "functional" style

Function composition

Imperative steps

Higher-order functions

Loops, conditionals

Functions as first-class values

Code duplication

Effect-free functions

Side-effecting functions

Effects as values

Immediate effects

Expressions

Statements

Immutable data

Mutable data

ADTs & pattern matching

Classes, inheritance

Data & behavior separate

Data & behavior combined

Now that we've built some intuition and discussed the practical side of things—which characteristics of programming languages are perceived as "functional"—let's turn to theory and formal definitions.

## A theoretical take on FP

In our quest to find out and understand what Functional Programming is, an obvious first reflex is to check out [Wikipedia](https://en.wikipedia.org/wiki/Functional_programming). The article is quite elaborate, but let's focus on the first paragraph, which holds the definition:

> a paradigm where programs are constructed by applying and composing functions

And that's it—it goes along with what we've discovered so far. If we want to use function application & composition as the _primary_ tool to construct programs, we'll quickly need **higher-order functions** and functions as **first-class values**. Otherwise, we won't be able to use this programming style efficiently.

As a result, a functional program is a tree of function applications. On the one hand, this has a declarative flavor, where we specify the "what" over the "how" (however, that distinction is often blurry). Declarativeness also means that the behavior of our program is defined without explicit control flow constructs, or at least that they are used less frequently. On the other hand, we end up working with **expressions**—another trait of functional programming, that we've seen in the examples.

Note that when we mention "functions as first-class values" or "higher-order functions" as necessary features of a language, we mean that these have a possibly light-weight syntax, and that usage of these constructs is ergonomic; mere semantic possibility to "hack around and define a higher-order function" does not suffice.

### But what's a function?

The above definition has one weak point. What is, actually, a function? Here, we can take two perspectives. The first is to follow the `function` link on Wikipedia, where we can find out that:

> a function is a callable unit of software with a well-defined behavior which can be invoked multiple times

The second perspective is for the more mathematically inclined. We know very well that a function `f: D → C` is a relation such that for each `x ∈ D`, there's _exactly one_ `f(x) ∈ C`. Mathematical functions are deterministic and effect-free; their output depends only on their input and nothing else. The state of the world, time of day, weather, and content of the database do not influence the result of a function.

Depending on which function definition we use, we get different flavors of functional programming. If we take the computer-focused one, where functions might have (side)-effects, we get what I'll call **casual functional programming** (a term I just invented, not commonly used—at least not yet).

If we take the mathematical definition, we get **pure functional programming**, a term that is much more widely used and where all functions are effect-free.

Purity is a great and noble goal. However, no widely used language allows us to verify that a function is pure. There's always an escape hatch—even Haskell has `unsafePerformIO`. That doesn't mean that it's not a useful concept, but it might indicate that requiring purity might not be a desirable characteristic of the entire codebase.

### Isn't casual FP just clean code?

But—you'll say—expanding the definition of "casual FP", we effectively say that we want to construct programs by applying and composing callable units of software (which might have arbitrary effects). Isn't it simply programming using small functions? Something that has been advocated as part of [clean code](https://gist.github.com/wojteklu/73c6914cc446146b8b533c0988cf8d29#functions-rules) for a long time?

Yes—refactoring OO spaghetti code to use small methods is a step towards FP. Clean code might be full of FP principles.

And no, if we want to use function composition more often, small methods are not enough. Their shape will have to change drastically as well: instead of mutation and side-effects, we'll want them to return meaningful values, which can be used as inputs to other functions.

Only when further combined with higher-order functions, functions as 1st-class values, ADTs, immutability, an expression-oriented language, limiting (but not necessarily eliminating) effects etc., we'll arrive at casual FP.

![what-is-fp-small-methods](https://softwaremill.com/user/pages/blog/239.what-is-functional-programming/what-is-fp-small-methods.png?g-208c1a3c "what-is-fp-small-methods")

Whether using these FP-traits to create programs is ergonomic and the primary approach (not secondary or merely possible), defines how functional a language can be considered.

### Where FP's value lies

I would argue that most of the value the functional programming style brings comes from crossing the chasm between _imperative/procedural_ styles and _casual FP_. That is, we leverage the traits of FP that we have defined above (functions as 1st-class values, higher-order functions, immutable data, limiting effects) but are not necessarily very strict about it.

The second step, advancing from casual FP to pure FP (effect-free functions, which means all effects as values), might be valuable, but might also provide diminishing returns.

Consider the following three examples:

```
var users = new ArrayList[User]()
for id <- peopleIds do
  users.add(fetchFromDb(id))

var likes = new ArrayList[Response]()
var dislikes = new ArrayList[Response]()
for user <- users do
  val response = sendRequest(user)
  if response.body.likedSciFiMovies.contains("Star Wars")
  then likes.add(response)
  else dislikes.add(response)
```

```
peopleIds
  .map(fetchFromDb)
  .map(sendRequest)
  .map(_.body.likedSciFiMovies)
  .partition(_.body
    .likedSciFiMovies
    .contains("Star Wars"))
```

```
peopleIds
  .traverse: id =>
    fetchFromDb(id)
      .flatMap(sendRequest)
  .map(_.partition(_.body
   .likedSciFiMovies
    .contains("Star Wars")))
```

The first uses an imperative, mutable style rich with control flow constructs like loops. We've got the `fetchFromDb` and `sendRequest` side-effecting methods. The code is "OK", but can we make it better?

Then, the second snippet has the same functionality but is refactored to casual FP. We're using the higher-order `map` and `partition` functions to express the transformation that we want to implement, function composition to chain the execution; `fetchFromDb` and `sendRequest` are still effectful. However, that's expected, given how they are named and what's the functionality that we want to implement.

Finally, the third snippet sees a refactoring to pure FP, where effects are represented as values. Hence, their composition & transformation needs to be done on the value level, which introduces an additional layer, here visible in `traverse` and `map` invocations. Effects are controlled and lazily evaluated; we've got definitions of effects separated from their evaluation, but most of the time, we don't use those features.

A similar sentiment is expressed in a popular talk on FP by Jane Street—who are, as far as I know, the biggest commercial user of OCaml and active FP community members. The talk ["Why FP doesn't matter"](https://www.youtube.com/watch?v=kZ1P8cHN3pY) first introduces some of the concepts that we've talked about above and then explains the features because of which FP _does_ matter for Jane Street:

1.  Correctness: expressive static types and ADTs allow to make illegal states unrepresentable
2.  Dexterity: no boilerplate, static type verification e.g. exhaustiveness checking when evolving data types
3.  Performance: translation of high-level OCaml code to machine code is predictable and relatively easy to understand

Purity and laziness are far down the list—occasionally useful, but not crucial elements of functional programming.

To close the argument on the importance of purity, or lack thereof, I think it's worth keeping in mind that shared mutable state is always going to be there. I fully agree that eliminating it from the in-memory state of a program is a good programming practice that we should all follow and strive to achieve, whatever our preferred programming style. However, consider a program that executes two processes concurrently:

```
// thread 1
writeToDatabase(user.copy(age = user.age + 1))

// thread 2
readFromDatabase(userId)
```

Whatever approach we take to represent these effectful functions—using a monad, immediate effects, or abilities—when reading the code, we still have to keep in mind that upon execution, some global mutable state (in the database, in that case) is going to be mutated.

The state that our code manipulates is not only what's in the memory, such as global variables. (Which, once again, we should avoid using! Don't make life harder than it is.) But there's also the database, the filesystem, and a plethora of external services, where each POST/PUT call causes a mutation in the broadly understood "state of the world", of which the service that we are writing is a part.

There's no escaping from mutating the global state—sorry!

### Other definitions of FP

As we could expect, many other definitions of FP circulate in the virtual world. Since AI is taking over anyway, let's see what it has to say:

![what-is-fp-chat-gpt](https://softwaremill.com/user/pages/blog/239.what-is-functional-programming/what-is-fp-chat-gpt.png?g-208c1a3c "what-is-fp-chat-gpt")

ChatGPT focuses on purity, immutability, and higher-order functions, which is very similar to our findings so far. Maybe purity will go down the list after this article is included in the training set; we'll see!

What about StackOverflow? There are a couple of related questions, but let's examine the one that considers [FP and non-FP programming](https://stackoverflow.com/questions/24279/functional-programming-and-non-functional-programming). The accepted answer involves functions as first-class values and immutability, no surprise here.

![what-is-fp-so1](https://softwaremill.com/user/pages/blog/239.what-is-functional-programming/what-is-fp-so1.png?g-208c1a3c "what-is-fp-so1")

There's also another answer, which goes along the casual vs. pure distinction we've made above. If the answer's historically correct, casual FP was there first, only later taken over by Haskell's emphasis on purity!

![what-is-fp-so2](https://softwaremill.com/user/pages/blog/239.what-is-functional-programming/what-is-fp-so2.png?g-208c1a3c "what-is-fp-so2")

Talking of history, we have to mention the [Why Functional Programming Matters](https://www.cs.kent.ac.uk/people/staff/dat/miranda/whyfp90.pdf) paper by John Hughes—by now probably considered a classic. The definition used in the paper at first glance talks only about function composition & application:

![what-is-fp-hughes](https://softwaremill.com/user/pages/blog/239.what-is-functional-programming/what-is-fg-hughes.png?g-208c1a3c "what-is-fp-hughes")

However, upon further reading, it's clear that the functions in the paper are the mathematical variant. That is, no side-effects and mutation: pure FP. The paper presents higher-order functions and laziness as two new kinds of "glue" that allow writing modular programs, comparing this to how structured programming improved over `goto`s. We've also already indirectly referenced John's paper before when discussing the Jane Street talk, which only partly agrees with the paper's thesis.

Finally, what about the front page of the Internet—Reddit? Indeed, there are a couple of discussions, such as [What even is FP and why do we like it?](https://www.reddit.com/r/functionalprogramming/comments/16ud127/what_even_is_functional_programming_and_why_do_we/) (do we?). No memes in the subreddit, but there's one answer that I particularly like:

![what-is-fp-reddit1](https://softwaremill.com/user/pages/blog/239.what-is-functional-programming/what-is-fp-reddit1.png?g-208c1a3c "what-is-fp-reddit1")

It emphasizes the ergonomic and community aspect of a functional language: not only is it possible to do everything functionally, but it's also the recommended way, going along the **spirit of the language**.

Other often upvoted answers do take a turn towards pure FP:

![what-is-fp-reddit2](https://softwaremill.com/user/pages/blog/239.what-is-functional-programming/what-is-fp-reddit2.png?g-208c1a3c "what-is-fp-reddit2")

## What is FP, then?

Let's try to sum up what we've found out so far in a possibly compact definition of FP:

**Functional programming** is an approach in which a program's logic is primarily expressed by composing functions. In this context, a function is repeatedly callable code with a well-defined interface. Functional programming often uses the following tools and techniques, though not necessarily all of them or all the time:

*   Functions as 1st-class values
*   Higher-order functions
*   Expressions over statements
*   Immutable data structures
*   Algebraic Data Types & pattern matching
*   Effects as values
*   Avoiding shared mutable state
*   Avoiding or limiting effects
*   Separating behavior & data

A **functional programming language** is a language that allows functional programming to be done ergonomically, as witnessed by the standard library, external libraries, and documentation. A language is functional only if FP is the _dominant_ way of constructing programs. FP must be part of the _spirit_ of the language, not just technically possible.

As for the tools & techniques, a good question is whether they are _desirable_ features of a programming language, and to what degree? How functional should our languages be?

Some of these are non-controversial and rather widely accepted as beneficial; others are disputable. None is a silver bullet. Each could be a separate article, and the Internet is full of such materials, so we'll stop here.

Using FP won't make your code magically and universally better. It often will, but not always. Code written in functional style tends to be safer, more readable, more compact, etc. Of course, for some use-cases it might also be worse, and the imperative, mutable version might be the more maintainable one.

## How functional are the languages we use & love?

Using the above characteristics, let's try to introduce a "functionality scorecard": a subjective, hand-wavy scoring of "how FP" some popular languages are. So yes, you do need to take these with a grain of salt, and you're invited to [fiddle with the scores](https://docs.google.com/spreadsheets/d/1K5IKejIUklDv4Kw0KVDo5r7AjobPvhq_TC9n7aDYXhA/edit?usp=sharing) to fix the mistakes I've made.

The categories we'll use for scoring correspond to the characteristics defined above, enriched with a category covering "how functional the standard library is", which aims to reflect if FP is the style for which the language was designed or merely possible.

Here's the table, linked to a Google Sheet, which you can copy and freely adjust:

[![Functionality scorecard](https://softwaremill.com/user/pages/blog/239.what-is-functional-programming/what-is-fp-table.png?g-208c1a3c "Functionality scorecard")](https://docs.google.com/spreadsheets/d/1K5IKejIUklDv4Kw0KVDo5r7AjobPvhq_TC9n7aDYXhA/edit?usp=sharing)

There's a mix of languages, some of which we've used for code snippets above. First, we've got Java. The first association that you might have is with object-oriented, not functional programming, and rightly so. While you can represent functions as values and program in a functional style if you want to, the language and standard library will fight back. Java's standard collections are mutable, and the entire Java ecosystem is built with mutable data structures that encapsulate data within objects. Recently introduced records and pattern matching shift the language towards FP, but it will never be a language where FP is on par with OO, imperative, or procedural styles.

What about Kotlin, then? The language fixes many of Java's problems, starting with syntax, but also offers tools to create immutable data structures. There are tools for writing code in FP style; however, Kotlin is still deeply embedded in Java's ecosystem. The standard library collections are not immutable, and the libraries often have a Java flavor to them. While this provides excellent interop with Java, it also falls short of fixing some of Java's problems.

Continuing the JVM theme, we've got Scala, a language designed to be a hybrid of OO and FP approaches. Since Scala is the language I use most often, I've separated two flavors of Scala that are used today: the direct-style one, corresponding to casual FP, and a pure-FP one. Scala's standard library is entirely functional and, by default, offers immutable data structures. This deeply impacts the style in which Scala libraries are written. Mutable shared state and constraining effects are common in Scala, but still rely on discipline—the language's compiler does not verify it.

Then we've got "the" FP language, Haskell. It ticks nearly all the boxes, offering pure FP, allowing effects to be only defined in terms of the `IO` monad. There are still escape hatches, though (in the form of the `unsafePerformIO` function, which by definition, is unsafe). Haskell explores several interesting ideas in programming, which is both a blessing and a curse, as it's famous for many compiler extensions, effectively creating many different flavors of Haskell itself. However, thanks to that, FP is often pushed towards new frontiers.

Finally, we've got a seemingly unlikely contender: Rust. Can Rust be considered a functional programming language at all? It turns out that, yes, it scores pretty highly on our scorecard. Hence, either Rust is indeed functional, or our scorecard is broken. But, let's take a closer look: functions are first-class values; the default way of modeling data is by using `enum`s and structs (= ADTs); disallowing shared-mutable-state is one of Rust's primary design goals. The tools Rust uses to achieve this are different (ownership tracking vs immutability), but the outcome is not that different. There's an occasional fight with the borrow checker, but you get raw performance and more predictable memory usage in exchange.

![Ranking of languages](https://softwaremill.com/user/pages/blog/239.what-is-functional-programming/what-is-fp-ranking.png?g-208c1a3c "Ranking of languages")

Some languages are obviously functional: Haskell, Scala, F#, and OCaml would fall into this category (it's worth noting that only in Haskell the "default" is that all functions are pure & effects are represented as values). Some languages are obviously not functional: Java and C# are prime examples. Most fall somewhere in between, such as Kotlin and Rust. It's worth keeping in mind that "how FP our code is" should never be the end goal; it's just a set of tools that work well together to let us create better software.

Most of the code we write will use a mix of styles, even within a single function, and that's totally fine.

## Concluding

Functional programming is here to stay. While it hasn't taken over the world, many of today's popular programming languages have at least borrowed some of its concepts. It's good to identify them correctly and grasp how FP is used in the wild. FP is not only programming with pure functions but a broader term, as illustrated by the code samples from the first section.

We've looked closely at Haskell, Rust, Scala, Java, and Kotlin. However, there are also C#, TypeScript, JavaScript, Python, Ruby, and many others—they all have at least some functional aspects, not to mention functional-first languages such as F# or OCaml. These are all languages used in production daily to deliver working software. By using functional programming, we can do so with greater confidence and efficiency.

What matters in FP are the simple things: ergonomic syntax for treating functions as first-class values, higher-order functions, immutable data structures, ADTs, and a functional standard library. That's why most of the value of FP lies in the "casual" variant and, hence, is accessible to a broad audience.

If your language offers FP as the most ergonomic and practical style, leveraging it throughout the language, standard library, and community—great! If not, there's also significant value to be delivered by functional programming.
