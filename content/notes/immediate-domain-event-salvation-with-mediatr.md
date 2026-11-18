---
title: "Immediate Domain Event Salvation with MediatR"
date: '2026-11-18T12:00:47+00:00'
category: webclip
summary: 'Article shows how to implement immediate, pre-persistence domain events in .NET using MediatR, using a static helper, event handlers with dependencies, and startup wiring.'
tags: ["domain-events", "mediatr", "aspnet-core", "ddd"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Immediate Domain Event Salvation with MediatR"
    url: "https://ardalis.com/immediate-domain-event-salvation-with-mediatr/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/ardalis-com--immediate-domain-event-salvation-with-mediatr.md"
    kind: repo
---

The text explains how to implement immediate, pre-persistence domain events in .NET using MediatR. It distinguishes pre- and post-persistence events and focuses on triggering events from the domain model when entities cannot have dependencies injected. A static helper in the Core or SharedKernel project exposes a Mediator factory and a generic Raise method that publishes MediatR notifications, enabling entity methods to raise domain events before persistence.

The article walks through an example where an entity update operation must verify name uniqueness before saving. The entity’s Update method raises an UpdatingNameEvent, which is handled by a MediatR notification handler living in the Core project. This handler depends on an async repository, loads all items, checks for a different item with the same name, and throws a specific exception when a duplicate is found. The event class is a simple INotification carrying the entity id and the new name. Finally, the setup in Startup configures MediatR, a ServiceLocator, and assigns DomainEvents.Mediator to resolve the current IMediator instance using a [ThreadStatic] delegate per thread. The author notes that this approach is still being tested, might have issues under high concurrency, and that the service locator could likely be replaced or improved later.

## Reading notes

- Author contrasts pre-persistence and post-persistence domain events and notes an existing MediatR-based post-persistence implementation in a Clean Architecture template.
- Goal is to add an immediate, pre-persistence domain event implementation for .NET inspired by Udi Dahan’s static helper pattern that used StructureMap and static methods.
- MediatR should be added to the ASP.NET Core app first, and it can help simplify controllers and potentially lead to using API Endpoints and the REPR pattern at the web layer.
- Domain events are to be raised from entities and domain model types, which cannot easily receive injected services, so a static helper class is required.
- The static DomainEvents helper resides in the Core or SharedKernel project so domain model types can access it.
- DomainEvents exposes a [ThreadStatic] public static Func<IMediator> Mediator used as a factory for the current scoped IMediator instance.
- The Raise<T> method on DomainEvents is async and invokes the Mediator factory, then calls Publish on IMediator for the given notification type.
- The Core or SharedKernel project must take a dependency on MediatR for the DomainEvents helper to compile.
- The front-end (ASP.NET Core) needs to wire up the Mediator static property so it returns the scoped MediatR instance at runtime.
- In the example, an entity needs to ensure its name is unique before saving and cannot easily do this with data annotations or self-contained logic.
- The entity’s Update method calls DomainEvents.Raise with an UpdatingNameEvent containing the entity id and new name, then assigns the Name property.
- The author notes that Update should ideally be async since it calls an async method via Wait, but keeps the example simple.
- This pre-persistence event lets a handler perform checks or work before the entity’s state is changed.
- To enforce uniqueness, a MediatR notification handler, ValidateUniqueCatalogItemNameHandler, is implemented in the Core project.
- The handler implements INotificationHandler<UpdatingNameEvent> and depends on IAsyncRepository<CatalogItem>.
- In Handle, it retrieves all catalog items asynchronously and converts them into a list.
- It searches the list for an item whose name equals the event’s new name and whose id differs from the event id.
- If such a duplicate item exists, the handler throws a DuplicateCatalogItemNameException with a message and the duplicate id.
- The author highlights that a simple table existence check is insufficient; the handler must exclude the current record so updates to the same value do not fail.
- The article points out that domain event handlers can have dependencies, which allows domain behavior that needs services to live near entities without pushing all such behavior into external services.
- This approach avoids forcing clients of the model to decide between calling a domain service or an entity method for operations that require dependencies.
- The UpdatingNameEvent class implements INotification and stores the entity id and new name as read-only properties.
- In Startup.ConfigureServices, services.AddMediatR is called with an assembly type (CatalogItem) to register MediatR handlers.
- A ServiceProvider is built from the service collection, and ServiceLocator.SetLocatorProvider stores it for later resolution.
- DomainEvents.Mediator is assigned a lambda that calls ServiceLocator.Current.GetInstance<IMediator>() to provide the current IMediator.
- The ServiceLocator class wraps a static ServiceProvider and exposes a Current property that returns a new ServiceLocator using the stored provider.
- ServiceLocator offers static SetLocatorProvider for initialization and GetInstance methods for resolving services by type or generic type.
- The author reused a ServiceLocator implementation from another article and reports it worked well in this scenario.
- They mention that ServiceLocator might be replaceable with another pattern or NuGet package in the future.
- The author plans to eventually integrate this immediate domain event approach into eShopOnWeb or CleanArchitecture but states it is not there yet.
- A note warns that the solution relies on [ThreadStatic], so non-Core apps should configure the Mediator Func in Application_BeginRequest, and Core apps may need middleware that runs before ASP.NET Core MVC.
- The author emphasizes that this setup is still under testing, may show issues in highly concurrent scenarios, and expresses some reservations about using service location.
- They describe the solution as a modernized version of Udi Dahan’s pattern and say that pattern is known to work without issues.
- The article links to additional resources including DDD Fundamentals and SOLID Principles for C# Developers on Pluralsight.
- At the end, the author invites readers to subscribe to an email newsletter with weekly software development tips or share the post on Hacker News.
