---
url: "https://www.c-sharpcorner.com/blogs/liskov-substitution-principle-in-c-sharp-with-example?ref=dailydev"
captured_at: "2026-09-25T21:54:43+01:00"
title: "Liskov Substitution Principle in C# with Example"
domain: "c-sharpcorner-com"
---

The Liskov Substitution Principle (LSP) is one of the five SOLID principles of object-oriented design.

"Objects in a program should be replaceable with instances of their subtypes without altering the correctness of that program."

In simpler terms, if you have a base class (or interface) and a derived class, you should be able to replace the base class with the derived class without introducing errors or changing the expected behavior of the program.

## The Problematic Code

Let's start with an example that violates the LSP. Consider a base class Bird and a derived class Ostrich.

```
public class Bird
{
    public virtual void Fly()
    {
        Console.WriteLine("Flying");
    }
}

public class Ostrich : Bird
{
    public override void Fly()
    {
        throw new NotSupportedException("Ostriches can't fly");
    }
}

public class Program
{
    public static void Main()
    {
        Bird bird = new Ostrich();
        bird.Fly(); // Throws NotSupportedException
    }
}
```

In this example,

*   The Bird class has a method Fly that prints "Flying".
*   The Ostrich class inherits from Bird but overrides the Fly method to throw a NotSupportedException because ostriches cannot fly.

When you instantiate an Ostrich and assign it to a Bird reference, calling the Fly method results in an exception. This violates the LSP because substituting an Ostrich for a Bird changes the expected behavior, making the program incorrect.

## Adhering to LSP

To adhere to LSP, we need to ensure that substituting a subclass for a superclass does not break the program. One way to achieve this is by creating a more appropriate class hierarchy or using interfaces to represent different behaviors.

**Step 1.** Define an Interface for Birds.

First, we define an interface IBird that represents the common behavior of all birds.

```
public interface IBird
{
    void Move();
}
```

**Step 2.** Implement Specific Bird Classes.

Next, we implement specific bird classes that adhere to the IBird interface. Each class will have its own implementation of the Move method, encapsulating the specific movement behavior of the bird.

### FlyingBird Class

```
public class FlyingBird : IBird
{
    public void Move()
    {
        Fly();
    }

    public virtual void Fly()
    {
        Console.WriteLine("Flying");
    }
}
```

The FlyingBird class implements the IBird interface and provides a Fly method. The Move method called the Fly method, represents the flying behavior.

### Ostrich Class

```
public class Ostrich : IBird
{
    public void Move()
    {
        Run();
    }

    public void Run()
    {
        Console.WriteLine("Running");
    }
}
```

The Ostrich class also implements the IBird interface but provides a Run method instead of Fly. The Move method is called the Run method, representing the running behavior.

**Step 3.** Use the Bird Classes.

Now we can use these bird classes in our program without violating the LSP.

```
public class Program
{
    public static void Main()
    {
        IBird bird1 = new FlyingBird();
        bird1.Move(); // Outputs: Flying

        IBird bird2 = new Ostrich();
        bird2.Move(); // Outputs: Running
    }
}
```

In this refactored version.

*   FlyingBird and Ostrich both implement the IBird interface.
*   The Move method in each class encapsulates the specific movement behavior of the bird.
*   Calling Move on an instance of FlyingBird results in "Flying", and calling Move on an instance of Ostrich results in "Running".

## Conclusion

By refactoring the original code to adhere to the Liskov Substitution Principle, we ensure that substituting subclasses for the base class does not break the program. This makes our code more robust, maintainable, and scalable.

## Summary

*   The original code violated the LSP because substituting an Ostrich for a Bird caused an exception.
*   We introduced an interface IBird to represent common bird behavior.
*   We created specific bird classes (FlyingBird and Ostrich) that implemented the IBird interface and encapsulated their respective behaviors.
*   This approach ensures that our program behaves correctly regardless of the specific bird type used.

By following the Liskov Substitution Principle, we improve the design and reliability of our software, making it easier to understand, extend, and maintain.
