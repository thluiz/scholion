---
url: "https://www.codesimplicity.com/post/the-fundamental-philosophy-of-debugging/"
captured_at: "2026-11-16T17:02:55+00:00"
title: "The Fundamental Philosophy of Debugging"
domain: "codesimplicity-com"
---

Sometimes people have a very hard time debugging. Mostly, these are people who believe that in order to debug a system, you have to _think_ about it instead of _looking_ at it.

Let me give you an example of what I mean. Let’s say you have a web server that is silently failing to serve pages to users 5% of the time. What is your reaction to this question: “Why?”

Do you immediately try to come up with some answer? Do you start guessing? If so, you are doing the wrong thing.

The right answer to that question is: **“I don’t know.”**

So this gives us the first step to successful debugging:

> **When you start debugging, realize that you do not already know the answer.**

It can be tempting to think that you already know the answer. Sometimes you can guess and you’re right. It doesn’t happen very often, but it happens often enough to trick people into thinking that _guessing the answer_ is a good method of debugging. However, most of the time, you will spend hours, days, or weeks guessing the answer and trying different fixes with no result other than complicating the code. In fact, some codebases are full of “solutions” to “bugs” that are actually just guesses—and these “solutions” are a significant source of complexity in the codebase.

Actually, as a side note, I’ll tell you an interesting principle. Usually, if you’ve done a good job of fixing a bug, you’ve actually caused some part of the system to go away, become simpler, have better design, etc. as part of your fix. I’ll probably go into that more at some point, but for now, there it is. Very often, the best fix for a bug is a fix that actually deletes code or simplifies the system.

But getting back to the process of debugging itself, what _should_ you do? Guessing is a waste of time, imagining reasons for the problem is a waste of time—basically most of the activity that happens _in your mind_ when first presented with the problem is a waste of time. The only things you have to do with your mind are:

1.  Remember what a working system behaves like.
2.  Figure out what you need to look at in order to get more data.

Because you see, this brings us to the most important principle of debugging:

> **Debugging is accomplished by gathering data until you understand the cause of the problem.**

The way that you gather data is, almost always, by _looking_ at something. In the case of the web server that’s not serving pages, perhaps you would look at its logs. Or you could try to reproduce the problem so that you can look at what happens with the server when the problem is happening. This is why people often want a “reproduction case” (a series of steps that allow you to reproduce the exact problem)—so that they can _look_ at what is happening when the bug occurs.

Sometimes the first piece of data you need to gather is what the bug _actually is_. Often users file bug reports that have insufficient data. For example, let’s say a user files the bug, “When I load the page, the web server doesn’t return anything.” That’s not sufficient information. What page did they try to load? What do they mean by “doesn’t return anything?” Is it just a white page? You might _assume_ that’s what the user meant, but very often your assumptions will be incorrect. The less experienced your user is as a programmer or computer technician, the less well they will be able to express specifically what happened without you questioning them. In these cases, unless it’s an emergency, the first thing that I do is just send the user back specific requests to clarify their bug report, and leave it at that until they respond. I don’t look into it _at all_ until they clarify things. If I did go off and try to solve the problem before I understood it fully, I could be wasting my time looking into random corners of the system that have nothing to do with any problem at all. It’s better to go spend my time on something productive while I wait for the user to respond, and then when I _do_ have a complete bug report, to go research the cause of the now-understood bug.

As a note on this, though, don’t be rude or unfriendly to users just because they have filed an incomplete bug report. The fact that you know more about the system and they know less about the system doesn’t make you a superior being who should look down upon all users with disdain from your high castle on the shimmering peak of Smarter-Than-You Mountain. Instead, ask your questions in a kind or straightforward manner and just get the information. Bug filers are rarely intentionally being stupid—rather, they simply don’t know and it’s part of your job to help them provide the right information. If people frequently don’t provide the right information, you can even include a little questionnaire or form on the bug-filing page that makes them fill in the right information. The point is to be helpful to them so that they can be helpful to you, and so that you can easily resolve the issues that come in.

Once you’ve clarified the bug, you have to go and look at various parts of the system. _Which_ parts of the system to look at is based on your knowledge of the system. Usually it’s logs, monitoring, error messages, core dumps, or some other output of the system. If you don’t _have_ these things, you might have to launch or release a new version of the system that provides the information before you can fully debug the system. Although that might seem like a lot of work just to fix a bug, in reality it often ends up being faster to release a new version that provides sufficient information than to spend your time hunting around the system and guessing what’s going on without information. This is also another good argument for having fast, frequent releases—that way you can get out a new version that provides new debugging information quickly. Sometimes you can get a new build of your system out to just the user who is experiencing the problem, too, as a shortcut to get the information that you need.

Now, remember above that I mentioned that you have to remember what a working system looks like? This is because there is another principle of debugging:

> **Debugging is accomplished by comparing the data that you have to what you know the data from a working system should look like.**

When you see a message in a log, is that a normal message or is it actually an error? Maybe the log says, “Warning: all the user data is missing.” That looks like an error, but really your web server prints that every single time it starts. You have to know that a _working_ web server does that. You’re looking for behavior or output that a _working_ system does not display. Also, you have to understand what these messages _mean_. Maybe the web server optionally has some user database that you aren’t using, which is why you get that warning—because you _intend_ for all the “user data” to be missing.

Eventually you will find something that a working system does not do. You shouldn’t immediately assume you’ve found the cause of the problem when you see this, though. For example, maybe it logs a message saying, “Error: insects are eating all the cookies.” One way that you could “fix” that behavior would be to delete the log message. Now the behavior is like normal, right? No, wrong—the actual bug is still happening. That’s a pretty stupid example, but people do less-stupid versions of this that don’t fix the bug. They don’t get down to the [basic cause of the problem](http://www.codesimplicity.com/post/make-it-never-come-back/) and instead they paper over the bug with some workaround that lives in the codebase forever and causes complexity for everybody who works on that area of the code from then on. It’s not even sufficient to say “You will know that you have found the real cause because fixing that fixes the bug.” That’s pretty _close_ to the truth, but a closer statement is, “You will know that you have found a real cause when you are confident that fixing it will make the problem [never come back](http://www.codesimplicity.com/post/make-it-never-come-back/).” This isn’t an absolute statement—there is a sort of scale of how “fixed” a bug is. A bug can be more fixed or less fixed, usually based on how “deep” you want to go with your solution, and how much time you want to spend on it. Usually you’ll know when you’ve found a decent cause of the problem and can now declare the bug fixed—it’s pretty obvious. But I wanted to warn you against papering over a bug by eliminating the symptoms but not handling the cause.

And of course, once you have the cause, you fix it. That’s actually the simplest step, if you’ve done everything else right.

So basically this gives us four primary steps to debugging:

1.  Familiarity with what a working system does.
2.  Understanding that you don’t already know the cause of the problem.
3.  Looking at data until you know what causes the problem.
4.  Fixing the cause and not the symptoms.

This sounds pretty simple, but I see people violate this formula all the time. In my experience, _most_ programmers, when faced with a bug, want to sit around and think about it or talk about what might be causing it—both forms of guessing. It’s okay to talk to other people who might have information about the system or advice on where to look for data that would help you debug. But sitting around and _collectively_ guessing what could cause the bug isn’t really any better than sitting around and doing it yourself, except perhaps that you get to chat with your co-workers, which could be good if you like them. Mostly though what you’re doing in that case is wasting a bunch of people’s time instead of just wasting your own time.

So don’t waste people’s time, and don’t create more complexity than you need to in your codebase. This debugging method works. It works every time, on every codebase, with every system. Sometimes the “data gathering” step is pretty hard, particularly with bugs that you can’t reproduce. But at the worst, you can gather data by looking at the code and trying to see if you can _see_ a bug in it, or draw a diagram of how the system behaves and see if you can perceive a problem there. I would only recommend that as a last resort, but if you have to, it’s still better than guessing what’s wrong or assuming you already know.

Sometimes, it’s almost magical how a bug resolves just by looking at the right data until you _know_. Try it for yourself and see. It can actually be fun, even.

\-Max
