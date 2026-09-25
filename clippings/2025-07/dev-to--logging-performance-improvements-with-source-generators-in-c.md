---
url: "https://dev.to/rmaurodev/logging-performance-improvements-with-source-generators-in-c-net-531c?context=digest"
captured_at: "2025-07-17T13:23:10+01:00"
title: "Logging Performance Improvements with Source Generators in C# .NET - DEV Community"
domain: "dev-to"
---

---
In recent .NET releases, source generators have become a game-changer, offering new possibilities for compile-time code generation. One area where source generators have made a significant impact is logging.

In this post, we will explore how to use source generators for logging, the improvements and benefits they bring, and some practical tips to get the most out of this feature.

## [](https://dev.to/rmaurodev/logging-performance-improvements-with-source-generators-in-c-net-531c?context=digest#logging-with-source-generators)Logging with Source Generators

Using source generators for logging in .NET can help streamline logging calls, reduce overhead, and provide more efficient, type-safe logging.

The `Microsoft.Extensions.Logging` namespace has integrated support for source-generated logging, which we will explore in detail.

### [](https://dev.to/rmaurodev/logging-performance-improvements-with-source-generators-in-c-net-531c?context=digest#setting-up-sourcegenerated-logging)Setting Up Source-Generated Logging

To get started, you need to ensure you have the necessary packages. Typically, you would include the following in your project:  

```
dotnet add package Microsoft.Extensions.Logging
dotnet add package Microsoft.Extensions.Logging.Abstractions
```

Next, you need to enable the logging source generator. This is done by defining logging methods in a static partial class with the `LoggerMessage` attribute.

Here’s an example:  

```
<span>using</span> <span>Microsoft.Extensions.Logging</span><span>;</span>

<span>public</span> <span>static</span> <span>partial</span> <span>class</span> <span>Log</span>
<span>{</span>
    <span>[</span><span>LoggerMessage</span><span>(</span><span>EventId</span> <span>=</span> <span>0</span><span>,</span> <span>Level</span> <span>=</span> <span>LogLevel</span><span>.</span><span>Information</span><span>,</span> <span>Message</span> <span>=</span> <span>"Processing item {ItemId}"</span><span>)]</span>
    <span>public</span> <span>static</span> <span>partial</span> <span>void</span> <span>ProcessingItem</span><span>(</span><span>ILogger</span> <span>logger</span><span>,</span> <span>int</span> <span>itemId</span><span>);</span>

    <span>[</span><span>LoggerMessage</span><span>(</span><span>EventId</span> <span>=</span> <span>1</span><span>,</span> <span>Level</span> <span>=</span> <span>LogLevel</span><span>.</span><span>Error</span><span>,</span> <span>Message</span> <span>=</span> <span>"Failed to process item {ItemId}: {ErrorMessage}"</span><span>)]</span>
    <span>public</span> <span>static</span> <span>partial</span> <span>void</span> <span>ProcessingItemFailed</span><span>(</span><span>ILogger</span> <span>logger</span><span>,</span> <span>int</span> <span>itemId</span><span>,</span> <span>string</span> <span>errorMessage</span><span>);</span>
<span>}</span>

```

### [](https://dev.to/rmaurodev/logging-performance-improvements-with-source-generators-in-c-net-531c?context=digest#using-the-generated-logging-methods)Using the Generated Logging Methods

With the logging methods defined, you can use them in your application as follows:  

```
<span>public</span> <span>void</span> <span>ProcessItem</span><span>(</span><span>int</span> <span>itemId</span><span>)</span>
<span>{</span>
    <span>try</span>
    <span>{</span>
        <span>// Processing logic here</span>
        <span>Log</span><span>.</span><span>ProcessingItem</span><span>(</span><span>_logger</span><span>,</span> <span>itemId</span><span>);</span>
    <span>}</span>
    <span>catch</span> <span>(</span><span>Exception</span> <span>ex</span><span>)</span>
    <span>{</span>
        <span>Log</span><span>.</span><span>ProcessingItemFailed</span><span>(</span><span>_logger</span><span>,</span> <span>itemId</span><span>,</span> <span>ex</span><span>.</span><span>Message</span><span>);</span>
    <span>}</span>
<span>}</span>
```

## [](https://dev.to/rmaurodev/logging-performance-improvements-with-source-generators-in-c-net-531c?context=digest#behind-the-scenes-the-generated-code)Behind the Scenes: The Generated Code

During the compilation of the project the partial class for `Log` will generated and compiled along with the source code.

[![Logging Performance Improvements with Source Generators in C# .NET](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fctz2pwke1oswzajjhjz7.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fctz2pwke1oswzajjhjz7.png)

Observe the generated code for the logging methods.  

```
<span>partial</span> <span>class</span> <span>Log</span>
<span>{</span>
    <span>/// &lt;summary&gt;</span>
    <span>/// Logs "Processing item {ItemId}" at "Information" level.</span>
    <span>/// &lt;/summary&gt;</span>
    <span>[</span><span>global</span><span>::</span><span>System</span><span>.</span><span>CodeDom</span><span>.</span><span>Compiler</span><span>.</span><span>GeneratedCodeAttribute</span><span>(</span><span>"Microsoft.Gen.Logging"</span><span>,</span> <span>"8.2.0.0"</span><span>)]</span>
    <span>public</span> <span>static</span> <span>partial</span> <span>void</span> <span>ProcessingItem</span><span>(</span><span>global</span><span>::</span><span>Microsoft</span><span>.</span><span>Extensions</span><span>.</span><span>Logging</span><span>.</span><span>ILogger</span> <span>logger</span><span>,</span> <span>int</span> <span>itemId</span><span>)</span>
    <span>{</span>
        <span>if</span> <span>(!</span><span>logger</span><span>.</span><span>IsEnabled</span><span>(</span><span>global</span><span>::</span><span>Microsoft</span><span>.</span><span>Extensions</span><span>.</span><span>Logging</span><span>.</span><span>LogLevel</span><span>.</span><span>Information</span><span>))</span>
        <span>{</span>
            <span>return</span><span>;</span>
        <span>}</span>

        <span>var</span> <span>state</span> <span>=</span> <span>global</span><span>::</span><span>Microsoft</span><span>.</span><span>Extensions</span><span>.</span><span>Logging</span><span>.</span><span>LoggerMessageHelper</span><span>.</span><span>ThreadLocalState</span><span>;</span>

        <span>_</span> <span>=</span> <span>state</span><span>.</span><span>ReserveTagSpace</span><span>(</span><span>2</span><span>);</span>
        <span>state</span><span>.</span><span>TagArray</span><span>[</span><span>1</span><span>]</span> <span>=</span> <span>new</span><span>(</span><span>"ItemId"</span><span>,</span> <span>itemId</span><span>);</span>
        <span>state</span><span>.</span><span>TagArray</span><span>[</span><span>0</span><span>]</span> <span>=</span> <span>new</span><span>(</span><span>"{OriginalFormat}"</span><span>,</span> <span>"Processing item {ItemId}"</span><span>);</span>

        <span>logger</span><span>.</span><span>Log</span><span>(</span>
            <span>global</span><span>::</span><span>Microsoft</span><span>.</span><span>Extensions</span><span>.</span><span>Logging</span><span>.</span><span>LogLevel</span><span>.</span><span>Information</span><span>,</span>
            <span>new</span><span>(</span><span>0</span><span>,</span> <span>nameof</span><span>(</span><span>ProcessingItem</span><span>)),</span>
            <span>state</span><span>,</span>
            <span>null</span><span>,</span>
            <span>[</span><span>global</span><span>::</span><span>System</span><span>.</span><span>CodeDom</span><span>.</span><span>Compiler</span><span>.</span><span>GeneratedCodeAttribute</span><span>(</span><span>"Microsoft.Gen.Logging"</span><span>,</span> <span>"8.2.0.0"</span><span>)]</span> <span>static</span> <span>string</span> <span>(</span><span>s</span><span>,</span> <span>_</span><span>)</span> <span>=&gt;</span>
            <span>{</span>
                <span>var</span> <span>itemId</span> <span>=</span> <span>s</span><span>.</span><span>TagArray</span><span>[</span><span>1</span><span>].</span><span>Value</span><span>;</span>
                <span>return</span> <span>global</span><span>::</span><span>System</span><span>.</span><span>FormattableString</span><span>.</span><span>Invariant</span><span>(</span><span>$"Processing item </span><span>{</span><span>itemId</span><span>}</span><span>"</span><span>);</span>
            <span>});</span>

        <span>state</span><span>.</span><span>Clear</span><span>();</span>
    <span>}</span>

    <span>/// &lt;summary&gt;</span>
    <span>/// Logs "Failed to process item {ItemId}: {ErrorMessage}" at "Error" level.</span>
    <span>/// &lt;/summary&gt;</span>
    <span>[</span><span>global</span><span>::</span><span>System</span><span>.</span><span>CodeDom</span><span>.</span><span>Compiler</span><span>.</span><span>GeneratedCodeAttribute</span><span>(</span><span>"Microsoft.Gen.Logging"</span><span>,</span> <span>"8.2.0.0"</span><span>)]</span>
    <span>public</span> <span>static</span> <span>partial</span> <span>void</span> <span>ProcessingItemFailed</span><span>(</span><span>global</span><span>::</span><span>Microsoft</span><span>.</span><span>Extensions</span><span>.</span><span>Logging</span><span>.</span><span>ILogger</span> <span>logger</span><span>,</span> <span>int</span> <span>itemId</span><span>,</span> <span>string</span> <span>errorMessage</span><span>)</span>
    <span>{</span>
        <span>var</span> <span>state</span> <span>=</span> <span>global</span><span>::</span><span>Microsoft</span><span>.</span><span>Extensions</span><span>.</span><span>Logging</span><span>.</span><span>LoggerMessageHelper</span><span>.</span><span>ThreadLocalState</span><span>;</span>

        <span>_</span> <span>=</span> <span>state</span><span>.</span><span>ReserveTagSpace</span><span>(</span><span>3</span><span>);</span>
        <span>state</span><span>.</span><span>TagArray</span><span>[</span><span>2</span><span>]</span> <span>=</span> <span>new</span><span>(</span><span>"ItemId"</span><span>,</span> <span>itemId</span><span>);</span>
        <span>state</span><span>.</span><span>TagArray</span><span>[</span><span>1</span><span>]</span> <span>=</span> <span>new</span><span>(</span><span>"ErrorMessage"</span><span>,</span> <span>errorMessage</span><span>);</span>
        <span>state</span><span>.</span><span>TagArray</span><span>[</span><span>0</span><span>]</span> <span>=</span> <span>new</span><span>(</span><span>"{OriginalFormat}"</span><span>,</span> <span>"Failed to process item {ItemId}: {ErrorMessage}"</span><span>);</span>

        <span>logger</span><span>.</span><span>Log</span><span>(</span>
            <span>global</span><span>::</span><span>Microsoft</span><span>.</span><span>Extensions</span><span>.</span><span>Logging</span><span>.</span><span>LogLevel</span><span>.</span><span>Error</span><span>,</span>
            <span>new</span><span>(</span><span>1</span><span>,</span> <span>nameof</span><span>(</span><span>ProcessingItemFailed</span><span>)),</span>
            <span>state</span><span>,</span>
            <span>null</span><span>,</span>
            <span>[</span><span>global</span><span>::</span><span>System</span><span>.</span><span>CodeDom</span><span>.</span><span>Compiler</span><span>.</span><span>GeneratedCodeAttribute</span><span>(</span><span>"Microsoft.Gen.Logging"</span><span>,</span> <span>"8.2.0.0"</span><span>)]</span> <span>static</span> <span>string</span> <span>(</span><span>s</span><span>,</span> <span>_</span><span>)</span> <span>=&gt;</span>
            <span>{</span>
                <span>var</span> <span>itemId</span> <span>=</span> <span>s</span><span>.</span><span>TagArray</span><span>[</span><span>2</span><span>].</span><span>Value</span><span>;</span>
                <span>var</span> <span>errorMessage</span> <span>=</span> <span>s</span><span>.</span><span>TagArray</span><span>[</span><span>1</span><span>].</span><span>Value</span> <span>??</span> <span>"(null)"</span><span>;</span>
                <span>return</span> <span>global</span><span>::</span><span>System</span><span>.</span><span>FormattableString</span><span>.</span><span>Invariant</span><span>(</span><span>$"Failed to process item </span><span>{</span><span>itemId</span><span>}</span><span>: </span><span>{</span><span>errorMessage</span><span>}</span><span>"</span><span>);</span>
            <span>});</span>

        <span>state</span><span>.</span><span>Clear</span><span>();</span>
    <span>}</span>
<span>}</span>
```

## [](https://dev.to/rmaurodev/logging-performance-improvements-with-source-generators-in-c-net-531c?context=digest#improvements-and-benefits)Improvements and Benefits

1.  **Performance** : Source-generated logging methods are more performant than traditional logging methods because the code is generated at compile time, avoiding reflection and dynamic code generation at runtime.
    
2.  **Type Safety** : The generated methods provide type-safe logging. If you change the parameters or the message template, you will get compile-time errors instead of runtime issues.
    
3.  **Reduced Boilerplate** : You write the logging methods once, and the source generator takes care of the rest, reducing the amount of repetitive code in your project.
    
4.  **Consistency** : Ensures that logging messages are consistent across the application, as they are defined in one place.
    

## [](https://dev.to/rmaurodev/logging-performance-improvements-with-source-generators-in-c-net-531c?context=digest#practical-tips)Practical Tips

-   **Use Descriptive Names** : When defining logging methods, use descriptive names and message templates to make it clear what each log entry represents.
    
-   **Keep It Organized** : Group related logging methods in the same partial class to keep your code organized.
    
-   **Event IDs** : Use unique event IDs for each logging method to help with filtering and analyzing logs.
    
-   **Log Levels** : Carefully choose the appropriate log level (e.g., Information, Error, Warning) to avoid cluttering your logs with unnecessary information.
    
-   **Template Matching** : Ensure that the message templates match the method parameters exactly to avoid runtime errors.
    

### [](https://dev.to/rmaurodev/logging-performance-improvements-with-source-generators-in-c-net-531c?context=digest#keeping-organized)Keeping Organized

Group related logging methods in the same partial class to keep your code organized.  

```
<span>using</span> <span>Microsoft.Extensions.Logging</span><span>;</span>

<span>namespace</span> <span>TodoList</span><span>;</span>

<span>public</span> <span>static</span> <span>partial</span> <span>class</span> <span>Log</span>
<span>{</span>
    <span>[</span><span>LoggerMessage</span><span>(</span><span>EventId</span> <span>=</span> <span>0</span><span>,</span> <span>Level</span> <span>=</span> <span>LogLevel</span><span>.</span><span>Information</span><span>,</span> <span>Message</span> <span>=</span> <span>"Processing item {ItemId}"</span><span>)]</span>
    <span>public</span> <span>static</span> <span>partial</span> <span>void</span> <span>ProcessingItem</span><span>(</span><span>ILogger</span> <span>logger</span><span>,</span> <span>int</span> <span>itemId</span><span>);</span>

    <span>[</span><span>LoggerMessage</span><span>(</span><span>EventId</span> <span>=</span> <span>1</span><span>,</span> <span>Level</span> <span>=</span> <span>LogLevel</span><span>.</span><span>Error</span><span>,</span> <span>Message</span> <span>=</span> <span>"Failed to process item {ItemId}: {ErrorMessage}"</span><span>)]</span>
    <span>public</span> <span>static</span> <span>partial</span> <span>void</span> <span>ProcessingItemFailed</span><span>(</span><span>ILogger</span> <span>logger</span><span>,</span> <span>int</span> <span>itemId</span><span>,</span> <span>string</span> <span>errorMessage</span><span>);</span>
<span>}</span>

<span>public</span> <span>class</span> <span>Todo</span><span>(</span><span>ILogger</span><span>&lt;</span><span>Todo</span><span>&gt;</span> <span>logger</span><span>)</span>
<span>{</span>
    <span>public</span> <span>void</span> <span>ProcessItem</span><span>(</span><span>int</span> <span>itemId</span><span>)</span>
    <span>{</span>
        <span>try</span>
        <span>{</span>
            <span>// Processing logic here</span>
            <span>Log</span><span>.</span><span>ProcessingItem</span><span>(</span><span>logger</span><span>,</span> <span>itemId</span><span>);</span>
        <span>}</span>
        <span>catch</span> <span>(</span><span>Exception</span> <span>ex</span><span>)</span>
        <span>{</span>
            <span>Log</span><span>.</span><span>ProcessingItemFailed</span><span>(</span><span>logger</span><span>,</span> <span>itemId</span><span>,</span> <span>ex</span><span>.</span><span>Message</span><span>);</span>
        <span>}</span>
    <span>}</span>
<span>}</span>
```

## [](https://dev.to/rmaurodev/logging-performance-improvements-with-source-generators-in-c-net-531c?context=digest#conclusion)Conclusion

Source generators provide a powerful way to improve logging in .NET applications.

By generating logging code at compile time, you can achieve better performance, type safety, and consistency. Incorporate source-generated logging into your projects to take advantage of these benefits and streamline your logging implementation.

If you have any questions or would like to see more examples, feel free to reach out. Happy coding!

___

For more detailed articles and hands-on tutorials on .NET and C#, check out my blog at [rmauro.dev](https://rmauro.dev/). Subscribe to my newsletter, Developers Garage, for weekly updates and curated content.
