---
url: "https://dev.to/logicmason/elixir-structs-are-maps-with-checks-and-default-values-135m"
captured_at: "2026-11-16T19:21:43+00:00"
title: "Elixir Structs are maps with checks and default values"
domain: "dev-to"
---

After our crash course, [Elixir maps made effortless](https://alchemist.camp/articles/how-to-update-elixir-maps), the next logical building block is structs.

## [](#what-are-elixir-structs)What are Elixir Structs?

As explained in the official docs, _Structs are extensions built on top of maps that provide compile-time checks and default values_. Maps, as we covered, are one of Elixir's basic data structures. They're the primary way we store key-value pairs:  

```
> users = %{
  "sam" => %{age: 22},
  "pat" => %{age: 58}
}

> user1 = Map.get(users, "sam")
%{age: 22}

> Map.get(user1, :age)
22

# Or in one step...
> get_in(users, ["pat", :age])
58
```

Aside from getting values from maps via standard library functions like `Map.get/3` or `Kernel.get_in/2`, there are also two built-in syntaxes:

*   The dot syntax, which throws errors on missing keys

```
> user1.weight
** (KeyError) key :weight not found in: %{age: 22}
```

*   The \[\] syntax, which is forgiving:

```
> users[:nobody]
nil
```

Note that the dot syntax assumes keys are atoms and if keys are Strings as above, only the bracket syntax can be used. For more on working with maps, see: [Elixir maps made effortless](https://alchemist.camp/articles/how-to-update-elixir-maps)

## [](#structs-are-built-on-top-of-maps)Structs are built on top of maps

Let's try pasting a simple module with a `defstruct` into iex and then poking around at it:  

```
defmodule User do
  defstruct age: :nil, name: "anonymous"
end

> user1 = %User{age: 32}
%User{age: 32, name: "anonymous"}

> user2 = %User{}
%User{age: nil, name: "anonymous"}
```

Using a struct makes it possible to define default values. It also lets us be confident that any `User` we create will at least have the two keys of `age` and `name`. It also makes it possible for us to match various kinds of structs in a case statement, like this:  

```
case user1 do
  %User{} -> IO.puts("This is a user")
  %Admin{} -> IO.puts("This is an admin")
  _ -> IO.puts("I don't know what this is")
end
```

This will do a **compile-time** check to ensure both the structs are defined and then it will check the hidden `__struct__` key of `user1` to see which kind of struct it is. If the `Admin` struct isn't defined, then you'll see this:  

```
Admin.__struct__/0 is undefined, cannot expand struct Admin
```

## [](#enforcing-keys)Enforcing keys

We can go a step further. By using `@enforce_keys` at the top of a struct module, we can enforce that a specific set of keys are used when creating a struct  

```
defmodule User do
  @enforce_keys [:age, :name]
  defstruct age: :nil, name: "anonymous", favorite_color: "purple"
end
```

Then, we'll see the following in iex:  

```
> bob = %User{}
(ArgumentError) the following keys must also be given when building struct User: [:age, :name]
> bob = %User{name: "Bob", age: 48, favorite_food: "steak"}
** (KeyError) key :favorite_food not found
> bob = %User{name: "Bob", age: "48"}
%User{age: 48, favorite_color: "purple", name: "Bob"}
```

Now, users **must** have names and ages, but favorite colors are optional. Any other key is invalid. Again, this is enforced at compile-time, so it is possible to patch together a struct that violates the specified behavior by directly setting the `__struct__` field rather than using the `%User{}` syntax. This isn't a good idea to abuse, but it can be useful in some situations when building libraries.

Here's how we could create a "user" who's missing a required key _and_ includes a key that isn't part of the %User{} struct:  

```
> evil_bob = %{__struct__: User, name: "Bob", favorite_food: "steak"}
> case evil_bob do  
>   %User{} -> IO.puts("This is a user")
>   _ -> IO.puts("This isn't a user")
> end
This is a user
:ok
```

😱

## [](#a-handson-example)A hands-on example

If you want to dig into a simple, plain Elixir project using Structs, take a look at the [Tic-tac-toe game board](https://alchemist.camp/episodes/tictac-game-board) screencast!

_Request a free email-based Elixir course from [Alchemist.Camp](https://alchemist967856.typeform.com/to/FA0SUF)_
