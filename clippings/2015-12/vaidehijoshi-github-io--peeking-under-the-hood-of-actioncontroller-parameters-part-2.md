---
url: "http://vaidehijoshi.github.io/blog/2015/11/24/peeking-under-the-hood-of-actioncontroller-parameters-part-2"
captured_at: "2015-12-23T15:03:31-03:00"
title: "Peeking Under the Hood of ActionController Parameters, Part 2 - Words and Code"
domain: "vaidehijoshi-github-io"
---

# Peeking Under the Hood of ActionController Parameters, Part 2

[#technicaltuesdays](http://vaidehijoshi.github.io/blog/categories/number-technicaltuesdays/), [computer science](http://vaidehijoshi.github.io/blog/categories/computer-science/), [rails](http://vaidehijoshi.github.io/blog/categories/rails/), [ruby](http://vaidehijoshi.github.io/blog/categories/ruby/)

*This blog post is part of a series on strong parameters. Read Part 1 [here](http://vaidehijoshi.github.io/blog/2015/11/17/peeking-under-the-hood-of-actioncontroller-parameters-part-1/).*

Rails often feels like a black box, with all of the complex logic abstracted away and hidden from view. This leaves behind a clean, convention-abiding framework where form follows function. But another, perhaps less-intentional side effect of all the “metaprogramming away” of this framework’s complexities is a frequent lack on clarity of what’s going on behind the scenes.

In my year of working with Rails, I’ve come to appreciate and respect so many things about it. In fact, I think that there’s something incredibly approachable about Ruby as one’s first programming language, with Rails as its corresponding framework. And of course, there’s something truly unique and welcoming about the Ruby and Rails programming community. All of these factors combined make it so easy for beginners of such different backgrounds to start building applications very quickly.

However, once you get past the intial stage of building applications with the basic CRUD operations, or if you’re trying to build something a bit more complex with added functionality, or trying to integrate with another framework, you eventually hit a wall where you realize that that you’re not completely sure how something works. This can be a hard wall to climb over, especially given the fact that you can start building things very quickly with Rails. Some people have heavily critiqued this aspect of the framework, arguing that it’s detrimential to abstract away so much of what’s *actually* going on, which makes it difficult for people to understand what their code is truly doing under the hood. I’ve peronally encountered this “wall of abstraction” a few different times, but each time I found some piece of logic that worked differently than I thought it would, it only lead me to learn something new about the framework. Most recently, that lead me down a wild goose chase into the source code for `ActionController::Parameters` — a class that I didn’t even know existed!

## Quack Like A Hash

![6a00d8341d3df553ef01053719d13a970b-pi.jpg](vaidehijoshi-github-io--peeking-under-the-hood-of-actioncontroller-parameters-part-2/c60d8aee8264fb52db1cc922606e43c3.jpg)

There’s a well-known saying that Rubyists often attribute to duck typing: *if it looks like a duck, and quacks like a duck, it probably is a duck.* In other words, if an object behaves like another object, it doesn’t matter that it’s of a certain class or “type” (or species!) of another object, just so long as it can respond to the correct method calls to implement the behavior of that object.

This saying actually comes from a concept referred to as the “duck test”, which is a form of abductive reasoning, which is based on the idea that one can identify an unknown object by observing its habitual characteristics. However, this can be a little bit tricky because *sometimes*, just because something quacks like a duck and waddles like a duck doesn’t mean that we should stop questioning what it actually is and just assume that it’s a duck!

Let me explain with an example. Whenever we send or receive data from the server, it appears that everything is being sent as a `Hash`. If we look at our `GET` requests or `POST` and `PUT` requests using HTTP protocol, our data usually looks like some variation on a theme of something like the following:

|  |  |
| --- | --- |
|  | ```  order       total        number 'ABC123' ``` |

If it acts like a hash, and quacks like a hash, it must be a hash, right? Well, not exactly. Last week we learned that `params` in our controllers are actually instances of `ActionController::Parameters`. But this data that we’re sending back and forth still looks like its a plain old Ruby `Hash`. It also seems to behave like a hash, right? We can do something like this

|  |  |
| --- | --- |
|  | ```  params:orderpresent?   @ordercreateorder_params ``` |

and access a key in this so-called “hash” the same way we would with any other `Hash` data structure. So, what’s different about `ActionController::Parameters`?

Well, let’s find out. We’ll start by opening up [the source code](https://github.com/rails/rails/blob/9ab2d030209d9608a6c866d83210f5b3b7d2319e/actionpack/lib/action_controller/metal/strong_parameters.rb#L108) for this class, which lives inside of the `ActionController` module. The first thing we’ll notice is this:

|  |  |
| --- | --- |
|  | ``` module ActionController   class Parameters  ActiveSupportHashWithIndifferentAccess ``` |

Interesting! The `Parameters` class subclasses from `ActiveSupport::HashWithIndifferentAccess`. If we were really curious about what type of object *this* class inherits from, we could trace that back to see that `HashWithIndifferentAccess` simply [inherits from](https://github.com/rails/rails/blob/df6048407faefdc6774a8b5a02344fd4b1a734b1/activesupport/lib/active_support/hash_with_indifferent_access.rb#L43) the class `Hash`. So, what makes `HashWithIndifferentAccess` different from plain old Ruby hashes?

Well, the [Rails guides](http://api.rubyonrails.org/classes/ActiveSupport/HashWithIndifferentAccess.html) answers this question pretty well:

> `HashWithIndifferentAccess` implements a hash where keys `:foo` and `"foo"` are considered to be the same. Internally symbols are mapped to strings when used as keys in the entire writing interface. You are guaranteed that the key is returned as a string. This class is intended for use cases where strings or symbols are the expected keys and it is convenient to understand both as the same. For example the `params` hash in Ruby on Rails.

Awesome, this answers our question and more! This subclass gives us the flexibility to access the keys in a `params` “hash” by either a string or a symbol. The `HashWithIndifferentAccess` class still responds to the majority of the same methods that a Ruby `Hash` instance does, but with some added functionality, which can be especially handy if we’re dealing with JSON responses.

*Protip:* we can easily create `HashWithIndifferentAccess` instances by creating a Ruby `Hash` instance and calling `with_indifferent_access` on it. This method is available to us since core extensions has the `with_indifferent_access` method defined on the `Hash` class by default:

|  |  |
| --- | --- |
|  | ```  rails  Loading development environment Rails        'hello' with_indifferent_access => => =>"hello"  class => ActiveSupportHashWithIndifferentAccess ``` |

So, parameters aren’t quite a hash, but they quack pretty much exactly like how a hash would quack. But there must be a good reason why they are different classes, right? Let’s investigate further.

## Waddle Like A Param

On a very basic level, `ActionController::Parameters` could be simplified to hashes with some serious restrictions and permissions. Because `ActionController::Parameters` inherits from `ActiveSupport::HashWithIndifferentAccess`, we can fetch values from our params “hash” using a symbol `:key` or a string `"key"`. But there are a few things that we can’t do so easily, and that’s where the functionality of `ActionController::Parameters` really starts to come into play and begins to make a lot more sense.

We can easily create a new instance of `ActionController::Parameters`. In fact, we do it within the context of our controllers all the time!

|  |  |
| --- | --- |
|  | ``` permitted_params  paramsrequire:orderpermit:total permitted_params # => {"total"=>"100.00"} permitted_paramsclass # => ActionController::Parameters ``` |

Except usually we wrap it in a `_params` suffixed method like this:

|  |  |
| --- | --- |
|  | ```  order_params   paramsrequire:orderpermit:total ``` |

Here is one example of the added functionality of this class. When we create a new instance of a `ActionController::Parameters` class, it is by default, not permitted.

|  |  |
| --- | --- |
|  | ``` params  ActionControllerParameters paramspermitted? # => false ``` |

The `permitted?` method actually doesn’t do anything more than return an attribute on an instance of a `ActionController::Parameters` object, called `@permitted`:

|  |  |
| --- | --- |
|  | ```  permitted?   @permitted ``` |

So the question is, where does this attribute get set? Well, there are two places that can set this attribute to `true`. The first place is a method that we’re already familiar with: the `permit` method! As we learned last week, this method calls `params.permit!` as its last line, after it filters out any paramters that aren’t permitted scalar values (think `Symbol`, `String`, or `Hash`). However, we can also just call `permit!` on an instance of `ActionController::Parameters` ourselves.

|  |  |
| --- | --- |
|  | ``` params  ActionControllerParameters paramspermitted? # => false paramspermit! paramspermitted? # => true ``` |

The `permit!` method sets the `@permitted` attribute to `true`, and returns `self`, which in this case is just the instance of the params class. This method [is quite useful](https://github.com/rails/rails/blob/9ab2d030209d9608a6c866d83210f5b3b7d2319e/actionpack/lib/action_controller/metal/strong_parameters.rb#L223) for mass assignment, since it effectively removes the need to list all the permitted values. It can be handy in a controller that is used only by admins that should have control over — and can be trusted with — updating all attributes of an object:

|  |  |
| --- | --- |
|  | ``` # def blog_params   # params.require(:blog).permit(:title,        # :author, :published_at, :tags,        # :excerpt, :image, :image_caption, :external_url)  blog_params   paramsrequire:blogpermit! ``` |

However, this doesn’t really make sense to use unless you are *sure* that you want to allow all the values to the params hash to be whitelisted. Proceed with caution!

## Heavy Metal Controllers

Now that we know a little bit more about `ActionController::Parameters` and what kinds of ducks — oops, I mean *objects* — they really are, there’s one question that we probably still have floating around in our heads: where on earth does our params come from during the request-response cycle…and *how* does it get set on a controller?

To answer this question, we must trace back how a parameter comes in from a request, and then how it is set on a controller. It isn’t magic (even though it seems like that’s the case!). In reality, it’s actually happening in a cool place called `ActionController::Metal`. Yes, that’s a thing, and it happens to be the very class that `ActionController::Base` [inherits](https://github.com/rails/rails/blob/7978ec722172b45e72ee78baefc23ab907a91131/actionpack/lib/action_controller/base.rb#L164) from. By default, we should always inherit from `ActionController::Base`, because it gives us a ton of functionality and modules that help speed things up.

But even `ActionController::Base` has to come from *somewhere*, right? And that somewhere happens to be `ActionController::Metal`, which is the simplest possible controller that we can create in Rails, which provides little more than a Rack interface. Here’s a very, *very* simplified version of what that class looks like in the Rails source code:

|  |  |
| --- | --- |
|  | ``` class Metal  AbstractController   # Very truncated from the Rails source code!   attr_internal :headers :response :request    initialize       @_headers  "Content-Type" => "text/html"       @_status         @_request         @_response         @_routes         super ``` |

As a request goes out or a response comes in, these values are set as instances on the controller itself! So if there was any doubt in your mind, everything in Ruby is an object — even controllers are just objects with instance variables and attr\_readers and attr\_accessors.

So, where do our parameters get set? Well, they also live in an instance attribute called `@_params`, which is set by a [params method](https://github.com/rails/rails/blob/2910956fc9006d3c26f56992dab630fa97b7f7bc/actionpack/lib/action_controller/metal.rb#L140). The parameters come in from a request, and are beautifully memoized in a method that looks like this:

|  |  |
| --- | --- |
|  | ```  params   @_params  requestparameters ``` |

Pretty amazing, right? That black box of `ActionController` and strong parameters doesn’t seem so intimiating any more, does it?
It’s a little strange that we always talk about and use `params.require` and the `permit` method so often in Rails, particularly when we are first starting out, but we don’t necessarily question where it comes from! Or how it is set or being used, for that matter! But now we know. And we’ll never mistake our strong params for a simple Ruby hash again.

Or a duck, for that matter.

## Rails 5 Update

I recently learned that there’s a significant change coming to `ActionController::Parameters` with the soon-to-be-released Rails 5! Namely, another Rubyist brought this to my attention over the interwebz:

It turns out that `ActionController::Parameters` will soon return an object, rather than a `Hash` instance, which also means that it will no longer Hash will no longer inherit from `ActiveSupport::HashWithIndifferentAccess` as this post explains. Check out this great [blog post](http://eileencodes.com/posts/actioncontroller-parameters-now-returns-an-object-instead-of-a-hash/) by Eileen Uchitelle, a developer at Basecamp, to learn more about how `ActionController::Parameters` will be changing with the next release of Rails.

## tl;dr?

- An instance of `ActionController::Parameters` behaves a lot like a hash that can be accessed with either symbol or string keys. This class has some added methods like `permitted?` and `permit!` which check and set the `@permitted` instance attribute on a params object.
- Curious to learn more about how strong params handles nested attributes? Check out this great [blog post](http://patshaughnessy.net/2014/6/16/a-rule-of-thumb-for-strong-parameters) by Pat Shaughnessy.
- New to `ActionController::Metal`? Head over to the Rails docs [to learn more](http://api.rubyonrails.org/classes/ActionController/Metal.html) and read this helpful [StackOverflow post](http://stackoverflow.com/a/18189580).
