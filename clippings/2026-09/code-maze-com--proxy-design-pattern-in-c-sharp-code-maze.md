---
url: "https://code-maze.com/csharp-proxy-design-pattern/?ref=dailydev"
captured_at: "2026-09-24T23:18:02+01:00"
title: "Proxy Design Pattern in C# - Code Maze"
domain: "code-maze-com"
---

In this article, we are going to talk about a structural design pattern, the Proxy Pattern. We will discuss what problem this pattern solves and how to implement it in C#.

To download the source code for this article, you can visit our [GitHub repository](https://github.com/CodeMazeBlog/CodeMazeGuides/tree/main/csharp-design-patterns/ProxyPattern).

If you want to read more about design patterns in C#, you can inspect our [C# Design Patterns](https://code-maze.com/design-patterns-csharp/) page.

Let’s start.

## What is The Proxy Design Pattern?

**The Proxy design pattern allows us to introduce an extra layer of control over access to an object.** **This access control comes with the provision of a wrapper object (`Proxy`) that acts on behalf of the original object (`RealSubject`).** Since the proxy mimics the real subject, it essentially needs to implement the same set of contracts (`ISubject`) as the real subject does:

[![Proxy Design Pattern in C# Diagram-Flow](https://code-maze.com/wp-content/uploads/2024/06/Proxy-Design-Pattern-5.png)](https://code-maze.com/wp-content/uploads/2024/06/Proxy-Design-Pattern-5.png)

As the class diagram states, the `Proxy` operates and serves the result to the client using the same interface (or abstract class) as the `RealSubject` does. Under the hood, it holds a reference to the `realSubject` instance.

During the `operation()`, the proxy delegates the call to `realSubject.operation()` before/after doing some other actions by itself.

## What Problem Does The Proxy Pattern Solve?

As we know, each design pattern is meant for solving a particular set of problems. So exactly what problem does a proxy pattern solve?

Well, it can help us in a variety of cases but they all seek one common goal – **incorporating additional logic without changing the functionality and intent of the original object.**

As an example, let’s imagine we are using a data service that fetches exchange rates from a remote API service:

public class ExchangeRateService : IExchangeRateService
{
    public ExchangeRate\[\] GetExchangeRates()
    {
        // In real-world application, this data comes from a remote API service
        ExchangeRate\[\] data = \[
            new("CAD", 0.73m),
            new("EUR", 1.07m),
            new("GBP", 1.27m),
        \];

        Console.WriteLine("Fetched data from remote service");

        return data;   
    }
}

And, we call this data service throughout the application whenever we need exchange-rates data:

var service = new ExchangeRateService();

for (int i = 1; i <= 3; i++)
{
    Console.WriteLine($"Request {i}");

    \_ = service.GetExchangeRates();
}

Every time we call this data service, it sends a request to the remote service:

Request 1
Fetched data from remote service
Request 2
Fetched data from remote service
Request 3
Fetched data from remote service

Now the problem is, that exchange rates usually do not change so frequently, and initiating a network communication for every such request is bad for performance. A wiser approach is to load data from the remote service once, cache it for a certain duration, and serve the cached data on subsequent requests.

**However, client code shouldn’t be bothered about how data is provided and the data service shouldn’t be coupled to the caching layer. That means neither client nor the data service should be altered for this purpose.**

Free ebook

Is your Web API ready for production?

33 things to check before you ship, with the fix for each one. A free 76-page PDF for .NET 10.

[Get the free checklist](https://code-maze.com/free-ebook-aspnetcore-webapi-best-practices/?box=3)

Free PDF. One email to send it. Unsubscribe any time.

![The Web API Production Checklist, free ebook](https://code-maze.com/wp-content/uploads/ebooks/covers/cover-beige-2-chevron-400.webp)

So how can we solve this problem?

A proxy service comes to the rescue! It can encapsulate all the logic that ties the caching layer to the data service layer while offering the same interface to the client code.

## Implement a Caching Proxy in C#

Let’s see how we can implement such a caching proxy.

As the pattern states, we must implement the contract of actual data service i.e. the `IExchangeRateService` interface:

public interface IExchangeRateService
{
    ExchangeRate\[\] GetExchangeRates();
}

Keeping this in mind, let’s go for the proxy implementation:

public class CachedExchangeRateService : IExchangeRateService
{
    private readonly IExchangeRateService \_exchangeRateService;
    private ExchangeRate\[\]? \_exchangeRates;

    public CachedExchangeRateService()
    {
        \_exchangeRateService = new ExchangeRateService();
    }

    public ExhangeRate\[\] GetExchangeRates()
    {
        if (\_exchangeRates is null)
        {
            \_exchangeRates = \_exchangeRateService.GetExchangeRates();

            return \_exchangeRates;
        }

        Console.WriteLine("Read data from cache");

        return \_exchangeRates;
    }
}

We first initialize a local instance of the original `ExchangeRateService` in the constructor. We also need a local cache of `_exchangeRates` to hold the result obtained from the service operation.

The next thing is, of course, to implement the `GetExchangeRates()` method of  `IExchangeRateService` interface. Inside this method, we serve the result directly from `_exchangeRates` if it already has data. If we don’t have that, we fetch data by invoking the `GetExchangeRates()` method of the original service instance and store the data into `_exchangeRates`. Also, we make things interesting by adding some logging. 

What’s more interesting is, that to use this proxy implementation, we don’t need any change in the client code except only switching to the proxy constructor:

var service = new CachedExchangeRateService();

for (int i = 1; i <= 3; i++)
{
    Console.WriteLine($"Request {i}");

    \_ = service.GetExchangeRates();
}

And, if we inspect the log:

Request 1
Fetched data from remote service
Request 2
Read data from cache
Request 3
Read data from cache

We see data is being read from the cache as expected!

That’s how we can leverage a caching proxy on top of a remote data service without altering the existing client and service.

## Other Use Cases of Proxy Pattern

Apart from caching proxy, there are many other cases where we can apply proxy design patterns. Let’s explore some of them in brief.

**Logging proxy** – A proxy class is a good way to add enhanced logging and monitoring around a service, especially when we deal with third-party library classes.

**Protection proxy** – Sometimes we want to protect a service execution from certain incoming requests. This might be the case when we want to validate request parameters or restrict calls from unauthorized clients. A proxy allows us to intercept such requests and perform validation/security checks before delegating the request to the actual service.

Free ebook

Is your Web API ready for production?

33 things to check before you ship, with the fix for each one. A free 76-page PDF for .NET 10.

[Get the free checklist](https://code-maze.com/free-ebook-aspnetcore-webapi-best-practices/?box=3)

Free PDF. One email to send it. Unsubscribe any time.

![The Web API Production Checklist, free ebook](https://code-maze.com/wp-content/uploads/ebooks/covers/cover-beige-2-chevron-400.webp)

**Remote proxy** – When working with remote services, we often need additional code for warm-up procedures, fault tolerance, exception handling, and other hectic network communication drills. A proxy is an effective way to encapsulate such logic and keep the client code clean and maintainable.

**Virtual proxy** – For performance concerns, it’s important to control the lifecycle of a resource-intensive service. An effective strategy is to perform deferred initialization or on-demand instantiation, intermediate caching, and disposal when unused. All such controls can be put in a proxy class without disrupting existing uses in client code.

**Selection proxy** – A proxy also offers a convenient way to [conditionally resolve a certain service variant](https://code-maze.com/dotnet-conditionally-resolve-dependencies/) from different available variants and delegate the client’s request accordingly. Such proxies are handy to deal with fallback and backward-compatible service operations.

## Caveats of Proxy Pattern

Proxy is a powerful design technique to address certain categories of problems. That said, like any other design pattern, it is not a cure-all solution. **The improper use of it might bring more problems than it solves.**

Since a proxy brings in an extra layer of abstraction, it might lead to **additional complexity and maintenance overhead**. The overhead is even more when there are more dependencies involved. For example, when the constructor dependencies in the actual subject get changed, we need relevant changes in the proxy class as well. On top of it, if we deal with asynchronous or multithreaded operations, we may need more provisions before and after delegating that operation to the actual subject.

**Although the performance cost of an additional proxy layer might be negligible in many cases, it might be a significant concern for performance-critical applications**. Virtual proxies are more prone to performance degradation due to improper lifecycle management.

**Maintaining state synchronization between the real object and the proxy might be challenging** too. For example, in the case of a caching proxy, it might get tricky to invalidate the cache and ensure that no stale data is served to the client.

Another potential drawback is **leaky abstraction**. This might happen for virtual and caching proxies if the client needs knowledge of lifecycle events and cache invalidation events.

Last but not least, while a protection proxy offers a convenient way of access control, **relying solely on it for security is dangerous**.

In a nutshell, it is crucial to assess the benefits as well as the trade-offs while introducing a proxy. It is also important to carry out performance profiling when a proxy is involved.

## Conclusion

In this article, we have learned how to employ the Proxy Design pattern in a C# application. We have demonstrated how this pattern can help us solve particular problems. We have also discussed some factors we should consider while using such patterns.

**Like always, a specific design pattern should not be imposed, rather it should come as a natural choice for solving a particular problem**.
