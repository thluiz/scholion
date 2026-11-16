---
url: "https://dev.to/taillogs/how-to-write-a-good-piece-of-code-2gmj"
captured_at: "2026-11-16T18:46:11+00:00"
title: "How to Write a Good Piece of Code"
domain: "dev-to"
---

[Source](https://steemit.com/technology/@trollfarmer/the-only-valid-measurement-of-code-quality)

## [](#how-to-write-a-good-piece-of-code)How to Write a Good Piece of Code

[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fl6cp6r1wix5gbhi6liv7.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fl6cp6r1wix5gbhi6liv7.png)  
[XKCD](https://xkcd.com/844/)

## [](#make-sure-your-code-can-be-good)Make Sure Your Code "Can Be Good"

The first and probably most important step to writing a good piece of code is to not code at all.

*   Have you validated your assumptions?
*   What is the scope of the code?
*   How will it affect existing code?
*   Has someone already written this code?

Being able to answer questions like these are the foundation of a good piece of code.

#### [](#discuss-with-others)Discuss With Others

The best way to validate your choices is by getting the input of others. Strive to be in an environment where people aren't afraid to challenge your decisions and ideals.

_Even the strongest wall might look weak when looked at with the right perspective._

[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fmiafrycnd9nwuqu87dtv.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fmiafrycnd9nwuqu87dtv.gif)

## [](#break-it-down)Break It Down

Now that you're confident that your code "can be good", it's time to figure out how to actually make it good. Start, by thinking in terms of API's and attempt to break down your proposed code into the smallest pieces possible.

Understanding how to break down tasks into smaller pieces, is the number one thing I see junior programs struggle with. Remember, a chunk of code that you've broken down is one that others are able to help you with. Left as a monolith, it only serves to isolate you from the team.

The first part of a code design phase should very rarely touch on the implementation. Instead, you should be dealing in needs and constraints. Time spent on implementation is often wasted time, because high level API changes can invalidate implementation assumptions. In my personal experience, starting an implementation discussion with already agreed upon API, usually makes the discussion go a lot smoother.

## [](#write-tests-that-define-it-before-writing-it-spicy-and-opinionated)Write Tests That Define It Before Writing It (_Spicy and Opinionated_)

[![maxwidth](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fua04xzptee84tb64sjaj.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fua04xzptee84tb64sjaj.gif)

Now that you know how to break down the code. Write a test for each discrete unit you've identified. Writing a test for each piece of functionality your code will expose, before you code it, is the defining trait of TDD (Test Driven Development). [There's been a number studies on the effectiveness of TDD. While some of the studies are controversial, almost all of them report positive improvement on the number of bugs after using TDD](https://www.computer.org/csdl/magazine/so/2007/03/s3024/13rRUygT7kK).

Edit: I originally made a claim of 40%-80% reduction in bugs from TDD. After receiving comments in [this Reddit thread](https://old.reddit.com/r/programming/comments/c5ap50/how_to_write_a_good_piece_of_code/) I realized that it was a inherently biased representation of the data. I've instead included a picture of the studies results below, so you can judge for yourself. I've also included the precursor paragraph from the author.

> The results are sometimes controversial (more so in the academic studies). This is no surprise, given incomparable measurements and the difficulty in isolating TDD's effects from many other context variables. In addition, many studies don't have the statistical power to allow for generalizations. So, we advise readers to consider empirical findings within each study's context and environment.

[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fr9l9cpgfc8b9zoylvtmp.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fr9l9cpgfc8b9zoylvtmp.gif)

> A 2005 study found that using TDD meant writing more tests and, in turn, programmers who wrote more tests tended to be more productive. Hypotheses relating to code quality and a more direct correlation between TDD and productivity were inconclusive. Hypotheses relating to code quality and a more direct correlation between TDD and productivity were inconclusive.

[Source: Wikipedia](https://en.wikipedia.org/wiki/Test-driven_development#Benefits)

I believe test driven development forces you to put yourself in the point of view of users first, and this will result in a more practical and natural set of API's.

Resist the temptation to tackle multiple tasks at once. You should be writing failing tests for a single unit of your code, followed by writing the implementation for that test. This will allow you to validate your design efficiently, and maintain test coverage even though you're adding code to the codebase.

## [](#keep-your-code-consistent)Keep Your Code Consistent

Personal style and preferences will differ between developers. What should not differ is code consistency. You should have consistent and predictable naming conventions for variables and declarations. If you use tabs, you should use tabs everywhere. If you use spaces, you should use spaces everywhere.

Many junior developers get caught up in the nuances of each choice. In reality, what's far more important is how reliable you are with with your choice. At first this may seem like a relatively small task, but consistency extends far past tabs vs spaces.

The logic of you code also needs to be consistent. Why did you use a `map` here and a `for each` over there? Why are you using `var` in some places but `let` and `const` in others? Predictability is one of the hardest traits to find in a programmer (or a human in general), it's also one of the most valuable.

Your worth as a programmer is defined by your "maximum potential value" multiplied by your "projected risk". Quality is meaningless without reliability.

## [](#review-it)Review It

[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fq99xk0wfki96x6exec6q.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fq99xk0wfki96x6exec6q.png)  
[Source](http://geek-and-poke.com/geekandpoke/2010/11/1/how-to-make-a-good-code-review.html)

If code goes into master it should be reviewed. For a review to be beneficial, the author needs to truly appreciate the value of the review process.

Never in this life will you know everything.

_A good programmer writes great code and doesn't get it reviewed._

_A great programmer writes decent code but puts it through a scrutinous review process._

You should account for failure in every aspect of your life, including coding. Mistakes will be made, and most often all that's needed to stop them is another set of eyes.

## [](#ship-it)Ship It

Congrats, you've now written a good piece of code. It's possible to write a good piece of code without this process, but it's not possible to "always write a good piece of code" without it.

After shipping, remember to communicate with your team about what you've accomplished, it may unblock someone.

## [](#dont-overthink-it)Don't Overthink It

[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Ffu9mbimjacoghhtnqydz.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Ffu9mbimjacoghhtnqydz.png)

Every rule here should be taken with a grain of salt. Should a 2 line commit to an internal `README` really be reviewed?

Strive for the best practices but remain practical and rational, don't engineer things that didn't need to be engineered in the first place. The most important tool you have in your arsenal is your gut (intuition). Rules do not exist to get in your way, they exist to be consistent and reliable when you are not (and you won't be).

[![Foo](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fg3hk69dlodu18eckmzyx.png)](https://twitter.com/taillogs)

[My Blog](https://www.cdevn.com/how-to-write-a-good-piece-of-code)
