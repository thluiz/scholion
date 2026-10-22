---
url: "https://yiming.dev/blog/2021/07/18/stop-using-behaviour-to-define-interfaces-use-protocol/"
captured_at: "2021-07-22T14:48:07-03:00"
title: "Stop using Behaviour to define interfaces, use Protocol! - Yiming Chen"
domain: "yiming-dev"
---

# Stop using Behaviour to define interfaces, use Protocol!

I think Elixir developers (me included) often misuse Behaviour to define common interfaces.

For example, let's say we have a `Weather` interface:

```
defmodule Weatherdo@callback temperature(Location.t())::{:ok,Temperature.t()}end

defmodule Weather.SourceAdo@behaviourWeather@implWeatherdef temperature(location),do:...endMox.defmock(Weather.Mock,for:Weather)
```

Then we need to inject a `module` into the caller function in order to achieve polymorphism:

```
def controller(weather_mod)do
  location =...
  temp = weather_mod.temperature(location)...end
```

## Something is off

This is a valid use case for Behaviour, but I always feel something is off here:

1. The name `behaviour` / `callback` confused me a lot when I first learned about this design pattern in Elixir.  
   Coming from a Object-Oriented background, what I want is just `interface` and `implementation`.  
   > I can understand `behaviour` as a different way of saying `interface`.  
   > But what's this `callback` non-sense?
2. We need to pass the module around as variables in our application code.  
   This adds more difficulties to tools like `mix xref` to analyze our code.
3. The mocks defined by `Mox` are basically modules that have some global state.  
   Which means that:
   1. We need to use `global` mock sometimes, or spend some efforts to allow a child process to use the `private` mock.
   2. We can't have 2 mocks with different `expect`-s or `stub`-s for the same Beahviour.  
      For example, to test the following `chain/2` function, we may need to call `Mox.defmock` twice, which is so weird that I guess no body would actually do it.

      ```
      defmodule Weather.Chainabledodef chain(source1, source2)do
          fn location ->with{:ok, temp}<- source1.temperature(location)do{:ok, temp}else{:error, _}->
                source2.temperature(location)endendendendMox.defmock(Weather.Mock1,for:Weather)Mox.defmock(Weather.Mock2,for:Weather)
      ```
4. A common pattern is to delegate function calls from behaviour module to callback modules:

   ```
   defmodule Weatherdo@callback temperature(Location.t())::{:ok,Temperature.t()}@weather_modApplication.get_env(:my_app,:weather_mod)

     defdelegate temperature(location), to:@weather_modend
   ```

   And this pattern is so common that we have a library for it:  
   <https://github.com/sascha-wolf/knigge>

Actually, I'm not the only one who feels this oddness:

> This use is almost entirely the inverse of how I usually see behaviors being used in Elixir.  
>   
> Here, they tend to define a public interface, and are often used to separate out pure code from impure code: by defining an interface for a client to a third-party system, for example.
>
> — Quinn Wilton (@wilton\_quinn) [June 24, 2021](https://twitter.com/wilton_quinn/status/1408191089316560898?ref_src=twsrc%5Etfw)

## Pure interfaces (Protocol) vs. Impure interfaces (Behaviour)

Inspired by the thread above, I think I've found the reason why defining common interfaces via Behaviour feels off to me:  
Because the whole Behaviour mechanism from Erlang/OTP was designed to define **impure** interfaces, rather than **pure** interfaces.

Pure interfaces
:   Pure interface function don't have any logic inside it.  
    All it does is to dispatch the function call to an implementation module.  
    Like the `Inspect.inspect/2` protocol function.

Impure interfaces
:   Impure interface function not only dispatches the function call, but also adds more features upon this function call.

    The best example would be `GenServer`:  
    First of all, `GenServer` is an interface for sure.  
    We can think of callbacks like `handle_info`, `handle_call`, `handle_cast` as common interfaces,  
    i.e. all the callback modules need to implement these interfaces.  
    And `GenServer` would do all the dynamic dispatching for us.

    But are we using `GenServer` just for polymorphism?  
    I guess every Elixir/Erlang developer would answer "NO".  
    The real power of `GenServer` is complex async logic encapsulated inside `GenServer.call`, `GenServer.cast`, etc..  
    Because these logic are so common, they get extracted as shared functions like `GenServer.call`.  
    Every callback module we write leverages these common logic.  
    So that we don't need to care how to handle the async mess, and can just write our business logic in a procedural way.

    Note here "impure" is just a neutral adjective.  
    (I really hope I could've found a better adjective-pair than pure/impure.)  
    I don't mean that impure interfaces are worse than pure interfaces.  
    (As impure functions are not worse or better than pure functions.)  
    From the `GenServer` example, I even believe that impure interfaces are way better than pure interfaces.  
    Because every time we define a callback module, we are reusing the logic encapsulated in impure interfaces.  
    This means that every line of code we add to the impure interface would be extremely cost-effective, because the effect of that code is amplified by the number of callback modules we have.

So I believe that defining common interface with Behaviour is just scratching the surface of the power of Behaviour.  
We are misusing a powerful design pattern for defining impure interfaces, and we just use it to define pure interfaces.  
What we really should do is to **extract as many common logic to the behaviour module**, in a way that the callback modules can be deadly simple.  
(Based on this argument, `defdelegate` from a behaviour module to a callback module is definitely an anti-pattern.)

Finally, if you really need to define a common interface, then I believe the right way to do it in Elixir is `Protocol`.  
As it was explained in the [official doc](https://hexdocs.pm/elixir/Protocol.html):

> A protocol specifies an API that should be defined by its implementations.

Then you may find [Promox](https://github.com/dsdshcym/promox) useful as it helps you define mocks for Protocols easily in your tests :).

## Objext: From Protocol to Behaviour

Now you may notice a gap between Protocol and Behaviour:  
What if I start with a Protocol that defines an interface, but then I want to extract more common logic to the interface functions, to make them more powerful like `GenServer.call`?

The most common solution in Elixir is to define another module (`Enum`) besides the Protocol module (`Enumerable`).  
But I find it hard to name the Protocol module already, not to say I need to name 2 modules.  
(Naming is hard in software development, right?)[1](https://yiming.dev/blog/2021/07/18/stop-using-behaviour-to-define-interfaces-use-protocol/#fn.1)

Besides the difficulty of naming 2 modules, I still believe a separate module should be unnecessary.  
To me, Protocol and Behaviour are both ways to define interfaces.  
The only difference is the amount of common logic at the interface level:

- Protocol has no common logic, it's just pure interfaces
- Behaviour has a ton of common logic, we should be able to grow pure interfaces into this kind of complex interfaces.

Given this reason, I made [Objext](https://github.com/dsdshcym/objext), which allows you to define interfaces in Elixir easily.  
(plus some other goodies like fully-encapsulated data structure and Promox-like mock features.)

## Takeaways

If anything you can take away from this blog post, I hope is this:  
**be aware of what kind of interface you are going to define**,

1. use Protocol for pure interfaces
2. use Behaviour for impure interfaces
3. grow pure interfaces to impure interfaces when possible

These tips can be achieved with Protocol and Behaviour with some dedicated discipline.  
If you find that cumbersome, you may find [Promox](https://github.com/dsdshcym/promox) and [Objext](https://github.com/dsdshcym/objext) to be useful.  
Please give them try and let me know how they compare to Mox and Protocol.

## Footnotes:

[1](https://yiming.dev/blog/2021/07/18/stop-using-behaviour-to-define-interfaces-use-protocol/#fnr.1)

If you are also like me, who's bad at naming things but still wants to use Protocol.  
You can use `Kernel.def` inside your `Protocol` definition,  
so you can define a normal function instead of a callback function:

```
defprotocol EnumerabledoKernel.def map(enumerable, map_fn)do
    reduce(enumerable,[],&(&2++[map_fn.(&1)]))enddef reduce(enumerable, acc, fun)end
```
