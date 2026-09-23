---
url: "https://blog.avanscoperta.it/2021/09/14/domain-driven-design-meets-functional-programming-scott-wlaschin/"
captured_at: "2026-09-23T18:41:21+01:00"
title: "Domain-Driven Design meets Functional Programming | Avanscoperta Blog"
domain: "blog.avanscoperta.it"
---

Domain-Driven Design meets Functional Programming
Matteo Baglini, Scott Wlaschin
•
Interviews With Experts
•
Sep 14, 2021
Matteo Baglini interviews Scott Wlaschin

One of the things we love the most in Avanscoperta is putting together great minds and see what happens once the connection is made.
So what's better than asking our friend and trainer Matteo Baglini to interview Scott Wlaschin aka Mr. Domain Modeling Made Functional?

Domain-Driven Design and F# do seem like an odd pair, but with this in-depth conversation we find out that they actually work very well together, that both have an unexpected appeal to non-developers, and that it's very easy to explain what a monad is.
Really? Read on and find out more.

Matteo: One is always curious about how others kicked off their careers. How did you get started into programming?

Scott: I didn't start programming until I was in my 20's. My dad had a computer and needed help with managing a big data set, so I learned how to program. I'm old, so that was back in the dark ages, when computers still had floppy disks.

Anyway I discovered that I really enjoyed designing and coding and that got me started on learning programming seriously. I read lots of programming books and I especially loved learning new languages: I started with Prolog, then Smalltalk, then Python and PHP, and then C#, and now I'm mostly using F#.

Matteo: What do you do in your daily life? What's your job and what keeps you busy?

Scott: Right now, I make a living by consulting and training, mostly in F#. I made a deliberate choice to move away from big cities and to live in the countryside instead. It's way less stressful, and my cost of living is much lower, which means I can be quite lazy.

Matteo: Functional programming is currently enjoying his moment of "hype". Do you reckon it's here to stay or is it just some temporary fashion? And what's the most popular of them all?

Scott: Yes, I think that functional programming is here to stay. I've lived through lots of hype cycles so I think I am quite good at recognizing them now, such as the hype around microservices.
Functional programming is a fundamental paradigm of programming -- it's older than object-oriented programming -- and I think it should be part of every professional programmer's toolkit.

The ideas in FP are seeping into object-oriented languages as well. For example, Java added lambdas recently, and C# has just added immutable records.  
I think that many people are now discovering the benefits of immutability and deterministic code, and trying to change the way they work to incorporate these ideas.

Matteo: Where should one not use functional programming? What are its cons and disadvantages?

Scott: Most real-world programs consist of transforming data, generally in some sort of a pipeline. Functional programming is excellent for this. On the other hand, if you have a distributed system with independent components, then an actor model approach is appropriate, such as the way that Erlang works. Or if you care more about behavior than data, such as with a graphical widget library, then an object-oriented approach would be more suitable.

I don't think that there are drawbacks with functional programming in itself, as long as it is used appropriately, but there is a tendency by some in the functional programming community to be extremist about functional programming concepts, and make things very mathematical or very abstract, and that can be off-putting to beginners.

Matteo: Let's dig into F# a little more. Is there an environment where this particular programming language "works better"? Any language where libraries are actually designed for f# and not only adapted?

Scott: Well, I am biased, of course, but I think that F# can do everything that C# and Java can do, which is to be used as a general purpose language. There are lots of people using F# for development, especially in finance and trading, but many libraries are not public -- the companies involved like to keep a competitive advantage!

Matteo: Explain to us some of the most interesting constructions of the functional programming jargon. Beginners with FP often complain that it can be a bit difficult to grasp. What do you reckon? Did you have the same issues when you started off?

Scott: Yes, this can be a problem. Until recently, FP programmers tended to have a very mathematical background, and were happy to use mathematical jargon.

One of my goals in my teaching is to avoid that jargon, as I don't believe it is necessary or helpful. For example, a scary word like "monad" can be explained as just a pattern for chaining together certain kinds of functions without ever using that word.

It's nice to see that there are now many good FP resources available that focus on practical things rather than theory, so I think the jargon problem is going away.

Matteo: We know you've been working a lot with what apparently seems like a weird couple: Domain-Driven Design and Functional Programming. Is the marriage between DDD and FP more a strategic or a tactical choice? How did that come to life?

Scott: I've always been a fan of user-centric design, and so when I read the DDD book, it resonated with me immediately. And then when I learned F# some years later, I realized that FP was a great fit for DDD.

Here's an example of what I mean: DDD emphasizes composability and autonomy for subsystems, and so we need to be sure to do this when we program our implementation. OO languages support composability and autonomy in theory but often in practice the code can become tangled up easily. FP languages automatically guide you to write composable and autonomous code because there is no mutable state and no side effects, and so it is much harder for components to become entangled.

Matteo: We can implement a domain model both with Object-oriented programming or with Functional programming. Is the one done with FP better than the other? If so, why? What are the differences?

Scott: There are two things that stand out for me. First, FP languages have an "algebraic" or composable type system, which makes it very easy to model a domain, especially choices, in a concise way. In human languages we use the words "AND" and "OR" to define a model, and these words map directly to an algebraic type system. In OO, choices would be modeled with subclasses, which is more verbose and less clear.

Second, FP encourages a one-directional "pipeline" approach which is not only easier to understand but also maps better to most business processes than an OO approach.

Matteo: How do domain modeling and functional programming work in a distributed world (aka microservices architecture)?

Scott: Within each autonomous subsystem, I would treat it as a domain in its own right and use FP for domain modeling in the usual way. For communicating between subsystems, I would use the standard technique of buffered asynchronous messages (aka queues).

Matteo: Domain-Driven Design and Functional Programming. Which one is the most complex to grasp for a dev or a team? And, should one have to ditch one… which one?

Scott: Domain-Driven Design is easier to understand -- the basic principles are simple. Working in an FP way is a new paradigm for many people, and will require a bit of time to become comfortable with.
However, DDD is harder to actually put into use, because it requires collaboration and cooperation from other people. Just like "agile", it is easy to talk about but much harder to practice well, just like anything when other people are involved!

If I had to ditch one, it would depend on the context. If it is a large project, then not understanding the domain is asking for problems, so a DDD approach is more important than any particular implementation language. If it was a smaller project, I would try to become a domain expert myself, and then I could ditch the DDD process and program in F# without even talking to anybody else!

Matteo: DDD and Functional Programming -- is the "general public" ready for them? Where do you see resistance in adopting them? Let's leave aside their marriage for a moment and talk about each one of them.

Scott: As I said above, DDD is easy to understand and many people will be happy to try it out. But then it often becomes bogged down in process, or technical jargon, and people sometimes end up disliking "DDD", which is a shame.
As for FP, there is a lot of resistance from programmers because it is not familiar. In my experience though, there is no resistance from non-developers! When I show them the domain model written in F# they say: That looks great! Where's the code?

Matteo: To know something is one thing, to teach it is another altogether. When did you start teaching functional programming to other developers and teams?

Scott: I've always enjoyed teaching. And I know that a great way to truly learn something is to explain it to others. So I did that when I was learning F# about 9 years ago. I created a website (fsharpforfunandprofit.com) and then started posting on there regularly as I learned about each topic. I'm glad that other people still find it useful!

Matteo: You're the author of a workshop called Domain Functional Programming, organised in collaboration with with Avanscoperta. Why should one join your workshop?

Scott: We cover a lot of ground in 4 half days, so if you're a developer, I think it's a great way to get a head start on learning functional programming and also DDD. Once you see how they go together so nicely, I think it will change the way you think about programming!

Matteo: Tell us something about the workshop we don't see in the description.

Scott: If you ask nicely, I will explain what a monad is. :-)

Matteo: What kind of approach will you be using during your workshop? What's the theory-practice balance? Who's gonna be the domain expert?

Scott: I alternate between doing short presentations to explain things, and then exercises where you practice what I just talked about. And when it comes to domain modeling, I use examples where everyone can be a domain expert.

Matteo: Who's gonna benefit from your workshop the most? What's the target audience?

Scott: The target audience are people who are curious about functional programming but haven't had the chance to work on it. This is a great jump-starter for that.
It's also great for developers who are user-focused and want a better way to capture requirements than UML diagrams. And if you are both a user-focused developer who is also curious about functional programming, then it's perfect for you!

Matteo: What are your workshop's main takeaways?

Scott: That functional programming is fun and very useful and not as scary as some people think.

Matteo: You're a very active writer and contributor, I've been reading your blog for years. How did the idea to write your book "Domain Modeling Made Functional" (watch Marijn Huizendveld present it here) come about?

Scott: I saw a lot of these domain modeling ideas floating around the FP community but no one had put them together in one place and also connected them with the DDD approach. So I was wanting to write a book about this and at around the same time I was approached by Brian McDonald from PragProg press and so it went on from there.

Matteo: What tools do you use in your daily life at work?

Scott: Unlike some developers, I'm not particularly passionate about my tools. My everyday computer has Windows with WSL to do Linux-y things. For an editor, I switch between VS code and Visual Studio, depending on which project I'm working on. Overall, there's nothing special about my setup.

Matteo: What's the perfect soundtrack for your workshop?

Scott: I'm a musician and I love music, but generally I prefer silence when I code. If my workshop had a soundtrack, it would be something happy and non-vocal.

Matteo: Recommend us a hidden gem, a book we don't usually see suggested.

Scott: I love getting ideas from non-programming books. Two that had a big influence on me with respect to user centered design are "The Design of Everyday Things" by Don Norman, which helped me understand why people aren't being stupid when they pull on a door marked "Push", and  "How Buildings Learn" by Stewart Brand, which showed me that all systems and structures evolve in unpredictable ways, and designers should recognize this and support it rather than fighting it.

Cover photo by Shaun Wadham on Unsplash.

Learn with Scott Wlaschin and Matteo Baglini

Scott is the trainer of the Domain Modeling Made Functional Workshop.

Matteo is the trainer of the Applied Functional Programming Workshop.

Check out the full list of our upcoming training courses: Avanscoperta Workshops.

Related topics Functional Programming Domain-Driven Design Domain Model
Matteo Baglini

Software craftsman, technical coach, clean code addicted and co-founder of doubleloop.io

 
Scott Wlaschin

Scott Wlaschin is a developer, architect and author. He is the author of the popular F# website fsharpforfunandprofit.com, and the book Domain Modeling Made Functional, by Pragmatic Bookshelf.

Subscribe to our newsletter

Get exclusive content from experts in software development, technology, business and design.

Subscribe
You may also like
Sep 04, 2026
•
Alberto Brandolini
The sweet taste of AI-assisted indulgence
Domain-Driven Design
Aug 27, 2026
•
Alberto Brandolini
Code is still a side effect
Agentic Software Development
May 29, 2025
•
Alessandra Granaudo
KanDDDinsky and the pre-conference Workshops
Domain-Driven Design
