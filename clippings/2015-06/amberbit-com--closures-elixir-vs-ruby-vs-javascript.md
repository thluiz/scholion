---
url: "https://www.amberbit.com/blog/2015/6/14/closures-elixir-vs-ruby-vs-javascript/"
captured_at: "2015-06-14T19:27:54-03:00"
title: "Closures: Elixir vs. Ruby vs. JavaScript"
domain: "amberbit-com"
---

#

##### 2015-6-14

## tl;dr

Closures in Elixir prevent nasty side-effects. Closures in JavaScript
are the worst of the three (suprirse, surprise!). Ruby is slightly better thanks to functional elements in the language, but not perfect.

## The ugly: JavaScript

If you have ever written a piece of JavaScript code, you might come up
the surprising side-effects of closures and mutable state. Most common
*what the heck* moment is when you iterate over an array, and want to
perform some tasks based on current index of element in the array.

```
 functions 
  functionsfunction
    console

functions
functions
functions
```

Let’s run the code:

```
$ node closure
```

Oops. What has happened? Functions in JavaScript save the environment in
which they were defined, so we have access to variable *i* in side of
each function call. This value is, however, being mutated from 0 to 1,
then from 1 to 2, then from 2 to 3. The last value, at which the
condition in the loop stopped being true, is sudenly, and unexpectedly,
printed out by all of the function calls.

Let’s use the standard *hack* to work around the problem:

```
 functions function
    functionsfunction
      console

functions
functions
functions
```

```
$ node closure_fix
```

Better. Sort of. We had to create new context by wrapping the definition
of our anonymous function in another anonymous function, and then,
calling that funkction. Fun, fun, fun.

This is the reason why [every](http://api.jquery.com/jquery.each/)
[single](https://docs.angularjs.org/api/ng/function/angular.forEach)
[JavaScript](http://guides.emberjs.com/v1.10.0/enumerables/)
[framework or library](https://lodash.com/docs#forEach) out there implements some sort of
iterator wrapper, which solves the problem.

## Bakku-shan: Ruby

In Ruby we do not have this problem, right? Let’s write some code to
test:

```
closures 3.times-> puts i 

closurescall
closurescall
closures
```

```
$ ruby closure
```

Alright, let’s move on? Not so fast. The code above only works because
we used nice built-in iterators of the language’s standard library.
Most Ruby developers would write the code using similar techniques, but
we can use bare language constructs to do the same as well:

```
closures while
  closures(-> puts i 

closurescall
closurescall
closures
```

```
$ ruby closure_broken
```

Crap.

## The pretty one: Elixir

Let’s write some code in Elixir:

```
closures |>->

closures
  |>
```

```
$ elixir closure_pretty
```

For those new to Elixir, I am using the *awesome pipe* operator. I think
the official name is *pipe* operator, but it is awesome indeed, so I intend to
keep naming it this way. The operator *|>* allows us to reverse the
method call chain, taking the expression before it and using it as the
first parameter to method call after it. This is so:

```
closures ->
```

becomes:

```
closures |>->
```

This works okay, but one can argue we are using built-in iterators
again. Let’s change that and write most explict code possible:

```
closures 
closures  closures ->puts i 
closures  closures ->puts i 
closures  closures ->puts i closuresclosuresclosures
```

```
$ elixir closure_explict
```

This works! But why? Elixir uses immutable data structures. When we we
assign new value to variable *i*, we are not changing the variable
value (I know, I know, this is pattern matching not
normal assignment). You can explain the behavior by assuming the
*i=1*, *i=2* and *i=3* are effectively creating new variable *i* in the
current scope. Our functions reference the the values with the same
label *i*, but the values stay unchanged, when the variable is re-used
later on.

When you think about it, it really makes a lot of sense to define
closures this way. This default behavior can help you stay away from a
lot of trouble in single-threaded code, not to mention multi-threaded
applications.

## Summary

Always use iterators when they are available, if you are writing
JavaScript and Ruby code. If you embrace some of the functional
programming patterns in your daily coding style, you can save yourself
some headaches. Learn Elixir. ;)

by Hubert Łępicki, twitter: [@hubertlepicki](http://twitter.com/hubertlepicki)
