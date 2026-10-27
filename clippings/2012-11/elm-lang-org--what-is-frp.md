---
url: "http://elm-lang.org/learn/What-is-FRP.elm"
captured_at: "2012-11-05T13:44:55-03:00"
title: "What is FRP?"
domain: "elm-lang-org"
---

[**Elm**](http://elm-lang.org/)

About

Examples

Docs

Download

## What is “Functional Reactive Programming”?

Functional Reactive Programming (FRP) allows rich interaction in a functional setting. It answers the question, “How can I handle user input and update a GUI in a functional way?” FRP ends up making it much easier to create interactive GUIs and to work with complex sequences of synchronous and asynchronous events. Its ideas can be valuable in an imperative setting too [[1]](http://en.wikipedia.org/wiki/Dataflow_programming "Dataflow Programming") [[2]](http://en.wikipedia.org/wiki/Reactive_programming "Reactive Programming").

FRP comes down to one simple idea: *some values change over time*. In FRP, these time-varying values are called *signals* and they update automatically.

You can see some signals in action in the colorful box to the right. Take a second to play around with each of the examples. Try to make them change and guess what they do.

The first example is the position of the mouse. In Elm, the mouse position is represented by a signal named `Mouse.position`. When the mouse moves, the value of `Mouse.position` changes automatically [[3]](http://elm-lang.org/edit/examples/Reactive/Position.elm "mouse").

The `Window.dimensions` signal works exactly the same way, automatically changing whenever the window is resized [[4]](http://elm-lang.org/edit/examples/Reactive/ResizePaint.elm "dimensions").

The third example uses the `count` function which counts the number of times a signal is updated. In this case we are counting mouse clicks.

**Source Code**

**Value**

Mouse.position

(1648,1351)

Window.dimensions

(1903,976)

clks = count Mouse.clicks

0

lift (\n -> n^2) clks

0

In the fourth example we square the number of clicks. The `lift` function is used to “lift” a normal function onto a signal. Once lifted, a function is applied automatically whenever the signal updates. So if the function produces static graphics, [lifting it onto a signal produces an animation](http://elm-lang.org/edit/examples/Reactive/Clock.elm "animation")!

These examples are just the basics of FRP. There are tons of other [interactive examples](http://elm-lang.org/examples/Basic.elm) that allow you to play around with FRP in [Elm](http://elm-lang.org/). More information on how to use signals can be found [here](http://elm-lang.org/docs/Signal/Signal.elm).

FRP becomes truly powerful when paired with a good [graphics library](http://elm-lang.org/docs/Graphics/Element.elm), making it possible to create interactive pages such as the one you are currently looking at ([interactive source](http://elm-lang.org/edit/learn/What-is-FRP.elm)) or design purely functional games ([Creating purely functional Pong](http://elm-lang.org/blog/games-in-elm/part-0/Making-Pong.html))

---

## Combining Signals

FRP is also great for working with multiple signals. This means you can combine multiple event sources really easily.

The following examples start to get fancy with the `Mouse.position` signal. Take a look and try to figure out what they do.

**Source Code**

**Value**

lift2 (/) Mouse.x Window.width

0.8660010509721492

sampleOn Mouse.clicks Mouse.position

(0,0)

keepWhen Mouse.isDown (0,0) Mouse.position

(0,0)

The first example shows how you combine two different signals. In this case we finding out the x-coordinate of the mouse as a percentage of screen width. So we can know that the mouse is 75% of the way accross the screen.

The second example produces a signal of click locations. The `sampleOn` function allows you to “sample” a signal whenever a particular signal updates.

In the third example, we keep the mouse position when the mouse is down. The resulting signal updates only when the mouse is dragged.

The `keepWhen` function takes three args: a signal of booleans, a default value, and a signal of anything. It returns a signal that only updates when the first signal is true. The default value is needed in case the first signal is *never* true. This ensures that the resulting signal always has a value.

Again, this stuff becomes even cooler when you mix it with a good graphics library!

---

## “Why is FRP a good idea?”

Functional reactive programming (FRP) is a *declarative* approach to GUI design. The term *declarative* makes a distinction between the “what” and the “how” of programming. A declarative language allows you to say *what* is displayed, without having to specify exactly *how* the computer should do it.

The term declarative is important only because most current frameworks for graphical user interfaces are *not* declarative. They mire programmers in the many small, nonessential details of handling user input and manually modifying the display.

So with FRP, many of the irrelevant details are left to the compiler, freeing the programmer to think about things that matter. That means no event handlers, no callbacks, no DOM manipulations. These things simply are not necessary with FRP in Elm.

Coding these examples in a traditional GUI framework – such as HTML/CSS/JavaScript – would require significantly more work and headache. Imagine manually extracting the mouse position from an event, adjusting the value to deal with cross-browser incompatabilities, finding a node in the DOM based on its ID, and finally describing exactly how to destructively modify that node. Not only is that painful to code, but it also requires broad and deep knowledge of inconsequential things.

FRP makes tasks considerably easier by taking care of the messy “how” of events, display, and updates.

© 2011-2012 [Evan Czaplicki](https://github.com/evancz)
