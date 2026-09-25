---
url: "https://www.milanjovanovic.tech/blog/breaking-it-down-how-to-migrate-your-modular-monolith-to-microservices"
captured_at: "2026-09-25T22:32:19+01:00"
title: "Breaking It Down: How to Migrate Your Modular Monolith to Microservices"
domain: "milanjovanovic-tech"
---

Migrate one module at a time. Tighten module boundaries and data ownership first, then extract a low-coupling module into its own project and database. Direct method calls become HTTP or messaging calls, and an API gateway gives clients one entry point.

Integrate e-signatures into your workflows with the [**BoldSign .NET SDK**](https://boldsign.com/esignature-api/?utm_source=milanjovanovic&utm_medium=newsletter_ad&utm_campaign=boldsign). The e-signature API lets you embed signature requests, verify signer identity, and add custom branding. Free coding assistance and migration support is available. Try the [**free API sandbox**](https://boldsign.com/esignature-api/?utm_source=milanjovanovic&utm_medium=newsletter_ad&utm_campaign=boldsign) today!

[**Webinar: "Unlocking AI's Potential: Why the Future Depends on APIs"**](https://app.zuddl.com/p/a/event/8e8f96c1-99d5-4392-96a1-c68b8c8b9d2d?utm_source=influencer&utm_medium=referral&utm_campaign=fy25q3_global_ent_unlocking_ai_potential_webinar&utm_term=existing_influencer_relationships&utm_content=milan_jovanovic). Join Postman CTO, Ankit Sobti, and Head of Customer Experience and Success, Kristine Chin, at this free webinar to maximize the success of your API products and provide a world-class experience for your developers, partners, and customers. [**Join here**](https://app.zuddl.com/p/a/event/8e8f96c1-99d5-4392-96a1-c68b8c8b9d2d?utm_source=influencer&utm_medium=referral&utm_campaign=fy25q3_global_ent_unlocking_ai_potential_webinar&utm_term=existing_influencer_relationships&utm_content=milan_jovanovic).

As your application grows, you might find yourself considering a move from a modular monolith to microservices. This transition isn't just a technical shift. It's a strategic move that can reshape how your entire system operates. But let's be clear: it's not a magic solution and comes with its own challenges.

In this article, I'll share my experience of migrating from a modular monolith to microservices.

We'll explore why you might consider microservices, how to prepare for the migration and the critical steps in the migration process - from choosing your first module to implementing inter-service communication and managing data migration.

Let's dive in!

## [Why Consider Microservices?](#why-consider-microservices)

A [**modular monolith**](https://www.milanjovanovic.tech/blog/what-is-a-modular-monolith) serves as an excellent starting point for many applications. It's simpler to develop, easier to understand, and faster to deploy than a distributed system. But as your application grows, you might start facing some problems.

Here are the key challenges I've encountered with modular monoliths:

*   High-load modules can become bottlenecks, affecting the entire system's performance
*   As the monolith grows, deployments become riskier and more time-consuming
*   Large teams working on a single codebase often step on each other's toes
*   You're locked into a single technology stack for the entire application

Microservices can address these issues, but it's not a decision to be taken lightly.

![Modular monolith to microservices comparison.](https://www.milanjovanovic.tech/blogs/mnw_109/modular_monolith_vs_microservices.png)

Here's how microservices can help:

*   **Scalability**: You can scale individual services based on their specific load, optimizing resource use.
*   **Independent deployability**: Updates to one service don't require redeploying the entire application, reducing risk and downtime.
*   **Team autonomy**: Separate teams can own different services, leading to faster development cycles.

The good news? If you've built a well-designed modular monolith, you're already halfway there. The clear boundaries between modules in your monolith can serve as a blueprint for your microservices architecture.

Remember, microservices come with their own complexities in areas like data consistency and inter-service communication. But for the right use cases, they can provide the flexibility and scalability needed for growing applications.

## [Preparing for Migration](#preparing-for-migration)

The success of your migration largely depends on how well you prepare. Your best starting point is a well-structured modular monolith.

Here are key areas to focus on:

1.  **Review module boundaries**: I can't stress this enough: [**clear module boundaries**](https://www.milanjovanovic.tech/blog/module-boundaries-bounded-contexts) are crucial. Each module should have a distinct responsibility and minimal dependencies on others. If boundaries are blurry, refactor before migrating.
    
2.  **Ensure proper data encapsulation**: Modules should not directly access each other's data stores. I make sure each module owns and manages its data exclusively. No shared tables, no direct database access across modules. This clean separation makes it much easier to extract modules into microservices later.
    
3.  **Implement clean public APIs**: Define clear contracts between modules to facilitate future separation. Modules should communicate through well-defined APIs, not by accessing each other's internals.
    

Here's an example of the above:

```
// Good: Clear module boundary
namespace BookingsModule;

public class CreateBooking
{
    private readonly IBookingRepository _bookingRepository;
    private readonly IPaymentGateway _paymentGateway; // Public API

    public CreateBooking(IBookingRepository bookingRepository, IPaymentGateway paymentGateway)
    {
        _bookingRepository = bookingRepository;
        _paymentGateway = paymentGateway;
    }

    public async Task<BookingResult> CreateBookingAsync(BookingRequest request)
    {
        var booking = await _bookingRepository.CreateAsync(Booking.FromRequest(request));

        // Accessing the other module's data through an abstraction
        var paymentResult = await _paymentGateway.ProcessPaymentAsync(booking.Id, booking.TotalAmount);

        return new BookingResult(booking, paymentResult);
    }
}
```

By focusing on these areas, you're not just preparing for migration - you're improving your modular monolith. Even if you decide not to migrate, these steps will make your system more maintainable and scalable.

## [Choosing and Extracting the First Module](#choosing-and-extracting-the-first-module)

Selecting the right module to extract first can set the tone for your entire migration. In my experience, it's crucial to start with a module that's self-contained and has clear boundaries.

When I'm evaluating modules, I look for these characteristics:

*   Low coupling with other modules
*   High cohesion within the module
*   A distinct business function
*   Potential performance or scalability gains from separation

For instance, in an e-commerce system, I might choose the product catalog module. It typically has a clear purpose, doesn't heavily depend on other modules, and could benefit from independent scaling.

Once you've chosen your module, here's the extraction process I follow:

1.  Create a new project for the microservice.
2.  Move the module's code to the new project. This often reveals hidden dependencies, which is valuable information.
3.  Update the dependencies, ensuring the microservice is self-contained. This might involve copying some shared code or refactoring to remove unnecessary dependencies.
4.  Set up a separate database for the microservice. This enforces data independence.
5.  Implement a data migration strategy (more on this later)

Here's what this might look like in practice:

![Modular monolith extraction process into microservices.](https://www.milanjovanovic.tech/blogs/mnw_109/modular_monolith_extraction.png)

Remember, the goal isn't perfection on the first try. I often iterate on this process, gradually refining the separation between the new microservice and the monolith.

The first extraction is a learning experience. It'll show you how to approach subsequent modules and help you refine the overall migration strategy.

## [Implementing Inter-Service Communication](#implementing-inter-service-communication)

Once you've extracted a module into a microservice, you have to update the [**module's communication**](https://www.milanjovanovic.tech/blog/modular-monolith-communication-patterns) with the rest of the system. This typically involves transitioning from direct method calls to network-based communication.

Here's how I approach this transition:

1.  Replace direct method calls with HTTP API calls. I often use libraries like [**Refit**](https://www.milanjovanovic.tech/blog/refit-in-dotnet-building-robust-api-clients-in-csharp) to simplify API interactions. Here's a before and after example:

```
// Before: Direct method call
BookingDto booking = await _bookingService.GetAsync(bookingId);

// After: HTTP API call
var response = await _httpClient.GetAsync($"http://bookings-service/api/bookings/{bookingId}");

var booking = await response.Content.ReadFromJsonAsync<BookingDto>();
```

2.  For asynchronous communication, consider implementing a messaging system. While the implementation details vary, tools like [**RabbitMQ**](https://www.milanjovanovic.tech/blog/using-masstransit-with-rabbitmq-and-azure-service-bus), [**Amazon SQS and SNS**](https://www.milanjovanovic.tech/blog/complete-guide-to-amazon-sqs-and-amazon-sns-with-masstransit), or [**Azure Service Bus**](https://www.milanjovanovic.tech/blog/messaging-made-easy-with-azure-service-bus) can significantly improve system resilience and decoupling.
    
3.  Network communication introduces new failure modes, so I always implement [**resilience patterns**](https://www.milanjovanovic.tech/blog/building-resilient-cloud-applications-with-dotnet). Here's how I use Polly with resilience pipelines:
    

```
using Polly;

var pipeline = new ResiliencePipelineBuilder<HttpResponseMessage>()
    .AddRetry(new RetryStrategyOptions
    {
        ShouldHandle = new PredicateBuilder().Handle<ConflictException>(),
        Delay = TimeSpan.FromSeconds(1),
        MaxRetryAttempts = 2,
        BackoffType = DelayBackoffType.Exponential,
        UseJitter = true
    })
    .AddTimeout(new TimeoutStrategyOptions
    {
        Timeout = TimeSpan.FromSeconds(10)
    })
    .Build();

var response = await pipeline.ExecuteAsync(
    async ct => await _httpClient.GetAsync($"http://bookings-service/api/bookings/{bookingId}", ct),
    cancellationToken);
```

Transitioning to HTTP-based communication always brings new problems to solve. Serialization, error handling, and [**API versioning**](https://www.milanjovanovic.tech/blog/api-versioning-in-aspnetcore) become crucial. I've learned to plan for these aspects from the start to avoid headaches down the line.

## [Implementing an API Gateway](#implementing-an-api-gateway)

As you extract more services, managing the communication between clients and your microservices can become complex. An API Gateway can help manage this complexity by providing a single entry point for all clients.

YARP (Yet Another Reverse Proxy) is an excellent tool for [**implementing an API Gateway**](https://www.milanjovanovic.tech/blog/implementing-an-api-gateway-for-microservices-with-yarp) in .NET. Here's how I typically set it up:

```
var builder = WebApplication.CreateBuilder(args);

builder.Services.AddReverseProxy()
    .LoadFromConfig(builder.Configuration.GetSection("ReverseProxy"));

var app = builder.Build();

app.MapReverseProxy();

app.Run();
```

Then, I configure the routing in `appsettings.json`:

```
{
  "ReverseProxy": {
    "Routes": {
      "bookings-route": {
        "ClusterId": "bookings-cluster",
        "Match": {
          "Path": "/api/bookings/{**catch-all}"
        }
      },
      "payments-route": {
        "ClusterId": "payments-cluster",
        "Match": {
          "Path": "/api/payments/{**catch-all}"
        }
      }
    },
    "Clusters": {
      "bookings-cluster": {
        "Destinations": {
          "destination1": {
            "Address": "http://bookings-service/"
          }
        }
      },
      "payments-cluster": {
        "Destinations": {
          "destination1": {
            "Address": "http://payments-service/"
          }
        }
      }
    }
  }
}
```

This setup routes requests to the appropriate microservice based on the path. For example, any request to `/api/bookings/*` will be routed to the `bookings-service`.

![Modular monolith extraction process into microservices with an API gateway introduced.](https://www.milanjovanovic.tech/blogs/mnw_109/modular_monolith_extraction_api_gateway.png)

In my projects, I've found that an API Gateway often becomes a critical point for implementing cross-cutting concerns. As your architecture evolves, consider adding features like:

*   [**Rate limiting**](https://www.milanjovanovic.tech/blog/advanced-rate-limiting-use-cases-in-dotnet) to protect your services from overload
*   [**Caching**](https://www.milanjovanovic.tech/blog/caching-in-aspnetcore-improving-application-performance) to improve response times for frequently requested data
*   Request/response transformation to adapt your internal APIs for external consumption

Start simple, but be prepared to evolve your gateway as you learn more about your system's needs and usage patterns.

## [Data Migration Strategy](#data-migration-strategy)

Data migration is often the trickiest part of moving from a modular monolith to microservices. In my experience, there are two main approaches:

1.  **The "One and Done" Approach**
    
    For simpler systems or those that can handle some downtime, I use this method:
    
    *   Create a new database for the microservice
    *   Copy the relevant schema and data from the monolith
    *   Switch the application to use the new database
    
    It's quick and simple but requires a brief downtime.
    
2.  **The Synchronization Approach**
    
    For complex systems needing minimal disruption, I use this method:
    
    *   Copy the schema and initial data to the new database
    *   Set up a sync mechanism (like [change data capture](https://en.wikipedia.org/wiki/Change_data_capture)) to keep the new database updated
    *   Gradually shift traffic to the new microservice
    *   Eventually, remove the old schema from the monolith
    
    This approach is more complex but allows for a smoother transition.
    

In both cases, I always ensure I have a solid backup and rollback plan. The key is to choose the method that best fits your system's needs and tolerance for complexity.

Remember, if your modular monolith already uses [**separate database schemas for each module**](https://www.milanjovanovic.tech/blog/modular-monolith-data-isolation), you're starting with an advantage. This logical isolation makes the migration process significantly easier.

## [Summary](#summary)

Migrating from a modular monolith to microservices is a journey I've taken several times, and it's always both challenging and rewarding. The process we've covered here - from preparing your monolith and choosing the right module to extract to implementing proper communication patterns - forms the foundation of a successful migration.

Don't rush the process. Careful planning and incremental changes are key. Each step teaches you something valuable about your system.

While we've covered the fundamentals, there's always more to learn. I recommend exploring these advanced topics:

*   [**Service discovery**](https://www.milanjovanovic.tech/blog/service-discovery-in-microservices-with-net-and-consul) and API gateway patterns
*   [**Monitoring and observability**](https://www.milanjovanovic.tech/blog/introduction-to-distributed-tracing-with-opentelemetry-in-dotnet) in a microservices environment
*   Advanced [**deployment strategies**](https://www.milanjovanovic.tech/blog/how-to-build-ci-cd-pipeline-with-github-actions-and-dotnet), like blue-green deployment

If you're ready to master this process and gain hands-on experience, I've put together a comprehensive [**Modular Monolith Architecture**](https://www.milanjovanovic.tech/modular-monolith-architecture) course. There's an entire chapter dedicated to extracting modules and moving to microservices. You'll gain practical skills to confidently navigate your microservices transformation.

Remember, the goal isn't to blindly adopt microservices but to evolve your architecture to best serve your business needs. Sometimes, a well-structured modular monolith is the right solution. Other times, a full microservices architecture is the way to go. The key is understanding the trade-offs and making informed decisions.

Good luck out there, and I'll see you next week.

* * *

## Frequently Asked Questions

When should you migrate from a modular monolith to microservices?

When high-load modules become bottlenecks, deployments grow risky and slow, large teams keep colliding in one codebase, or you need different technology stacks. Microservices bring independent scaling, independent deployment, and team autonomy, but they add complexity, so migrate for a concrete reason.

How do you prepare a modular monolith for a microservices migration?

Review module boundaries so each module has a distinct responsibility, enforce data encapsulation with no shared tables or cross-module database access, and make modules communicate through clean public APIs. These steps improve the monolith even if you never complete the migration.

Which module should you extract into a microservice first?

Pick a module with low coupling to other modules, high cohesion, a distinct business function, and a potential scalability gain from separation, like a product catalog. Then create a new project, move the code, resolve hidden dependencies, set up a separate database, and migrate the data.

How do services communicate after extracting a module from a monolith?

Direct method calls become network calls. Use HTTP APIs for synchronous communication, and a messaging system like RabbitMQ, Amazon SQS and SNS, or Azure Service Bus for asynchronous communication. Network calls introduce new failure modes, so add resilience patterns like retries and timeouts with Polly.

Do you need an API gateway for microservices?

As you extract more services, an API gateway gives clients a single entry point and routes requests to the right service by path. YARP works well for this in .NET, and the gateway often becomes the place for cross-cutting concerns like rate limiting, caching, and request transformation.

How do you migrate data from a monolith to a microservice?

There are two main approaches. The "one and done" approach copies the schema and data to a new database and switches over, which is quick but needs brief downtime. The synchronization approach keeps the new database updated, for example with change data capture, while traffic shifts gradually.
