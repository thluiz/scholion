---
url: "https://dev.to/hint/macro-see-macro-do-2985"
captured_at: "2026-11-16T01:42:59+00:00"
title: "Macro See, Macro Do"
domain: "dev-to"
---

_Originally posted on [Hint's blog](https://hint.io/blog/elixir-demystifying-quote)._

_This post assumes you have Erlang/Elixir installed and that you can spin up a Phoenix project._

I've been diving into Elixir and Phoenix as of late. I have thoroughly enjoyed my time spent with both and could gush about them for far, far too long. Elixir has some features whose underlying implementation wasn't obvious at first glance, namely the macro `quote/2` (that slash and number indicates the arity).

I first came across `quote/2` in a fresh Phoenix project. Let's create one now! Run `mix phx.new foo`, open up `lib/foo_web/foo_web.ex` and see `quote/2` being used:  

```
# lib/foo_web/foo_web.ex

defmodule FooWeb do
  def controller do
    quote do
      use Phoenix.Controller, namespace: FooWeb

      import Plug.Conn
      import FooWeb.Gettext
      alias FooWeb.Router.Helpers, as: Routes
    end
  end

  # ...
end
```

`controller/0` is then used in controllers like this:  

```
# lib/foo_web/controllers/page_controller.ex

defmodule FooWeb.PageController do
  use FooWeb, :controller

  # ...
end
```

Going through [Programming Phoenix](https://pragprog.com/book/phoenix14/programming-phoenix-1-4) I saw this macro being used again and again. I understood what it _meant_: the `use`, `import`, and `alias` macros are being injected into `PageController`, so dependencies can be shared across modules. But why not just include them in the function definition? What is going behind the scenes? Why `quote/2`? Being a Rails developer accustomed to magic, I accepted it and moved on.

One of Phoenix's (and Elixir) strengths is that nothing is hidden from the developer. Everything is gloriously defined, displayed, and explicitly composed right in front of you. There really _isn't_ any magic. Thus my acceptance of it bothered me, so let's dive in and learn about `quote` together!

## [](#copy-and-almost-paste)Copy and (almost) paste

The best way to learn is by doing, so why don't we create some modules and reproduce what we've seen. Here's a very simple example I came up with:  

```
# bar.exs

defmodule Bar.Math do
  def sum(x, y), do: x + y
end

defmodule Bar.AllTheThings do
  def things do
    quote do
      alias Bar.Math
    end
  end
end

defmodule Bar.Work do
  use Bar.AllTheThings, :things

  def print_sum(x, y) do
    IO.puts("the sum of #{x} and #{y} is #{sum(x, y)}")
  end
end

Bar.Work.print_sum(2, 2)
```

Again, I don't _really_ know what `quote/2` is doing and why, but we mimicked what we saw in Phoenix pretty close. I think we're ready to try this out, let's run `elixir bar.exs` and see what happens:  

```
> elixir bar.exs
** (UndefinedFunctionError) function Bar.AllTheThings.__using__/1 is undefined or private
    Bar.AllTheThings.__using__(:things)
    bar.exs:18: (module)
    bar.exs:17: (file)
```

🤔

It seems that we're missing a function that Elixir assumes we have implemented. I'll be honest - I've never written a module that was consumed by `use`, so let's double back to `FooWeb` in our Phoenix App to see if we missed anything. At the bottom of the file, you'll see:  

```
  defmacro __using__(which) when is_atom(which) do
    apply(__MODULE__, which, [])
  end
```

Ah! Elixir was looking for that function, so let's slap that it in `Bar.AllTheThings`:  

```
defmodule Bar.AllTheThings do
  def things do
    quote do
      alias Bar.Math
    end
  end

  defmacro __using__(which) when is_atom(which) do
    apply(__MODULE__, which, [])
  end
end
```

Diving into `defmacro` is outside the scope of this post, but we can acknowledge it as a requirement of a module that's consumed by `use`. The use of `apply/3` is straightforward: take a module, an atom that represents the function name, and call it with some arguments.  

```
apply(Bar.AllTheThings, :things, [])
# is equivalent to
Bar.AllTheThings.things([])
```

And then:  

```
> elixir bar.exs
the sum of 2 and 2 is 4
```

Great, our dependency injection works. Now that we understand the structure let's dig into what's happening under the hood.

## [](#i-heard-you-like-elixir-so-lets-represent-some-elixir-with-elixir)I heard you like Elixir, so let's represent some Elixir with Elixir

From the [docs](https://hexdocs.pm/elixir/Kernel.SpecialForms.html#quote/2):  

```
> quote(opts, block)

Gets the representation of any expression.
```

Let's try it out:  

```
> iex
iex(1)> quote do sum(2, 2) end
{:sum, [], [2, 2]}
```

That's right! We are representing Elixir with Elixir. Elixir's AST ([abstract syntax tree](https://en.wikipedia.org/wiki/Abstract_syntax_tree)) is... Elixir! Pretty cool, huh? Macros, such as `quote/2`, are represented by a tuple of three elements. The first element is (usually) an atom, the second is for metadata, and the third is the argument list.

I wonder what our `import Bar.Math` looks like as an AST? Let's find out! Comment out everything in `bar.exs` except for the `Bar.Math` module. Rename the file to `bar.ex` so Elixir can compile it, and run `iex`:  

```
> iex
iex(1)> c "bar.ex"
[Bar.Math]
iex(2)> quote do
...(2)>   import Bar.Math
...(2)> end
{:import, [context: Elixir], [{:__aliases__, [alias: false], [:Bar, :Math]}]}
```

There it is! We can see the AST as a three element tuple. It holds all the information that Elixir needs to know to `import` a module. `quote/2` gives us some fantastic syntax sugar; could you imagine writing these tuples everywhere? Just for fun, let's see how deep into the rabbit hole we can go. Rename `bar.ex` back to `bar.exs`, uncomment all the code, and change the `import Bar.Math` to the AST representation without `quote/2`:  

```
# bar.exs

# ...
defmodule Bar.AllTheThings do
  def things do
    {:import, [context: Elixir], [{:__aliases__, [alias: false], [:Bar, :Math]}]}
  end

  defmacro __using__(which) when is_atom(which) do
    apply(__MODULE__, which, [])
  end
end
# ...
```

And:  

```
> elixir bar.exs
the sum of 2 and 2 is 4
```

It works! Let's go another level in by removing `things/0` and placing our AST directly in `__using/1`:  

```
# bar.exs

# ...
defmodule Bar.AllTheThings do
  defmacro __using__(which) when is_atom(which) do
    {:import, [context: Elixir], [{:__aliases__, [alias: false], [:Bar, :Math]}]}
  end
end
# ...
```

You know the drill:  

```
> elixir bar.exs
the sum of 2 and 2 is 4
```

Nice! Is it possible to inline the AST we have _in_ our `Bar.Work` module? Sadly, we can't. The `use/2` macro changes this:  

```
use Bar.AllTheThings, :things
```

to:  

```
Bar.AllTheThings.__using__(:things)
```

We've come to the end of this Elixir in Elixir train! There are no other stops on this line.

### [](#wrapping-up)Wrapping up

So, what did we learn? The `quote` macro transforms Elixir code to an AST. We can then leverage that to achieve real dependency injection in a functional language. How cool is that?
