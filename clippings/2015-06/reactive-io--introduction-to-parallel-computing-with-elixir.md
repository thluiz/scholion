---
url: "http://www.reactive.io/tips/2015/02/03/introduction-to-parallel-computing-with-elixir/"
captured_at: "2015-06-01T10:07:37-03:00"
title: "Introduction to Parallel Computing with Elixir - Reactive.TIPS - The Official Blog of Reactive.IO"
domain: "reactive-io"
---

# [Introduction to Parallel Computing with Elixir](http://www.reactive.io/tips/2015/02/03/introduction-to-parallel-computing-with-elixir)

With real-time software becoming more and more popular, building applications that support concurrency and parallel computing becomes a must. As such, many new languages and platforms are sprouting up to help engineers do just that. Not long ago, [Elixir](http://elixir-lang.org/) came out into the field and has some features that are hard to beat. Built on top of [Erlang’s](http://www.erlang.org/) virtual machine (known as ), Elixir can use all of Erlang’s existing libraries and leverage all of it’s proven computing benefits. What Elixir brings to the table is a fresh syntax, powerful metaprogramming facilities, and some additional tools that help in building fault tolerant, real-time software.

### Mixing Up a New Project

Elixir is a compiled language and comes with its own build tool, called Mix. With Mix, we can start a new project by running `mix new fibex` and opening the project up in your text editor of choice.

Inside the project, make a new module called `Fibex.Fn` and place in code that will generate [Fibonacci](http://en.wikipedia.org/wiki/Fibonacci_number) numbers. In this example, we are taking advantage of [tail recursion](http://en.wikipedia.org/wiki/Tail_call), which you can learn more about in the previous tip [Parallel Computing Made Easy With Scala and Akka](http://www.reactive.io/tips/2014/04/08/parallel-computing-made-easy-with-scala-and-akka/). In this module, we use Elixir’s `def` keyword for public functions, and `defp` for private functions. We then want to update our `Fibex` module with a run function, which will allow us to generate Fibonacci results for an array of numbers. We’ll also use the `|>` operator to pipe the `ns` array through its necessary transformations.

**/lib/fibex/fn.ex**

```
defmodule Fibex.Fn
```

**/lib/fibex.ex**

```
defmodule Fibex 
    
    
    |> Fibex.Fn
    |> inspect
    |>
```

Now, lets run it from the terminal via the Mix build tool and see what we get back.

```
$ mix run -e "Fibex.run([20, 18, 32, 28, 22, 42, 55, 48])"
[6765, 2584, 2178309, 317811, 17711, 267914296, 139583862445, 4807526976]
```

Looking good, but not good enough!

### Going Parallel

Our Fibonacci calculator works, but its not taking advantage of multiple cores because it is running sequentially. The good news is that Elixir shines at making concurrent, parallel computing easy. To do so, we are going to use Elixir’s ability to spawn off new processes, and then use message passing to return the results when they are ready. Let’s get started.

> **What Does Spawn Do?**
>
> In Elixir and Erlang, the `spawn` command runs a function in a new light weight process. This way, the program can continue running without waiting for the function to return. Processes in Erlang also support [intra-process communication](http://en.wikipedia.org/wiki/Erlang_%28programming_language%29#Concurrency_and_distribution_orientation) via message passing. Together, these features make up the [Actor Model](http://en.wikipedia.org/wiki/Actor_model) that Erlang is highly recognized for.

First, we’re going to add two new functions to our `Fibex.Fn` module: `spawn_run` will spawn a new Fibonacci process so we can compute multiple numbers in parallel, and `send_run` will return our result when it’s computed. For `spawn_run`, we will use the Module, Function, Arguments call to `spawn` and pass the `__MODULE__` token instead of writing `Fibex.Fn`, just in case we change our module name in the future.

Next, we’ll change our `Fibex` module to farm out each Fibonacci calculation to a new process and catch the results via a `receive` loop. Something to notice is that we are tossing along the index for each number so we can sort the results at the end. This is important as we loose the order of the inputs once we concurrently calculate each Fibonacci. Furthermore, we are tossing along the input length and decrementing the counter with each receive loop recursion, this way we know when we’re done calculating the result.

**/lib/fibex/fn.ex**

```
defmodule Fibex.Fn 
   spawn_run  
    spawn __MODULE__ :send_run  
  

   send_run
```

**/lib/fibex.ex**

```
defmodule Fibex 
    
    
    |> with_index
    |>   ->
      Fibex.Fnspawn_run 
    

    receive_fibslength 
  

   receive_fibs result 
    receive 
       ->
        result    result

            
          print_fibsresult
        
          receive_fibs   result
        
    
  

   print_fibs 
    
    |>     ->    
    |>   ->  
    |> inspect
```

Let’s run our program again and see what we get back.

```
$ mix run -e "Fibex.run([20, 18, 32, 28, 22, 42, 55, 48])"
[6765, 2584, 2178309, 317811, 17711, 267914296, 139583862445, 4807526976]
```

Looking better, but its not as easy to use as it could be.

### Building our Escript

One thing that is great about Elixir is that it is all Erlang through-and-through. One great benefit Erlang gives us is the ability to compile an entire project, dependencies and all, into one executable package called an escript. And as Elixir compiles down to Erlang byte-code, we would not even have to install Elixir on the machine running our escript, only Erlang is required.

First step, is we have to specify a `main` function that will be called upon executing our escript. We can put this function anywhere, but for this project `Fibex` makes the most sense. The only housekeeping we need to do is convert each argument into an integer, as they will be captured as strings. We can then pipe them to our run function.

Next, we need to open our `mix.exs` file and add our escript config to our project function. This way, Mix knows what function to pipe our command line arguments into.

**/lib/fibex.ex**

```
defmodule Fibex 
    
     |> Stringto_integer |> 
  

    
    
    |> with_index
    |>   ->
      Fibex.Fnspawn_run 
    

    receive_fibslength 
  

   receive_fibs result 
    receive 
       ->
        result    result

            
          print_fibsresult
        
          receive_fibs   result
        
    
  

   print_fibs 
  
  |>     ->    
  |>   ->  
  |> inspect
```

**mix.exs**

```
defmodule Fibex.Mixfile 
   Mix.Project

   project 
     :fibex
     version "0.0.1"
     elixir "~> 1.0"
     escript main_module Fibex
      
  

  # Configuration for the OTP application
  
  # Type `mix help compile.app` for more information
   application 
    applications :logger
  

  # Dependencies can be Hex packages:
  
  #   {:mydep, "~> 0.3.0"}
  
  # Or git/path repositories:
  
  #   {:mydep, git: "https://github.com/elixir-lang/mydep.git", tag: "0.1.0"}
  
  # Type `mix help deps` for more examples and options
```

Once we make these changes, run the `mix escript.build` build task, and you should see an executable file called `fibex` in our project directory. Go ahead and run it with your numbers sent as arguments, and see what you get back.

```
$ ./fibex 20 18 32 28 22 42 55 48
[6765, 2584, 2178309, 317811, 17711, 267914296, 139583862445, 4807526976]
```

Wonderful, we just reduced our application into an easy to use command-line utility. Now, try passing some large numbers and watch your usage spike up across every core.

### Summary

By using the tools that came with the Elixir platform, we were able to build and package a tool that easily and efficiently utilizes multiple CPU’s. We also learned a bit about what Elixir is, and how it leverages the proven components of the Erlang ecosystem. From here, you can start digging deeper into how Elixir and Erlang work together, and start building real-time software that scales.
