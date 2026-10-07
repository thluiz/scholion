---
url: "http://learnxinyminutes.com/docs/elixir/"
captured_at: "2015-02-15T11:23:48-03:00"
title: "Learn elixir in Y Minutes"
domain: "learnxinyminutes-com"
---

# [Learn X in Y minutes](http://learnxinyminutes.com/)

## Where X=elixir

Get the code: [learnelixir.ex](http://learnxinyminutes.com/docs/files/learnelixir.ex)

Elixir is a modern functional language built on top of the Erlang VM.
It’s fully compatible with Erlang, but features a more standard syntax
and many more features.

```
# Single line comments start with a number symbol.

# There's no multi-line comment,
# but you can stack multiple comments.

# To use the elixir shell use the `iex` command.
# Compile your modules with the `elixirc` command.

# Both should be in your path if you installed elixir correctly.

## ---------------------------
## -- Basic types
## ---------------------------

# There are numbers
    # integer
 # integer
  # float

# Atoms, that are literals, a constant with name. They start with `:`.
:hello # atom

# Tuples that are stored contiguously in memory.
 # tuple

# We can access a tuple element with the `elem` function:
    #=> 1

# Lists that are implemented as linked lists.
 # list

# We can access the head and tail of a list as follows:
    
 #=> 1
 #=> [2,3]

# In elixir, just like in Erlang, the `=` denotes pattern matching and
# not an assignment.

# This means that the left-hand side (pattern) is matched against a
# right-hand side.

# This is how the above example of accessing the head and tail of a list works.

# A pattern match will error when the sides don't match, in this example
# the tuples have different sizes.
# {a, b, c} = {1, 2} #=> ** (MatchError) no match of right hand side value: {1,2}

# There are also binaries
<<>> # binary

# Strings and char lists
hello" # string
'hello' # char list

# Multi-line strings
"""
I'm a multi-line
string.
"""
#=> "I'm a multi-line\nstring.\n"

# Strings are all encoded in UTF-8:
héllò" #=> "héllò"

# Strings are really just binaries, and char lists are just lists.
<<  >> #=> "abc"
     #=> 'abc'

# `?a` in elixir returns the ASCII integer for the letter `a`
 #=> 97

# To concatenate lists use `++`, for binaries use `<>`
       #=> [1,2,3,4,5]
'hello '  'world'  #=> 'hello world'

<<>> <> <<>> #=> <<1,2,3,4,5>>
hello " <> world"  #=> "hello world"

# Ranges are represented as `start..end` (both inclusive)
 #=> 1..10
lowerupper   # Can use pattern matching on ranges as well
lower upper #=> [1, 10]

## ---------------------------
## -- Operators
## ---------------------------

# Some math
    #=> 2
   #=> 5
    #=> 10
   #=> 5.0

# In elixir the operator `/` always returns a float.

# To do integer division use `div`
  #=> 5

# To get the division remainder use `rem`
  #=> 1

# There are also boolean operators: `or`, `and` and `not`.
# These operators expect a boolean as their first argument.
   #=> true
false   #=> true
# 1 and true    #=> ** (ArgumentError) argument error

# Elixir also provides `||`, `&&` and `!` which accept arguments of any type.
# All values except `false` and `nil` will evaluate to true.
    #=> 1
false   #=> false
    #=> nil
!true #=> false

# For comparisons we have: `==`, `!=`, `===`, `!==`, `<=`, `>=`, `<` and `>`
   #=> true
   #=> false
    #=> true

# `===` and `!==` are more strict when comparing integers and floats:
    #=> true
   #=> false

# We can also compare two different data types:
  :hello #=> true

# The overall sorting order is defined below:
# number < atom < reference < functions < port < pid < tuple < list < bit string

# To quote Joe Armstrong on this: "The actual order is not important,
# but that a total ordering is well defined is important."

## ---------------------------
## -- Control Flow
## ---------------------------

# `if` expression
 false 
  This will never be seen"

  This will"

# There's also `unless`
unless  
  This will never be seen"

  This will"

# Remember pattern matching? Many control-flow structures in elixir rely on it.

# `case` allows us to compare a value against many patterns:
   
  :four :five ->
    This won't match"
    ->
    This will match and bind `x` to `:two`"
   ->
    This will match any value"

# It's common to bind the value to `_` if we don't need it.
# For example, if only the head of a list matters to us:
    
 #=> 1

# For better readability we can do the following:
  _tail    
 #=> :a

# `cond` lets us check for many conditions at the same time.
# Use `cond` instead of nesting many `if` expressions.
 
       ->
    I will never be seen"
       ->
    Me neither"
       ->
    But I will"

# It is common to see the last condition equal to `true`, which will always match.
 
       ->
    I will never be seen"
       ->
    Me neither"
   ->
    But I will (this is essentially an else)"

# `try/catch` is used to catch values that are thrown, it also supports an
# `after` clause that is invoked whether or not a value is caught.
 
  throw:hello
catch
  message -> message
after
  I'm the after clause."

#=> I'm the after clause
# "Got :hello"

## ---------------------------
## -- Modules and Functions
## ---------------------------

# Anonymous functions (notice the dot)
square   ->    
square #=> 25

# They also accept many clauses and guards.
# Guards let you fine tune pattern matching,
# they are indicated by the `when` keyword:
  
        ->   
    ->   

   #=> 4
  #=> -3

# Elixir also provides many built-in functions.
# These are available in the current scope.
is_number    #=> true
is_listhello" #=> false
  #=> 1

# You can group several functions into a module. Inside a module use `def`
# to define your functions.
defmodule  
     
      
  

   square 
      
  

   #=> 3
square #=> 9

# To compile our simple Math module save it as `math.ex` and use `elixirc`
# in your terminal: elixirc math.ex

# Inside a module we can define functions with `def` and private functions with `defp`.
# A function defined with `def` is available to be invoked from other modules,
# a private function can only be invoked locally.
defmodule PrivateMath 
     
    do_sum 
  

   do_sum  
      
  

PrivateMath     #=> 3
# PrivateMath.do_sum(1, 2) #=> ** (UndefinedFunctionError)

# Function declarations also support guards and multiple clauses:
defmodule Geometry 
   :rectangle   
      
  

   :circle   is_number 
        
  

Geometry:rectangle   #=> 6
Geometry:circle        #=> 28.25999999999999801048
# Geometry.area({:circle, "not_a_number"})
#=> ** (FunctionClauseError) no function clause matching in Geometry.area/1

# Due to immutability, recursion is a big part of elixir
defmodule Recursion 
   sum_list    
    sum_list   
  

   sum_list  
    
  

Recursionsum_list  #=> 6

# Elixir modules support attributes, there are built-in attributes and you
# may also add custom ones.
defmodule MyMod 
  @moduledoc """
  This is a built-in attribute on a example module.
  """

  @my_data  # This is a custom attribute.
  inspect@my_data #=> 100

## ---------------------------
## -- Structs and Exceptions
## ---------------------------

# Structs are extensions on top of maps that bring default values,
# compile-time guarantees and polymorphism into Elixir.
defmodule Person 
  defstruct name:    height: 

joe_info  Person name:    height:  
#=> %Person{age: 30, height: 180, name: "Joe"}

# Access the value of name
joe_info #=> "Joe"

# Update the value of age
older_joe_info   joe_info    
#=> %Person{age: 31, height: 180, name: "Joe"}

# The `try` block with the `rescue` keyword is used to handle exceptions
 
  raise some error"
rescue
  RuntimeError -> rescued a runtime error"
  _error -> this will rescue any error"

# All exceptions have a message
 
  raise some error"
rescue
    RuntimeError ->
    message

## ---------------------------
## -- Concurrency
## ---------------------------

# Elixir relies on the actor model for concurrency. All we need to write
# concurrent programs in elixir are three primitives: spawning processes,
# sending messages and receiving messages.

# To start a new process we use the `spawn` function, which takes a function
# as argument.
   ->     #=> #Function<erl_eval.20.80484245>
spawn #=> #PID<0.40.0>

# `spawn` returns a pid (process identifier), you can use this pid to send
# messages to the process. To do message passing we use the `send` operator.
# For all of this to be useful we need to be able to receive messages. This is
# achieved with the `receive` mechanism:
defmodule Geometry 
   area_loop 
    receive 
      :rectangle   ->
        Area =   
        area_loop
      :circle  ->
        Area =     
        area_loop
    
  

# Compile the module and create a process that evaluates `area_loop` in the shell
  spawn -> Geometryarea_loop  #=> #PID<0.40.0>

# Send a message to `pid` that will match a pattern in the receive statement
  :rectangle  
#=> Area = 6
#   {:rectangle,2,3}

  :circle 
#=> Area = 12.56000000000000049738
#   {:circle,2}

# The shell is also a process, you can use `self` to get the current pid
 #=> #PID<0.27.0>
```

## References

---

Got a suggestion? A correction, perhaps?
[Open an Issue](https://github.com/adambard/learnxinyminutes-docs/issues/new) on the Github Repo, or make a pull request yourself!

Originally contributed by
Joao Marques, and updated by
[10
contributors](https://github.com/adambard/learnxinyminutes-docs/blame/master/elixir.html.markdown)

© 2015
[Joao Marques](http://github.com/mrshankly),
[Dzianis Dashkevich](https://github.com/dskecse)
