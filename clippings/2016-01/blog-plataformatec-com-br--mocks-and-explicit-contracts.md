---
url: "http://blog.plataformatec.com.br/2015/10/mocks-and-explicit-contracts/"
captured_at: "2016-01-02T13:57:17-03:00"
title: "Mocks and explicit contracts"
domain: "blog-plataformatec-com-br"
---

# Mocks and explicit contracts

A couple days ago I expressed my thoughts regarding mocks on Twitter:

The blame is not on mocks though, they are actually a useful technique for testing. However our test tools often maks it very easy to abuse mocks and the goal of this post is to provide better guidelines on using them.

## What are mocks?

The [wikipedia definition](https://en.wikipedia.org/wiki/Mock_object) is excellent: mocks are simulated entities that mimic the behavior of real entities in controlled ways. I will emphasize this later on but I always consider “mock” to be a noun, never a verb.

## Case study: external APIs

Let’s see a common practical example: external APIs.

Imagine you want to consume the Twitter API in your web application and you are using something like Phoenix or Rails. At some point, a web request will come-in, which will be dispatched to a controller which will invoke the external API. Let’s imagining this is happening directly from the controller:

```
defmodule MyApp.MyController 
  (conn, %{"username" => username}) 
    
    MyApp.TwitterClient.get_username(username)
```

The code may work as expected but, when it comes to make the tests pass, a common practice is to just go ahead and *mock* (warning! mock as a verb!) the underlying `HTTPClient` used by `MyApp.TwitterClient`:

```
mock(HTTPClient, , to_return: %{..., "username" => "josevalim", ...})
```

You proceed to use the same technique in a couple other places and your unit and integration test suites pass. Time to move on?

Not so fast. The whole problem with mocking the `HTTPClient` is that you just coupled your application to that particular `HTTPClient`. For example, if we decide to use a new and faster HTTP client, a good part of your integration test suite will now fail because it all depends on mocking `HTTPClient` itself, *even when the application behaviour is the same*. In other words, the mechanics changed, the behaviour is the same, but your tests fail anyway. That’s a bad sign.

Furthermore, because mocks like the one above changes modules *globally*, they are particularly aggravating in Elixir as changing global values means you can no longer run that part of your test suite concurrently.

### The solution

Instead of mocking the whole `HTTPClient`, we could replace the Twitter client (`MyApp.TwitterClient`) by something else during tests. Let’s explore how the solution would look like in Elixir.

In Elixir, all applications ship with configuration files and a mechanism to read them. Let’s use this mechanism to be able to configure the Twitter client for different environments. The controller code should now look like this:

```
defmodule MyApp.MyController 
  @twitter_api Application.get_env(:my_app, :twitter_api)

  (conn, %{"username" => username}) 
    
    @twitter_api.get_username(username)
```

And now we can configure it per environment as:

```
# In config/dev.exs
config :my_app, :twitter_api, MyApp.Twitter.Sandbox

# In config/test.exs
config :my_app, :twitter_api, MyApp.Twitter.InMemory

# In config/prod.exs
config :my_app, :twitter_api, MyApp.Twitter.HTTPClient
```

This way we can choose the best strategy to retrieve data from Twitter per environment. The sandbox one is useful if Twitter provides some sort of sandbox for development. The `HTTPClient` is our previous implementation while the in memory avoids HTTP requests altogether, by simply loading and keeping data in memory. Its implementation could be defined in your test files and even look like:

```
defmodule MyApp.Twitter.InMemory 
   get_username("josevalim") 
    %MyApp.Twitter.User{
      username: "josevalim"
    }
```

which is as clean and simple as you can get. At the end of the day, **`MyApp.Twitter.InMemory` is a mock** (mock as a noun, yay!), except you didn’t need any fancy library to define one! The dependency on `HTTPClient` is gone as well.

### The need for explicit contracts

Because a mock is meant to replace a real entity, such replacement can only be effective if we have explicitly defined how the real entity should behave. Failing this, you will find yourself in the situation where the mock entity grows more and more complex with time, increasing the coupling between the components being tested, but you won’t ever notice it because the contract was never explicit.

Furthermore, we have already defined three implementations of the Twitter API, so we better make it all explicit. In Elixir we do so by defining a behaviour with callback functions:

```
defmodule MyApp.Twitter 
   "..."
  @callback get_username(username  String.t)  %MyApp.Twitter.User{}
   "..."
  @callback followers_for(username  String.t)  [%MyApp.Twitter.User{}]
```

Now add `@behaviour MyApp.Twitter` on top of every module that implements the behaviour and Elixir will help you provide the expected API.

It is interesting to note we rely on such behaviours *all the time* in Elixir: when you are using Plug, when talking to a repository in Ecto, when testing Phoenix channels, etc.

### Testing the boundaries

Previously, because we didn’t have a explicit contract, our application boundaries looked like this:

```
[MyApp] -> [HTTP Client] -> [Twitter API]
```

That’s why changing the `HTTPClient` could break your integration tests. Now our app depends on a contract and only one implementation of such contract/behaviour rely on HTTP:

```
[MyApp] -> [MyApp.Twitter (contract)]
[MyApp.Twitter.HTTP (contract impl)] -> [HTTPClient] -> [Twitter API]
```

Our application tests are now isolated from both the `HTTPClient` and the Twitter API. However, how can we test `MyApp.Twitter.HTTP` (the second line)?

The challenge in testing a large system is exactly in finding the proper boundaries. If you define and isolate too many of them without integration tests, your tests can become brittle and you will end-up finding errors only in production. On the other hand, defining very few boundaries can lead to slow suites and hard to debug tests. Often times there is no correct answer and boundaries will vary depending on the team confidence and other external factors.

Personally, I would test `MyApp.Twitter.HTTP` by directly reaching the Twitter API. We would run those tests only when needed in development and configure them as necessary in our build system. The `@tag` system in ExUnit, Elixir’s test library, provides conveniences to help us with that:

```
defmodule MyApp.Twitter.HTTPTest 
   ExUnit.Case, async: 

  # All tests will ping the twitter API
  @moduletag :twitter_api

  # Write your tests here
```

In your test helper, you want to exclude the Twitter API test by default:

```
ExUnit.configure exclude: [:twitter_api]
```

But you can still run the whole suite with the tests tagged `:twitter_api` if desired:

```
mix  --include twitter_api
```

Or run only the tagged tests:

```
mix  --only twitter_api
```

Although I prefer this approach, external conditions like rate limiting may make such solution inpractical. In such cases, we may actually need a mock HTTPClient, as long as we don’t break the properties we have previously defined:

1. If you change your HTTP client, your application suite won’t break but only the tests for `MyApp.Twitter.HTTP`
2. You won’t mock (warning! mock as a verb) your HTTP client. Instead, you will pass it as a dependency via configuration, similar to how we did for the Twitter API
3. You still need a way to test, that is not in production, that your client works as expected

Alternatively, you may avoid mocking the HTTP client by running a dummy webserver that emulates the Twitter API. [bypass](https://github.com/pspdfkit-labs/bypass) is one of many projects that can help with that. Those are all options you should discuss with your team.

## Other notes

I would like to finish this article by bringing up some common concerns and comments whenever the mock discussion comes up.

### Making the code “testable”

Quoting from [elixir-talk mailing list](https://groups.google.com/d/msg/elixir-lang-talk/oYXyvEUi64Y/_sNnsoirCQAJ):

> So the proposed solution is to change production code to be “testable” and making production code to call Application configuration for every function call? This doesn’t seem like a good option as it’s including a unnecessary overhead to make something “testable”.

I’d argue it is not about making the code “testable”, it is about improving the design of your code.

A test is a consumer of your API like any other code you write. One of the ideas behind TDD is that tests are code and no different from code. If you are saying “I don’t want to make my code testable”, you are saying “I don’t want to decouple some modules” or “I don’t want to think about the contract behind these components”.

Just to clarify, there is nothing wrong with “not wanting to decouple some modules”. For example, you don’t want to decouple every time you call the `URI` module. But if we are talking about something as complex as an external API or such, defining an explicit contract and making the contract implementation configurable is going to make your code wonders and make it easier to manage its complexity.

Finally, the overhead is also minimum. Application configuration in Elixir is stored in ETS tables which means they are directly read from memory.

### Mocks as locals

Although we have used the application configuration for solving the external API issue, sometimes it is easier to just pass the dependency as argument. Imagine this example in Elixir where some function may perform heavy work which you want to isolate in tests:

```
defmodule MyModule 
   my_function 
    
    SomeDependency.heavy_work(arg1, arg2)
```

You could remove the dependency by passing it as an argument, which can be done in multiple ways. If your dependency surface is tiny, an anonymous function will suffice:

```
defmodule MyModule 
   my_function(heavy_work \\ &SomeDependency.heavy_work/) 
    
    heavy_work.(arg1, arg2)
```

And in your test:

```
test "my function performs heavy work" 
  heavy_work =   ->
    # Simulate heavy work by sending self() a message
    send (), :heavy_work
  

  MyModule.my_function(heavy_work)

  assert_received :heavy_work
```

Or define the contract, as explained in the previous section of this post, and pass a module in:

```
defmodule MyModule 
   my_function(dependency \\ SomeDependency) 
    
    dependency.heavy_work(arg1, arg2)
```

Now in your test:

```
test "my function performs heavy work" 
  # Simulate heavy work by sending self() a message
  defmodule TestDependency 
     heavy_work(_arg1, _arg2) 
      send (), :heavy_work
    
  

  MyModule.my_function(TestDependency)

  assert_received :heavy_work
```

Finally, you could also make the dependency a data structure and define the contract with [a protocol](http://elixir-lang.org/getting-started/protocols.html).

In fact, passing the dependency as argument is much simpler and therefore should be preferred over relying on configuration files and `Application.get_env/3`. When not possible, the configuration system is a good fallback.

### Mocks as nouns

Another way to think about mocks is to treat them as nouns. You shouldn’t mock an API (verb), instead you create a mock (noun) that implements a given API.

Most of the bad uses of mocks come when they are used as verbs. That’s because, when you use mock as a verb, you are changing something that already exists, and often those changes are global. For example, when we say we will mock the `SomeDependency` module:

```
mock(SomeDependency, :heavy_work, to_return: )
```

When you use mock as a noun, you need to create something new, and by definition it cannot be the `SomeDependency` module because it already exists. So “mock” is not an action, it is something you pass around. I’ve found the noun-verb guideline to be very helpful when spotting bad use of mocks. Your mileage may vary.

### Mock libraries

With all that said, should you discard your mock library?

It depends. If your library incentivates you to break the guidelines above, like using mocks to replace global entities (or using mock as a verb), changing static methods in OO or replacing modules in FP languages, you should definitely consider how the library is being used in your codebase and potentially discard it.

However there are mock libraries that does not promote any of the “anti-patterns” above and are mostly convenience to define “mock objects” or “mock modules” that you would pass to the testing system as argument and collect information how many times the mock was invoked, with which arguments and so on.

## Summing up

Part of testing your system is to find the proper contracts and proper boundaries between the components. If you follow closely a guideline that mocks will be used only if you define a explicit contract, it will:

1. protect you from overmocking as it will push you to define contracts only for the parts of your system that matters (as mentioned, you very likely don’t want to hide interactions with the `URI` or `Enum` modules behind a contract)
2. make it easier to manage the complexity between the components themselves. Every time you need a new function from your dependency, you need to add it to the contract (a new `@callback` in our Elixir code). If the list of `@callback`s are getting bigger and bigger, it will be noticiable as the knowledge is in one place and you will be able to act on it
3. make it easier to test your system because it will push you to isolate the interaction between complex components

Defining contracts allows us to see the complexity in our dependencies. Your application will always have complexity, so always make it as explicit as you can.
