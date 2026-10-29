---
url: "http://www.cursingthedarkness.com/2015/08/thinking-about-stream-and-enum-in-terms.html"
captured_at: "2015-10-02T07:51:23-03:00"
title: "Curse the Darkness: Thinking about Stream and Enum in Terms of Function Composition"
domain: "cursingthedarkness-com"
---

# Thinking about Stream and Enum in Terms of Function Composition

Coming from a Ruby background it took me a while to wrap my head around what Stream and really are. It's far too easy to think about them as a generalized version of a Ruby Array.  
  
At their heart, they are both tools for composing functions.  
  
Let's start with Enum, in most object style languages enumerators support an "each" method  
that allows you to operate one at a time on members of the collection.  
  
Elixir looks quite different at first. It requires that the collection implement these basic functions.

|  |  |
| --- | --- |
| [count(collection)](http://www.cursingthedarkness.com/2015/08/thinking-about-stream-and-enum-in-terms.htmlfile:///Users/booker/Library/Application%20Support/Dash/DocSets/Elixir/Elixir.docset/Contents/Resources/Documents/docs/elixir/Enumerable.html#count/1) | Retrieves the collection’s size |
| [member?(collection, value)](http://www.cursingthedarkness.com/2015/08/thinking-about-stream-and-enum-in-terms.htmlfile:///Users/booker/Library/Application%20Support/Dash/DocSets/Elixir/Elixir.docset/Contents/Resources/Documents/docs/elixir/Enumerable.html#member?/2) | Checks if a value exists within the collection |
| [reduce(collection, acc, fun)](http://www.cursingthedarkness.com/2015/08/thinking-about-stream-and-enum-in-terms.htmlfile:///Users/booker/Library/Application%20Support/Dash/DocSets/Elixir/Elixir.docset/Contents/Resources/Documents/docs/elixir/Enumerable.html#reduce/3) | Reduces the collection into a value |

None of these looks like an "each" method[1].

All the functions do is use these 3 basic functions to provide handy shortcuts for

using the reduce function of the original collection. Unlike a typical "each" method in Ruby,

an  function can bail out at any time. For example, look at the implementation for

Enum.all?

def all?(collection, fun) do

Enumerable.reduce(collection, {:cont, true}, fn(entry, \_) ->

if fun.(entry), do: {:cont, true}, else: {:halt, false}

end) |> elem(1)

Like most of the functions in , it's using the collection's reduce function to implement a specific kind of reduction. In effect it's a composition of functions. It's also "lazy" in the sense that it only iterates as far as it has to generate the correct result. It's important to note that Enumerable implements a different reduce function than the standard one in Enum. ( The accumulator variable must return a tuple consisting of status and "real" accumulator. )

Now let's consider the case of Stream. What it does is very similar to , except that it doesn't  
actually execute the reduce function. In effect it creates an anonymous function for transforming the   
collection into another collection. You can use this "dynamic" collection anyplace you can use a regular collection.   
iex(9)> foo =  1..10 |> Stream.map( fn(x) -> x \* 2 end )  
#Stream<[enum: 1..10,   
funs: [#Function<45.113986093/1 in Stream.map/2>]]>  
iex(10)> foo |> Enum.max  
  
iex(11)> foo |> Enum.min  
  
iex(12)> foo |> Enum.take(1)  
  
iex(13)> foo |> Enum.take(3)  
[2, 4, 6]

The important thing to note from this example is that the a collection defined by Stream does not imply state. It behaves just like a normal collection and is just as immutable. Every time you use it  
it starts at the beginning. The decision about when to use a Stream is should be based on the tradeoffs of storing the collection verses creating it runtime. One difference that is important to note is that Stream only supports using reduce, using count member directly from Enumerable will fail. Looking at the code for Enum.count we see how you can use reduce  
emulate these functions.   
def count(collection) do  
    case Enumerable.count(collection) do  
      {:ok, value} when is\_integer(value) ->  
        value  
      {:error, module} ->  
        module.reduce(collection, {:cont, 0}, fn  
          \_, acc -> {:cont, acc + 1}  
        end) |> elem(1)

[1]- It's simple enough to create an "each" from a reduce once you've played around with enough

examples of reduce.
