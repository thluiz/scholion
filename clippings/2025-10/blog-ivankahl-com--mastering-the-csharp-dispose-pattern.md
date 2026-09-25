---
url: "https://blog.ivankahl.com/csharp-dispose-pattern/?utm_source=bonobopress&utm_medium=newsletter&utm_campaign=2144"
captured_at: "2025-10-21T18:14:20+01:00"
title: "Mastering the C# Dispose Pattern"
domain: "blog-ivankahl-com"
---

---
The .NET runtime comes with efficient resource management, helping you build robust applications. It can allocate, manage, and reclaim memory efficiently for objects, helping prevent memory leaks and memory exhaustion. Most cleanup is done automatically. However, there are scenarios where you, as the developer, need to manually clean up unmanaged resources that the runtime cannot see.

This guide will briefly explain how .NET's resource management works and its limitations when it comes to dealing with unmanaged resources. You'll then see how the `IDisposable` interface can be implemented in different scenarios to ensure resources are cleaned up properly.

## Resource Management in .NET

The .NET runtime manages a memory heap for your application's reference types. While the runtime handles the allocation, the Garbage Collector (GC) is responsible for automatically reclaiming memory from objects that are no longer in use. It is also responsible for optimizing memory by compacting the heap. This entire process frees you from manually deallocating memory.

ℹ️

****What are Reference Types?****  
[Reference types](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/reference-types?ref=blog.ivankahl.com) are any .NET types whose values get stored on the heap instead of the stack. When you assign such a type to a variable, the variable stores a __reference__ to the object on the heap. This is unlike [value types](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/value-types?ref=blog.ivankahl.com), which store the actual value in the variable.

Since the runtime manages the memory for reference types, it's called _managed memory_. However, applications can often use _unmanaged resources._ The memory for these resources sits outside the runtime's control and visibility. Such resources can include file handles, database connections, and network sockets. Because it has no visibility of these resources, the GC has no way of compacting or reclaiming this memory automatically. Instead, the class itself needs to release these unmanaged resources to prevent memory leaks.

To solve this problem, .NET provides the `IDisposable` interface to [deterministically cleanup resources](https://learn.microsoft.com/en-us/dotnet/fundamentals/runtime-libraries/system-idisposable?ref=blog.ivankahl.com). The following section demonstrates a simple `IDisposable` implementation that is most commonly used.

## The Basic Dispose Pattern: A Simple Implementation

In most cases, your classes will work with unmanaged resources that are already wrapped in their own `IDisposable` classes.

For instance, your class might use the `NpgsqlConnection` class to establish a connection to a PostgreSQL database. Even though the database connection is an unmanaged resource, the `NpgsqlConnection` class already implements a `Dispose()` method to manage those resources. Your class's `Dispose()` method simply needs to call the database's `Dispose()` method.

This is demonstrated in the code snippet below:

Notice how the `CustomerRepository.Dispose()` method makes a call to the underlying database connection to dispose it. Now the unmanaged resource is taken care of. Nothing too complicated!

The `_disposed` field also keeps track of whether the dispose method has been called already. This is important, since your `Dispose()` method [_should_ _always be idempotent_](https://learn.microsoft.com/en-us/dotnet/standard/garbage-collection/implementing-dispose?ref=blog.ivankahl.com#implement-the-dispose-pattern-for-a-derived-class)_,_ otherwise exceptions might be thrown.

ℹ️

****Cascading**** **`**Dispose()**`** ****Calls****  
Whenever your class __owns__ a class that implements `IDisposable`, it __must__ [cascade dispose calls](https://learn.microsoft.com/en-us/dotnet/standard/garbage-collection/implementing-dispose?ref=blog.ivankahl.com#cascade-dispose-calls) down to those owned objects to ensure proper cleanup.

However, this is __not necessary__ if your class __doesn't own__ the resource (e.g., it was passed in as a dependency in the constructor).

### Consuming the `IDisposable` Class

When consuming the class above, you should use the `using` block as it automatically calls `Dispose()` for you when you're finished with the object:

Notice how the `Dispose()` method is called as soon as you reach the end of the `using` block.

You can also remove the block, in which case the `Dispose()` method will be called when the surrounding code block ends:

In the snippet above, the `Dispose()` method will be called automatically after the function returns.

## The Full Dispose Pattern: Handling Unmanaged Resources

The implementation above will suffice for most of your `IDisposable` implementations. However, there might be times when you're dealing with unmanaged resources directly (i.e., they aren't wrapped in their own `IDisposable`). In those cases, there are a couple more things to consider in your implementation.

Take a look at the implementation below:

That's a bit more code!

First, notice how the class has an `IntPtr` pointing to a file, which is created using Window's low-level `CreateFile` method. This pointer is an unmanaged resource that has to be cleaned up manually.

A `MemoryStream` is also created to act as a buffer. This is another unmanaged resource. However, because the `MemoryStream` class implements `IDisposable`, you only need to call the `Dispose()` method on that field.

There's also a new `Dispose(bool disposing)` method. It cleans up managed and unmanaged resources. This method can be called from two places in the class: the `IDisposable.Dispose()` method, or the class finalizer.

ℹ️

****What are Finalizers?****  
Finalizers are another name for destructors in C#. These methods have a simple signature: `public ~ClassName() {}`

The GC calls the finalizer before reclaiming the object's memory.

When calling the new `Dispose(bool disposing)` method, the `disposing` parameter is determined by the origin of the method call:

-   When called from `IDisposable.Dispose()`, then `disposing` is `true`, meaning both managed and unmanaged resources should be cleaned up.
-   When called from the finalizer (i.e., `~UnmanagedFileHandler()`), then `disposing` is `false`, so only unmanaged resources are cleaned up. This is because the GC will finalize the owned managed resources, so no need to `Dispose()` them ourselves.

`GC.SuppressFinalize()` is also called on the current object in the `Dispose()` method. This tells the GC that it does _not_ need to call the finalizer method on this class.

This is necessary for performance reasons, since finalizers are not exactly efficient. When the GC encounters a class with a finalizer that needs to be reclaimed, it first places that finalizer on a queue to execute later. This is to prevent the current GC run from being potentially delayed by calling the finalizer immediately. Once the current GC run is finished, the finalizer is executed. Only after the finalizer is executed does the class become eligible to be reclaimed.

![](https://blog.ivankahl.com/content/images/2025/10/GC-and-Finalizers-1.png)

Diagram illustrating how the finalizer is executed after the current GC run, delaying memory being reclaimed.

So by suppressing the finalizer on the class, the memory for that class can be immediately reclaimed without waiting for the finalizer to execute first.

Finally, you'll see the `Dispose(bool disposing)` method is `virtual`. In the next section, you'll find out why this is necessary when it comes to class inheritance with `IDisposable`.

## Disposing of Inherited Classes

What happens if a class inherits from your `IDisposable` class and uses its own unmanaged resources? The child class's resources also need to be cleaned up, along with the parent class's resources.

Fortunately, since the `Dispose(bool disposing)` method is `virtual`, a child class can execute its own cleanup logic when the class is disposed.

The code snippet below is for a `LogFileHandler` class, which inherits from the `UnmanagedFileHandler` class referenced above.

The `LogFileHandler` class has its own `MemoryStream` field, which is used to buffer log messages. This resource implements the `IDisposable` interface, so the `LogFileHandler` must override the `Dispose(bool disposing)` method from the parent class to dispose of the buffer. When overriding the method, _the base class `Dispose(bool disposing)` method must still be called._

Since the `Dispose(bool disposing)` method is already called from the `IDisposable.Dispose()` and finalizer in the base class, there's no need to implement them in the `LogFileHandler` class.

ℹ️

****What If I Never Plan On Inheriting?****  
If your `IDisposable` class will never be inherited from, [mark the class as `sealed`](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/sealed?ref=blog.ivankahl.com) and remove the `virtual` flag from the `Dispose(bool disposing)` method.

## Best Practices

When implementing any of the patterns above, keep these things in mind to ensure your disposal logic is robust.

### Ensure Idempotency

Calls to `Dispose()` should always be idempotent to avoid exceptions from being thrown. This can happen if part of disposing of a property sets it to an invalid value (like `null`):

If, for any reason, the `Dispose()` method above is called again, a `NullReferenceException` will be thrown because `_connection` was set to `null` previously.

So it's best to always use a `_disposed` private field to track if the dispose has already been run:

Now the method will return early if it's ever called multiple times.

### Don't Throw Exceptions in Finalizers

When implementing a finalizers that dispose resources, it's crucial to avoid throwing any exceptions as they can have unintended side effects, [like causing the entire application to crash](https://stackoverflow.com/questions/20358401/throwing-exception-in-finalizer-to-enforce-dispose-calls?ref=blog.ivankahl.com).

Always write your finalizers as defensively as possible to prevent unhandled exceptions from surfacing.

### Cascade Dispose Calls to Owned Resources

Any class that owns resources that implement `IDisposable` must implement the `IDisposable` interface and call the `Dispose()` method on those resources in its own `Dispose()` method. If not done, owned resources won't be released, which could cause memory leaks.

### Always Call Base Class Dispose

If a class inherits from another class implementing `IDisposable`, make sure you override the `Dispose(bool disposing)` method to release any unmanaged resources in the inherited class.

Also, always _call the base class's `Dispose(bool disposing)` method from the overridden method._

### Use `SafeHandle` to Managed Those Unmanaged Resources

The full Dispose pattern is necessary if your class deals with unmanaged resources directly (i.e., the resources don't have an existing `IDisposable` wrapper, such as `IntPtr`). However, the .NET runtime comes with `SafeHandle` classes that can wrap any raw unmanaged `IntPtr` in an `IDisposable`. These wrapper classes manage the pointer for you, meaning your class only needs to implement [the Basic Dispose pattern](https://blog.ivankahl.com/csharp-dispose-pattern/?utm_source=bonobopress&utm_medium=newsletter&utm_campaign=2144#the-basic-dispose-pattern-a-simple-implementation).

The [official documentation goes into great detail on `SafeHandles` and how they simplify disposing of a class](https://learn.microsoft.com/en-us/dotnet/standard/garbage-collection/implementing-dispose?ref=blog.ivankahl.com#safe-handles).

### Disposing Asynchronously with `IAsyncDisposable`

When your class holds resources that involve asynchronous operations during cleanup (like closing a database connection or releasing a lock), you should implement the `IAsyncDisposable` instead of (or in addition to) `IDisposable`. This allows for non-blocking cleanup, keeping your application responsive.

The `IAsyncDisposable` interface [expects a `ValueTask DisposeAsync()` method to be implemented](https://source.dot.net/?ref=blog.ivankahl.com#System.Private.CoreLib/src/libraries/System.Private.CoreLib/src/System/IAsyncDisposable.cs).

Below is an example of implementing the `IAsyncDisposable` interface:

Consuming an `IAsyncDisposable` class is similar to the `IDisposable` class. You just need to add `await` to your using statement:

## Conclusion

While the .NET GC does a great job of managing memory, it cannot clean unmanaged resources, like low-level file handles or database connections. The `IDisposable` interface helps ensure all managed and unmanaged resources are cleaned up deterministically.

Hopefully, this guide has shed some light on the Dispose pattern in C#. In most cases, you'll stick to the first, simple implementation. However, if you ever have to clean up unmanaged resources manually, a bit more code is needed to make it work.

By implementing the `IDisposable` interface properly, you'll reduce the number of potential memory leaks, resulting in a robust and stable end product.
