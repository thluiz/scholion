---
url: "https://arstechnica.com/gadgets/2026/09/mozillas-head-of-firefox-talks-product-priorities-ai-skepticism-and-browser-choice/?utm_source=tldrnewsletter"
captured_at: "2026-10-12T23:54:31+01:00"
title: "Interview: Firefox's chief on why he hopes a redesign will help win users from Chrome"
domain: "arstechnica-com"
---

[Skip to content](#main)

Firefox 157

Mozilla’s Ajit Varma explains why a redesign suits the fight for the open web.

Can a more modern look help gain market share? It can't hurt, but it's not the whole solution. Credit: [Mozilla](https://www.youtube.com/watch?v=l7tQ1v4TCeY)

Today, the [Firefox 157](https://www.firefox.com/en-US/whatsnew/157/) update will roll out a redesign of the web browser across desktop and mobile platforms. The team that made it hopes it will help expand the browser’s audience beyond privacy-conscious techies and open-web or open source advocates to a broader audience who might simply pick the browser because they prefer its user experience over competitors like Chrome, Edge, and Safari.

In advance of the redesign’s launch, I spent half an hour chatting with Mozilla’s head of Firefox, Ajit Varma, about Firefox’s current market position and product strategy, and what barriers or opportunities there are for gaining ground in a Chromium-dominated landscape.

Firefox’s interface has recently felt more conservative than niche browsers. And when I asked Paddy Harrington, a senior analyst at Forrester who covers this space, what Firefox’s main barrier to adoption is, he was frank.

“The biggest is they’re not Chrome,” he replied. “That sounds simplistic, but it’s the clear truth. Safari and Edge are built into the leading operating systems in business and consumer markets, yet people still download and deploy Chrome.”

That said, for many of the people who have chosen to use Firefox, “it’s not Chrome” is much of the appeal. Google-led Chromium dominates the web. It doesn’t just power Google’s own Chrome browser (which has majority market share by a wide margin), it powers most of the rest of the competition, too, including Microsoft Edge.

Firefox, which is built on the open source Gecko, serves as a Chromium-free alternative and has become one of the go-to choices for users who don’t want to contribute to one company’s dominance of the open web—though there [is even tension there](https://arstechnica.com/tech-policy/2025/02/firefox-deletes-promise-to-never-sell-personal-data-asks-users-not-to-panic/), and a deal to offer Google search as Firefox’s default provides Mozilla with the majority of its revenue. For now, Firefox seeks independence for the web while remaining financially dependent on its dominant competitor.

But to expand beyond the relatively small market share it now has, Firefox has to inspire users to actively select it over incumbents by providing a better browsing experience; most people don’t care whether Chromium dominates, and most have never heard of Gecko.

In our conversation, Varma expressed hope and ambition that these modernizations will help more users choose Firefox for its merits as a product. We also discussed the Firefox team’s competing priorities, its development resources, AI features and tooling, the general browser market, and more.

## A conversation with Ajit Varma

_This interview has been edited for length and clarity._

_**Ars Technica**: It’s nice to see a bit of modernization of the design of Firefox. But what problems does this redesign solve? How does it advance browser choice and the open web beyond just being a browser that’s a little more appealing and a little easier to use?_

**Ajit Varma**: Yeah, I think there’s been a lot of questions around, “What are we doing this at the cost of?” Like should we be focused on performance? Should we be focused on compatibility?

We are trying to do all of the above and work faster, and I think that’s one of the challenges that Firefox had in the past, was there was slow decision-making. There was a lot of debate, and in the last like year and a half, we’ve actually been trying to say, can we get a lot more velocity, and compete? And part of this is made possible by AI tools, to be honest with you. We are able to do a lot more.

People want to feel like they’re in a modern browser—things that match the design language of the operating system. So that’s part of it. We are bringing back compact mode as well… and we also have launched more customization options.

There’s a lot of functionality that’s been built to give all the modern productivity things that people wanted, and those are all very utilitarian, but it’s also the emotional connection, and do people feel like it’s a browser that feels modern as well.

_**Ars**: Sure, I’m happy to see it. But right now, I would guess most users pick Firefox as almost a values statement, right? That’s not always the same thing as thinking it’s the most effective or enjoyable browser to use. And not everyone even cares about that values question, right? So are you trying to win users over by providing superior features and a better experience to become everyone’s browser? Or are you just trying to build the best browser for a particular audience with a certain set of values?_

**Varma**: We are focused on building the best browser for a wide group of people. I agree with you that there is a subset of people who really understand the importance of competition and choice in a browser engine. When people look at a lot of competitive browsers, they are built on top of Chromium, and there’s a lot of risks to that. For me personally, that is the reason that I work at Firefox and work on Gecko; it’s because I don’t want this consolidation to exist that destroys all the things that we love about an open Internet.

When we talk to a lot of users that are the broad set, people don’t understand, like, what is Chromium versus Blink versus Chrome, what is Gecko versus Firefox. A lot of people actually don’t even really know what the difference is between a search engine and a browser, and it’s all conflated.

So the reality is that even though I think a lot of our values are what drive us internally—this preservation of the open Internet—it’s hard for people to connect all those dots. Many of us people are like, well, does the browser feel enjoyable to use? And when I download it for the first time, does it feel special? Does it feel unique?

And that’s where we do have an opportunity to also differentiate against Chromium browsers. When you look at a lot of those projects, they feel all very similar because it is much easier to fork and make superficial changes than make deeper changes. But we get an advantage by owning the entire stack. We can actually make bolder changes.

I do think that we need to cater to more than just very educated and informed people, going for a mass audience that doesn’t care about Gecko versus Chromium.

_**Ars**: With that mass audience, you need it to even occur to them to change. How much of Firefox’s minority position right now is platform obstruction, how much is inertia, how much is Firefox’s own product execution, and how much of it is people picking their desktop browser to match what they’re using on mobile, where you’re not as competitive?_

**Varma**: We do see that when people have a moment to decide what they use, Firefox does really well. That kind of goes into your point around, like, consideration is actually the biggest barrier. A lot of people just don’t really consider what browser they use as an important decision. The reason we know this is because in Europe, you have choice screens on mobile. This is part of the Digital Markets Act. There’s a split second when you get a new device: here’s the list of browsers, what do you want to use? We see a lot of growth in Firefox since these choice screens were implemented because I think people know Firefox, they understand privacy values, and then that resonates with them.

The biggest indicator, though, of what browser someone uses is actually, what browser did they use last month? People just use what they were using before; they’re not taking this moment to consider. But the last year we’ve actually seen a lot of moments that cause people to start to consider what browser they use.

So some examples—Chrome went through with their deprecation of Manifest V2. Manifest V2 is basically a much more powerful extension system. And people were like, well, why did this decrease? Why didn’t they just fix the security vulnerabilities in Manifest V2? And it’s very clearly because of ad blockers. That was the reason to deprecate it. Whereas, Mozilla, we’re not maximizing for profits, we’re maximizing for user experience and browser experience, and we want people to have powerful extensions. So we noticed when that shutoff moment happened, there was a moment where people said, do you want the power of an engine to be able to dictate how I control my experience? Because once Chromium shut it off, Edge shut it off, all the Chromium browsers then shut off Manifest V2 support. We still support it, and so we saw a big surge of actual users who started using us.

Also, with AI controls, you see a lot of worries that people have with AI, and whether societal implications or my own personal experience, of whether I want to use it or not. And many browsers are pushing AI very heavily, because if you look at major browsers and they have their hierarchy of needs, they actually probably care more about AI adoption than they do about browser experience. And so there was a criticism around Edge becoming a Copilot app—Gemini is very forceful in its integration in Chrome—but neither Copilot nor Gemini are the main AI that people use. People use ChatGPT, people use Claude. And so our approach is all about choice.

So we built AI controls. It’s a prominent, top-level setting. People can turn it off if they don’t want it. People can set only certain features that they want, like translations. And so we’ve noticed a lot of people actually want that from Firefox. And so this is another consideration moment where someone is like, my browser is getting bloated, I want a choice. A lot of our strategy over the next year is really around, how do we create more and more consideration moments where people take that second to think of what browser they should use? So we think something like customization is more of a consideration.

_**Ars**: You mentioned that the best predictor of what browser someone’s going to use is what browser they were using last year. The browsers that people use are not just the ones they’re using on their personal devices. How important are schools, employers, and IT administrators to Firefox’s growth strategy? Does a consumer-focused redesign like this address what those decision-makers need?_

**Varma**: One of the biggest new investments that we’re making is actually building the tools that enterprises and schools need. So if you look at especially over the last year, I don’t think we’ve made as many public announcements, but we have a fairly sizable team that’s actually going after this area. Enterprises care a lot about other features like digital loss prevention, like manageability, the ability to have more controls. This is a big area.

The other thing that we’re seeing around this is there are more and more companies that care a lot about digital sovereignty, and they want tools that they have more confidence aren’t going to be under the control of any particular government that may have been viewed as antagonistic or more challenging to work with. In a lot of places in Europe, a lot of places in Asia, we’re actually seeing a lot of people reach out to us about, how do they use Firefox because of our open source nature.

We’re a global company. And we don’t have some of the same ability to control us because we don’t have all these other tentacles spread out. We can really just focus on building the best browser. The needs of enterprises and schools are very different, but it’s actually probably the biggest new area of investment that we’ve had over the last 12 months.

_**Ars**: You mentioned the idea of sovereignty for these enterprises, and another consideration under that umbrella is AI model choice. I know that’s a big emphasis with what you’re doing with the AI features in Firefox, so I do want to talk about AI for a minute. What signals suggest to you that AI features are in high demand, especially among the arguably privacy-conscious, maybe even a little bit old-school users that Firefox is known for? Is there a tension in investing so much in AI when one of Firefox’s key differentiators is the ability to block or decline it?_

**Varma**: The usage of AI is still a minority compared to the overall browser usage. Like, you have billions of people who are using a browser every day; there’s definitely not anywhere close to that using AI tools in a browser every day. In the future, though, you have different paths, and I think that there is a plausible path where for a lot of the productivity kind of use cases, people want the benefits of AI, and you’re starting to see that emerge—things like translations are AI, summarization, auto-grouping of your tabs in a more organized way.

The stance that we’re taking is we just want to make it easy for people to be in the state that they want to be in, but we’re not doing it in a way that is typical of VC-backed companies that are like, we’re gonna spend hundreds of millions of dollars and see what happens. We are much more thoughtful about it. We are looking at things like on-device models that are cheaper to run. We are looking at open source models. There’s this balance that we are definitely looking at in terms of investment.

But the thing I’d say is, we want people to have choice. For someone who is an AI skeptic who wants to turn all AI off, that’s fine, we’re not going to push you to use AI. Once you turn AI controls off we’re never going to prompt you to use any AI tools. If you are an AI dabbler and you want really private models, we’re gonna give you that choice. But then if you’re someone who really wants to have AI on autopilot and check a price for you, or check if a new product is launching every day, and your browser goes and searches, well, that’s a convenience aspect that we think that a subset of people want for sure, that we want to provide that functionality to.

But one of the things that we do hear from people is people love auto-complete and suggest and stuff, and so we spent a lot of time on the non-AI version of that, which is, here’s an address, fill an address. But it goes to, well, what if you want your job application filled out? Those things are made better with on-device ML and AI that I don’t think people are equating to the AGI world, or you know, reinforced learning of bots that might take over the world and kill humans. This is like, we’re helping you fill in a form. That technically is still AI.

_**Ars**: I agree with you that some of those things are useful and a lot of people don’t even think about them as being AI. On the other hand, you have something like Smart Windows, which is AI-in-the-face, right? There is a lot of investment going into AI features that maybe could have gone to other things, like making the mobile app better. How do you manage the tension where you have a significant portion of your audience who just don’t care about this, but then, you look at your product roadmap and there’s a lot of AI stuff in there and there’s people working on that AI stuff?_

**Varma**: I think that there’s probably speculation, because I don’t know that we disclose how much our allocation to each area is. But I think that we need to make bets. But the number of engineers that we have working on this versus all the other stuff is less than 10 percent of the overall engineering. The core and the biggest investment that we have is on Gecko.

That’s things like performance, web compatibility, new APIs for developers, and I think some of those things are just harder for people to notice… but historically, I do think that one of the mistakes that Mozilla made 15 years ago was, it didn’t invest in mobile apps early enough. The bread and butter was desktop, and it was, let’s focus on desktop, desktop, desktop. And then mobile turned into a big opportunity that I think in retrospect was something that could have been invested in more.

Now, Mozilla did try something—the Firefox OS to build HTML apps. It tried this very ambitious, can you create a competitor to Android and iOS? I think in this approach, we’re not doing that.

So you could imagine that one world is: we’re going to build our own AI models, we’re going to build our own agents. And that’s where I think a lot of the expensive investment is, but we’re not doing any of that. We’re using open source models. We’re not building AI, but we’re applying AI to building tools that we think would benefit people. We’re not an AI company, we’re not pushing AI, but there are real benefits that AI can have to certain productivity use cases.

And then the other side of it is a conversation that we have: What do people use browsers for in the future? We do think that there are gonna be entertainment use cases plus productivity use cases. AI will help with the productivity use cases, but the browser core is still gonna really be needed for the entertainment cases. Ninety percent of our attention is still very focused on those core fundamentals.

_**Ars**: What is the actual path to Gecko on iPhone? Apple now provides routes for alternative engines in the EU and Japan. Which remaining obstacles are Apple’s requirements, and which ones are engineering cost restrictions?_

**Varma**: The biggest challenge for us is, we’re not a big tech company, so for us, forking to build two different versions of iOS, one for markets where this is possible and then for markets where it’s not possible, would mean we would basically have to double the size of our iOS team. And so what we’ve been pushing on Apple and regulators is, can we have a single set of global rules that allows us to build Gecko across the world?

I think it’s great, what’s happened in certain markets, but the reality is, it’s very challenging for us to actually invest to create this global, forked system. There are also just limitations like, well, how do you appear in the App Store? You can only have a single app. There are challenges of how you do migration and stuff that are also there. But I think the primary challenge is still that the cost goes up pretty significantly to have to build two totally different builds on iOS.

_**Ars**: Speaking of cost and revenue, Firefox is dependent on its search deal with Google. There’s the concern that if that ends, Firefox may be in a tougher spot. But also, longer term, do you worry about your dependence on Google search revenue in a time of rapid change with LLMs that could bring into question Google’s long-term search dominance?_

**Varma**: This is definitely a big question. I don’t think anyone really knows what’s gonna happen in the long term, but in the short term I’d say that I think competition is great—it’s why I work on Firefox. It would be great for there to be legitimate competitors to Google, which I think is the right outcome for consumers. I think it’s the best outcome for Firefox.

But in the short term, Google is doing really well, and so when we look at it as the power of AI and LLMs, it doesn’t mean yet that people are moving from Google searches over to LLMs. It actually is growing the overall pie. Search queries and monetizable queries are actually going up. Google’s also integrating AI Mode pretty deeply into search results. And again, this goes into techies versus the average person out there. For the average person, the muscle memory of going to Google is still very strong.

I don’t know how that’ll play out over the next several years. AI is going to have these kinds of questions, but also it’s helping us accomplish a lot more and become a lot more efficient than I think we ever thought was possible, and so for us being a smaller company, the bottleneck is not code creation anymore. We can create tons of code. It’s actually code review.

My hope is that we can actually compete with organizations much bigger than us, which has always been a constraint. These tools are very expensive, but my hope is they get commoditized so our cost structure doesn’t go up.

So I don’t know how it’ll play out, but I would also say that’s why I would encourage everyone to use Firefox. The more people use Firefox, the more power I think we have to negotiate, the more power that we have to create balance and competition and protect the web. So that goes back into something you started off with: the values-based reasons to use Firefox and Gecko. I think it’s pretty important.

## Takeaways

[![Vertical tabs on a web browser](https://cdn.arstechnica.net/wp-content/uploads/2026/09/Firefox-design-1024x576.jpg)](https://cdn.arstechnica.net/wp-content/uploads/2026/09/Firefox-design.jpg)

A Mozilla-provided image of the new styling in the Firefox redesign.

Credit: Mozilla

A Mozilla-provided image of the new styling in the Firefox redesign. Credit: Mozilla

Firefox’s new redesign is—at least to me—a welcome one. It no longer looks like a browser from 2015. That was probably never what mattered most to someone who uses the browser in part as a mission statement about the value of the open web. It does, however, make the browser more palatable in a culture and market that is currently seething with frustration at Big Tech’s dominance, and in one that (at least in some regions) is taking regulatory measures to ensure users have choices when faced with the usual defaults.

As Varma tells it, AI-assisted coding workflows have enabled Mozilla to accelerate development. That’s a clear boon, provided the Firefox team (and most other software development teams in the world, for that matter) can work out its post-AI-overhaul code review challenges. That said, when I spoke to Forrester analyst Paddy Harrington, he argued that isn’t necessarily a de facto advantage for the software world’s Davids against its Goliaths. Goliath can use coding agents, too. “If large companies like Apple, Google, and Microsoft aren’t using AI within their dev processes, then I’ll eat my hat, as the old saying goes,” he said. “The question is what are they using it for? How are they using it differently than any other company who is using AI tools in their dev process?”

Given Varma’s statement that tools for enterprise deployments have been Firefox’s most significant new investment area over the past year, I also asked Harrington for his perspective on Firefox’s opportunity in the enterprise space. “I’d certainly love to see them come back with new things that expands them in the enterprise, but it’s not going to be easy, and they would have to truly wow IT decision makers,” he said. Insomuch as there is a clear opening, it’s with businesses in Europe, where “we’re seeing interesting moves in those countries where they’re looking to move away from some of the platform giants like Microsoft or Google,” according to Harrington.

Whatever the scope of the enterprise opportunity, Varma is right that the more people use Firefox, the more leverage it has and the more true independence becomes plausible. This new redesign aims to make the browser more appealing in the mass market, and that’s a welcome start, but it’s not the finish line, and there’s a long way to go against competitors with more resources, albeit also with muddier incentives.

Maybe engine independence creates freedom to differentiate, as Varma said, and maybe AI coding tools do give smaller teams more power to stand up to well-resourced incumbents. But even so, Mozilla will have to continue to turn that freedom and capability into improvements that give people a reason to switch.

[![Photo of Samuel Axon](https://cdn.arstechnica.net/wp-content/uploads/2025/11/photo1-300x300.jpeg)](https://arstechnica.com/author/samuelaxon/)

Samuel Axon is the editorial lead for tech and gaming coverage at Ars Technica. He covers physical and generative AI, large language models, software development, gaming, entertainment, and mixed reality. He has been writing about gaming and technology for nearly two decades at Engadget, PC World, Mashable, Vice, Polygon, Wired, and others. He previously ran a marketing and PR agency in the gaming industry, led editorial for the TV network CBS, and worked on social media marketing strategy for Samsung Mobile at the creative agency SPCSHP. He also is an independent software and game developer for iOS, Windows, and other platforms, and he is a graduate of DePaul University, where he studied interactive media and software development.

[289 Comments](https://arstechnica.com/gadgets/2026/09/mozillas-head-of-firefox-talks-product-priorities-ai-skepticism-and-browser-choice/#comments "289 comments")

1.  [![Listing image for first story in Most Read: Review: 4-hour Musk documentary feels like two different films](https://cdn.arstechnica.net/wp-content/uploads/2026/10/musk3-500x500.jpg)](https://arstechnica.com/culture/2026/10/review-4-hour-musk-documentary-feels-like-two-different-films/)
