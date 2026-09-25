---
url: "https://www.c-sharpcorner.com/article/http-best-practices-using-asp-net-core-and-polly/"
captured_at: "2026-09-25T21:53:25+01:00"
title: "HTTP Best Practices Using ASP.NET Core And Polly"
domain: "c-sharpcorner-com"
---

In [part 1](https://www.c-sharpcorner.com/article/http-best-practices-using-asp-net-core/) of this series, we compared HTTP Client vs HTTP Client Factory. Also, discussed the advantages that can be gained by using HTTP Client Factory or overcoming the shortfalls of socket exhaustion with HTTP Client.

We had already overcome socket exhaustion but there are challenges around resiliency and they must be addressed.

## Resiliency

Resiliency comes with the capability of handling faults by itself or without causing the application to crash. Resiliency must be designed during the SDLC cycle to address the below issues in the architecture

*   Capacity to recover when stressed by load or serving request for a particular service
*   Accidently through bugs or deliberately through attacks such as DDoS (Distributed denial of Service).
*   Failure of component/s during workload

In our case, let us talk only about HTTP operation.

Many questions arise here

*   How to implement resiliency?
*   Do we need to implement resiliency for all HTTP error codes?
*   What is the best way of implementing resiliency?

Let us address these questions in sequence

## How to implement resiliency?

To handle resiliency, we will be using Polly Library.

> Polly is a .NET resilience and transient-fault-handling library that allows developers to express policies such as Retry, Circuit Breaker, Timeout, Bulkhead Isolation, and Fallback in a fluent and thread-safe manner.
> 
> SOURCED FROM POLLY

You can read more about this library [here](https://github.com/App-vNext/Polly).

## Do we need to implement resiliency for all HTTP error codes?

No, not required. Resiliency must be implemented only for transient errors such as

*   Network failures
*   HTTP 5XX status code (server errors)
*   HTTP 408 (request timeout)

Polly library handles these transient failures by default.

There are multiple ways to address these issues

### Retry

Generally, these transient failures are typically self-correcting and the request is triggered after a certain interval causing it successful. Ex: Database service that processes a large number of concurrent requests that can reject further requests until the workload is eased.

We are reusing the source code of HttpClientFactory’s typed client implementation.

In order to make necessary changes to support the retry mechanism, the Polly library must include it as a NuGet package in the front-end application.

```
Microsoft.Extensions.Http.Polly
```

After adding the NuGet package, make the necessary changes in our program file

```
builder.Services.AddHttpClient<IWeatherService, WeatherService>(client =>
 {
     client.BaseAddress = new Uri("https://localhost:7054");
     client.DefaultRequestHeaders.Add("Accept", "application/json");
 })
    .AddTransientHttpErrorPolicy(policy => policy.WaitAndRetryAsync(3, _ => TimeSpan.FromSeconds(2)));
```

AddTransientHttpErrorPolicy method is a part of PollyHttpClientBuilderExtensions. It handles transient errors such as

*   Network Failure
*   HTTP 5XX status codes
*   HTTP 408 status code

The above code will retry 3 times with a time interval of 2 seconds.

Let us test this, I am using “Fiddler everywhere” to set the respective status code. You can refer to the below article to set the rules

[https://docs.telerik.com/fiddler-everywhere/knowledge-base/how-to-mock-responses](https://docs.telerik.com/fiddler-everywhere/knowledge-base/how-to-mock-responses)

![HTTP best practices using ASP.NET Core and Polly](https://cdn.c-sharpcorner.com/article/http-best-practices-using-asp-net-core-and-polly/retrypolly.webp)

Retry is great but is it sufficient?

There are many scenarios where the service might take a longer time period to fix. These faults can vary from long-term network connectivity to the complete failure of service.

Additionally, if the service is very busy handling the load. Any failure in one part of the service can cause cascading effects across services due to the retry mechanism.

For such a scenario, is best to fail quickly and give time to the service to auto-recover. Here circuit breaker comes in handy.

### Circuit Breaker

The purpose of the circuit breaker is different from the retry pattern. The retry pattern will keep retrying for iteration with the assumption of getting succeeded. However, the circuit breaker prevents an application from performing an operation that is likely to fail. The best practice is to combine both patterns to achieve resiliency.

The circuit breaker has 3 states

*   Closed: When everything is normal, the circuit remains in the closed state and the flow goes normal. When the number of failures exceeds the determined threshold then it goes into an open state
*   Open: The circuit breaker returns an error immediately without calling the upstream systems.
*   Half Open: After the configured timeout period is reached, the circuit breaker switches to the half-open state and validates whether the call to the upstream system is working without any failures. In case of failure, the circuit breaker again switches back to an open state. However, in case if it succeeds, the circuit breaker resets it back to the closed state.

Perform these changes in a program file.

```
builder.Services.AddHttpClient<IWeatherService, WeatherService>(client =>
 {
     client.BaseAddress = new Uri("https://localhost:7054");
     client.DefaultRequestHeaders.Add("Accept", "application/json");
 })
    .AddTransientHttpErrorPolicy(policy => policy.WaitAndRetryAsync(3, _ => TimeSpan.FromSeconds(2)))
    .AddTransientHttpErrorPolicy(policy => policy.CircuitBreakerAsync(5, TimeSpan.FromSeconds(10)))
```

In our application, the circuit breaker switches to the open state after the weather service API fails 5 times, and the waiting period for switching the circuit breaker to a half-open state is 10 seconds.

After 5 failures, you will receive the below error

![HTTP best practices using ASP.NET Core and Polly](https://cdn.c-sharpcorner.com/article/http-best-practices-using-asp-net-core-and-polly/circuitbreaker.webp)

Is it good enough to have a retry and circuit breaker to achieve resiliency?

Well, no.

Let us take an example, assume there are 3 services – service A, service B, and service C. Service A acts as a gateway to services B and C. Assume that service A can handle only 5 concurrent requests and that service B requires more processing time to complete the execution.

Now, imagine 10 concurrent requests triggers to Service A

1.  5 calls to service B
2.  5 calls to service C

In case, requests are forwarded to service B (time-consuming), there are high chances of timeout for service C.

Now, you might be thinking, how about sending 3 requests to service B and 2 requests to service C. In that way, we can improve the user experience and avoid timeout.

The same mentioned above can be achieved using the BulkHead pattern.

### BulkHead

The concept of BulkHead is derived from the shipping industry. A ship is built into small compartments called BulkHeads – these are used to prevent the entire ship from sinking in case of a flood.

From the above example, it will avoid cascading effects across services.

```
var bulk = Policy.BulkheadAsync<HttpResponseMessage>(3, 5, x =>
{
    Console.WriteLine("rejected"+x.OperationKey);
    return Task.CompletedTask;
});
builder.Services.AddHttpClient<IWeatherService, WeatherService>(client =>
 {
     client.BaseAddress = new Uri("https://localhost:7054");
     client.DefaultRequestHeaders.Add("Accept", "application/json");
 })
    .AddTransientHttpErrorPolicy(policy => policy.WaitAndRetryAsync(3, _ => TimeSpan.FromSeconds(2)))
    .AddTransientHttpErrorPolicy(policy => policy.CircuitBreakerAsync(5, TimeSpan.FromSeconds(10)))
    .AddPolicyHandler(policy => bulk);
```

MaxParallelism is set to 3 which means the max number of concurrent actions handled through this policy.

MaxQueuingAction is set to 5 which means the max number of actions that may be queued. Waiting for execution slot.

onBulkheadRejectedAsync is invoked when it is oversubscribed.

## Conclusion

To sum up, in this series, we learned:

*   What problems HttpClientFactory solves
*   How to use HttpClientFactory in our application
*   The way to use Named and Typed client instances
*   Implementation of resiliency patterns such as Retry, Circuit Breaker, and BulkHead.

Until the next article.

All the best.
