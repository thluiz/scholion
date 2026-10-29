---
url: "https://www.quora.com/Which-language-has-the-brightest-future-in-replacement-of-C-between-D-Go-and-Rust-And-Why"
captured_at: "2015-11-11T11:18:15-03:00"
title: "Andrei Alexandrescu's answer to Which language has the brightest future in replacement of C between D, Go and Rust? And Why? - Quora"
domain: "quora-com"
---

# Which language has the brightest future in replacement of C between D, Go and Rust? And Why?

79.7k ViewsUpvoted by [Laeeth Isharc](https://www.quora.com/profile/Laeeth-Isharc), Programming in C since 1985[Miguel Paraz](https://www.quora.com/profile/Miguel-Paraz),

In spite of my status and obvious bias as co-creator of D, I'll do my best to answer candidly; I follow Go and Rust, and I also definitely know where D's dirty laundry is. I'd encourage people with similar positions in the Rust and Go communities to share their honest opinion as well. So here goes.  
  
First off, C++ needs to be somewhere in the question. Whether it's to be replaced alongside C, or be one of the candidates that's supposed to replace C, the C++ language is a key part of the equation. It's the closest language to C and the obvious step up from it. Given C++'s age, I'll assume in the following that the question also puts C++ alongside with C as a target for replacement.  
  
Each language has a number of fundamental advantages (I call them "10x advantages" because they are qualitatively in a different league compared to at least certain baselines) and a number of challenges. The future of these languages, and their success in supplanting C, depends on how they can use their 10x advantages strategically, and how they overcome their challenges.

## So let me dispense with D first

Obviously this is my house's tour so I know where to walk you all to appropriately show/hide the clean and dirty corners. I'll also have probably more to say about D than the two others for the simple reasons I *know* more about D than the two others. Speaking with brutal honesty, D's main challenges are:

- *Poor adoption after many nominal years of existence.* Insiders to the D community could qualify this statement (D in its current form is relatively new, adoption does grow, etc). Yet the perception remains, and adoption is driven by perception and becomes fact. So managers and engineers are nervous about adopting a language that's been around unsuccessfully for so long. Furthermore, time works against D unless/until a major uptick in adoption becomes obvious.
- *Weak story about D's relationship to garbage collection.* GC is a great invention, but the decision to use it for D has instantly alienated a core market - existing C and C++ programmers. For those, the party line has historically been "Don't want GC? No problem! You can use D with RAII or manual management style as well!" Though true, that's next to useless because there's little support in the standard library for alternative memory management styles, which means the putative user would need to start with the language stripped down to the studs and create all the core infrastructure. Also, for those who are okay with using a GC, the quality of its implementation is lackluster. Overall it could be said that D has the downsides of GC but doesn't enjoy its benefits.
- *A historical lack of vision.* Absent corporate support, D has been community-driven, where engineering acumen is easier to find than long-term vision, charisma, and leadership. For a good while, the stridency of D's attempts at promotion and PR has had negative value. The first vision document (<http://wiki.dlang.org/Vision/2015H1>) is dated January 1, 2015, and the next iteration ([Vision/2015H2 - D Wiki](http://wiki.dlang.org/Vision/2015H2)) has been four months late in a six-months cycle, which is at best ironic.

There would be, of course, other issues but they either derive from the above or have a much smaller impact.  
  
D's 10x advantages are, I think, the following (when I say "10x" in the following I mean it colloquially a la "one order of magnitude"):

- *10x faster to compile than C++ for comparable produced code.* This gap is essentially impossible to bridge for C++ and prohibitively difficult for any other language. (Go compiles a tad faster than D, but produces slower code.) The experience of using a system language that builds this fast code this fast is transformative and far-reaching. Combined with D's abstraction power, it essentially makes D a good choice for writing highly optimized code for the simple reason that experimentation has a low cost.
- *10x faster than scripting languages for comparable convenience.* A good use of D is as a convenient scripting language for a variety of casual tasks. The build/run cycle is just as quick, and the gain in speed is enormous. Also, there's no "hitting the wall" effect - if a script grows large, D has always more power and modular mechanisms to offer. Of course, this must be taken with a grain of salt because e.g. Python has much more libraries available. But the 10x gap is fundamental: systems languages would have difficulty getting to D's level of conviviality, whereas scripting languages would have difficulty closing the speed gap.
- *10x easier to interface with C and C++ than any other language.* D uses the same memory layout as C and C++; all it does is build structure on top of it, but the lower layers are readily accessible at no cost. The entire C standard library is readily accessible at no syntactic or speed cost,  there is work to allow the same for the C++ standard library, and many C libraries are easy to interface with ([https://github.com/D-Programming...](https://github.com/D-Programming-Deimos)). It could be claimed that literally no other language can reach that level of integration.
- *10x better than any other system language at generic and generative programming.* D's static introspection, compile-time evaluation, and mixin-driven code generation combine to a powerful cocktail that is very difficult to mix right in other languages, be they new or extant; at this game, Go is so out of depth it doesn't even get the point; C++17 is hopelessly lost in the woods; and Rust is just trying to dabble.

## **On to Go**

I should reinforce here that this is solely my opinion, worth what you pay for it. Go's challenges are the following:

- *Fundamental slowdown due to indirect calls and garbage collection.* Virtually no meaningful Go can be written without resorting to indirect function calls and garbage collection, which are central to its core features. These are major impediments to achieving in-core performance. The response of the Go team has been tactical, e.g. work on a better garbage collector. However, it's unlikely that the challenge of replacing C can be won tactically.
- *Politics.* Go's party line has been disproportionately strong and rigid on a number of issues, small and large. Among the larger issues, the approach on generics has been heavy-handed and demeaning enough to make generics the N word of Go; the whole topic has become enough of a stigma to discourage any attempts at meaningful dialog. I think politicizing of technical matters is an extremely damaging pattern in the long run, and I hope Go finds a way to repair this.
- *Simple-cum-simplistic.* Go is famously simple - there are anecdotes of people picking it up quickly. However, that becomes problematic as time goes by; Go code is hopelessly pedestrian - Go coders find themselves writing again and again the same things from an ant's vantage point because Go cannot abstract even the simplest notions or algorithms. Domains that are not already served by easy to glue libraries are difficult to get into. There is backlash from coders who have used Go for one project and wouldn't want to ever use it again. It would be great if Go made life better for repeat customers.

Go's 10x advantages are in my perception the following:

- *10x better strategy.* After a brief period in which Go claimed to be a systems programming language, it has fully committed to the niche of networking services. This has been a brilliant marketing move, which capitalized on the strengths of the Go team (some of the best engineers in the world at networking services). That market is hot, and Go was a fresh breath of air in a world dominated by Java EE bureaucracy and slow scripting languages. Now Go is a major player in that area, and it would be difficult to displace it.
- *10x engineering.* Go has a solid engineering team behind it, and that's a major influencer of the quality of the language and in particular the networking library and the tooling. Until now, good engineering has compensated very well for the lack of power in the language.
- *10x branding.* Many of us are ready to admit that a main motivator of Go is its connection to Google. That gives it a clout of professionalism, quality, and stability. Of course, brand is not everything, but what it means is all Go has to do is be a decent language; it doesn't have to be a fantastic language. The brand works out the rest.

## Last but not least, Rust

Let me again remind that this is only my opinion. I think Rust is facing some interesting challenges:

- *A disharmonic personality.* Reading any amount of Rust code evokes the joke "friends don't let friends skip leg day" and the comic imagery ([https://www.google.com/search?q=...](https://www.google.com/search?q=friends+don%27t+let+friends+skip+leg+day&safe=off&tbm=isch&tbo=u&source=univ&sa=X&ved=0CB0QsARqFQoTCM_ViveKhMkCFUfZPgodVsgLsA&biw=1582&bih=1352)) of men with hulky torsos resting on skinny legs. Rust puts safe, precise memory management front and center of everything. Unfortunately, that's seldom the problem domain, which means a large fraction of the thinking and coding are dedicated to essentially a clerical job (which GC languages actually automate out of sight). Safe, deterministic memory reclamation is a hard problem, but is not the only problem or even the most important problem in a program. Therefore Rust ends up expending a disproportionately large language design real estate on this one matter. It will be interesting to see how Rust starts bulking up other aspects of the language; the only solution is to grow the language, but then the question remains whether abstraction can help the pesky necessity to deal with resources at all levels.
- *Foreign syntax.* Rust's syntax is different, and there's no apparent advantage to the difference. This is irritating for folks coming from Algol-style languages, who need to deal with a gratuitously different syntax in addition to getting the resource bookkeeping right.

Rust's 10x advantages are:

- *10x better theorists.* Of the three, Rust is the only language with world-class PL theorists on roster. This can be seen in the precise definition of the language and the depth of its technical approach.
- *10x better safety than other systems programming languages.* Of course that had to be here, we just discussed the cost of that.
- *10x better PR*. There has been a long period pre-1.0 when Rust was a community darling and could do no wrong: whatever problem there was, either Rust had a solution to it, or will have had by 1.0. The realities of 1.0 ended that honeymoon and marked (by my measurements and estimates) a stark decrease in general interest, but these effects have a way to linger. Plus, after all, Rust is a decent language with real things going for it, and it's well positioned to convert this lingering hype into solid marketing.

## In brief

Whether any of these languages is well positioned to either progressively replace C, C++, or both in existing codebases; and whether any of these languages become preferred choices for projects that today would choose C or C++ by default---it all depends on the ability of these languages to play into their respective strengths and find creative solutions to their respective challenges.
