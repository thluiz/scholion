---
url: "https://code-maze.com/improve-performance-sealed-classes-dotnet/"
captured_at: "2026-09-24T23:20:41+01:00"
title: "Boosting Performance With Sealed Classes in .NET - Code Maze"
domain: "code-maze-com"
---

Updated on March 22, 2024

In this article, we are going to learn how we can boost performance with sealed classes in our .NET projects.

**By default, all classes in C# are open for inheritance**. We can use the sealed keyword to prevent inheriting from the class and improve performance for certain operations. We are going to see how performant sealed classes are compared to open classes and when we should use them.

To download the source code for this article, you can visit our [GitHub repository](https://github.com/CodeMazeBlog/CodeMazeGuides/tree/main/dotnet-performance/SealedClasses).

Let’s start.

## What is a Sealed Class?

**Sealed classes in C# restrict inheritance**. When we define our class as a sealed class, we cannot inherit from it anymore.

We can use the `sealed` keyword to mark our class as sealed:

sealed class A {}

`sealed class A {}`

That said, we can also use the `sealed` modifier on a method or property that overrides a virtual method or property. With that, we prevent specific virtual methods from being overridden.

## Prepare the Environment

Initially, let’s prepare the environment and our class structure that we will use for comparison between sealed and open classes.

Let’s create our base class:

public class Animal
{
    public virtual void DoNothing() { }
    public virtual int GetAge() => -1;
    public static string Walk() => "I'm walking..";
}

Inside the `Animal` class, we have two virtual and one static method that we will use later for comparison.

Secondly, let’s create our first derived class:

public class Bear : Animal
{
    public override void DoNothing() { }
    public override int GetAge() => 4;
}

Here we create the open class named `Bear` and override the `DoNothing()` and `GetAge()` methods from our base `Animal` class.

Lastly, let’s add our sealed class:

public sealed class Husky : Animal
{
    public override void DoNothing() { }
    public override int GetAge() => 11;
}

Again, we inherit from the `Animal` class and override the two methods.

It is important to note that the `Husky` class is sealed since it is a specific dog breed. On the other hand, the `Bear` class is open for inheritance because we could have multiple types of bears in the future. 

## Sealed Class Performance Benchmark

Let’s start our comparison between the two classes to determine if there are any performance differences.

We will create different methods and run them with the [BenchmarkDotNet](https://code-maze.com/benchmarking-csharp-and-asp-net-core-projects/) library to measure the time performance.

First, let’s add a new class that we will use to perform our benchmark:

\[Orderer(SummaryOrderPolicy.FastestToSlowest)\]
public class PerformanceBenchmark
{
    private readonly Bear \_bear = new();
    private readonly Husky \_husky = new();
}

Here we create the new `PerformanceBenchmark` class with two read-only fields to store our `Bear` and `Husky` objects.

### Calling a Void Method

Now, let’s add new methods to the `PerformanceBenchmark` class to check the performance of the void method:

\[Benchmark\] 
public void Sealed\_VoidMethod() => \_husky.DoNothing();

\[Benchmark\]
public void Open\_VoidMethod() => \_bear.DoNothing();

The `Sealed_VoidMethod()` method executes the `DoNothing()` method from the `Husky` class.

We call the second method `Open_VoidMethod()` for executing the same method from the open class.

After that, let’s run our project with the `dotnet run -c Release` command and check the performance results:

|            Method |      Mean |     Error |    StdDev |    Median |
|------------------ |----------:|----------:|----------:|----------:|
| Sealed\_VoidMethod | 0.0030 ns | 0.0056 ns | 0.0159 ns | 0.0000 ns |
|   Open\_VoidMethod | 0.6350 ns | 0.0661 ns | 0.1917 ns | 0.6182 ns |

Wow, we can see that our `Sealed_VoidMethod()` method executes much faster.

### Calling a Method With a Return Value

Next, we’re going to see if our sealed class performs faster only when running void methods or if that is the case for the methods with return types.

Let’s add another two methods with the return type of `int`:

\[Benchmark\] 
public int Sealed\_IntMethod() => \_husky.GetAge();

\[Benchmark\]
public int Open\_IntMethod() => \_bear.GetAge();

Here we return an integer type from both classes.

Again, let’s run the benchmark to see the results:

|           Method |      Mean |     Error |    StdDev |
|----------------- |----------:|----------:|----------:|
| Sealed\_IntMethod | 0.0857 ns | 0.0320 ns | 0.0535 ns |
|   Open\_IntMethod | 0.5081 ns | 0.0321 ns | 0.0343 ns |

The method executed from a sealed class is much more performant.

Free ebook

Most Web APIs ship with the same 33 mistakes.

The Web API Production Checklist walks through every one of them, with the fix, in .NET 10. 76 pages, free.

[Download the free PDF](https://code-maze.com/free-ebook-aspnetcore-webapi-best-practices/?box=6)

Free PDF. One email to send it. Unsubscribe any time.

### Calling a Static Method

Let’s now check how the static `Walk()` method from the base class executes when we call it from both sealed and open classes:

\[Benchmark\]
public void Sealed\_StaticMethod() => Husky.Walk();

\[Benchmark\]
public void Open\_StaticMethod() => Bear.Walk();

Now, let’s run the program:

|              Method |      Mean |     Error |    StdDev |    Median |
|-------------------- |----------:|----------:|----------:|----------:|
| Sealed\_StaticMethod | 0.0183 ns | 0.0168 ns | 0.0340 ns | 0.0000 ns |
|   Open\_StaticMethod | 0.0340 ns | 0.0222 ns | 0.0464 ns | 0.0183 ns |

Interestingly, we can see similar results from both methods. We’ll dive into that later.

### Calling the ToString() Method

One method that we frequently use on objects and different types is the `ToString()` method. 

Let’s check how it performs on both class types:

\[Benchmark\]
public string Sealed\_ToString() => \_husky.ToString()!;

\[Benchmark\]
public string Open\_ToString() => \_bear.ToString()!;

And run the benchmark with the results:

|          Method |     Mean |     Error |    StdDev |
|---------------- |---------:|----------:|----------:|
| Sealed\_ToString | 5.731 ns | 0.1882 ns | 0.4510 ns |
|   Open\_ToString | 7.149 ns | 0.2152 ns | 0.3475 ns |

The sealed class performance is better, but the difference is not noticeable.

### Casting Objects

Aside from method calls, we can do different operations with our classes. One of the most common operations is casting with the `as` operator.

First, let’s add a private read-only `Animal` object to the class:

private readonly Animal \_animal = new();

`private readonly Animal _animal = new();`

Now, let’s implement two methods to cast a base type to its subtypes:

\[Benchmark\]
public Husky? Sealed\_Casting() => \_animal as Husky;

\[Benchmark\]
public Bear? Open\_Casting() => \_animal as Bear;

With that done, we have the performance benchmark:

|         Method |      Mean |     Error |    StdDev |
|--------------- |----------:|----------:|----------:|
| Sealed\_Casting | 0.2757 ns | 0.0819 ns | 0.2158 ns |
|   Open\_Casting | 2.0827 ns | 0.1232 ns | 0.2652 ns |

Great, the casting operation of our sealed class is multiple times faster.

### Checking the Type of Objects

Along with the `as` operator, one of the operators we use frequently is the `is` operator. The `is` operator comes in handy when we are checking the type of an object.

With that, let’s add two methods for checking the type:

\[Benchmark\]
public bool Sealed\_TypeCheck() => \_animal is Husky;

\[Benchmark\]
public bool Open\_TypeCheck() => \_animal is Bear;

Here both methods return `true` if our `_animal` variable is of type `Husky` or of type `Bear`.

Let’s check the results again:

|           Method |      Mean |     Error |    StdDev |
|----------------- |----------:|----------:|----------:|
| Sealed\_TypeCheck | 0.3880 ns | 0.0342 ns | 0.0625 ns |
|   Open\_TypeCheck | 2.0330 ns | 0.0733 ns | 0.1610 ns |

Now we already see it coming. The sealed class performs much better when checking for the type with the `is` operator.

### Working With Arrays

Lastly, we will see how both types of classes work with arrays. We work with arrays very often, so it is important to check that aspect.

First, let’s add two different arrays to our class:

private readonly Bear\[\] \_bears = new Bear\[1\];
private readonly Husky\[\] \_huskies = new Husky\[1\];

Now, let’s add two different methods to add objects of each type to an array:

\[Benchmark\]
public void Sealed\_AddToArray() => \_huskies\[0\] = new Husky();

\[Benchmark\]
public void Open\_AddToArray() => \_bears\[0\] = new Bear();

With that, let’s run our benchmark:

|            Method |     Mean |     Error |    StdDev |
|------------------ |---------:|----------:|----------:|
| Sealed\_AddToArray | 4.322 ns | 0.1173 ns | 0.2899 ns |
|   Open\_AddToArray | 5.629 ns | 0.1436 ns | 0.2732 ns |

Not as much as before, but our sealed class is the winner again.

## Sealed Classes Performance Behind the Scenes

In our benchmark tests, we conclude that **the sealed class is faster in all cases except for calling a static method** from the parent `Animal` class. How can that be?

Well, there are different reasons.

### Methods in Sealed Classes

When we call overridden methods in sealed classes, this is done **directly on the memory address of the sealed class object**. In an open class, we need to call methods through virtual dispatch. **The virtual dispatch cannot use a direct call** since it has to check if the method has been overridden.

We will use the simplified version of our program in the [SharpLab](https://sharplab.io/) online compiler to see how JIT commands are executed.

First, let’s add the code:

var benchmark = new Benchmark();

benchmark.Sealed();
benchmark.NonSealed();

public class Benchmark {
    private Husky \_sealed = new();
    private Bear \_nonSealed = new();

    public void NonSealed() => \_nonSealed.DoNothing();

    public void Sealed() => \_sealed.DoNothing(); 
}

public class Animal
{
    public virtual void DoNothing() { }
}

public class Bear : Animal
{
    public override void DoNothing() { }
}

public sealed class Husky : Animal
{
    public override void DoNothing() { }
}

After that, let’s set the “Results” option to **JIT Asm in release mode** and check the output:

[![jit result sealed class](https://code-maze.com/wp-content/uploads/2022/10/JITResults.png)](https://code-maze.com/wp-content/uploads/2022/10/JITResults.png)

Free ebook

Most Web APIs ship with the same 33 mistakes.

The Web API Production Checklist walks through every one of them, with the fix, in .NET 10. 76 pages, free.

[Download the free PDF](https://code-maze.com/free-ebook-aspnetcore-webapi-best-practices/?box=6)

Free PDF. One email to send it. Unsubscribe any time.

Fantastic, note how our `NonSealed()` method uses **additional** `mov` **instructions** to find the exact address of the method to invoke, which makes it less performant.

However, if the JIT can determine the type, it can avoid using the virtual dispatch on open class methods.

Let’s check that by creating an instance of an object directly in the method which later uses the object:

\[Benchmark\]
public void SealedDeclaredInMethod\_VoidMethod()
{
    var husky = new Husky();
    husky.DoNothing();
}

\[Benchmark\]
public void OpenDeclaredInMethod\_VoidMethod()
{
    var bear = new Bear();
    bear.DoNothing();
}

Here we create two different methods for calling void methods from our `Husky` and `Bear` classes. The only difference from our first benchmark is that **we create the instance of the class inside the method**.

Let’s check the results:

|                            Method |      Mean |     Error |    StdDev |    Median |
|---------------------------------- |----------:|----------:|----------:|----------:|
| SealedDeclaredInMethod\_VoidMethod | 0.0529 ns | 0.0296 ns | 0.0542 ns | 0.0337 ns |
|   OpenDeclaredInMethod\_VoidMethod | 0.0535 ns | 0.0288 ns | 0.0505 ns | 0.0386 ns |

Surprising? Not exactly. Here, **the performances are almost identical because the JIT knows the actual type,** so it uses a direct call.

That works differently with static methods since they can’t be overridden. That is the reason we got similar results when calling the `Walk()` static method from the `Animal` parent class.

### Operations With Sealed Classes

Similarly, **casting and type-checking operations are faster on sealed classes** because we only need to compare the type to itself. With open classes, we need to check for a potential hierarchy of classes.

Our sealed class outperformed the open class when inserting it into an array. The reason is that **sealed classes don’t need a** [covariance](https://code-maze.com/csharp-covariance-and-contravariance/) **check** when the element is stored.

## Mocking With Sealed Classes

**Unit testing can become harder with sealed classes, as mocking is not allowed**. For example, when we use some mocking frameworks like [Moq](https://code-maze.com/using-moq-to-determine-if-method-is-called/) we can get errors.

Let’s try to create a mock for our `Husky` sealed class:

var huskyMock = new Mock<Husky\>();

`var huskyMock = new Mock<Husky>();`

This will produce a runtime error from the Moq library:

System.NotSupportedException - Type to mock must be an interface or an abstract or non-sealed class

`System.NotSupportedException - Type to mock must be an interface or an abstract or non-sealed class`

We can avoid that issue by **coding to an interface instead of the concrete type**. In this case, we should create an abstraction above our `Husky` class and then mock one level up from that.

## When to Use a Sealed Class?

Sealed classes are mostly used with security features to avoid changing the original behavior. Most performance-based applications will also use sealed classes because it speeds up the processes. **A specific class should be sealed if it doesn’t make sense to inherit from it.**

As with everything in software, sealed classes have both pros and cons. That said, we already mentioned that mocking with sealed classes is harder.

### Detecting Unreachable Code With Sealed Class

Another benefit of sealed classes is **the detection of unreachable code when conversions are not valid**.

For example, let’s say that we have an interface:

public interface IFlyingAnimal { }

`public interface IFlyingAnimal { }`

If we try to cast our `Husky` class with the `as` keyword to the `IFlyingAnimal` interface, the compiler will throw an error. Also, if we try to check if our sealed class is of type `IFlyingAnimal` with the `is` keyword, we will get a warning. With that, we can reduce errors and remove unreachable code from our project.

## Conclusion

In this article, we’ve learned about how to boost the performance of the sealed classes with the sealed modifier in C#. We’ve checked different methods and operations on sealed and open classes.

The main conclusion is that **most operations are significantly faster when using sealed classes**. That said, if we are certain that we won’t inherit from a class, we should mark it as sealed. One of the drawbacks when using sealed classes is the potential complexity added for mocking classes in unit tests.

Still, in most cases, the pros outweigh the cons.
