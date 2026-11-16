---
url: "https://devblogs.microsoft.com/visualstudio/how-do-i-think-about-async-code"
captured_at: "2026-11-16T03:44:50+00:00"
title: "How Do I Think About Async Code?!"
domain: "devblogs-microsoft-com"
---

Increasingly essential to writing responsive applications, asynchronous code is becoming more and more popular. Unfortunately, asynchronous programming adds an additional level of complexity to your code.  As a result, understanding how this code even works can be tough no matter your experience level.  Whether you’re new to it or you just want a refresher, here is an intro to the world of asynchronous code!

#### **What is asynchronous code?**

Asynchronous (async) programming lets you execute a block of code without stopping (or _blocking_) the entire thread where the action is being executed.  A common myth about async code is that it improves performance, which isn’t necessarily true.  Instead, the major perk of async programming is that it increases the number of tasks (_throughput_) that can be executed concurrently without having to block the thread where these actions are taking place.

You may think async code seems a little like multithreaded code.  After all, many methods could be executing at the same time in both.  In reality, async programming can be used together with singular or multithreaded applications.  This means you can have a single-threaded async program, where one thread can run concurrent tasks.  Conversely, you can also have a multi-threaded async application, where multiple threads can each run multiple concurrent tasks.

#### **Why should I use async** **code?  Example please!**

To use an analogy to demonstrate async programming, consider the action of baking a cake. This action will be represented by a thread that is executing several steps (or _tasks),_ as illustrated in code below.  This code is serviceable, and you will still have a yummy cake once the method is done executing.  However, since all the code is _synchronous_, each line will run sequentially.  In other words, you will be standing completely still while waiting for the oven to finish preheating.  You could be making the batter for your cake in the meantime!

[![Synchronous MakeCake() function](https://devblogs.microsoft.com/visualstudio/wp-content/uploads/sites/4/2020/06/SyncCake_Light.png)](https://devblogs.microsoft.com/visualstudio/wp-content/uploads/sites/4/2020/06/SyncCake_Light.png)

_Synchronous MakeCake() function_

Synchronous cake program, image

_Synchronous cake program_

In real life, you typically want to multitask by making the batter while the oven preheats or making the icing while the cake is baking.  Doing this increases your productivity and allows you to bake the cake much faster. This is where asynchronous code comes in handy!  By making our existing code asynchronous, we can perform more actions to pass the time even while we are _awaiting_ a _task_ like baking the cake in the oven to complete. To do this, we modified our code to include a new function called _PassTheTime._ This code saves a task’s state, starts running another synchronous or asynchronous function, and retrieves the saved task’s value when it’s actually needed.

[![Asynchronous MakeCake() function](https://devblogs.microsoft.com/visualstudio/wp-content/uploads/sites/4/2020/06/AsyncCake_Light.png)](https://devblogs.microsoft.com/visualstudio/wp-content/uploads/sites/4/2020/06/AsyncCake_Light.png)

_Asynchronous MakeCake() function_

Image AsyncCake Run, image

_Asynchronous cake program_

When compared to the synchronous MakeCake method that lacks a _PassTheTime_ function call, MakeCakeAsync manages to complete more tasks without blocking the thread and shortens the time it takes to execute the whole method.

Async versus sync program comparison, image

_Async versus sync program comparison_

#### **How do I write async code in .NET?**

Thankfully, C# makes it a “piece of cake” to write asynchronous code with the _[Task](https://docs.microsoft.com/en-us/dotnet/api/system.threading.tasks.task?view=netframework-4.8)_ type and the _[await](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/async)_ and _async_ keywords.  The _Task_ type tells the caller about the eventual return value type. It also indicates that other actions can execute while the caller method is being processed.  The _async_ keyword enables the _await_ keyword, which lets the compiler know that we’ll need the return value of the function, but not right away.  As a result, we don’t need to block the call and can continue running other tasks until the awaited value is needed.  An async method will initially run synchronously until it hits an _await_ keyword. This is when the asynchronous execution will begin.

#### **I just learned about async** **code!  Now what?**

While using async code to bake a cake is great, there are plenty of other real-life applications to use asynchronous code.  Two of the most common examples include:

*   **Programs using HTTP requests** – Depending on the request, HTTP calls can take a long time to fully process. Using async code can let you perform other work while waiting for the server to respond.

[![HTTP GET request example](https://devblogs.microsoft.com/visualstudio/wp-content/uploads/sites/4/2020/06/HTTPCallExample.png)](https://devblogs.microsoft.com/visualstudio/wp-content/uploads/sites/4/2020/06/HTTPCallExample.png)

_HTTP GET request example_

*   **[Programs using UI elements](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/async#example)** – WPF apps or any apps using buttons, textboxes, and other UX assets lend themselves well to async implementation. For instance, a WPF app taking in a file to be parsed may take a while.  By making this action async, you can still interact with the UI without having the app completely freeze as you wait for the function to complete.

Now that you know the basics of asynchronous programming, it’s time to improve on it!  There are a lot of secret do’s and don’ts when writing solid async code.  For a great resource that explores these tips and tricks, check out [David Fowler’s post on async programming](https://github.com/davidfowl/AspNetCoreDiagnosticScenarios/blob/master/AsyncGuidance.md).

Like all code, there will come a time where you’ll need to diagnose bugs in your async program.  To learn how to debug your async code in Visual Studio, tune in for an upcoming blog post…

Side note: And no, I did not use the cake analogy just because I’ve been doing a lot of baking recently. ![😉](https://s.w.org/images/core/emoji/17.0.2/svg/1f609.svg)

[![Red velvet cupcake](https://devblogs.microsoft.com/visualstudio/wp-content/uploads/sites/4/2020/06/Cupcake-291x300.jpg)](https://devblogs.microsoft.com/visualstudio/wp-content/uploads/sites/4/2020/06/Cupcake-291x300.jpg)

## Author

![Leslie Richardson](https://devblogs.microsoft.com/visualstudio/wp-content/uploads/sites/4/2023/03/4m_du_GZ_400x400-96x96.jpg)

Program Manager

Leslie is a Program Manager on the C# developer experience team, focusing primarily on improving the overall .NET and C# productivity experience and feature set.
