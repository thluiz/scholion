---
url: "https://t.co/CMMkwpYdBM"
captured_at: "2026-09-25T21:18:53+01:00"
title: "API Versioning in ASP.NET Core"
domain: "t-co"
---

API versioning lets your API evolve without breaking the clients already integrated with it. Instead of shipping a breaking change, you publish a new version and let clients migrate on their own schedule. In ASP.NET Core you add it with the `Asp.Versioning` packages, then read the version from the URL segment, a header, or the query string.

[**ABP Framework**](https://commercial.abp.io/pricing?utm_source=milanw&utm_medium=w70) is a platform for building enterprise-grade ASP.NET Core applications. It comes with production-ready components, modular architecture, and Domain-Driven Design. [**Get started here.**](https://commercial.abp.io/pricing?utm_source=milanw&utm_medium=w70)

[**IcePanel**](https://u.icepanel.io/1eec0e6f) is a C4 model diagramming tool for complex software systems. Align your software engineering & product teams on technical decisions across the business. [**Learn more here.**](https://u.icepanel.io/1eec0e6f)

In the past year, I built and maintained a large public API. The API has dozens of integrations, serving mainly mobile applications.

When your API is serving so many clients, breaking changes are expensive.

So, everything I implemented on the public API had to be planned.

Adding a new field? Forget about it.

Renaming existing fields? Forget about it.

If I wanted to introduce breaking changes, I had to version the API.

Today, I'll show you how to implement API versioning in ASP.NET Core.

## [What Is API Versioning?](#what-is-api-versioning)

API versioning is the practice of assigning distinct identifiers to different iterations of an API, so that clients can target a specific version and continue working even as the API evolves.

Without versioning, every change you make to your API is potentially a breaking change for clients already integrated with it. With .NET API versioning, you can introduce a new `v2` endpoint with the updated behavior while `v1` continues to work exactly as before. Clients upgrade on their own schedule, and you maintain full control over which old versions to deprecate and remove.

This is what makes API versioning essential for any public-facing or long-lived .NET API. The same principles apply whether you're building with ASP.NET Core MVC controllers or [**Minimal APIs**](https://t.co/blog/minimal-apis-dotnet).

## [Why API Versioning Matters in .NET APIs](#why-api-versioning-matters-in-net-apis)

API versioning allows your API to evolve independently from the clients using it.

Introducing breaking changes to your API is a bad user experience. API versioning gives you a mechanism to avoid exposing breaking changes to clients. Instead of making a breaking change, you introduce a new API version.

What's the definition of a breaking change?

This isn't an exhaustive list, but a few examples of breaking changes are:

*   Removing or renaming APIs or API parameters
*   Changing the behavior of existing APIs
*   Changing the API response contract
*   Changing the [**API error codes**](https://t.co/blog/rest-api-http-status-codes)

You can decide what a breaking change means for your API. For example, adding a new field to the response doesn't have to be a breaking change.

Let's see how to implement API versioning.

## [How to Implement API Versioning in .NET Core](#how-to-implement-api-versioning-in-net-core)

Let's start by installing three NuGet packages that we'll need to implement API versioning:

*   `Asp.Versioning.Http`
*   `Asp.Versioning.Mvc`
*   `Asp.Versioning.Mvc.ApiExplorer`

```
Install-Package Asp.Versioning.Http # This is needed for Minimal APIs
Install-Package Asp.Versioning.Mvc # This is needed for Controllers
Install-Package Asp.Versioning.Mvc.ApiExplorer
```

This allows us to call `AddApiVersioning` and provide a delegate to configure the `ApiVersioningOptions`.

```
builder.Services.AddApiVersioning(options =>
{
    options.DefaultApiVersion = new ApiVersion(1);
    options.ReportApiVersions = true;
    options.AssumeDefaultVersionWhenUnspecified = true;
    options.ApiVersionReader = ApiVersionReader.Combine(
        new UrlSegmentApiVersionReader(),
        new HeaderApiVersionReader("X-Api-Version"));
})
.AddMvc() // This is needed for controllers
.AddApiExplorer(options =>
{
    options.GroupNameFormat = "'v'V";
    options.SubstituteApiVersionInUrl = true;
});
```

Here's the explanation for the `ApiVersioningOptions` properties:

*   `DefaultApiVersion` - Sets the default API version. Typically, this will be `v1.0`.
*   `ReportApiVersions` - Reports the supported API versions in the `api-supported-versions` response header.
*   `AssumeDefaultVersionWhenUnspecified` - Uses the `DefaultApiVersion` when the client didn't provide an explicit version.
*   `ApiVersionReader` - Configures how to read the API version specified by the client. The default value is `QueryStringApiVersionReader`.

The `AddApiExplorer` method is helpful if you are using Swagger. It will fix the endpoint routes and substitute the API version route parameter.

## [Types of API Versioning in .NET](#types-of-api-versioning-in-net)

There are several strategies for .NET API versioning, each with different tradeoffs.

### [URL Versioning](#url-versioning)

URL versioning embeds the version directly in the request path:

`GET https://localhost:5001/api/v1/workouts`

This is the most explicit approach. The version is visible at a glance, trivial to test in a browser or with curl, and is the most widely-used strategy for public .NET APIs. The `UrlSegmentApiVersionReader` in `Asp.Versioning.Http` handles this automatically.

Header versioning passes the API version via a custom request header:

`GET https://localhost:5001/api/workouts` with header `X-Api-Version: 1`

This keeps your URLs clean, but the version is invisible unless clients inspect outgoing headers. The `HeaderApiVersionReader` supports this strategy.

### [Query String Versioning](#query-string-versioning)

Query string versioning appends the version as a query parameter:

`GET https://localhost:5001/api/workouts?api-version=1`

This is the default behavior in `Asp.Versioning.Http` using `QueryStringApiVersionReader`. It's easy to use during development and testing without any special tooling.

There are a few other ways to implement API versioning, such as using the `accept` or `content-type` headers, but they aren't used often.

The `Asp.Versioning.Http` library provides several `IApiVersionReader` implementations to support these strategies:

*   `UrlSegmentApiVersionReader`
*   `HeaderApiVersionReader`
*   `QueryStringApiVersionReader`
*   `MediaTypeApiVersionReader`

[Microsoft's API versioning guidelines](https://github.com/Microsoft/api-guidelines/blob/master/Guidelines.md#12-versioning) suggest using URL or query string parameter versioning.

I use URL versioning almost exclusively in the applications I'm developing.

## [Versioning Controllers](#versioning-controllers)

To implement API versioning in ASP.NET controllers, you have to decorate the controller with the `ApiVersion` attribute.

The `ApiVersion` attribute allows you to specify which API versions that `WorkoutsController` supports. In this case, the controller supports both `v1` and `v2`. You use the `MapToApiVersion` attribute on the endpoints to specify the concrete API version.

The route parameter `v{v:apiVersion}` lets you specify the API version using `v1` or `v2` in the URL.

```
[ApiVersion(1)]
[ApiVersion(2)]
[ApiController]
[Route("api/v{v:apiVersion}/workouts")]
public class WorkoutsController : ControllerBase
{
    [MapToApiVersion(1)]
    [HttpGet("{workoutId}")]
    public IActionResult GetWorkoutV1(Guid workoutId)
    {
        return Ok(new GetWorkoutByIdQuery(workoutId).Handle());
    }

    [MapToApiVersion(2)]
    [HttpGet("{workoutId}")]
    public IActionResult GetWorkoutV2(Guid workoutId)
    {
        return Ok(new GetWorkoutByIdQuery(workoutId).Handle());
    }
}
```

## [Deprecating API Versions](#deprecating-api-versions)

If you want to deprecate an old API version, you can set the `Deprecated` property on the `ApiVersion` attribute. The deprecated API versions will be reported using the `api-deprecated-versions` response header.

```
[ApiVersion(1, Deprecated = true)]
[ApiVersion(2)]
[ApiController]
[Route("api/v{v:apiVersion}/workouts")]
public class WorkoutsController : ControllerBase
{
}
```

## [Versioning Minimal APIs](#versioning-minimal-apis)

Versioning Minimal APIs requires you to define an `ApiVersionSet`, which you'll pass to the endpoints.

*   `NewApiVersionSet` - Creates a new `ApiVersionSetBuilder` that you can use to configure the `ApiVersionSet`.
*   `HasApiVersion` - Indicates that the `ApiVersionSet` supports the specified `ApiVersion`.
*   `ReportApiVersions`\- Indicates that all APIs in the `ApiVersionSet` will report their versions.

After creating the `ApiVersionSet`, you must pass it to a Minimal API endpoint by calling `WithApiVersionSet`. You can map to an explicit API version by calling `MapToApiVersion`.

```
ApiVersionSet apiVersionSet = app.NewApiVersionSet()
    .HasApiVersion(new ApiVersion(1))
    .HasApiVersion(new ApiVersion(2))
    .ReportApiVersions()
    .Build();

app.MapGet("api/v{version:apiVersion}/workouts/{workoutId}", async (
    Guid workoutId,
    ISender sender,
    CancellationToken ct) =>
{
    var query = new GetWorkoutByIdQuery(workoutId);

    Result<WorkoutResponse> result = await sender.Send(query, ct);

    return result.Match(Results.Ok, CustomResults.Problem);
})
.WithApiVersionSet(apiVersionSet)
.MapToApiVersion(1);
```

Specifying the `ApiVersionSet` for each Minimal API endpoint can be cumbersome. So you can define a route group and set the `ApiVersionSet` only once. Route groups are also practical because they allow you to specify the route prefix.

```
ApiVersionSet apiVersionSet = app.NewApiVersionSet()
    .HasApiVersion(new ApiVersion(1))
    .ReportApiVersions()
    .Build();

RouteGroupBuilder group = app
    .MapGroup("api/v{version:apiVersion}")
    .WithApiVersionSet(apiVersionSet);

group.MapGet("workouts", ...);
group.MapGet("workouts/{workoutId}", ...);
```

## [API Versioning Best Practices in .NET](#api-versioning-best-practices-in-net)

Here are key practices to keep in mind when implementing API versioning in .NET Core:

*   **Version from day one.** It's far easier to add API versioning before you have external clients. Even a single version (`v1`) gives you room to introduce `v2` later without painful migrations.
*   **Define what a breaking change is.** Agree as a team on what constitutes a breaking change (removing fields, changing response contracts, modifying error codes), and document it. Adding a new optional field or a new endpoint is typically safe.
*   **Deprecate, don't delete.** When retiring a version, mark it as deprecated first using `[ApiVersion(1, Deprecated = true)]`. Give clients time to migrate before removing it entirely.
*   **Report supported versions.** Set `ReportApiVersions = true` so that clients can discover available versions via the `api-supported-versions` response header.
*   **Keep old versions stable.** Once a version is published, treat it as immutable. New features go into a new version, not the old one.
*   **Prefer URL versioning for public APIs.** It's the most discoverable, easiest to cache, and works across all HTTP clients without special configuration.

## [Takeaway](#takeaway)

API versioning is one of the best practices for designing modern APIs. Consider implementing API versioning from the first release. This makes it easier for clients to support future API versions. And it gets your team used to managing breaking changes and versioning the API.

You can use the `Asp.Versioning.Http` library to add API versioning in ASP.NET Core. Define the supported API versions, and start using them in your endpoints.

Remember to agree as a team what represents a breaking change. This should be well documented in the team's API design guidelines.

My preferred way to implement API versioning is using URL versioning. It's simple and explicit.

And since this is the last issue for the year, I wish you a happy and prosperous new year.

Thanks for reading, and stay awesome!

* * *

## Frequently Asked Questions

What is API versioning?

API versioning is a strategy that allows your API to evolve independently from the clients consuming it. Instead of making breaking changes that force all clients to update at once, you introduce a new version of the API and let clients migrate on their own schedule.

Is API versioning required in ASP.NET Core?

API versioning is not required by default in ASP.NET Core, but it is strongly recommended for public or long-lived APIs. The Asp.Versioning.Mvc NuGet package adds full versioning support.

What is the best API versioning strategy in .NET?

The most common strategy is URL segment versioning (e.g. /api/v1/resource) because it is explicit and easy to test in a browser. Header versioning is cleaner but less discoverable. The best choice depends on your client base.

Does ASP.NET Core support API versioning out of the box?

Not natively. You need to install the Asp.Versioning.Http and Asp.Versioning.Mvc packages, then call AddApiVersioning() in your service registration.

How do you version Minimal APIs in .NET?

With Minimal APIs, you assign endpoint groups to an API version group using MapGroup and tag them with the appropriate ApiVersion attribute. The Asp.Versioning.Http package provides the necessary extension methods.

Is adding a new response field a breaking change?

Adding a new field to a response is generally not a breaking change for well-written API clients. However, removing or renaming fields, changing types, or altering behavior are all breaking changes.

Should I use URL or header API versioning in .NET?

URL versioning is simpler to implement and easier for clients to consume. Header versioning keeps URLs clean but requires clients to set a custom header. Most public APIs use URL versioning.
