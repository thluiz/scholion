---
url: "http://arne-mertz.de/2015/03/simple-and-clean-code-vs-performance/"
captured_at: "2015-04-01T11:08:12-03:00"
title: "Simple and Clean Code vs. Performance"
domain: "arne-mertz-de"
---

# I don’t think so

There are many reasons why I don’t think we should sacrifice simple and clean code to write more performant code per se. In contrary, I have been criticized for advocating the sacrifice of performance for simplicity.

I would prefer if everyone wrote simple and clean code by default. OK, that’s pretty obvious, because that’s what this blog is all about.  But what about reasons why I think so? Here are some.

## Performance is not efficiency

There is an important point to get out of the way first. We have to distinguish between efficiency and performance. What is the difference? In very simple terms it is how fast you do something (performance) vs. how long it takes to do it (efficiency).

At first glance that might sound like it’s the same, but it’s not. Imagine you have to go from point A to point B. Efficiency means you go the shortest way. Performance means you run instead of walking. So if you run as fast as you can around the whole block to get to your neighbour, you are at high performance, but not very efficient.

In programming, loops often contribute much to program run time. Here, performance would mean that a single loop cycle executes faster. Efficiency means that you have to do less cycles, mostly because you have a smarter algorithm.

Sometimes you can not have the best of both worlds. The steps of a more efficient algorithm may be less performant. However, before you try to squeeze the last bit of performance out of a piece of code, make sure it is efficient. Only if you have tested all possibilities in terms of efficiency it can pay off to worry about performance.

> Sometimes it is enough to make your code more efficient to get the desired speed without having to worry about performance details.

## We don’t need performance everywhere

This one is obvious, but many programmers, especially new programmers, tend to overlook it. There are tons of questions on forums and stackoverflow, asking about how a certain piece of code can be optimized. When one asks the counter question if the code is really a performance bottleneck it most often turns out that it is not.

There is a saying that 80% of the run time of a program is spent in only 20% of the code. Some say it’s 90/10. The exact numbers are not very important in general. The crucial point is that the program spends a lot of time in a small amount of code.

On the other hand that means that most code does not contribute much to the total run time, and if we optimize the hell out of it we won’t see much of a result, if we see anything at all.

> Don’t optimize code that you have not proven to be vital for the overall program performance.

## We don’t really know how to write performant code

I know, how can I dare to say something like that. The fact is that one of the major contributions to program run time is the number of instructions the processor has to execute. And those are not written by us, but by the compiler and its optimizer.

Optimizers come in all shapes and colors, and unless you are an expert in the field, you can’t even guess what they will do to a nontrivial piece of code. Optimizers can eliminate temporary objects, they can inline functions, sometimes even at link time, and they can shuffle around and eliminate lots of those instructions.

So, with those super powers in the machine and our complete ignorance of what code will give the best result, what can we do to make our code more performant? At first, nothing. And if we really have to care about performance, we can not rely on our imagination or experience, we have to use a tool.

> By default, write code for maintainability, because it might be as performant as anything else. If you really have to improve performance, use a profiler.

Of course this does not mean you should prematurely pessimize. If there are two or more ways to write a piece of code that are equally readable, use the way that will probably give the best performance. For example, use `++iter` instead of `iter++` if you don’t save the result of the expression, and so on.

## Performance and simplicity don’t always contradict each other

The other major contribution to program run time, maybe even more than the amount of instructions, is the layout and structure of data in memory. There is a [great talk about getting better performance by using the right data structures by Chandler Carruth](http://channel9.msdn.com/Events/CPP/C-PP-Con-2014/Efficiency-with-Algorithms-Performance-with-Data-Structures "Chandler's "), so I won’t go further into this.

All I want to say is, if the memory layout of your data is bad, much of the run time goes into the fetching of data from memory and saving a few instructions won’t have as much of an impact as using the right data structures.

> Make sure you use the most performant data structures before you start tweaking your code for more performance.

There is another point to writing performant *and* simple code: [Using the libraries you have, and using them right](http://arne-mertz.de/2015/02/know-your-libraries/ "Know your libraries"). Those library writers usually are smart guys and know how to write performant code. They particularly know how to use their profilers.

So if you use libraries instead of rolling your own solutions, your code is likely to be not only more robust and simple to maintain, but also to be more performant.

> Know and use your libraries, unless your profiler showed them to have bad performance.

# Conclusion

Write readable and simple code by default. If you actually have a performance problem and have located it, there are still many options that are more promising than turning your code into a fast but unreadable mess. Sacrifice simplicity for performance only as a last resort, and *always* use a profiler when you are dealing with performance problems.
