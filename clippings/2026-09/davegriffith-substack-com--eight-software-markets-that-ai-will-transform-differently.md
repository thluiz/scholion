---
url: "https://davegriffith.substack.com/p/eight-software-markets-ai-that-will?utm_source=tldrai"
captured_at: "2026-09-24T23:32:03+01:00"
title: "Eight Software Markets That AI Will Transform Differently"
domain: "davegriffith-substack-com"
---

Chris Loy recently published a thoughtful piece called [“The Rise of Industrial Software”](https://chrisloy.dev/post/2025/12/30/the-rise-of-industrial-software) that asks the right questions about what impact agentic coding is tools will have on the quality and quantity of software produce. He draws on Jevons paradox, an economic construct about just how markets change the cost of production drops, and shows historical parallels to changes in markets for agriculture, textiles, and even the printed word. He refers to this as “industrial” software, and expects increases in the amount of software produced, and decreases in the it’s quality.

It’s good work, and you should read it. But it has a blind spot.

Loy treats software as a single commodity undergoing uniform transformation. It’s not. Software is produced in at least eight distinct markets, each with different constraints, different demand elasticities, and different relationships to the factors that AI coding actually changes. Predicting what happens to “software” is like predicting what happens to “transportation”—the answer for container shipping is different from the answer for bicycle commuting.

(Also, anyone who uses “industrial” as a pejorative stop-word should have to plow fields behind a mule for a few days. Industrialization fed billions of people and freed them from backbreaking labor. The romanticization of pre-industrial craft production is suspiciously prevalent in only in people who’ve never had to do it at scale.)

For each software market, we need to ask: **What currently constrains production, and how does agentic coding change that constraint?**

If the constraint is implementation skill, AI helps a lot. If the constraint is domain knowledge, AI helps less. If the constraint is organizational politics or regulatory approval, AI might not help at all—and might actually make things worse.

Jevons paradox—the observation that increased efficiency in resource use can lead to _higher_ total consumption—only applies when demand is elastic, which economist-speak for “people would like more of it, please”. When cars got more fuel-efficient, miles driven and total fuel consumed increased because people were previously driving much less than they wished to because of the cost. But if demand is inelastic, this doesn’t occur. No matter how cheap clean drinking water gets, you’re only going to drink so many glasses per day. When demand is constrained by something other than production cost, cheaper production doesn’t increase volume. It just changes who captures the surplus.

With that frame, let’s walk through the markets.

Every ops team has a spreadsheet that should be an app. Every department has a “someday” project that never gets prioritized because developer time gets allocated to revenue-generating work. The backlog of useful-but-not-flamingly-urgent internal tooling is enormous and largely invisible—it lives in feature requests that never get scheduled, in workarounds that everyone complains about, in information sources that never quite get integrated.

*   **Current constraint:** Developer time is expensive and usually targeted toward product priorities
    
*   **AI impact:** The backlog becomes buildable.
    
*   **Jevons applies:** Strongly. Latent demand is vast and real
    
*   **Quality expectation:** Bifurcated—quick wins get vibe-coded, critical path stays careful
    

This is where “disposable software” actually makes sense. If the ops dashboard breaks, you regenerate it, and have the robot toss in a few more healthchecks and auto-diagnostics while you’re there. The data export script doesn’t need to be maintained for a decade, it just needs to last for the course of the Q2 marketing campaign. The internal tool that three people use can be rebuilt faster than it can be documented.

The interesting dynamic here is political, not technical. IT departments have historically controlled software production as a power base. When anyone can generate a working tool, that control erodes. Expect turf wars dressed up as security or performance concerns.

This is where a sizable plurality of professional developers work, and where the “industrial software” framing seems most applicable. Surely if any market is ripe for Jevons-style explosion, it’s the one with the most competitive pressure?

Not so fast.

*   **Current constraint:** Competition, talent acquisition, time-to-market—but market size is relatively fixed
    
*   **AI impact:** Faster iteration, but competitors have the same tools. Red Queen’s Race dynamics
    
*   **Jevons applies:** Weakly. The market for CRM software doesn’t grow just because CRMs are cheaper to build.
    
*   **Quality expectation:** Pressure toward feature velocity over correctness. “Ship it, we’ll fix it” intensifies. As a counterbalance to this, user experience may improve due to AI-driven automation in the design space and customer desire for “Apple-like” usability.
    

The enterprise SaaS market is not constrained by the cost of building software. It’s constrained by customer acquisition costs, switching costs, and the pace at which enterprises can absorb change. There’s a reason why the predominant sales motion in this space is “land-and-expand”. Making production cheaper doesn’t expand the market—it just accelerates the arms race among existing players.

What AI coding _does_ change is the competitive dynamics. Incumbents can iterate faster, but so can challengers. The moat of “we have more engineers” becomes less defensible. Whether this leads to consolidation (big players absorb productivity gains) or fragmentation (niche players become viable) is genuinely unclear. For extra bonus confusion nachos, the companies producing AI models and tools are themselves SaaS players of one sort or another, so these same dynamics are playing out there.

Before photography, almost no one made images. The only way to create images was painting, and it required enormous amounts of training, skill, and usually elite patronage. After photography, everyone makes images constantly. The snapshot, the family album, the selfie—none of this was “professional” image-making, and none of it displaced professional work (the elites still have paintings on their walls, not photographs). It was a new category that couldn’t exist before. We should absolutely expect that agentic coding will create a similar democratization.

*   **Current constraint:** Skill barrier to entry. You need to know how to code, and have access to all of the necessary infrastructure to build and deploy what you want to build
    
*   **AI impact:** Barrier collapses. Non-programmers make software for themselves
    
*   **Jevons applies:** Absolutely. This market barely exists today; it’s about to explode
    
*   **Quality expectation:** Irrelevant. If my personal script breaks, I regenerate it
    

This is _vernacular software_—software made by non-programmers for personal use, with no expectation of maintenance, sharing, or durability. It’s the computational equivalent of a grocery list or a journal entry.

Did I need to create a custom web scraper to keep me up to date with scientific papers in my areas of interest from Arxiv, NBER, and some other repositories? Probably not. But it only took twenty minutes to build one so why wouldn’t I? I think it’s in Typescript, but I could be misremembering. As I write this, my wife (the lovely Brenda) is sitting next to me having Claude create a Python script for creating an index and table of contents for the reissue of one of her books, while sitting on a ship off of Aruba drinking sangria. Brenda has many great skills and interests, ranging from kiln-formed glass to horsemanship to beekeeping, but software development is absolutely not one of them.

We don’t have good language for this yet. “Vibe coding” is a dismissive and frankly horrible term. “Prompt-driven development” is clinical, and probably won’t accurately describe the mechanics of software development for much longer. But whatever we call it, it’s coming, and it represents a genuine expansion of who participates in software creation. Small pieces of software development will start being something that people just do. Expect transitional scenes similar to pirate radio, the ‘zine explosion of the 80s, or the formative days of hip-hop in strip clubs, ripe with the joy of newly possible creation.

I sometimes style myself a “feral academic”, who fled the ivy-coated walls for things like “money” and “living in desirable places” and “passable mental health”. As such, I’ve seen enough academic software to know the baseline: it’s pretty much universally terrible. Written by sad, sad graduate students[1](#footnote-1) who are experts in biology or physics but had to sort-of learn Python last semester, as though they didn’t have enough problems. These programs are optimized for “get the thesis done” rather than “anyone else will ever run this.” Documentation is whatever comments survived the deadline crunch. It’s software written by people who desperately need software and have no idea what quality software means or how to achieve it.

*   **Current constraint:** Intensely labor constrained. Researchers aren’t trained or incented as developers; software is a means to an end
    
*   **AI impact:** Scientists can focus on science, let AI handle the quality
    
*   **Jevons applies:** Yes. Lots of unbuilt analysis tools, simulations, visualizations
    
*   **Quality expectation:** _Improves_, because the floor is embarrassingly, often degradingly low
    

This might be the market where AI coding is most unambiguously positive. Reproducibility improves if code is more standardized, and if robots can handle the work of making the source code accessible and reusable, that could be an enormous win. Researchers can explore more variations of their analyses. The sad, sad grad student can focus on the science instead of debugging gplot parameters.

An interesting question is whether this helps or hurts the replication crisis. More reproducible code is good. But more automated analysis means more researcher degrees of freedom, more p-hacking, more “I ran it until it worked.” The tool is neutral; the incentives are sadly still not. With luck, this be counter-balanced by AIs capable of recognizing and critiquing methodological issues.

Games are already comfortable with procedural generation. Roguelikes, procedural levels, AI-driven NPCs—the industry has been exploring “let the computer create content” for decades. AI coding is just more of the same, extended to the code itself.

*   **Current constraint:** Content production cost (art, writing, sound, level design) as much as code
    
*   **AI impact:** Applies to the whole pipeline, not just code. Indie explosion possible
    
*   **Jevons applies:** Strongly. Humanity has an apparently infinite appetite for new games
    
*   **Quality expectation:** Massive expansion of the long tail. More games, mostly mediocre but with some brilliant outliers
    

Four-eight games ship on [Steam](https://steamdb.info/stats/releases/) per day. That number is unlikely go down.

The pattern will likely echo what happened with YouTube and music production: vastly more content, a small number of breakout successes, a long tail of niche work that finds small audiences, and a flood of useless dross to navigate. The economics favor platform owners (Steam, app stores) over individual creators, unless you can build an audience directly.

What’s different about games is that quality matters in a particular way—games need to be _fun_, which is hard to specify in a prompt. The AI can generate code for game mechanics, but “is this actually enjoyable to play?” requires human judgment and iteration. The creative bottleneck moves from implementation to design.

As is so often the case, there is no good news here.

*   **Current constraint:** Budget, procurement, risk aversion, contractor lock-in, political dysfunction
    
*   **AI impact:** Minimal in the short term. Same procurement structures, same risk calculus
    
*   **Jevons applies:** Weakly. Demand is inelastic and politically allocated
    
*   **Quality expectation:** Probably unchanged. The constraint isn’t production cost
    

Government software is not slow and expensive because coding is hard. It’s slow and expensive because procurement rules optimize for audit trails over outcomes, because contractors are incentivized to bill hours rather than ship features, because risk aversion means nobody wants to be blamed for a new approach that fails.

AI coding changes none of this, other than super-charging the risk aversion.

On the other hand, [various](https://opencommons.org/CHAOS_Report_on_IT_Project_Outcomes#:~:text=U.S.%2DSpecific%20Figures,M\)%20succeed%20%5B5%5D.) [studies](https://www.pwc.ch/en/publications/2017/pmi-are-public-projects-doomed-to-failure-en-2017.pdf) [place](https://www.mckinsey.com/industries/public-sector/our-insights/unlocking-the-potential-of-public-sector-it-projects#:~:text=Extreme%20cost%20overrun%20is%20higher%20for%20public%2Dsector%20IT%20projects&text=Planning%20four%20years%20into%20the,projects%20that%20are%20over%20budget.) the failure rates of government software projects in the 50%-80% range, so it’s not like agentic coding practices could realistically make matters much worse.

What might change is the leverage of small, motivated teams within government who can use AI to build things faster than the official process would allow. Skunkworks projects. Prototypes that prove concepts. Projects where newly minted “governmental CTOs” put their thumbs on the scale. But these exist at the margins; the core dysfunction is institutional, not technical.

Prediction: Government lags the AI coding transition by 5-10 years, creating a widening capability gap with the private sector. Bad for society, but it’s nice steady indoor work if you’re that sort.

Here’s where the optimism stops.

Medical devices. Avionics. Industrial control systems. Automotive software. These domains have something in common: the code can kill people, and regulators know it. Certification processes exist precisely to ensure that humans understand what the software does and can defend its correctness.

*   **Current constraint:** Certification, testing, liability, long product lifecycles
    
*   **AI impact:** Potentially _negative_. Regulators don’t know how to certify AI-generated code
    
*   **Jevons applies:** No. Demand is largely tied to physical products, not embedded code economics
    
*   **Quality expectation:** Might _decline_ temporarily as pressure to ship faster meets irreducible safety requirements, and fewer humans gain the skills to code without AI assistance.
    

“Explain how this works” is already a hard requirement in safety-critical domains. AI-generated code makes it harder to satisfy. The black-box nature of LLM output is antithetical to the transparency that certification requires.

This is the domain where “who maintains software nobody understands” is most dangerous. A vibe-coded internal dashboard can fail gracefully. A vibe-coded pacemaker cannot.

My prediction: Safety-critical software will be among the _last_ domains to adopt AI coding extensively, and will require new certification frameworks that don’t yet exist. The only glimmer of hope here is that advanced formal methods might someday be LLM-automatable, enabling agentic tools to produce code that is provably correct, mathematically.

Finally, the domain where speed matters most and long-term thinking matters least.

*   **Current constraint:** Time, founder technical ability, runway, speed of iteration
    
*   **AI impact:** Non-technical founders can prototype. Technical founders move faster. Teams can be smaller (down to the limit of sole developers) and more nimble
    
*   **Jevons applies:** Yes. Lower barriers mean more swings of the bat
    
*   **Quality expectation:** Lower floor, but that’s fine—MVPs are supposed to be barely working, that’s what the “M” means.
    

This is probably the area where agentic coding has advanced the fastest. Even in the distant early days of Claude Code back in, um, July, 25% of the startups going through YCombinator bootcamp were already producing >95% of their code with agentic tools.

The interesting question is what this does to the value of technical co-founders. Historically, a non-technical founder needed a technical partner to build anything. If AI coding lets non-technical founders prototype independently, does the technical co-founder become less essential? Or does the ability to _evaluate_ AI output—to know when the generated code is subtly wrong—become the new scarce skill?

I suspect the latter. The person who can look at AI-generated code and say “this will break at scale” or “this has a security hole” is more valuable than ever. The judgment layer doesn’t automate away. Expect a fair number of current silverback engineers to chase side-gigs as “fractional CTOs” (I’ve considered it myself).

Let’s be precise. Jevons paradox requires elastic demand—people wanting more of something when it gets cheaper. Looking across our eight markets:

**Strong Jevons effect:**

*   Enterprise internal tools (huge latent backlog)
    
*   Personal/hobbyist (new market entirely)
    
*   Games/entertainment (infinite appetite)
    
*   Academic research (lots of unbuilt tooling)
    
*   Startups/MVPs (lower barriers = more attempts)
    

**Weak or no Jevons effect:**

*   Enterprise SaaS (market size is demand-constrained, not supply-constrained)
    
*   Government/nonprofit (institutional dysfunction is the binding constraint)
    
*   Safety-critical (regulatory and physical constraints dominate)
    

The “industrial software” narrative implicitly assumes the first category dominates. It doesn’t. A huge amount of economically significant software lives in the second category, where AI coding changes _how_ things are built without changing _how much_ gets built or at what quality.

If you’re an embedded systems engineer, your world isn’t changing as fast as Twitter suggests. If you’re building enterprise SaaS, you’re in an arms race where everyone got the same weapons. If you’re a researcher, this might be the best thing that’s happened to your workflow in decades.

The strategic question isn’t “how does AI change software?” It’s “which market am I in, and what are its specific dynamics?” Changes to production costs will cause enormous changes in who makes money from software, with possible answers that may very well include “notably fewer professional software engineers”

Loy asks: “Who maintains the software that no one owns?”

It’s a good question, but it’s incomplete. The fuller version is: “In which markets does maintenance matter, and in which can we afford or even welcome disposability?”

For vernacular software, disposability is a feature. For safety-critical systems, it’s terrifying. The answer isn’t uniform because the problem isn’t uniform.

Industrialization isn’t one thing. Neither is its software equivalent.

_This post was constructed with the able assistance of Claude Opus 4.5, who is basically to blame for all of these changes. Additionally, the arguments in this post were vetted and improved using the Future Tokens set of Claude Skills, developed by Jordan Rubin and available [here](https://github.com/jordanrubin/future_tokens/)._

[1](#footnote-anchor-1)

There are almost no happy graduate students. Stumbling across one is jarring, like meeting a generous banker or an introverted politician.
