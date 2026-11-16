---
url: "https://fluentcpp.com/2020/06/19/great-developers-dont-just-write-great-code"
captured_at: "2026-11-16T03:39:03+00:00"
title: "Great Developers Don’t Just Write Great Code"
domain: "fluentcpp-com"
---

Published June 19, 2020

I’m assuming that, if you’re reading this, you are aspiring to become a good developer.

But what _is_ a good developer, to begin with?

Let’s reflect on what we need to do in our jobs as software developers to identify what is important–and therefore what we have to master in order to become “good developers”.

### Good developers write good code

As software developers, our mission is to ship software that works. And what is software made of? Code, of course!

What comes out of this simple analysis is that if you want to be a good developer, you need to be able to write **good code**.

Fine. But now we’re left with a new question: what is “good code”?

To answer this question, let’s think about what code it useful for. Code is what makes software, and the mission of developers is to make software that works. So following this, good code is code that works.

Except that there is a hundred ways to write code to make a feature work. But all those ways are not as good as each other. Note that in code that “works”, I’m also including the fact that it runs fast enough, so I’m not talking about which code has the best algorithmic complexity.

The differences between the various pieces of code that all “work” is their design. So good code is code that has **good design**.

Bear with me, we’re getting there. We now need to define what “good design” is.

Once we’ve written a piece of code that works, why does its design matter in the first place? It matters if someone is going to come back to this code. Let’s call this someone Bill. Bill can be you or can be anyone else in the company. Bill can even be someone who is not here yet but will be recruited in the future.

So a good design is a design that will make Bill’s life easier. As a result, a good design needs to be understandable. If we unroll the logic we’ve just built, a good developer can produce code that is **understandable**.

But this is only a part of the picture. To be a good developer you also need to do an great job when you _are_ Bill.

### Good developers can work with any code

How much time do you spend writing code every day? Even if you work as a professional software developer, you probably don’t spend all day coding. You probably spend more time reading code than writing it.

Indeed, we read code all the time. We read code to analyse it and think about how to integrate new features. We read code when we debug maintenance issues. We read code during code reviews, when writing documentation, or simply when we help out another developer with his task.

As software developers, we read a lot of code. We spend much more time being Bill than writing code.

As a result, we need to embrace our Bill’s responsibilities. On top of writing expressive code to make Bill’s life easier, we need to figure out **how to work with existing code**. Because that is what we do the most in our daily work. **We are Bill**.

#### Understanding code

On top of giving instructions to the machine, the purpose of code is for a developer to communicate their intent to other developers. Like we said, we write code with good design for Bill to understand.

But there is code out there, that is not easy to understand. A good part of this code is what we collectively call “legacy code”. If you’re a software professional, you probably have to work with legacy code.

I’ve worked for over 7 years in our industry, I go to a lot of conferences and user groups, some of which I’m an organizer of, and I have a [popular blog](https://www.fluentcpp.com/) about writing expressive code. With all this I get to talk with a lot of developers, and I can tell you one thing: **legacy code is everywhere**.

Since a large part of your job is about reading code, and that you get to work on tough code, to be a good developer you need to be able to read code you don’t know and quickly make some sense out of it.

Fortunately, there are techniques to understand unfamiliar code. Here is a practical one: when you read a function or a method for the first time, **start by looking at its end** **first**.

Indeed, functions often have a progression with intermediate objects and actions, that leads to deliver a final result or effect that is located at its end. If you start by looking at that, you’ll get an idea of where the function or method is going, and it will make the reading of the rest that much easier. Sometimes, it will even save you from reading the rest at all, because you’ll have understood what the function is about.

Of course, to know what a function is about, its name and parameters should be enough. But there is code out there where functions don’t have a name as informative as they “should be”.

Peeking at the end of a function or method can save you a great deal of time. This is one of the 10 techniques to understand legacy code that are presented in [The Legacy Code Programmer’s Toolbox](https://leanpub.com/legacycode).

#### Humility

When you’re Bill, it can be tempting to blame the person who wrote the code you’re trying to figure out. After all, their job was to write code with good design, and if you can’t make sense out of their writing, then they didn’t do such a good job.

You may be right or you may be wrong. Maybe it was a difficult piece of code to write, and that we wouldn’t have done a better job if we had had to write it ourselves. Maybe we’re lacking a piece of context. Or maybe the person who wrote it didn’t find the optimal solution indeed, but who always find the optimal solutions after all?

The thing is that it doesn’t matter. The code is here, and it’s what you have to work with. Don’t think about whether the author did a good job or a poor job designing the code, unless you’re doing this for the explicit purpose of improving the code or improving your skills.

#### Focus on what matters

What does matter in your ability to be efficient when working with existing code is what you know about it. In software engineering like in many places, knowledge is power.

There are plenty of ways to increase your knowledge about your codebase. One of them is to write a piece of documentation on a region of code you don’t know.

It can seem surprising at first: if you don’t know a piece of code, how can you write anything about it?

If you start documenting little by little what you discover in a region of code, this will direct your research. By explaining what you just start understanding, you’ll discover questions to be answered in order to complete your explanation. This is very valuable because it gives you specific things to look for in code.

Little by little, your exploration goes from a random one to a a directed one. Until you know your way around the region of code.

Note that there are plenty of [other practical ways](https://leanpub.com/legacycode) to increase your knowledge, and more generally to be more efficient when working with legacy code.

### It’s still easier to work with good code

If we’re spending most of our time in the role of Bill, reading and working with existing code, does it matter much to be able to write good new code after all?

The answer is yes, because the code you produced will be used by Bill. And even if it is Bill’s responsibility to be able to work with any code, you want to make his work as easy as possible.

Writing code is about writing more than about code. You send a clear message, you reader open their eyes wide, and you hope that you guys will meet in the middle.

### You will also like

*   [The Legacy Code Programmer’s Toolbox](https://leanpub.com/legacycode/)
*   [The Legacy Code Programmer’s Toolbox is out](https://www.fluentcpp.com/2019/02/01/the-legacy-code-programmers-toolbox-is-out/)
*   [It all comes down to respecting levels of abstraction](https://www.fluentcpp.com/2016/12/15/respect-levels-of-abstraction/)

Don't want to miss out ? **Follow:**   [](https://twitter.com/joboccara "Follow me on twitter")[](https://www.linkedin.com/in/jonathan-boccara-23826921/ "Find us on Linkedin")[](https://www.fluentcpp.com/feed/ "Subscribe to our RSS Feed")  
Share this post!
