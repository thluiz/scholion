---
url: "https://code-maze.com/dotnet-dynamically-change-the-servicelifetime-of-a-registered-service/?ref=dailydev"
captured_at: "2026-09-24T23:18:52+01:00"
title: "Dynamically Change the ServiceLifetime of a Registered Service in .NET - Code Maze"
domain: "code-maze-com"
---

Updated on July 19, 2026

Managing dependencies is essential in modern application development. .NET provides a powerful Dependency Injection (DI) system, with ServiceCollection at its core. Typically, we register a service and use it as is. However, there are instances when we need to change the ServiceLifetime of services after registration.

To download the source code for this article, you can visit our [GitHub repository](https://github.com/CodeMazeBlog/CodeMazeGuides/tree/main/dotnet-dependency-injection/ChangeServiceLifetimeOfAlreadyRegisteredService).

This article explores methods for changing ServiceLifeTime, providing practical examples for direct use in any project.

**Related Articles:** [How to Test IServiceCollection Registrations in .NET](https://code-maze.com/dotnet-how-to-test-iservicecollection-registrations/) · [IHostedLifecycleService Interface in ASP.NET Core](https://code-maze.com/aspnetcore-ihostedlifecycleservice-interface/)

## Frequently Asked Questions

### How do you change a registered service's lifetime in .NET?

After registering, remove the original descriptor and add a new one with the desired ServiceLifetime (Singleton, Scoped, or Transient) in a later ConfigureServices step or decoration pass.

### Why change a service lifetime at runtime?

To adapt behavior for testing, feature flags, or environment-specific wiring without rewriting the original registration.

### What can go wrong changing lifetimes?

Captive dependencies — a Singleton depending on a Scoped service can cause scope leaks; always check the dependency graph when promoting a lifetime.

## Motivation to Change the ServiceLifetime

Depending on the application’s configuration or the environment, we may need to change the service’s lifetime or implementation. For instance, in environments like `development`, `staging`, or `production`, different service lifetimes or implementations can optimize performance or resource usage.

Additionally, replacing real services with mock implementations helps isolate and test specific components during testing. This ensures reliable tests, free from external dependencies.

## Methods to Change the ServiceLifetime

Let’s create some reusable extension methods that will help us change the `ServiceLifetime` of service after it has been registered:

using Microsoft.Extensions.DependencyInjection.Extensions;

public static class ServiceCollectionExtensions
{
    public static IServiceCollection ReplaceWithSingleton<TService, TImplementation>(this IServiceCollection services)
        where TService : class
        where TImplementation : class, TService
        => services.Replace(new ServiceDescriptor(typeof(TService), typeof(TImplementation), 
               ServiceLifetime.Singleton));

    public static IServiceCollection ReplaceWithSingleton<TImplementation>(this IServiceCollection services)
       where TImplementation : class
       => services.Replace(new ServiceDescriptor(typeof(TImplementation), typeof(TImplementation), 
               ServiceLifetime.Singleton));

    public static IServiceCollection ReplaceWithScoped<TService, TImplementation>(this IServiceCollection services)
        where TService : class
        where TImplementation : class, TService
        => services.Replace(new ServiceDescriptor(typeof(TService), typeof(TImplementation), 
                ServiceLifetime.Scoped));

    public static IServiceCollection ReplaceWithScoped<TImplementation>(this IServiceCollection services)
        where TImplementation : class
        => services.Replace(new ServiceDescriptor(typeof(TImplementation), typeof(TImplementation), 
                ServiceLifetime.Scoped));

    public static IServiceCollection ReplaceWithTransient<TService, TImplementation>(this IServiceCollection services)
        where TService : class
        where TImplementation : class, TService
        => services.Replace(new ServiceDescriptor(typeof(TService), typeof(TImplementation), 
                ServiceLifetime.Transient));

    public static IServiceCollection ReplaceWithTransient<TImplementation>(this IServiceCollection services)
        where TImplementation : class
        => services.Replace(new ServiceDescriptor(typeof(TImplementation), typeof(TImplementation), 
                ServiceLifetime.Transient));
}

We create two overloads for the `ReplaceWithSingleton()`, `ReplaceWithScoped()`, and `ReplaceWithTransient()` methods to support cases where we replace services with interface registration and another one using the concrete implementation.

These methods enable us to replace an existing service registration with a new one, specifying the desired lifetime or even a different implementation. They leverage the `Replace()` method from `Microsoft.Extensions.DependencyInjection.Extensions` to update the service registration.

Free ebook

Most Web APIs ship with the same 33 mistakes.

The Web API Production Checklist walks through every one of them, with the fix, in .NET 10. 76 pages, free.

[Download the free PDF](https://code-maze.com/free-ebook-aspnetcore-webapi-best-practices/?box=4)

Free PDF. One email to send it. Unsubscribe any time.

![The Web API Production Checklist, free ebook](https://code-maze.com/wp-content/uploads/ebooks/covers/cover-dark-2-chevron-400.webp)

Essentially, these methods search for the service descriptor in the `IServiceCollection`, remove it if found, and then add it again with the new specified `ServiceLifetime` and optionally a different implementation.

## Practical Example to Change the ServiceLifeTime

Let’s now use these extension methods in a practical scenario.

Suppose we have an application that uses the `IService` interface. For all environments, we use the `DefaultService` implementation, but for development purposes, we want to use the `LocalDevelopmentService` implementation:

public interface IService
{
}

public class DefaultService : IService
{
    public DefaultService(ILogger<DefaultService> logger)
    {
        logger.LogInformation("Hello from DefaultService");
    }
}

public class LocalDevelopmentService : IService
{
    public LocalDevelopmentService(ILogger<LocalDevelopmentService> logger)
    {
        logger.LogInformation("Hello from LocalDevelopmentService");
    }
}

For illustration purposes, the constructors of the services log a message in the console.

### Registration

Let’s see how we register our implementation:

builder.Services.AddScoped<IService, DefaultService\>();

`builder.Services.AddScoped<IService, DefaultService>();`

Initially, we register our `IService` interface as a scoped service with `DefaultService` implementation which is our default desired behavior.

However, during the application setup, we check the environment and replace the registration with a `Singleton` lifetime and a new `LocalDevelopmentService` implementation for development purposes:

if (builder.Environment.IsDevelopment())
{
    builder.Services.ReplaceWithSingleton<IService, LocalDevelopmentService>();
}

We achieve this with the `ReplaceWithSingleton()` extension method we’ve defined.

Free ebook

Most Web APIs ship with the same 33 mistakes.

The Web API Production Checklist walks through every one of them, with the fix, in .NET 10. 76 pages, free.

[Download the free PDF](https://code-maze.com/free-ebook-aspnetcore-webapi-best-practices/?box=4)

Free PDF. One email to send it. Unsubscribe any time.

![The Web API Production Checklist, free ebook](https://code-maze.com/wp-content/uploads/ebooks/covers/cover-dark-2-chevron-400.webp)

### Testing

To test our example, we create a minimal API that just resolves the `IService` dependency:

app.MapGet("/use-service", (IService service) =\> Results.Ok())

`app.MapGet("/use-service", (IService service) => Results.Ok())`

Since the implementation of `IService` log messages to the console when their constructor is called, it is enough to just resolve the `IService` dependency in our endpoint.

Firstly, let’s run the project in `Development` mode and call our minimal API: 

info: ChangeServiceLifetimeOfAlreadyRegisteredService.Services.LocalDevelopmentService\[0\]
      Hello from LocalDevelopmentService

We see that the log message comes from our `LocalDevelopmentService` class.

Now, let’s run the application in `Production` and call our minimal API again:

info: ChangeServiceLifetimeOfAlreadyRegisteredService.Services.DefaultService\[0\]
      Hello from DefaultService

We see that the message comes from the `DefaultService` class.

## Conclusion

For various reasons, developers may need to change the ServiceLifetime of services after adding them to the IServiceCollection. Whether for optimization, new requirements, or configuration changes, understanding how to modify service lifetimes effectively is essential. By applying the methods discussed, such as creating extension methods for easy service replacement, we can maintain flexibility and control over our application’s dependencies, ensuring robust and maintainable code.
