---
url: "https://www.michaelgmccarthy.com/2016/12/09/web-service-integrations-using-hangfire-in-asp-net-core/"
captured_at: "2020-10-30T08:38:06-03:00"
title: "Web Service Integrations Using Hangfire in ASP.NET Core"
domain: "michaelgmccarthy-com"
---

# Web Service Integrations Using Hangfire in ASP.NET Core

#### [Michael McCarthy](https://www.michaelgmccarthy.com/author/software-simplified/)

09 Dec 2016 • 11 min read

![telephones.jpg](michaelgmccarthy-com--web-service-integrations-using-hangfire-in-asp-net-core/445b6eb7cce647a8cc15a5a7f722f5d8.jpg)

By either exposing an endpoint that others will invoke into your system or making an HttpClient call to a web service outside your system, [you need to take into account the nature of RPC-style communication](https://www.michaelgmccarthy.com/2015/07/21/why-the-pope-needs-nservicebus/) and the [Fallacies of Distributed Computing](http://www.rgoarchitects.com/Files/fallacies.pdf "Opens in a new window").

Although the .NET framework has given us async/await, the naming of it is unfortunate, in that you're not really working in a true asynchronous fashion. What you're really doing is allowing the framework to utilize threads and worker processes more efficiently under the hood.

To truly operate in a asynchronous fashion you need to use some type of queue or service bus framework with an underlying transport that will allow you to return control to the calling code while relying on durable storage so your message data is never lost.

I this post, I will examine both an incoming and outgoing web service integration for [Humanitarian Toolbox](http://www.htbox.org/ "Opens in a new window")'s [AllReady project](https://github.com/HTBox/allReady "Opens in a new window"), which involved breaking RPC-style web service code into async, retry-able operations using the [Hangfire framework](http://hangfire.io/ "Opens in a new window").

## Hangfire

For those of you who missed [my previous post on Hangfire](https://www.michaelgmccarthy.com/2016/11/07/using-hangfire-to-schedule-jobs-in-asp-net-core/), [it's a framework which allows you to build "fire and forget", scheduled or recurring jobs in the .NET framework](http://hangfire.io/ "Opens in a new window"), without relying on items like Windows Scheduler.

My [previous post](https://www.michaelgmccarthy.com/2016/11/07/using-hangfire-to-schedule-jobs-in-asp-net-core/) focused on working with Hangfire's `Schedule` method, which allowed me to schedule jobs for sending out sms text messages. Since all the scheduling is in code, that means it's 100% testable, plus Hangfire gives us the durability of SQL Server (the out of the box "transport" for Hangfire) as well as a [basic retry policy](http://docs.hangfire.io/en/latest/background-processing/dealing-with-exceptions.html "Opens in a new window") that can fix most transient errors. **But most importantly, Hangfire gives us true asynchronicity that will enqueue the work to be done in a "job" and immediately return control to the caller**.

## Importing Smoke Alarm Requests into AllReady

During my continuing work on [Humanitarian Toolbox](http://www.htbox.org/ "Opens in a new window")'s [AllReady project](https://github.com/HTBox/allReady "Opens in a new window"), we were looking for a way to import smoke alarm requests into our system from a third party, [getasmokealarm.org](https://getasmokealarm.org/ "Opens in a new window") (GASA from here on out). These imported requests would be brought into AllReady's system, and once acted on (aka, assigned to an "Itinerary"), would take place in the assignment, coordination and fulfillment of the request.

Here is a look at the overall process:

1. Receive incoming http request with a smoke alarm Request on it from GASA.
2. validate the Request
3. write the Request to our database
4. decide whether or not we could "service" the Request based on region/zip code information included on the Request
5. invoke an http call back to GASA which would carry a `true` (we could service the request) or a `false` (we could not service the request) on the message.

That is large list of things to do. If I didn't think about it at all, I probably would end up with a controller that looked like this:

```
[Route("api/request")]
[Produces("application/json")]
public class RequestApiController : Controller
{
    private readonly IMediator mediator;

    publicRequestApiController(IMediator mediator){
        this.mediator = mediator;
    }

    [HttpPost]
    [ExternalEndpoint]
    publicasyncTask<IActionResult>Post([FromBody]RequestApiViewModel viewModel){
        if (!ModelState.IsValid)
        {
            return BadRequest();
        }

        //we can only accept the requests with the status of "new" from getasmokealarm
        if (viewModel.Status != "new")
        {
            return BadRequest();
        }

        //make sure we are not trying to import a duplicated Request
        if (await mediator
            .SendAsync(new RequestExistsByProviderIdQuery { ProviderRequestId = viewModel.ProviderRequestId }))
        {
            return BadRequest();
        }

        //insert the Request into our database

        //execute algorithm that determines whether or not we could service this request 
        //based on geographical information on the incoming Request
        
        //invoke HttpClient call back to GASA endpoint with a true/false if we could 
        //service the Request
        using (var httpClient = new HttpClient())
        {
            var response = httpClient.PostAsJsonAsync("PathToEndpoint", message).Result;
        }
        
        //return status code to caller
        return StatusCode(202);
    }
}

12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849
```

This code should be setting off alarm bells.

The problem here is we're starting with an RPC to `RequestApiController.Post`, validating incoming field/data, doing a database read, writing the Request to the database, running some type of algorithm to figure out if we can service the incoming Request and to top it off, invoking **another** RPC back to GASA's endpoint with our decision, **all in one process**.

This is one, long, synchronous operation with many moving parts combining transactional resources (db's) with non-transactional resources (web services).

Here is a diagram of what's going on:

![WebServiceHangfireOneTransaction-2.png](michaelgmccarthy-com--web-service-integrations-using-hangfire-in-asp-net-core/4c5b6be6844261139bb44f097f4fee78.png)

What could POSSIBLY go wrong? ;)

Stepping back, and thinking about it a little longer, I stared to see where I could break this one, large, synchronous workflow down into pieces consisting of multiple transactions and async operations bolstered by Hangfire's retry policy.

## The Incoming Integration

Let's start with the contract for the exposed WebApi controller/endpoint.

```
[Route("api/request")]
[Produces("application/json")]
public class RequestApiController : Controller
{
    [HttpPost]
    [ExternalEndpoint]
    publicasyncTask<IActionResult>Post([FromBody]RequestApiViewModel viewModel){
        //do the work
    }
}

1234567891011
```

this endpoint would be invoked from GASA with the incoming json on the message represented by the strongly typed `RequestApiViewModel`.

Now, I needed to decompose the functionality into separate processes, some of which were sync, and some of which were async keeping an eye on which async processes I'd like to bolster with Hangfire retries.

### 1. Basic field/data validation

I needed to make sure that fields on `RequestApiViewModel` were marked as `[Required]` as well as making sure data like `Phone` and `Email` were in the correct format. This was easily accomplished using data attributes and MVC's built-in model binding.

```
public class RequestApiViewModel
{
    [Required]
    public string ProviderRequestId { get; set; }
    [Required]
    public string Name { get; set; 
    [Required]
    public string Address { get; set; }
    [Required]
    public string City { get; set; }
    [Required]
    public string State { get; set; }
    [Required]
    public string Zip { get; set; }
    [Required]
    [Phone(ErrorMessage = "Invalid Mobile phone Number")]
    public string Phone { get; set; }
    [Required]
    [EmailAddress(ErrorMessage = "Invalid Email Address")]
    public string Email { get; set; }
    [Required]
    public string Status { get; set; }
    public string ProviderData { get; set; }
}

123456789101112131415161718192021222324
```

On inbound integrations, a lot of times, this type of upfront field/data validation can be considered an [anti-corruption layer](http://www.markhneedham.com/blog/2009/07/07/domain-driven-design-anti-corruption-layer/ "Opens in a new window") of sorts. All the work to make sure the Request is ingest-able into our system is done here. Most of the time, field/data validation is very simple and executes very quickly, hence, executing it synchronously should pose no problems.

I started by returning a 400 http status code for any field/data validations that failed. These checks are very quick and when one of them failed, I could immediately return a 400 to the caller (GASA) and be done with it.

```
[Route("api/request")]
[Produces("application/json")]
public class RequestApiController : Controller
{
    [HttpPost]
    [ExternalEndpoint]
    publicasyncTask<IActionResult>Post([FromBody]RequestApiViewModel viewModel){
        if (!ModelState.IsValid)
        {
            return BadRequest();
        }

        //we can only accept requests with the status of "new" from getasmokealarm
        if (viewModel.Status != "new")
        {
            return BadRequest();
        }
    }
}

1234567891011121314151617181920
```

### 2. Business validations

There were two other things I needed to check.

1. did this Request already exist in our system?
2. based on the region/zip code of the Request, did our system have the appropriate coverage in that area that would allow us to service the Request?

These types of checks are beyond basic field/data validations. Validations like this usually include things like checking the database for existing records or invoking another web service to get information that we need (in this case, possibly using a Google API to get latitude and longitude information).

> Usually, these types of validations are more complex than field/data validation, and as such, incur an overhead in execution speed and resources. Because of this, you want to try to offload these checks into an async operation where the caller's request is not left "hanging" while you're system does a lot of process-heavy work.

#### Request Validation

For the Request validation, I wrote a query against our database checking to make sure we were not trying to import a Request that already existed. If we received a Request from GASA that already existed in our system, that means something happened on their end, as they should not be sending us duplicate requests.

I ended up bringing this check into the synchronous portion where my field/data validations were, because there was no way to communicate back to GASA later that they tried to send us a duplicate Request.

Here is the code I added to the RequstApiController with the added db check for the Request:

```
[Route("api/request")]
[Produces("application/json")]
public class RequestApiController : Controller
{
    [HttpPost]
    [ExternalEndpoint]
    publicasyncTask<IActionResult>Post([FromBody]RequestApiViewModel viewModel){
        ...
        //if we get here, the incoming request is already in our database with a matching 
        //ProviderId ("serial" field for getasmokealarm) and the request was sent with a status of "new"
        if (await mediator.SendAsync(
            new RequestExistsByProviderIdQuery { 
                ProviderRequestId = viewModel.ProviderRequestId }))
        {
            return BadRequest();
        }
    }
}

12345678910111213141516171819
```

I'm using Jimmy Bogard's [MediatR framework](https://github.com/jbogard/MediatR "Opens in a new window") to send a "query" message via the mediator. The message's handler will simply see if a Request already exists in our database with the same `ProviderRequestId`.

```
public class RequestExistsByProviderIdQueryHandler : IAsyncRequestHandler<RequestExistsByProviderIdQuery, bool>
{
    private readonly AllReadyContext context;

    publicRequestExistsByProviderIdQueryHandler(AllReadyContext context){
        this.context = context;
    }

    publicasyncTask<bool>Handle(RequestExistsByProviderIdQuery message){
        return await context.Requests.AnyAsync(x => x.ProviderRequestId == message.ProviderRequestId);
    }
}

1234567891011121314
```

#### Is the Request Serviceable?

For the second validation, whether or not we can "service" the request based on region/zip code information would be more involved.

We'd have to look up some records in a database based on a user token we received on the request and match that up to an Organization. Seeing how this check could be even slower, and since we were still finalizing the code for "what does it mean for a request to be serviceable" by our system, I wanted to try to find a way to make this an async operation.

Luckily, GASA had a callable API set up on their end that allowed us to report back to them either a `true` (that we would service the request) or a `false` (that we would not service the request).

> In short, we could invoke a call back to GASA separately from their call they made to our endpoint for the initial Request. This was the perfect opportunity to make this an async operation.

[Using Hangfire's Enqueue method](http://docs.hangfire.io/en/latest/background-methods/calling-methods-in-background.html# "Opens in a new window"), I set up a job (`IProcessApiRequests`) that would create a `Request` entity in our database from the `RequestApiViewModel`. I also injected [Hangfire's IBackgroundjobClient abstraction](http://docs.hangfire.io/en/latest/background-methods/writing-unit-tests.html "Opens in a new window") so `RequestApiController` was still testable.

```
[Route("api/request")]
[Produces("application/json")]
public class RequestApiController : Controller
{
    private readonly IMediator mediator;
    private readonly IBackgroundJobClient backgroundjobClient;

    publicRequestApiController(IMediator mediator,IBackgroundJobClient backgroundjobClient){
        this.backgroundjobClient = backgroundjobClient;
        this.mediator = mediator;
    }

    [HttpPost]
    [ExternalEndpoint]
    publicasyncTask<IActionResult>Post([FromBody]RequestApiViewModel viewModel){
        ...
        //this returns control to the caller immediately so the client is not left 
        //locked while we figure out if we can service the request
        backgroundjobClient.Enqueue<IProcessApiRequests>(x => x.Process(viewModel));

        return StatusCode(202);
    }
}

12345678910111213141516171819202122232425
```

when `backgroundjobClient.Enqueue` is called, the job is serialized into durable storage in sql server to be picked up by the Hangfire server for processing on a separate thread. Control is immediately returned to the caller with a 202 http status code.

> NOTE: an HttpStatus code of 202 means that we've successfully received the request, yet processing of the request might not have been started yet, or might not be complete yet if it was started. Seeing how we still had yet to do the work of whether or not we would service this request, then invoke GASA's API with our decision, and 202 status code here makes sense. More on the 202 http status code can be found [here](https://httpstatuses.com/202 "Opens in a new window").

## The Outgoing Integration

Let's take a look at the `ProcessApiRequests` job class that was invoked via Hangfire from the `RequestApiController`:

```
public class ProcessApiRequests : IProcessApiRequests
{
    public Func<Guid> NewRequestId = () => Guid.NewGuid();
    public Func<DateTime> DateTimeUtcNow = () => DateTime.UtcNow;

    private readonly AllReadyContext context;
    private readonly IMediator mediator;
    private readonly IGeocoder geocoder;

    publicProcessApiRequests(AllReadyContext context,IMediator mediator,IGeocoder geocoder){
        this.context = context;
        this.mediator = mediator;
        this.geocoder = geocoder;
    }

    publicvoidProcess(RequestApiViewModel viewModel){
        //since this is job code now, it needs to be idempotent, this could be re-tried by 
        //Hangire if it fails
        var requestExists = context.Requests
            .Any(x => x.ProviderRequestId == viewModel.ProviderRequestId);
        if (!requestExists)
        {
            var request = new Request
            {
                RequestId = NewRequestId(),
                ProviderRequestId = viewModel.ProviderRequestId,
                ProviderData = viewModel.ProviderData,
                Address = viewModel.Address,
                City = viewModel.City,
                DateAdded = DateTimeUtcNow(),
                Email = viewModel.Email,
                Name = viewModel.Name,
                Phone = viewModel.Phone,
                State = viewModel.State,
                Zip = viewModel.Zip,
                Status = RequestStatus.Unassigned,
                Source = RequestSource.Api
            };

            var address = geocoder.Geocode(viewModel.Address, viewModel.City, 
                viewModel.State, viewModel.Zip, string.Empty).FirstOrDefault();
            request.Latitude = address?.Coordinates.Latitude ?? 0;
            request.Longitude = address?.Coordinates.Longitude ?? 0;

            context.Add(request);
            context.SaveChanges();

            mediator.Publish(new ApiRequestProcessedNotification { ProviderRequestId = viewModel.ProviderRequestId });
        }   
    }
}

123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354
```

### A Note on Idempotent Code

> When executing code within a Hangfire process you need to make the code [idempotent](http://docs.hangfire.io/en/latest/best-practices.html "Opens in a new window"). In other words, the code needs to be able to execute more than once without undesirable side effects. Because the class above could throw an error from either the `geoCoder.GeoCode()` call (which is an API into an RPC Google web service) or the `context.SaveChanges()` call, we need to make this code repeatable. This is accomplished by checking first for the existence of the Request in the database. If the does not request exists, all the code in the `Process` method is executed. If it does exist (which means we're retrying) the code is bypassed.

> This code has yet to be decomposed further into smaller transactions. We can separate the `geoCoder` call into another Hangfire-driven process and not only query for the Lat and Long data asynchronously further down the pipeline, but insert that data once retrieved into the Request. This is a work in progress, and hopefully will be done soon.

here you can see we're creating the Request in our database then publishing `ApiRequestProcessedNotification`. The`ApiRequestProcessedNotificationHandler` decides whether or not to service the Request. Let's have a look at the code:

```
public class ApiRequestProcessedNotificationHandler : INotificationHandler<ApiRequestProcessedNotification>
{
    private readonly IBackgroundJobClient backgroundJobClient;

    publicApiRequestProcessedNotificationHandler(IBackgroundJobClient backgroundJobClient){
        this.backgroundJobClient = backgroundJobClient;
    }

    publicvoidHandle(ApiRequestProcessedNotification notification){
        //TODO: a bunch of code that determines whether or not we can service the request

        backgroundJobClient.Enqueue<ISendRequestStatusToGetASmokeAlarm>(x => x.
            Send(notification.ProviderRequestId, "new", [TRUE/FALSE BASED ON IF REQUEST IS SERVICABLE]));
    }
}

1234567891011121314151617
```

Note the invocation of Hangfire's `Enqueue` method once more to execute the `ISendRequestStatusToGetASmokeAlarm` job which invokes an HttpClient call back to GASA's endpoint so we can send GASA the response as to whether or not we will service the Request.

Why are we `Enqueue`'ing a job from `ApiRequestProcessedNotificationHandler` instead of just invoking the HttpClient code directly?

1. because we want the outbound RPC operation to be async (not tied into our executing thread)
2. since Hangfire has built-in retries, and since RPC-style web service invocations often result in transient-type exceptions, we can move this async operation into a separate transaction that will [retry based on Hangfire retry policy](http://docs.hangfire.io/en/latest/background-processing/dealing-with-exceptions.html "Opens in a new window") until it succeeds or ends up in the failed messages area of the Hangfire Dashboard.

Let's have a look at the job code:

```
public class SendRequestStatusToGetASmokeAlarm : ISendRequestStatusToGetASmokeAlarm
{
    private static HttpClient httpClient;

    publicSendRequestStatusToGetASmokeAlarm(IOptions<GetASmokeAlarmApiSettings> getASmokeAlarmApiSettings){
        CreateStaticHttpClient(getASmokeAlarmApiSettings);
    }

    publicvoidSend(string serial,string status,bool acceptance){
        var updateRequestMessage = new { acceptance, status };
        var response = httpClient.PostAsJsonAsync(
            $"{getASmokeAlarmApiSettings.Value.BaseAddress}PATH_TO_GASA_ENDPOINT{serial}", 
                updateRequestMessage).Result;
        
        //throw HttpRequestException if response is not a success code.
        response.EnsureSuccessStatusCode();
    }

    privatevoidCreateStaticHttpClient(IOptions<GetASmokeAlarmApiSettings> getASmokeAlarmApiSettings){
        if (httpClient == null)
        {
            httpClient = new HttpClient();
            httpClient.DefaultRequestHeaders.Accept.Clear();
            httpClient.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));
            httpClient.DefaultRequestHeaders.Add("Authorization", getASmokeAlarmApiSettings.Value.Token);
        }
    }
}

12345678910111213141516171819202122232425262728293031
```

Here we invoke the GASA endpoint to communicate back to them whether or not we'll service the Request. Note the use of `response.EnsureSuccessStatusCode();`. This will throw an exception if the status code is not 200. But remember, since this class is being run by Hangfire, when an exception is thrown, Hangfire's retry policy is invoked until either the call succeeds or the "message" is moved into Hangfire's failed message holding area in the Hangfire dashboard.

## Summary

Here is a look at the final "flow" of the message in, processing and message out:

![WebServiceHangfireMultipleTransactions.png](michaelgmccarthy-com--web-service-integrations-using-hangfire-in-asp-net-core/a7fb5f25b6c3ffc1f96ec82da76baa58.png)

What could have been an RPC-locking nightmare of an integration (both inbound and outbound) is now a transactionally consistent, async and retry-friendly operation that should mitigate most of the transient errors that can be thrown at us from RPC web services.
