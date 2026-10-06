---
url: "http://stevehanov.ca/blog/index.php?id=105"
captured_at: "2010-09-15T06:34:31-03:00"
title: "Finding awesome developers in programming interviews - Steve Hanov's Programming Blog"
domain: "stevehanov-ca"
---

**[Finding awesome developers in programming interviews](http://stevehanov.ca/blog/?id=105)**

Posted on: 2010-09-13 18:00:00

In a job interview, I once asked a very experienced embedded software developer to write a program that reverses a string and prints it on the screen. He struggled with this basic task. This man was awesome. Give him a bucket of spare parts, and he could build a robot and program it to navigate around the room. He had worked on satellites that are now in *actual orbit.* He could have coded circles around me. But the one thing that he had never, ever needed to do was: display something on the screen.

Some people have a knack for asking the right questions to spot awesome developers in a job interview. Other interviewers dread it, come in with their tail between their legs, ask a few questions from the Internet and just go along with the group decision. But interviewing is an essential skill for most developers. A bad hire has terrible long term consequences, because eventually a sub-par employee may bring others into the organization. On the other hand, unfairly excluding an awesome candidate also hurts.

A programming interview includes at least three parts. In part I, we prove any assumptions we have after reading the resume. In part II, we get a sense for how much **true experience** the candidate has. Finally, we test this experience using a few spot checks and a coding question.

**Part I: Testing assumptions from the resume**

Once I was intervewing a candidate along with a fellow co-worker. When it was done, I thought the candidate had done okay, but not brilliantly. My co-worker, on the other hand, seemed angry. "He lied about technology X. He obviously has not worked with it. Definately a no-hire." Technology X was not even important to us. *"If he lied about that,"* my co-worker went on, *"I don't trust anything else on the resume."*

Candidates *should* use the resume to portray themselves in a positive light. However, there is a line where this positive portrayal becomes misrepresentation. In the example above, I wasn't as concerned as my colleague, because I already assume that everything on the resume is false until proven otherwise. If the resume says, "expert in technology X", then I will assume that the candidate merely knows the *name* of technology X. If the resume says, "Worked in a group that created a multi-threaded stock trading platform," then I will assume that the candidate merely chose the colours for the background. I used to be less strict until I met the guy with 10 years of experience who couldn't write code. If someone says that they wrote the text formatter in OpenOffice, or has a Ph.D, it is easy to make assumptions about their skills. **Assume nothing. All must be tested.**

For each relevant item on the resume, I first try to get a sense of what the candidate actually did. Then, I get him or her to prove it by talking about it.

- Created a real-time operating system as a course project.  
  *How large a group did you work in? A group of 15? Oh, okay then, what specific part did you work on? The message queue? Great! Can you describe what happens when a high priority task sends a message to a low priority task?*
- Developed from scratch an audio transfer protocol for wireless security systems.  
  *How large was your team? Just you? Wow, how did you test it? Why didn’t you use RTP?*
- Fixed bugs in the XYZEngine.  
  *Can you describe a bug that you found particularly challenging, and how you fixed it?*

**Part II: Finding****true experience**

Having more experience is a good indication of awesomeness. Experienced developers have made mistakes. They know when, and when not to apply design patterns. They have a sixth sense about what part of requirements will probably change, and what part will probably stay the same. They know when to be lazy and when to be pedantic. It is *true* experience which makes the gap between awesome and mediocre programmers so wide.

![4634b356178c32be18cd0933a40e3488.png](stevehanov-ca--finding-awesome-developers-in-programming-interviews/4634b356178c32be18cd0933a40e3488.png)

But not all experience is the same. It is certainly possible for someone to gain solid skills in a couple of years, simply by working on lots of different things, writing and rewriting countless lines of code, and making many mistakes. On the other hand, it is also possible for someone to spend a decade writing one-line changes to a single project, without learning anything new.

![cf93f80a3bec128373ea0626f6155c8c.png](stevehanov-ca--finding-awesome-developers-in-programming-interviews/cf93f80a3bec128373ea0626f6155c8c.png)

**Finding hidden time**

There are lots of great developers who started coding when they were in their second year of university. By the time they get out of school, they will have had a few years of experience. On the other hand, some awesome developers started learning their art at an early age. I know several people who wrote some non-trivial programs in their teens or earlier. This information is nowhere to be found on their resume, and must be coaxed out during an interview.

- Why did you get into the software development field?
- What's the first programming language that you ever learned?

**Density of Experience**

Many awesome programmers do all of their coding at work. These are great, well, rounded individuals that you should definitely hire. However, doing personal programming projects outside of work or class is a pretty good indicator of awesomeness. A candidate with personal programming time simply has more flight time under his or her belt, and will be better for it. No personal projects? These other indicators will also count for some points:

- Working on smaller teams or groups.
- Working on a wide variety of projects
- Detailed knowledge of several layers of abstraction on a large project
- Being the main contributor in a group project

**Part III: Verifying experience**

After gaining a sense of the candidate's true level of experience, it is important to verify that experience testing their programming abilities. A few minutes of time is completely inadequate for a true test, but that's all that's available. We can get an idea of the breadth and depth of knowledge of the candidate by asking questions about different areas of software development. Of course your perception of the candidate's skills will be biased by your own experiences. You cannot judge the correctness of answers in topics that are unfamiliar to you. That's why there are several interviewers.

The specific topics depend on the job requirements. Nevertheless, some example areas are:

- data structures and algorithms
- multithreading
- bit manipulation
- memory allocation
- objects and inheritance, design patterns
- recursion
- compilation and how computers run programs

Each area that I choose has a selection of basic questions (“What’s a semaphore?”). These are so basic that if the candidate has done any work at all in the area he or she would be able to answer. Each area also has some more detailed follow-up questions. The way in which a candidate answers can prove or disprove awesomeness. For example something is amiss if you ask a seasoned embedded programmer to convert 0x4c to binary, and they start by writing down 4 x 16 + 12.

**The Coding Question**

Usually, after all of the above, I have a very good idea whether the candidate will pass or fail, but the coding question removes all doubt. It is so important, that even phone interviews are not exempt. To be useful, a coding question requires careful thought and planning before the interview. Asked the wrong way, the response will be useless.

First, one must choose a question based on what the candidate has had experience with. You may have a clever problem that becomes easy if you think of converting everything to intersecting 3D planes. Save it for the lunch hour with your colleagues. If the job does not involved 3D graphics, candidates would be unfairly excluded.

The question must be precisely worded. "Write a function to shuffle a deck of cards" is woefully ambiguous. Provide the function header and avoid misunderstandings, which are all too common. If you are not careful, the candidate will answer a harder or easier problem than the one you asked. The harder one is nice, unless it causes him or her to freeze up. The easier one provides no information. To prevent a huge waste of time, ask for a verbal outline of the solution after a few minutes, to check if the candidate is on the right track.

**Going further**

The guidelines above *do not address everything*. They focus on experience, and they might miss awesome developers that have little experience, but a lot of innate ability. In particular, interviewers may want to test problem solving ability using puzzles that don't require any coding.

The interviewing technique that I have described here is based on proving a hypothesis, probability, and gut instinct. The hypothesis is that the candidate is an awesome developer. What traits does an awesome developer have? You cannot directly measure those traits, so you have to instead ask: What is the probability that the candidate has those traits given that he or she can answer a particular question quickly? It is not possible to assess a candidate within an interview with 100% success, but by asking thoughtful questions, you can come close.
