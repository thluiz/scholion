---
url: "http://www.pirrmann.net/making-program-behaviour-explicit/"
captured_at: "2026-09-27T00:43:56+01:00"
title: "Making program behaviour explicit | Pirrmann's train of thought"
domain: "pirrmann-net"
---

![](http://www.pirrmann.net/wp-content/uploads/2016/04/FSM.jpg)When observing developers in their day-to-day work, it’s quite usual to see them swearing at their programs, because they don’t behave as they should. You often see them asking the program to obey, sometimes cursing, and even praying from time to time. If we take some time to think about it, the main reason why a programmer shouts at a running program is because it doesn’t quite behave as he/she wants it to do. Unfortunately, this is less common in the functional programming community. Having a language that promotes usage of immutability and option types (to name only a few), sometimes deprives you of cursing and praying.

Fortunately, F# has a feature called computation expressions, that can bring you back the joy of an unpredictable behaviour at runtime! I hope you’ll enjoy the ones I’m going to introduce today. For instance, they allow you to write the following code:

`let` `theAnswer = usually {` `return` `42 }`

`let` `basicArithmetic = mostProbably {` `return` `6 * 7 }`

As those samples clearly state, they _usually_ and _mostProbably_ behave as expected. However, they sometimes do slightly different things. Indeed, the computation expressions are sometimes mutated, and then evaluate to something else. Using this, you can cause _subtle bugs_, that _only occur from time to time_, deep inside more complex computations. And as you can expect, the debugging experience will be completely awful.

That’s a nice first step. But didn’t I mention cursing an praying? Stay tuned. Using a combination of custom operations and mutable state (ouch!), this is perfectly valid code:

`pray God {`

    ` ``The lord is my shepherd`` `

    `let` `x = 6`

    ` ``He led me ` `in` `the paths` `of` ` righteousness`` `

    `let` `y = 55`

    ` ``Whoever walks ` `in` ` integrity walks securely`` `

    `let` `z = 2`

    ` ``But whoever takes crooked paths will be found out`` `

    ` ``I walk through the valley ` `of` `the shadow` `of` ` death`` `

    `return` `(y * z + 1) * x`

`}`

And it comes in different flavours, you can pray your own favourite god if you wish:

`pray FlyingSpaghettiMonster {`

    ` ``I believe Thou art the Creator ` `of` `Goodness` `and` ` Nourishment`` `

    `let` `x = 1`

    ` ``I believe that Thou are neither Male, nor Female`` `

    `let` `y = 2`

    ` ``I thank Thee ` `for` `the giving` `of` ` healthful Green Salad`` `

    `let` `z = 3`

    ` ``R'amen`` `

    `return` `x + y - z`

`}`

In the previous samples, you compose a prayer, that will change the mood of the god who listens to it:

*   in the default state, there is a small chance that mutation occur in the expressions,
*   when the god is pleased, the code is safe and no mutation occurs,
*   when the god is angry, expect numerous mutations.

Of course, using a sentence which is not intended for the right god will trigger mutations.

So how do we build this? Computation expressions are in most cases just used as syntactic sugar that allows you to bind continuation functions to a given state (as very well explained [on fsharpforfunandprofit](https://fsharpforfunandprofit.com/series/computation-expressions.html)). But you can also use computation expressions to get a [quotation](https://msdn.microsoft.com/en-US/library/dd233212.aspx) of the expression. This is what’s behind the [cloud expression offered by MBrace](http://mbrace.io/programming-model.html#Cloud-Workflows).

Once given an expression, you can manipulate it to build a new derived expression. In the end, in order to evaluate the expression, I’ve used the evaluator packaged in [Unquote](http://www.swensensoftware.com/unquote). In the end, the computation expression builder class is almost empty:

`type` `ChaosBuilder (mutationSitePicker:IMutationSitePicker,`

                   `expressionReplacer:IExpressionReplacer) =`

    `member` `this.Return(x) = x`

    `member` `this.Quote (expr) = expr`

    `member` `this.Run (expr:Expr<'T>) =`

        `let` `choaticExpr =`

            `mutate mutationSitePicker expressionReplacer expr`

        `choaticExpr.Eval<'T>()`

The IMutationSitePicker is responsible for choosing a site, ant the IExpressionReplacer actually performs the expression maniputation. Here is a sample implementation that give every eligible expression a random chance to be replaced:

`type` `MutateWithProbability(proportion) =`

    `let` `r =` `new` `System.Random()`

    `let` `mutable` `lastRandom = r.NextDouble()`

    `interface` `IMutationSitePicker` `with`

       `member` `this.PickNextSite = lastRandom < proportion`

       `member` `this.NotifyIgnoredSite() = lastRandom <- r.NextDouble()`

       `member` `this.NotifyMutation() = lastRandom <- r.NextDouble()`

I’m not going to include the actual expression manipulation code here, but my current work on this very valuable feature is [available as a Gist](https://gist.github.com/pirrmann/aeef0b53362e84abe4ca9c1f69485c8e). Implementing computation expressions which allow (and encourage) cursing is left as an exercise to the reader.

Some of the code used here could actually be used to perform [mutation testing](https://en.wikipedia.org/wiki/Mutation_testing). the only replacement implemented so far is numeric constants mutation, but there are many other kinds of fun mutations to add (see [Mutation Testing of Functional Programming Languages](http://web.engr.oregonstate.edu/~alipourm/pub/fp_mutation.pdf) for instance) such as “replacing an arithmetic, relational, logical, bitwise logical \[…\] operator by another of the same class”, “Reordering Pattern Matching”, and even “Type-aware Function Replacement”.

As a conclusion, I want to say that even if I often abuse computation expressions to do stupid things, they’re a really powerful feature of the F# language and really allow to write cool DSLs.

EDIT: I’ve implemented the arithmetic operator replacement in the train this morning, the gist has been updated.
