---
url: "http://blog.pluralsight.com/2012/05/22/solid-code-for-solid-reasons/"
captured_at: "2012-05-24T11:02:19-03:00"
title: "SOLID Code for SOLID Reasons | the pluralsight blog"
domain: "blog-pluralsight-com"
---

# SOLID Code for SOLID Reasons

Posted on [May 22, 2012](http://blog.pluralsight.com/2012/05/22/solid-code-for-solid-reasons/ "10:00 am")by [Jim Cooper](http://blog.pluralsight.com/author/jimcooperps/ "View all posts by Jim Cooper")

We should write good code because good code is easy to maintain, not because it makes the code easier to unit test. However, it just so happens that well written code is easy to unit test; and testing our code, especially test-driving our code, helps us to write good code.  But ease of unit-testing is not the only reason for writing good code, in fact it is one of the very last reasons.

So how do we define good code? I think a great starting point, at least for OO code, are the SOLID principles of object oriented design defined by Bob Martin and the concepts of bounded context and anti-corruption layers defined by Eric Evans.

Wikipedia has a [great overview](http://en.wikipedia.org/wiki/SOLID_(object-oriented_design)) of SOLID, or if you prefer, here it is [from the horses mouth](http://butunclebob.com/ArticleS.UncleBob.PrinciplesOfOod). SOLID is an acronym for the following 5 principles: Single Responsibility Principle, Open/Closed Principle, Liskov Substitution Principle, Interface Segregation Principle, and Dependency Inversion Principle.  If you are not familiar with SOLID, I’d recommend you read that now.

Eric Evans recommends in his book, Domain Driven Design, that we define the various Bounded Contexts that exist in our code.  Typically when we work on a project, we have a code base that we work on most often and then there are the external systems with which our code communicates.  That is an example of bounded context — with our traditional code base being one bounded context and each external system  being considered a separate bounded context.  Evans suggests that when we identify a context boundary we should use anti-corruption layers to prevent the contexts from leaking through to one another.  An anti-corruption layer often takes the form of an adapter that translates and isolates the external context from our code.  This has two very valuable advantages; first, it prevents our code from having to speak the language of the other context (except within the adapter itself); and second, it isolates our code from changes to the other context.  If the other context makes dramatic changes to it’s interface, we have no need to panic because that code is not sprinkled throughout our bounded context, it is isolated to the anti-corruption layer.

With that understanding, I would like to address some questions that come up frequently when doing TDD (test-driven development):

Why do we create small classes and break up complex tasks among multiple objects?  It is NOT because it makes it easier to write isolated unit tests and it is NOT because it solves the “how do I test private methods?” question. We do it because classes who do too much work cause spaghetti-like coupling, and maintaining the large class and all the classes that interact with it, becomes tiresome and error-prone.  **(Single Responsibility, Interface Segregation and Open/Closed Principles)**

Why do we inject dependencies and depend on abstractions (interfaces), rather than concretions (classes)?  It is NOT because it makes our code easier to unit test even though it is nearly impossible to unit test code that depends on concretions.  We depend on abstractions because it makes our code much more loosely coupled and therefore much easier to change without negative consequences. **(Dependency Inversion Principle)**

Why do we wrap third-party dependencies in adapters?  It is NOT because it’s hard to isolate the third-party dependencies from our tests.  We do it because third party dependencies, especially those over which we have little or no control, are subject to change and we want to isolate our code from that change.  We also do it because sometimes those third parties do not believe in the same principles, such as SOLID, that we do, and creating an adapter allows us to adhere to the principles we hold dear. **(Anti-Corruption Layer)**

When we see code that does not adhere to our principles, we need to stop arguing that the reason to change them is for the sake of unit testing — because, frankly, that’s a tough argument to defend.  We first need to understand the reasons why we believe what we do, and “because it makes it unit testable” shouldn’t be a primary reason.  Furthermore, when we believe in a core principle like those above, it should guide everything we do and arguments like “It’s too hard in this case” or “It doesn’t really apply here because I have a simpler way to do it even though it violates my principles” should rarely if ever be valid arguments.  When we find ourselves making arguments like those, and we really think about the reasons why we believe in these principles, we will almost always find that the principle still applies even in complex (or very simple) cases.

The good news is that TDD, done right, helps us to realize when we are violating our own principles.  In my experience when I’ve run into a hard-to-unit-test piece of code, it has always been because of a violation of one of the above principles.  The failure, then, is not a failure of our testing tools, it is our failure to adhere to these good coding principles.

And this is why I so dislike moles as test doubles; and it is my biggest beef with the VS11 testing framework which includes moles (they’re called shims in the VS11 framework).  When you use moles (or shims) in your unit-testing framework, it keeps you from recognizing that you have poorly-written code that does not adhere to principles like those above.

A classic example of how the VS11 testing framework is going to be widely misused can be found in Rich Czyzewski’s blog post, [Noninvasive Unit Testing in ASP.NET MVC4 – A Microsoft Fakes Deep Dive](http://www.richonsoftware.com/post/2012/05/02/Noninvasive-Unit-Testing-in-ASPNET-MVC-A-Microsoft-Fakes-Deep-Dive.aspx).  I understand the temptation to want to solve problems like those Rich discusses using moles and I think his post was very clear and well thought out.  Using moles to test (or test-drive) poorly designed code can be easier (up front) than writing the code correctly, especially when working with legacy code.  But, I fundamentally disagree with his assertion that KISS (keep it simple, stupid) and YAGNI (you ain’t gonna need it) should be used to dismiss such fundamental principles as SOLID and context boundaries.  Even Peter Provost, a Visual Studio program manager lead at Microsoft, disagrees with using shims in this manner as he lays out in [his post on shims](http://www.peterprovost.org/blog/2012/04/25/visual-studio-11-fakes-part-2/).

Our industry is young and evolving.  We need to be sure, as we evolve, that we are basing our evolution on sound principles, not just on what makes our daily jobs less frustrating up-front, especially, when it causes long-term maintainability consequences.  What do you think?

![cd88add445db2a109c4440359c77fd63.jpg](blog-pluralsight-com--solid-code-for-solid-reasons/cd88add445db2a109c4440359c77fd63.jpg)
