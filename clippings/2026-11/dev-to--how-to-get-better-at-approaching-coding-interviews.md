---
url: "https://dev.to/jacobjzhang/how-to-get-better-at-approaching-coding-interviews-nnp"
captured_at: "2026-11-16T01:00:25+00:00"
title: "How to Get Better at Approaching Coding Interviews"
domain: "dev-to"
---

## [](#how-to-get-better-at-approaching-coding-interviews)How to Get Better at Approaching Coding Interviews

So you want to get better at interviewing? It's all in the approach-- this guide is a **step by step walkthrough** on exactly how to answer coding interview question from companies like Facebook, Amazon, Microsoft, Netflix, or Google.

This article will cover a lot. It'll walk you through a common technical (whiteboard or non-whiteboard) interview question, and you'll be exposed to things like:

*   The mentality you need to conquer nerves
*   Every step to take during the interview
*   What patterns to brush up on

And much more. Let's start by tackling **the mental aspects** of the interview before the tangible steps to approaching such problems.

[![](https://res.cloudinary.com/practicaldev/image/fetch/s--ZIB6PB2_--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://storage.googleapis.com/algodailyrandomassets/curriculum/misc/approaching-coding-interviews.svg)](https://res.cloudinary.com/practicaldev/image/fetch/s--ZIB6PB2_--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://storage.googleapis.com/algodailyrandomassets/curriculum/misc/approaching-coding-interviews.svg)

## [](#getting-over-nerves)Getting Over Nerves

Software engineering and technical interviews are nerve-wracking. We all know this, but rarely do we ask why.

Why do these kinds of interviews specifically conjure up such dread?

[![](https://res.cloudinary.com/practicaldev/image/fetch/s--S64Fx7sT--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://images.pexels.com/photos/105472/pexels-photo-105472.jpeg%3Fauto%3Dcompress%26cs%3Dtinysrgb%26dpr%3D2%26h%3D650%26w%3D940)](https://res.cloudinary.com/practicaldev/image/fetch/s--S64Fx7sT--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://images.pexels.com/photos/105472/pexels-photo-105472.jpeg%3Fauto%3Dcompress%26cs%3Dtinysrgb%26dpr%3D2%26h%3D650%26w%3D940)

Really, there are few consequences.

Worst case scenario, you fail to correctly express the algorithm they're looking for. Or maybe you can't think of the correct definition for something. You then probably don't get the job.

That's not a great outcome, but there are far worse things. You can always just go home, brush up on what you missed, and try to apply elsewhere.

Knowing that doesn't seem to help though, and here's why.

Our fears usually derive from _uncertainty_. That is, the belief that there's a chance you'll be presented with a question or challenge that _you have no idea how to solve_.

But this is not actually the case!

First off, with the right approach-- which the rest of this article will explore in-depth, you can solve any problem.

Secondly-- yes there is a chance you're asked something completely out of left field. But for the most part, interviewers really _do_ want to see **how you think**. As someone who's been on the other end quite a number of times, know that we want you to do well.

If nerves are still in the way, there are some other solutions. Some things that might be helpful are [daily meditation](https://www.amazon.com/gp/product/1439195455/ref=as_li_qf_asin_il_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1439195455&linkCode=as2&tag=algodaily03-20&linkId=00452c0588f28a516612a0778b749753), eating a healthy meal that fuels your brain, and [regular aerobic exercise](https://www.amazon.com/gp/product/0316113514/ref=as_li_qf_asin_il_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0316113514&linkCode=as2&tag=algodaily03-20&linkId=2344bdbddf2327be22643a8ac562f0ac).

[![](https://res.cloudinary.com/practicaldev/image/fetch/s--0A4LDYU9--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://images.pexels.com/photos/1092730/pexels-photo-1092730.jpeg%3Fauto%3Dcompress%26cs%3Dtinysrgb%26dpr%3D2%26h%3D650%26w%3D940)](https://res.cloudinary.com/practicaldev/image/fetch/s--0A4LDYU9--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://images.pexels.com/photos/1092730/pexels-photo-1092730.jpeg%3Fauto%3Dcompress%26cs%3Dtinysrgb%26dpr%3D2%26h%3D650%26w%3D940)

## [](#what-to-do-if-you-blank-out-completely)What to Do If You Blank Out Completely

With almost any technical challenge, if you have the right approach, you can figure out a way to solve a problem. But what if you genuinely have no idea where to start?

So let's address something quickly-- if you really have no clue, here's what to do.

Let's say you're a frontend engineer with a few years of `Javascript` Single Page App development under your belt. You're asked the following technical question in an interview.

> _When would you apply asynchronous communication between two backend systems?_

You freeze, and suddenly your chest tightens. You've never worked on any backend systems, and you've forgotten what `asynchronous` means. For a few seconds, you stare at the interviewer, and your mind has nowhere to go.

Here's two potential ways to address this:

1.  Link it to _something_ you've done
2.  Emphasize how _excited you are_ to learn and work on such things

The first response works because it still allows you to demonstrate your experience:

> _I haven't directly worked on backend systems, but can you remind me what `asynchronous` means again? Ah, a form of a programming that allows work to be done separately from the primary application thread? I've done something similar with React-- sometimes inserting data into the database via a REST endpoint takes some time, but we want to give immediate feedback to the user that it's being persisted. So \*\*my educated guess_\* is that it would be when you want to have a process do something while waiting for something else to complete.\*

In this case, it may not be 100% what the interviewer wanted to hear, but you've shown _some_ technical acumen. You were also able to include some discussion about past experiences.

On the other hand, what if there's nothing at all you can relate the question to? Talking about how excited you are and how you _would_ learn this might be a good alternative:

> _To be honest, I'm not sure, but I've heard the term `asynchronous` and would love to learn more about backend systems. I'll be sure to read up on it after this interview, do you recommend any books or articles to start with?_

## [](#are-whiteboard-algorithm-interviews-good)Are Whiteboard Algorithm Interviews Good?

The rest of this lesson will be talking about approaching standardized data structures and algorithm based questions. It will be still relevant, but less so, to small sample challenges like "_here's a basic setup, implement a REST API with some scaffolding_".

[![](https://res.cloudinary.com/practicaldev/image/fetch/s--jSee2lXN--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://miro.medium.com/max/600/1%2AHPGzysLVdFgdfV356RpKRA.jpeg)](https://res.cloudinary.com/practicaldev/image/fetch/s--jSee2lXN--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://miro.medium.com/max/600/1%2AHPGzysLVdFgdfV356RpKRA.jpeg)

Yes, **whiteboard algorithm interviews are controversial**. However, there are several reasons they still persist. Firstly, they give several strong signals to the interviewer, such as:

*   Can the candidate can think with clarity in front of others (what this lesson aims to address)
*   Do they sound like they've prepped for the interview (signal for work ethic)
*   Do they have a reasonable amount of logical ability?
*   Can they tell a good solution from a bad one?
*   How is their grasp of computer science fundamentals?

**Secondly**, they _are easy to do at scale_, a consideration especially important if you are a conglomerate that needs to make thousands of annual hires.

Yes, there are take-home assignments, build-a-feature type of interviews, and week-long "trial" periods. I'm sure these are all great methods.

However, the standard "can you solve this problem in front of me" `data structure` and algorithm questions are still very much the standard at most software companies.

Let's figure out how to tackle them.

## [](#the-approach-of-good-interviewees)The Approach of Good Interviewees

Before we dive in, here's an important note. For any of this to work, you've got to have your data structures and algorithms down pat.

The more practice you have with these topics, the easier it will be to `pattern`\-ize them. It'll also be easier to retrieve them from memory come interview time.

A good starting point is, of course, [AlgoDaily's Premium Course](https://algodaily.com/curriculum) and [daily newsletter problem](https://algodaily.com/challenges/daily). Other recommendations can be found in our lesson around [How to Prepare for a Technical Interview](https://www.algodaily.com/lessons/how-to-prepare-for-a-technical-interview).

With all that said, here's the typical steps we recommend for **solving whiteboard questions**. We'll spend plenty of time exploring each in depth.

1.  Run through a few (1-3) example inputs to _get a feel for the problem_
2.  Unpack _the brute force solution_ quickly by asking how a human would do this
3.  Tie the brute force solution back to a **pattern, data structure, or Computer Science technique**
4.  _Optimize and run through the same test cases_ from step 1 again
5.  If you have time, _call out edge cases_ and improvements to the problem

## [](#communication-during-the-interview)Communication During the Interview

[![](https://res.cloudinary.com/practicaldev/image/fetch/s--DrwN5YO6--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://images.pexels.com/photos/7374/startup-photos.jpg%3Fauto%3Dcompress%26cs%3Dtinysrgb%26dpr%3D2%26h%3D650%26w%3D940)](https://res.cloudinary.com/practicaldev/image/fetch/s--DrwN5YO6--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://images.pexels.com/photos/7374/startup-photos.jpg%3Fauto%3Dcompress%26cs%3Dtinysrgb%26dpr%3D2%26h%3D650%26w%3D940)

It's not a secret that a big part of the interview is a test of your communication skills. Software engineering is a team sport.

The myth of the lone genius programmer is simply that-- a myth. This is especially for big, hairy, impactful projects that require hundreds of thousands of engineers.

How do you demonstrate strong communication skills?

**You must keep talking** - I can't emphasize this enough. Unless you need complete silence to think-- which is fine-- you should be voicing your thoughts.

*   If you're stuck, let the interviewer know
*   If you don't understand the problem, ask more clarifying questions
*   If you have no idea what's going on, say you need more context
*   If you need a hint, let them know!

**If you're shy, that's perfectly fine**. But with regards to the interview-- know that you might be working with either this person, or someone of a similar aptitude and technical ability. For better or worse, how the interviewer sees you during the interview is what they think they'll get when you come on board. Try your best to be friendly and vocal, if only for the few hours it takes to land the job.

## [](#how-to-gather-requirements)How to Gather Requirements

Let's move on to practical technical interview tips. We can examine the [Zeros to the End](https://algodaily.com/challenges/zeros-to-the-end) problem. Here's the prompt:

> _Write a method that moves all zeros in an array to its end._

The very first thing you should do is **to clarify the requirements.** Until you know exactly what the problem is, you have no business trying to come up with a solution. Here's why:

> _Candidate: Cool, zeros to the back, nonzeros in front. That's it right?_

Seems simple enough. Why not jump right to the solving it? Because the interview might then say:

> _Interviewer: Also, note that you should maintain the order of all other elements. Oh, and this needs to be done in O(n) time._

If you hadn't considered that, you might have gone a very bad path. It's crucial to always **repeat the question in your own words** and clarify heavily. Get the full scope of requirements, and repeat it so they know you've fully grasped the entirety of the problem

> _Candidate: So we want to move all the zeros to the back, while keeping nonzeros in front. We want to also keep the order the nonzeros were originally in, and the algorithm should run in linear time._
> 
> _Interviewer: Right on._

## [](#start-with-inputs-and-outputs)Start With Inputs and Outputs

The very _next_ thing to do is either ask for few sample arrays, or come up with your own. Start building your test cases. It helps you start to process how to transform the inputs to get the outputs.

_Try to start with a very small input, and increase its size as you do more examples._ Here's what you might say:

> _Candidate: Very interesting problem. Alright, just to make sure I understand the transformation and result that we want, let me run through a few examples. So if I'm given `[0, 1]`, we'd want `[1, 0]` back?_
> 
> _Interviewer: Yes, exactly. _(Candidate begins to think of how to move that lone zero in the first example)__
> 
> _Candidate: Hm, for that one, we just needed to swap the `0` with the `1`. Now, if given `[1, 0, 2, 0, 4, 0]`, I would want `[1, 2, 4, 0, 0, 0]` back._
> 
> _Interviewer: Correct._
> 
> _Candidate: And `[0, 0, 4]` becomes `[4, 0, 0]`. Hm..._

## [](#how-to-come-up-with-a-brute-force-solution)How to Come Up With a Brute Force Solution

Now that you've tried some inputs and outputs, the primary question to ask is this:

`If a machine were not available, how would a human manually solve this?`

Remember, computers are just tools. Before we had them, humans had to calculate things by hand. So asking yourself how you'd do it manually is a great way to start brainstorming ways to solve the problem. When loops and conditionals aren't available, you're able to say in plain English what you need to do.

> _Candidate: Hm, yeah, for these examples, the result keeps returning an array of the non-zeros plus an array of the zeros at the end. Thinking through a very basic implementation, what I've been doing is: iterating through, finding the non-zeros, and just putting them in an another `temp` array. Then I've been filling the rest of the result array with `0`s until we've gotten the original length._
> 
> _Interviewer: Interesting. Want to write that implementation out?_

## [](#use-pseudocode-to-clarify-your-thoughts)Use Pseudocode To Clarify Your Thoughts

Unless an algorithm is extremely simple, you'll want to write pseudocode first.

This is especially true for brute-force solutions. The interviewer may be okay with _just_ the pseudocode for the first pass, and could ask you to spend the remaining time solving and coding an optimized solution.

Additionally, thinking in pseudocode is much easier to modify should you find a deleterious error. Here's what it might first look like:  

```
temp = []
zero_count = 0
iterate through array:
  if nonzero, push to new temp
  if zero, increment count
for zero_count times:
  push to temp
return temp
```

It's a good sign you're on the right track if the interviewer modifies the problem to make it a bit more complicated. They might do this by adding a constraint (do this in constant time), or by making the input significantly larger. _In my experience, most interviewers will plan to do one easy problem and one harder problem._

> _Interviewer: Great, now can you do this without instantiating a new array?_

Don't lose your cool at this point, and also don't get too excited about passing the first part. It's time to tie our brute force solution to a technique to improve it. We will now cover a number of ways to do so.

## [](#how-to-optimize-with-patterns-and-abstractions)How to Optimize With Patterns and Abstractions

After you've done about ~50-100 practice interview challenges, you'll begin to recognize patterns you can leverage. Here's an example of one: `If you want speed, you usually need more space/memory.` This is especially relevant to the next section about using a data structure.

Look at each step in your solution so far and think about any potential ways to simplify it or break it down. Are there any ways to reduce its complexity?

One trick is to think about what you're doing from a higher-level. By this, I mean get yourself out of the weeds of the logic, and go back to input-to-output. In the above example, yes we're moving zeros to the end by concatenating arrays, but what are the actual things we'll need to do? The process might be thought of as:

*   Identify the non-zero elements
*   Put elements at different indexes
*   Find out how many `0`s there are

The beauty of having clear steps like the above is that _you can now explore alternative ways to accomplish each one_.

*   For example, to identify the non-zero elements, you can iterate over the array and use a conditional.
*   Alternatively, you can use a `filter` method.
*   And if that's not helpful, you can also look for multiple `zeros` in a row and `splice` a new array out.

Something else to ask yourself: `What am I trying to do in plain English?`

Another very easy way to make progress is to **try to futz with the input.**

*   If it's a collection, does _sorting_ or _grouping_ help?
*   If it's a tree, can we transform it into an array or a linked list?

[![](https://res.cloudinary.com/practicaldev/image/fetch/s--lZy6Pgmk--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://images.pexels.com/photos/45883/cable-computer-sata-s-ata-45883.jpeg%3Fauto%3Dcompress%26cs%3Dtinysrgb%26dpr%3D2%26h%3D650%26w%3D940)](https://res.cloudinary.com/practicaldev/image/fetch/s--lZy6Pgmk--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://images.pexels.com/photos/45883/cable-computer-sata-s-ata-45883.jpeg%3Fauto%3Dcompress%26cs%3Dtinysrgb%26dpr%3D2%26h%3D650%26w%3D940)

If tweaking the input doesn't make a dent, maybe it's time to make a bigger transformation.

## [](#introduce-a-data-structure-or-abstract-data-type)Introduce a Data Structure or Abstract Data Type

This is where a study of data structures (and experience implementing and using them) really helps. If you can identify the bottleneck, you can start to try to throw data structures at the problem to see if there are any performance or spatial gains.

Going back to the [Zeros to the End](https://algodaily.com/challenges/zeros-to-the-end) problem we did earlier, our bottleneck is likely the step of `putting elements at different indexes`. In that case, we may realize that using a `counter` variable is beneficial.

_Note that the `data structure` doesn't need to be fancy. In our case, we're literally introducing a single `int` variable-- but sometimes that's all you need._

What should the `counter` be counting? Well, once we've split the array up into non-zeros (`[1, 2, 3]`) and zeros (`[0, 0, 0]`), we only really care about where the non-zeros end.

Because we don't need to worry about what is in the array after non-zero elements, we can simply keep a separate pointer to track the index of the final array. It will let us know where to start the zeros.

We could then write the follow pseudocode to utilize this strategy:  

```
insert_position = 0
for i in nums
  if i is not 0
    increase insert_position
    keep it in insert_position
  fill the rest in with 0
```

Despite having two loops, the time complexity simplifies to `O(n)`. However, the space complexity is constant since we're using the same array, so we have an improvement!

[![](https://res.cloudinary.com/practicaldev/image/fetch/s--UzMuJQMe--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.imgur.com/W4mdIiN.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--UzMuJQMe--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.imgur.com/W4mdIiN.png)

## [](#a-tactical-data-structure-cheatsheet)A Tactical Data Structure Cheatsheet

Need access to an element in a collection really fast? **An array already has the location in memory.**

Have to insert data quickly? **Add it to a hash table or linked list.**

Need a maximum or minimum in O(1) time? **Call in a heap.**

Need to model connections? **Get a [`graph`](https://algodaily.com/lessons/simple-reference-to-graphs) in there.**

[![](https://res.cloudinary.com/practicaldev/image/fetch/s--GwY5kjmx--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://images.pexels.com/photos/533189/pexels-photo-533189.jpeg%3Fauto%3Dcompress%26cs%3Dtinysrgb%26dpr%3D2%26h%3D650%26w%3D940)](https://res.cloudinary.com/practicaldev/image/fetch/s--GwY5kjmx--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://images.pexels.com/photos/533189/pexels-photo-533189.jpeg%3Fauto%3Dcompress%26cs%3Dtinysrgb%26dpr%3D2%26h%3D650%26w%3D940)

The more data structures you know, the better. You can check [the curriculum](https://algodaily.com/curriculum) for a list of absolute requirements.

It's also useful (but not necessary) to play with more advanced structures-- think AVL trees, tries, priority queues, suffix arrays, and bloom filters. They are less likely to be needed, but they are useful in industry and can be impressive to pull out during an interview.

**A special note about hash tables:**

_Get to know these guys very well! They can be used in a surprising number of solutions. Many problems can be reduced to searching for elements in a large data collection, finding duplicates in said collection, or storing/retrieving items. Hash tables/hash maps do these things extremely well, so always have it top of mind._

If an additional `data structure` doesn't help, it may be time to try out an old-school (but reliable) technique.

## [](#introduce-a-computer-science-algorithm-technique)Introduce a Computer Science Algorithm Technique

There are a few techniques that everyone should be aware of. Usually these are covered in `Intro to Algorithms` classes to categorize algorithms.

They are generally tools not just beneficial for interviews, but for software engineering work in general, so get to know them!

**Divide and Conquer**: [try to divide the problem](https://algodaily.com/lessons/problem-solving-with-recursion-vs-iteration) into sub-problems that are easier to think through or solve. This allows for the possibility of..

**Recursion** - see if you can leverage a function that calls on itself. Be especially wary of [`recursion`](https://algodaily.com/lessons/a-primer-on-recursion) for trees.

**Memo-ization**\- Can the partial results you've generated in the brute force solution can be used for larger or different inputs? [If so, leverage caching of some sort](https://algodaily.com/lessons/memoization-in-dynamic-programming). What data can you store in memory (or create and store in memory) to help facilitate the algorithm?

**Greedy** - think about what the best move at each iteration or step is. Is there an obvious one at each step? This comes up a lot in [`graph`](https://algodaily.com/lessons/simple-reference-to-graphs) traversal problems like Dijkstra's algorithm.

## [](#what-to-do-when-none-of-the-above-worked)What to Do When None Of the Above Worked

So none of the above patterns, data structures, or techniques are shining any light on the problem. What to do?

You have two options.

**Ask more questions.**

OR

**Say, I'm stuck. Can I please get a hint?**

Keep communicating! Interviewers are usually more than happy to give a hint-- in fact, that's their job. Certain interview questions will unfortunately have one or two "key intuitions" that you must grok before you can get to a solution.

## [](#after-you-have-a-working-solution)After You Have A Working Solution

Here's a huge key that takes a while to click. After you've written pseudocode for an optimized solution, **manually run through 1-3 example inputs, step by step, through your pseudocode to make sure it works**. Warning: nerves will be there, and you may lose your place from time to time, but this is extremely important.

Good engineers test their code thoroughly and can step through logic. The space between having a pseudocode solution and writing code on the whiteboard is a good time to demonstrate this.

At this point, you'll also be able to weed out incorrect assumptions or make important realizations ("oh wait, we should use a `Map` instead of a JS object instead").

> _Candidate: Let's start with `[1, 0, 3]`, I think that's a good test candidate. OK, starting with `1`, we see that it's not a zero, so it can stay put. We're going to the next element so let's increment our final array index counter. Now we have `0`, let's skip. OK, `3`, not a zero, our counter is at `1` so we put it after `1` and we have `[1, 3]`. Great! Then we put a `0` at the end and we get the results we want._

The interviewer will likely say something like "great, let's code it up", or they may try to find out how confident you are in your solution. If the input-outputs check in, you should feel good about moving on.

Note: if you're going to be interviewing on a whiteboard, buy a [Magnetic White Board Dry](https://www.amazon.com/gp/product/B075LLKL9F/ref=as_li_qf_asin_il_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B075LLKL9F&linkCode=as2&tag=algodaily03-20&linkId=112235175903de2af465b96357b3c5d4) and practice handwriting code on it.

There's many things that people don't consider about coding on a whiteboard: space management mostly, but also how to use shorter variables, and writing horizontally.

Anyway, you've now written this code:  

```
function zerosToEnd(nums) {
    let insertPos = 0;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] != 0) {
            nums[insertPos++] = nums[i];
        }
    }

    for (let j = insertPos; j < nums.length; j++) {
        nums[j] = 0;
    }

    return nums;
}
```

Once you've written your solution code out, the technical portion should be done.

The interview will now steer towards questions for the interviewer. Make sure that you have questions prepped, and try your best not to think about your performance.

At that point, whatever happened is out of your control, so be forward looking and keep your mind in the present with the interviewer. You'll come across as much more professional if you can maintain your composure, even if the interview didn't go exactly how you wanted.

I hope you've found this guide helpful. Remember that any coding challenge can be solved with the right approach, and the right mentality. Best of luck!

_This lesson was originally published at [https://algodaily.com](https://algodaily.com/lessons/how-to-get-better-at-coding-interviews), where I maintain a technical interview course and write think-pieces for ambitious developers._
