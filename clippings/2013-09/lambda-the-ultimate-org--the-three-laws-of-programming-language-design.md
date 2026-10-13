---
url: "http://lambda-the-ultimate.org/node/4754"
captured_at: "2013-09-27T10:22:07-03:00"
title: "The Three Laws of Programming Language Design | Lambda the Ultimate"
domain: "lambda-the-ultimate-org"
---

# **T**he Three Laws of Programming Language Design

Joe Armstrong(of Erlang) while reviewing Elixir(Ruby like language that compiles to Erlang Virtual Machine) states his [Three Laws of Programming Language Design](http://joearms.github.io/2013/05/31/a-week-with-elixir.html) **.**

- What you get right nobody mentions**.**
- What you get wrong, people bitch about**.**
- What is difficult to understand you have to explain to people over and over again**.**

> Some language get some things so right that nobody ever bothers to mention them, they are right, they are beautiful, they are easy to understand**.**
>
> The wrong stuff is a bitch**.** You boobed, but you are forgiven if the good stuff outweighs the bad**.** This is the stuff you want to remove later, but you can’t because of backwards compatibility and some nitwit has written a zillion lines of code using the all the bad stuff**.**
>
> The difficult to understand stuff is a real bummer**.** You have to explain it over and over again until you’re sick, and some people never get it, you have to write hundred of mails and thousands of words explaining over and over again why this stuff means and why it so**.** For a language designer, or author, this is a pain in the bottom**.**

By [bashyal](http://lambda-the-ultimate.org/node/user/5663 "View user profile.")  at 2013-05-31 13:26 | [Critiques](http://lambda-the-ultimate.org/node/taxonomy/term/4)  | [other blogs](http://www.technorati.com/search/lambda-the-ultimate.org/node/4754 "Technorati search of other blogs commenting on this post.")  | 81118 reads

## Comment viewing options

Select your preferred way to display the comments and click "Save settings" to activate your changes**.**

### [I don't like the third law**.**](http://lambda-the-ultimate.org/node/node/4754#comment-75509)

Personally, I think that if you need to explain a feature of a language, you got that feature wrong**.**

The whole point of language design, to me, is that you provide a tool to programmers which is fast and intuitive, and the design space is such that you should be able to make most people happy**.** A language should feel like a comfortable glove**.** A feature which isn't easily adopted contradicts what you're supposed to be doing for the programmer, and should indicate that you should go back to the drawing board**.**

By [marco](http://lambda-the-ultimate.org/node/user/1360 "View user profile.")  at Fri, 2013-05-31 15:19 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [As my law professor taught me in college](http://lambda-the-ultimate.org/node/node/4754#comment-75513)

Sometimes, The Law pulls Society along**.**

Sometimes, Society pulls The Law along**.**

[Something](http://plato.stanford.edu/entries/thomas-kuhn/)  to think about**.**

By [Z-Bo](http://lambda-the-ultimate.org/node/user/5173 "View user profile.")  at Fri, 2013-05-31 17:16 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [But usability-for-beginners and usability-for-experts differ....](http://lambda-the-ultimate.org/node/node/4754#comment-75520)

One of the fundamental observations of usability is that things that are usable for beginners are not necessarily usable for experts, and vice versa**.** For instance, a set of pull-down menus (as in a typical Windows application) may be very usable and intuitive for beginners, but an expert user may quickly find it to be too slow**.** By contrast, things that are initially less intuitive but are powerful and fast may be opaque to a beginner but ideal for an expert**.**

It's the same with programming languages**.** If you're having to explain things over and over again, you're probably explaining them to beginners**.** That doesn't mean that they're not extremely powerful, intuitive, and fast for experts who understand them**.**

Certainly it's nice when everything in a language is easy for new users to understand, but I don't think it's reasonable to expect that every language should avoid features that are easy only for expert users**.**

By [Brooks Moses](http://lambda-the-ultimate.org/node/user/3313 "View user profile.")  at Sat, 2013-06-01 03:51 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Really**?**](http://lambda-the-ultimate.org/node/node/4754#comment-75559)

Just curious: Have you ever had to explain recursion to an undergraduate**?**

By [Pseudonym](http://lambda-the-ultimate.org/node/user/1053 "View user profile.")  at Tue, 2013-06-04 07:20 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Way too late**.** You need to](http://lambda-the-ultimate.org/node/node/4754#comment-75562)

Way too late**.** You need to learn it in kindergarten, elementary school at the latest**.**

By [Ehud Lamm](http://lambda-the-ultimate.org/node/user/1 "View user profile.")  at Tue, 2013-06-04 08:52 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Don't they play tapes of](http://lambda-the-ultimate.org/node/node/4754#comment-75563)

Don't they play tapes of McCarthy explaining recursion to foetuses *in utero***?**

By [Jason Grossman](http://lambda-the-ultimate.org/node/user/7175 "View user profile.")  at Tue, 2013-06-04 09:04 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [They should (if such tapes](http://lambda-the-ultimate.org/node/node/4754#comment-75570)

They should (if such tapes exists)**!** Not sure I ever heard of those tapes before, though**.**

By [Ehud Lamm](http://lambda-the-ultimate.org/node/user/1 "View user profile.")  at Tue, 2013-06-04 20:59 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [fixed point](http://lambda-the-ultimate.org/node/node/4754#comment-75693)

you should go to church to learn about fixed point**.**

By [Gergely Buday](http://lambda-the-ultimate.org/node/user/3197 "View user profile.")  at Thu, 2013-06-20 17:22 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [What about the Monads**?**](http://lambda-the-ultimate.org/node/node/4754#comment-75595)

Doesn't this mean that due to the huge numbers of Monad tutorials and confused beginners that Haskell would have to drop Moands**?** Even though there's totally valid reasoning behind their use**.**

There are a lot of programmers confused about parametric polymorphism and generics as well**.**

By [Daniel Slaney](http://lambda-the-ultimate.org/node/user/2071 "View user profile.")  at Fri, 2013-06-07 10:28 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Parametric polymorphism vs subtyping](http://lambda-the-ultimate.org/node/node/4754#comment-75596)

> There are a lot of programmers confused about parametric polymorphism and generics as well**.**

While true, I find that most of these programmers are mostly confused about *what* they are actually confused about**.** It's not really parametric polymorphism but rather its interaction with subtyping**.** Ultimately, it's subtyping that is making it complicated, not parametric polymorphism as such (which is straightforward on its own)**.** Without bounded quantification, it just isn't as visible how complicated subtyping is, and how intricate the assumptions are in many OO-style abstractions based on it**.**

Or in other words, those who don't understand generics usually just fail to understand the implications of subtyping**.**

By [Andreas Rossberg](http://lambda-the-ultimate.org/node/user/1569 "View user profile.")  at Fri, 2013-06-07 13:36 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [succinct paper/pointer**?**](http://lambda-the-ultimate.org/node/node/4754#comment-75597)

sorry to be dense; it sounds like something everybody in plt knows, but i'm having trouble googling up stuff on it, but i did hit something that to my clueless eyes [claims to have resolved it](http://www.pps.univ-paris-diderot.fr/~gc/papers/icfp11.pdf)  (and maybe the paper even explains it enough for programmers to realize what they are actually confused about, but i'm still struggling**.**)

By [raould](http://lambda-the-ultimate.org/node/user/2292 "View user profile.")  at Fri, 2013-06-07 20:42 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Subtyping and parametric](http://lambda-the-ultimate.org/node/node/4754#comment-75599)

Subtyping and parametric polymorphism are both quite simple on their own, and very complex together**.** If you gave up many of the functions that you are used to using with parametric polymorphism, subtyping is actually quite simple**.** It is definitely intuitive in its natural form, and becomes non intuitive only when combined with non intuitive mathematical type theory**.**

By [Sean McDirmid](http://lambda-the-ultimate.org/node/user/1852 "View user profile.")  at Fri, 2013-06-07 22:05 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Intuitions for subtyping are](http://lambda-the-ultimate.org/node/node/4754#comment-75600)

Intuitions for subtyping are often misleading or fallacious, e.g. with regards to covariance and contravariance when operating on functions, collections, manipulation of structure (the ellipse vs**.** circle question). Intuition is valuable only when it leads in the right direction (i**.**e. 'intuitive' can be good or bad)**.**

Is the idea of 'subtype' really worthwhile**?** We might achieve more precision and reuse (due to less loss of information) focusing on dependent types**.**

By [dmbarbour](http://lambda-the-ultimate.org/node/user/6002 "View user profile.")  at Fri, 2013-06-07 22:52 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Subtyping with regards to](http://lambda-the-ultimate.org/node/node/4754#comment-75601)

Subtyping with regards to covariance and contravariance is not intuitive, but you are again judging subtyping against a system that it is not entirely compatible with**!**

We would do much better to design type systems specifically for type subtyping rather than trying to hammer the concept into pre-existing parametric type systems that weren't designed for subtyping anyways**.** I'll have much more to say on this topic soon (with observations based on my maze of twisty classes work)**.** But in general, we have just explored so little of the type design space to say anything very definitive**.**

By [Sean McDirmid](http://lambda-the-ultimate.org/node/user/1852 "View user profile.")  at Fri, 2013-06-07 23:44 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [I'm judging subtyping](http://lambda-the-ultimate.org/node/node/4754#comment-75602)

I'm judging subtyping against systems with typed collections, functions, or mutable variables**.** I believe subtyping is compatible with these things, just not intuitive in a way that leads to correct conclusions**.** I doubt this is a matter of redesigning the type system**.**

By [dmbarbour](http://lambda-the-ultimate.org/node/user/6002 "View user profile.")  at Sat, 2013-06-08 00:32 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Subtyping is very compatible](http://lambda-the-ultimate.org/node/node/4754#comment-75603)

Subtyping is very compatible and intuitive with respect to typed collections, functions, and especially mutable variables ("a := b" is just "b <: a" after all)**.** I am claiming that subtyping, especially the nominative kind used in OOP, is not very compatible nor very intuitive with Hindley Milner, parametric polymorphism, and other type system features designed SPECIFICALLY for functional programming languages (see Scala)**.** I believe it is completely possible to define a type system that gives you everything that you want (type inference, typed collections, functions, assignment) that is compatible and intuitive with respect nominative subtyping**.**

By [Sean McDirmid](http://lambda-the-ultimate.org/node/user/1852 "View user profile.")  at Sat, 2013-06-08 01:09 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [There is a long history of](http://lambda-the-ultimate.org/node/node/4754#comment-75604)

There is a long history of PL designers messing up subtyping for mutable collections, for functions, and for mutable objects**.** Java and Eiffel come to mind immediately**.**

There is no metric for 'intuitive', but it seems to me that subtyping isn't (even without parametric polymorphism)**.**

By [dmbarbour](http://lambda-the-ultimate.org/node/user/6002 "View user profile.")  at Sat, 2013-06-08 01:27 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Nominative subtyping is an](http://lambda-the-ultimate.org/node/node/4754#comment-75605)

Nominative subtyping is an intrinsic concept in natural language, you can't get more intuitive than that with respect to human beings with language skills**!** On the other hand, many typing concepts that work nicely mathematically (via set theory) are not intuitive by the standard of natural language**.** They must instead be explicitly learned in much the same way that we must learn math while we don't need to explicitly learn how to speak**.**

I agree that we keep messing up subtyping and mutable collections, but you can't prove that something doesn't exist just because it hasn't been found**.**

By [Sean McDirmid](http://lambda-the-ultimate.org/node/user/1852 "View user profile.")  at Sat, 2013-06-08 02:14 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Subtyping in the PL sense is](http://lambda-the-ultimate.org/node/node/4754#comment-75606)

Subtyping in the PL sense is not very close to natural language**.** We may create taxonomies and categories, but they almost always are fuzzy, vague, and overlap in ad-hoc ways**.** Any given object may fit a number of categories, which we judge based on our observations**.** There is no natural notion of safe substitution or type derivation**.**

Rather than subtyping being unintuitive, the intuitions we have for it are misleading**.** This is a sort of 'false' intuition. The impression of intuitiveness may be, as you mention, due to natural language**.**

> you can't prove that something doesn't exist just because it hasn't been found

True enough**.** I'll limit my claims to subtyping as I've observed it thus far**.** Also, I'll note that: what we find 'intuitive' will usually have a common analog in the human's physical or perceptual experience, which probably excludes any non-fuzzy notion of subtyping, and probably favors analytic notions of type (e**.**g. predicate typing, typestate) due to their similarity with perception**.**

By [dmbarbour](http://lambda-the-ultimate.org/node/user/6002 "View user profile.")  at Sat, 2013-06-08 03:00 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [$0**.**02 concurr](http://lambda-the-ultimate.org/node/node/4754#comment-75628)

my (minor) experience in bioinformatics tells me much the same thing about subtyping**.** hierarchical ontologies are often really frankly bull-pucky**.** i've so far seen the confusion around the Liskov substitution principle as proof this**.**

By [raould](http://lambda-the-ultimate.org/node/user/2292 "View user profile.")  at Mon, 2013-06-10 17:42 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Nominal subtyping does not solve anything](http://lambda-the-ultimate.org/node/node/4754#comment-75640)

...because you still need to figure out when defining a nominal subtyping relation actually is semantically valid**.** And that brings you back to square one. Ultimately, you need to understand the semantic implications, you cannot define that away**.**

And if you still think that these semantics are simple than you are fooling yourself**.** Subtyping may look simple if all you have is scalars and products**.** But as soon as you add just one of type recursion, functions, or mutability, I'm pretty sure that 99% percent of programmers will be failed by their intuitions, usually without even noticing**.** (And OO makes very heavy use of all of these**.**)

Parametric polymorphism just forces the hidden complexity into the light, because it requires you to be explicit about it at the abstraction boundary**.**

By [Andreas Rossberg](http://lambda-the-ultimate.org/node/user/1569 "View user profile.")  at Thu, 2013-06-13 15:25 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [I'm doing it**.** Functions and](http://lambda-the-ultimate.org/node/node/4754#comment-75647)

I'm doing it**.** Functions and mutability are not that hard to deal with**.** Not having to worry about principal types is an enormous simplifier**.** Type recursion is quite interesting, and I've made big trade offs concerning precision**.**

The system I'm working on represents a type as a graph of nodes each with a set of required traits and directed links representing what they are assigned to; required traits then propagate to assignees from their assignments**.** I've started writing the post, but it will take me awhile to write**.** Basically, the challenges are:

- Defining type incompatibility for traits**.** Here, we realize that traits that implement the same abstract method are incompatible (e**.**g. int and double implement some method such that one object cannot implement them both)**.**
- Slots, including mutable fields, take on the role of type parameters in my type system**.** Dealing with the slot types as their parent nodes are assigned is quite tricky and requires splitting the nodes into hi/lo versions and involves a few different propagation cases**.** I promise to explain this in more detail later with many examples :)
- Encapsulation is simply graph abstraction: take an original graph and eliminate all nodes that are hidden by a signature (e**.**g. local variables of a method, private fields of a trait); add edges so that connectivity is preserved between visible nodes**.** But this isn't good enough...
- Not for lack of trying, I had to give up on public parametric methods that could see the same private fields of a trait**.** Instead, I model the arguments and return value of a trait's methods as slots (just like fields) of the trait so that method call types are shared according to the method receiver**.** However, top-level procedures that cannot see private trait fields can be parametric, so Map and Filter can still be expressed, at least**.** The arguments and return value of higher order functions like trait methods are treated as slots**.** tl;dr: traits and top-level procedures are parametric, methods within a trait are not parametric beyond the parametricity of their containing trait**.**
- Objects (including constants) that become encapsulated cause any public nodes that they are assigned to be "frozen" so that more required traits cannot be propagated to these nodes without causing an error**.** Such "frozen" nodes will also in turn freeze public nodes they are assigned to when they are hidden**.** In this way, traits will not accidentally propagate to objects that you can't see in your current scope**.**
- For efficiency and decidability reasons, the type system will never manifest a node whose path contains the same slot twice; so "A**.**T.B.T" will point to the same node as "A**.**T" and their assignment relationships will be merged**.** This means all recursive linked structures will share the same type, which isn't such a big deal, but we also can't express lists of lists or dictionaries of dictionaries, which is a very big deal**.** This restriction requires a lot more thought, but I'm going with it for now**.**
- Other features that I think are reasonable but haven't implemented yet: abstract methods (graph connectivity must be preserved), and dynamic type casts (creates a new version of the node to propagate....)**.**
- Various UX issues. How to communicate inferred types and type errors that can be reasoned about locally but involve multiple nodes in different locations**.** How to use partial type information to aid in code completion**.**

Phew! There probably isn't enough context to make much sense of the post, but it was useful for me to write this as I prepare my more complete write up :)

By [Sean McDirmid](http://lambda-the-ultimate.org/node/user/1852 "View user profile.")  at Fri, 2013-06-14 05:30 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [i'm still slow](http://lambda-the-ultimate.org/node/node/4754#comment-75648)

do you mean that when the unenlightened developer writes a parametrically polymorphic function, and then makes use of some field (variable or function or whatever) member of the passed-in-generic-thing, they are effectively doing the same thing as cowboy.draw() vs**.** artist.draw() mistakes from structural subtyping**?**

By [raould](http://lambda-the-ultimate.org/node/user/2292 "View user profile.")  at Fri, 2013-06-14 18:05 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Yea, that's about what it's like**.**](http://lambda-the-ultimate.org/node/node/4754#comment-75655)

When you define an interface, you have to say what essential properties of that interface you are relying on as semantics**.**

For example, if you overload '==' to tell something that isn't an equality relationship (reflexive, symmetric, transitive) or overload '+' with something that doesn't follow the rules of addition (identity element/zero, associative, commutative) then whatever you've got that expects to use the 'mathematics' interface is going to occasionally produce humorous results**.**

Similarly, if you have an interface named 'artist' with a 'draw' function that results in the production of an 'art' value, and you have an interface named 'gangster' with a 'draw' function that comprises preparation to kill another process**.** You mustn't get it confused and think that some object satisfies both of these interfaces just because it has a draw() method**.**

In this particular case simple type checking should sort it out; presumably the gangster::draw() method will not return something that is of type 'art**.**' But even if both are defined returning 'void' it shouldn't be possible to get the interfaces they satisfy mixed up**.** The interface/s a method satisfies ought to be part of its type signature**.** And we would really like it if the fact that it satisfies the requirements of that interface were something that could be statically tested**.**

Unfortunately, there's this little thing called the halting problem, so you can't reliably and automatically check for semantic properties**.** It is possible to write test suites which anything implementing some interface ought to pass, and then have them autorun immediately after compilation as a final typecheck**.** So you could have tests like that be part of your type system**.** Obviously, there's the possibility of bugs in writing the test suite, but well, if you try to rule that out by writing test suites for the test suites, it's turtles all the way down**.**

By [Ray Dillinger](http://lambda-the-ultimate.org/node/user/7251 "View user profile.")  at Sat, 2013-06-15 02:56 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Names are too valuable to be wasted on compilers](http://lambda-the-ultimate.org/node/node/4754#comment-75657)

(tm) J. Edwards

There is no 'draw' function, just function 49908AFA-D14D-433D-8B83-93B296E41698 that is documented to be named 'draw' in some class documented to be named 'Artist', and function 0CAFE6F6-7BFA-40A2-91B8-3BCC94C66890 that is documented to be named 'draw' in some class documented to be named 'Cowboy**.**' Having the compiler decide what 'draw' we mean via some weird rules, especially those that involve "math," is crazy, this is why we have code editors**!**

Or at least that is how it should be**.** I have put a [post out](http://lambda-the-ultimate.org/node/4764)  that explains my type system a bit more, but I'm not finished with it yet**.**

By [Sean McDirmid](http://lambda-the-ultimate.org/node/user/1852 "View user profile.")  at Sat, 2013-06-15 04:55 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Interesting**!**](http://lambda-the-ultimate.org/node/node/4754#comment-75659)

Interesting..**.**

I like the way this makes a lot of type/method boilerplate relatively implicit, incremental, and emergent**.** It's a good approach, I think.

One thing that bothers me about it is that I'm afraid the existence of emergent conflicts might be too subtle for a lot of programmers to sort out in some cases**.** You can help them if you make error messages really specific and explain \*why\* the typechecker infers that something is of a particular type, or of each of two conflicting types**.**

The method implementation, if I understand it correctly, is in your system a link connecting the type and its interface for some graph theory that you use to typecheck**.** You ought to formalize the 'laws' of this particular graph theory, and explain it with node/edge diagrams and examples**.**

So you take the 'connection' and use it to infer that the other methods of that interface, even if not already visible, will be valid on that type**.**

When you declare that something implements a method for a given type that makes it exclusive; It means that no object can be of both that type and of another type that provides an implementation for that method**.** So in your example, something could be both a 'cat' and a 'dog', while the cat has an explicit method implementation, right up until the point that a different method is declared explicitly to implement that method for 'dog'**.** This is reasonable and logical on its face, but it will confuse some because they now get errors not local to the thing they were working on, and the evidence that something is both a 'cat' and a 'dog' in the first place can be hard to follow if it's more than a few steps**.**

By [Ray Dillinger](http://lambda-the-ultimate.org/node/user/7251 "View user profile.")  at Sat, 2013-06-15 09:50 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Copying your comment to this](http://lambda-the-ultimate.org/node/node/4754#comment-75668)

Copying your comment to this [post](http://lambda-the-ultimate.org/node/4764) **.**

By [Sean McDirmid](http://lambda-the-ultimate.org/node/user/1852 "View user profile.")  at Sun, 2013-06-16 02:17 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [No polymorphism**?**](http://lambda-the-ultimate.org/node/node/4754#comment-75607)

But how would you express "my function/method expects an argument that has method/property Foo, and returns this argument" in your system**?** I don't see how one can avoid parametric polymorphism to give a variable name to the argument's type -- but I see how one can avoid subtyping using row polymorphism**.**

By [gasche](http://lambda-the-ultimate.org/node/user/7012 "View user profile.")  at Sat, 2013-06-08 08:09 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [You can**!** Or at least...I](http://lambda-the-ultimate.org/node/node/4754#comment-75609)

You can**!** Or at least...I think you can**.** I'm using assignment/subtype/alias graphs like I talked about in a previous [submission](http://lambda-the-ultimate.org/node/4660)  and finding it can actually work while supporting encapsulation**.**

I'll have more to talk about soon, hopefully**.**

By [Sean McDirmid](http://lambda-the-ultimate.org/node/user/1852 "View user profile.")  at Sat, 2013-06-08 09:31 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Hm](http://lambda-the-ultimate.org/node/node/4754#comment-75610)

(Funny how the automatic cutting of the beginning of your message for the title significantly changes its meaning from "at least I think you can" to "at least I can"**.**)

But in the submission you mention, you have parametric polymorphism, right**?** When you write (trait Dictionary[K,E]), isn't that precisely a form of polymorphism**?**

By [gasche](http://lambda-the-ultimate.org/node/user/7012 "View user profile.")  at Sat, 2013-06-08 11:43 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Ya, I wrote that post awhile](http://lambda-the-ultimate.org/node/node/4754#comment-75611)

Ya, I wrote that post awhile ago**.** The current system I'm working with is annotation free even for interfaces (where you write fake code to establish type relationships instead)**.** So every field is potentially parametric, covariance and contravariance just fall out of graph requirements**.** Its expressive, but I want to have my encapsulation/separate compilation story down before I talk about this too much (e**.**g**.** what happens when you hide a field in a trait and methods assign to and from that field**?**)**.**

By [Sean McDirmid](http://lambda-the-ultimate.org/node/user/1852 "View user profile.")  at Sat, 2013-06-08 12:30 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Subtyping is usually done in error**.**](http://lambda-the-ultimate.org/node/node/4754#comment-75608)

Liskov substitutability is required before something can really be claimed to be a subtype in ways that don't cause problems and confuse other paradigms at scale**.**

I am more a fan of interfaces than inheritance**.** However, even interfaces need checks on invariant properties in order for one to be meaningfully used in place of another**.**

By [Ray Dillinger](http://lambda-the-ultimate.org/node/user/7251 "View user profile.")  at Sat, 2013-06-08 09:10 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Presentation](http://lambda-the-ultimate.org/node/node/4754#comment-75598)

A language is never under any obligation or requirement to drop a concept or feature**.** It doesn't matter that the feature might be confusing or even useless**.**

But it would be wise to learn from the experience with Haskell**.** If I were to develop a language that models sequential operations via monads, I would aim to present them differently - i.e. allowing the concept of 'monad' to be presented in its generic form only after the developer is comfortable with a few concrete examples**.**

I wonder if that separation might require a more general concept of Typeclass, perhaps such that the typeclass requires certain functions be defined, but not locally to a class 'instance' declaration**.**

By [dmbarbour](http://lambda-the-ultimate.org/node/user/6002 "View user profile.")  at Fri, 2013-06-07 20:55 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Meh**.**](http://lambda-the-ultimate.org/node/node/4754#comment-75510)

This seems to or would easily confuse 'right' with 'familiar' and 'wrong' with 'unfamiliar'**.**

By [dmbarbour](http://lambda-the-ultimate.org/node/user/6002 "View user profile.")  at Fri, 2013-05-31 15:23 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [I agree**.** However, the](http://lambda-the-ultimate.org/node/node/4754#comment-75511)

I agree**.** However, the symptom of rule 3 is having to repeat something over and over, while the examples cited as things that Elixir devs will need to repeat over and over include "why do I need a comma here**?**", "why use '<-' instead of '!'?" and "why can't I declare a function directly in the shell**?**". I would call these gotchas; things which everyone must learn to avoid the hard way, but are pretty arbitrary implementation details**.**

I would keep a separate list of those things which will need explaining over and over, but which are crucial features of the language (monads in Haskell, macros in LISP, processes in Erlang, closures in Javascript, etc**.**).

Even though many new users will be constantly asking for explanations of both gotchas and features, the difference is that experienced users will instinctively avoid the gotchas ("I declare my pointers as equal to 0 out of habit") while instinctively head towards the features ("I tend to write functions that act on pure values, since I can get a monad to do the plumbing later")**.**

By [Chris Warburton](http://lambda-the-ultimate.org/node/user/11268 "View user profile.")  at Fri, 2013-05-31 15:59 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [+1](http://lambda-the-ultimate.org/node/node/4754#comment-75512)

you said what i was thinking, thank you**.**

By [raould](http://lambda-the-ultimate.org/node/user/2292 "View user profile.")  at Fri, 2013-05-31 17:06 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [When something is](http://lambda-the-ultimate.org/node/node/4754#comment-75514)

When something is essentially (rather than accidentally) difficult to explain, it's waiting for something better to replace it**.** Its replacement may be incredibly hard to devise, though, so if it's a significant improvement on what preceded it, it's worth using in the meantime**.** And explaining it may help devise its replacement**.**

Monads? I've no doubt they badly need replacing, though with what, [I await enlightenment](http://fexpr.blogspot.com/2011/12/trouble-with-monads.html) **.** Macros? Their replacement is already [visible on the horizon](http://fexpr.blogspot.com/2011/04/fexpr.html) , though likely a lot of things about the replacement will have to be worked out between here and there**.** Another case in point I'm rather fascinated by atm is [guarded continuations](http://fexpr.blogspot.com/2012/01/guarded-continuations.html) , which I deem a profound improvement over the R5RS continuations their design forked from, while again I've no doubt they need replacing with something better**.**

By [John Shutt](http://lambda-the-ultimate.org/node/user/7549 "View user profile.")  at Fri, 2013-05-31 19:28 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Beyond Beyond Monads](http://lambda-the-ultimate.org/node/node/4754#comment-75515)

[The Sequential Semantics of Producer Effect Systems](http://www.cs.cornell.edu/%7Eross/publications/productors/)

> Since Moggi introduced monads for his computational lambda calculus, further generalizations have been designed to formalize increasingly complex computational effects, such as indexed monads followed by layered monads followed by parameterized monads**.** This succession prompted us to determine the most general formalization possible**.** In searching for this formalization we came across many surprises, such as the insufficiencies of arrows, as well as many unexpected insights, such as the importance of considering an effect as a small component of a whole system rather than just an isolated feature**.** In this paper we present our semantic formalization for producer effect systems, which we call a productor, and prove its maximal generality by focusing on only sequential composition of effectful computations, consequently guaranteeing that the existing monadic techniques are specializations of productors**.**

By [chrisoliver](http://lambda-the-ultimate.org/node/user/3591 "View user profile.")  at Fri, 2013-05-31 20:27 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Monads remind me of duck tape](http://lambda-the-ultimate.org/node/node/4754#comment-75516)

Monads, like duck tape, are a great fix for engineering problems. So much, that lots of bad home-grown engineers believe the following saying: If a problem can't be solved by duck tape, then the problem isn't worth solving**.**

(Monads are duck tape in the sense that they glue together pure programs to achieve impure effects**.** At least, in the IO monad case**.**)

By [marco](http://lambda-the-ultimate.org/node/user/1360 "View user profile.")  at Fri, 2013-05-31 21:09 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [It ain't broke, it just lacks duck tape](http://lambda-the-ultimate.org/node/node/4754#comment-75517)

Another gem I found roaming the Intertubes**.** s/duck tape/Monad/g

By [marco](http://lambda-the-ultimate.org/node/user/1360 "View user profile.")  at Fri, 2013-05-31 21:18 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Polymonads:From their](http://lambda-the-ultimate.org/node/node/4754#comment-75518)

[Polymonads:](http://research.microsoft.com/en-us/um/people/nswamy/papers/polymonads.pdf)

> From their semantic origins to their use in structuring effectful computations, monads are now also used as a programming pattern to structure code in a number of important scenarios, including for program veriﬁcation, for information ﬂow tracking, to compute complexity bounds, and for deﬁning precise type-and-effect analyses**.** However, whilst these examples are inspired by monads they are not strictly speaking monadic but rather something more general**.** The ﬁrst contribution of this paper is the deﬁnition of a new categorical structure, the polymonad, which explains these notquite-monadic constructions, and subsumes well-known concepts including monads, layered monads, and systems of monads and monad morphisms, among others**.**

They also discuss Tate's Productors**.**

By [naasking](http://lambda-the-ultimate.org/node/user/2352 "View user profile.")  at Fri, 2013-05-31 21:50 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Do monads have a simple non-math explanation**?**](http://lambda-the-ultimate.org/node/node/4754#comment-75521)

Suppose I'm talking to an expert in assembler, going back to super computer days in the 80's**.** Say his name is Irv**.** Can I explain monads to him without resorting to abstract mathematics**?** I rarely bother to learn technical topics I can't explain to coworkers so they'll understand**.** So far I've been putting monads in that category. Every time I read a description, it's either hand-wavy drivel that doesn't seem to mean anything, or it goes straight into math an average high school student cannot understand**.** So I see no reason to bother.

Arithmetic I liked, up through calculus, but I hate abstract algebra as dry word games and anal quality distinctions**.** If I ever worked with colleagues into monads, I would ask them to explain them**.** But I've never encountered such a coworker**.** I gather folks interested in monads are quite uncommon, and they strike typical practictioners as high falutin**.**

I know for a fact pipes are considered related to monads in some way**.** Can you explain monads using a metaphor that doesn't require using proper definitions in jargon from mathematics**?** If the answer is no, I predict monads will never figure into the way most folks think about programming problems. (While you're welcome to post a link, I won't read another page about monads unless someone can say something here that makes sense in less than a couple hundred words; pages I've seen so far vary little from the two buckets of lightweight nonsense and heavyweight math jargon**.**) Edit: I think you mean duct tape, Marco; what you wrote makes my eyes want to see duck type**.**

By [McCusker](http://lambda-the-ultimate.org/node/user/2390 "View user profile.")  at Sat, 2013-06-01 07:01 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Duct tape](http://lambda-the-ultimate.org/node/node/4754#comment-75522)

Both go according to Wikipedia**.** I guess in Europe, I am Dutch, the misnomer duck tape is more popular since most people don't know what a duct is**.** In the US, duck is probably recognized as incorrect**.** Or maybe duct is the misnomer, the first tapes were made from duck cloth**.** I wouldn't know**.** (I read Wikipedia again. It was duck, after the cloth, became duct, after the air ducts which were often fixed with it**.**)

Let's not go over what a monad is**.** There are many explanations on LtU not everyone agrees upon, which I personal already find troubling**.**

Duct tape isn't even a bad analogy, albeit a bit nondescriptive**.** Hey, if it made it to the moon, it can't be all bad**.**

By [marco](http://lambda-the-ultimate.org/node/user/1360 "View user profile.")  at Sat, 2013-06-01 08:30 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Does this work for a non-mathy explanation**.**](http://lambda-the-ultimate.org/node/node/4754#comment-75523)

Abstract algebra is just object oriented math, where groups and fields are pure abstract base classes**.** Simple and useful in some ways but a ridiculously hard route to go to understand monads**.**

Monads are running code in the pattern a()**.**b().c()**.**d().e().f() ...

Monads have the nickname the programmable semicolon**.**

A monad is constructed of types and nested function calls to ensure one piece of code is executed after another piece of code**.**

In using types and function calls instead of using a built in construct in the language monads can add additional structure/restrictions to what can be sequenced after something else**.**

If you look at the implementation of a monad you will see that the monad type has a parameter that allows monads to wrap other types**.**  
aka mymonad;

If you dig into the implementation details you will find a monad has a method wrap that takes an ordinary value and creates a value of the monad type**.**

mymonad wrap(T value);

In the implementation of a monad you will also find a function unwrap\_and\_call that takes a monad typed value and an ordinary function and calls it**.**

mymonad unwrap\_and\_call(mymonad, T2 (\*func)(T1 value));

And if you look at the usage of a monad without any syntax help you will find the code looks like:

unwrap\_and\_call(unwrap\_and\_call(unwrap\_and\_call(unwrap\_and\_call(wrap(some\_value), f1), f2), f3), f4)

Which is a really long winded way of saying:  
f4(f3(f2(f1(some\_value))))

That allows you to use times to give extra guarantees, and it allows tedious work that you only need to do once to be factored out into the unwrap\_and\_call function**.**

Ultimately monads are pretty boring and the exist only to help automate the boring bits**.**

A complement to the monad that is very handy and does a much better job of guaranteeing sequencing of values are uniqueness types**.** Making a type unique is like making it const. The rule with uniqueness types is that the a parameter or a variable with a uniqueness type must be read exactly once**.**

A peculiarity with monads for guaranteeing sequencing is that in principle a variable with a monad type can be read multiple times and have multiple monadic sequences of function calls descending from it**.** Which unfortunately causes problesm for using monads for I/O or array modification**.**

And that is probably more about monads than you ever wanted to know**.**

By [Eric Biederman](http://lambda-the-ultimate.org/node/user/13691 "View user profile.")  at Sat, 2013-06-01 09:13 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Wrong](http://lambda-the-ultimate.org/node/node/4754#comment-75524)

It is simply not true that monads are just syntactic sugar for function application, as you explain here**.** That is true of the identity monad, as the type of `bind : M(A) -> (A -> M(B)) -> M(B)` specializes to `A -> (A -> B) -> B`, which is exactly the reverse application**.** But that is not true in the general case; it is already wrong for the Option/Maybe monad, for example**.**

(It is true that the pattern suggested by bind is to "evaluate" the first argument (for a effectful notion of evaluation), get a value of type A, and pass it to the function**.** So it is reverse application, but with potentially rich effects in between**.**)

PS: I also don't think your comparison with unique types is fair**.** Monads work fairly well for guaranteeing linear access to a resource, as this is exactly what the IO monad does, or the Writer or State monad**.** And arrays of linear values are also painful to handle in the general case**.**

By [gasche](http://lambda-the-ultimate.org/node/user/7012 "View user profile.")  at Sat, 2013-06-01 09:37 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [I thought his explanation](http://lambda-the-ultimate.org/node/node/4754#comment-75525)

I thought his explanation was pretty good, although you're right that somebody who does not understand monads might interpret that as "monads are just a different way of writing function calls"**.** What he meant is "monads are a way to overload the meaning of function calls"**.** Here's my attempt at a non-mathematical explanation:

It may be a little easier to understand if you say that monads are a way to overload `let` and `return`**.** For instance in F# you have a construct that lets you overload them by providing your own `foo` record:

```
foo {
  let! x = m
  let! y = n
  return x*y
}
```

Here `foo` is a record containing two functions: `foo.Bind(m, f)` and `foo.Return(x)`**.** The compiler replaces the `let!` and `return` inside the `foo { ... }` block with calls to `foo.Bind` and `foo.Return`, so this allows you to overload their meaning**.** It would be more clear if instead of `foo.Bind` we'd have the name `foo.Let` but for historical reasons it's `Bind`**.** Here is what the above example gets translated to:

```
foo.Bind(m, fun x ->
foo.Bind(n, fun x ->
foo.Return(x*y)))
```

This is just like in some languages you can overload the operator `+` by providing your own function for `+`, except instead of `+` we are overloading `let` and `return`**.** When you overload `+` it is advisable that your function satisfies certain laws to avoid confusion for the programmer**.** For instance `(a+b)+c = a+(b+c)`. The same goes for `Bind` and `Return`: to avoid confusion it's advisable that they satisfy certain laws to make sure that their behavior somewhat resembles normal `let` and `return`**.** For instance one of those laws is that

```
foo {
  let! x = m
  return x
}
```

should be the same as just `m`, i.e. if you let and then immediately return the same value, it doesn't do anything**.** In terms of `Bind` and `Return`, that translates into:

```
foo.Bind(m, fun x ->
foo.Return(x))

=

m
```

There are two other laws that it should satisfy (google "monad laws")**.** Such a record `foo` with a pair of functions `foo.Bind` and `foo.Return` is called a monad if it satisfies those laws**.** [To those who know a bit of mathematics you could say that a monad is to let and return as a group is to + and 1]**.**

To really understand it and how it is useful you have to get some practical programming experience with monads**.** It turns out that overloading `let` and `return` is useful for a lot of things: error handling, asynchronous programming, parsing, logic programming (& probabilistic/quantum programming), stateful computations, dynamic scoping, accumulating logs, structuring I/O in pure languages with respectively the Maybe monad, continuation monad, parsec, list monad & more advanced forms, state monad, reader monad, writer monad, and I/O monad**.**

Each of these is a record with a pair of functions `Bind` and `Return` that make that programming task easier**.** Usually those functions are very short. For example for asynchronous programming you can have a record called `async` and its components are:

```
async.Bind(m, f) = m f
async.Return(x) = fun f -> f x
```

Now you may think how could those two functions possibly help us with asynchronous programming**?** That's the thing with monads, in addition to understanding the overarching structure, you also have to understand each monad on its own**.** Just like if you have a couple of functions that overload +, then you have to understand what those functions do and why**.**

By [Jules Jacobs](http://lambda-the-ultimate.org/node/user/2891 "View user profile.")  at Sat, 2013-06-01 12:10 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [still digesting](http://lambda-the-ultimate.org/node/node/4754#comment-75532)

Thanks a lot for this explanation**.** I relate to `let` and `return` operations, and the idea of abstracting them, so mulling this over will likely be fruitful**.**

Especially after Ray Dillinger's reply, and your well-organized presentation, I'm starting to form a mental model that I'm still sorting out**.** Eric's opening was a start, but left me wondering why wrap and unwrap operations occur, and whether sequencing was with respect to time, space, or execution order**.** I was missing the context answering, "What is the problem**?**" But it's starting to look like the idea is a way to manage call trees in a functional language pretending the platform is not actually altering registers and memory during execution**.** If so, then Irv is likely to say he's not having a problem doing that, and wonders why it matters**.**

Irv is not hypothetical: he's one of my coworkers who heard the Elmer Fudd bit**.** I just changed his name. Normal courtesy and discretion involves not describing colleagues and work in public spaces**.** But for purposes of my question, he could just as easily be me, because I learned C++ while debugging it in 68K assembler so I think of it at the assembler level**.** Except I'm comfortable with some higher level abstractions at the same time, which sometimes puzzle my coworkers when they appear in my briefs on how things work**.** My decades of obsessive programming, all the time, were the 80's and 90's**.** Irv and I are members of a 50 something to 60 something cohort where I work, some with pedigrees better than mine**.** (Edit: side story about another coworker Al pruned to to respect privacy, anonymous or not**.**) Irv is great at some things, so makes a good person to imagine telling new ideas**.**

I can write a simulated dialog with Irv where he ends up asking me questions whose answers I admit I don't know, and that would tell you what parts aren't yet clear**.** But I'll avoid doing that until after we're done hearing from others, and I get a chance to clean up my virtual story told to Irv**.** Ray's summary has me thinking I would focus on the idea of reifying a planned computation as a data structure to be executed**.**

I see the relation to async programming, since any way of delaying computation can be used to write a green thread simulation, and abstracting operations like `let` and `return` let you reify activation frames**.**

By [McCusker](http://lambda-the-ultimate.org/node/user/2390 "View user profile.")  at Sat, 2013-06-01 23:58 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [dialog format casual, incomplete summary](http://lambda-the-ultimate.org/node/node/4754#comment-75590)

Please feel free to correct my errors, or supply detail I missed**.** In particular, where any character expresses uncertainty is a good place to fill the gaps**.** To repeat myself, the main idea is to explain monads briefly without reference to jargon from abstract mathematics**.** Neither is Haskell mentioned, except in passing, under a theory monads mean something outside that language**.** The idea is to consider how you implement monads in any language, or even tell what one is**.** Wil is unable to define monads, but has a vague idea what a monad resembles, learned from this LtU thread**.**

Below is an imperfect, partial summary of monads as told to Irv in dialog with Wil**.** Neither understands them. In particular, Wil just reports hearsay and conjecture**.** Coworker Stu sits nearby, working on a laptop and listening, so he can interject remarks**.** Pretend Stu has been telling Irv about Scheme and Smalltalk, and has just a touch of Asperger's syndrome, so he's prone to making jokes with an unfriendly edge to them which Irv and Wil pretend are not offensive**.** (Irv is unfailingly polite, so I need Stu to get rude questions; Stu's a composite and corresponds to no one in particular**.**) We assume everyone present knows enough assembler, C, C++, Scheme, and Smalltalk to freely share references to basic features without definition**.** For example, vtables, interfaces, method tables and dynamic dispatch are considered trivial concepts**.**

>      "What's the word on monads**?**" Irv asked Wil. "Do I care about them?"  
>      "Monads are very cool," Stu blurted, looking up**.** "But you have to use Haskell."  
>      "I don't know the first thing about Haskell," Wil shook his head**.** "Except that it's functional and purity in avoiding side effects is a big deal**.** Monads are part of a scheme to organize computation using immutable values under types amenable to static analysis**.**"  
>      "Specifically, how?" Irv prompted. "And what does the word *monad* mean**?**"  
>      "I have no idea what it means," Wil shrugged**.** "I think it's an arbitrary term chosen to name a feature in Haskell with math associations, to sound like *monoid*, which I also don't understand—nor care about**.**"  
>      "You never studied," Stu quoted from *Ghostbusters***.**  
>      "How do I make a monad, and what are they for**?**" Irv persisted.  
>      "Well," Wil cleared his throat, "they're about manipulating collections of immutable values using functions, in a way promoting composition and letting you optimize after analysis if you want**.**"  
>      "Wow, that's kind of boring," Stu observed, "like a business aiming to 'provide value' as a goal**.** Are monads a collection class framework?"  
>      "Good question," Wil nodded. "Let's try to approach an idea of monads from a similar concept, then later inch closer by constraining our definitions until they obey monad laws, whatever they are**.** What's a synonym for *collection* you usually don't use in programming**?** Pick any noun that contains things**.** Shorter names are better."  
>      "Box?" Irv suggested. "Does the type of container matter**?**"  
>      "Anything that holds a value, or collection of values, or can generate one value or set of them can be called a box," Wil defined**.** "So list, vector, stream, pointer, and function are all things that can hold or generate a value**.** We can present all of them using an abstract box api of some kind**.** Pick a name that means *abstract box interface***.**"  
>      "Easy: ibox," Irv began to sound impatient**.** "Does monad mean ibox**?**"  
>      "Close," Wil squinted in thought. "Except we actually want just the vtable for ibox, and the specific set of virtual methods must be the correct ones matching a monad api**.** And behavior involves returning functions for higher order operations**.** In some places, semantics resembles *map* in Lisp languages like Scheme, except instead of returning the mapped set of values right away, maybe we return a reified function that can perform *map* later**.**"  
>      "I'm trying not to roll my eyes," Irv admitted**.** "Do monads generate a giant AST for later execution, or something**?**"  
>      "Maybe abstract function application tree," Stu suggested**.** "AFAT instead of AST."  
>      "We're reaching *I don't know* territory," Wil warned**.** "I think the interface for monads creates a reified structure representing a computation that can be executed when you evaluate it, but I don't yet see how that occurs from the interface mentioned**.**"  
>      "What's the interface?" Irv asked, getting interested**.**  
>      Wil brought up both hands and acted like he was turning large knobs, which Irv didn't find helpful at all**.** "Picture three abstract methods in the ibox vtable," Wil explained**.** "Each method has something to do with processing values inside a box: *map* is just like the operation in Lisp, *flatten* reduces a box hierarchy to just one shallow box layer, and *asBox* constructs a box given a value**.** Apparently you can give many sorts of box collection that sort of interface and compose elaborate networks of value transformations**.** Some kind of magical takeoff point happens here if you do it right**.**"  
>      "Wait," Irv objected**.** "That isn't enough! Where's all the machinery making things go**?**"  
>      "Don't know," Wil sighed. "Maybe there's a box framework**.** Could be the secret sauce in Haskell: a box composition engine, requiring only collections with an ibox interface**.**"  
>      "You can write infinite lazy lists in Scheme, you know," Stu reminded Wil once again**.**  
>      "Sounds like you're missing a step," Wil suggested**.**  
>      "That wasn't as short as I hoped," Irv noticed**.** "And I don't care yet. Unless you want to write a flexible box composition engine**?**"  
>      "Not especially," Wil evaded. "I want to stream with async pipes, and I want to know when something looks like monads**.** But I still don't know an exact definition."

By [McCusker](http://lambda-the-ultimate.org/node/user/2390 "View user profile.")  at Thu, 2013-06-06 05:05 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Algebra quibble](http://lambda-the-ultimate.org/node/node/4754#comment-75649)

> To those who know a bit of mathematics you could say that a monad is to let and return as a group is to + and 1

As a very minor quibble, you surely meant “to `+` and `0`”, or (perhaps better) “to `•` and `1`”**.** (Or one could make a still subtler analogy and say “as the positive integers (viewed as an examplar of Peano's axioms) are to `+ 1` and `1`” …**.**)

By [L Spice](http://lambda-the-ultimate.org/node/user/6798 "View user profile.")  at Fri, 2013-06-14 18:26 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Yes, + with 0 or \* with 1**.**](http://lambda-the-ultimate.org/node/node/4754#comment-75652)

Yes, + with 0 or \* with 1**.**

By [Jules Jacobs](http://lambda-the-ultimate.org/node/user/2891 "View user profile.")  at Fri, 2013-06-14 22:06 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [I share your annoyance for](http://lambda-the-ultimate.org/node/node/4754#comment-75527)

I share your annoyance for filling nothing from one empty bottle into another one**.** However when it comes to the imagined software engineers in the ancient times of the digital age I'd probably suggest to watch the following [Channel9 show](http://channel9.msdn.com/Series/Beckman-Meijer-Overdrive/Brian-Beckman-and-Erik-Meijer-What-is-a-database-really)  featuring Erik Meijer and Brian Beckman, just for the fun both have with their mouse database and monadic queries**.** It's probably closer in mood and spirit to their own weird ages then it is to ours**.**

By [Kay Schluehr](http://lambda-the-ultimate.org/node/user/2128 "View user profile.")  at Sat, 2013-06-01 16:07 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Container metaphor](http://lambda-the-ultimate.org/node/node/4754#comment-75533)

You can get pretty far with the container metaphor: A *Functor of X* is jargon for something (a data structure) that you know contains an *X***.** In addition, if you have functions which apply to raw *X*'s, it automatically makes them available to be applied in the context of the container (via an operation often called 'map')**.** Typically this corresponds to what you'd think of as a loop over the container, e.g, assuming it contained Integers (pseudo-code)

```
    foreach (x in container) { x + 1 }
```

This would create a new container of the same type, with each contained element incremented by 1**.** Note that this differs slightly from your typical imperative programming language loops, as a new container is produced in the process as the result of the expression**.** From a function on X's we get a function on containers of X's**.**  
The compiler's implementation of the loop syntax delegates to the container, treating the body of the loop as an anonymous function, i.e. the above would be translated to:

```
    container.map(function(x) { x + 1 })
```

Thus each container can provide its own implementation**.**

A *Monad of X* is jargon for something that's a *Functor of X*, i.e. a container, which also allows you to wrap a single *X* in its own container, or to flatten a container of containers of *X* into a single container of *X***.** Typically the latter corresponds to what you'd think of as nested loops:

```
     foreach (x in container1, y in container2) { x + y }
```

for which the compiler would generate something like:

```
     container1.map(function(x) { container2.map(function(y) { x + y } }).flatten()
```

Without *flatten* we'd end up with nested containers**.**  
The specific api can vary, for example, in Scala flatten and map are merged into a single operation called 'flatMap'**.**  
Note that *Monad*'s don't give you any means to get something out of the container (although a specific type of container might)**.** However, if you have a container of X's and also a raw X, and you have a means to wrap the raw X in its own container, then you can operate on it together with those in your container, e.g:

```
   var x1: Integer = ...;
   var container: Container<Integer> = ...;
   foreach (x in toContainer(x1), y in container) { x + y }
```

The combination of *map*, *flatten*, and *toContainer* together with some reasonable "laws" on their use, corresponds to a *Monad* - or as I mentioned some equivalent such as *map*, *flatmap*, *toContainer***.**

In Haskell, these operations are called *fmap*, *>>=* (pronounced "bind"), and *return*, and they are not operations on the container itself, but rather on a singleton 'instance' associated with the type of the container called a "type-class" (which you can think of as a "vtable" for those operations)**.** Instead of the *foreach* syntax, you have *do*:

```
do { x <- container; return x + 1 }
```

The Haskell compiler translates this into calls to the Monad type-class instance of the particular container, which provides the implementation of *fmap*, *>>=*, and *return***.**

You can think of List's as a prototypical example, but as mentioned, there are surprisingly wide variety of data structures that fit this pattern (which is not an accident)**.** For example, you can think of a function that returns an *X* as "containing" its output (reader monad), a pointer to an *X* as "containing" its reference (identity monad), functions that accept callbacks with argument type *X* as "containing" an X that will be handed to the callback - (continuation monad)**.** All of these data structures can be conveniently composed and transformed with *foreach* or *do***.** That this is no accident, is due to the fact that a Monad is a fundamental algebraic structure, namely a *Monoid* of Functors**.** It's the very essence of combining containers.

Although I'd be among the first to agree that traditional Math jargon and notation is often shamefully awful, it's unfortunately the case that one person's obscure jargon is the next person's "familiar terminology"**.** In this post, I've used a bunch of "hacker" jargon, (callback, pointer, data structure, compiler, implementation, vtable, loop etc), and pseudo-code, that is by no means less obscure to "most people" than *Monad***.** I'm not sure if there's a way out of this tower-of-Babel situation, but I've often hoped that [Curry-Howard](http://en.wikipedia.org/wiki/Curry–Howard_correspondence)  will someday have a "column" based on natural language in addition to logic, computation, topology, etc - a "Curry-Howard-[Montague](http://en.wikipedia.org/wiki/Montague_grammar) " if you will - that would provide all of us with a "true" [Rosetta Stone](http://math.ucr.edu/home/baez/rosetta.pdf) **.** And regardless of the jargon, I think the curry-howard correspondence is rightly seen as quite amazing**.**

The container metaphor can be related to the idea of Monad's encapsulating side-effects, if you think of a container of X's as also containing the hidden side-effect internally, and passing it along, in addition to any X's**.**

It doesn't help that most (all?) statically-typed mainstream programming languages are actually incapable of even expressing these api's, since they require higher order generics**.** In Java-like pseudo-code:

```
interface Monad<Container<T>> {
     public <X, Y> Container<Y> map(Container<X> container, Function<X, Y> f);
     public <X> Container<X> flatten(Container<Container<X>> container);
     public <X> Container<X> toContainer(X x);
}

class ListMonad implements Monad<List> {
     public <X, Y> List<Y> map(List<X> container, Function<X, Y> f)
     {
        List<Y> result = new LinkedList<Y>();
        for (X x: container) {
            result.add(f.apply(x))
        }
        return result;
     }
     public <X> List<X> flatten(List<List<X>> container)
     {
        List<X> result = new LinkedList<X>();
        for (List<X> list: container) {
            result.addAll(list);
        }
        return result;
     }
     public <X> List<X> toContainer(X x)
     {
        return Collections.singletonList(x);
     }
}
```

Here the type parameter "Container<T>" itself takes parameters**.** This is inexpressible in Java, C#, and similar. To be fair, LINQ does provide monads based on naming conventions rather than on types to circumvent this limitation**.**

Monads only combine containers of the same type**.** In some cases its possible to combine different types of containers - this is what the papers cited elsewhere in this thread deal with**.**

You can see that algebraically it's possible if there's a "distributive" law which allows you to transpose the containers, i.e. assuming you had containers F, G, to turn G<F<X>> into F<G<X>>**.** Given a nested composite container, F<G<F<G<X>>>, you could first apply the distributive law to get F<F<G<G<X>>> and then use each of F's and G's flatten to get back to F<G<X>>**.**

By [chrisoliver](http://lambda-the-ultimate.org/node/user/3591 "View user profile.")  at Sun, 2013-06-02 00:22 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [has-a container, is-a container, or can-manipulate-a container**?**](http://lambda-the-ultimate.org/node/node/4754#comment-75538)

In the example, `Monad` as abstract base class has no state as expected, but the pseudo code also seems to show no state in subclass `ListMonad`: no class or instance member variables**.** Does that means it's just an interface supplying the operations on `List` where all the state is kept**?** (And is this common to all monads or just this one**?**) Your whole post has me thinking, but this part puzzles me**.**

Edit: I did not say thank you, but I should have; your comments appear more clearly than others in a summary dialog I wrote later**.** (LtU thread structure isn't really suitable for replying to everything anyway, because it would bloat presentation a bit**.**)

By [McCusker](http://lambda-the-ultimate.org/node/user/2390 "View user profile.")  at Sun, 2013-06-02 04:51 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Type Class](http://lambda-the-ultimate.org/node/node/4754#comment-75544)

This is written in the style of Haskell type classes**.** Essentially separating data from the dynamically dispatched interface (which can therefore be a singleton)**.** I.e, in this pseudo-java code you'd also have a single instance:

```
static public final Monad<List> THE_LIST_MONAD = new ListMonad();
```

which would work for all List's**.**

Unlike in Java, in Haskell and Scala the compiler will automatically locate such singleton instances and generate the calls to it on your behalf**.**

By [chrisoliver](http://lambda-the-ultimate.org/node/user/3591 "View user profile.")  at Sun, 2013-06-02 16:16 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [A container monad is not-a-container**.**](http://lambda-the-ultimate.org/node/node/4754#comment-75546)

Remember that the monad is made entirely of function applications**.**

I'm going to drop to a more familiar (ie, non-monadic) representation of function applications to show what's going on**.** When you're not familiar with what the monadic syntax means it just gets in the way of understanding what's going on**.**

Think of it this way:

empty monad has no state**.** ---> ()

Now we add a foo to the end of the list, and we get a new monad:

new monad ---> addtail( foo, ())

now we add a bar to the beginning of the list, and we get a third monad:

third monad ---> addhead(bar(addtail(foo,())))

now we add a baz at the second position in the list, and we get a fourth monad:

fourth monad ---> addpos(baz, 1, (addhead(bar(addtail(foo())))))

then we want to access whatever's now at the third position in the list and we get a fifth monad:

fifth monad ---> fetch(2, addpos(baz,1,(addhead(bar(addtail(foo()))))))

we're not going to know what the actual procedure wrapped as 'fetch' returns until the monad actually runs, so the 'fetch' monad function doesn't have to deal with state at all, and doesn't return a list element; it just returns another monad**.**

The monadic list (like any monad) is just a composition of function calls**.** It isn't working with state at all, and doesn't have to be committed to any particular representation of state**.** Different list representations (different state representations) can be swapped out as easily as choosing a different set of procedures to wrap**.**

This is what wrapping and unwrapping are about as used in monads**.** A conventional 'fetch' procedure that works on some particular list representation and returns a list element, gets 'wrapped' creating a monadic 'fetch' function that works on a monad and returns another monad**.**

I'm using some specific terminology here, which may help you understand it; 'function' vs**.** 'procedure'**.** Procedures deal with state and functions don't.

Later, when the monad is actually being run, the monad that's an argument to the 'fetch' function will have run returning a list**.** Then the monadic 'fetch' function will be 'unwrapped' meaning the original list-based 'fetch' procedure will be retrieved, and then it 'runs' meaning the list-based 'fetch' procedure is actually called, yielding a list element**.**

One application of something like this would be in the use of adaptive containers**.** The monad is a static object, and can be read as a 'plan' of what operations you intend to do to the list**.** An optimizing system could analyze the plan and select a list representation that can execute it efficiently**.** So you could delay 'wrapping' until you have built and analyzed the complete monad**.**

If your analysis tells you you're using only addhead and fetchtail, then a queue representation is the obvious choice**.** On the other hand if you're using addhead and fetchhead (or addtail and fetchtail) then a stack representation is obvious -- and the choice of which monad operation wraps 'pop' and which wraps 'push' depends on whether the monad operations are working with the head or tail of the monadic 'list'**.**

Another possible application is 'delegation without authority:' a pattern in which a process without some access authority submits a query whose result will be forwarded to a process that has the authority to access the results**.** Monads can make such queries marvellously precise or arbitrarily complex beyond the previous abilities of any secure query interface to execute**.**

For example, I may not have the security clearance to find out what the most expensive hammer in the air force budget is, how many of them were purchased, from whom and at what price, where they are now, and which air force officer signed off on the purchase authorization**.** But for some reason I think that a senator in the budget office, who has the right to access that data, ought to know**.** So, presuming there were an interface that supported delegation without authority on behalf of private citizens, I could send a monad across a security boundary to do that complicated query and forward the result to the senator's office, and the monad could run without a security violation**.** I still haven't accessed anything I didn't have the right to access and neither has the senator, but as a result of my "shot in the dark", something possibly relevant has been brought to her attention that she might not otherwise have known**.**

By [Ray Dillinger](http://lambda-the-ultimate.org/node/user/7251 "View user profile.")  at Sun, 2013-06-02 17:02 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Hmm, forgot to mention....](http://lambda-the-ultimate.org/node/node/4754#comment-75547)

In a 'delegation without authority' pattern the 'empty monad' has to wrap some existing representation of state, which also commits all the functions on that monad to wrap procedures compatible with that representation of state**.**

Having the empty monad actually wrap existing state means that a delegation without authority query would be an example of an 'impure monad' and therefore abstract a representation of a transaction on a database, rather than an abstracting the database itself**.**

By [Ray Dillinger](http://lambda-the-ultimate.org/node/user/7251 "View user profile.")  at Sun, 2013-06-02 17:21 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [I don't know.. I wonder if a](http://lambda-the-ultimate.org/node/node/4754#comment-75519)

I don't know.. I wonder if a better syntax for monads wouldn't be possible to reduce the explanation (i don't find Haskell's shortcut for monads very readable)

By [renox](http://lambda-the-ultimate.org/node/user/1458 "View user profile.")  at Fri, 2013-05-31 22:41 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Probably](http://lambda-the-ultimate.org/node/node/4754#comment-75560)

I personally loved monad comprehensions, and I'm sorry that they were removed from H98**.** Arrow calculus also looks pretty good.

By [Pseudonym](http://lambda-the-ultimate.org/node/user/1053 "View user profile.")  at Tue, 2013-06-04 07:44 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [These are rules of](http://lambda-the-ultimate.org/node/node/4754#comment-75526)

These are rules of programming language reception, not design**.**

By [Ehud Lamm](http://lambda-the-ultimate.org/node/user/1 "View user profile.")  at Sat, 2013-06-01 13:52 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Laws of Programming Language Reception](http://lambda-the-ultimate.org/node/node/4754#comment-75529)

Agreed, insofar as these 'laws' are explanatory rather than predictive**.** I think we could do better with cognitive dimensions of notation, studies of learning curves, models of developer progression (i**.**e. start concrete, move towards abstract as needed), etc**.**

By [dmbarbour](http://lambda-the-ultimate.org/node/user/6002 "View user profile.")  at Sat, 2013-06-01 21:37 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [A monad is state represented as nested function calls**.**](http://lambda-the-ultimate.org/node/node/4754#comment-75528)

This is how I'd explain monads to an assembly programmer sans deep mathematical background or terminology**.**

A monad is a way to represent state without doing assignment and mutation and using side effects**.** You apply functions to monads to get a new monad. A monad is actually made entirely of such nested function applications**.** The functions aren't actually run until the whole monad is built**.**

Thus, the entire interaction of a program can be described using this one ridiculously complex function that you built by composing simpler functions**.** When your monad is built, your program which has operated without doing anything mathematically "complicated" with state, is finished; all the actions, or interactions, to be done, including their sequence and dependencies on one another, are described by the monad**.**

At that point, you actually run the monad, according to simple rules**.** This can take input and have side effects on the outside world, and plug actual values into the inputs of the next composed function/s to be evaluated**.** But because none of that stuff was actually going on during your program's run, you've created a static thing using static values, which is much easier to reason mathematically about**.**

Now, explaining \_why\_ it's easier to mathematically reason about is likely to completely escape a 1980's assembly language programmer with no math background**.** He would most likely see the entire exercise as pointless**.**

By [Ray Dillinger](http://lambda-the-ultimate.org/node/user/7251 "View user profile.")  at Sat, 2013-06-01 21:30 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [That's not half bad, as an explanation](http://lambda-the-ultimate.org/node/node/4754#comment-75530)

That's not half bad, as an explanation; could be worth further refinement**.** Though somewhat ominous that a not-half-bad explanation involves the terms "ridiculously complex" and "pointless"**.** ;-)

By [John Shutt](http://lambda-the-ultimate.org/node/user/7549 "View user profile.")  at Sat, 2013-06-01 22:03 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Um, yeah**.** I think I'll plead bias.](http://lambda-the-ultimate.org/node/node/4754#comment-75534)

I admit it; I don't find monad-based programming to be especially virtuous over any other kind of programming**.** I actually do regard fully constructed monads composed of hundreds or thousands of function applications as ridiculously complex functions, in the same quirky-but-within-possibility-for-enthusiasts way that a 64-ounce cup is a ridiculously large drink of coffee**.** I mean, sure, I can believe some people enjoy that; But I personally am not one of them**.** That much coffee would keep me awake long enough to start hallucinating, and I am not on particularly friendly terms with my hallucinations**.**

Clearly I just don't enjoy my hallucinations as much as some other people enjoy theirs**.** After all there's a market for LSD too, which I find completely mystifying**.**

My own first reaction, when I finally penetrated the math-speak, was, "Wait; this is just writing all the stateful parts of the program as single-expression macroexpanders in a functional lisp dialect**.** I can do that, sure, but .... why?!"

On the one hand, it's nice to see some folks outside the Lisp community finally understanding that first-order code is pretty neat and allows you to do some amazing things to leverage the power of your language**.** On the other, monads seem to me like an incredibly narrow and somewhat contrived application of the concept**.**

What they're doing with Haskell, etc, is taking a rather limited, in fact straitjacketed, language that's not intrinsically very expressive, and amplifying its expressiveness with First-Order code in the form of Monads**.** In the same way Lisps, which are otherwise fairly simple languages, have their expressiveness amplified with First-Order code in the form of macros**.**

By [Ray Dillinger](http://lambda-the-ultimate.org/node/user/7251 "View user profile.")  at Sun, 2013-06-02 01:02 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [applications outside statically typed functional languages**?**](http://lambda-the-ultimate.org/node/node/4754#comment-75537)

> He would most likely see the entire exercise as pointless**.**

Does abstraction of generalizing high order operations on containers have useful application in contexts where folks use C and/or assembler**?** I guess I'm asking for intuition. (By which I mean, does *monad* as concept add anything**?**)

Edit: never mind, I think I'm done for now, so I'll check back again in a few days**.** It looks like monads do not have a short explanation, going into definitive detail**.** The sort of explanation you first gave summarizes something of the effect, without a rule letting someone tell whether a given hypothetical example fits**.**

By [McCusker](http://lambda-the-ultimate.org/node/user/2390 "View user profile.")  at Sun, 2013-06-02 04:33 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Except..**.**](http://lambda-the-ultimate.org/node/node/4754#comment-75561)

...that's not what a monad *is***.** It's one thing that it's *used for***.**

This was the hardest thing for me to grasp about monads**.** Monads, fundamentally, are what they are. But they are used for at least three very distinct purposes (possibly more):

1**.** The overloaded semicolon.  
2. A generalisation of list comprehensions.  
3**.** Term algebras with substitution.

The last one you don't see that often, but it's damn useful to know about:

```
data Fact f = P f | N f

instance Functor Fact where
    fmap f (P x) = P (f x)
    fmap f (N x) = N (f x)

instance Monad Fact where
    return x = P x
    P x >>= k = k x
    N x >>= k = case k x of
                    P x' -> N x'
                    N x' -> P x'

data Disj f = Disj { fromDisj :: [f] }

instance Functor Disj where
    fmap f = Disj . fmap f . fromDisj

instance Monad Disj where
    return f = Disj [f]
    m >>= k = Disj . concat . map fromDisj . fromDisj . fmap k $ m

data Conj f = Conj { fromConj :: [f] }

instance Functor Conj where
    fmap f = Conj . fmap f . fromConj

instance Monad Conj where
    return f = Conj [f]
    m >>= k = Conj . concat . map fromConj . fromConj . fmap k $ m

instance MonadPlus Conj where
    mzero = Conj []
    mplus (Conj as) (Conj bs) = Conj (as ++ bs)

cnf :: Conj (Disj f) -> Disj (Conj f)
-- implementation left as an exercise
```

By [Pseudonym](http://lambda-the-ultimate.org/node/user/1053 "View user profile.")  at Tue, 2013-06-04 08:06 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Okay, go on..**.**](http://lambda-the-ultimate.org/node/node/4754#comment-75567)

> ...that's not what a monad is**.** It's one thing that it's used for.
>
> This was the hardest thing for me to grasp about monads**.** Monads, fundamentally, are what they are. But they are used for at least three very distinct purposes (possibly more):
>
> 1**.** The overloaded semicolon.  
> 2. A generalisation of list comprehensions**.**  
> 3. Term algebras with substitution.

Wait, do you have our roles reversed**?** I was the one giving an explanation of what a monad \*is\* -- that is, I claim it's a reification of a set of nested function calls**.** I didn't say a word about what they are used for, except by using a few function calls on something that's probably a list as a concrete example**.** You opened with a sentence that indicated you were going to give a different idea of what monads *are*, but then you went on to just say a few of the things they are *used for***.**

What do you claim a monad actually is**?**

I have seen the line about the "overloaded semicolon" more than once**.** But a semicolon, by itself, never had semantics at all in my universe, so those words have never made sense to me**.** The most common use of the semicolon is just something that some languages require to be stuck in particular places because their syntax is otherwise deficient or ambiguous and they can't disambiguate things at those places without it**.** I think of its presence as an aid to parsing, nothing more**.** But if the line about "overloading" makes sense to you, then clearly you have some semantics for a semicolon in mind, with and without monads**.** So I can ask you this question, which I've been wanting to ask someone for a while now**.** What are they? In all seriousness, the "overloaded semicolon" cryptich has been driving me nuts**.** Help me solve the puzzle!

I'm agreeing with you that the other things you mentioned are among the many possible applications of monads, but I don't see any way that invalidates the idea that monads are made of nested function calls**.** Do you?

By [Ray Dillinger](http://lambda-the-ultimate.org/node/user/7251 "View user profile.")  at Tue, 2013-06-04 17:09 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [laws of reaction](http://lambda-the-ultimate.org/node/node/4754#comment-75531)

I like the way Joe writes, and his Elixir advice is admirably good-spirited**.** I wish a cooperative, well-meaning attitude was more common in the tech industry**.** Joe's point about version numbers is very useful, and helps manage chaos resulting from evolution in code and data schemes**.** Many folks prefer to optimistically pretend chaos going forward is unlikely**.**

(This post mainly aims to make up for any thread hijacking related to monads which I thought was off-topic, and obfuscating in a really subtle way, but made a good excuse to ask whether anyone can explain them simply**.**)

> What you get right nobody mentions**.**

That sounds right, especially when it's about framing**.** The way ideas get framed seems invisible to most people, the way we say fish might ignore water**.** (Who knows how fish actually think?) I don't have a good model to explain this absence of meta structure in how folks think**.** It may just be hard to talk about; resistance to framing discussions can be really strong, though, so it plays out like aversion or blindness**.**

> What you get wrong, people bitch about**.**

The fish-in-water metaphor goes like this: "The pool just dried up, and I only have gills, buddy**!**" Pain points have high visibility**.** Contrast and loss seem amplified more by the human brain than other things**.** (Then if we put on a cynic's hat, sometimes folks bitch to get their way, as simple manipulation**.** I think a lot of tech folks with an honest disposition miss this angle sometimes: that others can crassly pursue personal agenda, sounding like, "Make it better, Mr. Wizard**.**")

> What is difficult to understand you have to explain to people over and over again**.**

Yes, that's the chin-rubbing part**.** My suggestion here is two-fold: spend time on careful framing for hard parts, then put those explanations in a standard place where they go right with other parts of the system described**.** Then you can say, "Using feature X and don't understand**?** Did you read the FAQ for X stored right next to the X code and docs**?**" A curation aspect is involved since useful explanations might otherwise drown in a sea of distracting messages**.**

Note this is one reason I think it's a good idea to write a short explanation of something before you code it**.** When it's just you, choosing between version A and version B of code might seem arbitrary**.** But version A might be awful to explain, while version B is simple**.** Brevity of explanation is a good coarse heuristic**.** You don't want lots of implicit gotchas**.**

By [McCusker](http://lambda-the-ultimate.org/node/user/2390 "View user profile.")  at Sat, 2013-06-01 22:21 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [I didn't like the examples](http://lambda-the-ultimate.org/node/node/4754#comment-75535)

I didn't like the examples posted about right/wrong/confusing**.**

Functions I will grant**.** More than anything else in the whole list, if you get lexical binding wrong, then it's really hard to explain, and people will be confused all the time**.** If you get it right, then it won't even get talked about**.**

Defmacro and quasiquote I will also grant**.** If you do it right, nobody notices it**.** Do it wrong, and there will be some really long threads on your language's mailing list**.**

Joe should have stopped there**.** The rest of the list I am not even sure is obviously the best way to do things**.**

XML headers are awful if you've ever had to work with them**.** To be brief, they don't tell you useful things like whether the file expects XML includes to work**.** No, they tell you "1**.**0", and they tell you a DTD that you should probably ignore**.** Mapping this to programming languages, it does not get better**.** Again, to be brief, (a) developers usually use a pretty recent compiler, and (b) you need a solution to library versions, and whatever you do for library versions will subsume your problem with compiler versions**.**

REPLs should take their own blame, rather than pinning it on the language**.** Yes, better languages make it easier to write a REPL**.** Really, though, the REPL should bend over backwards to be intuitive**.** If you can't write a basic function definition in the Erlang REPL, then fix the REPL**!****!** Kluge it whatever way will do the trick. The Scala REPL includes regexp rewrites of stdout so that it appears to be doing what people expect**.** It's gross, but you can't lecture your users about the difference between an expression and a form**.** The Scala REPL does a pre-parse to guess what they wrote and then compiles it in the appropriate way**.**

The right-arrow operator in Elixir is cute, but I don't think it looks better than a sequence of variables and initializers that is shown as an alternative**.** It also looks prone to failing as your definition grows longer**.** Your cute sequence of right-arrows is going to look pretty bad if any of the intermediate forms itself becomes multi-line, or worse, needs its own internal right arrows**.**

Bang versus left arrow are equally obscure, at least for me**.** I guess things are different if you are marketing for Erlang programmers**!**

Whitespace? I think it's better to be less flexible. I used to say the opposite, and then I programmed on some larger software teams. The whitespace that sticks out should be backspaced down**.**

By [lexspoon](http://lambda-the-ultimate.org/node/user/3293 "View user profile.")  at Sun, 2013-06-02 01:10 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Versioned data - win or lose, depending**.**](http://lambda-the-ultimate.org/node/node/4754#comment-75536)

> XML headers are awful if you've ever had to work with them**.** To be brief, they don't tell you useful things like whether the file expects XML includes to work**.** No, they tell you "1**.**0", and they tell you a DTD that you should probably ignore**.**

To be fair, XML version numbers were a particularly bad choice for demonstrating the value of version numbers, because XML versions as found in the wild are perpetrated by different people than the ones who produce the standard, by people who don't have the authority to bump the version number when they change something, by people who are not developing products on exactly the same schedule as the release of new version numbers, and by people who are in fact producing incompatible changes from each other**.**

Every browser, and every version of every browser, ought to have its own HTML DTD, because there are differences in how every**.** damn**.** one of them processes HTML. Web developers look at the DTD version number and laugh, because they have to simultaneously satisfy four to a dozen sets of quirks and exceptions each of which ought to have spawned its own DTD**.** And yet, if you put anything other than the complete lie of a single version number in the header, it won't mean anything because the standards committee hasn't, and can't, assign any meaning to anything else**.**

By contrast, versioned data when developed by a single source is a huge win**.** Because a single source controls the both the implementation and the version number, they can bump the version number whenever they change something and therefore it has an unambiguous meaning**.**

By [Ray Dillinger](http://lambda-the-ultimate.org/node/user/7251 "View user profile.")  at Sun, 2013-06-02 02:03 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Monads are explained a lot](http://lambda-the-ultimate.org/node/node/4754#comment-75539)

Monads are explained a lot not because they are hard to understand, but because they are fun to explain and explaining them makes the explainer feel smart**.**

By [Ehud Lamm](http://lambda-the-ultimate.org/node/user/1 "View user profile.")  at Sun, 2013-06-02 14:14 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [A statement like that should](http://lambda-the-ultimate.org/node/node/4754#comment-75540)

A statement like that should have a Devil's Advocate**.** Here's an alternative: monads are explained a lot because some people swoon over them while others see them as a poor-to-horrid idea, so that both groups feel that one or the other group must not really understand them**.** To do the Devil's Advocate thing properly, I'll also suggest that *both* groups are failing to understand monads — rather like quantum mechanics, of which iirc Richard Feynman observed, anyone who thinks they understand it, doesn't**.**

By [John Shutt](http://lambda-the-ultimate.org/node/user/7549 "View user profile.")  at Sun, 2013-06-02 15:03 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Another: Simple and Abstract](http://lambda-the-ultimate.org/node/node/4754#comment-75542)

Monads are hard to explain because they're simple and abstract**.** Humans have an easier time grasping things that have concrete features**.** The notion that 'simple' implies 'easy to understand' is an epic fallacy**.**

By [dmbarbour](http://lambda-the-ultimate.org/node/user/6002 "View user profile.")  at Sun, 2013-06-02 15:27 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Monads are hard to](http://lambda-the-ultimate.org/node/node/4754#comment-75543)

*Monads are hard to explain..**.***

And here I thought that they were hard to *understand***.**

By [Ehud Lamm](http://lambda-the-ultimate.org/node/user/1 "View user profile.")  at Sun, 2013-06-02 15:47 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Those go hand in hand**.**](http://lambda-the-ultimate.org/node/node/4754#comment-75545)

Those go hand in hand**.** Explanations are for humans, after all. If something is easy to comprehend, it rarely requires much explanation**.** If something is difficult to understand, our explanations become a little desperate**.** (E**.**g. explaining monads in terms of burritos.)

By [dmbarbour](http://lambda-the-ultimate.org/node/user/6002 "View user profile.")  at Sun, 2013-06-02 16:22 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [I think you got me there**.**](http://lambda-the-ultimate.org/node/node/4754#comment-75554)

I think you got me there**.** Though this is not entirely true, it is a good point**.**

By [Ehud Lamm](http://lambda-the-ultimate.org/node/user/1 "View user profile.")  at Mon, 2013-06-03 16:13 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [My initial reaction was: why](http://lambda-the-ultimate.org/node/node/4754#comment-75551)

My initial reaction was: why this bunch of random type signatures, bundled together and not another one**?** Then a diversity of examples, beginning with the Maybe monad, were exercised which was somehow missing the point for me**.** I wanted contingency to be eliminated, an abstract form being derived by canceling out others or constructed from something even more primitive, say function composition - not stated like an axiom**.** It is somewhat scary that programmers could state axioms like this of small or arbitrarily large complexity, which come from nowhere and are finally justified by plumbing**.**

Not nowhere. When people asked where monads came from they were delegated to category theory which works basically the same: build an algebraic structure, show a universal property by drawing a commutative diagram, give lots of heterogeneous examples**.** Very frustrating and not exactly what math seems *needed* for**.**

By [Kay Schluehr](http://lambda-the-ultimate.org/node/user/2128 "View user profile.")  at Mon, 2013-06-03 03:27 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Concrete abstract](http://lambda-the-ultimate.org/node/node/4754#comment-75548)

Monads are being used concretely, so we legitimately need to understand then concretely**.** Something that is simple as an abstract concept is not necessarily simple in concrete application**.**

By [John Shutt](http://lambda-the-ultimate.org/node/user/7549 "View user profile.")  at Sun, 2013-06-02 17:55 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Concrete usage](http://lambda-the-ultimate.org/node/node/4754#comment-75549)

It's relatively easy to teach people to *use* concrete monads, e.g. the IO monad or a Canvas drawing monad, so long as you don't distract with the word 'monad' or trying to explain what one is first**.** The abstraction can come later, conceptual refactoring after the person has experience with several concrete monads**.**

I think that's how it should be done**.** And not just for monads; also for rings, groups, algebras, categories, etc.. Unfortunately, some languages effectively force developers to learn about monads, to learn the word 'monad', before using the concrete instances, e.g. via `import Control.Monad`**.** This runs backwards to the normal human learning process, and intimidates potential developers**.**

Do we have a good way to support the progession of developers from 'concrete' to 'abstract'**?** It seems easy for a new project, but what about the latecomers to an old project**?** Can we provide a concrete view of code for them, that fits their level of comprehension**?**

Those are questions that interest me, though I lack solid answers**.**

By [dmbarbour](http://lambda-the-ultimate.org/node/user/6002 "View user profile.")  at Sun, 2013-06-02 19:45 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [People think differently**.**](http://lambda-the-ultimate.org/node/node/4754#comment-75552)

People think differently**.** (I've been thinking of writing a blog post on this; it's more profoundly true than commonly appreciated**.**) I remember a highschool math teacher not wanting to give me a concrete example of an abstract structure, feeling students may latch on to the concrete and fail to apprehend the abstract — but I suspect that's a trend amongst people for whom the abstract just doesn't come naturally anyway**.** There are I suspect some people to whom the concrete doesn't come naturally**.** People like me want to see the abstract definition, motivate it with a concrete example, and then move outward; we're in no danger of getting stuck on the example, but we generally need it to begin illuminating the abstract definition**.**

By [John Shutt](http://lambda-the-ultimate.org/node/user/7549 "View user profile.")  at Mon, 2013-06-03 16:09 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [People like me..**.** You mean](http://lambda-the-ultimate.org/node/node/4754#comment-75553)

*People like me..**.***

You mean smart people? (joking, joking)

By [Ehud Lamm](http://lambda-the-ultimate.org/node/user/1 "View user profile.")  at Mon, 2013-06-03 16:11 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Everyone is crazy except](http://lambda-the-ultimate.org/node/node/4754#comment-75556)

Everyone is crazy except me and thee**.** And sometimes I wonder about thee.

By [John Shutt](http://lambda-the-ultimate.org/node/user/7549 "View user profile.")  at Mon, 2013-06-03 19:05 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [People think and learn similarly](http://lambda-the-ultimate.org/node/node/4754#comment-75555)

Barring abnormalities or syndromes, people learn from similar experiences and have very similar progressions**.** This is why schooling works, and why we can fill the gaps in natural language so easily**.** I think your 'profound truth' is about as true as 'people grow differently' or 'people have different numbers of fingers'**.** People think and learn by the same psychological and biological processes, even though they have different experiences, talents, and skills**.**

Your highschool math teacher probably started concrete like everyone else, then predictably forgot about it (like so many mathematicians do)**.** I've seen this happen many times, to several grad students come part-time professors, even to myself (which I can track only due to reviews of my notes) - as I become comfortable and experienced with a particular class of abstractions, the concrete becomes difficult to remember and diminishes in value**.** I've even had the same fears, of people latching onto one concrete example**.** (But those fears aren't well justified - we can provide multiple examples, ask test questions over multiple examples, etc.. The difficult part is thinking of the concrete examples**.**)

There are very few people like you with respect to having studied 'abstraction' for its own sake for two decades**.** But I expect, if you kept your notes from way back and review their progression, even you'd find you and your concepts of abstraction grew through the concrete**.** Given enough different examples of abstraction, even those examples become concrete objects for higher layers of abstraction - e.g. category theory, topology**.**

By [dmbarbour](http://lambda-the-ultimate.org/node/user/6002 "View user profile.")  at Mon, 2013-06-03 17:05 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [I'm peripherally aware](http://lambda-the-ultimate.org/node/node/4754#comment-75557)

I'm peripherally aware there's a lot of literature about different learning styles, but I'm more interested in differences in the way people think**.** From research I was somewhat involved in as an undergraduate, key to cognitive style is *compensatory strategy* — how one uses what one's mind is good at to compensate for what it isn't**.** (I suggest that Leonhard Euler was good at something that Albert Einstein was not good at — I don't think either was "smarter", but no way would Al have come up with the stuff Leo did, nor vice versa**.**)

By [John Shutt](http://lambda-the-ultimate.org/node/user/7549 "View user profile.")  at Mon, 2013-06-03 19:18 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Schooling only works up to a](http://lambda-the-ultimate.org/node/node/4754#comment-75558)

Schooling only works up to a point, and mostly as a means of instilling social conformance and restricting divergent evolution of viewpoints, learning strategies, and experiences**.** Rather, it is \_because\_ people think, learn, and work differently (and at different speeds) that schooling is necessary**.**

By [Ben L. Titzer](http://lambda-the-ultimate.org/node/user/3395 "View user profile.")  at Tue, 2013-06-04 07:07 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [What vs**.** How](http://lambda-the-ultimate.org/node/node/4754#comment-75564)

"People think differently" is ambiguous as to whether it speaks of mechanism or opinion, but I'm interpreting it as mechanism**.** The answer to 'how do people walk' is universal, modulo severe injury or abnormal conditions**.** And similar seems to be true for 'how do people think' or 'how do people learn'**.**

The questions of 'how fast do people walk' or 'what paths do people walk' or 'what styles and skills for walking do people learn' (e**.**g. various trained forms of walking emphasize stealth, speed, stability, stamina, or aesthetic concerns) have very different answers, and more variation among people**.** And again, similar seems true for the analogous questions for learning or thinking**.** If you speak of strategies, heuristics, viewpoints, style - i.e. tools of thought and learning that are themselves learned - then you're not directly speaking of mechanism, of how people think or learn**.**

When I spoke above of 'why schooling works', I wasn't speaking of the subject matter, but rather of the similar mechanisms for learning**.** Schooling would not be economical if the processes of learning and thought were highly divergent**.**

Regarding your statement that schooling is necessary because people think, learn, and work differently - I think otherwise**.** Consider: even a clone army would benefit from schooling, and would perhaps do so more effectively than a class of heterogenous students**.** Schooling is more about economies of scale for education (i**.**e. relative to tutoring or apprenticeship)**.**

By [dmbarbour](http://lambda-the-ultimate.org/node/user/6002 "View user profile.")  at Tue, 2013-06-04 09:06 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [For the sake of clarity,](http://lambda-the-ultimate.org/node/node/4754#comment-75565)

For the sake of clarity, when I said "people think differently" I was indeed referring to mechanism**.** And before that research I was involved with years ago, I too would have said people's manners of thinking were rather like ways of walking, all basically the same except for a few pathological cases**.** But after seeing the research, I'd say the actual mechanisms are remarkably different (indeed, different enough that I see no way to save the walking analogy — it's considerably worse than the [Ministry of Silly Walks](https://en.wikipedia.org/wiki/Ministry_of_Silly_Walks) )**.**

By [John Shutt](http://lambda-the-ultimate.org/node/user/7549 "View user profile.")  at Tue, 2013-06-04 11:44 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Well, maybe the analogy](http://lambda-the-ultimate.org/node/node/4754#comment-75566)

Well, maybe the analogy is somewhat salvageable**.** One could say some people walk on two legs, some on more than two, some hop, fly, or swim**.**

> all creatures living beneath the sun  
> that creep or swim or fly or run  
>     — [The Pied Piper of Hamelin](https://en.wikisource.org/wiki/The_Pied_Piper_of_Hamelin_%28Browning%29) , Robert Browning

By [John Shutt](http://lambda-the-ultimate.org/node/user/7549 "View user profile.")  at Tue, 2013-06-04 12:05 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [All people walk by placing](http://lambda-the-ultimate.org/node/node/4754#comment-75568)

All people (humans) walk by placing one foot in front of the other under the ministrations of gravity**.** Mannerism is not mechanism. Swimming or flying are not even styles or mannerisms of walking**.** Walking on more than two legs is not possible for humans barring extreme abnormality (unless you're very generous in the interpretation of 'leg')**.**

Perhaps a better analogy for you would be: 'how do people fight' - I imagine you would answer with something like 'some with guns, some with swords, some with fists, some with words', thereby distinguishing 'what tools do people choose when fighting' yet failing to answer the original question (for which I do not have a proper answer)**.**

People have common sensory organs, common brains structures, common nervous systems, common mechanisms for learning and thinking**.** I grant they have different *styles or mannerisms* for thinking, which may be more or less effective for various purposes**.** But every style, whether it be rational, effective, or otherwise, is achieved within the same mechanisms. Styles of thinking can be learned and taught and subject to talent like any skill**.**

By [dmbarbour](http://lambda-the-ultimate.org/node/user/6002 "View user profile.")  at Tue, 2013-06-04 17:18 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Swimming or flying are not](http://lambda-the-ultimate.org/node/node/4754#comment-75569)

> Swimming or flying are not even styles or mannerisms of walking**.**

Exactly.

> Styles of thinking can be learned and taught

What made this research really interesting was that, no, the modes of thinking studied can't be taught to someone whose mind doesn't work that way**.** (If we're each clear on what the other is claiming, it's likely we won't do any better in this venue**.**)

By [John Shutt](http://lambda-the-ultimate.org/node/user/7549 "View user profile.")  at Tue, 2013-06-04 20:52 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [the modes of thinking](http://lambda-the-ultimate.org/node/node/4754#comment-75571)

> the modes of thinking studied can't be taught to someone whose mind doesn't work that way

How would you even begin to prove this negative hypothesis scientifically**?** What metrics are involved to determine "mind doesn't work that way"**?** Can you point me at this allegedly convincing research**?**

What I do know: people can be taught many modes and strategies for thinking, and even to switch between them**.** They're all constructed upon common biological mechanisms and substrate**.** AFAICT, it isn't a matter of "mind doesn't work that way" unless we speak of designed systems of thought (like math or logic) were no human's mind works that way**.** There certainly are issues of varying comfort and familiarity with different approaches, interference based on learning history, attitude, and maturity, and vast differences in motivation and opportunity to learn**.** I'm more inclined to believe people "won't" (or cannot be bothered to) learn certain modes of thinking than "can't"**.**

By [dmbarbour](http://lambda-the-ultimate.org/node/user/6002 "View user profile.")  at Tue, 2013-06-04 21:18 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Consider how one would prove](http://lambda-the-ultimate.org/node/node/4754#comment-75573)

Consider how one would prove it's possible to teach people "many modes and strategies for thinking"**.** Are these things, that can be taught, essentially procedural in nature**?** The stuff I'm talking about is not visibly procedural**.** For example, some programmers are *much* better than others at debugging; to appearances, they just sort of have a magic nose for asking the right question**.** You can teach procedures for debugging, and perhaps these may improve a given programmer's efficacy at debugging, but if the programmer doesn't have a magic nose, these procedures won't give them one**.**

By [John Shutt](http://lambda-the-ultimate.org/node/user/7549 "View user profile.")  at Wed, 2013-06-05 01:32 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Most things that can be](http://lambda-the-ultimate.org/node/node/4754#comment-75574)

Most things that can be taught aren't procedural in nature**.** What is procedural about chess**?** soccer? politics? It isn't even clear to me why you ask that question**.** Most teaching is by examples, experiences, tests, and a few piecewise skills**.** Modes of thinking are taught by the same means.

"magic nose"**?** You seem to have some superstitious beliefs about learning and use of knowledge**.**

Most developers aren't taught debugging, they're left to figure it out on their own**.** I expect many people who are ineffective at debugging are so primarily because they'd rather be doing something else, not because they *can't* learn to be very effective at debugging**.**

By [dmbarbour](http://lambda-the-ultimate.org/node/user/6002 "View user profile.")  at Wed, 2013-06-05 02:23 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Examples are procedural**.**](http://lambda-the-ultimate.org/node/node/4754#comment-75575)

Examples are procedural**.** Not everyone can learn, *or* be taught, to be a chess master**.**

Ironically, your apparent failure to understand why I asked that question indicates *that we think differently***.**

By [John Shutt](http://lambda-the-ultimate.org/node/user/7549 "View user profile.")  at Wed, 2013-06-05 03:13 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Examples are procedural**.**In](http://lambda-the-ultimate.org/node/node/4754#comment-75576)

> Examples are procedural**.**

In general they aren't**.** I wonder what makes you think otherwise. The process of reviewing examples might be procedural, but the examples themselves need not be**.** Examples can be situations, case studies, relationship graphs, datasets**.** What is procedural about such things?

> Not everyone can learn, or be taught, to be a chess master**.**

Not everyone can become a competitive weightlifter, but all people lift weights by the same mechanisms. Not everyone can become a competitive runner, but everyone runs by the same mechanisms. How is this claim about 'chessmaster' different**?** Is there something mystical about the brain that distinguishes it**?** Or the nose?

> your apparent failure to understand why I asked that question indicates that we think differently

We have different knowledge, different experiences, different skills, different viewpoints, priorities, and motivations**.** Our opinions, conclusions, and understandings will be different**.** You can't justifiably attribute my "apparent failure to understand" to different mechanism of thought, not when there are much simpler explanations**.** Is this the same level of justification you accepted for the research you mentioned**?**

By [dmbarbour](http://lambda-the-ultimate.org/node/user/6002 "View user profile.")  at Wed, 2013-06-05 03:31 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [You are reasoning by analogy](http://lambda-the-ultimate.org/node/node/4754#comment-75577)

You are reasoning by analogy to physical mechanics of human motion, and there is nothing to suggest such analogies transfer to thought processes**.** Moreover, no one can even enumerate or model thought processes in humans to any degree of completeness or fidelity, so how can you so confidently assert that they are all identical**?** That's not sound reasoning.

On the other hand, to reason by way of your own analogies, there is nothing to suggest that humans are all going to lift weights the same way**.** Seriously. The task of moving a weight from the floor to a shelf--for example--could be accomplished by dozens of different human motions, depending on the size and mass of the object(s) to be moved**.** To say nothing of using an assistive tool like a crane, inclined plane, hoist, lever, stairs, etc**.**

I believe the burden of proof is firmly on your side**.** You are going to suggest that all humans will choose to do a deadlift versus a clean-and-jerk, or a squat**?** You are suggesting that all humans use the same same thought processes**.** So prove it.

> > your apparent failure to understand why I asked that question indicates that we think differently
>
> We have different knowledge, different experiences, different skills, different viewpoints, priorities, and motivations**.** Our opinions, conclusions, and understandings will be different**.** You can't justifiably attribute my "apparent failure to understand" to different mechanism of thought

Sure he can**.** Are you suggesting that the chemistry of our brain gives rise to only one kind of consciousness, one kind of software**?** That's like positing that x86 can only run C programs. If there is a level jump from microchemistry to consciousness, and I believe there is, and the microchemistry is a kind of universal machine, then there is no reason to believe that it can't run another kind of software--which is, I think, what John is talking about**.** The microchemistry, the neurology, is the only kind of thing that we can physically inspect and say is pretty much the same across all humans**.** The software, we simply have not decoded yet**.** It would be extremely premature to pronounce it equivalent for all humans**.**

Again, the burden of proof is on you**.**

By [Ben L. Titzer](http://lambda-the-ultimate.org/node/user/3395 "View user profile.")  at Wed, 2013-06-05 11:41 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [admiration](http://lambda-the-ultimate.org/node/node/4754#comment-75579)

Ohh**.** I like your reply *much* better than mine**.**

By [John Shutt](http://lambda-the-ultimate.org/node/user/7549 "View user profile.")  at Wed, 2013-06-05 13:16 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Meh**.**](http://lambda-the-ultimate.org/node/node/4754#comment-75581)

You seem to be stretching everything I say to the point of absurdity**.** Get back to me when "competitive weightlifting" involves *"using an assistive tool like a crane"*, will you**?** I've already explained what I mean by 'mechanism', and it certainly isn't the choice of movements (not that you have much choice in competitive weightlifting)**.**

Thinking by common mechanisms doesn't mean having the same 'software', and this is clear enough from what you quoted (e**.**g**.** I mention having different skills). Further, even if we had the same 'software', it would not imply reaching equivalent decisions (since there are other, individualized inputs to the decision making - e.g. orientation, fatigue, priorities)**.**

Many people have a lot of mystical or religious ideas about the 'mind', perhaps because they like the idea of life after death**.** I don't even know what pseudo-mystical concept you mean by 'consciousness' (since I doubt you mean "the state of being conscious" or "not sleeping or comatose" which is what my dictionary supplies for the word)**.**

WRGT burden of proof: psychologists have found similarity after similarity among human behavioral processes, whether it be grief, anger, flirtation, cognitive development and comprehension, skill development, how it is influenced by drugs or injury**.** Con-men and magicians and politicians have found that we share common fallacies of judgement and perception**.** Historians find similar experiences and cycles of conflict, and similar moments of strength and weakness on both sides of every conflict**.** Fiction stories all have similar plots, despite vast differences in culture or writing style**.** It seems to me that any library is a towering monument of evidence on my side**.**

Have you any evidence that whatever you mean by 'consciousness' is a consequence of whatever you mean by 'software'**?**

By [dmbarbour](http://lambda-the-ultimate.org/node/user/6002 "View user profile.")  at Wed, 2013-06-05 15:58 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Many people have a lot of](http://lambda-the-ultimate.org/node/node/4754#comment-75583)

> Many people have a lot of mystical or religious ideas about the 'mind'

I've noticed that certain cognitive phenomena are generally described by those who have experienced them in terms that sound mystical/religious to those who haven't**.**

By [John Shutt](http://lambda-the-ultimate.org/node/user/7549 "View user profile.")  at Wed, 2013-06-05 17:01 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Yes, and even by those who](http://lambda-the-ultimate.org/node/node/4754#comment-75591)

Yes, and even by those who HAVE experienced them**.** At least, that's what I find when I teach philosophy of mind**.**

By [Jason Grossman](http://lambda-the-ultimate.org/node/user/7175 "View user profile.")  at Thu, 2013-06-06 06:39 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Interesting**.** Things like](http://lambda-the-ultimate.org/node/node/4754#comment-75592)

Interesting**.** Things like "revelation", "epiphany", and "transcendent experience", and less individually spectacular ones like the aforementioned "magic nose" for the right question, have in common that to the person experiencing them, they are primitive elements of experience that can't be further decomposed**.** This I expect is because one's experience of self is a construct built at a rather high level on top of the hardware (er, wetware)**.** Iirc, a chapter of *[The Meme Machine](https://en.wikipedia.org/wiki/The_Meme_Machine)*  had some things to say about composing the narrative of self (though I was hampered in reading the chapter because I'd always thought of *self* as an emergent phenomenon, whereas Blackmore had apparently grown up thinking of it as elementary and consequently the narrative notion had come to her as a major revelation which she expressed as 'there is no *self*', leading me to say 'what nonsense', headdesk, and ask rhetorically 'then who do you think is writing your book', till I figured out she was saying something didn't exist that I had never thought existed in the first place)**.** When programming in a high-level language, one doesn't have visibility of the low-level implementation**.**

By [John Shutt](http://lambda-the-ultimate.org/node/user/7549 "View user profile.")  at Thu, 2013-06-06 11:31 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Right**.** I've given up, at](http://lambda-the-ultimate.org/node/node/4754#comment-75594)

Right**.**

I've given up, at least temporarily, on understanding what people mean by "self"**.** I agree that there's a wide variety of meanings.

I find that the students can't even agree on whether we have conscious experiences at all, except in the behavioural sense**.** And that's even AFTER I've been teaching them for a semester**.** These days I try to teach other topics**.** :-/

By [Jason Grossman](http://lambda-the-ultimate.org/node/user/7175 "View user profile.")  at Fri, 2013-06-07 03:39 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Whose burden of proof is it anyway](http://lambda-the-ultimate.org/node/node/4754#comment-75585)

> You are suggesting that all humans use the same same thought processes**.** So prove it**.**

David's been a skeptic here, questioning the assertion that people think differently**.** No evidence/argument in favor of that assertion has convinced him yet**.**

> Moreover, no one can even enumerate or model thought processes in humans to any degree of completeness or fidelity, so how can you so confidently assert that they are all identical**?** That's not sound reasoning**.**

Even if we agree that "no one can even enumerate or model thought processes in humans to any degree of completeness or fidelity," why should we conclude people's thought processes are different**?** We'll need *some* degree of detail to start seeing a difference, and even then, a lack of completeness means we might be observing different parts of the same elephant**.**

Personally, I'm not sure where I'd fall in this debate, but I'm currently holding the following beliefs: I think we as individuals will fight to preserve the freedom of our free will, so there's always going to be some part of our thought processes that is not yet explained, if we have anything to say about it**.** At the same time, there's always *some* similarity between any two systems we call "thought process," since we've recognized them well enough to give them the same name**.** People leverage this similarity every day to pursue concrete goals in the fields of education, advertising, deception, design, entertainment, personal relationships, and human culture in general**.**

By [Ross Angle](http://lambda-the-ultimate.org/node/user/11926 "View user profile.")  at Wed, 2013-06-05 17:48 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Clearly this discussion is](http://lambda-the-ultimate.org/node/node/4754#comment-75578)

Clearly this discussion is going nowhere**.** You're consistently missing the point of pretty much everything I say**.** It's far too consistent to be plausibly explained by "different knowledge/experiences/etc**.**"; Ockham's Razor calls for a deeper explanation. Different experiences aren't nearly enough to explain something of this magnitude, or I'd be having similar problems with everyone I encounter on LtU; but cognitive type (how one's mind works) determines what one's mind will *do* with one's experiences**.** This has become a classic case study in contrasting cognitive types leading to total communications breakdown**.** (I'm disinclined to the other systemic explanation that comes to mind, that you're deliberately trolling, though it wouldn't be the first time I was led astray by my distaste for thinking ill of others**.**)

By [John Shutt](http://lambda-the-ultimate.org/node/user/7549 "View user profile.")  at Wed, 2013-06-05 11:44 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [You're consistently missing](http://lambda-the-ultimate.org/node/node/4754#comment-75582)

> You're consistently missing the point of pretty much everything I say**.** Different experiences aren't nearly enough to explain something of this magnitude

I think they are**.** But it isn't the only sufficient explanation. If I find your points lacking in merit or irrelevant, then it might seem to you like I'm missing them when I'm *dis*missing them**.** There is a difference between understanding your points and accepting them**.**

> cognitive type (how one's mind works) determines what one's mind will do with one's experiences

So does skill**.** Or motivation. You still haven't pointed me at this allegedly convincing research of yours on 'cognitive type'**.**

By [dmbarbour](http://lambda-the-ultimate.org/node/user/6002 "View user profile.")  at Wed, 2013-06-05 16:11 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Lovely logical impasse](http://lambda-the-ultimate.org/node/node/4754#comment-75584)

> If I find your points lacking in merit or irrelevant, then it might seem to you like I'm missing them when I'm *dis*missing them**.**

Lovely logical impasse, isn't it**?** If you are, in fact, so totally missing my points that you're unable to see that you're missing them, then when I suggest you are missing them, you might conclude that I'm failing to realize that you understand my points but are dismissing them**.** There is one curious point of asymmetry. If all minds work alike (as you appear to have claimed), then for me to misunderstand you that much would require me to be failing on the same playing field you're on; whereas if there are various different ways for minds to work (as I've claimed), then you could misunderstand me simply because we're on different playing fields**.**

By [John Shutt](http://lambda-the-ultimate.org/node/user/7549 "View user profile.")  at Wed, 2013-06-05 17:30 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [There are many reasons we](http://lambda-the-ultimate.org/node/node/4754#comment-75586)

There are many reasons we might misunderstand one another, even to argue on "different playing fields", despite thinking by the same mechanisms. Common cases include attributing different meanings for the same words, or having different unspoken foundation assumptions, or using different logics, or even due to simple but self-reinforcing errors in reasoning (our brains aren't deterministic, error-free machines; and they have a lot of known biases)**.** The dichotomy you are insinuating is false, and you seem too eager to classify the discussion as an example in your favor**.**

By [dmbarbour](http://lambda-the-ultimate.org/node/user/6002 "View user profile.")  at Wed, 2013-06-05 20:18 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [dichotomy](http://lambda-the-ultimate.org/node/node/4754#comment-75588)

It appears you've misunderstood what dichotomy I was describing**.** I'd get a chuckle out of that, if not for gloomy recognition that you're unlikely to appreciate the humor**.** (Sharing a joke is fun, regardless of whether folks disagree, so being unable to share one is just depressing**.**)

By [John Shutt](http://lambda-the-ultimate.org/node/user/7549 "View user profile.")  at Wed, 2013-06-05 22:45 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [studies](http://lambda-the-ultimate.org/node/node/4754#comment-75587)

I don't find this any more convincing than dmbarbour does**.** Could you please cite the studies you mentioned.

By [Anders Horn](http://lambda-the-ultimate.org/node/user/8702 "View user profile.")  at Wed, 2013-06-05 22:22 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Learn the math instead](http://lambda-the-ultimate.org/node/node/4754#comment-75541)

For what it is worth, from the perspective of an amateur mathematician, monads and adjoints in there true category theory form explain a lot about any theory of computation**.** But programming monads don't inherit much from their mathematical cousins**.** I suggest learning the math instead.

By [Hank Thediek](http://lambda-the-ultimate.org/node/user/1977 "View user profile.")  at Sun, 2013-06-02 15:10 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Misogynist language](http://lambda-the-ultimate.org/node/node/4754#comment-75864)

I realize this discussion thread is quite old, but perhaps it's not too late to say something, in case folks catch it in the "new comment" sidebar:

"Bitch" as it's used in this context is a gendered slur**.** Accepting this sort of language in our discourse has some unsettling underlying assumptions, specifically that certain kinds of criticism are invalid because they amount to whining about inconsequential things, i.e. "bitching"**.** The word used in exactly this context has a long history as the premise for gendered violence**.** For further reading, I suggest http://www.shakesville.com/2007/11/on-bitch-and-other-misogynist-language.html

While I'm sure no one here would intentionally promote misogyny, I would like to suggest refraining from using (even quoting) such language, or if you must quote it, making a short note at the top of the post (like "note: excerpt contains gendered slur")**.** This suggestion comes from my understanding that said language could deter new female participants to LtU -- perhaps due to being triggered by the slur itself or perhaps due to the lack of mention by 109 comments that there might be a problem**.** I'm hoping to at least take off the edge with a 110th that points it out**.**

I've mentioned this issue to Ehud Lam, who encouraged me to write this response**.**

By [Chris Martens](http://lambda-the-ultimate.org/node/user/4291 "View user profile.")  at Wed, 2013-07-03 18:44 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Thanks for noting this](http://lambda-the-ultimate.org/node/node/4754#comment-75865)

Thanks for noting this issue, Chris**.**

While I know these issues are contentious, I am glad you brought it up since I hope people will reflect on the issue**.** Even if this particular usage is not a problem, as some probably think, we should strive as a community to make everyone feel welcome**.**

Finally, let me note that I know that speaking up on such issues requires courage**.** I hope people here will accept your message as being in good faith and refrain from "shooting the messenger**.**"

By [Ehud Lamm](http://lambda-the-ultimate.org/node/user/1 "View user profile.")  at Wed, 2013-07-03 19:07 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Feedback welcome as always**.**](http://lambda-the-ultimate.org/node/node/4754#comment-75872)

I reply only because I used the word in the same verb sense Joe did, to echo his usage**.** Unless I can find a way to make this PL relevant, I'll keep this comment short, and may not say much more if this subthread grows (unless temptation is unbearable)**.** As preface, I agree with Ehud: thoughtful commentary is welcome, especially when it involves context, framing of ideas, and consideration to others**.**

The noun sense is gendered and sexist, yes**.** But the verb sense is not, as far as I've known in context from reading; it's just a vulgar way to say *complain***.** Undoubtedly an argument from [etymology](http://www.etymonline.com/index.php?allowed_in_frame=0&search=bitch&searchmode=none)  says they're closely related**.** I'm going from usage, but usage changes, and words wax and wane in popularity — usually a stock metaphor goes here, but I won't bother**.** On current usage, I'm willing to take the opinion of someone who has spent at least ten thousand hours reading in the last dozen years**.** Otherwise I'll stick with the old standard meaning**.**

I started reading a lot when I was in third grade, around 1967, starting with science fiction short stories on the playground**.** Either it was one of the ways I escaped being heckled as a northerner, by boys in Chattanooga, or else I just liked [A**.** E. van Vogt](https://en.wikipedia.org/wiki/A._E._van_Vogt)  writing about the weapon shops**.** Over the next ten years, I read a lot of golden age science fiction, to the extent I gave up television early in high school because I preferred reading**.** (Well, television was boring, like watching paint dry—always the same**.**) Maybe I was a bit shy of ten thousand hours of reading by age 18, but not by age 21 (hard to estimate)**.**

I can assure you, if Joe was using the same sense I was — with meanings once understood as standard back in the dark ages before the internet — any nuance of gendered framing is not present**.** Maybe it's changed. Censorship sucks. Consideration for others is cool. We'll work something out**.**

Edit: I expect to participate on LtU less, and may check discussions infrequently, but I'll still be around**.** Maybe a discussion topic should be started on culture, social convention, and standards of behavior**.** You could start by addressing how problematic that is**.**

By [McCusker](http://lambda-the-ultimate.org/node/user/2390 "View user profile.")  at Thu, 2013-07-04 08:22 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [This seems to match my](http://lambda-the-ultimate.org/node/node/4754#comment-75874)

This seems to match my experience of the language: the noun is gendered, the verb, not**.** It is, of course, entirely possible for such things to vary between idiolects**.**

I recall from years ago (worrisome, that I'm prone to wandering off into reminiscences) an *On Language* column of William Safire's about the evolution of US terms for Americans of African descent**.** Iirc he traced it through most of the nineteenth century, during which, again and again, there would be two terms, a slur and a euphemism, the slur would be abandoned, the euphemism would become a slur, a euphemism would arise to use instead of the slur, and the process would repeat**.** And repeat**.** Until at the end of the period covered, the term that had first been abandoned as a slur was reintroduced as a euphemism**.** The lesson I took from that was that politically correct termionlogy cannot change deep-seated attitudes, because the PC terms absorb the speakers' attitudes rather than the other way around**.** (I remember my grandmother struggling with this; she was a teenager in the 1890s — the Gay Nineties, culturally liberal like the 1920s and 1960s — and just couldn't keep track of which term was currently acceptable**.**)

The point of that weary digression is that how our culture's attitudes infect our words tells us something important about what those attitudes are**.** Does our culture allow the verb and the noun to be related only by an etymological footnote**?** For my part, I really applaud someone speaking up when they're uncomfortable with a term; and at the same time, I'd find it hopeful if our culture has relaxed enough to allow the verb to not be infected by the noun**.**

By [John Shutt](http://lambda-the-ultimate.org/node/user/7549 "View user profile.")  at Thu, 2013-07-04 12:05 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [Language is communication](http://lambda-the-ultimate.org/node/node/4754#comment-75876)

Language is communication between sender and receiver**.** What the receiver interprets may not be as benign as the sender intended due to cultural differences or simply different experiences in life**.** Fortunately the solution is easy: s/bitch/complain/**.** No meaning is lost, and no room for unintended interpretations**.**

By [Jules Jacobs](http://lambda-the-ultimate.org/node/user/2891 "View user profile.")  at Thu, 2013-07-04 14:32 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments

### [I’m not sure I agree**.**](http://lambda-the-ultimate.org/node/node/4754#comment-75868)

I’m not sure I agree**.** Language raises subtle issues, natural language especially so**.** “Bitch” is in an unfortunate state of transition at the moment**.** You cannot tell, in the absence of other information, what *connotation* an author has in mind when they use the contemporary denotation of “to complain excessively”—whether they intend to convey gender-biased undertones or not**.** Words themselves make no matter except by their intent and interpretation; without knowledge of someone’s intent, we should confer the benefit of the doubt—with the stipulation that *maybe* they should avoid certain language in polite company in the future**.** :)

By [Jon Purdy](http://lambda-the-ultimate.org/node/user/12454 "View user profile.")  at Thu, 2013-07-04 01:25 | [login](http://lambda-the-ultimate.org/node/user/login)  or [register](http://lambda-the-ultimate.org/node/user/register)  to post comments
