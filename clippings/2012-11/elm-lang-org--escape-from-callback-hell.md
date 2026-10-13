---
url: "http://elm-lang.org/learn/Escape-from-Callback-Hell.elm"
captured_at: "2012-11-05T13:45:34-03:00"
title: "Escape from Callback Hell"
domain: "elm-lang-org"
---

[**Elm**](http://elm-lang.org/)

About

Examples

Docs

Download

Escape from Callback Hell

*Callbacks are the modern `goto`*

Callbacks are used to structure programs. They let us say, “When this value is ready, go to another function and run that.” From there, maybe you go to *another* function and run that too. Pretty soon you are jumping around the whole codebase.

If you have worked with [AJAX](http://en.wikipedia.org/wiki/Ajax_(programming) "AJAX") or [node.js](http://nodejs.org/ "node.js") or any other callback heavy framework, you have probably been to Callback Hell. Your whole application ends up being passed around as callbacks, making the code extremely difficult to read and maintain. The resulting tangled mess of code is often pejoritively called [spaghetti code](http://en.wikipedia.org/wiki/Spaghetti_code "Spaghetti code"), a term borrowed from the days of `goto`.

Just like `goto`, these callbacks force you to jump around your codebase in a way that is really hard to understand. You basically have to read the whole program to understand what any individual function does.

And good luck if you want to add something to your code. A change in one function may break functions that *appear* to be unrelated (the functions may never even appear together in the entire codebase, connected only by deeply nested callbacks). You'll usually find yourself carefully tracing through the entire sequence of callbacks to find out what your change will really do.

If you are not convinced that callbacks and `goto` are equally harmful, read Edsger Dijkstra's famous [“Go To Statement Considered Harmful”](http://www.u.arizona.edu/~rubinson/copyright_violations/Go_To_Considered_Harmful.html "goto") and replace the mentions of `goto` with mentions of callbacks.

Okay, so there are a lot of things to dislike about callbacks, but they *do* serve a vital role in modern programs. In an effort to reach a better solution we must ask: why do we *really* need callbacks? What task do they perform? What is their fundamental role in our programs?

Well we often want to say, “When this value is ready, take this action.” This is a time-dependent relationship. We depend on a value as it changes over time. We also want to say, “While this is happening, that can happen too.” This is a time-dependent relationship too. These computations can happen concurrently. These time relationships are not covered by traditional control structures, so we use the modern `goto` to work around it.

## A Preview of the Solution

Just like `goto`, callbacks lead to non-linear code that is hard to read, maintain, and understand. And just like with `goto`, this problem can be solved by introducing higher level control flow mechanisms. So if you want to escape from Callback Hell, you need to understand [Functional Reactive Programming](http://elm-lang.org/learn/What-is-FRP.elm "FRP") (FRP). In short:

[goto](http://www.u.arizona.edu/~rubinson/copyright_violations/Go_To_Considered_Harmful.html "goto")   **:**   [structured programming](http://en.wikipedia.org/wiki/Structured_programming "Structured Programming")   **: :**   [callbacks](http://en.wikipedia.org/wiki/Callback_(computer_programming) "Callbacks")   **:**   [reactive programming](http://elm-lang.org/learn/What-is-FRP.elm "FRP")

“The unbridled use of the go to statement has an immediate consequence that it becomes terribly hard to find a meaningful set of coordinates in which to describe the process progress.”

[Edsger Dijkstra](http://www.u.arizona.edu/~rubinson/copyright_violations/Go_To_Considered_Harmful.html "goto")

[Functional Reactive Programming](http://elm-lang.org/learn/What-is-FRP.elm "FRP") (FRP) is a high-level framework for describing time-dependent relationships. FRP formalizes these time-dependencies, resulting in simple syntax and semantics.

FRP lets you make asynchronous calls without the callbacks. Without the non-linear control flow. Without the headache. You can write code that is both readable *and* responsive.

To understand the existing problem and how it is solved with FRP, let's make this more concrete. The following example will explain the current state of affairs and fully explain how to create readable, responsive code that is entirely free of callbacks.

“For a number of years I have been familiar with the observation that the quality of programmers is a decreasing function of the density of go to statements in the programs they produce.”

[Edsger Dijkstra](http://www.u.arizona.edu/~rubinson/copyright_violations/Go_To_Considered_Harmful.html "goto")

## Case Study: Using the Flickr API

Flickr – a photo sharing service – exposes an [API](http://www.flickr.com/services/api/ "Flickr API") that allows you to programmatically find and download photos. We want to find an image with a user defined tag. So if I ask for “Tokyo” I should get back a random image with a Tokyo tag.

This requires two explicit HTTP requests to Flickr, one to find some tagged photos and another to get the size options for a given image.

We will perform this task three ways: synchronously, asynchronously with callbacks, and asynchronously with FRP.

#### 1. Readable but Unresponsive

First let's do this with synchronous HTTP requests. We will rely on a couple of functions specified to the right. Here is our code:

```
    function getPhoto(tag) {
        var photoList  = syncGet(requestTag(tag));
        var photoSizes = syncGet(requestOneFrom(photoList));
        return sizesToPhoto(photoSizes);
    }

    drawOnScreen(getPhoto('tokyo'));
```

It's pretty clear what is going on here. The `syncGet` function takes a request and blocks until it receives a response. The logic of the program is simple and linear. If you wanted to add anything, it is pretty obvious where it would go. You never have moments where you need a value but it does not exist yet.

This code is really nice to read, but it will make your whole application freeze for the duration of the HTTP requests. It basically dodges the issue of time-dependence by just freezing if it is waiting for a value. This blocks everything in the program. Mouse and keyboard input just piles up, waiting to be processed, presenting the user with an unresponsive app. This is not an acceptable user experience.

#### 2. Responsive but Unreadable

The current solution is to instead make asynchronous HTTP requests (AJAX requests) that use callbacks that give finer-grained control over time-dependencies.

```
    function getPhoto(tag, handlerCallback) {
        asyncGet(requestTag(tag), function(photoList) {
            asyncGet(requestOneFrom(photoList), function(photoSizes) {
                handlerCallback(sizesToPhoto(photoSizes));
            });
        });
    }

    getPhoto('tokyo', drawOnScreen);
```

The `asyncGet` function takes a request and a callback to run once a response is received. We can now say, “These computations must happen one after another, but other things can happen in the meantime.”

Yay, we solved the problem of the site freezing, but now our code is a mess of deeply nested functions that is annoying to write and unpleasant to read and maintain. This is a glimpse into Callback Hell.

We have effectively done a manual conversion to [continuation passing style (CPS)](http://matt.might.net/articles/by-example-continuation-passing-style/ "cps"), a common compiler technique for functional languages.

CPS is great for compilers because it is easy to map onto assembly-level jumps (i.e. `goto`), helping [make functional languages efficient](http://matt.might.net/articles/cps-conversion/ "Compiling with Continuations")! CPS is terrible for humans for the same reason. It is pretty much the same as using `goto` to structure your programs.

**Function Specifications**

`requestTag` which turns a tag – such as `"badger"` – into a valid Flickr API request. These requests will return a JSON object containing a list of `"badger"` photos.

`requestOneFrom` takes a JSON object of photos and turns it into a request for just *one* photo. This request will return a JSON object of size options. Flickr is basically asking, “Do you want low resolution? Original quality? 800 by 600? ...” This function also handles any errors that might have occured with the previous request.

`sizesToPhoto` turns a JSON object of sizes options into an actual image that we can use. Again, this function handles any errors that might have occured with the previous request.

`drawOnScreen` puts the image on screen for the user to see. You do not need to mess around with the DOM in [Elm](http://elm-lang.org/), so this function only gets used in the JS code.

#### 3. Readable *and* Responsive

[Functional Reactive Programming](http://elm-lang.org/learn/What-is-FRP.elm "FRP") uses *signals*, values that change over time, to represent all interactive time-varying content. For example, the value of a text input field is a “signal” because it changes over time. We can create such a signal with:

```
    (inputField, tags) = Input.textField "Tag"
```

This creates two values. The first is a visual element called `inputField` that users can type into. This is a normal text box. The second is a signal called `tags`. The value of `tags` changes automatically as the user types into `inputField`. Here are the `inputField` and the `tags` signal in action. Try typing into the input box to see `tags` update automatically.

[]

We can then do all sorts of computations with `tags`. When `tags` changes the signals that depend on it change automatically:

lift length tags

0

lift reverse tags

[]

lift requestTag tags

[]

The `lift` function is used to transform a signal. It takes functions such as `length`, `reverse`, or `requestTag` and applies them to a signal. This lets us create new signals that automatically change whenever `tags` changes.

We are particularly interested in the third signal we created. The code `(lift requestTag tags)` produces a Flickr request that corresponds to the current user input (abbreviated for the sake of presentation). Now we just need to send this request! For this we use the `send` function:

send (lift requestTag tags)

Waiting

Notice that when `tags` changes, the result of `send` does *not* change immediately. The responses are sent and received asynchronously, so a response only arrives when it is ready. In the meantime, your program is free to go about its normal business.

This is great because it allows us to have asynchrony without leaving the conceptual framework of signals. The response is just another signal, exactly the same as `tags`. We can turn its values into requests and send them too. In fact, that's exactly what we are going to do. Here is the full Elm code for making many requests to the Flickr API:

```
    getPhotos tags =
        let photoList  = send (lift requestTag tags) in
        let photoSizes = send (lift requestOneFrom photoList) in
            lift sizesToPhoto photoSizes
```

We have effectively set up a processing pipeline of how to handle user input: we take in a tag, turn it into a request, send it, turn the response into a new request, send it, and finally turn *that* response into an image!

We have clear, linear control flow, and the resulting program automatically optimizes for asynchrony. It does not block while waiting for a response and our program is still well defined. We now have the readability of synchronous code with the efficiency of asynchronous callbacks. There is no trade-off between readability and responsiveness!

And because it is so easy to work with graphics in Elm, we can create a workable Flickr search interface with only four additional lines of code! The [full source code and interface can be seen here](http://elm-lang.org/edit/examples/Intermediate/Flickr.elm "Flickr API Example"), with a more idiomatic implementation of `getPhotos` that takes only one line. Take a look! All of the graphics code lives in the definition of `scene`, taking up a grand total of two lines. All told, [the core logic](http://elm-lang.org/edit/examples/Intermediate/Flickr.elm "Flickr API Example") is seven lines from start to finish.

In fact, here is an abbreviated version that fits in this blog post:

```
    scene img = flow down [ container 300  60 middle inputField
                          , fittedImage 300 300 img ]

    main = lift scene (getPhotos (dropRepeats tags))
```

In `scene` we stack two elements vertically so that they flow downward. The first one is a 300 by 60 container with our `inputField` text field right in the middle. The second is an image that is automatically cropped to fit nicely in a 300 by 300 square. The `main` function is what actually gets put on screen. The only new thing in this line is `dropRepeats` which filters out any values that are repeated, cutting down the number of HTTP requests we make. The result looks like this:

Your browser does not support the canvas element.

## Conclusions

Callbacks are the modern `goto`. Callbacks result in non-linear code that is hard to read, maintain, and understand. Functional Reactive Programming introduces high-level control structures that let you easily express time-dependencies. The resulting code is both readable, responsive, and significantly more concise.

Signals can express [many different time-relationships](http://elm-lang.org/docs/Signal/Signal.elm "Signal Docs"), such as dependence on the [present](http://elm-lang.org/edit/examples/Intermediate/Clock.elm "Clock") or [past](http://elm-lang.org/edit/examples/Intermediate/Stamps.elm "Stamps"), time-sensitive [sampling](http://elm-lang.org/edit/examples/Reactive/SampleOn.elm "sampleOn") and [filtering](http://elm-lang.org/edit/examples/Reactive/KeepIf.elm "keepIf"), and [asynchrony](http://elm-lang.org/edit/examples/JavaScript/ZipCodes.elm "Zip Codes"). This makes it much easier to deal with complicated time-dependent interactions, a task that is extremely common when designing user interfaces.

Look out for an upcoming post on **integrating Elm with JS code**. This post will show how Elm can be used to handle your time dependent logic without disrupting an existing codebase. So you can use FRP to escape Callback Hell and still directly use JavaScript, JQuery, Bootstrap, or any other existing web technology. Until then, you can read up on the [JavaScript Event Interface](http://www.testblogpleaseignore.com/2012/06/29/announcing-elm-0-3-5-javascript-integration-signal-filters-and-more/ "JavaScript Event Interface") which makes this all possible.

If you interested in this approach, [download Elm](https://github.com/evancz/Elm/blob/master/README.md#elm "Dowload") or [experiment online](http://elm-lang.org/edit/examples/Basic.elm)! Elm is only at version 0.5, but it already has lots of great [libraries](http://elm-lang.org/Documentation.elm). If you feel like there are some libraries or features missing, [you can help add them](http://elm-lang.org/Contribute.elm).

If you have questions or want to learn more, there are lots of helpful resources. This [thesis](http://www.testblogpleaseignore.com/wp-content/uploads/2012/04/thesis.pdf "thesis") has much more information on how asynchrony works in Elm. It also describes the history of FRP. It is quite accessible even if you do not have any experience reading academic papers. You can also email [the list](https://groups.google.com/forum/?fromgroups#!forum/elm-discuss "elm-discuss") or ask questions on the [#elm channel at freenode](http://webchat.freenode.net/?channels=elm "#elm channel").

© 2011-2012 [Evan Czaplicki](https://github.com/evancz)
