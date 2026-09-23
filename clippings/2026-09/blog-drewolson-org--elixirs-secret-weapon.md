---
url: "https://blog.drewolson.org/elixirs-secret-weapon/?utm_campaign=elixir_radar_96&utm_medium=email&utm_source=RD+Station"
captured_at: "2026-09-23T18:54:06+01:00"
title: "Elixir's Secret Weapon | software is fun"
domain: "blog.drewolson.org"
---

Elixir's Secret Weapon
May 12, 2017
 · Drew Olson

I recently began using a new(ish) feature of Elixir that completely transformed the way I build programs. I'm talking about the special form with. It can feel unfamiliar at first, but it is extremely powerful and flexible. This article will explain how with works and how it can be used to make your code more robust to errors. First, though, let's look at the problem with is trying to solve.

Tagged Tuples

The Elixir community has borrowed an idiom from the Erlang community called tagged tuples. Using this approach, our functions will return a tuple where the first value is an atom describing the "type" of the result. A common pattern is returning {:ok, value} for a successful response and {:error, some_error} for an error response.

defmodule Math do

  def divide(_, b) when b == 0, do: {:error, "divide by zero"}

  def divide(a, b), do: {:ok, a / b}

end



case Math.divide(1, 2) do

  {:ok, result} -> "success: #{result}"

  {:error, error} -> "error: #{error}"

end

# => "success: 0.5"


This is nice for a few reasons. First, it allows us to treat errors as values. We know that our function will always return even when provided semantically invalid data. Second, we can use pattern matching to act explicitly on both the success and failure case.

This patterns starts to break down when we want to perform multiple, dependent actions that can all fail. Suppose, for example, that we'd like to divide two numbers and, if successful, divide the result by a third number.

case Math.divide(1, 2) do

  {:ok, result} ->

    case Math.divide(result, 4) do

      {:ok, result} -> "success: #{result}"

      {:error, error} -> "error: #{error}"

    end

  {:error, error} -> "error: #{error}"

end

# => "success: 0.125"


This works, sure, but it's becoming challenging to read. You can easily imagine the mess this becomes with an arbitrarily long list of dependent operations.

What should we do? We want to continue using this pattern because it is safe and explicit but it feels ugly and unreadable with real-world examples. The answer, of course, is to use with.

Using with

The with special form allows you to define a set of operations to perform and associated patterns to match their results against. Each operation can use bindings from the pattern match of the previous operations. If any of the matches fail, the entire with form stops and that non-matching result is returned. Let's explore by rewriting the above example using with.

with {:ok, a} <- Math.divide(1, 2),

     {:ok, b} <- Math.divide(a, 4) do

  "success: #{b}"

end

# => "success: 0.125"


Let's walk through the execution. First, we call Math.divide(1, 2). The result is {:ok, 0.5}. The with form checks to see if this matches the pattern on the lefthand side of <-. It does, so the variable a is bound to 0.5 and execution continues. On the second line, we run Math.divide(0.5, 4) (because a is now bound to 0.5). This returns {:ok, 0.125}. We check if it matches the pattern on the lefthand side of its <-. It does, so b is bound to 0.125. There are no more operations to perform, so the body of the do block is executed. This do block can use any of the bindings from the with operations above. It uses b to return the string "success: 0.125".

Now, let's try walking through an error case.

with {:ok, a} <- Math.divide(1, 0),

     {:ok, b} <- Math.divide(a, 4) do

  "success: #{b}"

end

# => {:error, "divide by zero"}


First, we call Math.divide(1, 0). The result is {:error, "divide by zero"}. We check to see if this matches the patter on the left of <-. It doesn't! As soon as this mismatch occurs, the with form immediately stops executing further operations and returns the result that did not match. Therefore, the return value of the form is {:error, "divide by zero"}.

Better Error Handling

We're already in a better spot by using with but we can go even further. The with form allows us to describe an else clause that handles any non-matching values rather than simply returning them. Let's add one.

with {:ok, a} <- Math.divide(1, 0),

     {:ok, b} <- Math.divide(a, 4) do

  "success: #{b}"

else

  {:error, error} -> "error: #{error}"

end

# => "error: divide by zero"


Now, when the first operation returns {:error, "divide by zero"} and it doesn't match the pattern, the value is passed to the else block. Next, we check each clause of the else block in order (in this example there is only one clause). The first clause matches {:error, "divide by zero"}, so the string "divide by zero" is bound to error. Finally, the body of that clause is executed with the bindings from the match. It returns the string "error: divide by zero".

More

The with form allows even more flexibility, including guard clauses in each of the operations. For more examples see the docs.
