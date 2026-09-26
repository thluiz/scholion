---
url: "http://www.acodersjourney.com/2016/05/worst-programming-interview-question-ever/"
captured_at: "2018-11-21T01:09:33+00:00"
title: "The Worst Programming Interview Question I've Ever Seen ! - A CODER'S JOURNEY"
domain: "acodersjourney-com"
---

An interesting topic came up recently  at work – one of my colleagues asked me – what is the worst programming interview question that you’ve faced ?

I’ve been fortunate enough to have not faced any interview question that I thought was BS (except my first interview, which I’ll write about shortly). However, it did remind me of someone I met during an interviewing sprint to hire interns. We’ll call him Jack.

Years ago, Microsoft had this streamlined process to interview prospective interns on campus that looked similar to an assembly line. The idea was simple –

*   gather 40-50 interview candidates from various reputed schools
*   gather 15-20 interviewers (mostly senior engineers) from across the company
*   Create interview teams consisting of 3 interviewers each
*   arrange for a large number of interview rooms in the HR/training building on campus
*   Assign each interview candidate to an interview team
*   Make the candidates go through three interviews , one with each interviewer
*   Make a decision on spot and notify HR

This is where I met Jack. He was a very amicable person to work with and I was pretty happy that he was in my team. After the first set of interviews , we gathered to discuss the results for the first batch of candidates. As part of assigning the final scores, we started discussing the questions we asked each of the candidates.

Jack went on to explain the question he asked the candidate:

**“ Code up an algorithm to give the sum of integers from 1 to 1000 !”**

The obvious solution is to run a for loop from 1 to 1000, and add up the numbers.

I was a little surprised that he was asking such a simplistic question to the candidates. But I thought that maybe he just wants to go easy because he’s hiring interns.

_“So I have to give her a NO-HIRE”__–_ Jack said.  I was a bit surprised because the candidate was from a very reputed CS program in the country.

_“Why is that Jack – was she not able to solve this problem ?”_ I asked.

Jack shrugged his head in disappointment – _“No she gave me a solution all right – she just ran a loop from 1 to 1000. Not the optimized solution I was looking for.”_

This really intrigued me . Wow, I thought, maybe there is an optimal solution to this problem that I don’t know.

Jack continued – _“Well, I was looking for an O(1) solution whereas she gave me a O(n) solution”._

This really intrigued me and the other interviewer on our team, and we kept staring at Jack for the solution.

**Jack said _– “It’s super simple.. there is a formula for it – Sum = \[n(n+1)\]/2 !!!”_**

[![Worst Programming Interview Question](https://i2.wp.com/www.acodersjourney.com/wp-content/uploads/2016/05/AngryDonald-e1464637089181.jpg?resize=300%2C287 "Worst Programming Interview Question")](https://i2.wp.com/www.acodersjourney.com/wp-content/uploads/2016/05/AngryDonald-e1464637089181.jpg)

**_“ WHAT ?!!!?!!! “_** – I almost felt like screaming out. I mean, we’re trying to test candidates on their creative problem solving skills and here was this this guy, testing people on their memorizing ability.

Jack felt our unspoken resentment and went on to explain – “_They should have taken a discrete math course which covers the series formulae. Or even if they haven’t they can apply approximation of areas under a rectangle using Calculus to come up with an  algorithm – they must have taken a course on numerical analysis and algorithms !__”._

After a brief discussion and having failed to convince Jack that the question might not be very well suited for interview candidates, we went back to our respective interview booths.

I don’t know if Jack is still asking the same question to his candidates. It might be a great question for hiring research interns at Microsoft Research or hiring research software development engineers (yes, there is such a thing). I don’t know.

But here are my reasons for disliking this question.

## **1\. There is one specific right solution that the interviewer was looking for.**  

An interview should be really about assessing if a candidate can think for herself. It about gaining insights into the candidate’s approach to solving unknown or unfamiliar problems. It’s about having a candid discussion with the candidate on various aspects of the solution, problem solving methodology and related software engineering issues.

If the interviewer is fixated on a specific solution , or even worse, asks the candidate a question that has only one solution, it leaves no room for discussion. This in turn does not give you any insight into the person’s thinking ability.

**2\. The right solution is in not related to work the candidate would be doing.**

Most of run of the mill software engineering positions involves a lot of algorithms , some data structures (because you rarely write them from scratch) and quite a bit of domain specific knowledge. With interns, you cannot expect too much domain specific knowledge – so the next best thing is to ask them about algorithms and data structures. For example – if you ask a question that can be solved using a tree, hash table, parallel arrays or some other clever trick – the candidate has a fighting chance because he could go down one of the many solution paths. Along the way, you can have a fascinating discussion on the design alternatives and gain some insights into the person’s thinking abilities, knowledge of algorithm analysis and communication skills.

However, IMHO, being able to solve this question using calculus and numerical analysis or approximation is something the intern will not need to do unless they’re in Microsoft Research. And unless you’ve taken those calculus or discrete maths courses specifically, you’re pretty much dead in the water.

**3\. You might hire the wrong person !!!**

**What _if_ the candidate actually solves the problem the exact way Jack wanted ?** That is, she gives him the O(1) solution using the series summation formula.

**You’ve just give a “HIRE” to a person based on their memorization or mathematical aptitude without testing if they can code properly or design algorithms.**

They might be a good memorizer and good mathematician and good programmer all in one – but you as the interviewer don’t know that !

So, in case this person turns out to be a terrible problem solver and programmer, you’ve just put the team you hired for in a very tough spot. Training interns is very expensive . A senior engineer is usually assigned to each intern to mentor them and guide them in their project. For me, this has taken up anywhere between 1-4 hours of my time each day. The reason we invest so much in our interns is because we want to hire them back after graduation. But if you have an intern who is not upto the mark, all that effort, time and money is wasted.

              The problem is only magnified if  you’ve just hired a full time employee based on the answer to that specific question. Everyone knows how expensive it is to train new employees – at Microsoft we train folks for 3-6 months without even expecting them to be really productive during this time. It’s even more expensive and problematic for HR to show someone the door in case he’s not performing well. It also seriously handicaps the ability of the team  to execute if one of their team members  is not carrying his weight. And the list for dangers of a bad hire goes on …

## **_So what type of question should I ask ?_**  

This really depends on the type of position you’re hiring for. Most large companies like Microsoft and Google tend to focus on algorithmic and data structure questions with multiple possible solutions. We always assess how the candidate is able to formulate solutions using the various data structure and algorithmic tools available to him. Along the way, we also check how the candidate communicates his approach and solution, how he’s doing under pressure, whether he tests the finished solution etc. The following three books has some examples of great computer science problems that you can tweak (of course ) for your specific needs and interviews.

1.  [Algorithm Design Manual](http://www.amazon.com/Algorithm-Design-Manual-Steven-Skiena/dp/1848000693/ref=sr_1_1?ie=UTF8&qid=1464635538&sr=8-1&keywords=Algorithm+design+manual) _by Steven S Skiena_
2.  [Algorithms in a Nutshell](http://www.amazon.com/Algorithms-Nutshell-Practical-George-Heineman/dp/1491948922?ie=UTF8&keywords=Algorithms%20in%20a%20nutshell&qid=1464635513&ref_=sr_1_1&sr=8-1) _by George T. Heineman and Gary Pollice_
3.  [Programming Pearls](http://www.amazon.com/Programming-Pearls-2nd-Jon-Bentley/dp/0201657880?ie=UTF8&keywords=Programming%20Pearls&qid=1464635421&ref_=sr_1_1&sr=8-1) _by Jon Bentley_

Good luck in your future hiring endeavors ! Please share if you liked the post 🙂
