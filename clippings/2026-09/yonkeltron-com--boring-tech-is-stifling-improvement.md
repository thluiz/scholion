---
url: "https://yonkeltron.com/posts/boring-tech-is-stifling-improvement/?utm_source=tldrnewsletter"
captured_at: "2026-09-25T23:09:30+01:00"
title: "Post: Boring Tech Is Stifling Improvement"
domain: "yonkeltron-com"
---

Wed Oct 09 2024

Even US folks may not have seen the [headlines about it](https://apnews.com/article/philadelphia-interstate-i95-highway-collapse-fire-a90c5e3dd85de025050229bb6a37b780), but a section of [Interstate 95](https://en.wikipedia.org/wiki/Interstate_95) near me [collapsed in June of 2023](https://www.nytimes.com/article/i95-collapse-philadelphia.html). As the the [collapse took place on June 11th](https://en.wikipedia.org/wiki/2023_Interstate_95_highway_collapse), the original repair estimate had a timeline measured in months. However, through the leadership and collaboration of Pennsylvania officials, that segment was [repaired and reopened on June 23rd](https://www.inquirer.com/news/philadelphia/live/i95-philadelphia-repairs-bridge-collapse-livestream-traffic-20230623.html), less than two weeks later.

One headline which seemed lost in the celebrity hustle and bustle In the Philadelphia region, both the [Phanatic](https://en.wikipedia.org/wiki/Phillie_Phanatic) and [Gritty](https://en.wikipedia.org/wiki/Gritty) are major public figures. of reopening taught me something which I think about to this day. Namely, that an all-new construction material called [Foamed Glass Gravel](https://en.wikipedia.org/wiki/Foam_glass_gravel) was used [as infill](https://www.nbcphiladelphia.com/news/local/whats-backfill-crews-to-use-tons-of-glass-nuggets-to-rebuild-collapsed-section-of-i-95/3585523/) during [repair work](https://www.nj.com/traffic/2023/06/recycled-glass-will-temporarily-fill-the-hole-on-i-95.html). That is to say that the professionals in charge of rebuilding found a better way to do things than they’ve always been done. Moreover, those self-same professionals intentionally circumvented the slow supply chain to use the new-and-better thing.

Did anyone stand up to scream about how “I95 is a rock-gravel shop”? Where were the naysayers reminding people about standard practices and their importance?

Can you imagine had this been a software project? For more about the intersection of software engineering and other traditional engineering disciplines, see [The Crossover Project](https://hillelwayne.com/tags/crossover-project/).

I’ve recently noticed the rise of what I’ll call the “boring technology movement”. I derive this nomenclature from the 2015 essay entitled [“Choose Boring Technology”](https://mcfunley.com/choose-boring-technology) and its accompanying [presentation deck](https://boringtechnology.club/). These pieces have, in general, become a bit of a manifesto for folks in this movement.

The manifesto makes some very good points. I think the concept of an “innovation token” to help teams budget for adopting new technologies bears serious consideration. Furthermore, the dual points about operability and unfamiliarity really resonate with me, as someone who’s carried the pager.

One thing the manifesto identifies as problematic seems like the number of different solutions used. It’s not hard to imagine a company where the number of unqiue components in the technology portfolio nearly outnumbers the solutions built with those components. In such a case, seven different CI/CD tools surely seems extreme! What gives me pause is that a one-size-fits-all deployments of a _single_ CI/CD tool is also extreme. It just happens to be in the opposite direction.

So, really, I might really be against extremism in constraining or promoting choices.

Monocultures consisting of one tool or platform have their own downsides. One such downside is the introduction of a single-point-of-failure. Another is vendor lock-in and a higher cost of migration. Still yet is the missed cost savings from negotiating contracts with competing vendors.

Despite the helpful ideas offered by the boring tech source material, perhaps the movement has taken things too far. By my estimation Solely my personal opinion based on direct experience, observations, and discussions with others. , I’ve learned how _too_ heavily relying on boring tech can have negative effects on a macro level.

One negative effect is that it sucks the fun out of both our discipline and practice. Continuing to heavily leverage legacy technology leads to monotony and the suppression of enjoyment for those harboring a genuine enthusiasm for computing. Don’t discount the impact of turning away those with a passion for the craft!

A second negative effect is the chilling of innovation. Creating a better way of doing things definitionally requires deviation from existing practices. If that is too heavily disincentivized by “engineering standards”, then people don’t feel they have enough freedom to color outside the lines here and there. Therefore, it chills innovation in company environments where good ideas could, conceivably, come from anywhere. Put differently, use caution so as not to silence your [pioneers](https://medium.com/building-the-agile-business/a-structure-for-continuous-innovation-pioneers-settlers-town-planners-2f33be932179).

Another negative effect is the potential to cause stagnation. In this case, devotion to boring tech leads to overlooking better ways of doing things. Trading actual improvement and progress for “the devil you know” seems a poor deal. One of the main arguments in favor of boring tech is operability in the polycontext composed of predictability and repairability. Despite the emergence of [Site Reliability Engineering (SRE)](https://sre.google/sre-book/table-of-contents/), I think that this highlights a troubling industry trope where we continually underemphasize, and underinvest in, production operations.

Wouldn’t folks feel better making smart, reasonable, and incremental improvements? Consider cases like introducing [Kotlin](https://kotlinlang.org/) to gradually level-up a Java shop. What about a PostgreSQL operation rewriting SQL stored procedures in [PL/Python](https://www.postgresql.org/docs/current/plpython.html)?

Again, I respect the original manifesto. I don’t advocate for a world where having seven different CI/CD tools is ok. That would probably be arrogant and silly. Rather, I think it’s important that we don’t over-index on current state and forfeit chances to improve.

Besides. Let’s not take the fun out of everything.

[← _Back to All Posts_](https://yonkeltron.com/posts)
