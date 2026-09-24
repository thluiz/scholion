---
url: "https://dev.to/ben/what-computer-science-concepts-should-devs-without-a-cs-background-prioritize-learning"
captured_at: "2026-09-24T23:47:48+01:00"
title: "What computer science concepts should devs without a CS background prioritize learning?"
domain: "dev-to"
---

[![Ben Halpern](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F1%2Fbabb96d0-9cd2-49bc-a412-2dc4caf94c2a.png)](https://dev.to/ben)

## Top comments (64)

Subscribe

Collapse Expand

[![jedd\_ahyoung profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F2890%2FM9-ZI__X.jpg)](https://dev.to/jedd_ahyoung)

Some developers come from a Computer Science background. Others, like me, never studied Computer Science in an academic environment.

In my opinion, the three main things for developers without a Computer Science background to study are Data Structures, Algorithms, and Lambda Calculus. Why these three?

1.  Data Structures. These are the building blocks of data inside of a program. There are many different types of data structures, both simple and complex, and all of them have advantages and disadvantages (in terms of reading, writing, and space complexities). When a dev has to model a problem domain, he or she will first reach for the a data structure. It's good to know the pros and cons of different types of data structures and what they can offer in order to make the best choice for the problem domain. Understanding data structures will help a developer to solve problems quickly and efficiently using the right tools; in some cases, it will also give a better understanding of how data is mapped to computer memory.
    
2.  Algorithms. Computers are fast - very fast - but solving problems still takes time. Devs should understand algorithmic complexity, know the advantages and disadvantages of specific approaches, and cultivate the foresight to make algorithmic choices based on input and time. More importantly, devs should be able to identify problems which can be solved (trivially or non-trivially) versus problems that cannot be solved at all within a reasonable time period. Algorithms, in conjunction with Data Structures, are the meat and potatoes of our programs.
    
3.  Lambda Calculus. Modern languages have many design patterns - OOP, functional, declarative, and so on - but Lambda Calculus is a basic, simple model of computing that lends itself very well to any developer who wants to improve the way that they read, write, and understand code. Gaining an understanding of Lambda Calculus can allow a developer to think in terms of inputs and outputs, which lead to further inputs and further outputs. Understanding the compositional, functional style of Lambda Calc can make many problems much more accessible. With Data Structures and Algorithms, Lambda Calculus can elevate a developer to the next level.
    

Collapse Expand

[![mistermocha profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F16103%2Fcbab1dd8-b8ba-4471-aa63-46c3b1bfddcc.jpeg)](https://dev.to/mistermocha)

Non-CS-major here. Got any suggested readings on algorithms or lambda calc?

Collapse Expand

[![lluismf profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F13760%2F84d4dfac-ddc5-4cbc-aa73-3124f1a39040.JPG)](https://dev.to/lluismf)

Collapse Expand

[![aweary profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F688%2F6886061.jpeg)](https://dev.to/aweary)

I really liked the introduction to Lambda Calculus in Haskell: Programming from First Principles: [haskellbook.com/](http://haskellbook.com/)

Collapse Expand

[![adambrandizzi profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F1591%2FfKayanWx.jpg)](https://dev.to/adambrandizzi)

Besides data structures and algorithms, there is some math stuff that is surprising helpful. Calculus is fundamental to model a lot of real problems and to think in terms of velocity and aggregation. Linear algebra is pure computing: once you get to think in terms of matrices, a lot of very, very complex stuff becomes way simpler. Number Theory is fundamental for a lot of disciplines. But the most important math subject IMHO is Probability and Statistics: it permeates everything.

Besides that, the basic of networking and cryptography are very useful as well.

Collapse Expand

[![janpeuker profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F50985%2F6fc070dd-7ee8-4180-913a-5925c043200f.jpg)](https://dev.to/janpeuker)

+1. The one thing I do regret most not paying attention to in my CS degree (which might be a good way to think about the question above) was probability and statistics. With ML this is becoming ever more important. Personally, I still don't feel 100% confident about my maths.

Regarding data structures and algorithms: I find most lists out there not really useful as they tend to cover data structures either not really in use anymore (e.g. linked lists) or so frequently used that a CS degree doesn't add detail (e.g. hash tables). The biggest advantage of a university course is that it should teach you concepts and ideas you might one day find useful (e.g. bloom filters) - instead of tools that make you productive right now. As such, I believe graph algorithms, binary search, finite state machines, lambda calculus and yes, complexity analysis, are the most useful ones (all mentioned below) - alongside various Patters which are also mentioned below.

Collapse Expand

[![dev3l profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F20193%2F2f82dc32-cef2-48ac-8397-664407731715.png)](https://dev.to/dev3l)

[Justin L Beall](https://dev.to/dev3l)

Seasoned Staff Engineer at Artium, expert in agile methodologies and software development. Adept at leading teams and pioneering transformative solutions.

*   Email
    
*   Location
    
    Medina, Ohio
    
*   Education
    
    Agile Ninja
    
*   Work
    
    Staff Engineer at Artium
    
*   Joined
    
    May 30, 2017
    

• [Sep 8 '17](https://dev.to/ben/what-computer-science-concepts-should-devs-without-a-cs-background-prioritize-learning#comment-m42)

*   [Copy link](https://dev.to/ben/what-computer-science-concepts-should-devs-without-a-cs-background-prioritize-learning#comment-m42)

*   [Report abuse](https://dev.to/report-abuse?url=https://dev.to/dev3l/comment/m42)

My favorite non-CS computer science algorithms book is: Grokking Algorithms: An illustrated guide for programmers and other curious people.  
It stays at a pretty high level, touches the major algorithms, and explains big O very well!  
[Grokking Algorithms](https://www.manning.com/books/grokking-algorithms)

Collapse Expand

[![jt\_grimes profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F2873%2FPwiJqAQT.jpg)](https://dev.to/jt_grimes)

Big O notation, an understanding of what algorithms are "expensive," and an understanding of what happens with "expensive" algorithms at large scales.

Collapse Expand

[![ben profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F1%2Fbabb96d0-9cd2-49bc-a412-2dc4caf94c2a.png)](https://dev.to/ben)

[Ben Halpern](https://dev.to/ben)

A Canadian software developer who thinks he’s funny.

*   Email
    
*   Location
    
    NY
    
*   Education
    
    Mount Allison University
    
*   Pronouns
    
    He/him
    
*   Work
    
    Co-founder at Forem
    
*   Joined
    
    Dec 27, 2015
    

• [Feb 7 '17](https://dev.to/ben/what-computer-science-concepts-should-devs-without-a-cs-background-prioritize-learning#comment-30e)

*   [Copy link](https://dev.to/ben/what-computer-science-concepts-should-devs-without-a-cs-background-prioritize-learning#comment-30e)

*   [Report abuse](https://dev.to/report-abuse?url=https://dev.to/ben/comment/30e)

I second Big O notation and this whole idea. I didn't do an entire computer science degree, but I did some, and these concepts are what have stuck with me as considerations that come up a lot.

Collapse Expand

[![georgeoffley profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F3198%2Fccc96445-59d2-481e-b8ad-a44e5e91b8af.jpg)](https://dev.to/georgeoffley)

Time to write my Big O practical applications essay. Still need to fully understand it though. I read a great book about CS concepts written by someone who didn't have a CS degree. Not an ad but a good book.

[bigmachine.io/products/the-imposte...](https://bigmachine.io/products/the-imposters-handbook/)

[![patriklarsson profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F38098%2F3b005399-a182-4dff-96c0-57ff6b7c65f1.png)](https://dev.to/patriklarsson)

Ah, someone beat me to it I see :)

I couldn't agree more about this recommendation.

Collapse Expand

[![mattbidewell profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F3975%2F982827a4-82e4-42c4-ac3a-3afa6fcdae61.png)](https://dev.to/mattbidewell)

For some reason at my CS degree we hardly touched on Big O. Does anyone have some great resources for gaining a better understanding?

Collapse Expand

[![evanoman profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F19733%2Fbf5f4ed1-0938-47da-a6b6-a9ae78bd880e.jpg)](https://dev.to/evanoman)

I know it is expensive and massive but I really think every developer should have a copy of [CLRS](https://mitpress.mit.edu/books/introduction-algorithms). It is well organized, well written, and extremely thorough. In fact I was just paging through it today to review a few graph algorithms.

Collapse Expand

[![antero\_nu profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F32416%2Fb8461c01-bafb-4706-8f4f-5b9fadb22040.jpg)](https://dev.to/antero_nu)

[Antero Karki](https://dev.to/antero_nu)

Software developer in Sweden. Always interested in good opportunities in warmer climates...

*   Location
    
    Sweden
    
*   Education
    
    Some
    
*   Work
    
    Software Developer
    
*   Joined
    
    Sep 6, 2017
    

• [Sep 6 '17](https://dev.to/ben/what-computer-science-concepts-should-devs-without-a-cs-background-prioritize-learning#comment-lk7)

*   [Copy link](https://dev.to/ben/what-computer-science-concepts-should-devs-without-a-cs-background-prioritize-learning#comment-lk7)

*   [Report abuse](https://dev.to/report-abuse?url=https://dev.to/antero_nu/comment/lk7)

Most self taught colleagues I've worked with, and others as well, are missing skills in writing good clean code. If you write good code everything else will be much easier to fix later e.g. performance issues, bugs.

So I'd suggest reading "Clean Code" by Robert Bob Martin, he's not only fun to read and watch holding talks, but is good at explaining things so that they make sense.

Collapse Expand

[![high\_rigour profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F1649%2FW6ui1UDg.jpeg)](https://dev.to/high_rigour)

How to structure systems to support concurrency.  
We are entering a major shift in industry where concurrency is going to become mandatory. Programming with shared data and interwoven state is going to cause massive loss of time and energy in the future.  
The sooner we begin the shift toward a more stateless asynchronous programming methodology the better we will all be.

Collapse Expand

[![sadrobot profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F2677%2Fzdp08ZMt.jpg)](https://dev.to/sadrobot)

If you are a web developer: Databases. I took an intro to databases course in college and even at that pretty beginner level, I still use what I learned in that class every day. Technology stacks may change, but data isn't going anywhere.

Collapse Expand

[![shiling profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F11766%2F4a059374-4b4f-4777-bf0a-8a0301476298.png)](https://dev.to/shiling)

Yes I strongly agree. I had worked with new self-taught web developers and database skills was the most glaring thing they needed to learn. Knowing how to design a database to write SQL queries that has good enough read and write performance, knowing ACID concepts, knowing when transactions are needed, knowing the differences between SQL and no-SQL databases and to pick the best one to use rather than the easiest to use. Database is one of the most important things a web developer should know.

Collapse Expand

[![lluismf profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F13760%2F84d4dfac-ddc5-4cbc-aa73-3124f1a39040.JPG)](https://dev.to/lluismf)

Easily the most fundamental skill to have besides algorithms and data structures.

Collapse Expand

[![jacoby profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F3506%2Fd563bbf3-6636-49bf-b704-e38a0d0195f4.jpg)](https://dev.to/jacoby)

I'll toss a do-not in here: _Sorting._

Sorting can be fun, and can produce some [interesting visualizations](https://www.google.com/search?q=sorting+visualizations&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj7p6bJt97VAhVD94MKHRIoAqoQ_AUICigB&biw=1680&bih=936), but the best for most situations is already built into your language, probably, and it likely goes by the name `sort()`.

Collapse Expand

[![danidee10 profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F2359%2F11032373.png)](https://dev.to/danidee10)

There are a lot of things to learn, But the most important IMHO should be Data Structures and algorithms.

With some basic knowledge about both, Writing code becomes less about "Let's get this to run / work." and more about "how efficient is this? / could i do this is a more efficient way?"

Naturally the search for efficient ways to do stuff will lead to some other important concepts like concurrency, caching etc

Collapse Expand

[![etresoft profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F2562%2FAvatar.jpg)](https://dev.to/etresoft)

Stand-alone code.

At my current employer, I am one of the few people, if not the only person, with a computer science background. Yet almost everyone is a "coder". Some are writing Stata, some R, some Python, and I've heard rumors of a couple of web and db developers. They know far more math than I do and can Google the rest.

But what what they can't do is write stand-alone, automated code. One of the skills someone with a CS background must learn is how to write code that compiles and runs on someone else's machine. CS students have to submit source code that the professor will compile and run. The "but it works on my machine" refrain doesn't cut it in a CS class. Code has to run and run correctly under someone else's account, on someone else's machine, and maybe with different input data. That is a skill you can only get from a CS class, not Google, and not Coursera.

Collapse Expand

[![josesaldana profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F32832%2F613380e4-7c0a-45dd-90bf-a8ace85bffd3.jpeg)](https://dev.to/josesaldana)

Hi John. Could you please elaborate a bit more on this? A bit more of explanation would be very appreciated. Thanks!

Collapse Expand

[![etresoft profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F2562%2FAvatar.jpg)](https://dev.to/etresoft)

Most of the responses here are technical issues, like Big O notation or lambda calculus. Anyone can figure that stuff out on their own. I am talking about engineering issues that are important when building something. The differences between being a coder and a software engineer are not new. These engineering issues can be learned too, but someone learning on their own might never be aware of their existence to begin with.

I saw this in action at my (now former) employer. They knew about Big O notation, math of all kinds, and git. But they couldn't make a program run the same way twice, or on a different machine. There was no knowledge of UNIX, environments, dynamic loading, databases, information theory, text encoding, testing, validation, chain of reference, etc. Yet, by the only metric that mattered, securing more funding from wealthy donors, they were wildly successful.

I also see this in the Apple Developer forums. To get an app in the App Store, all you have to do is get it to launch once, for about 30 seconds, and maybe change a screen, on an Apple reviewers device. That is a challenge. Those indie developers, whether working alone or with a roomful of people just like them, don't understand the issues necessary to make an app run on someone else's device. They can figure it out eventually of course. But it is much more frustrating than having worked through those issues in a 2nd year data structures course in University.

[![atanask profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F17346%2Fd33544cd-c061-4185-841c-56e8cd7bdf65.jpeg)](https://dev.to/atanask)

[Atanas Kostovski](https://dev.to/atanask)

Software Engineer, loves working with Python, PHP, Javascript, and everything about Linux and Docker. Still student, but working part time as DevOps.

*   Location
    
    Skopje
    
*   Education
    
    Computer Science and Engineering
    
*   Work
    
    DevOps at Keitaro
    
*   Joined
    
    Apr 23, 2017
    

• [Dec 25 '17](https://dev.to/ben/what-computer-science-concepts-should-devs-without-a-cs-background-prioritize-learning#comment-1n55)

*   [Copy link](https://dev.to/ben/what-computer-science-concepts-should-devs-without-a-cs-background-prioritize-learning#comment-1n55)

*   [Report abuse](https://dev.to/report-abuse?url=https://dev.to/atanask/comment/1n55)

I understand your point, but the question was specific to CS, not Software Engineering as a topic. But I'm sharing your opinion here - CS is not that hard to learn on your own, while I notice that self taught devs lack the Software Engineering skills and practices, and don't even know about the existence of them.

I'd guess it's like that because CS topics are very hot and trending buzz-words that you can easily hear about and google random course/book. But Software engineering topics are a bit more specific, and you have to know about them before searching for materials.

For further actions, you may consider blocking this person and/or [reporting abuse](https://dev.to/report-abuse)
