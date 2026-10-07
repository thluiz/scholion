---
url: "http://blog.plataformatec.com.br/2014/09/writing-assertive-code-with-elixir/"
captured_at: "2015-02-03T16:22:25-03:00"
title: "Writing assertive code with Elixir « Plataformatec Blog"
domain: "blog-plataformatec-com-br"
---

Functional languages are typically great languages for writing assertive code and Elixir is no exception. In this blog post, I would like to discuss some anti-patterns I have seen in Elixir code and how to rewrite them in a way to make the best of Elixir.

### Pattern matching

Imagine you have a string with format `foo=bar&token=value&bar=baz` where you want to extract the value for the key `token` which may appear anywhere or not at all in the string.

Here is one solution a developer not very-acquainted with pattern matching would try:

```
def get_token(string) do
  parts = String.split(string, "&")
  Enum.find_value(parts, fn pair ->
    key_value = String.split(pair, "=")
    Enum.at(key_value, 0) == "token" && Enum.at(key_value, 1)
  end)
end
```

At first the code seems to work fine but once we go deeper we can see it makes many assumptions we have not really planned for!

For example, what happens if someone passes `"foo=bar&token=some=value&bar=baz"` as argument? The code will work and will return the string `"some"`. But is that what we really want? Maybe we wanted `"some=value"` instead? Or maybe we wanted to reject it all together?

There are other examples where the code above would work by accident, possibly adding complexity to the codebase as other users may start to rely on such behaviour.

The most idiomatic way of writing the code above in Elixir is by using pattern matching:

```
def get_token(string) do
  parts = String.split(string, "&")
  Enum.find_value(parts, fn pair ->
    [key, value] = String.split(pair, "=")
    key == "token" && value
  end)
end
```

With pattern matching, we are asserting that `String.split/2` is going to return a list with two elements. If someone passes `"foo=bar&token&bar=baz"`, it will crash as the list will have only one element. If someone passes `"token=some=value"`, it will crash too as it contains 3 items.

Our new code does not contain any of the accidental complexity of the previous one and it will also be faster. Any input that does not match the given pattern will lead to a crash, giving us the perfect opportunity to discuss and decide how to handle those corner cases.

### Polymorphism is opt-in

Elixir provides protocols as a mechanism for polymorphism. A protocol allows developers to express they are willing to work with any data type, as long as it implements the protocols X, Y and Z.

I have previously [compared Elixir protocols to alternatives in languages like Swift and Ruby](http://blog.plataformatec.com.br/2014/06/comparing-protocols-and-extensions-in-swift-and-elixir/). One nice aspect of Elixir protocols is that they are explicit, you need to explicitly outline and define a protocol for data structures to implement.

For example, one protocol in Elixir is the `String.Chars` protocol, which converts any data type to a string, if that data type can be converted to a human-readable string. The `to_string` function uses such protocol for conversions:

```
iex> to_string("hello")
"hello"
iex> to_string(1)
"1"
iex> to_string URI.parse("http://blog.plataformatec.com.br")
"http://blog.plataformatec.com.br"
iex> to_string %{hello: :world}
** (Protocol.UndefinedError) protocol String.Chars not implemented for %{hello: :world}
```

Imagine you have a function that converts underscores to dashes in a string:

```
def dasherize(string), do: String.replace(string, "_", "-")
```

Now imagine that at some point you decide to call `to_string/1` before calling `replace/3`:

```
def dasherize(data), do: String.replace(to_string(data), "_", "-")
```

Albeit small, this is a drastic change to our code. Our dasherize function went from supporting only strings as argument to support a large number of data types. In other words, our code became less assertive and more generic.

That said, before adding protocols to our code, we should ask if we really intend to open our function to all types. Maybe we want dasherize to support only atoms and strings? If so, we should rather write:

```
def dasherize(data) when is_atom(data), do: dasherize(Atom.to_string(data))
def dasherize(data), do: String.replace(data, "_", "-")
```

However, if we are confident we want a protocol, then we should indeed use the protocol and write a test case that guarantees our function works for at least a couple types that implement such protocol. Such tests are extremely important to guarantee we don’t make a different assumption somewhere in the same function.

Note this trade-off does not only happen in protocols, but in any polymorphic API, like the `Dict` module. In practice, one should rather use specific dict implementations, like the `Keyword` and `Map` modules, and rely on the `Dict` module only when polymorphism is desired.

### Map/struct access

Elixir provides maps, known as dictionaries in other languages, as a key-value data structure. Maps are created as follows:

```
map = %{name: "john", age: 42}
```

Maps allow two types of access. A strict access, that requires the field name to exist in the map, and a dynamic access, that returns nil if the field does not exist in the map:

```
# Strict access
iex> map.name
"john"
iex> map.address
** (KeyError) key :address not found in: %{age: 42, name: "john"}

# Dynamic access
iex> map[:name]
"john"
iex> map[:address]
nil
```

Both syntaxes have their use cases but we should prefer the strict syntax when possible as it helps us find bugs early on. The same applies to structs, which are named maps:

```
defmodule User do
  defstruct [:first_name, :last_name, :age]

  def name(user) do
    "#{user.first_name} #{user.last_name}"
  end
end

User.name %User{first_name: "John", last_name: "Doe"}
#=> "John Doe"
```

In the example above, we have defined a User struct and a `name/1` function that receives the struct and returns its name. Since we are using `user.first_name`, if we accidentally pass a struct that does not contain such a field, it will crash immediately, with a nice error message!

In fact, the strict aspect of the `user.first_name` syntax is one of the reasons why structs do not support the dynamic syntax out of the box:

```
user = %User{first_name: "John", last_name: "Doe"}
user[:first_name]
** (Protocol.UndefinedError) protocol Access not implemented for %User{...}
```

In case you want to use the dynamic syntax, you need to derive the Access protocol for the User struct:

```
defmodule User do
  @derive [Access]
  defstruct [:first_name, :last_name, :age]

  def name(user) do
    "#{user.first_name} #{user.last_name}"
  end
end
```

However, only derive Access when you truly need to do so, as it is much better to push yourself to rely more on the strict syntax. I would even say relying on Access for structured data is an anti-pattern itself!

### Wrapping up

The most interesting aspect of all examples above is that writing in the assertive style leads to faster, more concise and maintainable code. Even more, it allows us to focus on specific scenarios, postponing any complexity (incidental or accidental) to *only when we need them, if we need them*.

[![f993d3449b61509dbe51a7c3a1a2ef03.png](blog-plataformatec-com-br--writing-assertive-code-with-elixir/e96994f581c60dfaa9e552e349b0412d.png)](http://cta-redirect.hubspot.com/cta/redirect/378213/2aeae558-5b72-4df3-bf32-e1119f34d85e?__hstc=215850376.6f5d8708c0f7dbd5b9454f27423f43a2.1422991370583.1422991370584.1422991370584.1&__hssc=215850376.1.1422991370585&__hsfp=328591743)
