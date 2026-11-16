---
url: "https://web.archive.org/web/20200808064046id_/https://killalldefects.com/2020/01/16/dotnet-threading-gotchas/"
captured_at: "2026-11-16T07:58:37+00:00"
title: ".NET Threading Gotchas - Kill All Defects"
domain: "web-archive-org"
---

In this article, I’ll go over the top 5 threading mistakes I see in .NET applications and explain how to fix them. While threading is a complex topic with many different facets, these 5 mistakes represent the majority of beginner mistakes around threading.

I’m going to omit the mistake of “not using thread safety when you should” from this list, and instead focus on areas where you might accidentally make a mistake while attempting to handle threaded scenarios.

## Synchronous Async/Await

.NET’s `async` / `await` keywords make asynchronous programming significantly easier than it was in earlier iterations. However, this ease can make it tempting to propagate anti-patterns.

Sometimes code offers both a synchronous and an async implementation of an operation. Most developers would agree that an async approach is inherently better, but is it really?

Think about it this way: in an async operation, you need to spin up a new thread, wait for the thread to start, and then rejoin the original call. Additionally, that thread still needs to perform the same operation that the synchronous implementation does.

This means that async operations often cost _more_ than their synchronous variants.

So what am I saying? That async code is bad?

Threading certainly isn’t _bad_, but it’s something you need to be intelligent about. Asynchronous operations can allow the user interface to be responsive during long-running operations or allow you to perform operations in parallel.

Take a look at the following code:

![](https://i1.wp.com/killalldefects.com/wp-content/uploads/2020/01/Async1.png?w=770&ssl=1)

At first it might look like this is efficient, but what we’re actually saying here is:

1.  Run the `PlotDominationAsync` method and wait for it to complete
2.  Run the `DeployTroopsAsync` method and wait for it to complete
3.  Run the `EstablishEvilHeadquartersAsync` method and wait for it to complete
4.  Run the `LaunchDeathRayAsync` method and wait for it to complete

Here we’re paying for the overhead of threading four times while still executing methods synchronously. In this specific example we get all of the penalties for threading with none of the benefits.

Don’t do this.

Instead, use the `Task.WhenAll` method:

![](https://i1.wp.com/killalldefects.com/wp-content/uploads/2020/01/AsyncFixed.png?w=770&ssl=1)

This will limit your wait operation to the longest running task and actually introduce benefits from async code.

_Note that this example assumes that these four tasks can be run in any order._

## ConfigureAwait

Take a look at the following snippet:

`await ProgramKillerRobotsAsync`

The `await` keyword will _by default_ wait for a task to complete and attempt to join the original `SynchronizationContext` that started the operation. This can vary by programming platform (WPF vs WinForms vs ASP .NET for example).

This might not sound too bad, but imagine a busy web server that handles a large number of requests per second. In this scenario, waiting for the original context can create artificial delays and even deadlocks in some scenarios.

To combat this, we use the `ConfigureAwait` method on an awaitable operation like so:

`await ProgramKillerRobotsAsync.ConfigureAwait(false)`

Here we’re telling .NET that we don’t care what `SynchronizationContext` the operation resumes on. This is far more efficient in busy environments.

Of course, this is not a viable strategy in scenarios where you have certain special threads such as a user interface thread. In those cases, sometimes you _do_ want to ensure that you only perform operations on the same thread. In this case, you can omit `ConfigureAwait` or specify `ConfigureAwait(true)` to retain the same threading preference.

_Note: ASP .NET Core will by default not use a [SynchronizationContext](https://docs.microsoft.com/en-us/dotnet/api/system.threading.synchronizationcontext), meaning that `ConfigureAwait` doesn’t impact its performance in one way_ or _another. For .NET Framework applications, however, it is important._

## Using the Wrong Collection

In scenarios where you have potentially multiple threads interacting with a collection, your choice of collection classes matter.

Specifically, you need to make a conscious decision on if you _want_ your collection to be thread safe and, if so, how you want to accomplish that.

If you’re running in a scenario where multiple threads can manipulate the same collection, chances are that the collection _should_ have a thread safety strategy around it.

Take a look at the following example:

![](https://i0.wp.com/killalldefects.com/wp-content/uploads/2020/01/Async3.png?fit=770%2C446&ssl=1)

Here it’s possible for the underlying collection to be changed between checking for a key’s presence and retrieving that value, which could result in threading-related bugs.

At the most manual level, you can introduce a lock object every time the collection is interacted with:

![](https://i1.wp.com/killalldefects.com/wp-content/uploads/2020/01/Async4.png?fit=770%2C664&ssl=1)

This is better, but now we’ve accepted a certain degree of responsibility and risk over our threaded code. We’re essentially promising that any time we work with our collection that we will remember to use the `_myDataLock` and use it appropriately.

.NET gives us better tools than this.

In the [concurrent collections namespace](https://docs.microsoft.com/en-us/dotnet/api/system.collections.concurrent?view=netframework-4.8), we have a handful of thread-safe collections which simplify collection management in scenarios like this.

In the case of our example, we can use the [ConcurrentDictionary](https://docs.microsoft.com/en-us/dotnet/api/system.collections.concurrent.concurrentdictionary-2?view=netframework-4.8) class to handle multi-threading for us. Let’s take a look at the code:

![](https://i2.wp.com/killalldefects.com/wp-content/uploads/2020/01/Async5.png?w=770&ssl=1)

As with anything else in technology, there are tradeoffs to using concurrent collections. Because these classes assume thread safety as their responsibility, if you use them in scenarios where you don’t need that thread safety, you will be paying for the safety overhead in terms of slower performance.

For this reason, do not always default to thread safe collections, but they are a tool in your toolkit for scenarios where you need them.

## Static Classes / State

When working with static classes or singletons, thread safety becomes hard to manage.

If you are introducing some form of static state, you should plan on that state being accessed from multiple threads simultaneously at some point in the future.

Even if your main application uses threads infrequently, the presence of any sort of static state can wreak havoc on unit tests running in parallel, leading to inconsistent tests, hard to debug test failures, and tests that only fail when run in a certain order or alongside specific other tests.

In short, static state is a great way to lose hours of your time and wind up relying less on your unit tests at the same time.

My recommendation is to avoid static state whenever possible due to these concerns.

If this is somehow not possible, I recommend you use thread safe collections and lock statements as appropriate from the beginning, because if you don’t threading problems will arise later and it may take some time to track them down to the static state.

## Threads work on the IL Level

Finally, let’s take a look at a common point of confusion with threads by starting with an example:

![](https://i0.wp.com/killalldefects.com/wp-content/uploads/2020/01/Async6.png?resize=223%2C119&ssl=1)

This is a very simple method. You wouldn’t think this would have issues, but imagine if you had 50 threads calling to the same method on an instance in parallel. Odds are that you’re not likely to wind up with `DoggosPetted` being 50 at the end of that test run.

Why is this?

When we read code, we tend to think about things at a line by line or statement by statement basis. In this example we read this and think “Increase `DoggosPetted` by 1″.

However, this is not what the Common Language Runtime (CLR) sees. The CLR sees statements akin to the following:

```
Read the value of DoggosPetted
Add 1 to the register
Do an add operation between 1 and the value read from DoggosPetted
Store the result of that operation in DoggosPetted
```

In a multi-threaded environment, if the CLR context switches to a different thread _after_ the prior thread has read from `DoggosPetted` but _before_ it adds one and stores the new value back into `DoggosPetted`, you will overwrite any adds that threads have accomplished in that time.

Since working with a `lock` statement here would be a painful way of managing field state, .NET provides `Interlocked` operations to perform atomic operations with shared state.

Let’s take a look and see what I mean:

![](https://i2.wp.com/killalldefects.com/wp-content/uploads/2020/01/Async7.png?resize=409%2C119&ssl=1)

[Interlocked](https://docs.microsoft.com/en-us/dotnet/api/system.threading.interlocked?view=netframework-4.8) also provides methods to decrement, add, remove, and exchange integers, among other operations.

While talking about things at this level is a bit like getting into the weeds, it is important to understand that the way we read code and the way the CLR reads code is different and this can lead to problems in areas you don’t expect until you’ve been bitten by them.

## Additional Resources

While these are the most common threading issues in .NET in my experience, this list is in no way exhaustive.

There are a lot of things that can go wrong with threading and many people who have dug in at an expert level to provide in-depth resources.

If you want to learn more about threading and potential mistakes, I highly recommend giving the [Async Guidance page](https://github.com/davidfowl/AspNetCoreDiagnosticScenarios/blob/master/AsyncGuidance.md) a view on GitHub.
