---
url: "http://www.hanselman.com/blog/NewInterviewQuestionsForSeniorSoftwareEngineers.aspx"
captured_at: "2014-02-18T13:43:54-03:00"
title: "New Interview Questions for Senior Software Engineers - Scott Hanselman"
domain: "hanselman-com"
---

# [New Interview Questions for Senior Software Engineers](http://www.hanselman.com/blog/NewInterviewQuestionsForSeniorSoftwareEngineers.aspx)

Sponsored By

I'm putting together some practice interview questions for a friend who lost his job. I thought it'd be useful to crowd-source some questions from you, Dear Reader.

These questions should be more software design focused, less technical trivia like my previous two lists of interview questions:

**UPDATE: I think we all agree (or at least we should) that if you go into an interview tomorrow and you look across the table and the interviewer has simply printed out this list and is reading from it, that you should excuse yourself and run. This isn't a "guide to how to interview" nor is this meant to me a "best practices for engineers" list. It's simply a collective brain-dump of stuff that someone who's been in the business of developing software for money for 10 or so years should have some passing familiarity with. Of course, it's assumed that the interviewer is able to detect BS. This isn't, and shouldn't be, a trivia contest. If you're going to get a job (or you're looking for hire someone for a job) it's ultimately more important to understand if someone can Solve Problems and if Their Head is Screwed on Straight. Take it with a grain of salt, friends, remember, you found it on the Internet. - @**[**shanselman**](http://www.twitter.com/shanselman)

Here's what I have so far.

- What is something substantive that you've done to improve as a developer in your career?
- Would you call yourself a craftsman (craftsperson) and what does that word mean to you?
- Implement a <basic data structure> using <some language> on <paper|whiteboard|notepad>.
- What is SOLID?
- Why is the Single Responsibility Principle important?
- What is Inversion of Control? How does that relate to dependency injection?
- How does a 3 tier application differ from a 2 tier one?
- Why are interfaces important?
- What is the Repository pattern? The Factory Pattern? Why are patterns important?
- What are some examples of anti-patterns?
- Who are the Gang of Four? Why should you care?
- How do the MVP, MVC, and MVVM patterns relate? When are they appropriate?
- Explain the concept of Separation of Concerns and it's pros and cons.
- Name three primary attributes of object-oriented design. Describe what they mean and why they're important.
- Describe a pattern that is NOT the Factory Pattern? How is it used and when?
- You have just been put in charge of a legacy code project with maintainability problems. What kind of things would you look to improve to get the project on a stable footing?
- Show me a portfolio of all the applications you worked on, and tell me how you contributed to design them.
- What are some alternate ways to store data other than a relational database? Why would you do that, and what are the trade-offs?
- Explain the concept of convention over configuration, and talk about an example of convention over configuration you have seen in the wild.
- Explain the differences between stateless and stateful systems, and impacts of state on parallelism.
- Discuss the differences between Mocks and Stubs/Fakes and where you might use them (answers aren't that important here, just the discussion that would ensue).
- Discuss the concept of YAGNI and explain something you did recently that adhered to this practice.
- Explain what is meant by a sandbox, why you would use one, and identify examples of sandboxes in the wild.
- Concurrency
  - What's the difference between Locking and Lockless (Optimistic and Pessimistic) concurrency models?
  - What kinds of problems can you hit with locking model? And a lockless model?
  - What trade offs do you have for resource contention?
  - How might a task-based model differ from a threaded model?
  - What's the difference between asynchrony and concurrency?
- Are you still writing code? Do you love it?
- You've just been assigned to a project in a new technology how would you get started?
- How does the addition of Service Orientation change systems? When is it appropriate to use?
- What do you do to stay abreast of the latest technologies and tools?
- What is the difference between "set" logic, and "procedural" logic. When would you use each one and why?
- What Source Control systems have you worked with?
- What is Continuous Integration?  Have you used it and why is it important?
- Describe a software development life cycle that you've managed.
- How do you react to people criticizing your code/documents?
- Whose blogs or podcasts do you follow? Do you blog or podcast?
- Tell me about some of your hobby projects that you've written in your off time.
- What is the last programming book you read?
- Describe, in as much detail as you think is relevant, as deeply as you can, what happens when I type "cnn.com" into a browser and press "Go".
- Describe the structure and contents of a design document, or a set of design documents, for a multi-tiered web application.
- What's so great about <cool web technology of the day>?
- How can you stop your DBA from making off with a list of your users’ passwords?
- What do you do when you get stuck with a problem you can't solve?
- If your database was under a lot of strain, what are the first few things you might consider to speed it up?
- What is SQL injection?
- What's the difference between unit test and integration test?
- Tell me about 3 times you failed.
- What is Refactoring ? Have you used it and it is important? Name three common refactorings.
- You have two computers, and you want to get data from one to the other. How could you do it?
- Left to your own devices, what would you create?
- Given Time, Cost, Client satisfaction and Best Practices, how will you prioritize them for a project you are working on? Explain why.
- What's the difference between a web server, web farm and web garden? How would your web application need to change for each?
- What value do daily builds, automated testing, and peer reviews add to a project? What disadvantages are there?
- What elements of OO design are most prone to abuse? How would you mitigate that?
- When do you know your code is ready for production?
- What's YAGNI? Is this list of questions an example?
- Describe to me some bad code you've read or inherited lately.

Your thoughts? I'll add good questions from the comments throughout the day.

#### About Scott

Scott Hanselman is a former professor, former Chief Architect in finance, now speaker, consultant, father, diabetic, and Microsoft employee. I am a failed stand-up comic, a cornrower, and a book author.

[About](http://hanselman.com/about)   [Newsletter](http://www.hanselman.com/newsletter)

Thursday, February 17, 2011 7:34:29 PM UTC

What is the difference between TDD and BDD?

![](http://www.gravatar.com/avatar.php?gravatar_id=7c4f77e02bae85569daf4fe474f2efae&rating=PG&size=110&default=identicon)

Thursday, February 17, 2011 7:36:45 PM UTC

One I generally like is:  
  
Name three primary attributes of object-oriented design. Describe what they mean and why they're important.  
  
It amazes me how so many developers out there think that OO is nothing more than "classes with methods/members on them" and maybe "inheritance for sharing functionality." Also, I've found myself in some really interesting conversations with good developers on this subject. It segues pretty well into other topics too, such as some SOLID principles and interfaces.

![](http://www.gravatar.com/avatar.php?gravatar_id=648c8bba6edab74d2ef100f96636fcd0&rating=PG&size=110&default=identicon)

Thursday, February 17, 2011 7:38:09 PM UTC

Whenever I ask an about patterns in an interview 95% of the candidates will answer with the factory pattern. Ask them to describe a pattern that is NOT the factory pattern. (i.e. Decorator/Strategy/etc... ). This is where you will find most of the junior engineers will not be able to identify another pattern.

Thursday, February 17, 2011 7:38:13 PM UTC

Why is the phrase "being like Hanselman" considered a compliment?

![](http://www.gravatar.com/avatar.php?gravatar_id=723367994c323fecddda7a26683f2e67&rating=PG&size=110&default=identicon)Haddicus

Thursday, February 17, 2011 7:39:51 PM UTC

You have just been put in charge of a legacy code project with maintainability problems. What kind of things would you look to improve to get the project on a stable footing?

![](http://www.gravatar.com/avatar.php?gravatar_id=764e226cad54619d332428e11acaa932&rating=PG&size=110&default=identicon)KevDog

Thursday, February 17, 2011 7:40:03 PM UTC

Most of the questions here and on the other posts you referred to are great for gauging competency. Overall they're pretty similar to questions I've been asked when I applied a Microsoft and other companies.  
  
The one challenged I've had is that a lot of these concepts weren't covered in my college courses and many of these concepts haven't really come up in my career as a developer. Do you have any good recommendations for resources to learn more about these topics? I'd like to expand my horizons, but it's often tough to find articles and resources that focus on concepts rather than implementations.

![](http://www.gravatar.com/avatar.php?gravatar_id=b231e07e868d33adca6135fc54ca06ec&rating=PG&size=110&default=identicon)Ian

Thursday, February 17, 2011 7:41:10 PM UTC

While I had used most of these patterns at one time or another (and many of them I had discovered on my own in struggling through design problems), it wasn't until fairly recently that I learned that they had names. I recommend being careful not to quiz interviewees on specific patterns by name, and instead focus on their ability to problem solve. For example, give them a scenario when inversion of control might be needed, and see how they reason through it.

![](http://www.gravatar.com/avatar.php?gravatar_id=c7e9f7440f7f70379e72bb28f8b5ca67&rating=PG&size=110&default=identicon)[Dale Barnard](http://dalebarnardonwpf.wordpress.com/)

Thursday, February 17, 2011 7:41:24 PM UTC

I'm not to keen on the anti-pattern question. Anti-patterns can be patterns in certain contexts and the other way around. I think I would only be able to come up with two anti patterns in an interview, service locator and singleton. Both of these patterns has valid use cases.

![](http://www.gravatar.com/avatar.php?gravatar_id=6f938d827bec94dc8e3ea7263d5af9e5&rating=PG&size=110&default=identicon)

Thursday, February 17, 2011 7:41:28 PM UTC

I got asked the last one at an interview today, and it was for a junior position. Caught me out completely, so it's most likely a good question to ask.   
  
I'm poor at remembering theory. Advantages and disadvantages etc, purpose of things, sometimes interviews are a nightmare!

![](http://www.gravatar.com/avatar.php?gravatar_id=8ab980b87b44c231c79701196c65a2cc&rating=PG&size=110&default=identicon)Andy

Thursday, February 17, 2011 7:42:51 PM UTC

Show me a portfolio of all the applications you worked on, and tell me how you contributed to design them. Isn't it the only question that really matters?

![](http://www.gravatar.com/avatar.php?gravatar_id=86358e3a223c4eabd68d713e053ceb34&rating=PG&size=110&default=identicon)

Thursday, February 17, 2011 7:44:54 PM UTC

Ian - Awesome question. I'm going to think about this and how it can be done.

![](http://www.gravatar.com/avatar.php?gravatar_id=719c91f5c3013e43ee46ed2bdc67f883&rating=PG&size=110&default=identicon)[Scott Hanselman](http://www.hanselman.com)

Thursday, February 17, 2011 7:46:00 PM UTC

Patrik - I agree with your point, but I also think it's worth having those kinds of discussions. I would say there is no right or wrong answer for some of these.

![](http://www.gravatar.com/avatar.php?gravatar_id=719c91f5c3013e43ee46ed2bdc67f883&rating=PG&size=110&default=identicon)[Scott Hanselman](http://www.hanselman.com)

Thursday, February 17, 2011 7:48:56 PM UTC

Could not agree more with David !  
And based on \_that\_ answer you can start digging for things like patterns etc ... the person used during these projects.

![](http://www.gravatar.com/avatar.php?gravatar_id=46ef06169eda546d72280f9521f9ddb0&rating=PG&size=110&default=identicon)Bart De Keersmaeker

Thursday, February 17, 2011 7:49:56 PM UTC

What are some alternate ways to store data other than a relational database? Why would you do that, and what are the trade-offs?

jarodf

Thursday, February 17, 2011 7:51:45 PM UTC

I fail to see the relevancy of a 70's rock band to programming http://www.gangoffour.co.uk - I'm afraid I lose here :)

![](http://www.gravatar.com/avatar.php?gravatar_id=3eda6fcd3204ef285fa52176c28c4d3e&rating=PG&size=110&default=identicon)

Thursday, February 17, 2011 7:52:06 PM UTC

Explain the concept of convention over configuration, and talk about an example of convention over configuration you have seen in the wild.  
  
Explain the differences between stateless and stateful systems, and impacts of state on paralellism.  
  
Discuss the differences between Mocks and Stubs/Fakes and where you might use them (answers aren't that important here, just the discussion that would ensue).  
  
Discuss the concept of YAGNI and explain something you did recently that adhered to this practice.  
  
Explain what is meant by a sandbox, why you would use one, and identify examples of sandboxes in the wild.

![](http://www.gravatar.com/avatar.php?gravatar_id=fe5ef732ebda902e666b2f2ea197bc2c&rating=PG&size=110&default=identicon)

Thursday, February 17, 2011 7:53:06 PM UTC

David has a great point. I've long said that rather than certifications and degrees after our names, we should put projects.  
  
Signed,  
Scott Hanselman, 23 successful projects, 3 failed

![](http://www.gravatar.com/avatar.php?gravatar_id=719c91f5c3013e43ee46ed2bdc67f883&rating=PG&size=110&default=identicon)[Scott Hanselman](http://www.hanselman.com)

Thursday, February 17, 2011 7:53:55 PM UTC

Bittercoder - I love these.

![](http://www.gravatar.com/avatar.php?gravatar_id=719c91f5c3013e43ee46ed2bdc67f883&rating=PG&size=110&default=identicon)[Scott Hanselman](http://www.hanselman.com)

Thursday, February 17, 2011 7:56:39 PM UTC

1) Can you explain orthogonality, cohesion, and coupling as related to OOD. How much, or little, of each would you want in a system/class?  
  
2) Can you explain the difference between essence and ceremony?  
  
3) Can you explain convention over configuration? Can you give an example of it in action?

![](http://www.gravatar.com/avatar.php?gravatar_id=adde11c957096e6ea1342a5c16a25446&rating=PG&size=110&default=identicon)[Darrell Mozingo](http://darrell.mozingo.net)

Thursday, February 17, 2011 7:57:00 PM UTC

I think design exercises are a lot more useful than rote answers. You don't really care if someone knows the difference between DI and IoC, do you? Or listing the attributes of OOD? Maybe you do, I'm not sure I see value there. What's useful to me is to see how they apply relevant principles in the moment.  
  
Good interview questions are really hard to come by. Good luck!

Thursday, February 17, 2011 7:58:56 PM UTC

@Ian - Check out the book "Head First Design Patterns". It's probably the most approachable guide to helping one grok design patterns. It also covers, quite nicely, design principles.

![](http://www.gravatar.com/avatar.php?gravatar_id=3bb08583a7e7627f184b3ab279c2dd71&rating=PG&size=110&default=identicon)

Thursday, February 17, 2011 7:59:02 PM UTC

1.are you still writing code? Do you love it?  
2. You've just been assigned to a project in a new technology how would you get started?

![](http://www.gravatar.com/avatar.php?gravatar_id=9b3ab7f5c467f524121e966720082121&rating=PG&size=110&default=identicon)

Thursday, February 17, 2011 8:00:47 PM UTC

You might want to ask some questions about concurrency. What's the difference between Locking and Lockless concurrency models? What kinds of problems can you hit with locking model? And a lockless model? What trade offs do you have for resource contention? How might a task-based model differ from a threaded model? What's the difference between async and concurrency, if any?  
  
And you might ask some questions with more of a functional spin. What does composition mean in an OO and a functional context? What's the difference between a function and a predicate?

![](http://www.gravatar.com/avatar.php?gravatar_id=e0ba8c8bd830bddafff4d8f13572ffce&rating=PG&size=110&default=identicon)[Matthew Adams](http://endjin.com)

Thursday, February 17, 2011 8:02:06 PM UTC

Another thought: it's easier than you think to BS these kinds of questions, especially at senior levels. There's no substitute for having someone write actual code in an interview. If you haven't been doing this, you would probably be surprised at how many "programmers" this catches.  
  
Also, this might be useful: http://sites.google.com/site/steveyegge2/five-essential-phone-screen-questions

Thursday, February 17, 2011 8:07:26 PM UTC

I think these are MUCH better than the old questions. If someone can answer all of these, you can probably assume they know how to look up API documentation for framework specific problems.   
  
I might add something about incorporating SOA/data services/etc into application design and when is it appropriate.

![](http://www.gravatar.com/avatar.php?gravatar_id=5b83d213d5ab035a816d3e2fb0313140&rating=PG&size=110&default=identicon)

Thursday, February 17, 2011 8:09:16 PM UTC

1) Explain the concepts of coupling and cohesion and how they relate to maintainability. As a follow up, please explain afferent coupling and efferent coupling, and how those concepts fit above.

![](http://www.gravatar.com/avatar.php?gravatar_id=9ad4e9db75bec17539f5e5757112cfa2&rating=PG&size=110&default=identicon)[Steven Proctor](http://proctorit.wordpress.com)

Thursday, February 17, 2011 8:09:36 PM UTC

Roi - Love those!

![](http://www.gravatar.com/avatar.php?gravatar_id=719c91f5c3013e43ee46ed2bdc67f883&rating=PG&size=110&default=identicon)[Scott Hanselman](http://www.hanselman.com)

Thursday, February 17, 2011 8:11:18 PM UTC

Dave - Is the abilty to BS these questions a problem with the interviewee or the interviewer?

![](http://www.gravatar.com/avatar.php?gravatar_id=719c91f5c3013e43ee46ed2bdc67f883&rating=PG&size=110&default=identicon)[Scott Hanselman](http://www.hanselman.com)

Thursday, February 17, 2011 8:17:32 PM UTC

Roi paul question number one is awesome!!! I saw so many "consultant" minimizibg the importance of tech aspects and how many failing project due to requirements gathered from those "consultants"!

![](http://www.gravatar.com/avatar.php?gravatar_id=3c258ce0e2aeaca98757be3989979fc3&rating=PG&size=110&default=identicon)Gianluca

Thursday, February 17, 2011 8:18:01 PM UTC

Am I the only developer that doesn't know everything? Most of these questions I have no clue the answer. Or are programmers just so "smart" that we expect every developer to know everything?   
  
I consider myself a very good developer. Maybe I'm just not "senior" enough...  
  
How many of these questions would you expect a candidate to answer correctly?

![](http://www.gravatar.com/avatar.php?gravatar_id=3eda6fcd3204ef285fa52176c28c4d3e&rating=PG&size=110&default=identicon)

Thursday, February 17, 2011 8:18:45 PM UTC

Scott,  
  
The projects after the name may be good for a role like this, but for someone just starting out it's going to be a little difficult. :)  
  
Another pretty horrific question I got today was basically, the interviewer wrote some code on the board, and I basically had to describe the state of the stack and the heap after each line of code. I guess to demonstrate an underlying knowledge of the technology.   
  
How many people would actually be able to do that, without having to read up to refresh their memory first? Genuinely curious.

![](http://www.gravatar.com/avatar.php?gravatar_id=8ab980b87b44c231c79701196c65a2cc&rating=PG&size=110&default=identicon)Andy

Thursday, February 17, 2011 8:19:03 PM UTC

Many of these questions are so abstract that it's hard to say whether they predict actual job performance. I can answer most if not all of them, but I never encounter them asked in such an open-ended fashion in my daily work.   
  
I second the vote for giving them a keyboard and actually watching them program. Pair program, if possible.  
  
Failing that, hand the candidate a printout of actual code, in a language she'll be working in if hired. Have her code-review it. You can seed it with a range of problems: say, unchecked nulls, uninitialized collections, publicly mutable fields, to more subtle and arguable things like a function with multiple exit points, or a call to a virtual member from the constructor.  
  
Also, even though I'm mostly against definitional questions in interviews, I'd expect a senior dev to be able to define cyclomatic complexity.

![](http://www.gravatar.com/avatar.php?gravatar_id=117f5b7371380c244d562fc40bb5a6bf&rating=PG&size=110&default=identicon)[Mark Knell](http://machinedtolerance.blogspot.com)

Thursday, February 17, 2011 8:19:46 PM UTC

Ian - A number of those initial questions are described in Uncle Bob's book   
[Agile Principles, Patterns, and Practices in C#](http://www.amazon.com/Principles-Patterns-Practices-Robert-Martin/dp/0131857258) which I believe is a updated version of [Agile Software Development, Principles, Patterns, and Practices](http://www.amazon.com/Software-Development-Principles-Patterns-Practices/dp/0135974445/ref=ntt_at_ep_dpt_2) originally written for Java. I would strongly recommend **Agile Principles, Patterns, and Practices in C#** as a good read if you do object oriented development. Even if you have been doing OO for some years I have found it a good as a reference book to go back to occasionally and get refreshed on the concepts.

![](http://www.gravatar.com/avatar.php?gravatar_id=9ad4e9db75bec17539f5e5757112cfa2&rating=PG&size=110&default=identicon)[Steven Proctor](http://proctorit.wordpress.com)

Thursday, February 17, 2011 8:19:48 PM UTC

Another one that I think you might appreciate:  
  
"Tell me about 3 times you failed"  
  
:)

![](http://www.gravatar.com/avatar.php?gravatar_id=51c6697964956c0c4bb136c84bdecd4d&rating=PG&size=110&default=identicon)Rob Conery

Thursday, February 17, 2011 8:21:29 PM UTC

@Jonmichael - That book is actually sitting on my nightstand. It has been very helpful and I actually found that I already knew some of the concepts, just not their official names. It was also enlightening to see how similar Java and C# are. I've found there are many more resources that focus on Java rather than C#.

![](http://www.gravatar.com/avatar.php?gravatar_id=b231e07e868d33adca6135fc54ca06ec&rating=PG&size=110&default=identicon)Ian

Thursday, February 17, 2011 8:22:17 PM UTC

@Steven Thanks for the recommendation. That book is ordered and on it's way.

![](http://www.gravatar.com/avatar.php?gravatar_id=b231e07e868d33adca6135fc54ca06ec&rating=PG&size=110&default=identicon)Ian

Thursday, February 17, 2011 8:23:37 PM UTC

@Mark Knell - I like your style however a lot of those issues are basic programming issues. As I type that I had a thought that these are the majority of the problems that riddle our software. Sometimes I feel that we (programmers) forget some of the basics because it's "boring".

![](http://www.gravatar.com/avatar.php?gravatar_id=3eda6fcd3204ef285fa52176c28c4d3e&rating=PG&size=110&default=identicon)

Thursday, February 17, 2011 8:27:48 PM UTC

What do you do to stay abreast of the latest technologies and tools?  
  
Do you read other peoples code on a regular basis? What is the last open source project you read?  
  
What is your preferred programming language/platform? Why do you prefer it over others? Also, what don't you like about that language/platform?  
  
What is the last programming book you read?  
  
If you were required to look into and learn about a new platform/technology/language to get an understanding of what it would take to get the dev team started with it, what would you do?  
  
--  
Who really cares how much someone knows, if they don't do much to keep learning more? You also need to get an idea of how they think or approach a problem.

![](http://www.gravatar.com/avatar.php?gravatar_id=d565ce4d3fdf8007e1d707362cca9465&rating=PG&size=110&default=identicon)

Thursday, February 17, 2011 8:36:02 PM UTC

Don't look at these questions as interview questions. For developers not looking for a new gig, this is a great post to brush up on those ideas that you don't know, or may have forgotten.

![](http://www.gravatar.com/avatar.php?gravatar_id=e3764fde560988bb039cc6c40c9e8c2a&rating=PG&size=110&default=identicon)

Thursday, February 17, 2011 8:39:01 PM UTC

If all of those questions are related to .Net developments so I'm not a developer :) are we getting the answers soon?

![](http://www.gravatar.com/avatar.php?gravatar_id=587c599def016a77edbe5637f8a5de31&rating=PG&size=110&default=identicon)[Ahmed Magdy](http://devville.net)

Thursday, February 17, 2011 8:39:27 PM UTC

Yikes, looks I need to do my homework. I'm not able to answer a handful of these and I consider myself a senior developer. I've got 2 MCPD's and have written for MSDN magazine.

![](http://www.gravatar.com/avatar.php?gravatar_id=5c753d67506e0efb28858ca01f808b71&rating=PG&size=110&default=identicon)

Thursday, February 17, 2011 8:39:42 PM UTC

Good questions! How about this one to get a conversation going.  
  
Describe to me some bad code you've read or inherited lately.  
Can you describe some code smells?

![](http://www.gravatar.com/avatar.php?gravatar_id=44a2af12d83f8168282fb090a96a1075&rating=PG&size=110&default=identicon)

Thursday, February 17, 2011 8:40:51 PM UTC

Scott...  
  
>What's the difference between Locking and Lockless concurrency models?  
  
I assume you are asking about Optimistic and Pessimistic concurrency here? If not, what is that above... I don't think I've heard those terms... I pretty much "think" I could give pretty good answers for all of the rest.  
  
BOb

![](http://www.gravatar.com/avatar.php?gravatar_id=17d192e7e9143cfe67db67691318a35f&rating=PG&size=110&default=identicon)

Thursday, February 17, 2011 8:42:45 PM UTC

It's a problem with neither participant, rather it's a problem with (some of) the questions. They don't test what you really value, which is the ability to write good code, and to make good design choices in the moment. Not whether they know the methodology acronym of the day. It's a difference between knowing and doing, between being an advanced novice and being an expert. On the other hand, these are likely to be the questions he will face, so it's good for him to be ready for them.  
  
BTW, I find Singleton to be the most often quoted (and usually misapplied) pattern. Interesting that you zeroed in on Factory.  
  
In addition to interview practice, which is a good idea, I'd advise your friend to get busy with a project (possibly open source). It will keep his chops up, and is a great opportunity to learn something new. It also makes a fantastic story to tell a potential employer (and would provide a good context for answering these kinds of questions).

Thursday, February 17, 2011 8:45:16 PM UTC

> Describe a pattern that is NOT the Factory Pattern?

9 out of 10, when I ask for known patterns, I get Singleton and Factory, and only these two. Usually without the distinction between Factory Method and Abstract Factory.

![](http://www.gravatar.com/avatar.php?gravatar_id=a8aadeed64d0c69df05b0c3d40ae9471&rating=PG&size=110&default=identicon)

Thursday, February 17, 2011 8:46:33 PM UTC

Describe an interesting problem that you solved recently. What ideas and considerations did you personally bring to the solution? I find this is a good springboard into areas where the candidate will be able to talk passionately and avoid just fumbling with buzzwords.  
  
What is deferred execution? What role does it play in stateless/stateful systems?  
  
Describe a situation where contract first design is beneficial. Discuss a situation where it is not.  
  
When should a server technology dictate storage mediums? When are there good cases for a client to specify how/where/when their data is stored.  
  
Great thread. Thank you so much for starting this.

![](http://www.gravatar.com/avatar.php?gravatar_id=5c5a46115322ba7acbb5f7a357d79676&rating=PG&size=110&default=identicon)[Stuart Thompson](http://www.stuartthompson.net)

Thursday, February 17, 2011 8:46:57 PM UTC

Yes sure for your friend.. :)

Edward

Thursday, February 17, 2011 8:51:37 PM UTC

I think more important than the question is the context in which it is applied. Asking a laundry list of questions is more an exercise of endurance than a conversation between two developers. I prefer conversation, so when I interview a developer I send him to the board and ask him to describe the architecture of his last project.  
  
With that framework in place, both the developer and I get to talk about principles and patterns in a more meaningful way. The developer gets a chance to show me what he knows in a practical manner. More importantly, I get to see how the developer communicates on his feet.

![](http://www.gravatar.com/avatar.php?gravatar_id=fce36bb21c8287661e08e8d43c50e528&rating=PG&size=110&default=identicon)[TVD](http://techoctave.com/c7)

Thursday, February 17, 2011 8:58:27 PM UTC

I thought I was a decent .NET developer, but a good number of these questions will cause me to resort to googling! Any way to get some short answers to them posted in a future blog?

![](http://www.gravatar.com/avatar.php?gravatar_id=e422d568a74ee1df4298f4b403f8d7f2&rating=PG&size=110&default=identicon)

Thursday, February 17, 2011 9:01:51 PM UTC

It's scary when you know the answer but not the terminology that is being used in the question.  
  
That said, I might ask:  
  
- Left to your own devices, what would you create?  
- What elements of OO design are most prone to abuse? How would you mitigate that?  
- Why might it be bad to "burn the base class"?

![](http://www.gravatar.com/avatar.php?gravatar_id=3b0d930715cf8f5729e177981f69f44e&rating=PG&size=110&default=identicon)

Thursday, February 17, 2011 9:03:39 PM UTC

When do you know your code is ready for production?

![](http://www.gravatar.com/avatar.php?gravatar_id=9fd5ab4898425dfac5dfd7ef41d9e019&rating=PG&size=110&default=identicon)

Thursday, February 17, 2011 9:04:23 PM UTC

while these are good questions..... they all stem from very similar schools of thought. Very "Uncle Bob" like questions. They are very "pop" soft dev stuff. So if you are a fashionable geek, you'll have no problem with this stuff.  
  
But my problem is, you can know all this stuff and still suck at writing software.  
  
In fact it can make you suck even more at writing software...... implementing massive n'tiered, pattern bloated, acronym compliant, software. Adding 1 tiny thing can ripple through lots of layers of software and it becomes \*slow\* to do anything. TDD tests that just test layers and layers of CRUFT. Kool Aid frameworks. Hopeless.

![](http://www.gravatar.com/avatar.php?gravatar_id=22aac6106c44ae4078bd4c0a564714e0&rating=PG&size=110&default=identicon)[Keith](http://geekswithblogs.net/Designingcode)

Thursday, February 17, 2011 9:06:19 PM UTC

It seems like some people are upset that these questions are too "vague", and don't have enough technical detail. I think that these people are missing the point. These should not be asked \*instead\* of specific technical questions or coding checks, but rather in addition to.  
  
I have a very different expectation of a "senior" or "lead" developer than I do of an entry-level one. I expect that a senior dev has an ability to interact and communicate with others. I expect that they do things in a given way for a reason, and that they are analytical and reflective enough to tell me why. Open-ended questions with no clean-cut correct answer are perfect for evaluating these things.  
  
Furthermore, conceptual questions about practices and trends help to reveal where a person's motivation comes from. Are they learning in response to the immediate needs of their day to day work? Or are they going beyond that and investing in themselves by stepping outside their comfort zone and immediate environment? Are they hidden away heads-down in a corner grinding alone on all their challenges, or are engaging with the community to find new and better ways of doing things?  
  
I expect a senior dev to do more than just sit there and write code. I expect them to think, reflect, be aware, communicate, and invest in themselves. Candidates for such positions should absolutely be asked questions that foster a conversation where they can illustrate those skills and values, or fail to do so, as the case may be.

![](http://www.gravatar.com/avatar.php?gravatar_id=3eda6fcd3204ef285fa52176c28c4d3e&rating=PG&size=110&default=identicon)

Thursday, February 17, 2011 9:07:10 PM UTC

- What processes should every project have in place?  
- What value do daily builds, automated testing, and peer reviews add to a project? What disadvantages are there?  
- How can you mitigate technical debt?

![](http://www.gravatar.com/avatar.php?gravatar_id=3b0d930715cf8f5729e177981f69f44e&rating=PG&size=110&default=identicon)

Thursday, February 17, 2011 9:07:23 PM UTC

@Bobby Cannon Thanks. I agree, my examples were not especially challenging as code. But my philosophy is, they don't need to be. You can tell most of what you need to know about the candidate from how she talks about fairly mundane code. Does she struggle to find any flaws at all without the aid of a debugger or an IDE plugin? How does she express her opinions? Does she understand more than one point of view--is she at least aware that reasonable people disagree about, say, early exits from functions? Does she have a sense of various schools of thought--say, mockist vs classical tests, or functional vs OO idioms, or declarative vs imperative style? Is she likely to be able to propagate her knowledge to junior devs? Will she be able to articulate her opinions in a team code review or architectural discussion? Does she listen to your suggestions? Will you enjoy collaborating with her? Does she seem committed to team development? If you mention something she hasn't encountered, is she curious about the new idea? Is she conscientious, disciplined, and systematic, or will she make a mess for someone else to clean? Is she creative but able to work within team contraints? Is she a relentless problem solver? I'd weigh any ONE of these factors more heavily than her knowledge of any given pattern, tool, or even dev stack. The laundry list of facts is just a starting point for assessing the knowledge worker you're going to choose as a colleague. I want a glimpse of the candidate's mind, not a vocabulary test.

![](http://www.gravatar.com/avatar.php?gravatar_id=117f5b7371380c244d562fc40bb5a6bf&rating=PG&size=110&default=identicon)[Mark Knell](http://machinedtolerance.blogspot.com)

Thursday, February 17, 2011 9:11:44 PM UTC

It seems there are a fair number of people asking for answers to these questions. What about setting up a wiki where we can post these questions along with brief answers and links to more reading. Personally, I feel I did quite well with these questions, but it would be nice to "check the answer sheet" and make sure I'm not off base. If enough people are willing to contribute answers, I'll set it up.

![](http://www.gravatar.com/avatar.php?gravatar_id=880df7a18a8b445d917a25b3e0254043&rating=PG&size=110&default=identicon)

Thursday, February 17, 2011 9:16:49 PM UTC

I'm only a couple of months out of university and I immediately knew the answers to all but a couple of those questions. I'm a design geek and I wish junior dev interviews were that straight-forward. I find this high-level stuff much simpler to grok than the nitty-gritty technical details we get asked in junior dev technical assessments.

![](http://www.gravatar.com/avatar.php?gravatar_id=ead57e5bebe4e7d4a9bc06353d10de82&rating=PG&size=110&default=identicon)[Martin Doms](http://blog.martindoms.com)

Thursday, February 17, 2011 9:19:56 PM UTC

@ Jeff Yates  
  
"- Left to your own devices, what would you create?"  
  
Now THAT is a hard question. That's a cert for mind-blank syndrome.

![](http://www.gravatar.com/avatar.php?gravatar_id=8ab980b87b44c231c79701196c65a2cc&rating=PG&size=110&default=identicon)Andy

Thursday, February 17, 2011 9:20:33 PM UTC

I always like to ask candidates about their favorite dev tools. NOT just the ones they've used, but the ones that they really like on a gut level. And after they've gushed over some features, I ask them to tell me what, if anything, they dislike or would change about those tools.  
  
If a person can't tell me why they like a certain tool, then I don't think they have much experience using a wide variety of tools. If they can't tell me what they dislike about a certain tool, then I don't think they've really spent enough time using it.

![](http://www.gravatar.com/avatar.php?gravatar_id=eb4ff48079c87a23d3ab675fe5a4b4fe&rating=PG&size=110&default=identicon)Kelly

Thursday, February 17, 2011 9:28:22 PM UTC

I find job postings and interview questions fascinating in what the say about people on both sides of the table. Here (and commonly), the use of the term "Engineer" is used differently than it would be in, say, the mechanical or avionics fields where engineering is identified mainly by contrast with science. Engineers take science (and philosophy) and apply it to make things with positive net benefit to society, if you believe in the creed. So I suppose I tend to focus more on what a person can create rather than what they can describe. Maybe something like:  
  
"Let's talk about trade-offs. Tell me about some of the components you like to use, and how the fit into a couple systems you've help build." And then try to understand if the person thinks or merely acts.

![](http://www.gravatar.com/avatar.php?gravatar_id=39daa887485d1f4911beca219936abbc&rating=PG&size=110&default=identicon)[Lee](http://circuitpeople.com)

Thursday, February 17, 2011 9:50:05 PM UTC

I don't put to much stock in these sorts of questions. Our industry doesn't have much of a standardization in vernacular and many of the concepts asked above are new or transient in nature. I think the best interview of person is to sit them down in front of an IDE and give them a small programming project. Tell them to pretend they are writing for a production environment (rather than hacking away) and see what they do. Do they define some interfaces? Write tests? Use inheritance? Is the code readable? Do they take into account threading issues?  
  
After they are done ask them to modify the program to meet a new requirement. Watch what they do. When they are done, ask them why they made certain decisions.  
  
The number of candidates I've had come through the door that can talk the talk but fall to pieces when put in front of the IDE is amazing. I'd much rather have a person work for that knows the principles of SOLID but not acronym than a person that knows what the acronym stands for but can't apply the principles.

![](http://www.gravatar.com/avatar.php?gravatar_id=ded194212e0b55db5f341d4b163a4102&rating=PG&size=110&default=identicon)

Thursday, February 17, 2011 9:57:40 PM UTC

I agree with David Brabant.  
***"Show me a portfolio of all the applications you worked on, and tell me how you contributed to design them. Isn't it the only question that really matters?"***  
  
I think that these class room questions do not help you find a problem solver. Many are really silly.  
Does knowing about an anti-pattern really show you anything? Understanding why patterns are important is a good question because it is pertinent to development today. Who really cares what a YAGI is? Don't we have dozens of terms out there that we can throw at a developer to trip him up? What does this get you?  
This seems to be a measuring contest. Can I prove that I have more trivial knowledge than you?  
Ive coded in .NET since Beta1. Ive developed in other languages and on other platforms as well. Ive never failed on a single project no matter what tool I used and I make sure that I have a complete understanding of the architecture I am using even if I do not remember your terminology. I follow best practices and also know of best practices because of my years of experience. Most of this type of questioning produces nothing but an academic. We want experts right? People who know and love technology. I wonder if we gave a good doctor a pop quiz, would he pass the test. Sorry doctor Oz. There must be a better way.  
Furthermore, one thing is for sure, after 15 years in this industry I will not take a written test, so before you call someone in for an interview, let him know if you are planning to pull out an exam.

![](http://www.gravatar.com/avatar.php?gravatar_id=eacffb3924f0bc97db183a6d30fc726e&rating=PG&size=110&default=identicon)nate

Thursday, February 17, 2011 10:01:13 PM UTC

Q1: What is the difference between interfaces and abstract classes and when to use these?  
Q2: Explain how publisher/Subscriber pattern function and how to use it to eliminate problems reconnecting clients to servers

![](http://www.gravatar.com/avatar.php?gravatar_id=d99f476f2c8d666ec9ae53669e727830&rating=PG&size=110&default=identicon)Hussam Ahmad

Thursday, February 17, 2011 10:13:37 PM UTC

1)what blogs do you read  
2)When is logging to much logging  
3)why use AOp for logging  
4)When to use property injection over constructor injection  
5)When would you not use an ORM  
6)what other uses can you think of for AOP  
7)What is a T4 template  
8)write some lamdba expression in VB.Net  
9)Why F#  
10)Should you use a designer to make your view or not, what are the disadvantages of using a designer  
11)Have you ever read a blog of the famous chrissie1  
12)Do you want a chocolate?  
  
Done.

![](http://www.gravatar.com/avatar.php?gravatar_id=70e155e88e0ead5e2bdcb3e1c57506b4&rating=PG&size=110&default=identicon)[chrissie1](http://blogs.lessthandot.com)

Thursday, February 17, 2011 10:18:23 PM UTC

I'm still just a web dev, but here are a couple of questions that I use as barometers of current knowledge  
  
- What's the difference between a web farm and a web garden, and what are the differences in preparing a website for deployment to each of them.  
- If you're starting a greenfield web project, what third-party libraries do you include in your lib directory and why? What do you add to web.config by default?

![](http://www.gravatar.com/avatar.php?gravatar_id=dec2c5e29827a0814702d02610bd95fe&rating=PG&size=110&default=identicon)

Thursday, February 17, 2011 10:23:01 PM UTC

Looks like a b tag has been left open since Nate's post!

![](http://www.gravatar.com/avatar.php?gravatar_id=8ab980b87b44c231c79701196c65a2cc&rating=PG&size=110&default=identicon)Andy

Thursday, February 17, 2011 10:29:50 PM UTC

"The" Factory Pattern? My GoF book has two...

![](http://www.gravatar.com/avatar.php?gravatar_id=ce996304c4b69b3ef8161d3fff7a2769&rating=PG&size=110&default=identicon)Jim Cooper

Thursday, February 17, 2011 10:31:27 PM UTC

I think these are wonderful questions, but what is important is that the candidate should be judged based on thought process more than whether they are right or wrong. It is the application of these principles etc that is more important that knowing the theory behind them all.   
  
Heres one question that I would ask :   
  
Given the Quad - Time, Cost, Client satisfaction and Best Practices, how will you prioritise them for a project you are working on? Explain why?

![](http://www.gravatar.com/avatar.php?gravatar_id=42ceb00311a2dc5c400c7aaacad6f0c1&rating=PG&size=110&default=identicon)Pramod Raghavendran

Thursday, February 17, 2011 10:35:17 PM UTC

Good question Pramod.  
  
I imagine in a real life environment, Cost will always be #1 priority. I'd have client satisfaction as #2, and then i'd have the other 2 as #3 and #4 but the order they appear would be open to debate.

![](http://www.gravatar.com/avatar.php?gravatar_id=8ab980b87b44c231c79701196c65a2cc&rating=PG&size=110&default=identicon)Andy

Thursday, February 17, 2011 10:36:24 PM UTC

Hi Scott,   
  
Greate questions / subjects. But I miss something about the DRY principle....  
So : "What does DRY mean and why is it important?

![](http://www.gravatar.com/avatar.php?gravatar_id=7c0e18f88a3c3d844def67dee19aa515&rating=PG&size=110&default=identicon)Jaap

Thursday, February 17, 2011 10:41:16 PM UTC

I'm not sure I would be satisfied with my own answers to these questions. Many of them seem like good topics for blog posts just to explore my own understanding and clarify to myself how I might answer them.

![](http://www.gravatar.com/avatar.php?gravatar_id=a5c5e2bbaee6455e8ca1946111eb72b9&rating=PG&size=110&default=identicon)

Thursday, February 17, 2011 10:47:18 PM UTC

One I've asked for many years now is:  
  
You have two computers, and you want to get data from one to the other. How could you do it?  
  
Generally people will come up withe one, or maybe to solutions, to which I answer, "and what else?". I keep asking for more solutions until they run dry.  
  
The idea behind it is to test how they question requirements, and also how inventive they can be. There is no right or wrong answer, but it can give you a good idea about how easily someone might get "stuck" on a particular solution, and how much of a self-starter they might be.   
  
Phil

![](http://www.gravatar.com/avatar.php?gravatar_id=94060bfb5b1948ff7a6a88a6bc5b7836&rating=PG&size=110&default=identicon)

Thursday, February 17, 2011 11:10:34 PM UTC

@Phil  
  
I've used that same technique myself. I learned it from a former boss who used it in my own interview. I guess I did OK.  
  
I like to throw in questions about durability. For example, in an RPC scenario, what would happen if the response is lost? How do you avoid duplication?  
  
I also like to add the requirement that only one machine gets to work on a particular item. How do you ensure that someone else isn't working on it. I'm continually surprised by how many answers there are to this one, each with its own set of problems.

![](http://www.gravatar.com/avatar.php?gravatar_id=b46b0b9cd3f4825dd59d911496fa4665&rating=PG&size=110&default=identicon)

Thursday, February 17, 2011 11:19:45 PM UTC

What would you do if you were in charge of a team of people who refused to change and were set on doing things the wrong or outdated way?  
  
How would you handle a team member who took code reviews personally or would refuse to make the suggested changes?

![](http://www.gravatar.com/avatar.php?gravatar_id=f27acc5dd1224c882c673f22b1966154&rating=PG&size=110&default=identicon)

Thursday, February 17, 2011 11:27:20 PM UTC

I say - what you YOU ask YOUR INTERVIEWER -   
http://blog.wekeroad.com/thoughts/how-many-columns-does-an-int-have

![](http://www.gravatar.com/avatar.php?gravatar_id=51c6697964956c0c4bb136c84bdecd4d&rating=PG&size=110&default=identicon)Rob Conery

Thursday, February 17, 2011 11:56:38 PM UTC

What is DDD ? Why is it important ?  
What are aggregate roots ?  
What is ServiceBus ? CQRS ?  
Difference between unit test and integration test ?  
How you know your design is good ?  
What means that a class is immutable ? Make one ? Why is it important ?  
Difference between scale-out vs. scale-up ?  
How connection pool works ?  
What is SQL injection ?  
What is an ORM ?  
Would you use DataSets ? For what ?  
What is memchached/AppFabric Caching ?

![](http://www.gravatar.com/avatar.php?gravatar_id=6ad089a817870c9f92db929863b30495&rating=PG&size=110&default=identicon)

Friday, February 18, 2011 2:25:45 AM UTC

In my experience any question beginning with "What is.." or "Describe.." is too easy for a candidate to BS their way through by Wikipedia-ing during a telephone interview, or just having learnt parrot-fashion with no real understanding. You might get a satisfactory answer, only to put them in front of a PC on their first day on the job and they'll have no idea when to use that buzzword they memorized.  
  
I like turning the questions around into scenarios so you can test peoples problem solving abilities, for example:  
  
1) What are a few good practices to follow (and avoid) to make your code testable?  
2) How would you communicate between a Website and a Windows Service?  
3) If your database was under a lot of strain, what are the first few things you might consider to speed it up?  
4) How can you stop your DBA from making off with a list of your users’ passwords?   
5) What do you do when you get stuck with a problem you can't solve?

![](http://www.gravatar.com/avatar.php?gravatar_id=83f5a4fa6a98e9fbec01f1f4b77da335&rating=PG&size=110&default=identicon)

Friday, February 18, 2011 3:03:07 AM UTC

These are some great questions overall, really like most of them. That said, what about coding questions? I've seen people that could answer every one of these, but if I asked them to remove the duplicates from a list, they'd be clueless. I call these people "non-coding architects" and they're surprisingly common and often have 15+ years of experience and many applications shipped on their resume.  
  
I don't care how much you know, if you can't write code you suck. If you can write code but you don't know the fundamentals of Computer Science (data structures and algorithms mostly), you still suck. I can implement a linked-list on a whiteboard in less than two minutes (coming to alt.net seattle? Time me. I'm serious), I would expect ANYONE that I would want to hire to be able to implement some sort of linked list class in <15 minutes. Knowing concepts will only take you so far (believe me, I'm a professor, I know this well) but being able to know + do is what counts.

![](http://www.gravatar.com/avatar.php?gravatar_id=e8721a02562e61399a426f9fb8494a41&rating=PG&size=110&default=identicon)

Friday, February 18, 2011 3:26:34 AM UTC

I had just switched over to ASP.NET MVC in the past year from several years of ColdFusion. While I knew I still had lots to learn, I was feeling like I was starting to really get it...  
  
Then I read this post and realized I have a really long way to go :)  
  
Of course, that is why I am having so much fun.

![](http://www.gravatar.com/avatar.php?gravatar_id=55c6829969a6b0e873f5f1ee36e04bd1&rating=PG&size=110&default=identicon)

Friday, February 18, 2011 3:34:01 AM UTC

Should I be concerned? Most of the questions here are not ones I could answer with a high level of confidence, and they are for a title I currently hold.  
  
I'm in the "learn how they think" camp. I want to find people who are passionate about building software. I'm more interested in learning a person's aptitude than in testing their discrete skills. Anyone who knows how to think and solve problems can search, find and learn what they need to execute a solution in any given problem domain. But more importantly, basing qualification on skill is subject to rot. Is the technology they are quizzed on going to be applicable in 5 years, 2 years, 6 months? Whether they can regurgitate an acronym now won't help then. They need to be able to adapt and grow.  
  
Unfortunately it's far more difficult to gauge aptitude than to quiz on concepts or code. That's why I prefer to just converse. Certain questions are good catalysts for conversation, usually those involving projects about which the candidate can speak knowledgeably and passionately. If they can't do both, you find yourself digging for more questions, or that old "what's wrong with this code" test and it's easy to question their qualification. If they can, you regret having to pass them on to the next interviewer. That's the candidate you want to hire. After they've filled out the HR paperwork they can learn SOLID, MVVM and IoC (if they haven't already started to on their own).

![](http://www.gravatar.com/avatar.php?gravatar_id=1f8b331ee1b89573b7632226b8e6632b&rating=PG&size=110&default=identicon)[Peter Lanoie](http://www.compiledthoughts.com)

Friday, February 18, 2011 3:51:05 AM UTC

Many of the questions are focused on the acronym-of-the-day.  
  
Maybe these are the kind of interview questions companies are asking but I have to disagree that they (or answers to them) convey a candidate's proficiency as a developer or their seniority. IMO, the "senior" prefix should signify that a developer has a significant amount of experience although I all too often see it applied to one-company-one-product-three-years-work-experience kind of people.  
  
Much of the "fashion of the day" terminology rarely make it "down to the floor". (Well, maybe it does at Microsoft but then you're different than the rest of the industry in a whole lot of ways; a lot larger, a lot more resources/manpower behind every line of code, much longer product cycles, etc)  
  
Some of the "fashion of the day" terminology stuff is a way to formalize and convey the "best practices" and "common sense" that one normally picks up over the years into a more digestable [documented/discussed in blogs and conferences] format for the *junior* developers.  
  
I'd suggest posing a couple of *real world* problems and asking for a candidate's approach to solving them would be a better way to distinguish between a [good] senior developer and the rest of the crowd. That, and past track record in delivering real world apps that are *used* and *liked* by the users... :)  
  
Just my 2 baht...

![](http://www.gravatar.com/avatar.php?gravatar_id=8313d33da9a27377b32079d183b40c6b&rating=PG&size=110&default=identicon)[KristoferA](http://huagati.blogspot.com)

Friday, February 18, 2011 4:12:10 AM UTC

I know \_exactly\_ the question I would ask a person wanting to work for me as a senior .Net developer: "What's so great about PHP?" Seriously, what would you say? Would you hedge, fearing to be too complimentary? Would you bash it? On the sincere side, what qualities would you pull out as admirable and worth emulation?  
  
The same ploy works for any "antithesis" technology, process or even personality. Interviewing for an Agile team? Ask "A lot of really great software was developed under the waterfall process, why and how did that work?"

![](http://www.gravatar.com/avatar.php?gravatar_id=39daa887485d1f4911beca219936abbc&rating=PG&size=110&default=identicon)[Lee](http://circuitpeople.com)

Friday, February 18, 2011 4:18:37 AM UTC

+1 to all three of: Peter Lanoie, nate, and Matthew Schumaker. Spot on.

![](http://www.gravatar.com/avatar.php?gravatar_id=8313d33da9a27377b32079d183b40c6b&rating=PG&size=110&default=identicon)[KristoferA](http://huagati.blogspot.com)

Friday, February 18, 2011 4:20:07 AM UTC

These are questions I've seen asked and have asked others myself, which I think help get to a person's ability to communicate and self-develop:  
  
1. Describe the structure and contents of a design document, or a set of design documents, for a multi-tired web application. (Points if the person mentions the typical layers of an app. Bigger points for mentions of sequence and class diagrams. Even bigger points if he/she mentions writing docs for support/operations groups.)  
  
2. Describe a software development life cycle that you've managed. (Points if the person actually has participated in one. Bigger points if it involved source control and reviews.)  
  
3. How do you react to people criticizing your code/documents? (A senior person should be thanking others with genuine gratitude for their input when he/she is wrong or for a good idea, and be able to defend his/her thinking in a constructive manner.)  
  
4. Whose blogs or podcasts do you follow? (Points if the person mentions some. Big points if the person blogs. Out of the dozens of devs I've known and worked with, only 1 didn't answer "none", and he's fantastic. This is one of the blogs he mentioned :)  
  
5. Tell me about some of your hobby projects that you've written in your off time. (Points if the person has hobby projects. Big points if the person's face lights up and he/she goes deep into design details and issues encountered.)  
  
6. Give the person a little coding exercise with somewhat incomplete or slightly vague requirements. If they write the whole thing without asking questions, bad. If they write a bit, then ask some questions, good. If they ask a bunch of questions to clarify what's up to them vs. what's absolutely required before writing any code, outstanding. In all cases they need to explain the decisions they made. It just needs to compile on paper, though.

![](http://www.gravatar.com/avatar.php?gravatar_id=0c7d4784d453bbec161533e92e1fa5f3&rating=PG&size=110&default=identicon)

Friday, February 18, 2011 4:21:41 AM UTC

IMO, the questions with the most votes in each category on StackOverflow.com are also helpful from an interview point of view.

[Anil](http://mvark.blogspot.com/)

Friday, February 18, 2011 4:44:59 AM UTC

I would also add:  
  
Do you watch channel 9  
Name the 3 Scott's  
Are you a Mac or PC (I will pick a Mac guy for Windows and visa versa)

![](http://www.gravatar.com/avatar.php?gravatar_id=b8af64a41f304580e25f12e848d722d2&rating=PG&size=110&default=identicon)Mouhammad Fakhoury

Friday, February 18, 2011 5:09:50 AM UTC

I didn't have time to read through every single comment, but I found some good responses and James McLachlan more or less summed up my thoughts as well.  
  
I don't give a rat's ass about SOLID or YAGI or any of these other buzzword bingo terms. I don't care what TDD or BDD or even DDD is. I need to know that you actually have practiced the craft of coding, software engineering, programming, software architectural design, whatever you want to call what it is you do. I want to give you a small, quick, yet challenging interactive test to see if you truly understand algorithms and implementation details concerning them. Can you work within the limitations or constraints of an existing system? Can you impose restrictions on yourself in order to improve your productivity and possibly others' too?  
  
Communication is probably the most important skill you need. Can you communicate with me and other team members precisely and succinctly? This is very difficult to do, and most of the problems faced at a software development shop are centered around poor communication. I need to see moderate to excellent skill level in written and oral communication. I don't care about ERDs or UMLs or flow charts or any of that nonsense. Write it in plain English, clearly, precisely, and unambiguously, because it won't get any clearer with your drawings that gloss over key details of the system and/or design.  
  
I also need someone who is more action oriented than discussion oriented. Smart people don't waste their time endlessly listening to themselves and others babble on and on. If you could have implemented a proof of concept in the time it took you to gather everyone up to discuss the potential solution, you just wasted everyone's time. Something to look at and work with is far more descriptive and useful than abstract concepts discussed at length.  
  
These are the types of things you find out about the interviewee long after the interview process is over, and it's a lot harder to fire someone than it is to hire someone these days. I like to get it right the first time.

![](http://www.gravatar.com/avatar.php?gravatar_id=9f41bfc370c185365fea540def0fcd55&rating=PG&size=110&default=identicon)

Friday, February 18, 2011 5:26:37 AM UTC

I like to start off interviews by saying, "The questions I'm asking are much more important than anything you have to say."   
  
Then I speed-question using trivia-type questions and never, under any circumstance, allow the person time to answer properly. I find that this let's the other person know that I am not an interviewer to be toyed with.

![](http://www.gravatar.com/avatar.php?gravatar_id=7e25817b47e3f6a1cec646ad15b966b3&rating=PG&size=110&default=identicon)Tim jf

Friday, February 18, 2011 6:24:38 AM UTC

I would add:  
- Explain Command-query separation  
- What Source Control systems have you worked with  
- What is Continuous Integration? Have you used it and why is it important  
- Some questions about basic data structures and algorithms (Lists, Linked Lists, Trees, Sorting etc.) and a basic discussion on the trade-offs between choosing different algorithms/data structures

![](http://www.gravatar.com/avatar.php?gravatar_id=0f692990601721c06f141f4fe860685e&rating=PG&size=110&default=identicon)[Carel Lotz](http://fromthedevtrenches.blogspot.com)

Friday, February 18, 2011 7:51:22 AM UTC

Next time around I have to interview a senior dev, I'll make sure we have access to a whiteboard. Then I'll come up with a case to which I'd like to see a diagram of the technical design.  
Also I'll present a similar diagram of one of our applications and ask questions about how and where to add certain functionallity.  
  
To me, these are the most important points for a senior dev in order to add value to our team. If you can't do this, you are not hired.  
Then I'll ask some questions about technology they have worked with that require more underlying knowledge. I find this is important to test someones curiousity to how things work and their ability to find out about it.

![](http://www.gravatar.com/avatar.php?gravatar_id=cea0b794c69d34be3d3e22a163aa9e7f&rating=PG&size=110&default=identicon)[Jonathan van de Veen](http://jvdveen.blogspot.com)

Friday, February 18, 2011 7:53:53 AM UTC

Hi guys,  
I come from Germany and wiork as a ScrumMaster. I would like to present my point of view. Most of the suggested questions would either make me leave during an interview or have me internally decide to not work for the company.   
I totally agree with David, who suggested to have the applicant present a list of projects he has worked on and then talk about that. I don't want to and I don't need to pass a "Test" of knowledge questions to be able to work for somebody. Any HR person will tell you, that it is important to have a certain knowledge (which will be presented by certificates and credentials). More important are the "Soft Skills".   
  
And it is not like the applicant is the only person who "wants" something during an application process (and therefore has to pass multiple tests). The company wants the applicant as well...or to be more precise...his contribution to the enterprise. And it is, in my opinion, no value contribution at all to be able to explain who the "gang of four" is. So I would focus my questions on "how" can this person contribute to my company. Is he stress-resistant, a teamplayer, does he have a good capability of self-organization, can he explain things to other team-members, etc.  
  
And in my opinion, the list of projects and WHAT the person contributed to these projects is a good way to explore these facts. To be able to explain the difference between TDD and FDD is not...in my opinion.

Marcel Konnegen

Friday, February 18, 2011 8:24:43 AM UTC

Hi,   
Yes these questions are very important and I have come accross them many times. I think every developer knows they are important. the Questions is, what are the answers? :-)

![](http://www.gravatar.com/avatar.php?gravatar_id=93cf6e18e053d42cdc32ad5a6693981b&rating=PG&size=110&default=identicon)

Friday, February 18, 2011 9:19:45 AM UTC

@Hugoware and @Marcel  
  
The purpose of "Gang of Four" question IMHO is to detect if you ever did any research, learning or work related to design patterns, because that is something that Software Architect do. And if you ever did, you definitely had to know about the book written by four guys (hence the "Gang of Four"):  
  
"Design Patterns: Elements of Reusable Object-Oriented Software"  
http://www.amazon.com/Design-Patterns-Elements-Reusable-Object-Oriented/dp/0201633612  
  
(affiliate code free link)  
  
This book is mentioned in almost every book I read about the software design and architecture.

![](http://www.gravatar.com/avatar.php?gravatar_id=5bae369c713906f9df640a2a2518a65a&rating=PG&size=110&default=identicon)

Friday, February 18, 2011 9:25:37 AM UTC

So tell me about a project you've worked on that hasn't gone very well?

![](http://www.gravatar.com/avatar.php?gravatar_id=5ad2ef0ddff7ba1c4d06981bd8acba47&rating=PG&size=110&default=identicon)[Richard Astbury](http://coderead.wordpress.com)

Friday, February 18, 2011 9:35:24 AM UTC

These questions are interesting, but I like the idea of a question like "How would you go about writing code to read and write INI files, without using the specific Win32 API".   
  
The advantage of this is most people are at least vaguely familiar with it, and if they aren't you can give them the gist very fast. However, INI is incredibly loose in specification. This leads to all kinds of potentially interesting discussions. For example, does the candidate spot some of the issues up front without prompting, or do they take a simple approach and announce "Done!".   
  
How would you handle comments, especially when writing files. For example, is there a strategy that will let you delete sections and keep comments consistent? How would you handle writing to ensure that you don't get conflicts? Can you make sure if you code crashes the user is let with something usable? Should you read to memory and cache or parse the file each time? Then there's all the fun to be had with quoting, handling white space, and crazy stuff like:-  
  
Key Name = Someone's+"value=1;" ; this is a weird one  
  
How you cope with the different "flavours"? Line endings? Backslash quoting? Do you make everything an option?  
  
I think just talking aloud through an algorithm to parse the lines and handle quoting and spaces would reveal a lot about someone ability to model code in their head and test it in their head.  
  
Perhaps these are more for a coder than an Senior Software Engineer, but I'd still like a Senior Engineer who can code, or at least reason about code.

![](http://www.gravatar.com/avatar.php?gravatar_id=5f7d1dfd54656cb7a485d70f3a514873&rating=PG&size=110&default=identicon)

Friday, February 18, 2011 9:42:14 AM UTC

Nothing about requirements and nothing about software processes?

![](http://www.gravatar.com/avatar.php?gravatar_id=798edc87b13712a139b7c2833cf8c8bd&rating=PG&size=110&default=identicon)[Anthony Finkelstein](http://www.cs.ucl.ac.uk/staff/A.Finkelstein)

Friday, February 18, 2011 9:57:03 AM UTC

Though I wouldn't be surprised to be asked a lot of the questions. They are not the kind of questions I like to ask candidates when I interview. All the above questions is something you can google and memorize. I wish to see people think. I wanna know how they solve a problem. Sure if they can name and explain a few patterns\* at least they have studied (for the interview).   
I usually describe a system such as a fancy water boiler and ask the candidates to model it if they were to implement the software for it based on the design I ask them a lot of whys and coulds. "Why does those classes derive from the same base?" "Could you decrease the coupling with a gain and if so what would the gain be"  
  
If I was to add anything to the list of googlable questions it would be:  
Describe the liskov substitutional principle and describe when and why it's important. If the candidate does not know the principle I'll explain it and ask the latter part of the question again  
  
  
\*as an aside most descriptions in GoF fails to be patterns in the pattern language sense, which at least one of the authors admit

![](http://www.gravatar.com/avatar.php?gravatar_id=ff2995f9381e6a92064e7813dfb476f0&rating=PG&size=110&default=identicon)

Friday, February 18, 2011 9:59:56 AM UTC

My concern with technical interviews is that, quite often, they tend to over emphasize what the interviewer knows, compared to what the interviewee knows. Inconsciously (or at least I hope this is unconscious) this turns to an ego fight. "See how much more I know than you do". Or at least, "In my context I'm more buzzword compliant than you are."  
  
At that game, the interviewee always loses. Because we live in a world where learning is essentially driven by context. Your personnal "technical history" leads you to what you know today. You cannot know everything. What is important is how good you are at learning and understanding complex things. Questions in a technical interview should focus on these aspects, and these aspects only.

![](http://www.gravatar.com/avatar.php?gravatar_id=86358e3a223c4eabd68d713e053ceb34&rating=PG&size=110&default=identicon)

Friday, February 18, 2011 10:56:58 AM UTC

I like to add :  
- What is Refactoring ? Have you used it and why is it important ?  
- Which design/architecture patterns do you know that embed in .net framework ?

![](http://www.gravatar.com/avatar.php?gravatar_id=367f83bbdae20b953e8803ce8b9608d1&rating=PG&size=110&default=identicon)

Friday, February 18, 2011 11:12:17 AM UTC

It is shocking that I just did a quick Find on this page to see what had been said about "refactoring", and the word had not yet been used.  
  
So:  
  
Q: What is refactoring? How do you do it? Name three common refactorings.

![](http://www.gravatar.com/avatar.php?gravatar_id=cc060db2b5331d8cbbfe080cec4add6f&rating=PG&size=110&default=identicon)[Mark Rendle](http://blog.markrendle.net/)

Friday, February 18, 2011 11:14:24 AM UTC

And somebody had finally mentioned it between me loading the page and posting my comment.  
  
Vahid, I salute you. O>

![](http://www.gravatar.com/avatar.php?gravatar_id=cc060db2b5331d8cbbfe080cec4add6f&rating=PG&size=110&default=identicon)[Mark Rendle](http://blog.markrendle.net/)

Friday, February 18, 2011 11:17:13 AM UTC

I've been quite amused by the following typo : "a multi-tired web application". It's probably a very tired web application that's been working 24/24, 365/365 for quite some time now..

![](http://www.gravatar.com/avatar.php?gravatar_id=ea70b38ea893494ee0cd177adc0f54e5&rating=PG&size=110&default=identicon)[Andrei Rinea](http://blog.andrei.rinea.ro)

Friday, February 18, 2011 11:53:25 AM UTC

One I've used a lot this year:  
  
"When you have to decide for a bug or feature whether to re-write a chunk of code or keep an existing sub-optimal implementation, how do you approach the problem and communicate with your colleagues and managers?"

![](http://www.gravatar.com/avatar.php?gravatar_id=fac42e3f137bfe0f34b8493c41d28f9e&rating=PG&size=110&default=identicon)

Friday, February 18, 2011 1:08:07 PM UTC

Well, I disagree with the idea "I don't care about design patterns or buzzy words".  
Let's say that in an job interview you ask to the candidate:   
--If we where designing a framework with fluent interfaces, how you would model this scenario.....?  
or  
--Can you write some code to walk thru an AST using the visitior pattern?  
If the candidate doesn't known the patterns or the buzzy words, it'll take you a lot of time  
to explain what is your point or what you are asking for, other wise your chat would be more "Fluent" ;-)  
Even though I think that buzzy words and design patterns are important,  
when it comes to job interviews, I always stand for the phrase,  
"Talk is cheap, show me the code"

![](http://www.gravatar.com/avatar.php?gravatar_id=ac564150498e63873e0949a033ff31bb&rating=PG&size=110&default=identicon)[amiralles](http://www.amiralles.com.ar)

Friday, February 18, 2011 1:14:39 PM UTC

I agree with a few posters on having to be careful about question lists like this. I only use Interview Questions lists like this when I'm looking for a job myself. The reason being is I know there are interviewers out there that ask questions like this, so I memorize a lot of answers and then never use a high proportion of the answers ever again in real life work. Also, I wouldn't consider asking 2 different candidates the same questions. It just doesn't work. I remember an interview I performed a long time back where a recruiter was telling me all their interview questions the day before. That's something you might want to think about!  
  
Now, don't get me wrong, there are a few gems in there that are similar to interview questions I ask myself. But they are all primers that lead me on to the real questions which tell me "how they think" as opposed to "what they know".

![](http://www.gravatar.com/avatar.php?gravatar_id=75860e64258fc0e7a183558ac6edef34&rating=PG&size=110&default=identicon)Conor Gallagher

Friday, February 18, 2011 1:21:50 PM UTC

Actually, after re-reading your blog post I realised you're compiling a list of possible interview questions for a friend as opposed to a complete list you may use yourself!  
  
Here's one I was asked recently:  
  
Tell me about the most cost effective application you've ever written? What was it written in? Why was it the most cost effecitve?

![](http://www.gravatar.com/avatar.php?gravatar_id=75860e64258fc0e7a183558ac6edef34&rating=PG&size=110&default=identicon)Conor Gallagher

Friday, February 18, 2011 1:38:47 PM UTC

Amazing collection of question, though I don't know the answer to most of these. I spent an hour of reading it and the valuable comments on the same and that one hour was the most learned hour of my engineering graph :)  
Thanks everyone...

![](http://www.gravatar.com/avatar.php?gravatar_id=e5adbfcc4396d9b1b041fa62def9b966&rating=PG&size=110&default=identicon)[Sagar Mody](http://sites.google.com/site/sagarkm)

Friday, February 18, 2011 1:51:43 PM UTC

The YAGNI concept is an important one - don't neglect it (or misspell) ;)

![](http://www.gravatar.com/avatar.php?gravatar_id=324876b9814be0c622368a3f87bcec4c&rating=PG&size=110&default=identicon)Saul

Friday, February 18, 2011 2:07:53 PM UTC

Tim jf ... are you serious? The point of an interview is to find a person to fill the job and be good at it....not to make you, the interviewer, feel like a big guy. If your not interested in what the interviewee has to say why are you interviewing him/her in the first place?  
  
Seriously, if you did that to me I would probably cut the interview short, thank you for your time and walk out. Remember the interview process (especially for senior developers) is a two way process!

![](http://www.gravatar.com/avatar.php?gravatar_id=fb83231d59f394a7a1337e745a48502b&rating=PG&size=110&default=identicon)

Friday, February 18, 2011 2:26:35 PM UTC

The one question that stands out for me is this. In an interview I was asked what three questions would I ask to see if someone knew <insert subject matter>.

![](http://www.gravatar.com/avatar.php?gravatar_id=51d269ecb00e1079a176d055073f435b&rating=PG&size=110&default=identicon)

Friday, February 18, 2011 3:39:52 PM UTC

Describe, in as much detail as you think is relevant, what happens when I type "google.com" into a browser and press "Go".   
  
It's amazing how many people working on the web don't understand fundamental details such as request/response or the handoffs between IIS and the application server. I use this question as the entry point into more specific questions, many of which are represented here already.

![](http://www.gravatar.com/avatar.php?gravatar_id=592ce06e300c7947559cff31295ee0bd&rating=PG&size=110&default=identicon)

Friday, February 18, 2011 4:34:37 PM UTC

I think between the initial post and all the follow-up comments, there's a great diversity of general concepts (good since it applies beyond .Net) and specific concepts/acronyms (good since it enforces that you're keeping current on development trends).  
  
I think it would be a great exercise to type out my own responses in my blog, just to see where I'm at. I already saw a handful of them I don't know, and it gives a springboard for what I need to learn next! I guess I'm not as "senior" as I think I'm getting as a developer. 8^D

![](http://www.gravatar.com/avatar.php?gravatar_id=27ff4e53d6db5e5233fcdbf412604541&rating=PG&size=110&default=identicon)

Friday, February 18, 2011 4:58:07 PM UTC

While I agree with a lot of the more general questions, if someone asked me all those questions at an interview, I would likely not want to work for them. I once had someone ask me the proper c++ syntax for declaring an abstract function. I have used abstract functions several times and was able to explain what they were, but he basically wanted to rail me on technicalities like adding "= 0". These sorts of things can be looked up when needed. The guy proceeded to mention that they really wanted to hire someone who really knew their stuff (read the same book more than once) and did not want someone who needed to use a google search to look things up. Needless to say, I left there thinking that I would not work there if my life depended on it... I feel sorry for whoever ended up working for the guy.  
  
Instead of quizzing someone to death, it is better to talk about previous projects they have worked on in the past. Communication is everything in this field, and if they don't have good communication skills, none of these questions will matter. You can always read up on the latest design patterns, etc, at the time you need them.

Friday, February 18, 2011 4:58:14 PM UTC

In my opinion this interview questions are irrelevant and won't find you good developer. They will find someone who is very into theory and maybe make interviewer feel "big" in candidate's eyes. Even that I can answer for most of them easily, if someone would ask me this type of questions on interview, I would probably not accept job offer if I was given one.  
  
It reminded me one of interview - 1h15min over phone, from which good 50 minutes was about internal ins and outs of .net garbage collector, including questions like "why haven't you used reflector and other low level debugging tools to inspect what it does exactly". And that was "very important" even that it was all about Silverlight app where you have no influence over how it works anyway ;)

![](http://www.gravatar.com/avatar.php?gravatar_id=a2013bebcf29d34ff4c4e44fbe004bb6&rating=PG&size=110&default=identicon)

Friday, February 18, 2011 6:07:04 PM UTC

Don't know if it has been listed before, but I had the chance to ask a few times the question ....  
-> **Why does the CLR implementation propose both value types and reference types? Why not just one kind of type?**  
... I notice that the answer gives a good evaluation of the .NET programmer level. (Ex C++ programmers get a solid advantage here, anyway, ex C++ programmers usually becomes excellent .NET programmers).  
  
  
@Kelly: totally agre with you concerning tooling oriented question, but on this particular topic I am biaised :)

![](http://www.gravatar.com/avatar.php?gravatar_id=526161a664210d3946ca432ee787f2af&rating=PG&size=110&default=identicon)[Patrick Smacchia](http://www.NDepend.com)

Friday, February 18, 2011 6:37:14 PM UTC

Yeah I don't know ANY of the answers to these questions...but I've been a highly paid (mostly web) developer for a decade. Go figure! I guess there is still hope - the cushy jobs are out there. :)

![](http://www.gravatar.com/avatar.php?gravatar_id=dd4ccb9b1e8717f02551a32f40c870de&rating=PG&size=110&default=identicon)Danno

Friday, February 18, 2011 7:18:21 PM UTC

Two of my favorites are:  
  
1) What is the difference between "Set" logic, and "procedural" logic. When would you use each one and why?  
In terms of SQL, I often see procedural logic within stored procedures. This then goes down the path of: "Do good developers have to know SQL?", which is not important as SQL is a language. If I said: "Do good developers have to know C#?", it would be a ridiculous statement, yet I hear it all the time with SQL. There is a vast difference between them, and now with LINQ, the difference is becoming even more relevant and apparent.   
  
2) In detail, please describe how a client’s browser communicates with a web server.  
What I’m looking for here is the understanding of how the web actually works in terms of sockets. I feel this is important because, as a professional developer, this underlying knowledge bubbles up as to why host headers are required (for example), or why duplex communications is more resource intensive.

![](http://www.gravatar.com/avatar.php?gravatar_id=5955eddab324091353522c595cd70fc0&rating=PG&size=110&default=identicon)

Friday, February 18, 2011 7:36:03 PM UTC

This is a bit self-serving (Scott, feel free to moderate out), but if you think you know the answers to a lot of the questions posed here, I am currently looking to hire a Sr. .Net Developer. Send cover letter, resume, and desired compensation to me at michael \_dot\_ teper \_at\_ elanex \_dot\_ com. Please put GS106-SH in the email title. Thanks! :)

![](http://www.gravatar.com/avatar.php?gravatar_id=9804d0c6b66e60feb18c41c54247ef79&rating=PG&size=110&default=identicon)[Michael Teper](http://www.MichaelTeper.com)

Friday, February 18, 2011 9:31:24 PM UTC

I've noticed a lot of people have stated that these questions aren't good because they're trendy or they cover topics you don't know.  
  
I've interviewed with Microsoft before, and I got several questions I didn't know the answer to. Those were the questions that actually sparked discussion and were also the answers I was complimented on. For example, one question was about how I would approach designing an algorithm to efficiently sort a specific type of data. In all honesty, I had no idea how to answer the question, but I also recognized that the situation was unlikely to come up in the type of web apps I would likely be working on. I told the interviewer I didn't have a good answer to the question as asked, but I laid out an analogous situation I had solved in a web environment and explained how I solved it. Rather than giving a textbook/wikipedia answer, I had a real discussion about how I approach optimization in a context that was more relevant to the specific position I was applying for.

![](http://www.gravatar.com/avatar.php?gravatar_id=b231e07e868d33adca6135fc54ca06ec&rating=PG&size=110&default=identicon)Ian

Saturday, February 19, 2011 2:11:34 AM UTC

How do you approach mentoring/sharing knowledge with your team.

![](http://www.gravatar.com/avatar.php?gravatar_id=fa4fecbd83f5c5da19e4e2bf5a4751cb&rating=PG&size=110&default=identicon)

Saturday, February 19, 2011 3:41:29 AM UTC

@Paul Stanley To answer your first question: no. The rest of your post has been duly noted and forwarded to all known associates so they stop what they are doing immediately.  
  
</snark>

![](http://www.gravatar.com/avatar.php?gravatar_id=7e25817b47e3f6a1cec646ad15b966b3&rating=PG&size=110&default=identicon)Tim jf

Saturday, February 19, 2011 4:24:38 AM UTC

What do you read to keep up with the industry?  
Explain the differences between procedural, object oriented, and functional programming.  
If you are asked to implement something using a particular technology that you are not familiar with, what do you do first?  
Describe the circumstances that could lead two threads to deadlock.  
And of course there is the infamous [fizzbuzz](http://www.codinghorror.com/blog/2007/02/why-cant-programmers-program.html) problem.

Saturday, February 19, 2011 11:40:13 PM UTC

"Would you call yourself a craftsman (craftsperson) and what does that word mean to you?" is a dumb question to ask. Just because they wouldn't think of themselves in those terms doesn't necessarily mean that you wouldn't think of them. That's a very particular, almost dialectical language use. It would also be grossly prejudicial against candidates for whom English was not their mother tongue.  
  
Why do you ask them about YAGNI twice? Are you hoping to embarrass them when they still don't know what the acronym is the second time around.

![](http://www.gravatar.com/avatar.php?gravatar_id=3c0aac2191718ef0309dbc034d9b9961&rating=PG&size=110&default=identicon)David Heffernan

Sunday, February 20, 2011 2:37:48 AM UTC

Its better than asking about DRY twice.

Sunday, February 20, 2011 1:51:05 PM UTC

Is just me or are this interview question list always very web-development-heavy? Many questions are also ambiguous (is the sandbox question referring to execution-context-sandboxes or SCM-working-directory-sandboxes?).  
  
I'd also run away from those "Name three" type of questions. A job interview is not a game show. You want to know if a candidate understands important concepts not if she memorized all "important" terms. I was always bad at this type of questions in college. I made up with that by explaining my take on the domain, why it is important and how it differs from others. That usually got me enough points without any memorizing.

Sunday, February 20, 2011 5:47:32 PM UTC

The "big picture" here is this person is going to be leading your team. After all the technical questions are over (assuming he knows his chops), what do you really know about the person? That's why it's important to move pass code and find out what this person is really about. So ask:  
  
What do you do for fun outside of work?  
  
I'll speak for myself here, but I'm looking for two things. The first is that he codes for fun. For me this goes without saying because if you're passionate about your craft, you live and breathe it. Finally, and most importantly, I'm looking to see that this person has genuine and deeply personal activities that anchor his spirit. If he's into poetry, I want to hear about it. If he's into community gardens, I want to talk about his last project. Into running - show me!  
  
The idea is I want to know that you have a passion or two outside of the craft. Because all of us know, sometimes we have good days and sometimes we have bad days. I want to know that my team's moral and my lead's moral is going to be steady and consistent. Not fluctuating between the success or failure of our projects. A lead needs to have a fair amount of consistency between project outcomes and so this person needs to have something anchoring him other than code.  
  
What do you do for fun outside of work? I want to know that you have a LIFE.

![](http://www.gravatar.com/avatar.php?gravatar_id=fce36bb21c8287661e08e8d43c50e528&rating=PG&size=110&default=identicon)[TVD](http://techoctave.com/c7)

Sunday, February 20, 2011 6:45:01 PM UTC

After reading all the comments, I have made some observations:  
  
1) There isn't an agreement as to what a "senior software engineer" should know. But that is quite ok since different companies have different standards as to who should be a senior software engineer. I have been a senior software engineer in my second job and now I am in my 5th job and I don't expect be a senior software engineer in my current company for at least a couple of years from now.   
  
2) We all believe we are competent people (I am not saying you guys aren't, I am just saying most average and below-average developers think they deserve the job that they are interviewing for and believe that they would be able to do it decently if they are hired. And what is funny is that they are correct for a large percentage of time - not every job require superstars).  
  
2) Most people are looking for a candidate just like themselves. If the candidate knows the stuff that I know then I would probably hire them. If they don't know what I believe is important, then I probably won't hire him. It seems reasonable but the situation is quite sad if we look at the fact that what the interviewer thinks is important can vary widely from person to person.  
  
3) There are some people who doesn't read a lot and hence not familiar with acronyms and the names of the cool technology/process/framework/design strategies even though they might have a good sense of how to deal with situation involving them. For example, such a person might be able to arrive at an abstract factory solution for a problem where it is a good fit, without ever being aware that what he did has a name and is a standard solution for them problem he solved. Such people really hate the kind of questions where the interviewer asks him - what is dependency injection, even though he might be employing it in his projects (without knowing its name).  
Then there are people who are not big on previous experience but reads a lot and is aware of what is the newest thing in the technology space. They know what the different design patterns are, what TDD is, what IOC is etc even though they might never have used them in their projects or they might never be able to come up with abstract factory on their own without having read about it in some book or website. These people make up for their lack of ingenuity by reading about stuff. Those people would love the questions listed in this blog post (please note that I am not making the assumption that all the people who know the answers to the questions above are in the 2nd category, there are a lot of developers who read books and is always up-to-date on the technology space but also might have discovered abstract factory on their own)   
So which of these two kind of developers are more valuable ? I don't think we would have an agreement on that. If I am in the 1st category I am more prone to think that the 1st category developers are more valuable, same is the case with the 2nd category. This goes back to my 2nd point - we are looking for ourselves in others.  
  
4) If we know the answer to the a question from the above list, we have a tendency to think that it is a good question. If we don't know the answer, then we are are inclined to believe that the question is not really relevant to finding a good software engineer (with the following line of reasoning - I believe that I am a competent developer and if I don't know the answer to that question, hence the question is not relevant to finding a good software engineer :-))  
  
5) A good number of interviewers wouldn't be able to answer a good number of these questions themselves if asked in an interview.  
  
6) A good number of people who are already in the team for the position being interviewed won't be able to answer a good number of these questions.  
  
To summarize, i don't think we have any good solution to the problem of having to choose the right interview questions. No matter what strategy we choose, we always miss some good developers and sometimes hire a BS developer.

![](http://www.gravatar.com/avatar.php?gravatar_id=744b9fd09bb6e6da21af467158c8e80e&rating=PG&size=110&default=identicon)[Pradeep Chellappan](http://pradeepc.net)

Monday, February 21, 2011 12:52:33 AM UTC

Some of these are great and some of these are not so great, even for judging a senior level engineer. There are \_plenty\_ of "senior" engineers my dad tells stories of that are really not senior level at all that he deals with. I can't even answer half of these (on the spot) and I've been programming for 10 years.  
  
A few measures I can see that are good for judging a programmer are:  
  
1) How many and what \*kinds\* of projects have they worked on?  
2) Have they contributed to any open source project? Do they host or manage an open source project?  
3) How they deal with certain problems and why they chose the way they did  
4) How eager are they to learn new ways of doing things  
5) Do they think everything they touch is gold? If so, goodbye!  
  
I feel like anything I can just Google to look up is a useless question. It's not a judge of skill or character, just how well someone remembers a tidbit of information. How they \*use\* it, though, is not something you can Google. Case in point: "On this piece of paper, lay out an architecture for a so-and-so type of application." I don't think there's a right answer and it'll be far from optimal, but I'd be more interested in seeing how they arrive at their solution.  
  
Einstein once said, "Why should I remember anything if I can just look it up?" Words I live by.

![](http://www.gravatar.com/avatar.php?gravatar_id=b924bc0147903cbd7a4506d7d26ab328&rating=PG&size=110&default=identicon)

Monday, February 21, 2011 8:58:39 AM UTC

If you were asked to build an application that was "scalable", what information would you need to know and how would you use this information to build and test your solution.  
  
What is the difference between scaling up and scaling out a solution and what are the challenges or limitiations of each approach?

![](http://www.gravatar.com/avatar.php?gravatar_id=1f7df985cd7fac714c9840ac21f7d54c&rating=PG&size=110&default=identicon)

Monday, February 21, 2011 1:47:21 PM UTC

Pretty interesting questions and sort of sad in a way. The problem with this approach to interviewing is that programming (especially in the Microsoft "churn out a new framework by lunchtime" world) changes so quickly no one really knows it all. Or rather, when someone does master something its obsolete in a few years. So the relavance of much of this information is either domain specific (i.e. You work for a hedge fund and do lots of multi-threaded realtime work) or "time" specific.. i.e. You came into programming when ADO.Net was really big.. so your an expert in that, however you know nothing about Linq!  
  
What I'm getting at is that in this fast changing industry its nearly impossible to become and "expert" for more than a few years. Unlike other professions like Law, Accountancy, Medicine where every year you build on your knowledge and thus your skill improves, software requires you to re-learn the same things in a slightly different way every 3 yrs!  
  
When I studied at University there was no such thing as design patterns, TDD, BDD, Mocking etc... To be honest you would be hard pushed to find anyone who did that stuff regularly even 5-6 yrs ago. So in that climate how can you test for real seniority in the field when for most of us, anything we learnt 10 yrs ago is useless now.  
  
The interview questions are good in some ways because they pull out the "fans". The die-hard, live, eat, breathe code type people. And if you need that because your looking for a wonder kid who can save your ass then thats fine. But there are so few of those people because most of us want a life! They dont want to spend the rest of their lives learning how to display "hello world" in another language / framework for th 10th time in their career.   
  
I think the questions are really a reflection of how sad a career choice software development can be if you are looking for a long term profession. At the end of the day its a young persons game or a game where you will not have a life outside of it if you want to remain in it. You have to choose what u want I suppose...

![](http://www.gravatar.com/avatar.php?gravatar_id=45a6148653023ad243cf827f96158f4a&rating=PG&size=110&default=identicon)albsure

Monday, February 21, 2011 2:43:37 PM UTC

What do you know about "realtime", "NoSQL", "Socket.IO" and "Nodejs"?

Monday, February 21, 2011 2:48:21 PM UTC

1. What do you know about "realtime", "NoSQL", "Socket.IO" and "Nodejs"  
2. Have you hard of "Brewer's conjecture" or "CAP theorem"? What is it?

Monday, February 21, 2011 3:04:33 PM UTC

As long as you the interviewer are open to taking in different approaches other than your own (no you're not a God and your way is not the highway pal) for each of these topics (every developer has their preference for example on how best to decouple, etc.) then these are alright to ask...and is an excellent list to take SOME off of but you wouldn't want to ask all of these, it's just asking for too much perfection in a developer. It's when you get those interviewers who think only their way is right and thus "the interviewee fails because of it".  
  
I think the list is legit...for a Lead position. But looks like Sr. Devs are Lead level basically at MS.

Monday, February 21, 2011 3:16:10 PM UTC

I love Mark's suggestion above of testing with code that's likely to come up at the workplace. While I might not know the specific buzzwords I'm being asked about, I can take a pretty good guess at what well- (or badly-)written code does, and how I could make it better -- regardless of what language I'm working in. If it's something like a one-line Perl program, that's one thing, but a "normal" routine, I could figure out.  
  
Of course, with any luck, I won't have to go through any job interviews in the near future. :-)

![](http://www.gravatar.com/avatar.php?gravatar_id=3eda6fcd3204ef285fa52176c28c4d3e&rating=PG&size=110&default=identicon)

Monday, February 21, 2011 5:32:16 PM UTC

Why is it wrong to forget to put a cover sheet on your TPS report?

![](http://www.gravatar.com/avatar.php?gravatar_id=1bbb715054f18161771f171463ac047e&rating=PG&size=110&default=identicon)

Wednesday, February 23, 2011 7:23:21 AM UTC

Good article. "What are some alternate ways to store data other than a relational database" would really test the knowledge of somebody.

![](http://www.gravatar.com/avatar.php?gravatar_id=fde306145391eef24a82024702024308&rating=PG&size=110&default=identicon)[Gautam](http://fast-code.sourceforge.net/)

Wednesday, February 23, 2011 5:07:47 PM UTC

What motivates you?

Mathias

Wednesday, February 23, 2011 5:16:31 PM UTC

Can you inherit a value type, and is that (yes/no) a good or bad thing?  
  
Expain/teach me about the architecture/design of one of the systems you recently worked on. What was good/bad about it and why?

Mathias

Wednesday, February 23, 2011 5:20:36 PM UTC

What makes a software project successful?

Mathias

Wednesday, February 23, 2011 5:34:07 PM UTC

I think the point we are all missing is not getting all the questions answered correctly, but the attitude, personality, response, controlling frustration etc are important factors when working in team environment. You can be a super dude, but if you are working with 1/2 dudes then you have to slow down as well. I would have some serious doubts about a person who would ask all these questions in an interview.

![](http://www.gravatar.com/avatar.php?gravatar_id=fe01a830d10e6c386c3f04276a887903&rating=PG&size=110&default=identicon)Adann

Wednesday, February 23, 2011 7:09:36 PM UTC

Its a great list.  
  
I also started a .net question series on my blog (http://ankushbhatia.wordpress.com/category/questions/) where dev shares their views on different approchs http://ankushbhatia.wordpress.com/category/questions/  
  
Though I find really diffcult if somebody asks me a list of questions like this and expect to answer everything.   
  
Ankush

![](http://www.gravatar.com/avatar.php?gravatar_id=20b9bd8eba9c4aaa50100c19772a1d18&rating=PG&size=110&default=identicon)Ankush

Wednesday, February 23, 2011 9:20:37 PM UTC

Have You tried functional programming? What are the key differences that matter to You? When Do YOu like to use functional and when object?  
What is the difference between programming a website (a shop, a social network) and a high-volume processing system (a transaction processing system a risk simulation engine). Do YOu use different patterns, tools etc? What stays the same.   
What's You favorite algorithm? When was the last time You applied some well-known (or perhaps not so well known) algorithm to a problem? Did You solve some puzzles lately using computer programming?  
  
I personally the last one. I like programmers know problem solving techniques, not only frameworks and patterns. This make them also aware of something else than keep up to speed with the latest technologies and patterns (which change every 2 years apparently - something like a moore law for software development)

![](http://www.gravatar.com/avatar.php?gravatar_id=c59c3b79ba851df0fecf5f718a66ed1d&rating=PG&size=110&default=identicon)

Sunday, February 27, 2011 3:13:50 PM UTC

Must add...   
  
Why do you want to work as a developer here? Why don't you go home and write the next \*big thing\* yourself? If the developer doesn't see the value in collaboration, then I think somethink is missing. I think it's also a good ego-check for 12 page CV's. ;)

![](http://www.gravatar.com/avatar.php?gravatar_id=d83680486bdcb5cde870987a0285f024&rating=PG&size=110&default=identicon)

Monday, February 28, 2011 4:24:54 AM UTC

I have found after 15+ years in this industry and reading the comments here that I am one step closer to wanting to sell painted coconuts to tourists in Cancun.

![](http://www.gravatar.com/avatar.php?gravatar_id=3bfc033e029b5eaf0906e3558b58ac9a&rating=PG&size=110&default=identicon)

Saturday, March 12, 2011 11:18:35 AM UTC

I think you've reverse-cargo-culted... Confusing the ability to recite "latest trend" definitions with the production of quality software. The lesser of your offenses is the implicit assumption that OOD is the only principle that matters, thereby sideswiping those of us that might use different paradigms to deliver quality software. I personally gave up design patterns once template support was added to C++... And have since moved on to a more Functional style of programming.   
  
The absolute best way to interview, bar none, is to screen the applicants by having them complete a programming problem. Something not too complex, but not overly simple, so you can actually see their code (you wouldn't hire a band for a party w/o hearing them first).. Then, if they pass that test, bring them onsite for a day of whiteboarding (you can start with FizzBuzz, and work your way up to code to check if a graph is acyclic)...   
  
Unless of course, you're mainly interested in how well someone can call an API and write a consumer facing website, in which case I guess these questions work well.  
  
"Object-oriented programming is an exceptionally bad idea which could only have originated in California." -- Edsger Dijkstra  
  
"I find OOP technically unsound." -- Alexander Stepanov

Sunday, March 13, 2011 5:21:12 AM UTC

I think the interview questions for this career is totally tough, as tough as its competition. You know, being a software engineer is a tough job, it requires a lot of effort and logic to cope up with the career.

![](http://www.gravatar.com/avatar.php?gravatar_id=c64abb71d5e752f8d61a2816025d8b99&rating=PG&size=110&default=identicon)[interview preparation](http://www.preparationinterview.co.uk)

Monday, March 14, 2011 2:39:11 PM UTC

In my opinion all this questions are relevant, because here we are stating potential questions, that a senior software engineer could encounter in an interview. Anyway I don't think there is a good question and a bad one. Even if the question has little or no value, even if the candidate doesn't know the buzzword, it is always interesting to see how they manage a response and how they react to this situation. I join many others here in that, in an interview, we should aim for knowing the candidate and I assume that that's the purpose of the candidate also. For that purpose we only have one way, discussing and arguing. we should be able to evaluate the person in front of us and figure out if things will work smoothly with him. ;)

![](http://www.gravatar.com/avatar.php?gravatar_id=11fd76d71d624f861c3e558d8eb21e2a&rating=PG&size=110&default=identicon)

Tuesday, March 29, 2011 9:11:48 AM UTC

Thanks Scott, Two interviews this week with technical tests both ripped from this page. The interviewers believing that i should know the answers to ALL the questions asked because Hanselman says so.  
So i sit here with no job, trying to memorise the answers to all these questions.

![](http://www.gravatar.com/avatar.php?gravatar_id=8c323ac64e4491d9bd9dc790b31ec933&rating=PG&size=110&default=identicon)

Wednesday, March 30, 2011 8:34:30 AM UTC

I'm really sorry to hear that, Ben. That wasn't the intent of this post and I'm sorry that the interviewers used these questions against you.

![](http://www.gravatar.com/avatar.php?gravatar_id=719c91f5c3013e43ee46ed2bdc67f883&rating=PG&size=110&default=identicon)[Scott Hanselman](http://www.hanselman.com)

Friday, April 01, 2011 6:43:41 AM UTC

This is one of the reasons why I removed "Senior" from my CV. Really sad industry that I've been working on since age 16. At the age of 36, I reverted back to (junior) developer with enterprise applications done and selling it on my own. We are all kids playing with technology all day and night. Try to give yourself a month break and come to interview, I will make sure you look like a puppy software developer after that with latest buzzwords... You need to work on stopping the madness not spreading it all around!

Daniel

Friday, April 15, 2011 3:39:54 AM UTC

How about "how many lines is a typical method of yours?" Follow up with "why?"

![](http://www.gravatar.com/avatar.php?gravatar_id=c6d819207a3010b39d13e1f59f2c0029&rating=PG&size=110&default=identicon)

Monday, May 16, 2011 1:55:41 PM UTC

What? I thought Gang Of Four was a cool underrated english band! Obviously, I still have to learn a lot of things. Thank you Scott for this article!

![](http://www.gravatar.com/avatar.php?gravatar_id=8a7b42efefefaabd3900351c54dfe4ab&rating=PG&size=110&default=identicon)

Wednesday, May 25, 2011 12:53:40 AM UTC

I can't believe no-one has asked yet but where are the (comprehensive list and explanations of) answers at then? And because no-one seems to want to say what's the answer to x (sorry I mean foo lol) I figured I would ask! :)

![](http://www.gravatar.com/avatar.php?gravatar_id=1f3bc59b9207e5cfcd7ef321a2dd9450&rating=PG&size=110&default=identicon)[SteveyTxxx](http://www.steveyt.com/blog)

Tuesday, May 31, 2011 2:53:37 AM UTC

These questions are useless trivia for anyone working in corporate software development. Maybe slightly useful for someone who wants to work for a so-called "software company". But I've used too many products produced by said companies where everyone knew "Gang of Four" design patterns, and no one knew how to make a tool that a business user could use without calling the local IT staff every 5 minutes.   
  
Your n-tiered application with a beautiful object graph and a large ORM layer would get you a look of "you wanna do what!?" from most corporate app dev managers out there. No one gives a flying crap about your megabytes of XML config files - they just want the business users to be happy.  
  
Questions for corporate software devs:  
- Can you gather the real requirements directly from the users, after being emailed the contradictory "requirements" by the business analyst?  
  
- Can you code in whatever language the idiot Application Architect thinks is in style this week? Can you "fake" enough so-called "dependency injection" BS to get them off your back so you can get back to actually building apps that people use? Can you pretend to care about "Gang of Four" when you know its just what you've been doing for years anyway?  
  
- Can you pretend to be interested in the new buzzword that your manager wants you to learn about? He just got back from a conference and is really interested in XML-RPC since its supposed to be the bee's knees!

![](http://www.gravatar.com/avatar.php?gravatar_id=0b5ab17d35dd38eb74b4e224830a2edd&rating=PG&size=110&default=identicon)[Meh](http://%20)

Wednesday, June 01, 2011 5:27:51 AM UTC

trolling, trolling, I am trolling !!!

![](http://www.gravatar.com/avatar.php?gravatar_id=fd5d40f7921eb511d9a149c2a7b18686&rating=PG&size=110&default=identicon)Vasile

Wednesday, June 01, 2011 5:31:16 AM UTC

Here are some answers to some of the questions  
  
http://standupprogramming.com/2011/02/21/purely-fabricated-interview-expert-pattern/

![](http://www.gravatar.com/avatar.php?gravatar_id=fd5d40f7921eb511d9a149c2a7b18686&rating=PG&size=110&default=identicon)[Vasile](http://standupprogramming.com)

Wednesday, July 27, 2011 2:15:15 PM UTC

Interview questions are important. I am digging all patterns.  
  
How do we figure out if we are interviewing with the right company? How do we interview the interviewer on their "best practices", expectations, scope, BS ratings (AAA is the poorest BS rating), team dynamics....

![](http://www.gravatar.com/avatar.php?gravatar_id=7c12a5c655ec34c2fbce0d83cf795ae6&rating=PG&size=110&default=identicon)SamG

Sunday, September 04, 2011 11:07:11 PM UTC

Name the people in [this](http://i.imgur.com/cHCRo.jpg) picture, and explain why it's hilarious. (Sorry, couldn't resist :)

![](http://www.gravatar.com/avatar.php?gravatar_id=0c7d4784d453bbec161533e92e1fa5f3&rating=PG&size=110&default=identicon)

Comments are closed.
