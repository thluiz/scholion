---
url: "https://samwalpole.com/handling-dependency-injection-in-inherited-classes?utm_source=csharpdigest&utm_medium=email&utm_campaign=359"
captured_at: "2021-06-21T10:30:00-03:00"
title: "Handling Dependency Injection in Inherited Classes"
domain: "samwalpole-com"
---

# Handling Dependency Injection in Inherited Classes

Subscribe to my newsletter and never miss my upcoming articles

Dependency injection (DI) is a wonderful thing. Simply add your dependency as a parameter to the constructor (most commonly) of your class, register it with you DI container, and away you go - the DI container will manage the rest. Some of the key benefits of DI are: greater testability, greater maintainability, and greater reusability.

```
// without DI
public class OrderController : Controller
{
    public ActionResult Post(Order order)
    {
        using (var dbContent = new MyDbContext())
        {
            dbContext.Orders.Add(order);
            dbContent.SaveChanges();

            return Ok();
        }
    }

    public ActionResult Get()
    {
        using (var dbContext = new MyDbContext())
        {
            var orders = dbContext.Orders.ToList();

            return new JsonResult(orders);
        }
    }
}

// with DI
public class OrderController : Controller
{
    private readonly MyDbContext _dbContext;

    public OrderController(MyDbContext dbContext)
    {
        _dbContext = dbContext;
    }

    public ActionResult Post(Order order)
    {
        _dbContext.Orders.Add(order);
        _dbContent.SaveChanges();

        return Ok();
    }

    public ActionResult Get()
    {
        var orders = _dbContext.Orders.ToList();

        return new JsonResult(orders);
    }
}
```

However, I recently came across a use case where DI can be a real pain - dependency injection in inherited classes.

# The Problem

I have recently been working a lot with the [Mediatr](https://github.com/jbogard/MediatR) package, using it's request/request handler pattern to issue commands in the system (inspired by [Jason Taylor's Clean Architecture solution](https://github.com/jasontaylordev/CleanArchitecture)).

I typically create a RequestHandler base class that contains common dependencies and functionality. Each concrete request handler can then inherit from this base class.

```
public abstract class RequestHandler<TRequest, TResponse> : IRequestHandler<TRequest, TResponse>
    where TRequest : IRequest<TResponse>
{
    public RequestHandler(IApplicationDbContext dbContext)
    {
        DbContext = dbContext;
    }

    protected IApplicationDbContext DbContext { get; }

    public abstract Task<TResponse> Handle(TRequest request, CancellationToken cancellationToken);
}

public MyRequestHandler : RequestHandler<MyRequest, MyResponse>
{
    public MyRequestHandler(IApplicationDbContext dbContext) : base(dbContext) { }

    public override Task<MyResponse> Handle(MyRequest request, CancellationToken cancellationToken)
    {
        // handler logic
    }
}
```

The problem comes when I want to add more dependencies to the base class. Now I have to go through to every single concrete request handler and update the constructor to take the new dependency as well. Fortunately, the code will not compile if I miss one, so there is no risk of a runtime error, but it is still incredibly tedious work to have to update every single request handler. Also, you can end up with very large constructors, which obscures the intention of the class.

```
public abstract class RequestHandler<TRequest, TResponse> : IRequestHandler<TRequest, TResponse>
    where TRequest : IRequest<TResponse>
{
    public RequestHandler(IApplicationDbContext dbContext, ICurrentUser currentUser)
    {
        DbContext = dbContext;
        CurrentUser = currentUser;
    }

    protected IApplicationDbContext DbContext { get; }
    protected ICurrentUser CurrentUser { get; }

    public abstract Task<TResponse> Handle(TRequest request, CancellationToken cancellationToken);
}

public MyRequestHandler : RequestHandler<MyRequest, MyResponse>
{
    public MyRequestHandler(IApplicationDbContext dbContext, ICurrentUser currentUser) : base(dbContext, currentUser) { }

    public override Task<MyResponse> Handle(MyRequest request, CancellationToken cancellationToken)
    {
        // handler logic
    }
}
```

# The Solution - Dependency Aggregates

The solution to this problem is really quite simple. Rather than injecting the dependencies directly, create a new class that contains the dependencies (known as an aggregate) and inject that instead.

```
public interface IDependencyAggregate 
{
    IApplicationDbContext DbContext { get; }
    ICurrentUser { get; }
}

public class DependencyAggregate : IDependencyAggregate
{
    public DependencyAggregate(IApplicationDbContext dbContext, ICurrentUser currentUser)
    {
        DbContext = dbContext;
        CurrentUser = currentUser;
    }

    public IApplicationDbContext DbContext { get; }
    public ICurrentUser CurrentUser { get; }
}

public abstract class RequestHandler<TRequest, TResponse> : IRequestHandler<TRequest, TResponse>
    where TRequest : IRequest<TResponse>
{
    public RequestHandler(IDependencyAggregate aggregate)
    {
        DbContext = aggregate.DbContext;
        CurrentUser = aggregate.CurrentUser;
    }

    protected IApplicationDbContext DbContext { get; }
    protected ICurrentUser CurrentUser { get; }

    public abstract Task<TResponse> Handle(TRequest request, CancellationToken cancellationToken);
}

public MyRequestHandler : RequestHandler<MyRequest, MyResponse>
{
    public MyRequestHandler(IDependencyAggregate aggregate) : base(aggregate) { }

    public override Task<MyResponse> Handle(MyRequest request, CancellationToken cancellationToken)
    {
        // handler logic
    }
}
```

Now if I want to add a new dependency, the only places that I need to change the code are in the DependencyAggregate class and the RequestHandler base class (I don't need to make any changes to the inherited classes).

# Conclusion

In this post I have described a simple method for managing dependency injection in inherited classes, by creating a dependency aggregate class to inject into the base class. This ensures that new dependencies can easily be introduced with having to make changes to every inherited class.

I post mostly about full stack .NET and Vue web development. To make sure that you don't miss out on any posts, please follow this blog and [subscribe to my newsletter](https://samwalpole.com/). If you found this post helpful, please like it and share it. You can also find me on [Twitter](https://twitter.com/dr_sam_walpole).
