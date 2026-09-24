---
url: "https://dev.to/hypercodeplace/default-interface-implementations-in-c-where-inheritance-goes-to-troll-you-2djf?"
captured_at: "2026-09-25T00:07:07+01:00"
title: "Default Interface Implementations in C#: Where Inheritance Goes to Troll You"
domain: "dev-to"
---

## [](#introduction)Introduction

C# is a powerful and ever-evolving programming language, loved by developers for its robustness and versatility. With each new version, it introduces features that enhance convenience and streamline development.

However, much like Peter Parker, developers must wield this power responsibly. One slip-up, and you might find yourself tangled in a web of bugs and confusion.

[![With great power comes great debugging sessions](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Flhx5v33i6ctwz6mc522l.jpg)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Flhx5v33i6ctwz6mc522l.jpg)

A prime example of this is [Default Interface Implementations](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/proposals/csharp-8.0/default-interface-methods), introduced in C# 8.0. This feature allows developers to define methods with default implementations directly in interfaces. While it enables smoother API evolution by allowing methods to be added without breaking existing implementations and improves C#'s interoperation with platforms like Android (Java) and iOS (Swift), it also opens the door to subtle, hard-to-detect bugs, especially when combined with inheritance and dependency injection.

In this article, we’ll explore a seemingly straightforward scenario where Default Interface Implementations swing into action, only to deliver a surprise ending. This topic was inspired by a recent situation I encountered in my own practice, which highlighted how easily things can go awry. We’ll unravel the technical reasons behind this unexpected behavior and share tips to ensure your code doesn’t fall into the same trap.

## [](#a-simple-service)A Simple Service

Let’s start with a basic example. Imagine you’re working on a service, `MyService`, that depends on an `IFoo` interface. Nothing fancy, just your standard DI setup:  

```
public class MyService
{
    private readonly IFoo _foo;

    // Constructor with an injected service.
    public MyService(IFoo foo)
    {
        _foo = foo;
    }

    // A method that prints a value.
    public void PrintValue()
    {
        // Get the value.
        var value = _foo.GetValue();

        // Print the value.
        Console.WriteLine(value);
    }
}
```

Enter fullscreen mode Exit fullscreen mode

The `IFoo` interface has a single method, `GetValue`, which includes a default implementation. Here’s how the interface and its implementation look:  

```
public interface IFoo
{
    // A method declaration with a default implementation.
    string GetValue() => "IFoo";
}

// An implementation of the interface.
public class Foo : IFoo
{
    // Overriding the method.
    public string GetValue() => "Foo";
}
```

Enter fullscreen mode Exit fullscreen mode

When you run this in your trusty unit test, everything works as expected:  

```
[TestFixture]
public class FooTests
{
    [Test]
    public void GetValueMustReturnFoo()
    {
        // Create an instance of the service.
        var foo = new Foo();

        // Get the value.
        var value = foo.GetValue();

        // Ensure the value is correct and equal to "Foo".
        Assert.AreEqual("Foo", value);
    }
}
```

Enter fullscreen mode Exit fullscreen mode

The test passes, confirming that `Foo.GetValue()` returns `"Foo"`.

Finally, you use `MyService` in a console app. In reality, this is a common scenario where the service would typically be resolved from a Dependency Injection (DI) container, but for simplicity, let's use the console app to demonstrate the concept.  

```
class Program
{
    static void Main(string[] args)
    {
        // Create an instance of `Foo`.
        var foo = new Foo();

        // Create an instance of `MyService` using the `Foo` instance.
        var service = new MyService(foo);

        // Execute the method to get an output.
        service.PrintValue();
    }
}
```

Enter fullscreen mode Exit fullscreen mode

Running this program produces the expected output:  

```
Foo
```

Enter fullscreen mode Exit fullscreen mode

All is right in the world. Or so you think...

## [](#what-could-go-wrong)What Could Go Wrong?

Now, imagine someone on your team decides to refactor the `Foo` class by introducing a base class `FooBase`:  

```
// Introduce a base class.
public class FooBase : IFoo
{
}

// Derive `Foo` from the base class.
public class Foo : FooBase
{
    // No other changes here.
    public string GetValue() => "Foo";
}
```

Enter fullscreen mode Exit fullscreen mode

Seems harmless enough, right? **Right?**

You run the tests. They pass. You deploy to production, and then… SURPRISE! The output changes:  

```
IFoo
```

Enter fullscreen mode Exit fullscreen mode

[![One does not simply introduce a base class without consequences](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F2drugjl1o2q9q9xpdhu1.jpg)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F2drugjl1o2q9q9xpdhu1.jpg)

## [](#why-does-this-happen)Why Does This Happen?

When a type is loaded into the CLR, a **method table** is created and initialized. This table is used by the runtime to resolve method calls to the actual methods that will be executed. Think of it as a guide that tells the runtime which method to call based on the type and method signatures.

Before the base class was introduced, the class `Foo` directly implements the interface `IFoo`. In this case, the method table for `Foo` maps interface methods to the class’s implementation, as long as the method signatures match. So, when `GetValue()` is called on an instance of `Foo`, the runtime looks up the method in the `Foo` class and resolves it to the `GetValue()` method explicitly defined there.  

```
Before

+---------------+      +--------------+
| IFoo.GetValue | ---> | Foo.GetValue | 
+---------------+      +--------------+ 
```

Enter fullscreen mode Exit fullscreen mode

However, when you introduce a base class (`FooBase`) and derive `Foo` from it, things get interesting. Now, `Foo` no longer **directly** implements `IFoo`. Instead, it inherits from `FooBase`, which implements `IFoo`. The method table is updated accordingly, and the runtime resolves method calls based on the inheritance chain. This means it looks at `FooBase`'s method table to resolve the call. But here’s the kicker: `FooBase` doesn’t implement `GetValue()`, so the runtime falls back to the **default interface implementation** from `IFoo`.  

```
After

+---------------+      +--------------+
| IFoo.GetValue |      | Foo.GetValue | 
+---------------+      +--------------+ 
       ^  |            +------------------------------------+
       |  +----------> | FooBase.GetValue (not implemented) | 
       +--(default)--- +------------------------------------+
```

Enter fullscreen mode Exit fullscreen mode

In simpler terms, when `Foo` inherits from `FooBase`, the method table no longer directly points to `Foo.GetValue()`. Since `Foo` no longer explicitly implements `IFoo`, the runtime defaults to the method in the interface, which might not be what you intended, leading to the unexpected `"IFoo"` value instead of `"Foo"`.

## [](#how-to-prevent-this)How to Prevent This?

Don’t shoot yourself in the foot with Default Interface Implementations. Here’s how to use them wisely:

*   **Understand the Behavior**: Default methods are convenient, but they can be tricky when paired with inheritance.
*   **Avoid Unnecessary Inheritance**: Inheritance is powerful, but don’t overuse it. If you need shared logic, [prefer composition over inheritance](https://blog.ploeh.dk/2018/02/26/inheritance-composition-isomorphism/).
*   **Explicitly Derive from the Interface**: Even if you introduce a base class that implements an interface, the derived class should explicitly declare that it implements the interface itself and provide method overrides as necessary.

```
// Explicitly implement the interface
// Yes, even if the class is derived from `FooBase`, which implements `IFoo`.
public class Foo : FooBase, IFoo
{
    // Override the method.
    public string GetValue() => "Foo";
}
```

Enter fullscreen mode Exit fullscreen mode

*   **Test Through Interfaces**: Modify tests to interact with the interface directly, rather than through a concrete class or `var`. This ensures that the behavior being tested aligns with the contract defined by the interface. Using `var` or directly referencing the concrete class can inadvertently bypass interface behavior, masking potential issues with default implementations or inheritance.

```
// The improved test: Interact through the interface.
[Test]
public void GetValueMustReturnFoo()
{
    // Create an instance of the service using the interface, not `var`.
    IFoo foo = new Foo();

    // Get the value.
    var value = foo.GetValue();

    // Ensure the value is correct and equal to "Foo".
    Assert.AreEqual("Foo", value);
}
```

Enter fullscreen mode Exit fullscreen mode

*   **Leverage Static Analysis Tools**: Use tools like Roslyn analyzers (e.g. [Roslyn Analyzers for C#](https://github.com/dotnet/roslyn-analyzers) or [SonarAnalyzer for .NET](https://github.com/SonarSource/sonar-dotnet)) to catch risky patterns.
*   **Document and Review Changes**: Always document changes involving default methods and review them thoroughly.

## [](#conclusion)Conclusion

Default Interface Implementations in C# are a double-edged sword. While they provide immense flexibility and streamline API evolution, they also introduce complexities that can catch even experienced developers off guard. As shown in this example, subtle changes in class hierarchies can lead to unexpected behaviors, often surfacing only in production.

To avoid such pitfalls, prioritize composition over inheritance to reduce unintended coupling and improve code maintainability. Always test through interfaces to ensure that your implementations behave correctly, independent of specific class hierarchies. Additionally, document changes meticulously to keep the team aligned and prevent surprises.

Default Interface Implementations may be powerful, but with a thoughtful approach, you can navigate their pitfalls and ensure that inheritance doesn’t troll you again.
