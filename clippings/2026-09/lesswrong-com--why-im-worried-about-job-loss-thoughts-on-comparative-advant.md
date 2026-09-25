---
url: "https://www.lesswrong.com/posts/YPJHkciv6ysgsSiJC/why-i-m-worried-about-job-loss-thoughts-on-comparative?utm_source=tldrai"
captured_at: "2026-09-25T22:30:18+01:00"
title: "Why I'm Worried About Job Loss + Thoughts on Comparative Advantage"
domain: "lesswrong-com"
---

David Oks published a well-written essay [yesterday](https://davidoks.blog/p/why-im-not-worried-about-ai-job-loss) arguing that the current panic about AI job displacement is overblown. I agree with a few of his premises (and it’s nice to see that we’re [both fans](https://substack.com/@claypapertiger/p-181379561) of Lars Tunbjörk), but disagree with most of them and arrive at very different conclusions. I see other economists with similar views to Oks, so I thought it would be best to illustrate my perspective on econ/labor and why I choose to research gradual disempowerment risks.

My main claim is simple: it is possible for Oks to be right about comparative advantage and bottlenecks while still being wrong that "ordinary people don't have to worry." A labor market can remain "employed" and still become structurally worse for workers through wage pressure, pipeline collapse, and surplus capture by capital.

I'm writing this because I keep seeing the same argumentative move in AI-econ discourse: a theoretically correct statement about production gets used to carry an empirical prediction about broad welfare. I care less about the binary question of "will jobs exist?" and more about the questions that determine whether this transition is benign: **how many jobs, at what pay, with what bargaining power, and who owns the systems generating the surplus.**

Oks' points are as follows:

### **1: Comparative Advantage Preserves Human Labor**

_“...Labor substitution is about comparative advantage, not absolute advantage. The question isn’t whether AI can do specific tasks that humans do. It’s whether the aggregate output of humans working with AI is inferior to what AI can produce alone: in other words, whether there is any way that the addition of a human to the production process can increase or improve the output of that process."_

Oks brings the Ricardian argument here, and I think it's directionally correct as a description of many workflows today. We are in a "cyborg era" in which humans plus AI often outperform AI alone, especially on problems with unclear objectives or heavy context. But I don't think the comparative advantage framing does the work Oks wants it to do, because it leaves out the variables that determine whether workers are "fine." 

First, comparative advantage tells you that _some_ human labor will remain valuable in _some_ configuration, but nothing about the wages, number of jobs, or the **distribution of gains**. You can have comparative advantage and still have massive displacement, wage collapse, and concentration of returns to capital. A world where humans retain “comparative advantage” in a handful of residual tasks at a fraction of the current wages is technically consistent with Oks’ framework, but obviously is worth worrying about and is certainly not fine.

Another issue with the comparative advantage framing (and I think this is a problem with most AI/econ forecasting) – it implicitly assumes that most laborers have the kind of tacit, high-context strategic knowledge that complements AI. The continuation of the “cyborg era” presupposes that laborers have something irreplaceable to contribute (judgement, institutional context, creative direction). I agree with this for some jobs, but it’s not enough for me to avoid being worried about job loss.

Under capitalism, firms are rational cost-minimizers. They will route production through whatever combination of inputs delivers the most output per dollar (barring policy). Oks and David Graeber’s “[Bullshit Jobs](https://davidgraeber.org/articles/on-the-phenomenon-of-bullshit-jobs-a-work-rant/)” thesis agree on the empirical point that organizations are riddled with inefficiency, and many roles exist not because they’re maximally productive but because of social signaling and coordination failures. Oks treats this inefficiency as a buffer that protects workers. But if a significant share of existing roles involve codifiable, routine cognitive tasks, then they’re not protected by comparative advantage at all. They’re protected by social capital and organizational friction, the latter of which I believe will erode (and we’ll discuss later).

Oks links some evidence that demonstrates protection from displacement  – I’ll admit that the counter-evidence so far is inconclusive and contaminated by many other economic factors. I will bring up Erik Brynjolfsson’s “[Canaries in the Coal Mine](https://digitaleconomy.stanford.edu/app/uploads/2025/11/CanariesintheCoalMine_Nov25.pdf)” study, because I think it exemplifies the trend we’ll continue seeing in the next 2-3+ years before AGI.

Brynjolfsson analyzed millions of ADP payroll records and found a 13% relative decline in employment for early-career workers (ages 22-25) in AI-exposed occupations since late 2022. For young software developers specifically, employment fell almost 20% from its 2022 peak. Meanwhile, employment for experienced workers in the same occupations held steady or grew.

So what’s the mechanism at play? AI replaces _codified knowledge_ – the kind of learning you get from classrooms or textbooks – but struggles with _tacit knowledge_, the experiential judgement that accumulates over years on the job. This is why seniors are spared and juniors are not. But Oks’ thesis treats this as reassurance: _see, humans with deep knowledge still have comparative advantage!_ I believe this is more of a senior worker’s luxury, and the protection for “seniors” will move [up and up the hierarchy over time](https://intelligence-curse.ai/pyramid/).

Some other stats (again, not totally conclusive but worthy of bringing up):

1.  [Youth unemployment hit 10.8% in July 2025](https://www.bls.gov/news.release/youth.nr0.htm), the [highest rate since the pandemic](https://econofact.org/factbrief/fact-check-is-unemployment-for-young-us-workers-the-highest-since-the-pandemic), even as overall unemployment remained low.
2.  [Entry-level job postings](https://www.cnbc.com/2025/09/07/ai-entry-level-jobs-hiring-careers.html) across the U.S. declined roughly 35% between January 2023 and late 2024.
3.  [New graduate hiring](https://restofworld.org/2025/engineering-graduates-ai-job-losses/) at major tech companies dropped over 50% between 2019 and 2024, with only 7% of new hires in 2024 being recent graduates.
4.  A [Harvard study corroborated](https://fortune.com/2025/09/04/ai-entry-level-jobs-uncertainty-college-grads/) these findings: headcount for early-career roles at AI-adopting firms fell 7.7% over just six quarters beginning in early 2023, while senior employment continued its steady climb.

This is a disappearance of the bottom rung of the career ladder, which has historically served a dual function: producing output _and_ training the next generation of senior workers. Oks may point to other sources of employment (yoga instructors, streamers, physical trainers), or indicate that entry-level hiring is slowing down due to other economic forces, but I’ll ask: will the entire generation of incoming college graduates, who are rich with codified knowledge but lacking in tacit knowledge, all find AI-complementary roles? Or will firms slow hiring and enjoy the productive pace of their augmented senior employees? How high are labor costs for entry-level grads compared to the [ever-reducing cost of inference](https://epoch.ai/data-insights/llm-inference-price-trends)?

### **2: Organizational Bottlenecks Slow Displacement**

_“People frequently underrate how inefficient things are in practically any domain, and how frequently these inefficiencies are reducible to bottlenecks caused simply by humans being human… Production processes are governed by their least efficient inputs: the more productive the most efficient inputs, the more the least efficient inputs matter.”_

This is the strongest part of the essay and overlaps substantially with my own modeling work. The distance between technical capability and actual labor displacement is large, variable across domains, and governed by several constraints independent of model intelligence. The point about GPT-3 being out for six years without automating low-level work is good empirical evidence, though I don’t agree that GPT-3 or GPT-4 era models could automate customer service (they would need tool usage, better memory,  and better voice latency to do that).

Where the analysis is lacking is in treating bottlenecks as if they’re static features of the landscape rather than obstacles in the path of an accelerating force. Oks acknowledges that they erode over time but doesn’t discuss the rate of erosion or that AI itself may accelerate their removal.

The example below is likely overstated, but this is the worst Claude will ever be – are any of these agentic decisions something that we would previously classify as organizational friction?

![Image](https://res.cloudinary.com/lesswrong-2-0/image/upload/f_auto,q_auto/v1/mirroredImages/YPJHkciv6ysgsSiJC/gwyi940u5shsgjdhelko)

In my own modeling, I estimate organizational friction coefficients for different sectors and job types. The bottleneck argument is strong for 2026-2029, but I think it’s considerably weaker for 2030-2034. Oks brings up the example of electricity taking decades to diffuse but admits that the timeline isn’t similar. I would agree, it's not similar, and the data is increasingly pointing towards a compressed S-curve where adoption is slow until it isn’t.

Oks’ bottleneck argument is entirely about _incumbents_ – large, existing firms with accumulated infrastructure debt. What happens when AI-native organizational structures compete with those legacy enterprises? The infrastructure bottleneck is a moat that only protects incumbents until someone flies over it.

### **3: Intelligence Isn’t the Limiting Factor, and Elastic Demand Will Absorb Productivity Gains**

_“The experience of the last few years should tell us clearly: intelligence is not the limiting factor here… even for the simplest of real-world jobs, we are in the world of bottlenecks.”_

_“Demand for most of the things humans create is much more elastic than we recognize today. As a society, we consume all sorts of things–not just energy but also written and audiovisual content, legal services, ‘business services’ writ large–in quantities that would astound people living a few decades ago, to say nothing of a few centuries ago.”_

Here I’ll lean a little bit on Dean W. Ball's [latest](https://www.hyperdimensional.co/p/on-recursive-self-improvement-part) [pieces](https://www.hyperdimensional.co/p/on-recursive-self-improvement-part-d9b) on recursive self-improvement as well as some empirical evidence of job loss. Oks writes as though we haven’t seen meaningful displacement yet – I would say we have, within the limited capabilities of models today.

Beyond the entry-level crisis discussed earlier, displacement is already hitting mid-career professionals across creative and knowledge work. See reports linked on [illustrators](https://www.bloodinthemachine.com/p/artists-are-losing-work-wages-and) and [graphic designers](https://bloomberry.com/blog/i-analyzed-180m-jobs-to-see-what-jobs-ai-is-actually-replacing-today/), [translators](https://edition.cnn.com/2026/01/23/tech/translation-language-jobs-ai-automation-intl), [copywriters](https://bloomberry.com/blog/i-analyzed-180m-jobs-to-see-what-jobs-ai-is-actually-replacing-today/), and [explicitly AI-related](https://www.cnbc.com/2025/12/21/ai-job-cuts-amazon-microsoft-and-more-cite-ai-for-2025-layoffs.html) corporate layoffs.

**The models doing this aren’t even particularly good yet.** These losses are happening with GPT-4-class and early GPT-5-class models; models that still hallucinate, produce mediocre long-form writing, can't design well, and can’t reliably handle complex multi-step reasoning. If _this_ level of capability is already destroying illustration, translation, copywriting, and content creation, what happens when we reach recursive self-improvement? There needs to be some more investigative work to see how displaced designers/translators/copywriters etc. are reskilling and finding new work, but I would estimate it’s extraordinarily difficult in this job market.

Notice the distributional pattern: it’s not the creative directors, the senior art directors, or the lead translators with niche expertise getting hit. It’s everyone below them; the juniors, the mid-career freelancers, the people who do the volume work. Oks’ comparative advantage argument might hold for the person at the top of the hierarchy whose taste and judgment complement AI, but it offers no comfort for the twenty people who work below that person.

Then, we’ll consider the capabilities overhang. We haven’t even seen models trained on Blackwell-generation chips yet, and models are reaching the ability to [build their next upgrades](https://thenewstack.io/openais-gpt-5-3-codex-helped-build-itself/). 

[Massive new data centers are coming online](https://epoch.ai/data/data-centers) this year. Oks’ point about “GPT-3 being out for 6 years and nothing catastrophic has happened” – is looking at capabilities from 2020–2025 and extrapolating forward, right before a massive step-change in both compute and algorithmic progress hits simultaneously. The river has not flooded but the dam has cracked.

Ball offers another good point in his essays – there is a difference between AI that’s faster at the same things versus AI that’s qualitatively different – a Bugatti going 300 instead of 200 mph vs a Bugatti that learns to fly. Oks’ entire analysis assumes incremental improvements that organizational friction can absorb. But, again, automated AI research raises the possibility of capabilities that route _around_ existing organizational structures rather than trying to penetrate them. An AI system that autonomously manages end-to-end business processes doesn’t need to navigate office politics and legacy systems.

As for the Jevons paradox argument (often cited); that elastic demand will absorb productivity gains. I believe it’s real for some categories of output but cherry-picked as a general principle. Software is Oks’ central example, and it’s well-chosen: software is elastic in demand because it’s a general-purpose tool. But does anyone believe demand for legal document review is infinitely elastic? For tax preparation? For freelance video editors? These are bounded markets where productivity gains translate fairly directly to headcount reductions, and I’m still struggling to understand how we are telling early-wave displaced roles to upskill or find new careers.

Someone commented under Oks’ post [another example](https://davidoks.blog/p/why-im-not-worried-about-ai-job-loss/comment/213726665) that I’ll jump on. As global manufacturing [shifted toward China](https://www.annualreviews.org/content/journals/10.1146/annurev-economics-080315-015041) and other low-cost production regions, total manufacturing output continued to expand rather than contract, a Jevons-like scale effect where cheaper production increased overall consumption. American manufacturing workers, however, bore concentrated losses. The gains flowed disproportionately to consumers, firms, and capital owners, while many displaced workers (especially in Midwestern industrial regions) faced long-term economic decline that helped fuel a broader political backlash against globalization.

We can also address a concrete case – AI video generation. Models like Veo 3.1 and [Seedance 2.0](https://www.ctol.digital/news/seedance-2-bytedance-ai-video-generator-beats-sora-automates-film-editing-threatens-creative-jobs/) are producing near-lifelike footage with native audio, lip-synched dialogue, and most importantly, _automated editorial judgement_. Users upload reference images, videos, and audio, and the model assembles coherent multi-shot sequences matching the vibe and aesthetic they’re after. Seedance 2.0 shipped this week.

The U.S. motion picture and video production industry [employs roughly 430,000 people](https://datausa.io/profile/naics/motion-pictures-video-industries) – producers, directors, editors, camera operators, sound technicians, VFX artists – plus hundreds of thousands more in adjacent commercial production: corporate video, social content, advertising spots, educational materials. The pipeline between “someone has an idea for a video” and “a viewer watches it” employs an enormous intermediary labor force.

Oks’ elastic demand argument would predict that cheaper video production simply means _more video_, with roughly equivalent total employment. And it’s true that demand for video content is enormous – [McKinsey notes](https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/what-ai-could-mean-for-film-and-tv-production-and-the-industrys-future) the average American now spends nearly seven hours a day watching video across platforms. But I would challenge his thesis: is the number of people currently employed between producer and consumer equivalent to the number who will be needed when AI collapses that entire intermediary layer? When a single person with a creative vision can prompt Seedance/Veo/Sora into producing a polished commercial that once required a director, cinematographer, editor, colorist, and sound designer, does elastic demand for the _output_ translate into elastic demand for the _labor_?

People _now_ can produce [polished AI anime](https://x.com/deedydas/status/2021497522674598199?s=20) for about $5-$100. This content exists but the workforce does not. So, yes, there will be vastly more video content in the world. But the production function has changed; the ratio of human labor to output has shifted by orders of magnitude. The demand elasticity is in the _content_, not in the _labor_.

To summarize: Jevon's paradox in _aggregate output_ is perfectly compatible with catastrophic _distributional_ effects. You can have more total economic activity and still have millions of people whose specific skills and local labor markets are destroyed. The people being displaced _right now_ are not edge cases, they’re illustrators, translators, copywriters, graphic designers, video producers, and 3D artists who were told their skills would always be valuable because they were “creative.” The aggregate framing erases these people, and it will erase more.

### **4: We’ll Always Invent New Jobs From Surplus**

_“We’ll invent jobs because we can, and those jobs will sit somewhere between leisure and work. Indeed this is the entire story of human life since the first agrarian surplus. For the entire period where we have been finding more productive ways to produce things, we have been using the surplus we generate to do things that are further and further removed from the necessities of survival.”_

This is an argument by induction: previous technological transitions always generated new employment categories, so this one will too. The premise is correct, the pattern is real and well-documented. I don’t dispute it.

The problem is the reference class issue. Every previous transition involved humans moving _up_ the cognitive ladder, like from physical labor to increasingly abstract cognitive work. Oks mentions this – agricultural automation pushing people into manufacturing, then manufacturing automation pushing people into services, then service automation pushing people into knowledge work. The new jobs that emerged were always _cognitive_ jobs. This time, the cognitive domain itself is being automated.

I don’t think this means zero new job categories will emerge. But Oks’ assertion that “people will find strange and interesting things to do with their lives” doesn’t address three critical questions: the _transition path_ (how do people actually get from displaced jobs to new ones?), the _income levels_ (will new activities pay comparably to what they replace?), and _ownership_ (will the surplus that enables those activities be broadly shared or narrowly held?). There’s also the entry-level → senior pipeline problem I mentioned earlier.

The gesture toward “leisure” as an eventual end state is telling. If human labor really does become superfluous, that’s not a world where “ordinary people” are okay by default, but rather a world where the entire economic operating system needs to be redesigned. Oks treats this as a distant concern. I’d argue it’s the thing most worth worrying about, because policy needs to be built _before_ we arrive there, not after.

### **5: What’s Missing**

The deepest issue with Oks’ essay is the framing, rather than his individual claims. His entire analysis is labor-centric: _will humans still have jobs?_ I think this is assuredly worth asking, but also incomplete.

I’ll be charitable and say that the following section covers something he didn’t write about (instead of not considering), but he says “ordinary people don’t have to worry”, which I think is a bad framing.

The right question is: **who captures the surplus?** Is that worth worrying about?

If AI makes production 10x more efficient and all those gains flow to the owners of AI systems and the capital infrastructure underlying them, then “ordinary people” keeping their jobs at stagnant or declining real wages in a world of AI-owner abundance is not “fine.” It’s a massive, historically unprecedented increase in inequality. The comparative advantage argument is perfectly compatible with a world where human labor is technically employed but capturing a shrinking share of value.

This is what I’ve been working on in an upcoming policy document – the question of how ownership structures for AI systems will determine whether productivity gains flow broadly or concentrate narrowly. Infrastructure equity models, worker ownership structures, structural demand creation – these are the mechanisms that determine whether the AI transition is benign or catastrophic. Oks’ thesis has no apparent answer to the question.

Oks is right that thoughtless panic could produce bad regulatory outcomes. But complacent optimism that discourages the hard work of building new ownership structures, redistribution mechanisms, and transition support is equally dangerous, and arguably more likely given how power is currently distributed. Benign outcomes from technological transitions have _never_ been the default. They’ve been the product of deliberate institutional design: labor law, antitrust enforcement, public education, social insurance.

I don’t think we should be telling people “don’t worry”. **We should worry about the right things**. Think seriously about who will own the systems that are about to become the most productive capital assets in human history, and pay attention to whether the institutional frameworks being built now will ensure you share in the gains. The difference between a good outcome and a bad one is about political economy and ownership, and history suggests that when we leave that question to the default trajectory, ordinary people are the ones who pay.
