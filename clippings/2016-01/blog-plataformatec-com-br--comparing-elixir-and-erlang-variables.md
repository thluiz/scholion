---
url: "http://blog.plataformatec.com.br/2016/01/comparing-elixir-and-erlang-variables/"
captured_at: "2016-01-25T08:48:13-03:00"
title: "Comparing Elixir and Erlang variables"
domain: "blog-plataformatec-com-br"
---

# Comparing Elixir and Erlang variables

Sometimes Erlang programmers are worried “Elixir variables may be the source of hidden bugs”. This article discusses those concerns and shows how variables in Erlang can produce related “hidden bugs”, some of those eliminated by Elixir.

Before we start, a short disclaimer: Elixir does not have mutable variables, it has rebinding. Mutability is often associated with storage. In Elixir, the values being stored cannot be changed (same as in Erlang). For an example of mutable variables, we could look at F#. In F# explicitly using the `mutable` keyword (e.g. `let mutable x = 5`) would allow us to change a value inside an inner loop (equivalent to a list comprehension or inside `Enum.map`) and observe the change after the loop is over. That is mutability, and that is not possible in Elixir or Erlang without using explicit storage like processes or ETS.

Back on track. This article will explore the potential for hidden bugs when changing code. Those bugs exist because both Erlang and Elixir variables provide *implicit behaviour*. Elixir rebinds implicitly, Erlang pattern matches implicitly. Such bugs may show up if developers add or remove variables without being mindful of its context.

Let’s see some examples. Imagine the following Elixir code:

```
foo_bar = ...
# some code
use_foo_bar(foo_bar)
```

What happens if you introduce `foo_bar` before the snippet above?

```
foo_bar = ... # newly added line
foo_bar = ...
# some code
use_foo_bar(foo_bar)
```

The code would work just as fine and the compiler would even warn if the newly added `foo_bar` is unused. What would happen, however, if the new line is introduced after the `foo_bar` definition?

```
foo_bar = ...
# some code
foo_bar = ... # newly added line
use_foo_bar(foo_bar)
```

The semantics may have potentially changed if you wanted `use_foo_bar` to use the first `foo_bar` variable. Indeed, careless change may cause bugs.

Let’s check Erlang. Given the code:

```
FooBar = ...
% some code
use_foo_bar(FooBar)
```

What happens if you introduce `FooBar` before its definition?

```
FooBar = ... % newly added line
FooBar = ... % old line errors
% some code
use_foo_bar(FooBar)
```

The Erlang code crashes at runtime instead of silently continuing. Certainly an improvement, but it still means that introducing a variable in Erlang requires us to certify the variable is not matched later on, as `FooBar` will no longer be assigned to but matched on.

What happens if we introduce it after its definition?

```
FooBar = ...
% some code
FooBar = ... % newly added line and it errors
use_foo_bar(FooBar)
```

This time, the new line crashes. In other words, due to implicit matching in Erlang, we not only need to worry about all the code *after* introducing a variable, but we also need to be mindful of all the code *before* introducing it, as any previous code can cause future variables to become implicit matches.

In other words, so far Elixir requires you to be mindful of all later code after the introduction of a variable while Erlang requires you to know all previous and further code before the introduction of a variable. The one benefit of Erlang so far is that the code may crash explicitly on the match.

However, things get more complicated when considering case expressions.

Let’s say you want to match on a new value inside a case. In Elixir you would write:

```
 some_expr() 
  {, safe_value} -> perform_something_safe()
  -> perform_something_unsafe()
```

What would happen if you accidentally introduce a `safe_value` variable in Elixir before that case statement?

```
safe_value = ... # newly added line
# some code
 some_expr() 
  {, safe_value} -> perform_something_safe()
  -> perform_something_unsafe()
```

Nothing, the code works just fine due to rebinding.

Let’s see what happens in Erlang:

```
 some_expr() 
  {ok, SafeValue} -> perform_something_safe();
   -> perform_something_unsafe()
```

And what happens when you introduce a variable?

```
SafeValue = ... % newly added line
% some code
 some_expr() 
  {ok, SafeValue} -> perform_something_safe();
   -> perform_something_unsafe()
```

You have just silently introduced a potentially dangerous bug in your code! Again, because Erlang *implicitly matches*, we may now accidentaly perform an unsafe operation as the first clause no longer binds to `SafeValue` but it will match against it.

Similar bug happens in Erlang when you are matching on an existing variable and you remove it. Imagine you have this working Elixir code:

```
safe_value = ...
# some code
 some_expr() 
  {, ^safe_value} -> perform_something_safe()
  -> perform_something_unsafe()
```

Because Elixir explicitly matches, if you remove the definition of `safe_value`, the code won’t even compile. Let’s see the working version of the Erlang one:

```
SafeValue = ...
% some code
 some_expr() 
  {ok, SafeValue} -> perform_something_safe();
   -> perform_something_unsafe()
```

If you remove the `SafeValue` variable, the first clause will now bind to `SafeValue` instead of matching, silently changing the behaviour of the code once again! Again, another bug while the Elixir approach has shielded us on both cases.

At this point, Elixir:

- requires you to analyse all the following code when introducing a variable, failing to do so may cause bugs
- matching on a variable is always safe due to rebinding and the use of `^` for explicit match

while Erlang:

- requires you to analyse all the previous and further code when introducing a variable to be sure it is a match or an assignment, failing to do so will cause runtime crashes
- requires you to analyse all the following code when introducing a variable to be sure we won’t change a later case semantics, failing to do so may cause bugs
- requires you to analyse all the following code when removing a variable to be sure we won’t change a later case semantics, failing to do so may cause bugs

## Numbered variables

At the beginning, we have mentioned someone may introduce a new variable `foo_bar` in the Elixir code and change the code semantics if the variable was already used later on. However, most of those cases are desired. For example, in Elixir:

```
foo_bar = step1()
foo_bar = step2(foo_bar)
foo_bar = step3(foo_bar)
# some code
use_foo_bar(foo_bar)
```

In Erlang:

```
FooBar0 = step1(),
FooBar1 = step2(FooBar0),
FooBar2 = step3(FooBar1),
% some code
use_foo_bar(FooBar2)
```

Now what happens if we want to introduce a new version of `foo_bar` (`step_4`) in Elixir?

```
foo_bar = step1()
foo_bar = step2(foo_bar)
foo_bar = step3(foo_bar)
foo_bar = step4(foo_bar) # newly added line
# some code
use_foo_bar(foo_bar)
```

The code just works. What about Erlang?

```
FooBar0 = step1(),
FooBar1 = step2(FooBar0),
FooBar2 = step3(FooBar1),
FooBar3 = step4(FooBar2),
% some code
use_foo_bar(FooBar2) % A FooBar2   changed
```

If the developer introduces a new variable and forgets to change `FooBar2` later on, the code semantics changed, introducing the same bug rebinding in Elixir would. This is particularly troubling if you change all but miss one variable, since the code won’t emit “unused variable” warnings. This is even more prone to errors when adding an intermediate step (say between `step2` and `step3`).

Some will say that a benefit of numbered variables is that further code could use any of `FooBar2` and `FooBar3`, for example:

```
FooBar0 = step1(),
FooBar1 = step2(FooBar0),
FooBar2 = step3(FooBar1),
FooBar3 = step4(FooBar2),
% some code
use_foo_bar(FooBar2),
something_else(FooBar3)
```

However I would consider the code above to be a poor practice because there is nothing in the name `FooBar2` that hints to why it is different than `FooBar3`. In this case, the variable names would not reflect at all why part of the code would prefer to use one over the other. Your team will be much better off by giving explicit names instead of versioned ones.

## Summing up

Because both Elixir and Erlang variables provide implicit behaviour, rebinding and pattern matching respectively, both require care when adding or removing variables to existing code. Therefore, if Elixir can be source of hidden bugs, we have shown Erlang is the source of similar bugs under different situations. Not only that, Erlang requires both previous and further knowledge of the context when introducing new variables while Elixir requires only further knowledge. The only way to circumvent those bugs in both languages is by either forbidding or *explicitly providing both rebinding and pattern match* operations, which none of the languages do.

It is possible some will react to this article by saying: “this does not happen in my code”. The truth is that it does happen, even in small functions:

On the other hand, it does not mean writing code in Erlang or Elixir is going to lead to more bugs in your software. After all, Erlang developers have been writing robust software for decades. Those “quirks” exist in any language and they end-up internalized by programmers as they get experienced. That’s exactly from where the “this does not happen in my code” comes from.

At the end of the day, no language will guarantee you can safely change code without caring about its context. There will always be “hidden bugs”. For example, in languages like Clojure, JavaScript and Ruby, variables and function names exist in the same namespace, so introducing variables may change the semantics of function calls. Since both Erlang and Elixir provide two namespaces, one for variables and another for functions, they are shielded from these particular “hidden bugs”.

Furthermore, type systems, compiler warnings, test suites are all techniques that help solve those problems. Languages may also provide patterns, like the Elixir pipe operator (`|>`), to help to convert repetitive code into more readable and less error-prone versions.

At least, I hope this puts to rest the claim that Elixir variables are somehow unsafer than Erlang ones (or vice-versa).

*Thanks to Joe Armstrong, Saša Juric, James Fish, Chris McCord, Bryan Hunter, Sean Cribbs and Anthony Ramine for reviewing this article and providing feedback.*

[![02729411279d02d2d8aead9c2f810d98.png](blog-plataformatec-com-br--comparing-elixir-and-erlang-variables/02729411279d02d2d8aead9c2f810d98.png)](http://plataformatec.com.br/elixir-radar?utm_source=our-blog&utm_medium=referral&utm_campaign=elixir-radar&utm_content=elixir-radar-cta-blog-post-bottom)
