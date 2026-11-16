---
url: "https://stackoverflow.blog/2020/06/05/why-the-developers-who-use-rust-love-it-so-much"
captured_at: "2026-11-16T03:44:34+00:00"
title: "Why the developers who use Rust love it so much"
domain: "stackoverflow-blog"
---

The 2020 Developer Survey results are in, and once again, Rust is the number one most loved language among the 65,000 programmers who participated. Rust has taken the number one spot since 2016, showing that it’s got something that the developers who use it love. 86.1% of those survey respondents who said they currently use Rust want to continue using it next year. This is the fifth year in a row that Rust has taken this top spot, so we figured it’s got to have something special.

A few months ago, we asked Stack Overflow’s top Rust contributor, Jake Goulding (aka [Shepmaster](https://stackoverflow.com/users/155423/shepmaster)), to explain [what makes Rust such a hit](https://stackoverflow.blog/2020/01/20/what-is-rust-and-why-is-it-so-popular/) with the coders who used it. Here’s a sample of what he had to say:

“The short answer is that Rust solves pain points present in many other languages, providing a solid step forward with a limited number of downsides.”

The full article is well worth a read, as he covers the benefits (as well as the pain points) of Rust for coders coming from other languages. But as eloquent and persuasive as Jake is, we wanted to hear from more users. So I reached out for comment in our [Rust chatroom](https://chat.stackoverflow.com/rooms/62927/rust) and on the [Rust forums](https://users.rust-lang.org/). Rust users are a passionate bunch, and I got some fascinating insights along with some friendly debates.

(The quotes below are edited for length, clarity, and to group them conceptually. Many of them come from [this thread](https://users.rust-lang.org/t/rust-is-again-most-loved-in-stack-overflow-survey/43455/22) on the Rust user forums, so if you want to read them all in full and in context, feel free.)

Without further ado, here’s why Rust gets so much love, straight from the Rustaceans themselves (including two members of the Rust core team.)

_While some languages just add polish and ease to existing concepts, several users feel that Rust is actually doing new things with a programming language. And it’s not doing new things just to be showy; they feel these design choices solve hard problems with modern programming._

[**ZiCog**](https://users.rust-lang.org/u/ZiCog): “Rust is the only language of the dozen or so I have used professionally for four decades that actually introduces genuinely new features. Namely the whole idea of safety of memory usage in a compiled, real systems programming language with no garbage collection or complicated run-time system.”

[**Denys Séguret**](https://dystroy.org/): “We frequently have such enthusiasm when we discover that a quite powerful feature like reading a compilation context element under the disguise of an env variable can be done so elegantly, and even be solved at compile time, without any ugly inconsistency.”

[**janriemer**](https://users.rust-lang.org/u/janriemer): “A quote from Chris Dickinson, engineer at npm, sums it up perfectly for me, because I have thought the same, without knowing the quote at that time: ‘My biggest compliment to Rust is that it's boring, and this is an amazing compliment.’

Rust is a programming language that looks like it has been **developed by user experience designers.** They have a clear vision (a _why_) of the language and _carefully_ choose what to add to the language and what to rework, while listening to what the community really wants. There are no loose ends, it's all a coherent whole that perfectly supports a developer's workflow.”

**[skysch](https://users.rust-lang.org/u/skysch): “**I came to Rust from Haskell, and I feel that Haskell is a very elegant and safe language. The biggest differentiator for me is that there is a greater difference between high-performance code and idiomatic 'clean' code in Haskell than in Rust. Most Rust code looks like most other Rust code, even when it performs well. Haskell can become unfamiliar real quick if someone is operating under different libraries and goals from what you are typically doing. Small differences in syntax can result in huge differences in behavior, and Rust has more uniformity on that axis.”

**Jay Oster, Architect at [PubNub](https://www.pubnub.com/)**: “Beyond safety and performance, we have:

*   generics;
*   traits;
*   algebraic types;
*   functional and imperative paradigms;
*   perhaps the world's best dependency management and build tool, which has practically solved the ‘dependency hell’ problem;
*   fantastic support for inline documentation, tests, and benchmarks;
*   a large and growing ecosystem of libraries, abstractions, and tools;
*   procedural macros;
*   FFI interoperability with existing code;
*   support for dozens of platforms (with more on the way!);
*   and a developer experience that is just wholesome and unquestionably satisfying.

Rust is the only language that ticks all the boxes:

*   Memory safe
*   Type safe
*   Data race-free
*   Ahead-of-time compiled
*   Built on and encourages zero-cost abstractions
*   Minimal runtime (no stop-the-world garbage collection, no JIT compiler, no VM)
*   Low memory footprint (programs run in resource constrained-environments like small microcontrollers)
*   Targets bare-metal (e.g. write an OS kernel or device driver; use Rust as a ‘high level assembler’)”

[**daboross**](https://users.rust-lang.org/u/daboross): “Compile time guarantees: When I think of a "statically typed language", I think of Java, or C#, or something like TypeScript. They give compile-time assurances that your code has the correct types, and move a set of errors from runtime to compile time. Rust goes one magnitude further in this! Compile time checking extends to thread safety, to ownership semantics, to validation.

Enums mean that, at compile time, I can declare the set of variants my data can exist as, and when accessing that data I'm forced to consider all possibilities. Traits mean that when my code is templated/generic, I have exact capabilities I can require.

Rust is _extremely_ backwards compatible. I can run code written for Rust 1.0. Equally, I can write code which I know I won't have to update next time I update Rust.

And it's not just Rust itself - the language enables libraries to have the same guarantees. Consider two facts:

*   In type checking, _only the signature of functions are considered_. There's no relying on the implementation for determining if callers are correct (like you can do in Scala, or Haskell)
*   The extensive type system means _incorrect usages of interfaces become type errors, not runtime errors_.

Because of these two things, libraries can be 100% sure that they maintain backwards compatibility when releasing a new interface. In Python, or Java, or Javascript, or even Scala or Haskell, you need to pay extra attention to implementations of things if you want to ensure you maintain backwards compatibility. In Rust, it's free: if you haven't changed the function signature, it remains the same.”

[**Peter Varo**](https://petervaro.com/): “Rust found a sweet spot: it is just as low-level as C or C++ with all the advantages of these (e.g. control, size, speed, etc.) At the same time, it is as high-level as Haskell with an amazing amount of functional heritage. It is still imperative, so quite accessible to most people, and it is just as flexible as Python. For example, concepts like "duck-typing" are happening at compile time (i.e. trait bounds), yet it does not have the dated, object-oriented programming model and all of its well known problems.

Last but not least, the batteries which are included: the small and concise syntax, the small number of features the language provides, the integrity of the standard library as well as its consistency and the quality of its documentation, including the learning materials for both beginners and advanced users are all contributing factors.”

[**blonk**](https://users.rust-lang.org/u/blonk): “With Rust/cargo I can focus on the actual code rather than the build system. No need to spend whole days reading up on Yet Another Build System. Cross-compilation with Rust is so incredibly simple and painless that when you read up on how to do it, you can't help but think "Wait, I must be missing something."

When you're outside of Rust, there are things that sound like empty slogans, but when you start using it you'll become pleasantly surprised to realize there's a lot of truth to:

*   While you spend time fighting to compile your code, you save that time in not having to debug your code.
*   You're no longer afraid of major refactoring. Once your refactored code compiles, it works as intended.
*   It really does force you to do proper multithreading (well, you can still deadlock, but the crashy types of bugs are far more difficult to do).

I find myself doing far less boilerplate code. And what boilerplate code I do need, I can often hide in a different module so it doesn't get in the way of the actual application logic code. (Most common example of this is the error type conversions).”

_Many current programming discussions revolve around whether to use a fast, low-level language that lets you handle memory management or a higher-level language with greater safety precautions. For fans of Rust, they like that it does both._

**Jay Oster, Architect at [PubNub](https://www.pubnub.com/)**: “It's akin to wandering around in complete darkness for an entire career, and suddenly being enlightened to two facts:

1.  You are not perfect. You will make mistakes. Those mistakes will cause you a lot of problems.
2.  It doesn't have to be this way.

I see a common dissent where some proclaim that they _are_ in fact perfect, and that they do write flawless code, and everything is peachy, and they can't understand why everyone else is so interested in Rust. But it's clear to this old goat that these are the people who haven't yet learned that the problem is not _strictly themselves_; it's everyone else. It's a problem of economy of scale.

In other words, I myself could write flawless and bug-free code in isolation if I had the time and energy to pay attention to every minute detail and meticulously hand-craft every beautiful line regardless of the language or implementation details. _But that doesn't matter._ Once I start depending on code written by other people or new contributors come along and make modifications, all of my so-called guarantees of perfection are now incompatible with reality. ‘Correctness by convention’ does not scale.

Conventions will have faults and impractical amounts of time and energy will be spent trying to automate a bandaid that should not exist in the first place. The "aha!" moment is realizing that one can actually get much stronger guarantees by baking those same conventions directly into the language and compiler.

To top it off, you can also get performance equivalent to that of finely tuned hand-written assembly, if you so desire. You can have your cake and eat it too!”

[**daboross**](https://users.rust-lang.org/u/daboross): “As a library author, the complex trait/generic system means I can craft intricate, yet easy to use interfaces. These interfaces _cannot be used incorrectly_, which means I don't have to perform runtime checks, and my users don't have to even _think_ about problem cases, because they _can't write them_.

As a library consumer, the rich and extensive [crates](https://doc.rust-lang.org/book/ch07-01-packages-and-crates.html) ecosystem enables me to write code in vast different domains without needing to dig into the specifics of every one. I don't need to know how a JSON parser or writer works to use serde - and my lack of knowledge won't ever be a source of bugs, because I get compile time errors rather than runtime ones.

I just feel really taken care of when I'm using Rust. There are _so many_ trivial things, from package upgrades, to type errors, to passing in a string which an interface doesn't expect and getting a random runtime error which I'm _completely free of_ in Rust. I can just think about the algorithms!”

_Remember that debate I mentioned? Some of the back and forth I saw came from wondering if the Most Loved title comes from Rust having a small user base that mostly use the language by choice. While it’s true, only 5.1% of our survey respondents had used Rust in the past year, those users want to keep on using Rust._

**[CAD97](https://users.rust-lang.org/u/CAD97): “**To be perfectly frank: I think Rust benefits here that very few people are being forced to use Rust. Most people are electively using Rust, still.

I'm not saying Rust doesn't deserve the label (I'm pretty sure it does!), I'm just arguing that Rust is in a _very_ good position to "game" the metric SO is actually measuring here, because it has a large elective adoption from enthusiasts but a low(er) adoption by those who would mandate people to use a language they would rather not continue to use.”

[**ZiCog**](https://users.rust-lang.org/u/ZiCog): “If you use any programming language long enough you will come to think it sucks. Use many, over many years, they all suck.

Those that do a lot of programming in all kinds of languages and have the skill and talent, end up inventing and implementing their own new programming language to fix all the pains they have suffered in the past. As you know, new languages sprout like weeds as a result.

Given the above, if you ask programmers what language they love it will not be the one they are using or any they have used in the past.

As almost no programmers have had to use Rust for the long haul so far of course they will say they love Rust.”

**Jay Oster, Architect at [PubNub](https://www.pubnub.com/)**: “I had a similar ‘grass is always greener’ bias toward various languages over the decades. But I think this isn't one of the primary contributing factors to this phenomenon. If it were, we might expect some of the newer languages to come out on top in these surveys, right?”

**[H2CO3](https://users.rust-lang.org/u/H2CO3): “**Rust is currently my favorite language by far, despite the fact that I've been using it for 4 years now (for personal projects, as well as "real" code, out of need for performance). By the time I had this much experience with C and C++, I had already discovered their bundle of serious shortcomings.

Heck, even Haskell, the most elite of elegant languages, showed its inevitable ugliness after about a year or so, when I had to start fiddling with language extensions and dialects in order to get a somewhat advanced library to compile.

This simply didn't happen in Rust. The bag of footguns and design errors just never emerged from the mist.”

[**asafigan**](https://users.rust-lang.org/u/asafigan): “I believe that Rust is challenging to learn but rewarding to use. I think it is actually surprising how much people enjoy being challenged as long as the reward is good enough.

I found Rust hard to learn but pretty easy to use. I think a lot of people come to Rust from a different language and are surprised how much different (and therefore hard to learn) it is. But they forget how hard it was to learn to program in the first place. In college, we had two courses on Object Oriented Programming in Java. By the end, most people still didn't really get it. Rust is different enough from other languages to be hard to learn. It's hard to learn say Functional Programming if all you know is OOP. It's hard to learn OOP if all you know is Functional. It's hard to learn Ownership if all you know is GC or manual memory management. Traits are pretty weird too. But it's worth it for better software.”

**[cfsamson](https://users.rust-lang.org/u/cfsamson): “**In Rust, I find that a lot of the effort is front loaded. It makes easy problems somewhat harder to get started on, but it doesn't create hard problems later on. If there are problems it's most often the problem domain itself that is harder than I thought, and not related to the tools I use. I find the price I pay up front is definitely worth what I get. I also find the price low once you get to know the language well.”

_From talking to fans, I found that their love of the language shines through pretty hard, even when they disagree. Rust user blonk identifies this as a community-wide characteristic._

[**blonk**](https://users.rust-lang.org/u/blonk): It's pretty clear that this whole "be respectful" is working very well. There have been a few cases where people have, imho, asked questions in bad faith, but rather than coughing up a giant hairball over the situation, community members reply in good faith, and it defuses the situation.

_If you want to know what makes a devoted supporter, talk to the most devoted, right? I reached out to the Rust team to find out why they think Rust gets so much love, year over year. The format is a little different, I've kept the question and answer layout._

_Erin Power is a Rust developer based in Berlin. She has been using Rust since 1.0 in 2015. She is one of the leads of Rust's Governance WG, and is the creator of "[Tokei](https://github.com/XAMPPRocky/tokei)" a popular open source code counter written in Rust._

_**Q:** People who use Rust really seem to like it; why do you think that is?_

**A:** I think it's because Rust makes big promises, and delivers on them.  
Rust provides automatic memory management like any other high level language, but it's done at compile time so there's no hidden cost or behavior to account for.

Rust has always been designed for what we expect in modern hardware. Thread safety and data races, which can be a common footgun in other languages, were accounted for at the language level. As a result it can be incredibly easy to take full advantage of your workstation's capabilities without a lot of changes or headaches. It's always been impressive to me how `rayon` (a popular library in Rust) can parallelize your entire workload by changing just a single line of code.

As a result there's been a lot of high quality and fast implementations being written in Rust, and thanks to cargo and [crates.io](https://crates.io/) (Rust's package manager and community run package registry), it's never been easier to reuse and share that code both internally and with the world at large.

Cargo handles a large repository with several to dozens of packages just as well as it handles one, you don't need to spend days writing a build file to have the configuration you want.

Not only is it easy to manage and update your Rust dependencies, Rust itself is incredibly easy to upgrade and switch between different versions of the language with Rustup; a toolchain version manager that is included by default.

Any of the above points would be enough for somebody to like Rust, but taken altogether it makes Rust an incredibly compelling language that feels refreshing to write and create your projects in.

_**Q:** What's the Rust team planning to keep users in love with it?_

**A:** Well I can’t speak for what all the teams have planned, as Rust has dozens of teams consisting mostly of volunteers who are semi-autonomously all trying to improve the Rust language and the surrounding ecosystem. You can find out about [the project’s roadmap for the year](https://github.com/rust-lang/rfcs/blob/master/text/2857-roadmap-2020.md) on GitHub (though I will note that it was proposed and written before COVID-19).

_**Q:** Do you all use Rust regularly? How so?_

**A:** I’ve been writing Rust since it went 1.0 in 2015 and have tried to spend as much of my programming time writing in it since. I write and maintain quite a few open source applications and libraries that I maintain and I’ve been working with Rust professionally since 2018.

_**Q:** I've seen some comments that Rust is difficult to get the hang of, and in our survey, only a small (~5%) number of people had used Rust. Do you think there's a high barrier to entry to Rust? Why or why not?_

**A:** I think there are certainly specific concepts in Rust that have a high barrier to learn and use. Though speaking anecdotally, my background before Rust was in fullstack web dev and design; I had no previous “systems” or “functional” language experience, and I found it way easier to learn those concepts in Rust than other existing languages, so I wouldn’t agree that Rust as whole has a high barrier.

I feel that a lot of the high barrier comes from Rust being a relatively new programming language and there is not currently a wealth of resources coming from other perspectives that fit different people’s mental models to learn from like you have with the more well established languages. Hopefully, as time goes on we’ll have more diverse learning materials that help teach and improve understanding these concepts.

While only a small portion of people have written Rust, it's adoption has been such a success, a lot of critical pieces of software people use everyday have already been rewritten or created in Rust. Rust has already seen adoption in every single one of the big five tech corporations, and it's not just enterprises that are interested. Smaller tech firms like Dropbox or OneSignal have a lot of their core infrastructure for their services in Rust.

_Florian Gilcher has been programming in Rust since 2013. He’s a member of the community team since its inception and is currently part of the core team. Florian co-organised the first five RustFests and co-organises OxidizeConf. Before that, he was active in the Ruby community._

_**Q:** People who use Rust really seem to like it; why do you think that is?_

**A:** The simple first response is: because it’s a good product in many aspects. [Jake Goulding already gave a good overview](https://stackoverflow.blog/2020/01/20/what-is-rust-and-why-is-it-so-popular/) that I don’t want to repeat on your blog.

Beyond that, I’d highlight a few that are dear to my heart:

1.  A self-confident instead of a confrontational way of talking about the language.
2.  A good amount of new and brain-teasing concepts.
3.  A flexible organisational structure that covers many things ignored in other projects.

I’ll go a bit into detail why that matters: Many programming languages and tools are marketed in a confrontational and comparative matter. “Better than X”; “X is the new Y”; etc. Rust has always taken the approach of making good features stand out by themselves. For example, a cheap way of framing Rust would be to say that Ownership and Borrowing are fixes for C and C++ problems. This makes for a terrible argument, though: they are good for many other things, and this argument immediately pits Rust against C and C++. This can only end up in a heated argument. Rust is born out of the desire to improve on the current state of the art, with huge respect for the languages that came before it. For that reason, we do market Ownership and Borrowing as useful concepts to base a programming language on that are flexible and versatile underpinnings for Rust programmers' thinking. I think this fundamentally positive approach shapes the experience of people with the language.

Which brings me to point 2): Rust brings new concepts to the table that were previously in the realm of research. Those concepts carry back over into other programming languages. Ownership is such a case: “Which part of my program is responsible for this piece of data?” is a pretty good question to ask yourself during programming all the time, but Rust makes it a core concept and is rigorous about it. People spending time on Rust _will_ find something that will make them better programmers, even if they don’t immediately pick Rust up as their language of choice. This is not unique to Rust, but often mentioned in relation to it.

The final point is that Rust has chosen a holistic and flexible project structure and has been great at attracting a lot of experienced people. Producing an A+ community project does also mean we deal with a lot more then just code. If you look at the [team structure](https://www.rust-lang.org/governance), you’ll notice that there are quite a lot of teams with tasks you would not consider “core” tasks of building a programming language. This includes a community and a moderation team, a team dedicated to documentation, but also domain specific working groups, such as an embedded working group. This structures is always under flux and welcomes many efforts and experiences. This allows us to remain flexible and quickly address people’s particular needs. It also means that there’s always someone approachable for your particular question.

_**Q:** What's the Rust team planning to keep users in love with it?_

**A:** Making a great product even better!

For each piece of praise that Rust gets for its good tooling and design, there’s still a ton of things that could be improved!

I won’t speak for the team, but here’s my personal list that I’d like to help improving:

*   Make Rust more beginner-accessible by providing documentation geared to that group.
*   Have more localized documentation should be helpful.
*   Enable Rust in industry environments where it’s currently not being used (particularly safety-critical systems).
*   Work out existing edge cases and problems for all common platforms.
*   Make sure Rust has a great out-of-the-box IDE experience.

I’m rather okay with how the language is currently, so a focus improving the already good tooling is good.

_**Q:** Do you all use Rust regularly? How so?_

**A:** I use Rust or at least think about it daily. I run a Rust consultancy and train other people for using Rust better.

_**Q:** I've seen some comments that Rust is difficult to get the hang of, and in our survey, only a small (~5%) number of people had used Rust. Do you think there's a high barrier to entry to Rust? Why or why not?_

I don’t think Rust has a higher barrier to learning than any other language in the long run. It’s a pretty consistent language and once you have the basics down, they can carry you very far. There’s an immediate bump on that road, though: Rust is the worst language out there to run before you walk. The reason for that is that its core concepts, especially Ownership, don’t have something to compare to in other programming languages. And that concept is very nuanced. This means that Rust is hard to pick up in a day or two. Most people report that they need roughly one to two weeks to become productive with it. People that are productive in Rust appreciate a certain rigor and strive for correctness, but that takes some time to build.

Given that we have, in the last years, seen a drift towards “get productive immediately” in our industry and tooling, I can understand how the on-boarding experience of Rust differs a lot from what people are used to. I’d wish we found a way to provide this newcomer experience without compromising in the long-run experience.

If you’re looking for more reasons for why users love Rust, [**daboross**](https://users.rust-lang.org/u/daboross)suggested several links:

*   [fireflowers - The Rust Programming Language in the words of its practitioners](https://brson.github.io/fireflowers/) (three years old, but full of great insights)
*   [Why we chose Rust as our programming language (Bitbucket, June 2019)](https://bitbucket.org/blog/why-rust) 
*   [Still in love with Rust (@ dpc, Nov 2018)](https://dpc.pw/still-in-love-with-rust)
*   [Why I love Rust (Alex Kitchens, July 2018)](https://alexkitchens.net/why-i-love-rust)
*   [Why Rust? (Parity Technologies, July 2018)](https://medium.com/paritytech/why-rust-846fd3320d3f)
*   [Why Rust is the Most Loved Language by Developers (Jannette Ciborowski / Mozilla Tech, Apr 2017)](https://medium.com/mozilla-tech/why-rust-is-the-most-loved-language-by-developers-666add782563)
*   [Mozilla's Rust, and why we love it (Cambridge Consultants, Oct 2016)](https://www.cambridgeconsultants.com/insights/presentation-mozillas-rust-and-why-we-love-it)
