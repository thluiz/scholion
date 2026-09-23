---
url: "https://blog.ploeh.dk/2024/09/02/keeping-cross-cutting-concerns-out-of-application-code/"
captured_at: "2026-09-23T19:37:15+01:00"
title: "Keeping cross-cutting concerns out of application code"
domain: "blog-ploeh-dk"
---
ploeh blog
About
Archive
Hire Me
Pages
Schedule
Support the blog
Tags
Keeping cross-cutting concerns out of application code by Mark Seemann

Don't inject third-party dependencies. Use Decorators.

I recently came across a Stack Overflow question that reminded me of a topic I've been meaning to write about for a long time: Cross-cutting concerns.

When it comes to the usual suspects, logging, fault tolerance, caching, the best solution is usually to apply the Decorator pattern.

I often see code that uses Dependency Injection (DI) to inject, say, a logging interface into application code. You can see an example of that in Repeatable execution, as well as a suggestion for a better design. Not surprisingly, the better design involves logging Decorators.

The Stack Overflow question isn't about logging, but rather about fault tolerance; Circuit Breaker, retry policies, timeouts, etc.

Injected concern #

The question does a good job of presenting a minimal, reproducible example. At the outset, the code looks like this:

public class MyApi
{
    private readonly ResiliencePipeline pipeline;
    private readonly IOrganizationService service;
 
    public MyApi(ResiliencePipelineProvider<string> provider, IOrganizationService service)
    {
        this.pipeline = provider.GetPipeline("retry-pipeline");
        this.service = service;
    }
 
    public List<string> GetSomething(QueryByAttribute query)
    {
        var result = this.pipeline.Execute(() => service.RetrieveMultiple(query));
        return result.Entities.Cast<string>().ToList();
    }
}

The Stack Overflow question asks how to test this implementation, but I'd rather take the example as an opportunity to discuss design alternatives. Not surprisingly, it turns out that with a more decoupled design, testing becomes easier, too.

Before we proceed, a few words about this example code. I assume that this isn't Andy Cooke's actual production code. Rather, I interpret it as a reduced example that highlights the actual question. This is important because you might ask: Why bother testing two lines of code?

Indeed, as presented, the GetSomething method is so simple that you may consider not testing it. Thus, I interpret the second line of code as a stand-in for more complicated production code. Hold on to that thought, because once I'm done, that's all that's going to be left, and you may then think that it's so simple that it really doesn't warrant all this hoo-ha.

Coupling #

As shown, the MyApi class is coupled to Polly, because ResiliencePipeline is defined by that library. To be clear, all I've heard is that Polly is a fine library. I've used it for a few projects myself, but I also admit that I haven't that much experience with it. I'd probably use it again the next time I need a Circuit Breaker or similar, so the following discussion isn't a denouncement of Polly. Rather, it applies to all third-party dependencies, or perhaps even dependencies that are part of your language's base library.

Coupling is a major cause of spaghetti code and code rot in general. To write sustainable code, you should be cognizant of coupling. The most decoupled code is code that you can easily delete.

This doesn't mean that you shouldn't use high-quality third-party libraries like Polly. Among myriads of software engineering heuristics, we know that we should be aware of the not-invented-here syndrome.

When it comes to classic cross-cutting concerns, the Decorator pattern is usually a better design than injecting the concern into application code. The above example clearly looks innocuous, but imagine injecting both a ResiliencePipeline, a logger, and perhaps a caching service, and your real application code eventually disappears in 'infrastructure code'.

It's not that we don't want to have these third-party dependencies, but rather that we want to move them somewhere else.

Resilient Decorator #

The concern in the above example is the desire to make the IOrganizationService dependency more resilient. The MyApi class only becomes more resilient as a transitive effect. The first refactoring step, then, is to introduce a resilient Decorator.

public sealed class ResilientOrganizationService(
    ResiliencePipeline pipeline,
    IOrganizationService inner) : IOrganizationService
{
    public QueryResult RetrieveMultiple(QueryByAttribute query)
    {
        return pipeline.Execute(() => inner.RetrieveMultiple(query));
    }
}

As Decorators must, this class composes another IOrganizationService while also implementing that interface itself. It does so by being an Adapter over the Polly API.

I've applied Nikola Malovic's 4th law of DI:

"Every constructor of a class being resolved should not have any implementation other then accepting a set of its own dependencies."

Inversion Of Control, Single Responsibility Principle and Nikola's laws of dependency injection, Nikola Malovic, 2009

Instead of injecting a ResiliencePipelineProvider<string> only to call GetPipeline on it, it just receives a ResiliencePipeline and saves the object for use in the RetrieveMultiple method. It does that via a primary constructor, which is a recent C# language addition. It's just syntactic sugar for Constructor Injection, and as usual F# developers should feel right at home.

Simplifying MyApi #

Now that you have a resilient version of IOrganizationService you don't need to have any Polly code in MyApi. Remove it and simplify:

public class MyApi
{
    private readonly IOrganizationService service;
 
    public MyApi(IOrganizationService service)
    {
        this.service = service;
    }
 
    public List<string> GetSomething(QueryByAttribute query)
    {
        var result = service.RetrieveMultiple(query);
        return result.Entities.Cast<string>().ToList();
    }
}

As promised, there's almost nothing left of it now, but I'll remind you that I consider the second line of GetSomething as a stand-in for something more complicated that you might need to test. As it is now, though, testing it is trivial:

[Theory]
[InlineData("foo", "bar", "baz")]
[InlineData("qux", "quux", "corge")]
[InlineData("grault", "garply", "waldo")]
public void GetSomething(params string[] expected)
{
    var service = new Mock<IOrganizationService>();
    service
        .Setup(s => s.RetrieveMultiple(new QueryByAttribute()))
        .Returns(new QueryResult(expected));
    var sut = new MyApi(service.Object);
 
    var actual = sut.GetSomething(new QueryByAttribute());
 
    Assert.Equal(expected, actual);
}

The larger point, however, is that not only have you now managed to keep third-party dependencies out of your application code, you've also simplified it and made it easier to test.

Composition #

You can still create a resilient MyApi object in your Composition Root:

var service = new ResilientOrganizationService(pipeline, inner);
var myApi = new MyApi(service);

Decomposing the problem in this way, you decouple your application code from third-party dependencies. You can define ResilientOrganizationService in the application's Composition Root, which also keeps the Polly dependency there. Even so, you can implement MyApi as part of your application layer.

I usually illustrate Ports and Adapters, or, if you will, Clean Architecture as concentric circles, but in this diagram I've skewed the circles to make space for the boxes. In other words, the diagram is 'not to scale'. Ideally, the outermost layer is much smaller and thinner than any of the the other layers. I've also included an inner green layer which indicates the architecture's Domain Model, but since I assume that MyApi is part of some application layer, I've left the Domain Model empty.

Reasons to decouple #

Why is it important to decouple application code from Polly? First, keep in mind that in this discussion Polly is just a stand-in for any third-party dependency. It's up to you as a software architect to decide how you'll structure your code, but third-party dependencies are one of the first things I look for. A third-party component changes with time, and often independently of your base platform. You may have to deal with breaking changes or security patches at inopportune times. The organization that maintains the component may cease to operate. This happens to commercial entities and open-source contributors alike, although for different reasons.

Second, even a top-tier library like Polly will undergo changes. If your time horizon is five to ten years, you'll be surprised how much things change. You may protest that no-one designs software systems with such a long view, but I think that if you ask the business people involved with your software, they most certainly expect your system to last a long time.

I believe that I heard on a podcast that some Microsoft teams had taken a dependency on Polly. Assuming, for the sake of argument, that this is true, while we may not wish to depend on some random open-source component, depending on Polly is safe, right? In the long run, it isn't. Five years ago, you had the same situation with Json.NET, but then Microsoft hired James Newton-King and had him make a JSON API as part of the .NET base library. While Json.NET isn't dead by any means, now you have two competing JSON libraries, and Microsoft uses their own in the frameworks and libraries that they release.

Deciding to decouple your application code from a third-party component is ultimately a question of risk management. It's up to you to make the bet. Do you pay the up-front cost of decoupling, or do you postpone it, hoping it'll never be necessary?

I usually do the former, because the cost is low, and there are other benefits as well. As I've already touched on, unit testing becomes easier.

Configuration #

Since Polly only lives in the Composition Root, you'll also need to define the ResiliencePipeline there. You can write the code that creates that pieline wherever you like, but it might be natural to make it a creation function on the ResilientOrganizationService class:

public static ResiliencePipeline CreatePipeline()
{
    return new ResiliencePipelineBuilder()
        .AddRetry(new RetryStrategyOptions
        {
            MaxRetryAttempts = 4
        })
        .AddTimeout(TimeSpan.FromSeconds(1))
        .Build();
}

That's just an example, and perhaps not what you'd like to do. Perhaps you rather want some of these values to be defined in a configuration file. Thus, this isn't what you have to do, but rather what you could do.

If you use this option, however, you could take the return value of this method and inject it into the ResilientOrganizationService constructor.

Conclusion #

Cross-cutting concerns, like caching, logging, security, or, in this case, fault tolerance, are usually best addressed with the Decorator pattern. In this article, you saw an example of using the Decorator pattern to decouple the concern of fault tolerance from the consumer of the service that you need to handle in a fault-tolerant manner.

The specific example dealt with the Polly library, but the point isn't that Polly is a particularly nasty third-party component that you need to protect yourself against. Rather, it just so happened that I came across a Stack Overflow question that used Polly, and I though it was a a nice example.

As far as I can tell, Polly is actually one of the top .NET open-source packages, so this article is not a denouncement of Polly. It's just a sketch of how to move useful dependencies around in your code base to make sure that they impact your application code as little as possible.

← Previous
Archive
Next →
Wish to comment?
You can add a comment to this post by sending me a pull request. Alternatively, you can discuss this post on Twitter or somewhere else with a permalink. Ping me with the link, and I may respond.
Published
Monday, 02 September 2024 06:19:00 UTC
Tags
Software Design 317
Object-oriented Programming 12
Design Patterns 46
Support the blog
Buy my book Code That Fits in Your Head
Buy my book about Dependency Injection
Watch my Pluralsight courses
Watch my Clean Coders videos
Public speaking schedule

"Our team wholeheartedly endorses Mark. His expert service provides tremendous value."
Hire me!

© Mark Seemann 2024 with help from Jekyll Bootstrap and Twitter Bootstrap
</content>
