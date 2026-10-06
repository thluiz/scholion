---
url: "http://simpleprogrammer.com/2015/03/16/11-rules-all-programmers-should-live-by/"
captured_at: "2015-03-17T10:37:46-03:00"
title: "11 Rules All Programmers Should Live By - Simple Programmer"
domain: "simpleprogrammer-com"
---

# 11 Rules All Programmers Should Live By

I am a person who tends to live by rules.

Now granted, they are mostly rules I set for myself—but they are still rules.

I find that creating rules for myself helps me to function better, because I pre-decide things ahead of time instead of making all kinds of decisions on the fly.

Should I go to the gym this morning?

Well, my rule says that on Wednesdays I go to the gym and today is Wednesday, so I am going to the gym—that settles it.

This week, as I was thinking about some of the kinds of rules I impose on myself, I thought it might be a good idea to come up with a set of rules that I think all software developers should live by.

Now, I’ll admit, most of these rules are more of guidelines, but anyway, here they are:

## 1: Technology is how you get to the solution, it is not THE solution

We can get really carried away with the latest JavaScript framework—ahem, Angular—IoC container, programming language or even operating system, but all of these things are not actually solutions to the problems we are trying to solve as programmers, instead they are simply tools that help us solve the problems.

We have to [be very careful not to get too crazy about a particular technology](http://simpleprogrammer.com/2013/07/08/how-religion-destroys-programmers/) that we happen to like or that happens to be oh so popular right now, lest we run the risk of thinking about every problem as a nail, just because we happen to be holding a shiny hammer we just learned about.

## 2: Clever is the enemy of clear

When writing code, we should strive to write code that is clear and easy to understand.

Code that clearly communicates its purpose is much more valuable than code that is obscure—no matter how clever it may be.

It’s not always true, but in general, clever is the enemy of clear.

It’s usually true that when we write code that is “clever,” that code isn’t particularly clear.

It’s important to remember this rule whenever we think we are doing something particularly clever.

Sometimes we write clever code that is also clear, but usually that is not the case.

If you’re interested in writing clean code I highly recommend you check out [The Clean Coder: A Code of Conduct for Professional Programmers (Robert C. Martin)](http://www.amazon.com/exec/obidos/ASIN/0137081073/makithecompsi-20)

[![code-1024x683.jpg](simpleprogrammer-com--11-rules-all-programmers-should-live-by/5bf88299d1c0784b57552d173cf8a0e9.jpg)](http://spzone.simpleprogrammer.netdna-cdn.com/wp-content/uploads/2015/03/code.jpg?b24a4c)

## 3: Only write code if you absolutely have to

This one might seem a little contradictory, after all, isn’t our job as programmers to write code?

Well, yes and no.

Our jobs may involve writing code, but we should still strive to write as little of it as possible to solve the problem we are trying to solve.

This doesn’t mean we should make our code as compact as possible and name all our variables using single letters of the alphabet. What it does mean is that we should try to only write code that is actually necessary to implement the functionality that is required.

Often it is tempting to add all kinds of cool features to our code or to make our code “robust” and “flexible” so that it can handle all different kinds of situations. But, more often than not, when we try to guess about what features would be useful or we try to pave the road to solve for problems that we think might exist in the future, we are wrong.

This extra code may not add any value, but it can still do a lot of harm. The more code there is, the more chances for bugs and the more code that has to be maintained over time.

Good software engineers don’t write code unless it’s absolutely necessary.

Great software engineers delete as much code as possible.

## 4: Comments are mostly evil

I’m [not a big fan of writing comments](http://simpleprogrammer.com/2014/02/13/comment-code/) in code. I’m with Bob Martin, when he says:

*“Every time you write a comment, you should grimace and feel the failure of your ability of expression.”*

—[Clean Code: A Handbook of Agile Software Craftmanship](http://www.amazon.com/gp/product/0132350882/ref=as_li_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=0132350882&linkCode=as2&tag=makithecompsi-20&linkId=QFEKXNHPNQEASR5A)

This doesn’t mean that you should never write comments, but for the most part they can be avoided and instead you can focus on doing a better job of naming things.

Comments should only really be written when it’s not possible to clearly communicate the intent of a variable or method by using a name. The comment then serves an actual purpose that could not be easily expressed in the code.

For example, a comment could tell you that this strange order in which some operation was occurring in the code was not a mistake, but was intentional because of a bug in the underlying operating system.

In general though, comments are not only evil because in many cases they are necessary, but also because they lie.

Comments don’t tend to get updated with the rest of the code and this results in the comments actually becoming dangerous, because they very well could steer you in a completely wrong direction.

Do you check every single comment against the code to make sure the code is actually doing what the comment says? If so, what is the point of having the comment? If not, how can you trust that the comment is telling you the truth?

It’s a pickle, so it’s best to avoid it as much as possible.

Ok, haters, go ahead and leave your torrent of “comments” in the comment section below, but I’m not changing my stance on this one.

## 5: Always know what your code is supposed to do before you start writing it

It seems obvious, but it isn’t.

How many times have you sat down to write code without fully understanding what the code you were writing was actually supposed to do?

I’ve done it more times than I’d like to admit, so this is a rule that I need to read often.

Practicing test driven development (TDD) can help here, because you literally have to know what the code is going to do before you write it, but it still doesn’t stop you from creating the wrong thing, so it’s still important to make sure you absolutely, 100% understand the requirements of the feature or functionality you are building before you build it.

## 6: Test your sh—code before you ship it

Don’t just toss your code over the wall and have QA pound on it only to send it back to you so that you can waste a bunch of everyone’s time with unnecessary bug reports and resolutions.

Instead, take a few minutes to run through the test scenarios yourself, before you call your code done.

Sure, you won’t catch every bug before you pass your work on to QA, but you’ll at least catch some of the stupid and embarrassing mistakes that we all make from time-to-time.

Too many software developers think that it is only QA’s job to test their stuff. It’s simply not true. Quality is everyone’s responsibility.

[![books-1024x964.jpg](simpleprogrammer-com--11-rules-all-programmers-should-live-by/55a40afc43cc14089e3c8d63643fdea4.jpg)](http://spzone.simpleprogrammer.netdna-cdn.com/wp-content/uploads/2015/03/books.jpg?b24a4c)

## 7: Learn something new every day

If you didn’t learn something new today, you just made backwards progress, because I can guarantee you forgot something.

It doesn’t take a lot of time to learn something new each and every day.

Try spending just 15 minutes or so reading a book—[I read a whole lot of books last year, just reading about 45 minutes each day on average.](http://simpleprogrammer.com/2014/12/08/books-read-year/)

The little advances you make each and every day add up over time and will greatly shape your future. But, you have to start investing now if you want to reap the rewards later.

Besides, today technology is changing so rapidly that if you aren’t continually improving your skills and learning new ones, you are going to be left behind very quickly.

## 8: Writing code is fun

That’s right. You probably didn’t get into this profession just because it pays well.

I mean, there is nothing wrong with picking a job that pays well, but doctor or lawyer would have probably been a better choice.

Most likely you became a software developer, because [you love writing code](http://www.amazon.com/gp/product/1934356344/ref=as_li_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=1934356344&linkCode=as2&tag=makithecompsi-20&linkId=I57JFSYJSY6QO3CS). So, don’t forget that you are doing what you love.

Writing code is a lot of fun. I wish I could write more code.

I’m usually too busy keeping this business going to spend much time writing code these days, which is one of the reasons why I so clearly remember how much fun it is.

Perhaps you forgot that writing code is fun. Perhaps it’s time to remember how much fun it is again, by starting a side project or just changing your mindset and realizing that you get to write code and you are even paid for it. (Hopefully)

## 9: You can’t know it all

As much as you learn, there is still going to be a lot you don’t know.

It’s important to realize this because [you can drive yourself nuts trying to know everything.](http://simpleprogrammer.com/2014/06/23/dont-overwhelm-trying-learn-much/)

It’s OK to not have all the answers.

It’s OK to ask for help or to speak up when you don’t understand something.

In many cases, you can learn what you need to know pretty darn close to when you need to know it—believe me, I do it all the time.

My point is, don’t get caught up in trying to learn it all, when that is an impossible task. Instead, focus on learning what you need to know and building [the skills that enable you to learn things quickly](http://simpleprogrammer.com/2012/09/23/learning-to-learn/).

## 10: Best practices are context dependent

Is test-driven development, the best way to write code?

Should we always pair program?

Are you a scrub if you don’t use IoC containers?

The answer to all of these questions is “it depends.”

It depends on the context.

People will try to shove best practices down your throat and they’ll try to tell you that they always apply—that you should always do this or that—but, it’s simply not true.

I follow a lot of best practices when I am writing code, but I also conditionally don’t follow them as well.

[Principles are timeless, best practices will always be situational](http://simpleprogrammer.com/2013/02/17/principles-are-timeless-best-practices-are-fads/).

## 11: Always strive to simplify

All problems can be broken down.

The most elegant solutions are often the most simple ones.

But, simplicity doesn’t come easy. It takes work to make things simple.

The purpose of this blog is to take some of the complexities of software development, and life in general, and make them simple.

Believe me, this isn’t an easy task.

Any fool can create a complex solution to a problem. It takes extra effort and care to refine a solution to make it simple, but still correct.

Take the time. Put forth the effort. Strive for simplicity.

## What rules do you live by?

So, those are my rules, but what about yours?

What rules do you personally live by?

What do you think is important to remember every day?

Leave a comment below, and also, take a second to join over 10,000 other software developers who are part of the Simple Programmer community.

[Just click here and you can join for free](http://simpleprogrammer.com/email)—you’ll get some of my best content and other free goodies every week.
