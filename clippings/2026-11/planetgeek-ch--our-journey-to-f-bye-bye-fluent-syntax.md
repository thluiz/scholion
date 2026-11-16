---
url: "https://planetgeek.ch/2020/07/16/our-journey-to-f-bye-bye-fluent-syntax"
captured_at: "2026-11-16T04:38:43+00:00"
title: "Our journey to F#: bye-bye fluent syntax"
domain: "planetgeek-ch"
---

In C#, our preferred way to define a builder is using a fluent syntax. Whether it is setting up the system under test in our specifications by defining how we want external calls to be faked, setting up complex test data or defining the steps to be executed in an operation with automatic compensation in case of an exception.

In F#, this works, but feels weird, because a fluent syntax typically uses classes and/or extension methods and there are a lot of `.` involved.

So we experimented with a different style to define the above-mentioned things, and we found a way that better matches our taste of simple code (yes, this post is about taste ![🙂](https://s.w.org/images/core/emoji/17.0.2/svg/1f642.svg) ).

> Update 2020-07-21: Thanks to **Steve Gilham** and his comments, I found a simpler solution to write fluent syntaxes in F#. I’ll write about it in a future blog post and leave this one here as it reflects my learning-curve.

## A fluent syntax in C#

A fluent syntax in C# looks normally something like this:

1

2

3

4

5

`var` `result = Builder`

    `.Run(() =>` `this``.RunFirstThing(firstData))`

    `.Run(() =>` `this``.RunSecondThing(secondData))`

    `.Save(dataToBeSaved)`

    `.Execute()`

A `Builder` is used to define the steps (`Run` and `Save`) that are afterwards executed by `Execute`. Internally, the execute method typically wraps the passed actions or functions with some common code, like error handling and logging. Using this builder prevents code from being repeated and still allows a flexible usage.

## Modelling the steps with discriminated unions

In F#, we switched to a different design for such builders. We use a discriminated union to model the steps and pass them to a function for execution:

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

`type` `Data = ...`

`type` `Steps =`

    `| Run` `of` `unit -> unit`

    `| Save` `of` `Data`

`module` `Runner =`

    `let` `saveData data = ...`

    `let` `execute steps =`

        `for` `step` `in` `steps` `do`

            `match` `step` `with`

            `| Run action -> action ()`

            `| Save data -> saveData data`

`Runner.execute`

    `[`

        `Run (runFirstThing firstData)`

        `Run (runSecondThing secondData)`

        `Save dataToBeSaved`

    `]`

Note that we can specify for every step what data it needs to be executed in the discriminated union case.

## Adding error handling and logging

The common functionality is added in the `execute` function – as it is in C#:

1

2

3

4

5

6

7

8

9

10

11

12

13

14

`module` `Runner =`

    `let` `saveData data = ...`

    `let` `execute steps =`

        `logStart ()`

        `try`

            `for` `step` `in` `steps` `do`

                `match` `step` `with`

                `| Run action -> action ()`

                `| Save data -> saveData data`

            `logSuccess ()`

        `with`

        `| _ ->`

            `logError ()`

            `rollback ()`

## Passing dependencies

If we want to implement meaningful logging and rollback function, we need some more data to be passed to the runner:

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

`type` `Data = ...`

`type` `Saver = ...`

`type` `Steps =`

    `| Run` `of` `unit -> unit`

    `| Save` `of` `(Saver: Saver*Data)`

`module` `Runner =`

    `let` `saveData saver data = ...`

    `let` `execute operationId logger sendRollbackMessage steps =`

        `logger.LogStart operationId`

        `try`

            `for` `step` `in` `steps` `do`

                `match` `step` `with`

                `| Run action -> action ()`

                `| Save saver, data -> saveData saver data`

            `logger.LogSuccess operationId`

        `with`

        `| _` `as` `e ->`

            `logger.LogError operationId e`

            `sendRollbackMessage operationId`

Let’s assume that

*   `operationId` is an unique identifier for the operation executed
*   `logger` is a dependency that provides the logging functionality and knows where to write the logs
*   `sendRollbackMessage` is a dependency that writes a message to a service bus that the operation has to be rolled back.  
    _How we roll back operations in real is a topic of its own._
*   `saver` is a function that knows how to save the data

Dependencies and data that are shared by most steps are passed directly into the `execute` function. Dependencies and data used by single steps are better passed to the step itself.

And our F# runner is finished and can be used like this:

1

2

3

4

5

6

7

8

9

`Runner.execute`

    `operationId`

    `logger`

    `sendRollbackMessage`

    `[`

        `Run (runFirstThing firstData)`

        `Run (runSecondThing secondData)`

        `Save (saver, dataToBeSaved)`

    `]`

Almost as easy to use as the fluent syntax in C#, but with less syntax noise. I write “almost” because IntelliSense can’t quite help as much as with a fluent syntax. But it reads better in my opinion.

## A side note on computation expressions

I found a couple of examples that handle such scenarios with computation expressions and custom operations. We are not using this approach because our runners are nested in `async` workflows, I find nested computation expressions a pain.

## Feedback, please!

You know a better way to achieve the same? Please let me know in the comments!!

Find the next post in this series [here](https://www.planetgeek.ch/2020/07/17/our-journey-to-f-relearning-using-the-ide/).

Find all blog posts about our journey to F# [here](https://www.planetgeek.ch/tag/f-journey/).

[![](https://www.planetgeek.ch/wp-content/uploads/2020/05/timerocket-rocket-1024x992.png)](http://timerocket.ch/)

This blog post is made possible with the support of [Time Rocket](http://timerocket.ch/), the product this journey is all about. Take a look (German only).
