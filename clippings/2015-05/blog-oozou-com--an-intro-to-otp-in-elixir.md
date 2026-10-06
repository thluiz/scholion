---
url: "http://blog.oozou.com/an-intro-to-otp-in-elixir/?utm_campaign=Elixir+Radar&utm_source=hs_email&utm_medium=email&utm_content=17534844&_hsenc=p2ANqtz--QoQiBcY8hxtHp3pvhd5ay__j4rIb7R3J5I3BXhOPojC6CerYXava_T3sLO4m9td-lPMY5Y4r-d1gKUh-V_OMdEE2f1A&_hsmi=17534844"
captured_at: "2015-05-07T13:16:51-03:00"
title: "The Oozou Blog - An intro to OTP in Elixir"
domain: "blog-oozou-com"
---

# An intro to OTP in Elixir

By - February 13, 2015

In this installment in our series of introductory Elixir blog posts we’ll convert the FizzBuzz server from [last time](http://blog.oozou.com/exploring-elixir-processes/) into an OTP app.

## What is OTP?

According to [the documentation](http://www.erlang.org/doc/), OTP — [the Open Telecom Platform](https://en.wikipedia.org/wiki/Open_Telecom_Platform) — is “a complete
development environment for concurrent programming”, containing an Erlang compiler and interpreter, a database server ([Mnesia](http://en.wikipedia.org/wiki/Mnesia)), an analysis tool ([Dyalizer](http://www.erlang.org/doc/man/dialyzer.html)), as well as a lot of libraries. This latter part is what people generally refer to when talking about OTP.

## Behaviours

One of the central [design principles of Erlang/OTP](http://www.erlang.org/doc/design_principles/des_princ.html) are application patterns, or “behaviours” in OTP lingo. They define generic implementations for common tasks, for example a generic server ([gen\_server](http://elixir-lang.org/getting_started/mix_otp/3.html)) module. The application developer adds implementation specific code into a callback module which exports a set of specific functions. Unlike Erlang, Elixir provides default implementations for these functions, so you only have to override the ones you need.

## A FizzBuzz server using GenServer

Enough theory, let’s write some code!

We use [mix](http://elixir-lang.org/docs/stable/mix/) to create a new project. Since we want the module name to be in [CamelCase](https://en.wikipedia.org/wiki/CamelCase) we have to provide the `--module` option, otherwise it would default to `Fizzbuzz`.

```
$ mix new fizzbuzz --module FizzBuzz
```

This command creates a whole application template, but for the purposes of this blog post we’ll only work on `lib/fizzbuzz.ex`.

Let’s start by letting our application know that we are implementing the `GenServer` OTP behaviour:

```
 GenServer
require Logger
```

We also required the [Logger module](http://elixir-lang.org/docs/master/logger/Logger.html), since we are using it for debugging purposes. Next we define the API for our clients.

```
 start_link 
   GenServerstart_link__MODULE__  name: __MODULE__

  
  GenServer__MODULE__ :print 

 print 
  GenServer__MODULE__ :print
```

`FizzBuzz.start_link/0` is just a wrapper around [GenServer.start\_link/3](http://elixir-lang.org/docs/stable/elixir/GenServer.html#start_link/3) which starts the server as a linked process, often as part of a [supervision tree](http://elixir-lang.org/docs/stable/elixir/Supervisor.html). Note that we start our server with the `name` option for which we use the module name (`__MODULE__`). This way other functions don’t have to refer to our server by PID.

`FizzBuzz.get/1` and `FizzBuzz.print/1` are our server’s main interface. They receive a number as an argument and return or output the corresponding FizzBuzz value. `GenServer` supports two request types: [calls](http://elixir-lang.org/docs/stable/elixir/GenServer.html#call/3) and [casts](http://elixir-lang.org/docs/stable/elixir/GenServer.html#cast/2). The former is synchronous and supposed to send something back to the client (our `get` function), whereas the latter is asynchronous and doesn’t necessarily return anything to the client (our `print` function).

It’s common to wrap the `GenServer` interface in our own client APIs, so the above pattern is worth remembering.

With that out of the way, we now go on to implement the necessary `GenServer` callbacks.

```
  Loggerdebug FizzBuzz server started"
   

 handle_call:print  _from state 
    state  fetch_or_calculate state
  :reply  state

 handle_cast:print  state 
    state  fetch_or_calculate state
   
  :noreply state
```

`init/1` gets called by `GenSever.start_link/3` and returns a tuple of the form `{:ok, state}`. In our specific case the state is a simple Elixir map (`%{}`).

`handle_call/2` and `handle_cast/2` are the core of our application. We use pattern matching on the first argument to specify that we handle messages of the form `{:print, n}`. The private function `fetch_or_calculate/2` retrieves or calculates the value, and we then return the appropriate response. In the case of a call it will have the form `{:reply, response, state}`, whereas for a cast it will be `{:noreply, state}`. These are `GenServer` conventions, the [documentation](http://elixir-lang.org/docs/stable/elixir/GenServer.html) lists all possible answer types for every request type.

This is what the private helper looks like:

```
 fetch_or_calculate state 
   has_key?state  
    Loggerdebug Fetching 
       fetchstate 
  
    Loggerdebug Calculating 
      fizzbuzz
    state  state  
  
     state
```

`fetch_or_calculate/2` checks if the FizzBuzz value for `n` has been calculated before. If it has, we fetch it from the dictionary. If the value hasn’t been computed before, we do so and update the state by adding the newly computed value to it (`Dict.put(state, n, fb)`). Finally we return a tuple of the form `{:ok, value, state}` which we pattern match against in the handler functions.

That’s it, our FizzBuzz server is now ready for action! Here’s the complete code:

```
defmodule FizzBuzz 
   GenServer
  require Logger

  ## Client API

   start_link 
     GenServerstart_link__MODULE__  name: __MODULE__
  

    
    GenServer__MODULE__ :print 
  

   print 
    GenServer__MODULE__ :print 
  

  ## Server Callbacks

    
    Loggerdebug FizzBuzz server started"
     
  

   handle_call:print  _from state 
      state  fetch_or_calculate state
    :reply  state
  

   handle_cast:print  state 
      state  fetch_or_calculate state
     
    :noreply state
  

   fetch_or_calculate state 
     has_key?state  
      Loggerdebug Fetching 
         fetchstate 
    
      Loggerdebug Calculating 
        fizzbuzz
      state  state  
    
       state
  

   fizzbuzz 
         
        -> :FizzBuzz
        -> :Fizz
        -> :Buzz
            ->
```

Time to use our code. In the project directory, fire up an `iex` session in the context of our application with the following command:

```
iex -S mix
```

Now we can start a server and compute some values:

```
FizzBuzzstart_link
 |> FizzBuzzprint
```

Here’s the output generated by that command. Due to the asynchronous nature of the requests the outout, log messages and the function’s return value are interleaved:

```
4

10:54:58.026 [debug] Calculating 4
Buzz
[:ok, :ok, :ok]

10:54:58.028 [debug] Calculating 5
Fizz
```

Note how despite running in a separate process, the output of `IO.puts` happened in our `iex` session, since that’s the current [group leaer](http://elixir-lang.org/getting-started/io-and-the-file-system.html#processes-and-group-leaders).

If we now try to fetch an already computed value (`FizzBuzz.get(5)`), we can see that it’s actually retrieved from the cache:

```
10:58:56.774 [debug] Fetching 5
:Buzz
```

## Summary

In this post we explored how easy it is to implement server applications by leveraging OTP. Our FizzBuzz server is now ready to be deployed as part of a bigger Elixir application, offering features like supervision and hot code swapping.

## Resources
