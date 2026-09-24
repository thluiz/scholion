---
url: "https://code-maze.com/csharp-chain-of-responsibility-design-pattern/?ref=dailydev"
captured_at: "2026-09-24T23:17:17+01:00"
title: "Chain of Responsibility Design Pattern in C# - Code Maze"
domain: "code-maze-com"
---

Updated on July 19, 2026

In this article, we will talk about the Chain of Responsibility Design Pattern. We are going to see how to implement this pattern in C# and how it can solve certain design problems.

To download the source code for this article, you can visit our [GitHub repository](https://github.com/CodeMazeBlog/CodeMazeGuides/tree/main/csharp-design-patterns/ChainOfResponsibilityPattern).

Let’s start.

**Related Articles:** [Comparison of Rebus, NServiceBus, and MassTransit in .NET](https://code-maze.com/aspnetcore-comparison-of-rebus-nservicebus-and-masstransit/) · [How to Use Pointers in C#](https://code-maze.com/csharp-how-to-use-pointers/)

## Frequently Asked Questions

### What is the Chain of Responsibility pattern?

It passes a request along a chain of handler objects; each handler decides whether to process it or forward it to the next, decoupling the sender from the receivers.

### How do you implement Chain of Responsibility in C#?

Define a handler interface with a Next reference and a Handle method, link the handlers, and call Handle on the first one.

### When should you use Chain of Responsibility?

For pipelines such as middleware, validation, or logging, where multiple handlers may process or short-circuit a request.

Chain of Responsibility is a behavioral pattern that helps us design a complex component built over independent processing components. **This pattern suggests breaking down logic into smaller, more focused components, each with a distinct responsibility, and chaining them together to accomplish a larger task.** Chain of Responsibility is a powerful technique for fostering the [Single Responsibility Principle](https://code-maze.com/single-responsibility-principle/) and promoting loose coupling.

**ASP.NET Core middleware is a prime example of the chain of responsibility pattern.** **The middleware decouples a request’s sender from its receivers by allowing multiple handlers to handle it independently.**

In a typical use-case of this pattern, we send a request along a series of handlers:

[![Chain of Responsibility Design Pattern](https://code-maze.com/wp-content/uploads/2024/12/Chain-of-Responsibility-Design-Pattern.png)](https://code-maze.com/wp-content/uploads/2024/12/Chain-of-Responsibility-Design-Pattern.png)

Each handler addresses a specific aspect of the whole task. The client arranges the handlers in a particular sequence to form a chain and sends the request to the first handler, which then passes it along to the subsequent handlers, ultimately producing the final result. The entire mechanism involves two key functions: creating a chain and passing the execution call from one handler to the next.

The `IHandler` interface defines the basic methods needed to support the chain propagation process. One such method (e.g. `setNext()`) is responsible for building the chain and should accept and store a reference to the next handler.

Upon receiving a request, a handler executes its logic and then hands over the responsibility to the next handler in the chain. A method like `handle()` can serve this purpose and essentially should be a part of the `IHandler` interface. 

## Single-handler vs Multi-handler Workflow

The chain propagation can follow a single or multi-handler workflow depending on the overall intent.

In a multi-handler workflow, the handlers represent a sequence of steps, and the request is allowed to be handled by multiple handlers:

[![Chain of Responsibility (Multi-handler Workflow)](https://code-maze.com/wp-content/uploads/2024/12/Chain-of-Responsibility-Design-Pattern-Multi-handler-e1733206348883.png)](https://code-maze.com/wp-content/uploads/2024/12/Chain-of-Responsibility-Design-Pattern-Multi-handler.png)

![The Web API Production Checklist, free ebook](https://code-maze.com/wp-content/uploads/ebooks/covers/cover-dark-1-panel-400.webp)

Free ebook

Most Web APIs ship with the same 33 mistakes.

The Web API Production Checklist walks through every one of them, with the fix, in .NET 10. 76 pages, free.

[Download the free PDF](https://code-maze.com/free-ebook-aspnetcore-webapi-best-practices/?box=2)

Free PDF. One email to send it. Unsubscribe any time.

The request enters the first step, undergoes the operation performed by that handler, and then moves on to the next step if the previous operation succeeds. The process continues up to the terminal handler.

A multi-handler approach is handy when we perform a series of operations that may change dynamically based on various business factors. We can incorporate more steps in the process by adding more handlers to the chain without affecting existing ones. Similarly, we can eliminate steps that are not relevant to a particular case by removing the corresponding handler.

In the case of a single-handler workflow, only one handler in the chain ‘truly’ processes the request:

[![Chain of Responsibility (Single-handler Workflow)](https://code-maze.com/wp-content/uploads/2024/12/Chain-of-Responsibility-Design-Pattern-Single-handler.png)](https://code-maze.com/wp-content/uploads/2024/12/Chain-of-Responsibility-Design-Pattern-Single-handler.png)

In this scenario, the handlers are simply variations of one another. Each handler passes the request along to the next until it reaches the appropriate handler capable of processing that particular request. The designated handler stops the chain once it handles the request. 

## What Problem Does The Chain of Responsibility Pattern Solve?

To better understand how the Chain of Responsibility (**CoR**) pattern functions, let’s begin by discussing the problem it addresses.

Let’s consider a rental request processing API for a library:

public class RentalAssistService
{
    public RentalResponse ProcessRentRequest(RentalRequest request)
    {
        var result = CheckForBookAvailability(request.BookName);

        if (result != RentalResponse.BookAvailable)
            return result;

        result = CheckForMemberAccessibility(request.BookName, request.UserName);

        if (result != RentalResponse.AccessibleToUser)
            return result;

        result = CheckForAvailableBalance(request.UserName);

        if (result != RentalResponse.RentalApproved)
            return result;

        return IssueBook(request.BookName, request.UserName);
    }
    ...
}

The API provides a method to process a user’s `RentalRequest` after some due diligence procedure. This process involves four sequential operations: book availability checks, member eligibility checks, checks for sufficient balance, and book issuance procedures:

private RentalResponse CheckForBookAvailability(string bookName)
{
    if (DataStore.FindBook(bookName) is not { } book || book.IssuedTo is not null)
        return RentalResponse.BookUnavailable;

    return RentalResponse.BookAvailable;
}

private RentalResponse CheckForMemberAccessibility(string bookName, string userName)
{
    if (DataStore.FindUser(userName) is not { } user)
        return RentalResponse.MembershipRequired;

    if (!user.IsFaculty && IsReserved(bookName))
        return RentalResponse.FacultyOnlyAccess;

    return RentalResponse.AccessibleToUser;
}

private RentalResponse CheckForAvailableBalance(string userName)
{
    if (!HasBalance(userName))
        return RentalResponse.InsufficientBalance;

    return RentalResponse.RentalApproved;
}

private RentalResponse IssueBook(string bookName, string userName)
{
    var book = DataStore.FindBook(bookName)!;
    book.IssuedTo = userName;

    // Send email to user
    Console.WriteLine($"Your request for {bookName} has been processed");

    return RentalResponse.RentalIssued;
}

private static bool IsReserved(string bookName) => 
    DataStore.FindBook(bookName) is { IsReserved: true };

private static bool HasBalance(string userName) => 
    DataStore.FindUser(userName) is { Balance: >= Book.RentalFee };

This big monolithic class contains logic for all steps and conditional executions altogether making it tightly coupled and difficult to evolve further. The client code remains aware of how the request is processed in each step. Whenever we need to modify the internal logic of any operation, we must change the `RentalAssistService` class, leading to all the drawbacks of violating the Single Responsibility Principle.

A more efficient and streamlined approach is to encapsulate each step in a separate class and link them together, precisely what the Chain of Responsibility pattern enables.

## Implementation of Chain of Responsibility Pattern in C#

Let’s revise our `RentalAssistService` class to incorporate the CoR pattern (check out the “Solution” folder in the source code).

The first and foremost action is transforming each step into an independent handler class.

Let’s start with implementing `IHandler` interface in an abstract base handler class:

public abstract class HandlerBase : IHandler
{
    protected IHandler? \_nextHandler;

    public IHandler SetNext(IHandler nextHandler)
    {
        \_nextHandler = nextHandler;

        return \_nextHandler;
    }

    public abstract RentalResponse Handle(RentalRequest request);
}

The `SetNext()` method helps us connect with the next handler. We make it a bit more interesting by returning the reference of the next handler. This will simplify the chain formation from the client code.

![The Web API Production Checklist, free ebook](https://code-maze.com/wp-content/uploads/ebooks/covers/cover-dark-1-panel-400.webp)

Free ebook

Most Web APIs ship with the same 33 mistakes.

The Web API Production Checklist walks through every one of them, with the fix, in .NET 10. 76 pages, free.

[Download the free PDF](https://code-maze.com/free-ebook-aspnetcore-webapi-best-practices/?box=2)

Free PDF. One email to send it. Unsubscribe any time.

The core request processing logic of concrete handlers will go inside the `Handle()` method.

Let’s add the `BookAvailabilityCheckHandler` class to accommodate the logic of the book availability step:

public class BookAvailabilityCheckHandler : HandlerBase
{
    public override RentalResponse Handle(RentalRequest request)
    {
        if (DataStore.FindBook(request.BookName) is not { } book || book.IssuedTo is not null)
            return RentalResponse.BookUnavailable;

        if (\_nextHandler is null)
            return RentalResponse.BookAvailable;

        return \_nextHandler.Handle(request);
    }
}

Since our scenario reflects a multi-handler workflow, we call upon the next handler when the request meets the requirement of the current step. 

We can similarly transform other processing steps into individual handlers – `MemberEligibilityCheckHandler`, `UserBalanceCheckHandler` and the terminal `RentalIssuanceHandler` class. 

Once the handler classes are ready, we can refactor the `RentalAssistService` class: 

public RentalResponse ProcessRentRequest(RentalRequest request)
{
    var handler = new BookAvailabilityCheckHandler();

    handler.SetNext(new MemberAccessibilityCheckHandler())
        .SetNext(new UserBalanceCheckHandler())
        .SetNext(new RentalIssuanceHandler());

    return handler.Handle(request);
}

As expected, the client code is now only responsible for defining the sequence of handlers and initiating the `Handle()` call on the first step. The execution call will propagate through the handlers if it satisfies the relevant condition.

### An Implicit Advantage of Chain of Responsibility

One great advantage of the CoR pattern is the seamless workflow synthesis. For example, if the user requests a way to check the validity of  the rental request without the actual issuance of the book, we can easily do that too:

public RentalResponse AssessRentRequest(RentalRequest request)
{
    var handler = new BookAvailabilityCheckHandler();

    handler.SetNext(new MemberAccessibilityCheckHandler())
        .SetNext(new UserBalanceCheckHandler());

    return handler.Handle(request);
}

We just need to remove the last link of the chain, that’s it!

## Drawbacks of Chain of Responsibility Pattern

While the Chain of Responsibility pattern is useful for solving many design challenges, it requires thoughtful considerations during implementation.

**One major concern with chained flow is the order of dependencies.** A common risk in such cases is incorrectly placing handlers at the appropriate points in the chain. For example, adding a validation handler after a processing handler will end up processing an invalid request.

**The effectiveness of a chain pattern depends on clearly defining each step with a well-structured and reusable handler interface.** However, this can be challenging and may increase system complexity. For example, when steps need to exchange object states, handlers may become interdependent, leading to potential coupling.

Another potential side-effect of CoR is, that **there can be no guarantee of handling a request!** There is a risk that all handlers might be configured to pass the request without processing it, causing the request to be left entirely unhandled.

Despite its drawbacks, the Chain of Responsibility remains one of the most powerful and effective design patterns.

## Conclusion

In this article, we learned how to use the Chain of Responsibility design pattern in a C# application and discussed some factors to consider when using such patterns.
