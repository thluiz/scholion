---
url: "http://www.pirrmann.net/f-sharp-i-love/"
captured_at: "2026-09-27T00:48:23+01:00"
title: "F# |> I <3 | Pirrmann's train of thought"
domain: "pirrmann-net"
---

![](http://www.pirrmann.net/wp-content/uploads/2014/04/fsharp-pipe-i-love.jpg)

I’ve been writing about F# for a little while now, and how it has influenced the way I code in C# on an everyday basis for 3 years. During the last couple weeks, I’ve finally had the chance to use F# at work for a real project (I’ll probably talk about that later). Yesterday evening (Europe time) at Build, Roslyn was open-sourced. That’s nice and people are probably going to talk about it for a while. But for me there was another very nice announcement : Visual F# is now taking contributions! F# is already an exciting language, full of clever features. With this new step, I’m convinced that it will go even further and I’m already looking forward to F# 4.0!

So don’t expect to see many more posts about C# on this blog, I’ve totally gone F#.

And now, the latest sample from Arolla’s Code Jam. The aim was to write code to express values with a range of uncertainty, and operations which manipulate those numbers. For instance, a value 3.5 +/- 0.5, multiplied by 1.0 +/- 0.1. The goal of the kata was to write code that expresses intent (the why), and not implementation details (the how).

In F#, I’ve just defined a type to wrap both the value and its precision, and an operator to conveniently build those values :

`type` `Number = | Number` `of` `float * float`

`let` `(+-) n a = Number (n, a)`

This code alone already allows me to build values just by writing expressions such as “4.0 +- 1.0”. The next step for me was to write some expressive tests, using FsUnit.

`let` `[<test>] ``A number` `with` `accuracy is equal` `to` `itself`` () =`

    `(1.0 +- 0.5) |> should equal (1.0 +- 0.5)`

`let` `[<test>] ``Sum` `of` `two numbers sums the numbers` `and` `accuracies`` () =`

    `((5.0 +- 0.5) + (3.0 +- 0.5)) |> should equal (8.0 +- 1.0)`

Although we could handle distinctly every operator with specific logic, the goal of this kata is to express the intent in a generic fashion, so here is a combine method that has no specific meaning of what an operator does:

`let` `combine op (Number(n1, a1), Number(n2, a2)) =`

   `let` `all =`

      `seq {`

         `for` `x` `in` `[n1-a1; n1+a1]` `do`

         `for` `y` `in` `[n2-a2; n2+a2]` `do`

         `yield` `op x y`

      `}`

   `let` `minimum = all |> Seq.min`

   `let` `maximum = all |> Seq.max`

   `Number((minimum + maximum) / 2.0, (maximum - minimum) / 2.0)`

Finally, we just have to add operator overloading to the type, the full code becomes:

`type` `Number = | Number` `of` `float * float`

    `with` `override` `x.ToString() =` `match` `x` `with` `| Number(a, b) -> sprintf` `"%f +- %f"` `a b`

         `static` `member` `private` `combine op (Number(n1, a1), Number(n2, a2)) =`

            `let` `all =`

                `seq {`

                    `for` `x` `in` `[n1-a1; n1+a1]` `do`

                    `for` `y` `in` `[n2-a2; n2+a2]` `do`

                    `yield` `op x y`

                `}`

            `let` `minimum = all |> Seq.min`

            `let` `maximum = all |> Seq.max`

            `Number((minimum + maximum) / 2.0, (maximum - minimum) / 2.0)`

         `static` `member` `(+) (x, y) = (x, y) |> Number.combine (+)`

         `static` `member` `(-) (x, y) = (x, y) |> Number.combine (-)`

         `static` `member`

         `static` `member` `(/) (x, y) = (x, y) |> Number.combine (/)`

         `static` `member` `Pow (x, y) = (x, y) |> Number.combine ( ** )`

Thanks to @luketopia for the interactions on Twitter, and the trick which allows to pass the operator \*\* as an argument: use spaces between the parenthesis and the operator!

This entry was posted in [F sharp love](http://www.pirrmann.net/category/f-sharp-love/ "View all posts in F sharp love") and tagged [F#](http://www.pirrmann.net/tag/f/), [Kata](http://www.pirrmann.net/tag/kata/). Bookmark the [permalink](http://www.pirrmann.net/f-sharp-i-love/ "Permalink to F# |> I <3").
