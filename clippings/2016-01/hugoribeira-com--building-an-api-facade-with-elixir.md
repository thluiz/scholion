---
url: "http://hugoribeira.com/Building-An-API-Facade-With-Elixir/"
captured_at: "2016-01-08T08:42:56-03:00"
title: "Building an API Facade with Elixir – Eidge's Blog – Full-time geek with a crush on full-stack dev and biz. Paragliding pilot."
domain: "hugoribeira-com"
---

# Building an API Facade with Elixir

Coming from Ruby and growing a bit tired of resorting to caching every time things get a bit more complicated than a simple CRUD application, I’ve been meaning to try [Elixir](http://elixir-lang.org/) and its web framework [Phoenix](http://www.phoenixframework.org/) for a while.

[Elixir](http://elixir-lang.org/) is the new cool kid in the block. It’s built on top of the Erlang and uses most of its concurrency and failure handling models.

Needless to say, it’s blazingly fast!

### Building API’s with phoenix

With the market revolving more and more around smartphone and multi-client applications, I’ve been writing API based applications for a while now.

Building an API with Phoenix is quite straightforward and, if you came from
Rails, you'll find many of the same concepts and ideas with a fresh touch of
functional programming on top of it.

This post will cover the serialization of your objects into beautifully crafted
JSON (or any other protocol if that matters).

Phoenix has the concept of [views](http://www.phoenixframework.org/docs/views) whose responsibility is to expose variables and methods to be used when rendering templates.

```
defmodule HelloPhoenix.UserView 
   HelloPhoenix.Web :view

   render"index.json" users users 
    users   ->
```

While this works fine for HTML templates, it felt awkward for serializing
objects into JSON. I felt like I shouldn't worry about mapping over an array of
objects, or wrapping the response with a root key every time I wrote a new
serializer. Also, reusing these views for including nested objects wasn't easy either.

That being said, I ended up writing a small library to deal with this.

### Building an API Facade Library

When writing Ruby, I usually resort to either ActiveModel Serializers or Grape Entities, but this time around I wanted a simpler, more lightweight approach to go with the functional style Elixir has to offer.

I started by defining the way I wanted to write my serializers knowing that I wanted them to be format agnostic (they shouldn’t really care whether we’re rendering JSON or XML) and that a single method should handle both a single resource or a list of resources.

Writing and using a serializer should look like something like this:

```
defmodule HelloPhoenix.UserSerializer 
  alias HelloPhoenix.User

     
   root_plural  users

   resources
    # rendering logic
  

   serialize 
         
  

    
    #{user.first_name} #{user.last_name}”
  

     first_name  last_name Ribeira
 UserSerializer
client     Ribeira
 UserSer ializer 
clients     Ribeira     Ribeira
```

Once defined the interface, I went on with the implementation:

```
defmodule HelloPhoenix.UserSerializer 
  # (...)
     is_list 
     
       |>   -> serialize  
       |> Serializerwrap_with_root__MODULE__
  
    
    Serializerwrap_with_root serialize __MODULE__
  

   wrap_with_root serializer  is_list  # when non empty list
    (%{}, UserSerializerroot_plural 
  
   wrap_with_root serializer  # when single item
    (%{}, UserSerializer 
  

  # (...)
```

Elixir really shines here. Pattern matching and guard clauses give you some type
safety at compile time and avoid gigantic if clauses (that will be evaluated at
runtime) and the functional style provides a simple and idiomatic way to describe
the serialization process as a pipeline of transformations from your model to
the final API response.

We've got our implementation and the interface we defined is respected, but we
still have the problem of repeating common logic across our serializers. Gladly,
Elixir let's us DRY up our implementation quite easily.

The first step is to remove this duplicated logic into its own module.

```
defmodule HelloPhoenix.Serializer 
    serializer  is_list 
    
      |>   -> serializerserialize  
      |> wrap_with_rootserializer
  
    serializer 
    wrap_with_root serializerserialize serializer
  

   wrap_with_root serializer  is_list 
    (%{}, serializerroot_plural 
  
   wrap_with_root serializer 
    (%{}, serializer 
  

defmodule HelloPhoenix.UserSerializer 
     'user'
   root_plural  'users'

   serialize 
         
  

    
    #{user.first_name} #{user.last_name}”
  

 Serializer  first_name "Jonh" UserSerializer
    "Jonh"
```

That's better!

We decoupled the logic responsible for root wrapping and mapping from the
serialization logic itself but we ended up changing the interface to support
this refactor.

Hmmm, that's not nice!

Glady, Elixir has got us covered its powerful macro system that let's us inject functionality from a
module into another. Next we'll use these macros to refactor our serializer,
maintaining logic decoupled and our interface as described initially.

```
defmodule HelloPheonix.Serializer 
  defmacro __using__ 
    quote  # inject this code when :use macro is used inside a module
      @behaviour HelloPheonix.Serializer

      alias HelloPheonix.Serializer

         is_list 
        
          |>   -> serialize  
          |> Serializerwrap_with_root__MODULE__ # Pass extended module to :wrap_with_root
      

        
        Serializerwrap_with_root serialize __MODULE__
      
    
  

  @callback Struct  Struct
  @callback serializeStruct  Struct
  @callback   String
  @callback root_plural  String

   wrap_with_root serializer  is_list 
    (%{}, serializerroot_plural 
  
   wrap_with_root serializer 
    (%{}, serializer 
  

defmodule HelloPhoenix.UserSerializer 
   HelloPhoenix.Serializer # Import functionality from Serializer

     'user'
   root_plural  'users'

   serialize 
         
  

    
    #{user.first_name} #{user.last_name}”
  

 UserSerializer  first_name "Jonh"
    "Jonh"
```

The @behaviour and @callback macros are elixir's ways of defining an interface.

Elixir is dynamically typed, meaning that explicit interfaces are not needed
but defining them allows the compiler to assert at compile time that our serializers
abide the serialization contract. This avoids weird bugs caused by unexpected return
types or necessary but undefined methods.

### Wrapping Up

I must say I'm quite impressed with Elixir. Not only it is great to see your
endpoints return in microseconds rather then hundreds of milliseconds, as the functional
paradigm seems to fit perfectly around the data transformation and request life
cycle we work with when developing web applications.

When working with dynamic languages I sometimes miss the ability to explicitly
define interfaces, as implicit interfaces do come at the cost of needing more
documentation and/or extra runtime checks. Elixir really shines here, as besides
supporting implicit interfaces, the mix between pattern matching and explicit
interface definition allows for type safety when needed without too much runtime overhead.

Elixir is really fun and I'll probably end up writing a few more posts about it,
if you enjoyed this, do consider following me on twitter [@eidgeare](https://twitter.com/eidgeare)!
