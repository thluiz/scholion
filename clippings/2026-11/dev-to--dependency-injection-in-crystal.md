---
url: "https://dev.to/blacksmoke16/dependency-injection-in-crystal-2d66"
captured_at: "2026-11-16T19:09:24+00:00"
title: "Dependency Injection in Crystal"
domain: "dev-to"
---

**UPDATE:** January 12, 2020 for Athena version `0.8.0`  
**UPDATE:** June 16, 2020 for Athena version `0.9.0`

## [](#dependency-injection-di)Dependency Injection (DI)

Dependency Injection can be a powerful tool in making an application easier to test, more expandable, and increase the flexibility of the system's components.

This article assumes you are somewhat familiar with the concepts of DI. If not, check out some of these other articles:

*   [A quick intro to Dependency Injection](https://www.freecodecamp.org/news/a-quick-intro-to-dependency-injection-what-it-is-and-when-to-use-it-7578c84fa88f/)
*   [Dependency Inversion Principle with Code Examples](https://stackify.com/dependency-inversion-principle/)

DI is usable in every language, although it is more common in some than others. Crystal, and Ruby by extension, seem to not utilize DI as much as other languages. While its out of scope of this article to figure out _why_ that is, lets go through some useful patterns and examples of _how_ DI can be useful in your application.

We'll be using Crystal as our language of choice, along with [Athena](https://github.com/athena-framework/athena) as our framework. Athena's DI component is also available as a [standalone shard](https://github.com/athena-framework/dependency-injection).

## [](#manager)Manager

The first example is what I call the "manager" pattern. This pattern is most useful when dealing with multiple object instances based on a singular class/interface. I.e. multiple objects instantiated from the same class.

### [](#problem-statement)Problem Statement

Say you are going to partner with _n_ other companies. You want to setup an API endpoint that would expose partner specific data within your system for them to consume. You also want it to be easy to add partners; requiring minimal to no code changes to do so.

### [](#solution)Solution

*   Define a `Partner` class that implements common methods/properties that each partner would have in common.
*   Define a `PartnerManager` class that would be responsible for "managing" the `Partner` instances.
*   Define a `PartnerParamConverter` used to convert a partner's id (obtained from the API route) into a `Partner` instance.
*   Define a `PartnerController` to group of the logic of partner related API endpoints.

### [](#the-code)The Code

```
require "athena"

private PARTNER_TAG = "partner"

# Define a type that all partners wil be based off of, then register some partners.
@[ADI::Register(_id: "GOOGLE", name: "google")]
@[ADI::Register(_id: "FACEBOOK", name: "facebook")]
record Partner, id : String

# We can also use `ADI.auto_configure` to handle applying the
# correct tag to each `Partner` instance.
ADI.auto_configure Partner, {tags: [PARTNER_TAG]}

# Define another service that will have all partners injected into it.
# This manager will be injected into our param converter to handle
# resolving a `Partner` from their id.
@[ADI::Register(_partners: "!partner")]
struct PartnerManager
  @partners : Hash(String, Partner) = {} of String => Partner

  def initialize(partners : Array(Partner))
    # Create a mapping of partner ID to the partner instance.
    partners.each do |partner|
      @partners[partner.id] = partner
    end
  end

  # Returns a `Partner` with the provided *partner_id* or raises an
  # `ART::Exceptions::NotFound` exception if one could not be found.
  def get(partner_id : String) : Partner
    @partners[partner_id]? || raise ART::Exceptions::NotFound.new "No partner with an ID '#{partner_id}' has been registered."
  end
end

@[ADI::Register]
struct PartnerParamConverter < ART::ParamConverterInterface
  def initialize(@partner_manager : PartnerManager); end

  # :inherit:
  def apply(request : HTTP::Request, configuration : Configuration) : Nil
    # Grab the partner's ID from the request's attributes, then resolve it into a Partner.
    # Path/query params are automatically populated into the attributes.
    partner = @partner_manager.get request.attributes.get "id", String

    # Add the resolved partner object to the request's attributes
    # for it to later be resolved for the controller action argument.
    request.attributes.set configuration.name, partner, Partner
  end
end

# The controller that would house all partner related endpoints.
class PartnerController < ART::Controller
  @[ART::ParamConverter("partner", converter: PartnerParamConverter)]
  get "partner/:id", partner : Partner do
    # Notice we have access to the actual `Partner` object.
    # From here you can do whatever you need with the object.
    "Resolved #{partner.id}!"
  end
end

ART.run

# GET /partner/FOO    # => {"code":404,"message":"No partner with an ID 'FOO' has been registered."}
# GET /partner/GOOGLE # => "Resolved Google!"
```

Enter fullscreen mode Exit fullscreen mode

### [](#why-it-matters)Why It Matters

From here, if you wanted to add another partner you would simply register another partner service and everything would just work. E.x. `@[ADI::Register(_id: "YAHOO", name: "yahoo")]`.

This also makes the code generic. Nothing specific to any particular partner is defined anywhere other than their instance of the `Partner` class.

### [](#alternate-solutions)Alternate solutions

*   Hard code an array of `Partner` objects within the controller.
    *   This wouldn't be an ideal solution since it would tightly couple the `Partner` struct and the `PartnerController`. It shouldn't be the responsibility of the `PartnerController` to know all possible partners. It also would make updating/maintaining/testing of the controller harder due to that extra dependency.
*   Store the partner data in a database.
    *   Since our system isn't actually doing anything in the partner's system, this would just be mostly dead data. It would only exist for the sole purpose of resolving the ID. Having unnecessary data is just wasteful.

## [](#plug-and-play)Plug and Play

The next example isn't so much a pattern, but a core feature of DI. The ability to change the functionality of a class by just changing what service gets injected into it.

### [](#problem-statement)Problem Statement

You have a Worker class that will do some work, then write the output to `x`. `x` is an external service like Amazon `S3`, the local file system, `Redis`, etc. To start this worker will only support one of them, say `S3`. However, we want to be able to design the class in such a way where the implementation is generic and could work with any other service in the future if so desired.

### [](#solution)Solution

*   Define an "interface", in Crystal's case we'll use a module, to define the public API of our writers
*   Register an initial implementation of the interface for `S3`
    *   Register another implementation for `Redis`, but default to `S3` as the default implementation
*   Handle injecting the proper writer into our `Worker` class
*   Create a test for our class.

### [](#the-code)The Code

#### [](#initial-interface-implementation)Initial Interface Implementation

```
require "athena"

# Define an abstract class that will act as our base interface.
# It also will ensure our subclasses implement the correct method.
module WriterInterface
  abstract def write(content : String) : Nil
end

# Create an implementation of `WriterInterface` for S3 and register it.
@[ADI::Register]
class S3Writer
  include WriterInterface

  # :inherit:
  def write(content : String) : String
    # Write the content
    "Wrote data to S3"
  end
end

# Register our worker also as a service, and set it as public.
# Ideally everything would be a service, however in most cases
# at least one service will need to be public in order to be
# the "entrypoint" into the application.
@[ADI::Register(public: true)]
class Worker
  @writer : WriterInterface

  # DI will automatically resolve the correct `WriterInterface` based on the
  # type restriction of the argument, and optionally the argument's name (more on that later).
  def initialize(writer : WriterInterface)
    # Manually assign the ivar to make changing the writer instance easier;
    # as we would only have to update these two variables within initialize versus
    # throughout the class.
    @writer = writer
  end

  def do_work
    # Do some work
    @writer.write "did work"
  end
end

# Grab out worker instance from the container and see what work it does.
ADI.container.worker.do_work # => Wrote data to S3
```

Enter fullscreen mode Exit fullscreen mode

At the moment, since we only have one implementation of the `WriterInterface`, this example isn't that much more beneficial than just instantiating the `S3Writer` within the `Worker`. However, this changes when we introduce more than one implementation.

#### [](#multiple-interface-implementations)Multiple Interface Implementations

Based off the previous example:  

```
# Add another implementation for `Redis`
@[ADI::Register]
class RedisWriter
  include WriterInterface

  # :inherit:
  def write(content : String) : String
    # Write the content
    "Wrote content to Redis"
  end
end
```

Enter fullscreen mode Exit fullscreen mode

However, we now have a little problem. Since `ADI` resolves services based on argument type restrictions, and we now have multiple implementations of `WriterInterface`, how does it know which one to inject? We have two options:

##### [](#aliases)Aliases

`ADI` has the concept of [Service Aliases](https://athena-framework.github.io/dependency-injection/Athena/DependencyInjection/Register.html#aliasing-services) that allow defining a "default" service to use when the `WriterInterface` type restriction is encountered.  

```
# The `S3Writer` will now be injected by default
# when the `WriterInterface` type restriction is encountered.
@[ADI::Register(alias: WriterInterface)]
class S3Writer
  ...
end
```

Enter fullscreen mode Exit fullscreen mode

##### [](#argument-name)Argument Name

While having a default implementation is good the majority of the time, what if we want the _other_ implementation? This case can be handled by updating the name of the argument so that the resolution logic would now be based on both the type restriction _AND_ the name of the argument.  

```
@[ADI::Register(public: true)]
class Worker
  @writer : WriterInterface

  # DI would now automatically inject `RedisWriter` since its a `WriterInterface` instance
  # AND it's service name is `redis_writer`.
  def initialize(redis_writer : WriterInterface)
    @writer = redis_writer
  end

  ...
end
```

Enter fullscreen mode Exit fullscreen mode

#### [](#testing)Testing

One of the major benefits DI allows for is easier testing since nothing is too tightly coupled with anything else, i.e. everything is built upon abstractions aka interfaces.  

```
require "spec"

# Create a mock writer.
# This allows mocking the response from the external service as we shouldn't be worried about
# how the other service works since we should only be testing our worker, not its dependencies.
class MockWriter
  include WriterInterface

  def write(content : String) : String
    "WROTE_MOCK_DATA"
  end
end

# We can now test the functionality of our `Writer` type in isolation.
describe Worker do
  describe "#do_work" do
    it "should do work" do
      Worker.new(MockWriter.new).do_work.should eq "WROTE_MOCK_DATA"
    end
  end
end
```

Enter fullscreen mode Exit fullscreen mode

### [](#why-it-matters)Why It Matters

Since we defined the type restriction as our `WriterInterface` module, our `Writer` class is not tightly coupled with any one specific implementation of it. We are able to easily change which implementation gets injected by either updating our `alias`, or simply changing the name of the initializer argument.

As mentioned previously, one of the main benefits of this is to make the `Worker` class depend on upon abstractions as opposed to concrete classes. Or in other words, prevent a singular implementation from being tightly coupled with the `Worker` class. As long as each implementation correctly implements `WriterInterface`, the `Worker` class shouldn't care about which implementation it's using, just that calling `.write` on it, writes the content correctly.

Each `WriterInterface` implementation could also easily inject their own dependencies, such as credentials, API clients etc.

Another benefit of this pattern is if you have a service that has a singular purpose such as sending an email; you could easily reuse the service. For example, simply inject the `EmailProvider` service, then use it to send emails.

DI removes the need to worry about _how_ and _where_ objects are getting instantiated. If the `EmailProvider` had dependencies of its own and you were doing `sender = EmailProvider.new xxx` each time an email needed sent; that is less than ideal. DI allows the class to be instantiated once with the given arguments; then it can simply be injected where it's needed. E.x. `def initialize(@sender : EmailProvider); end`.

The `EmailProvider` service would ideally be tested so you can have confidence that anywhere you inject it, the emails will be sent properly without having to test the same logic multiple times. Speaking of tests, DI allows us to define a test implementation of `WriterInterface` . When testing a class with dependencies on other services, the dependencies should always be mocked. This gives you control over _how_ those services act. If you didn't mock them out and used the actual implementations your tests would be testing much more than they should.

## [](#sharing-data)Sharing Data

The last example is going to show how DI can be used to share data between disparate types.

### [](#problem-statement)Problem Statement

You are creating a JSON API. You recently got to the point of where you need to handle user authentication. You want to design things in such a way that allows you to access the current user outside of the request context.

### [](#solution)Solution

*   Define a service that will store current user object
*   Set the user on that service within your `SecurityListener` handles authorization.
    *   Also add some `Log` context to include this user's information
*   Use this service to expose user information via an endpoint

### [](#the-code)The Code

```
require "athena"

# Our user object, this would most likely be an ORM model.
class User
  include JSON::Serializable

  getter id, customer_id, name

  private def initialize(@id : Int64, @customer_id : Int64, @name : String); end

  # Simulate a ORM query method.
  def self.find(id : Int) : self
    new 1, 12, "Fred"
  end
end

@[ADI::Register]
# Our service that will store user the currently logged in user.
class UserStorage
  property! user : User
end

@[ADI::Register]
# Our custom listener that listens on the Request event.
#
# It'll handle making sure the user's token is valid, and setting the current user.
struct SecurityListener
  include AED::EventListenerInterface

  def self.subscribed_events : AED::SubscribedEvents
    AED::SubscribedEvents{
      ART::Events::Request => 30, # Set the priority higher so it runs before routing
    }
  end

  def initialize(@user_storage : UserStorage); end

  def call(event : ART::Events::Request, dispatcher : AED::EventDispatcherInterface) : Nil
    # Logic to make sure a token is provided.
    token = "PARSED_TOKEN"

    # Logic to validate the token and get the stored user_id from it.
    user_id = 1

    # Fetch the user from the database
    user = User.find user_id

    # Add some logging context for future logs
    Log.context.set user_id: user.id, customer_id: user.customer_id

    # Set the user in user storage.
    @user_storage.user = user
  end
end

# Register the controller itself as a service,
# NOTE: Controller services must be declared as public.
@[ADI::Register(public: true)]
class UserController < ART::Controller
  # Inject our `UserStorage` object
  def initialize(@user_storage : UserStorage); end

  # The user storage service could also be injected anywhere else you need the current user.
  get "user/me", return_type: User do
    Log.info { "Returning data for #{@user_storage.user.name}" }
    @user_storage.user
  end
end

# Start the server
ART.run

# GET /user/me # => {"id":1,"customer_id":12,"name":"Fred"}
# 2020-06-16T02:25:51.593601Z   INFO - athena.routing: Matched route /user/me -- uri: "/user/me", method: "GET", path_params: {}, query_params: {} -- user_id: 1, customer_id: 12
# 2020-06-16T02:25:51.593677Z   INFO - Returning data for Fred -- user_id: 1, customer_id: 12
```

Enter fullscreen mode Exit fullscreen mode

### [](#why-it-matters)Why It Matters

Notice that since we set some `Log` context with our `SecurityListener`, all logs after that point, within the same fiber, will include that data. Also, since our `SecurityListener` has a priority of `30`, it runs _before_ Athena's routing logic which has a priority of `25`. This is beneficial since it means we don't even have to invoke the router if the request is unauthorized.

Similarly to how `Log::Context` is fiber specific, the DI container is also fiber specific, or in other words unique per request. The benefit of this is it allows sharing arbitrary data between your services, without having to worry about resetting when the request is finished. Notice that the `User` object set on `UserStorage` within `SecurityListener`, is the same one provided to our `UserController`. Since the DI container handles instantiating and providing objects to our services, we can easily provide references to the same object instance in multiple services without needing to manually pass it through as part of the public API.

The most common way frameworks handle the "current\_user" is by reopening `HTTP::Server::Context` and adding it there, which works fine most of the time. But what happens when you want to access the current user somewhere that isn't a controller action or an `HTTP::Handler`? Having something that is able to be easily accessed anywhere it is needed is much more flexible.

The `UserStorage` class could also be expanded into say, `TokenStorage` which would store the token, which would have a `user` method; to handle the logic of resolving a `User` object from the token/data in the token. There could also be different implementations of the `Token` class, such as `AnonymousToken` if there is not currently a logged in user. Overall, this approach is just much more flexible than being tied to the request context to access common data, like the current user.

### [](#alternate-solutions)Alternate Solutions

*   Define the `current_user` as a class variable.
    *   This effectively makes the system not fiber safe and unable to handle more than 1 request at a time.
*   Store a reference within the database.
    *   This would solve the problem of being able to access the user anywhere, but is less than ideal. If a system is handling many requests, that would equate to a lot of extra unnecessary DB queries.
*   Store the user within the `HTTP::Request` object
    *   This is a viable solution assuming you don't need to access said user anywhere outside of the request context. If for example you wanted to include some user data within an asynchronous message context; how would you provide the user object? In sort there wouldn't be a clean way to do it without making it part of the public enqueuing API.

## [](#conclusion)Conclusion

As shown, DI can make your Crystal application less dependent on concrete classes and more dependent on abstractions. This prevents tight coupling, makes testing easier, and encourages code reuse. However, this does not mean DI is the best pattern to use 100% of the time. Being aware of its capabilities and being able to apply the pattern to a well suited problem is the key.

If anyone has any other alternate solutions (both good and bad), feel free to share them in the comments. I would be quite interested in seeing how people, those mainly coming from a Ruby background, would solve some of these scenarios.

As usual feel free to join me in the Athena [Gitter](https://gitter.im/athena-frameworkcr/community) channel if you have any suggestions, questions, or ideas. I'm also available on Discord (`Blacksmoke16#0016`) or via [Email](https://mailto:george@dietrich.app/).
