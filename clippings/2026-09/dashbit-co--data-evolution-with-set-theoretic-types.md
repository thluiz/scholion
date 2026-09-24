---
url: "https://dashbit.co/blog/data-evolution-with-set-theoretic-types"
captured_at: "2026-09-24T23:31:16+01:00"
title: "Data evolution with set-theoretic types"
domain: "dashbit-co"
---

*   José Valim
*   January 14th, 2025
*   [elixir](https://dashbit.co/blog/tags/elixir) , [types](https://dashbit.co/blog/tags/types) , [structs](https://dashbit.co/blog/tags/structs)

Recently I have been working on projects that integrate Elixir with native code in C and Rust. One of the Rust libraries defines the following struct (with fields removed for simplicity):

```
struct Schema {
  name: CString,
  format: CString,
  metadata: Option<Vec<u8>>,
  dictionary: Option<*mut Schema>
}
```

It turns out the structure above does not follow the C specification, which says the name may be _null_. Unfortunately, the C library I used was producing data with the name set to `null`, making it impossible to interoperate with the Rust one.

I was the unlucky one to find this out. Even though the library is well used within the Rust ecosystem, by several projects throughout the years, nobody ran into this before. The ideal solution is to change the type of the struct field, perhaps by wrapping the name into an `Option` type:

```
struct Schema {
  name: Option<CString>,
  format: CString,
  metadata: Option<Vec<u8>>,
  dictionary: Option<*mut Schema>
}
```

However, doing so would effectively break ALL existing users of the library. Who am I to propose such a breaking change to a library, based on a scenario that apparently no one else ran into after a few years? Such change would effectively split the library’ ecosystem in two.

Alternatively, we could convert `null`s into empty strings, keeping the current type definition and compatibility, but still not following the spec. This was the option taken for this particular case.

Honestly, this is a tough spot where none of the options are optimal. This article aims to explore how set-theoretic types could help address the issue that many statically typed languages do not allow libraries to evolve their public data definitions in a backwards-compatible manner. The proposed solution aims to be automatically verified by the compiler and type safe.

> There is on-going research to bring [a set-theoretic type system to the Elixir programming language](https://elixir-lang.org/blog/2023/06/22/type-system-updates-research-dev/). While this blog post is related to both Elixir and set-theoretic types, it is not an official proposal to the language. I am publishing it on the Dashbit blog to open up the discussion and collect feedback.

## Breaking changes: libraries vs applications

While changing the name from `CString` to `Option<CString>` would be acceptable within our own applications, since we control all consumers of the code, when it happens in a library, it causes a downstream flow of changes. For this article, let’s assume the library is called “data\_schema”.

If “data\_schema” changes a user facing type, such as the `Schema` type above, in a backwards incompatible manner, its authors have to release a new major version. A new major version can be a fork on the road. Libraries that depend on “data\_schema”‘s new version won’t accept the old ones. Old libraries that depend on “data\_schema” have to be updated and potentially forced to also release a new major version, cascading the problem. If any package along the way is unmaintained, it can stall and complicate further downstream updates.

On the other hand, we, as developers, deal with the fact our data definitions are evolving all the time. If you talk to a seasoned web application developer, they will tell you: “you should never rename a database column”. Instead, you must add a new column, copy the data, and remove the old column.

Similarly, the Erlang VM is used for building distributed systems, which may also require old and new nodes to interact with each other. It also performs hot code upgrades, allowing you to change the code that is running in production without bringing the system down. This requires our codebase to deal with both old and new versions of data.

Despite plenty of examples and uses of data versioning, our type systems often provide little support for us to do the same: once you change a data definition, it assumes all old versions of the data ceases to exist and all code must be immediately rewritten, with nothing between.

## Replicating the problem in Elixir

Let’s port the problem to Elixir. The Elixir team has not yet defined how structs will be declared under set-theoretic types but we can explore some ideas which are valid Elixir syntax today.

Imagine that we define typed structs in Elixir as follows (let’s call this v1):

```
defmodule Schema do
  defstruct do
    name :: string()
  end
end
```

In Elixir, we can now instantiate a new struct as `%Schema{name: "mycolumn"}`.

And let’s say there is a convenience function for upcasing the schema name. It is quite silly but enough to explore the problem space:

```
defmodule SchemaHelpers do
  $ Schema.t() -> Schema.t()
  def upcase_name(%{name: name} = schema) do
    %{schema | name: String.upcase(name)}
  end
end
```

Calling it with `%Schema{name: "mycolumn"}` returns `%Schema{name: "MYCOLUMN"}`.

Now what happens when we change the `Schema` definition to support `nil`s? Let’s call this v2:

```
defmodule Schema do
  defstruct do
    name :: string() or nil
  end
end
```

With the change above, you should now expect `SchemaHelpers.upcase_name/1` to report a typing violation. The `name` can now be `nil` but the `String.upcase/1` function will fail if given a `nil` value.

That looks correct… or does it?

In our v1 of `Schema`, we allowed `name` to only be a `string()`. In a statically typed language, we are effectively proving that all uses of `Schema` has a `string()` name. When we allow the name to also be `nil` in v2, that should not introduce bugs in our software _yet_ because, by definition, there is no instance of `Schema` where the name is `nil`!

In other words, all existing code remains correct, but most type systems would immediately flag them as wrong, on the possibility they _may_ receive a `nil` value. There must be a better way and that’s what we study in this article.

In particular, we want to provide a mechanism where both old and new version of `Schema` can coexist **while preserving type safety**. Luckily, Elixir’s type system allows us to explore this through structural subtyping. So let’s take a deeper look.

## Data instantiation with structural subtyping

In simple words, structural subtyping assigns types based on the `Schema` value, not on the `Schema` definition.

In nominal type systems, where types are represented by their name, the following Elixir code would commonly have type `Schema`:

```
%Schema{name: "mycolumn"}
```

If you want to know exactly what the field `name` represents, you would consult the `Schema` definition, and learn it is `string()` if you are using v1. If you are using v2, it is `string() or nil`, even if the field `name` is always given a string when the schema is instantiated.

However, with structural subtyping, the definition above gets the type `Schema.t(name: string())`, which is valid as long as it is a subtype of the field types specified in the `Schema` definition. Changing the `Schema` definition to a broader type won’t change the instantiated data nor cause type incompatibilities. Consequently, at this moment, there is no `Schema` instance where the name is `nil`.

## Type checking with revisions

As seen above, structural subtyping allows us to preserve the types of our schema fields when we instantiate them, even if the `Schema` definition changes. But what about function signatures?

The `upcase_name` function is a perfect example:

```
defmodule SchemaHelpers do
  $ Schema.t() -> Schema.t()
  def upcase_name(%{name: name} = schema) do
    %{schema | name: String.upcase(name)}
  end
end
```

If the type for the `name` suddenly changes to `string() or nil`, our function will report a typing violation because it is incapable of handling `nil` values. Now, let’s fix the function above to also handle `nil`s:

```
defmodule SchemaHelpers do
  $ Schema.t() -> Schema.t()
  def upcase_name(%{name: nil} = schema) do
    schema
  end

  def upcase_name(%{name: name} = schema) do
    %{schema | name: String.upcase(name)}
  end
end
```

Our code has been fixed but it has a downside. If I give it a struct `%Schema{name: "mycolumn"}`, which has type `Schema.t(name: string())`, the function signature says that it will return a new `Schema.t()`, which is equivalent to type `Schema.t(name: string() or nil)`. In other words, even though we can instantiate structs as `v1`, as soon as we do any operation on them, their types will get “upgraded” to `v2`, which has type `string() or nil`. This will lead to further typing violations, which can lead to breaking changes on codebases using our library.

Instead, it would be ideal if the `upcase_name` function could preserve the version of the schema. If a `schema` of type v1 is given, it returns a schema of type v1. If a schema of type v2 is given, it returns a schema of type v2. In fact, if you look at the implementation of the function, it already guarantees this! But the function signature does not encode this property.

This article proposes to address this problem by introducing an explicit versioning mechanism - let’s call them _revisions_ - to our structs. So in this case, the updated `Schema` struct would look like this:

```
defmodule Schema do
  defstruct do
    name :: string()

    revision 2 do
      name :: string() or nil
    end
  end
end
```

Fields declared without a revision are considered to belong to revision 1. Furthermore, from now on, we will say that `Schema.t()` always returns the field types of the latest revision, but remember you can specify a field type explicitly, such as `Schema.t(name: string())`.

As long as revision 2 (r2) is a supertype of revision 1 (r1), which is something the type system can enforce, we want to generally assert that all code written with r2 will work for both r1 and r2. While code written for r1, only works with r1.

The next challenge is to prove that `upcase_name` returns `r1` if given `r1`, and returns `r2` if given `r2`. Intuitively, we want that:

*   if given a schema that has type `r1`, i.e. the `name` field is a `string()`, it returns a schema with a `string()` name
    
*   if given a schema type that is `r2` but not `r1`, then the `name` field can only be `nil`, and it can return a schema with names of either `string()` or `nil` (after all, we don’t care if r2 downgrades to r1, only the opposite)
    

Luckily, thanks to intersection types, we can precisely encode the logic above into a function signature:

```
$ Schema.t(name: string()) -> Schema.t(name: string())
$ Schema.t(name: nil) -> Schema.t()
```

The definition above says: if the struct matches `r1`, it will return `r1`. Otherwise, if it receives a struct containing the additional parts of `r2`, which is the `nil` possibility in the `name` field, it will return `r2`. This will allow us to enforce what we call the **revision preservation property**.

Developers who work on most statically typed languages are aware that, for changes to be backwards compatible, you are only allowed to widen the types of your inputs. However, with an expressive type system, you also have the option of widening the output types, as long as you do so for the new input types, and that’s precisely what the type above does. You can only return a struct with `nil` `name`, if the `name` field was `nil` in the first place.

The most important part is that, you won’t have to write the signature above. Since we explicitly tagged the revisions, the Elixir compiler can automatically rewrite `$ Schema.t() -> Schema.t()` into a function signature that enforces the revision preservation property! Long story short: we can support both old and new versions of `Schema` and all of the work will be done by the compiler and the type system to guarantee correctness, enabling library authors to provide a safer and better experience to developers.

Let’s see a couple more examples before we dive deeper into how it works.

## Multi-field revisions

Let’s complicate our example a bit further. Imagine this was our struct definition.

```
defmodule Schema do
  defstruct do
    name :: string()
    age :: integer()

    revision 2 do
      name :: string() or nil
      age :: integer() or nil
    end
  end
end
```

Given the `$ Schema.t() -> Schema.t()` signature used `upcase_name/1`, what is the underlying signature the compiler should automatically generate to validate our revision presevation property?

Here it goes:

```
$ Schema.t(name: string(), age: integer()) -> Schema.t(name: string(), age: integer())
$ Schema.t(name: nil) or Schema.t(age: nil) -> Schema.t()
```

It is quite similar to the one before, except it now encompasses more fields. If we receive `r1`, where name is a string and age is an integer, we will return `r1`. Otherwise any field encoded by `r2` and not in `r1`, returns `r2`.

Note we wrote `Schema.t(name: nil) or Schema.t(age: nil)` and not `Schema.t(name: nil, age: nil)`. The latter requires both fields as `nil`, while we want any struct that has _any_ of the fields as `nil` would belong to r2. Hence `Schema.t(name: nil) or Schema.t(age: nil)`.

Therefore, to prove the **revision preservation property**, the number of possibilities we need to validate per revision will grow by the amount of revisioned fields. Each field changed in a new revision adds one new “union” for us to prove, which may have an impact on type checking times.

Regardless if the performance of multiple revisioned fields will be a concern or not, we propose to give users explicit control over which revisions they want to allow in their applications. It is unlikely - or shall we say, not advisable - for a given application to depend on several revisions over a long period of time. They are meant to be transitory.

So let’s see some examples of how one might control the revisions used in their application.

## Explicit revision control

As the author of the `data_schema` library, you want to prove that your library is compatible for all revisions you provide, therefore, you could set the configuration in your `mix.exs` to:

```
revisions: %{
  Schema => [1, 2]
}
```

This will guarantee to the author of the `Schema` struct that users can safely upgrade their codebases through the revision preservation property, as the compiler and type system will assume `r1` and `r2` should coexist.

On the other hand, applications that use `data_schema`, may simply start by supporting only r1 on upgrades:

```
revisions: %{
  Schema => [1]
}
```

Given `data_schema` was proven to work with both revisions, we can restrict our revision to a subset. Then, once application developers are ready to migrate to r2, they either bump the revision or remove the configuration altogether. Ideally, application developers do not need to work with multiple revisions at once. The mechanism is there mostly to empower library authors, but multiple revisions may be handy on large updates.

## Transitive dependencies

Let’s complicate our scenario a bit further. The biggest issue with doing breaking changes to a library is breaking all of the other libraries that depend on it, causing a rift in the ecosystem.

So imagine that we introduce a new dependency, called “depends\_on\_data\_schema”, such that:

```
my_app -> depends_on_data_schema -> data_schema
```

When you configure the revision of `Schema`, it applies to all libraries, so we know this state is valid:

```
my_app -> depends_on_data_schema -> data_schema
  r1                r1                  r1
```

As well as:

```
my_app -> depends_on_data_schema -> data_schema
  r2                r2                  r2
```

However, it is worth pointing out that we could allow a combination of revisions, as long as revisions are not removed as you descend the dependency tree. In particular, we could compile the project like this:

```
my_app -> depends_on_data_schema -> data_schema
  r1                r1                 r1-r2
```

Or like this:

```
my_app -> depends_on_data_schema -> data_schema
  r1              r1-r2                r1-r2
```

But not like this:

```
my_app -> depends_on_data_schema -> data_schema
  r2                r1                 r1-r2
```

This would enable us to upgrade dependencies piecemeal. In fact, `my_app` could even talk to two different libraries, which do not depend on each other, one depending on r1 and another depending on r2, and the type checker can still validate their boundaries are respected.

We could even downcast from r2 to r1. For example, we could mimic the choice done by the Rust library, downcast `r2` to a `r1` by setting the field to an empty string:

```
$ Schema.t() -> Schema.t(name: string())
def from_r2_to_r1(%{name: nil}), do: %{schema | name: ""}
def from_r2_to_r1(%{name: string} = schema), do: schema
```

Alternatively, if you’d rather downcast r2 to r1 while assuming that `name` can never be nil, failing at runtime otherwise (equivalent to an `unwrap`), you might write:

```
$ Schema.t() -> Schema.t(name: string())
def from_r2_to_r1(%{name: nil}), do: raise "not allowed"
def from_r2_to_r1(%{name: string} = schema), do: schema
```

The signature says we will preserve all fields of the given schema, except that `name` is overridden to always have type `string()`.

Would downcasting actually be useful in practice? That is yet to be seen.

## A pinch of formalization

We have learned so far that, by revisioning our schema evolution and guaranteeing that each revision is a supertype, the compiler and type system will work together to guarantee that our code works across several revisions. How does that work behind the scenes?

> This section is for those who are type curious and it is not required reading. Actually, most of this blog post is probably not required for those who’d want to simply _use_ this feature in the future.

When the compiler sees `Schema.t()` inside a type signature, it will add a new intersection (i.e. a new arrow) for each revision that we have. Each new clause will have:

*   the domain set to the current revision excepted by the domain of the previous revisions
*   the codomain set to the current revision unioned by the codomain of the previous revisions

Simply put, if a schema has three versions r1, r2, r3, the type signatures will be:

```
$ domain_r1 -> codomain_r1
$ domain_r2 and not domain_r1 -> codomain_r1 or codomain_r2
$ domain_r3 and not domain_r2 and not domain_r1 -> codomain_r1 or codomain_r2 or codomain_r3
```

Where `domain_r1` is the domain of the type signature with all instances of `Schema.t` replaced by r1 and so forth.

While this may sound complicated at first, they all boil down to standard set operations. Let’s see some examples.

Take our `Schema` with `r1 = Schema.t(name: string())` and `r2 = Schema.t(name: string() or nil)`. The function signature `$ Schema.t() -> Schema.t()` will become:

```
# domain_r1 -> codomain_r1
$ Schema.t(name: string()) -> Schema.t(name: string())

# domain_r2 and not domain_r1 -> codomain_r1 or codomain_r2
$ Schema.t(name: string() or nil) and not Schema.t(name: string()) ->
    Schema.t(name: string() or nil) or Schema.t(name: string())
```

That’s quite verbose but luckily that’s not what users will see in practice. Since `r2` is a supertype of `r1`, the type system will simplify many of these operations.

The first arrow is already in its simplest form. In the second one, `Schema.t(name: string() or nil) and not Schema.t(name: string())` is equivalent to `Schema.t(name: nil)` (all schemas with names `string() or nil` except the ones with names `string()` results in only schemas with `nil` names). Furthermore, `Schema.t(name: string() or nil) or Schema.t(name: string())` is the same as `Schema.t(name: string() or nil)`. After applying these simplications and eliding fields with their default types, we end-up with what we originally wrote:

```
$ Schema.t(name: string()) -> Schema.t(name: string())
$ Schema.t(name: nil) -> Schema.t()
```

#### What about contravariance?

One question people may ask this point is: what about contravariance? What if we have a higher-order function that receives a schema and returns a function that receives another schema and returns yet another schema?

It would have this type signature:

```
$ Schema.t() -> (Schema.t() -> Schema.t())
```

By applying the domain and codomain rules above, we will have the following two arrows, where `r1` and `r2` represents their respective schema versions:

```
$ r1 -> (r1 -> r1)
$ r2 and not r1 -> (r2 -> r2) or (r1 -> r1)
```

The first arrow is, as always, already in its simplified form. What about the second?

Once again we found `r2 and not r1`, which we know to be `Schema.t(name: nil)`. That simplifies the domain of the second arrow. What about its codomain?

When we have a union of arrows, because Elixir does not allow checking the types a function expects at runtime, the only valid application of `(a -> a) or (b -> b)` is an argument that satifies both `a` and `b`, therefore, we need to compute the intersection between their domain (aka inputs) and then return the union of the codomain (aka outputs). In this case, we have `(r2 -> r2) or (r1 -> r1)`, so the intersection of the inputs will be the smallest type, `r1`, and the union will be biggest one, `r2`, which leaves us with `(r1 -> r2)`. This is a less precise type than the original one, but one that mirrors Elixir semantics.

By replacing `r1 and r2` by their respective schemas, the final signature would be:

```
$ Schema.t(name: string()) ->
    (Schema.t(name: string()) -> Schema.t(name: string()))

$ Schema.t(name: nil) ->
    (Schema.t(name: string()) -> Schema.t())
```

There is something deeply elegant about the definition the type system produced here because it gives us the safest definition possible: the returned function only accepts schemas in r1 (i.e. it is strict on its input) and returns the broadest schema possible (i.e. it is broad on its output). These definitions were derived automatically and they are the semantics that your code will be typechecked against to guarantee the revision preservation property.

## Data evolution

There is one last topic to discuss: which changes are possible to our struct definitions when using revisions?

Since we require new revisions to be a supertype of previous ones, the operations we can perform are:

*   Making a field wider than before (a supertype).
    
*   Adding a new field with a default value.
    
*   Marking a field as deprecated (as it may be removed in a future breaking version). Deprecated fields are marked as optional, allowing new code to avoid instatiating them altogether, while retaining compatibility with old one.
    

> While adding a new field makes a revision a subtype of the previous one, if the field has a default value, we can consider that previous revisions actually had the field with an optional type. Therefore, the revision that effectively adds the field is equivalent to making it a required one, which is a supertype.

And the compiler can actually guarantee revisions follow these rules. Any other change (removing fields, changing it to a subtype or a disjoint type, etc) will be a breaking change. Although this looks limiting, all Elixir libraries (and of other programming languages) that desire to remain backwards compatible are already under such constraints today. Revisions should effectively improve the status quo by **making data evolution progressive and type safe**. This is important for the Elixir ecosystem, where the language and major frameworks, such as Phoenix, have remained backwards compatible for more than a decade.

## Summing up

I hope this article introduces the problem of data versioning present in many languages and outlines one possible solution. Overall, there are challenges ahead, including formalizing and proving the safety of the ideas outlined above, as well as asking ourselves how much of what was outlined here is practical.

The goal of data versioning is to provide more mechanisms for **library authors** to evolve their schemas without imposing breaking changes often. Application developers will have limited use of this feature, as they would rather update their existing codebases and their types right away. Although this may find use cases around durable data and distributed systems.

From the theoretical point of view, the only capabilities necessary to make this work is structural subtyping, with unions, intersections, and negations, all available out of the box in Elixir’s set-theoretic type system. The struct versioning itself, aka revisions, can be fully tackled by the compiler, which makes the implementation quite more accessible. The job of the type system is simply to provide a foundation to make this possible!

A massive thank you to Giuseppe Castagna, Guillaume Duboc, and Xuejing Huang for suggestions and the initial formalization of the solution. I am also grateful to Richard Feldman, Leandro Ostera, and Louis Pilfold for feedback on drafts. All opinions and innacuracies are my own.
