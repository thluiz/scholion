---
url: "https://dev.to/htissink/pseudo-traits-in-c-lnp"
captured_at: "2026-11-16T19:09:54+00:00"
title: "Pseudo Traits in C#"
domain: "dev-to"
---

## [](#c-80-interfaces-are-not-really-interfaces-anymore)C# 8.0 Interfaces _are not really Interfaces anymore_

![alt text](https://i.giphy.com/media/Lkle2NZinkcy3uUG8T/source.gif)

C# 8.0 ships with the wonderfully horrible idea of _interfaces with default implementations_.

First of all I'd like to start by saying that _interfaces with default implementation_ is a terrible idea. An interface is a contract void of implementation and has no place having _default implementation_. This defeats the entire purpose of an interface. What could _possibly_ be better is for the allowance of multiple inheritance of abstract classes. But I digress.

## [](#traits)Traits

![alt text](https://i.giphy.com/media/AAB8uJshCNsuk/giphy.gif)

The idea behind _interfaces with default implementations_ all comes from a programming concept known as a **trait**. A trait is a programming construct that allows you to attach default behaviour to objects, by simply having them _exhibit_ the trait.

You could have traits like `Runner`, `Swimmer`, and `Flyer`.

*   `Runner` would have an implementation for `Running() { ... }`
*   `Swimmer` would have an implementation for `Swimming() { ... }`
*   and `Flyer` would come with an implementation for `Flying() { ... }`.

Now you could simply define a `Penguin` with both the traits `Runner` and `Swimmer` without actually having to write the code for `Swimming()` or `Running()` because by having the traits the functionality is already implemented.

C# really wasn't developed to do this, or at least to do this well. Traits are a more functional construct. A language like `Swift`, with it's `Protocol-Oriented Programming` style, caters to this concept very nicely with `Protocol Extensions`.

Let's take a look at a _creative_ way of doing this in C# 7.0, and I use the term _creative_ very loosely.

## [](#get-schwifty)Get Schwifty

![alt text](https://i.giphy.com/media/fpCa9e3J5YmWc/source.gif)

In `Swift` a `Protocol` behaves very similarly to an `Interface` in C#, and achieves the ability of _traits_ through a `Protocol Extension`. A `Protocol Extension` in _Swift_ should in theory then be similar to an `Interface` extension in C#. This inspired me to try and figure out a way to achieve traits in C#.

Let's create shapes.

*   Some shapes can roll
*   and some shapes can bounce.
*   Some shapes can both roll and bounce.

The Object-Oriented way of implementing this would be to create interfaces for rolling and bouncing.

Any shape that rolls must implement the `rolling` interface, and any shape that bounces must implement the `bouncing` interfaces. Could it perhaps be agreed that rolling and bouncing are not so different for each of the shapes? That a bounce is a bounce and a roll is a roll. And maybe we don't want to go _and implement a bounce or a roll for every single shape we create_.

But wait, you may say, why not just create a `super class` that _rolls_? or a `super class` that _bounces_?

Firstly, **inheritance is bad**. Secondly, are you going to create a super class that rolls, a super class that bounces, and a super class that rolls and bounces? Mmm, if only you had multiple inheritance...

You don't have multiple inheritance with classes - but you _can_ implement multiple interfaces.

So... what do we do now? I hinted at interface extensions, let me explain how it works.

*   disclaimer: this is in **no-way** recommended as a good way of writing code, it is strictly a thought experiment.

## [](#lets-get-cooking)Let's Get Cooking

![alt text](https://i.giphy.com/media/BVXDnwZuSJcqc/giphy.gif)

Let's put together some **trait** boilerplate.  

```
public abstract class Trait { }

interface ITrait<T> where T : Trait { }
```

Enter fullscreen mode Exit fullscreen mode

We have an abstract class `Trait` to be a filter for our **traits**. We never want to implement `Trait` directly, but we sure do want a family of things that are **traits**. The **trait** class will be used when we define the interfaces.

Using an interface is key, because we can implement multiple of them, we can have as many traits as we want.

Next, let's create some traits.  

```
public CanRoll : Trait { }

public CanBounce: Trait { }
```

Enter fullscreen mode Exit fullscreen mode

Again, this is _kind of_ boiler plate. It's the bit of _fluff_ that will allow us to implement magical **traits**.

Finally, lets get to the _juice_.  

```
public static class ShapeTraits
{
    // this only applies to objects that CanBounce
    public static void Bounce(this ITrait<CanBounce> bouncer)
    {
        Console.WriteLine("I can bounce!");
    }

    // this only applies to objects that CanRoll
    public static void Roll(this ITrait<CanRoll> roller)
    {
        Console.WriteLine("I can roll!");
    }
}
```

Enter fullscreen mode Exit fullscreen mode

There it is - our two beautiful **traits** implemented. Next, let's create some shapes.  

```
// A cylinder can roll
public class Cylinder: ITrait<CanRoll>
{
    // this is empty!
}

// A cube can bounce
public class Cube: ITrait<CanBounce>
{
    // this is empty!
}

// And, implementing multiple interfaces,
// a ball can bounce and roll!
public class Ball: ITrait<CanBounce>, ITrait<CanRoll>
{
    // this is empty!
}
```

Enter fullscreen mode Exit fullscreen mode

Now we can create instances of these classes, classes containing no code at all, and because of these _pseudo traits_ they can actually do things!  

```
var cylinder = new Cylinder();
cylinder.Roll(); // this works!

var cube = new Cube();
cube.Bounce(); // this works!

var ball = new Ball();
// a ball that rolls and bounces
ball.Roll();
ball.Bounce(); 
```

Enter fullscreen mode Exit fullscreen mode

![alt text](https://i.giphy.com/media/xT9IgG50Fb7Mi0prBC/giphy.gif)

By using _interface extensions_, we have managed to mimic the ability of **traits**, to create something I call **pseudo traits**. It's a different way of thinking about objects, and I must say I really like it.

You can build extensions methods and hand pick which ones you want to belong to a certain trait. Picking which traits you want on an object allows you to construct an object bit-by-bit, just by implementing the right interfaces.

Is this a good idea? Honestly, I don't know. Is it a fun thought experiment? I definitely think so :\]
