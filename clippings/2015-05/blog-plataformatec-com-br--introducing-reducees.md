---
url: "http://blog.plataformatec.com.br/2015/05/introducing-reducees/"
captured_at: "2015-05-29T18:07:19-03:00"
title: "Introducing reducees"
domain: "blog-plataformatec-com-br"
---

# Introducing reducees « Plataformatec Blog

Elixir provides the concept of collections, which may be in-memory data structures, as well as events, I/O resources and more. Those collections are supported by the Enumerable protocol, which is an implementation of an abstraction we call “reducees”.

In this article, we will outline the design decisions behind such abstraction, often exploring ideas from Haskell, Clojure and Scala that eventually led us to develop this new abstraction called reducees, focusing specially on the constraints and performance characteristics of the Erlang Virtual Machine.

At the end, there is a link to a talk I have recently given at Elixirconf EU 2015, the first Elixir conference in Europe, that explores the next steps and how we plan to introduce asynchrony into the standard library.

## Recursion and Elixir

[Elixir is a functional programming language](http://elixir-lang.org/) that runs on the Erlang VM. All the examples on this article will be written in Elixir although we will introduce the concepts bit by bit.

Elixir provides linked-lists. Lists can hold many items and, with pattern matching, it is easy to extract the head (the first item) and the tail (the rest) of a list:

```
> [h|t] = [1, 2, 3]
> h

> t
[2, 3]
```

An empty list won’t match the pattern `[h|t]`:

```
[h|t] = []
** (MatchError)  match  right hand side value: []
```

Suppose we want to recurse every element in the list, multiplying each element by 2. Let’s write a double function:

```
defmodule Recursion 
   double([h|t]) 
    [h*|double(t)]
  

   double([]) 
    []
```

The function above recursively traverses the list, doubling the head at each step and invoking itself with the tail. We could define a similar function if we wanted to triple every element in the list but it makes more sense to abstract our current implementation. Let’s define a function called `map` that applies a given function to each element in the list:

```
defmodule Recursion 
  ([h|t], fun) 
    [fun.(h)|map(t, fun)]
  

  ([], _fun) 
    []
```

`double` could now be defined in terms of `map` as follows:

```
 double(list) 
  map(list,  x -> x *  )
```

Manually recursing the list is straight-forward but it doesn’t really compose. Imagine we would like to implement other functional operations like `filter`, `reduce`, `take` and so on for lists. Then we introduce sets, dictionaries, and queues into the language and we would like to provide the same operations for all of them.

Instead of manually implementing all of those operations for each data structure, it is better to provide an abstraction that allows us to define those operations only once, and they will work with different data structures.

That’s our next step.

## Introducing Iterators

The idea behind iterators is that we ask the data structure what is the next item until the data structure no longer has items to emit.

Let’s implement iterators for lists. This time, we will be using Elixir documentation and doctests to detail how we expect iterators to work:

```
defmodule Iterator 
   "
  Each step needs to return a tuple containing
  the next element and a payload that will be
  invoked the next time around.

      iex> next([1, 2, 3])
      {1, [2, 3]}
      iex> next([2, 3])
      {2, [3]}
      iex> next([3])
      {3, []}
      iex> next([])
      :done
  "
  ([h|t]) 
    {h, t}
  

  ([]) 
    :done
```

We can implement `map` on top of `next`:

```
(collection, fun) 
  map_next((collection), fun)

 map_next({h, t}, fun) 
  [fun.(h)|map_next((t), fun)]

 map_next(:done, _fun) 
  []
```

Since `map` uses the `next` function, as long as we implement `next` for a new data structure, `map` (and all future functions) should work out of the box. This brings the polymorphism we desired but it has some downsides.

Besides not having ideal performance, it is quite hard to make iterators work with resources (events, I/O, etc), leading to messy and error-prone code.

The trouble with resources is that, if something goes wrong, we need to tell the resource that it should be closed. After all, we don’t want to leave file descriptors or database connections open. This means we need to extend our `next` contract to introduce at least one other function called `halt`.

`halt` should be called if the iteration is interrupted suddenly, either because we are no longer interested in the next items (for example, if someone calls `take(collection, 5)` to retrieve only the first five items) or because an error happened. Let’s start with take:

```
(collection, n) 
  take_next((collection), n)

# Invoked on every step
 take_next({h, t}, n)  n >  
  [h|take_next((t), n - )]

# If we reach this, the collection finished
 take_next(:done,  
  []

# If we reach this, we took all we cared about before finishing
 take_next(value, ) 
  halt(value) # Invoke halt as a "side-effect" for resources
  []
```

Implementing `take` is somewhat straight-forward. However we also need to modify `map` since every step in the user supplied function can fail. Therefore we need to make sure we call `halt` on every possible step in case of failures:

```
(collection, fun) 
  map_next((collection), fun)

 map_next({h, t}, fun) 
  [try 
     fun.(h)
   rescue
     e ->
       # Invoke halt as a "side-effect" for resources
       # in case of failures and then re-raise
       halt(t)
       raise(e)
   |map_next((t), fun)]

 map_next(:done, _fun) 
  []
```

This is not elegant nor performant. Furthermore, it is very error prone. If we forget to call `halt` at some particular point, we can end-up with a dangling resource that may never be closed.

## Introducing reducers

Not long ago, Clojure introduced the concept of [reducers](http://clojure.com/blog/2012/05/08/reducers-a-library-and-model-for-collection-processing.html).

Since Elixir protocols were heavily inspired on Clojure protocols, I was very excited to see their take on collection processing. Instead of imposing a particular mechanism for traversing collections as in iterators, reducers are about sending computations to the collection so the collection applies the computation on itself. From the announcement: “the only thing that knows how to apply a function to a collection is the collection itself”.

Instead of using a `next` function, reducers expect a `reduce` implementation. Let’s implement this `reduce` function for lists:

```
defmodule Reducer 
   reduce([h|t], acc, fun) 
    reduce(t, fun.(h, acc), fun)
  

   reduce([], acc, _fun) 
    acc
```

With reduce, we can easily calculate the sum of a collection:

```
(collection) 
  reduce(collection, ,  x, acc -> x + acc )
```

We can also implement map in terms of reduce. The list, however, will be reversed at the end, requiring us to `reverse` it back:

```
(collection, fun) 
  reversed = reduce(collection, [],  x, acc -> [fun.(x)|acc] )
  # Call Erlang reverse (implemented in C for performance)
  :lists.reverse(reversed)
```

Reducers provide many advantages:

- They are conceptually simpler and faster
- Operations like `map`, `filter`, etc are easier to implement than the iterators one since the recursion is pushed to the collection instead of being part of every operation
- It opens the door to parallelism as its operations are no longer serial (in contrast to iterators)
- No conceptual changes are required to support resources as collections

The last bullet is the most important for us. Because the collection is the one applying the function, we don’t need to change `map` to support resources, all we need to do is to implement `reduce` itself. Here is a pseudo-implementation of reducing a file line by line:

```
 reduce(file, acc, fun) 
  descriptor = File.open(file)

  try 
    reduce_next(readline(descriptor), acc, fun)
  after
    File.close(descriptor)
  

 reduce_next({line, descriptor}, acc, fun) 
  reduce_next(readline(descriptor), fun.(line, acc), fun)

 reduce_next(:done, acc, _fun) 
  acc
```

Even though our file reducer uses something that looks like an iterator, because that’s the best way to traverse the file, from the `map` function perspective we don’t care which operation is used internally. Furthermore, it is guaranteed the file is closed after reducing, regardless of success or failure.

There are, however, two issues when implementing reducers as proposed in Clojure into Elixir.

First of all, some operations like `take` cannot be implemented in a purely functional way. For example, Clojure relies [on reference types](http://clojure.org/atoms) on its [take implementation](https://github.com/clojure/clojure/blob/4964194bae036dc2cddd3f9c03479657aeab6e8c/src/clj/clojure/core/reducers.clj#L234-L246). This may not be an issue depending on the language/platform (it certainly isn’t in Clojure) but it is an issue in Elixir as side-effects would require us to spawn new processes every time take is invoked.

Another drawback of reducers is, because the collection is the one controlling the reducing, we cannot implement operations like `zip` that requires taking one item from a collection, then suspending the reduction, then taking an item from another collection, suspending it, and starting again by resuming the first one and so on. Again, at least not in a purely functional way.

With reducers, we achieve the goal of a single abstraction that works efficiently with in-memory data structures and resources. However, it is limited on the amount of operations we can support efficiently, in a purely functional way, so we had to continue looking.

## Introducing iteratees

It was at Code Mesh 2013 that I first heard about iteratees. [I attended a talk by Jessica Kerr](http://www.infoq.com/presentations/io-code-data) and, in the first minutes, she described exactly where my mind was at the moment: iterators and reducers indeed have their limitations, but they have been solved in [scalaz-stream](https://github.com/scalaz/scalaz-stream).

After the talk, Jessica and I started to explore how scalaz-stream solves those problems, eventually leading us to [the Monad.Reader issue that introduces iteratees](https://themonadreader.files.wordpress.com/2010/05/issue16.pdf). After some experiments, we had a prototype of iteratees working in Elixir.

With iteratees, we have “instructions” going “up and down” between the source and the reducing function telling what is the next step in the collection processing:

```
defmodule Iteratee 
   "
  Enumerates the collection with the given instruction.

  If the instruction is a `{:cont, fun}` tuple, the given
  function will be invoked with `{:some, h}` if there is
  an entry in the collection, otherwise `:done` will be
  given.

  If the instruction is `{:halt, acc}`, it means there is
  nothing to process and the collection should halt.
  "
   enumerate([h|t], {:cont, fun}) 
    enumerate(t, fun.({:some, h})) 
  

   enumerate([], {:cont, fun}) 
    fun.(:done)
  

   enumerate( {:halt, acc}) 
    {:halted, acc}
```

With `enumerate` defined, we can write `map`:

```
(collection, fun) 
  {:done, acc} = enumerate(collection, {:cont, mapper([], fun)})
  :lists.reverse(acc)

 mapper(acc, fun) 
  
    {:some, h} -> {:cont, mapper([fun.(h)|acc], fun)}
    :done      -> {:done, acc}
```

`enumerate` is called with `{:cont, mapper}` where `mapper` will receive `{:some, h}` or `:done`, as defined by `enumerate`. The `mapper` function then either returns `{:cont, mapper}`, with a new `mapper` function, or `{:done, acc}` when the collection has told no new items will be emitted.

The Monad.Reader publication defines iteratees as teaching fold (reduce) new tricks. This is precisely what we have done here. For example, while `map` only returns `{:cont, mapper}`, it could have returned `{:halt, acc}` and that would have told the collection to halt. That’s how `take` could be implemented with iteratees, we would send `cont` instructions until we are no longer interested in new elements, finally returning `halt`.

So while iteratees allow us to teach reduce new tricks, they are much harder to grasp conceptually. Not only that, functions implemented with iteratees were from 6 to 8 times slower in Elixir when compared to their reducer counterpart.

In fact, it is even harder to see how iteratees are actually based on reduce since it hides the accumulator inside a closure (the `mapper` function, in this case). This is also the cause of the performance issues in Elixir: for each mapped element in the collection, we need to generate a new closure, which becomes very expensive when mapping, filtering or taking items multiple times.

That’s when we asked: what if we could keep what we have learned with iteratees while maintaining the simplicity and performance characteristics of reduce?

## Introducing reducees

Reducees are similar to iteratees. The difference is that they clearly map to a reduce operation and do not create closures as we traverse the collection. Let’s implement reducee for a list:

```
defmodule Reducee 
   "
  Reduces the collection with the given instruction,
  accumulator and function.

  If the instruction is a `{:cont, acc}` tuple, the given
  function will be invoked with the next item and the
  accumulator.

  If the instruction is `{:halt, acc}`, it means there is
  nothing to process and the collection should halt.
  "
   reduce([h|t], {:cont, acc}, fun) 
    reduce(t, fun.(h, acc), fun) 
  

   reduce([], {:cont, acc}, _fun) 
    {:done, acc}
  

   reduce( {:halt, acc}, _fun) 
    {:halted, acc}
```

Our reducee implementations maps cleanly to the original reduce implementation. The only difference is that the accumulator is always wrapped in a tuple containing the next instruction as well as the addition of a `halt` checking clause.

Implementing `map` only requires us to send those instructions as we reduce:

```
(collection, fun) 
  {:done, acc} =
    reduce(collection, {:cont, []},  x, acc ->
      {:cont, [fun.(x)|acc]}
    )
 :lists.reverse(acc)
```

Compared to the original reduce implementation:

```
(collection, fun) 
  reversed = reduce(collection, [],  x, acc -> [fun.(x)|acc] )
  :lists.reverse(reversed)
```

The only difference between both implementations is the accumulator wrapped in tuples. We have effectively replaced the closures in iteratees by two-item tuples in reducees, which provides a considerably speed up in terms of performance.

The tuple approach allows us to teach new tricks to reducees too. For example, our initial implementation already supports passing `{:halt, acc}` instead of `{:cont, acc}`, which we can use to implement `take` on top of reducees:

```
(collection, n)  n >  
  { {acc, } =
    reduce(collection, {:cont, {[], n}}, 
      x, {acc, count} -> {take_instruction(count), {[x|acc], n-}}
    )
 :lists.reverse(acc)

 take_instruction(),  :halt
 take_instruction(n),  :cont
```

The accumulator in given to `reduce` now holds a list, to collect results, as well as the number of elements we still need to take from the collection. Once we have taken the last item (count == 1), we `halt` the collection.

At the end of the day, this is the abstraction that ships with Elixir. It solves all requirements outlined so far: it is simple, fast, works with both in-memory data structures and resources as collections, and it supports both `take` and `zip` operations in a purely functional way.

## The path forward

Elixir developers mostly do not need to worry about the underlying reducees abstraction. Developers work directly with the module [Enum](http://elixir-lang.org/docs/master/elixir/#!Enum.html) which provides a series of operations that work with any collection. For example:

```
iex> Enum.map([, , ],  x -> x *  )
[, , ]
```

All functions in Enum are eager. The `map` operation above receives a list and immediately returns a list. None the less, it didn’t take long for us to add lazy variants of those operations:

```
iex> Stream.map([, , ],  x -> x *  )
#Stream<...>
```

All the functions in [Stream](http://elixir-lang.org/docs/master/elixir/#!Stream.html) are lazy: they only store the computation to be performed, traversing the collection just once after all desired computations have been expressed.

In addition, the `Stream` module provides a series of functions for abstracting resources, generating infinite collections and more.

In other words, in Elixir we use the same abstraction to provide both eager and lazy operations, that accepts both in-memory data structures or resources as collections, all conveniently encapsulated in both [Enum](http://elixir-lang.org/docs/master/elixir/#!Enum.html) and [Stream](http://elixir-lang.org/docs/master/elixir/#!Stream.html) modules.

While reducees are an important milestones, they are not our end goal. After all, the operations in Enum and Stream we have implemented so far are still purely functional and the [Rx developers](http://reactivex.io/) have showed us there is a long way to go once we decide to tackle asynchrony.

That’s exactly what we want to explore next for Elixir. For those interested in learning more, I have explored those topics at Elixirconf EU 2015 (the content related to this post [starts at 30:39](https://youtu.be/EaP0y4pdKD0?t=1839)):

We hope you are as excited as we are about our foundations and what is coming next!

*P.S.: An enormous thank you to Jessica Kerr for introducing me to iteratees and pairing with me at Code Mesh. Also, thanks to Jafar Husein for the conversations at Code Mesh and the team behind Rx which we are exploring next. Finally, thank you to James Fish, Pater Hamilton, Eric Meadows-Jönsson and Alexei Sholik for the countless reviews, feedback and prototypes regarding Elixir’s future.*

[![4f6edf7accbcf4e781edbaa36816ee9b.png](blog-plataformatec-com-br--introducing-reducees/4f6edf7accbcf4e781edbaa36816ee9b.png)](http://plataformatec.com.br/elixir-radar)
