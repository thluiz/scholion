---
url: "https://threadreaderapp.com/thread/1217120556098752512.html"
captured_at: "2026-11-16T02:25:32+00:00"
title: "Thread by @GeePawHill: How I Work (Test-Driving Mix) A while back, I wrote a muse about how I work focused just on the coding I do. Today I want to talk about how…"
domain: "threadreaderapp-com"
---

How I Work (Test-Driving Mix)

A while back, I wrote a muse about how I work focused just on the coding I do. Today I want to talk about how I test during that process.

[geepawhill.org/2019/11/27/how…](https://www.geepawhill.org/2019/11/27/how-i-work-just-programming-mix/)

The same caveat applies as before: This is not intended as prescription. I am happy, believe me, to tell you what to do. But that's not what this is. This is just what I do.

Meta: I don't separate testing from coding as activities. When I work, I am constantly bouncing back and forth between changing production code and changing test code. On those rare occasions where I spend a bunch of time on one vs the other, well, that's called "me messing up".

Meta: Tooling is super-important here. I've said I nearly always use an IDE, usually nowadays something from the IDEA/Intellij family, tho I've used many others. There are several test-related abilities that the modern IDE gives me.

1) UI rendering of results in lots of different forms/filters. Most standard is a tree with filter buttons.

2) Hotkeyed switching between source files and the corresponding test files for them.

3) Brainless gestures to run one, some, fast, or all tests. Brainless matters.

Meta: I almost never write tests that launch the shipping application. Instead, think of me as having two dependency trees of \*source\*. The test tree overlays the production tree, with a (usually) one-to-one relationship between file Something and file SomethingTest.

The tests are then run in a dedicated app that just runs tests. That app uses a framework tool -- that's what JUnit and the IntelliJ integration are -- that compiles the dependencies and runs the tests for me.

Okay, to cases, then.

I suppose the first thing that will surprise the non-TDD'ers in the room is this: I am the customer of my tests. I am the end-user. I am the one we please. I am the one who pays for them and values them, and the one who decides whether the cost/benefit ratio is good.

I almost never write a test to satisfy 1) a customer or 2) a metric or 3) a fondness for intellectual purity or 4) patriotism, good citizenship, the long term, art, or Plato.

I write tests cuz I am a mercenary. I make more money when I ship more value faster, and the tests I write help me do that.

(Okay, the reward isn't just money, I also get more support and much more approval. It's the modern way to translate everything to money, not mine.)

A decade ago I coined the term "microtest" for the kind of tests I write (or 95% of them). I found it easier to give people a new word than to try to parse the wildly variable meaning of any of the old words then in play, or even more inefficiently, argue definitions. I still do.

A microtest is a short, precise, descriptive, fast, grok-at-a-glance, executable and persistent demonstration that what I said is what the computer heard is what I meant.

That's all it is and all it does. Of course, meeting those criteria has lots of follow-on consequences.

(I sometimes use my testkit to write chunks of code that aren't tests at all. I'm taking advantage of the source-level access and ease of invocation.)

(I also sometimes use the testkit to write tests that \*aren't\* microtests. It's usually for one of two reasons: 1) I'm debugging and want to replicate a large-scale issue before I find the local one, or 2) I haven't figured out yet how to steer the code to be microtestable.)

"What I said was what the computer heard is what I meant" seems like a low bar. It is not. But before we get there, let's get a sense of the operational flow, the actual interactive way I use these microtests minute to minute.

My code is a huge directed (normally) acyclic graph of dependencies, a DAG, (It's not technically a tree, but I often think of it as a tree, anyway. Sue me.) Though most modern code is expressed as text, that text is, to me, a description of the DAG.

There are one or more entry points to the call-DAG, one or more exit points from it. Changing code means changing one path from entry to exit. Because I am a bear of little brain, I obsess first over shrinking the amount of that path I have to hold in my head as I work.

At its simplest, then: I find a minimal part of one path I want to change. I write a microtest that runs and fails because the change hasn't been made. I make changes until it runs and passes. Microtests persist, so I make sure \*all\* the ones I have still pass. Then I push.

The minimal size there is really important. In my head, I might see the change as having to do a whole lot of things by the time I'm done. In the code, though, I make it do just \*one\* of those things at at time, and pass \*one\* of those microtests at a time.

"Write a test, then pass it, then design the code" is the classic red-green-refactor of TDD pedagogy. It's certainly a thing I do at times. Often, tho, getting to a place where I can do that is quite a challenge, particularly so because lots of possible tests \*aren't\* microtests.

And this is the part that throws the noob: the value of the test-artifact is only one of many values provided by the operation of TDD.

I might have to dramatically rework a method to make it microtestable. I might have to pass a dependency. The dependency might not yet exist, or more likely, is used implicitly all through the method. I might have to take different arguments, return different values.

I do each of those things by writing a microtest that establishes just that each one of them does what I want when I want. Plink plink plink, one microtest/code-change pair at a time, chipping away at the face of the silicon mine.

Don't get me wrong, the artifact value isn't zero. It's worth quite a bit, cuz of the littleness of my brain, to have a continuously runnable set of all the old microtests that keeps me from breaking something I've already done and not finding out about it until brushfire time.

And boy do I continuosly run them. I run my microtests dozens and dozens of times on a programming day. I run them singly, sometimes in suites, and sometimes altogether. I run all the "fast" ones before a push, and 100% of all tests after the push, automagically via CI.

This is why the tests have to be super-fast and super-precise and super-grokkable: because I use them only very slightly less than I compile the code.

A standard size is about a half-dozen lines of code, including the declaration and the assertions. A standard name uses lots of words, but no formulaic repeated ones. A standard runtime is a few milliseconds.

Let's get back to "what I said is what the computer heard is what I meant". My imaginary respondent is saying, "Really? Cuz that doesn't seem like much.

I don't use tests to prove that the program is the right program -- that I have understood the customer's desire. I use my continuous warm relationship and lots of pictures and tables and dumb questions to ensure that.

I don't use tests to prove that code we don't own does what it should: databases, libraries, transport mechanisms. (I \*do\* sometimes use my testkit to write probes to make sure I get it.) When I have serious concerns about that, I have problems of a different order.

Almost all of the code I test comes under the heading of "our branching logic", where each word is significant. "ours" not "theirs", "branching" not "sequential", "logic" not "calculation". There are exceptions to all of these, but they're exceptions.

Note, I'm indifferent to \*calling\* code we don't own in the tests, provided it doesn't break one of the microtest criteria. A silly example: I use String extensively, though I don't own it and can't fix it if it's broken. The tests I call it in aren't meant to prove String works.

There are a lot of things that can make a program not okay. Some folks think of testing as a way to make sure that \*none\* of those things happen. I don't.

My tests mostly just establish for me "what I said is what it heard is what I meant". The reason for that is just this: in four decades of professional software development, 98% of the problems I've shipped have come down to a simple break in that simple three-way correlation.

Off by one. Inverted condition. Incomplete case partition. Unhandled degenerate. Literal spelling. Ordering assumption. External config.

Most of the problems I ship are -- I'm going to use a technical term here -- dumbassed mistakes. I use tests to find them before I ship them.

So there ya go. That's what I do. I write/change microtests interactively as I write/change production code. I do it in little tiny baby toy easy steps. It's at the center of my programming practice.
