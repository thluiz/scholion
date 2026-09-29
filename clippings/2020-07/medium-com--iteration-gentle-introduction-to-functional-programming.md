---
url: "https://medium.com/@BeardedTim/iteration-a-gentle-introduction-to-functional-programming-c59fcb0ab58d"
captured_at: "2020-07-12T10:33:39-03:00"
title: "Iteration: A Gentle Introduction to Functional Programming | by Tim Roberts | Medium"
domain: "medium-com"
---

# Iteration: A Gentle Introduction to Functional Programming

![1*P1LvPSR42ykC4g5IyO2XGA.jpeg](medium-com--iteration-gentle-introduction-to-functional-programming/fa78a94798cbce61fa65794f3411dcac.jpeg)

Supersonic Speed — Claus Tom Christensen (CC BY-NC-ND 2.0)

> The function of a computer is to manipulate information, […which is] fundamentally a matter of transformation
>
> Joseph Weizenbaum | [Computer Power and Human Reason](https://www.amazon.com/Computer-Power-Human-Reason-Calculation/dp/0716704633)

In Javascript understanding functional programming is becoming a necessity to quickly on-board and become productive thanks to React and Flux. But with [Monad](https://github.com/fantasyland/fantasy-land#monad) and [Setoid](https://github.com/fantasyland/fantasy-land#setoid) groups, being able to grok FP concepts seems like a monumental task. In order to see the beauty of functional programming, let’s forget what we have heard about it and instead focus on a problem we need to solve in code and see how we can add functional programming ideas and concepts to help.

One of our tickets is to build an application that, given a list of people, will print out their names. Doing just enough to get it to pass tests, we come up with the following solution:

We create a `for` loop to go through the `list` , grabbing the `person` from the list, and printing their `name` property. This works for the predefined value `list` but what if we wanted to make it work for any `array` ?

We can wrap the `for` loop in a function and tell our worker that we will at some point in the future know what `list` is, like so:

Notice that all we did was move the `for` logic inside of a closure. We hid away the implementation details of how we iterate and print a list of names and named it something very descriptive, `printNames`, so that when we use it later on ( `printNames(myList)` ), we know *what* it does without needing to know the details of *how.*

We send the above code to our team lead and everyone is happy that they can use our function `printNames` anywhere they need to iterate over a list and print the `name` property of every object. But soon someone says “I want it to print their `age` instead of their `name` .” How would we do that?

Our first approach could be to copy the code of `printNames`, change `person.name` to `person.age` and call it a day. But this breaks the [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) principle. We can see that `printNames` and `printAges` are basically the same *idea* but different *expressions* of that idea. To see what I mean, let’s describe our tasks in terms of our worker and instructions instead of code and logic.

For `printNames`, we are wanting to tell our worker: `Given a list, I want you to iterate through the list, grab the current item from the list, and print the name property`.

For `printAges`, we are saying: `Given a list, I want you to iterate through the list, grab the current item from the list, and print the age property`.

We see that those two instructions are nearly identical. To put it a different way, the steps involved in solving both of these problems are the same, it is the instructions to follow during those steps that change. Much like in our first example where we put the `for` loop inside of a function, we are keeping the overall *how* the same and only changing the *what.*

Knowing the above, let’s revisit `printAges` . In an abstract way, what we are trying to say is ‘*For each items in a given list, perform some function*’. Knowing that and stealing as much code as we can from `printNames`, we come up with:

We have created a way to describe to our worker *how* to do something instead of specifically *what* to do. All is right in the world and we get another PR merged.

A few tickets go by and during a code review we notice the following code:

We see an emerging pattern that our `forEach` function is being used for. Instead of simply *doing* something during each iteration, the above code is *creating* something. Not only that, it is dependent on state in an *implicit* manner.

What do I mean by implicit? With the above code, we are telling our worker that we will make sure it has all of the pieces, outside of its own world, in the correct place and labeled the correct name. Suppose that instead of the array being labeled `ages` we wanted it to be labeled `personAges`. What would happen when we call `forEach(addToAges, list)` ? What would we have to do in order to keep the contract with our worker that we will provide the necessary state outside of itself in order for it to function properly?

In the above, we would have to change the name for `ages` or `names` in two places which luckily are defined near each other. In a real code base, with thousands of lines of code, the implicit dependency between the function and the array might not be as clear. How can we make the dependency on the array *explicit?* Better yet, how can we describe the above without needing to know *how* it worksand instead it Just Works? Like `forEach`, let’s try to define the *what* in an abstract way:

*Iterate over a list and create a new list by transforming the values at each index.*

Luckily for us, we already have this idea done, we just need to wrap it in a function like we did with `forEach` :

Notice how we are assigning the result of `map` to the `names` array instead of using `map` to affect the array. We have removed the *implicit* nature of the instruction and instead made it *explicit* that we are creating a new array from a list of values. But we still are repeating ourselves in the above code and breaking the DRY principle that started this journey.

On lines 10 and 12 above, we are defining `getName` and `getAge` as functions that, given an object, return the `name` and `age` property respectively. Just like before, let’s describe those instructions in an abstract way:

*Given an object, return the property X*

How can we describe to our worker the idea of grabbing some property off of an object without knowing the property name or the object itself? Just like we did with `map` or `forEach`: abstracting the *how* from the *what:*

```
const prop = (key, obj) => obj[key];
```

We want to grab some property, *key,* for a given object, *obj.* We can use the above to grab the `name` , `age`, or any other property from an object and it works exactly how we need it to. But when we try to use it inside of our `map` function, we run into an issue.

`map` is expecting some function that, given a single value, will return some value. `prop` is a function that, given two values, returns a value. How can we use `prop` inside of `map`? One way would be to re-write `map` to take in a `key` value but then we are tying `map` to the *idea* of `prop`. What we’re wanting is a way to give `prop` half of the information now, or *partially apply* it, and later have `map` give the rest of the information. Toying around with the idea, we create the following:

```
const prop = key => obj => obj[key];
```

Now, when we call `prop('name')`, the resulting value *is a function*. We can pass that function to `map` and be given the rest of the information. Just like we did with `printNames`, we are enclosing some information inside of a closure for our worker to use later on. Instead of our worker being dependent on outside information *implicitly*, it is dependent on the values that we give it along the way *explicitly*.

Using the above, let’s re-write how we get the names and ages:

Or to make the fact that `prop('name')` is a function even more explicit:

Similarly to how we *partially applied* `prop` and tied getting a given key to a function, we can *partially apply* `map` and tie a transformation function to it:

What if we sometimes want to call `map` or `prop` at times with all of the arguments and at other times feed them one at a time? For that, we’d need to create a helper function called `curry` , which naively looks something like this:

`curry` is a function that takes a function as an argument and then keeps returning functions until it is given all of the expected arguments.

The above shows how functional concepts like `functional transparency` and `immutability` apply to actual problems we face in our day to day tasks as developers. What the above doesn’t show, however, is how it makes it any easier on ourselves than using imperative or object-oriented. To see how functional programming shines there, we need to use a different definition of `iteration`: development iteration.

Being able to quickly iterate on an idea is the quintessential requirement for creating a product that sells. As Jamie Zawinski said:

> If you spend the time to build the perfect framework…release 1.0 is going to take you three years to ship and your competitor is going to ship their 1.0 in six months and now you’re out of the game [because] someone else ate your lunch.

So how is it that functional programming helps us iterate more quickly on ideas? How can we ship v1 faster than our competitors that are using imperative or object oriented? First, we’re going to need one more helper function, `compose` that meets the following requirements:

Given *n* functions to start, we return a function that is expecting the initial value to start the calling with. Once given the initial value, it calls each function in reverse order passing it the previous result.

To see how we can use it, let’s look at a simple example:

Given the `compose` function, we finally have all of the pieces we need to see how easy it is to compose and extend functionality inside of a functional codebase. Building our application as small, composable functions like `prop`, `curry`, and `uppercase` we are free to solve the specifics of our domain ( *formatting a name* ) using common and shared methods. We have freed our solutions from the specifics of our problem and can instead focus on building lego pieces for other parts of our application to use.

Further, testing each of these functions becomes trivial: everything is based on the given input so we can test each function as a *unit* and know for certain that used anywhere it will behave as expected.

But how does it help you be more productive? By allowing us to reach the holy grail of programming: reusability. Joe Armstrong talks about how object-oriented programming languages [lack reusability](https://www.johndcook.com/blog/2011/07/19/you-wanted-banana/), about how you find yourself locked into a corner while trying to share solutions across instances or projects. However, looking at the above we can see that every function is dependent solely on its input and only cares about its output.

Once we have these lego pieces and need to solve domain specific problems, we can *compose* functions together, piping one function output into the next.
