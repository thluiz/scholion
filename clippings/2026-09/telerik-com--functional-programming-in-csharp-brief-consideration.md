---
url: "https://www.telerik.com/blogs/functional-programming-csharp-brief-consideration"
captured_at: "2026-09-25T23:06:00+01:00"
title: "Functional Programming in C#—A Brief Consideration"
domain: "telerik-com"
---

A very common problem encountered in most program code is high complexity. To deal with this, a great alternative is functional programming—an excellent paradigm that helps programmers to write code that is less susceptible to errors. Check out this post for an introduction to the subject with practical examples.

The purpose of this blog post is not to delve into the subject of functional programming, but rather to inform the reader about the various benefits of functional programming through a brief consideration of the topic, address the main topics, and show how functional programming can be applied through C#.

**Some topics covered:**

*   What does “functional programming” mean?
*   Is C# a functional language?
*   Pure functions (advantages and disadvantages)
*   Practical examples of functional programming in C#
*   Using immutable types
*   Avoiding the use of declarations
*   Functional programming with LINQ
*   Higher-order functions (HOF)

## Improving Something That Is Already Good

If you, like me, have some experience with software development, it is quite likely that you have already come across some code that needed to be refactored due to its high—and most of the time unnecessary—complexity.

Object-oriented programming (OOP) has solved many problems previously faced and brought countless possibilities and facilities when writing code, but this “gift” can turn into a real curse if used the wrong way.

Something I’ve noticed is that many developers, based on their experiences and taking advantage of the possibilities of OOP, have created totally empirical code, full of endless “if” and “else” statements and the fanciest classes to store data in memory.

The result is that systems are increasingly modern but look old, as they use resources created in the first versions of the language—not that these resources should not be used, but one should always consider their use.

An alternative to avoid these and other problems is the use of functional programming. Since its release in the 2000s, many features have been added, and today we can finally say that C# has a wide variety of options for functional programming.

Throughout this article, we will address aspects that aim to help the reader to write cohesive, elegant and functional code with the C# language.

## What Does Functional Programming Mean?

Functional programming is a declarative programming paradigm. In this paradigm, programs are built by composing functions.

Function definitions are expression trees that map values to other values, instead of a sequence of imperative instructions that update the program’s execution state.

In simple terms, programming in a functional style allows developers to create software with declarative code through small functions combined in a modular way, which makes the code cohesive, elegant and easy to understand.

Pure functions are a subset of functional programming that treats all functions as deterministic math functions. So, when a pure function is called with some given arguments, it will always return the same result and cannot be affected by any mutable state or other side effects. When you restrict a program from side effects, it tends to be less buggy, easier to test and more readable.

> Read more about [functional programming in TypeScript](https://www.telerik.com/blogs/functional-programming-typescript) and in [JavaScript](https://www.telerik.com/blogs/functional-programming-javascript).

  

## Is C# a Functional Language?

No, C# is an object-oriented language that emphasizes state changes through imperative programming. But that doesn’t mean that C# doesn’t support functional programming. On the contrary, the latest versions of the language show how much Microsoft is concerned with making C# geared toward functional programming.

LINQ and lambda expressions are the most relevant examples in C# in which we can use the functional approach because they were already developed with this in mind, but there are many other features in C# that fulfill this purpose.

Below we will see some examples where we can replace imperative programming with functional programming and how it can benefit our code on a day-to-day basis.

## Pure Functions

### What Are Pure Functions?

A pure function is a function whose output depends only on the arguments passed to it.  
If a pure function is invoked twice using the same input values, the result obtained will be the same output for both cases.

### Advantages of Using Pure Functions

Following are some of the advantages of using pure functions:

*   **Better understanding of the code**  
    According to Robert Martin’s _Clean Code_ book, the proportion of time spent reading code is much higher than writing it, so if we have code that is easy to understand, the time spent on maintaining it tends to be very low.
    
*   **Easy debugging**  
    In pure functions, we don’t have complexities created in imperative code. So to debug pure functions, most of the time it will only depend on observing the values passed and why the expected result is not occurring.
    
*   **Easy-to-test code**  
    The vast majority of projects today require unit tests to be carried out to ensure they work. When we write pure functions, we don’t have any external dependencies—that is, we don’t need any kind of mock or any other hack.
    

### Disadvantages of Pure Functions

Despite bringing many benefits, the use of pure functions also brings some disadvantages such as:

*   **Bigger learning curve**  
    Compared to object-oriented programming, functional programming has a higher learning curve, as there are not as many resources available as in OOP, in addition to the care that must be taken when writing pure functions.
    
*   **Greater processing**  
    The use of immutable values and recursion can generate more memory consumption, but it will depend a lot on each scenario.
    
*   **Extra code**  
    As there is no change of state, it is necessary to repeat code when copying values and returning them to new objects, but compared to the overhead of imperative programming, pure functions require much less overhead.
    

## Practical Examples of Functional Programming in C#

Following are some examples of functional programming in C#. In each topic, the imperative form of implementation is covered first and then the functional approach.

You can access the repository with the source code used in the examples here: [Source Code](https://github.com/zangassis/functional-programming-csharp).

### Using Immutable Types

Avoiding state change is essential for functional programming. To do this, an alternative is to create immutable types, so we guarantee that their values are not modified during execution. So, if there is a need to modify them, a new instance of it must be created.

The example below first demonstrates the use of the imperative approach where the values of properties of a mutable type are changed during execution.

In the second example, we created an immutable type with a method that returns a new instance instead of modifying it.

**1\. Mutable example**

*   Order

```
namespace FPExampleApp;
public class Order
{
    public int UnitPrice { get; set; }
    public int Discount { get; set; }

    public void SpecialCustomer(int unitPrice, int discount)
    {
        UnitPrice = unitPrice;
        Discount += discount;
    }
}
```

C#

*   State mutation

```
using FPExampleApp;

// Imperative Approach

var order = new Order();
order.UnitPrice = 99;
order.Discount = 10;
order.SpecialCustomer(99, 20); 

// order.UnitPrice is 99, order.Discount = 30, same instance of order
```

C#

**2\. Immutable example**

*   ImmutableOrder

```
namespace FPExampleApp;
public class ImmutableOrder
{
    public int UnitPrice { get; }
    public int Discount { get; }

    public ImmutableOrder(int unitPrice, int discount)
    {
        UnitPrice = unitPrice;
        Discount = discount;
    }

    public ImmutableOrder SpecialCustomer(int unitPrice, int discount) 
        => new ImmutableOrder(unitPrice, Discount + discount);
}
```

C#

*   Avoiding state mutation

```
// Functional Approach

var immutableOrder = new ImmutableOrder(99, 10);
immutableOrder = immutableOrder.SpecialCustomer(99, 20);

// order.UnitPrice is 99, order.Discount = 30, new instance of order
```

C#

### Avoiding the Use of Declarations

Whenever possible, use expressions instead of declarations. In addition to making the code easier to interpret, expressions are much faster than declarations and also avoid code complexity.

```
static string WeatherVerify(double tempInCelsius) 
{
	// Here we have state change, unnecessary logic, multiple lines of code

	string climate = string.Empty;

	if (tempInCelsius < 20.0)
		climate = "Cold";
	else
		climate = "Perfect";

	return climate;
}

static string ImmutableWeatherVerify(double tempInCelsius) => 
	tempInCelsius < 20.0 ? "Cold" : "Perfect"; // Here we avoid changing state, there is no unnecessary logic and only two lines of code
```

C#

### LINQ—The Master of Functional Programming

LINQ (Language Integrated Query) is the name of a set of technologies based on integrating query capabilities directly into the C# language.

LINQ was developed in a functional style, and in recent years it has gained several improvements and new functions. It brings in its essence the pillars of the functional language, such as avoiding state changes, in addition to being implemented through a declarative query syntax. Its use is highly recommended when it comes to functional programming. Below are some examples of using LINQ.

Note that the first approach uses the imperative style with unnecessary logic and several lines of code, while the other two examples use LINQ expressions (query and lambda), where the functional style is used.

```
int[] scores = { 97, 92, 81, 60 };

// Imperative approach
var scoreImperative = new List<int>();

foreach (var item in scores)
{
    if (item > 80)
    {
		scoreImperative.Add(item);
    }
}

// Functional approach

// Query expression
IEnumerable<int> scoreQuery = from score in scores
							  where score > 80
							  select score;

// Lambda expression
IEnumerable<int> scoreLambda = scores.Where(score => score > 80);
```

C#

### Higher-Order Functions (HOF)

Higher-order functions are functions that take a function as an argument or return a function (or do both).

The opposite of these are first-order functions—that is, they do not take a function as an argument or return a function.

It is common to find higher-order functions in lambdas, such as in the LINQ `Where` clause, where a predicate is passed to it:

```
var olderUser = users.Where(user => user.Age == 99);
```

C#

But how would we go about implementing a higher-order function? The example below shows how to create our own `Where`, in the same way as LINQ’s `Where`:

*   User class

```
namespace FPExampleApp
{
    public class User
    {
        public string Name { get; set; }
        public int Age { get; set; }

        public User(string name, int age)
        {
            Name = name;
            Age = age;
        }
    }
}
```

C#

*   Creation of higher-order function (MyWhere)

```
var users = new List<User>()
{
	new User("John smith", 99),
    new User("Alice Smith", 99),
};

var olderUser = users.MyWhere(user => user.Age == 99);

foreach (var user in olderUser)
	WriteLine(user?.Name);

static class Helper
{
    public static IEnumerable<T> MyWhere<T>
        (this IEnumerable<T> source, Func<T, bool> predicate) //A predicate is passed as an argument
	{
		//The criterium determining which items are included is decided by the caller
		foreach (T s in source)
            if (predicate(s))
                yield return s;
    }
}
```

C#

Note that the “MyWhere” function receives another function as an argument through the predicate, in addition to an IEnumerable (source) that will be traversed by the function. So the criterion that determines which items will be included in the list is decided by the caller of the function—something that gives us complete freedom to predict the outcome.

## Conclusion

As seen throughout the post, functional programming solves many gaps left by object-oriented programming, but in no way replaces it. OOP is something that revolutionized the way software is built and allows developers to have a world of possibilities.

By using OOP combined with functional programming, we get the ability to extract the most that a well-written software can offer, as we avoid numerous future problems.

So don’t worry about creating 100 percent functional programs—just use pure functions and others resources available where you can use them, and your code will be at a much higher level.
