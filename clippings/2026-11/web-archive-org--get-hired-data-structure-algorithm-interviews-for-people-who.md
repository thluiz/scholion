---
url: "https://web.archive.org/web/20200304131150id_/https://dev.to/techdebtor/get-hired-data-structure-and-algorithm-interviews-for-people-who-hate-them-32ga"
captured_at: "2026-11-16T07:47:59+00:00"
title: "Get Hired: Data Structure and Algorithm Interviews For People Who Hate Them"
domain: "web-archive-org"
---

I'm gonna be honest: I hate data structure and algorithm (DSA) interviews. Between phone interviews and on-sites I must have done 30+ of them during my recent job search, and every single time I felt like I was going to vomit. To my friends outside the tech industry, I describe them as taking a final exam on a whiteboard while somebody deciding the fate of your career watches. But y'all, a girl needed a job, so I had no choice but to suck it up and do them. I learned some techniques that made them bearable and went from bombing them to landing a job at my dream company.

One thing that helped me in this process was my experience on the other side of the table. When I worked at Salesforce, I administered DSA interviews. I'd say I've given 15-20 in the past 3 years.

Now that I've gotten through to the other side, I want to share what I've learned. I can’t teach you all the major data structures and algorithms in a blog post, so that’s not what I’m going to do here. I want to walk you through the DSA interview from both sides. Then I'll share what helped me study and provide resources to help you too. I'll also give you my thoughts about the whole process and share some red flags that can indicate deeper problems at the company. I hope that I can demystify the interview process and make you hate it a little bit less.

## [](#interview-format)Interview Format

First off, let's define what I mean by a DSA interview. I'm referring to a specific type of interview format where the interviewee is given a programming question and the solution involves using data structures (such as arrays, maps, and trees) and/or common algorithms (such as sorting and searching). Some example questions include reversing an array and printing a binary tree in ascending order. The questions are self-contained and focus on solving a problem as a stand-alone function. They can be rather abstract and are not necessarily problems you'll encounter on your day-to-day job. DSA interviews can be administered as phone interviews where you live code in a shared browser-based IDE, or they can be done in-person on a whiteboard. Interviews typically consist of 2-3 questions that are expected to take 20-30 minutes each to solve.

Why do companies do DSA interviews? Well, there's a philosophy among many companies that an engineer who is good at the "fundamentals" will be good at any job you put them in. One upside is that the result of the interview is independent of any team you may join. Many large companies don't match new hires with teams until late in the interview process, so their interviews test candidates for skills that are applicable across a broad swath of teams. My opinion is that engineers who do well in DSA interviews typically do well on the job, but DSA interviews also filter out candidates who may have done well on the job but lacked the skill of interviewing. But good news - **interviewing is a learnable skill.** More on that later 🦄

## [](#anatomy-of-an-interview)Anatomy of an Interview

#### [](#interviewers-side)Interviewer's Side

Let's walk through an actual DSA interview question I used to ask to senior engineers and go over what my expectations of the candidate were.

##### [](#question-given-an-unsorted-array-of-integers-find-all-unique-pairs-of-numbers-that-add-up-to-a-value-k)Question: Given an unsorted array of integers, find all unique pairs of numbers that add up to a value k.

Why did I pick this question? I like that it has multiple solutions of varying [time complexity](https://www.interviewcake.com/article/java/big-o-notation-time-and-space-complexity). There's a brute force solution that's O(N2), a sorting solution that's O(NlogN), and a hash map (also called a hash table, dictionary, or just a map) solution that's O(N). This means that a candidate can work through the problem even if their solution isn't the best possible solution. I also like that the optimal solution uses a hash map, which is a data structure we use every day. The question is practical in that it shows whether the candidate understands an important data structure, but also abstract enough that it's not tied to any work they'd be doing on my team.

The steps for the best solution would be:

*   Initialize a map of integers and a list of integer pairs.
*   Iterate through the input array and put each integer into the map as the key, with the number of occurrences as the value. Each time you see a given integer in the array, increment its occurrences value in the map.
*   Iterate through the map. For each value v, check if the map contains the integer k - v. If so, put the pair (v, k - v) in the pair list and remove both values from the map. Special case: If k = 2v, make sure there are at least 2 occurrences of v in the map (i.e. map.get(v) >= 2)
*   Return the pair list.

I wrote this as a list of steps in English rather than in code because **you should be able to articulate your solution out loud before you start coding.** You definitely don't have to be this detailed, but at the minimum you need to communicate that you're going to use a hash map to keep count of the numbers in the array and then iterate through the map to find pairs. This way, I can give you feedback on whether this is the best solution before you write anything down.

As you're coding, I will try to help you when you get stuck and nudge you in the right direction. I may ask questions to clarify your approach or suggest test cases.

I typically give candidates 30 minutes for this question. Once those 30 minutes are up, I let them finish their thoughts and then we move on to the next question, which could either be technical or non-technical depending on how the interview schedule is broken up for the day.

#### [](#candidates-side)Candidate's Side

Now let's talk about what you, the candidate, should be doing.

After I read you the question, you should take a moment to gather your thoughts. Don't feel pressured to respond right away. Once you're ready, ask me some clarifying questions. Some questions you could ask for this question would be "how big is the array?" and "is the pair (4,6) considered the same as the pair (6,4)?" Make sure you understand what the question is asking you to do.

Next, before you even think about code, walk through some example inputs. If this is a phone interview, type out a few examples, and if this is on a whiteboard, write them down. For this question, let's say you pick the array \[1, 2, 3, 0, 1\] and the value k = 2. The set of all unique pairs that add up to 2 would be (1, 1) and (2, 0). So by working through this example, you can see you need some way to match up combinations of the numbers in the array.

So now, you can move on to a brute force solution. It's a nested for-loop where the outer loop selects an element in the array and the inner loop iterates through the rest of the array looking for a match. I'd suggest first verbally describing a brute force solution to your interviewer before writing anything down. This is because your brute force solution should be the starting point for solving the question - it's your fallback in case your other solutions don't pan out. Your interviewer may want you to explore some more options before writing anything down.

Now you optimize your solution. **This is the key to passing a DSA interview.** Ask yourself if any data structures can help. **"Can I use an array, a set, a list, a map, a stack, a queue, a tree, or a graph?"** Then ask if any common algorithms would help. **"Would sorting, searching, using recursion, or dynamic programming help?"** The vast majority of the time, the answer is going to lie somewhere in those two lists.

The key to getting the optimal solution to this problem is optimizing the time it takes to figure out whether or not a number's match is in the array. Hash maps have a retrieval time of O(1), so that's a hint that they might be helpful here. Next up is figuring out what values the hash map should hold. The numbers from the array need to go in the map, but since map entries are unique, we'll lose information about how many times the number appears in the array when we put it in the map. (We need this information for dealing with duplicates.) So we'll make the entry's key the number itself, and the entry's value will be the number of times that number appears in the array. From there, we can turn this into a full-fledged solution by filling in the gaps.

So now you have a solution written down, but your work isn't done yet. You must test that your solution actually works. I'd recommend walking through a few negative test cases - input is null, input is an empty array - and a few positive test cases - input is \[1, 1\], input is \[1, 2, 3\], input is \[-1, 1\]. This is your chance to catch your bugs before your interviewer does.

At this point, you have a well-tested, performant solution. Nice! Your interviewer may ask you some follow-up questions and then you'll move on to the next interview question.

## [](#red-flags)Red Flags

I outlined a basic but fairly common interview process above. Interviewers should be engaged and helpful, working with the candidate as a team. However, it doesn't always work out that way. Here are some red flags to look out for:

1.  The interviewer is unengaged.  
    The interviewer indicates they don't want to be there. They don't pay attention to you and instead are on their phone or laptop. This can be the result of one of a few things. It could be that the interviewer does want to be there but is overworked and can't take an hour away from work to interview you. This is a red flag because it means you're also going to be that level of busy all the time. It could also be that the interviewer actually doesn't care, and they're only there because they're required to be - being on the hiring committee is often a prerequisite for senior-level promotions. That's a red flag because something is broken in their interview process - you should have your interviewer's full attention for the entirety of your interview.
    
2.  The interviewer is condescending.  
    Here's a dirty secret: companies know they hire assholes, and they know who the assholes in the company are. If a company puts an asshole on an interview panel, that means they value a known asshole's opinion. And guess what: that asshole's opinion is ALWAYS going to matter. You're going to have to run decisions by this person, they'll be on your code reviews, and you'll have to appease them in meetings. Remember that when a company is interviewing you, you're interviewing the company too. If your interviewer is condescending, rude, or judgmental of your performance, expect to receive that treatment for your entire tenure at that company.
    
3.  The interview question's solution involves an obscure data structure or algorithm.  
    I was asked a whiteboarding question in an on-site interview where the solution was to use a min heap while parsing an array. I have never used a min heap in my professional life. In fact, between the hundreds of software engineers I know in real life and on Twitter, I couldn’t find a single person who had. This is a red flag because the company is looking for a candidate who has read a textbook on computer science, not one who has actually worked as a software engineer. **Interview questions shouldn't be measuring whether you passed a university-level data structures class.** They should be measuring whether you can succeed at an abstraction of your job.
    

## [](#preparing-for-the-interview)Preparing for the Interview

I mentioned above that **interviewing is a learnable skill.** And it absolutely is. You just need to study the types of questions that will be asked in an interview and practice answering questions in the same format as an interview.

My top piece of advice for anyone preparing for a DSA interview is to **pratice writing code outside of an IDE.** The canonical recommendation is to get a copy of Cracking the Coding Interview by Gayle Laakmann McDowell and write your solutions in pen and paper. I've also listed some web resources where you can solve code puzzles below.

Also incredibly important is to **practice talking while you code.** You will feel stupid at first. But it's vital to do it in an interview to let the interviewer know what you're thinking. As much as your interviewer is judging your coding skills, they're also judging your communication skills.

For me, the hardest part of the interview is that **my mind goes blank.** One thing that gets me through it is having a list of techniques I can fall back on - "Can I use an array, a set, a list, a map, a stack, a queue, a tree, or a graph?" and "Would sorting, searching, using recursion, or dynamic programming help?" Chances are, at least something from those lists will be helpful.

Here are some of the resources I used to prepare for DSA interviews:

*   [js.checkio.org](https://js.checkio.org/) - JavaScript coding puzzles that start at absolute beginner and work up to expert
*   [CodingBat](https://codingbat.com/java) - Beginner to intermediate difficulty Java and Python coding puzzles
*   [HackerRank](https://www.hackerrank.com/) - Intermediate to expert difficulty puzzles in many different languages
*   [LeetCode](https://leetcode.com/) - Intermediate to expert difficulty puzzles in many different languages

Some companies actually administer their DSA interviews through HackerRank and LeetCode, so I'd recommend getting familiar with those two.

## [](#final-thoughts)Final Thoughts

DSA interviews are daunting. You're expected to solve a hard problem under a tight time constraint while being judged by a third party. If you hate them, you're not alone. But with some studying and practicing, you can conquer them.
