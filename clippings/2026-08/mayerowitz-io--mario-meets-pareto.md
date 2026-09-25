---
url: "https://www.mayerowitz.io/blog/mario-meets-pareto?utm_source=braze&utm_medium=email&utm_campaign=the-overflow-newsletter&lid=rfks4gm0nq3h"
captured_at: "2026-08-12T15:48:51+01:00"
title: "Mario meets Pareto"
domain: "mayerowitz-io"
---

---
In Mario Kart 8, choosing your driver, kart's body, tires, and glider isn't just about style — it's as crucial as your racing skills to win a race. Ever wondered how to truly find the best ones?

For each of those four elements, you have tens of options. For each option, there are distinct statistics (speed, acceleration, ...) affecting your performance.

This adds up to an unbelievable amount of builds to choose from.

Hopefully, many choices are just stylistic — they have identical statistics — but even after ignoring those duplicates, it remains a tough job to navigate the thousands of options.

Is there any chance to find the best build or is it just luck? Should you favor _speed_ to be the fastest, or _acceleration_ to quickly recover after taking a hit? Let me show you a solution proposed over a century ago by economist Vilfredo Pareto.

Finding the fastest driver is as simple as ranking them by their _speed_ statistic. Here you might think that ![Bowser](https://r2.mayerowitz.io/mk8_data/images/64px-MK8_Bowser_Icon.png)Bowser or ![Wario](https://r2.mayerowitz.io/mk8_data/images/64px-MK8_Wario_Icon.png)Wario are a no-brainer.

But you can't just rely on speed to find the optimal build. You have to consider acceleration as well. Now, finding the best is not trivial anymore — you have to make trade-offs between and  

Look closely though! You'll find out that some options are always _dominated_. Let's focus on this poor ![Koopa Troopa](https://r2.mayerowitz.io/mk8_data/images/64px-MK8_Koopa_Icon.png)Koopa for instance.

![Cat Peach](https://r2.mayerowitz.io/mk8_data/images/64px-MK8_Cat_Peach_Icon.png)Cat Peach has more speed for the same acceleration, and ![Toadette](https://r2.mayerowitz.io/mk8_data/images/64px-MK8_Toadette_Icon.png)Toadette has more acceleration for the same speed. Between you and me, if you want to win, never allow ![Koopa Troopa](https://r2.mayerowitz.io/mk8_data/images/64px-MK8_Koopa_Icon.png)Koopa to sit in your kart!

You can identify all efficient drivers that, unlike Koopa, are never dominated on both _speed_ and _acceleration_. Together, they form what is called the _Pareto front_ (or frontier).

Mind you: not all elements of the frontier are equally good. You probably won't pick a driver sitting on the edge of the frontier because you want some balance between _speed_ and _acceleration_. The Pareto _efficiency_ is an objective criteria to filter out suboptimal choices, but you still need to make up your final decision.

Given your play style and skills, you may put more weight on one statistic over the other. Those preferences will reveal the component on the frontier that suits you the best.

Best : { ![Cat Peach](https://r2.mayerowitz.io/mk8_data/images/64px-MK8_Cat_Peach_Icon.png) }  

In practice, you not only choose a driver, but a full set of body, wheels, and glider. In the next section, I'll display every build as a distinct point. It will however make the number of choices explode. But Pareto's with us!

## Speed

## Acceleration

## Weight

## Handling

## Off Road

## Mini Turbo

585 builds with unique _speed_ and _acceleration_ properties are available — tough decision for a player to make. But we can apply the same method as before. See, the Pareto front — in yellow — narrows it down to 14 efficient options!

Now, if you're a skilled player, you need a build that optimizes more than just and . There is a third crucial statistic: the _mini turbo_ that provides a speed boost after drifting.

Good news: the Pareto frontier concept can be generalized to more than two dimensions. See, I added the _mini turbo_ as a third one!

Sadly, it comes at a cost. As a rule of thumb, the size of the Pareto front expands exponentially with the number of (potentialy infinite) dimensions, making your choice harder.

As in the 2D case, you have to put weights on each dimensions to reveal the optimal build. Open the dialogue below and find the best build for you!

Customize

Let's look at the build currently favored by top players — which is composed of ![Peach](https://r2.mayerowitz.io/mk8_data/images/64px-MK8_Peach_Icon.png) Peach, ![Teddy Buggy](https://r2.mayerowitz.io/mk8_data/images/100px-TeddyBuggyBodyMK8.png) Teddy Buggy, the ![Roller tires](https://r2.mayerowitz.io/mk8_data/images/100px-RollerTiresMK8.png) roller tires, and the ![Cloud glider](https://r2.mayerowitz.io/mk8_data/images/100px-Cloud_Glider.png) cloud glider. Unsurprisingly, the build sits right on our frontier when optimizing _speed_, _acceleration_, and _mini turbo_.

We've had a bit of fun here, but don't you see the pattern? We're often faced with similar trade-offs. You want a [meal that's both cheap and delicious](https://en.wikipedia.org/wiki/Noodle_soup)? A job that's both well-paid, easy, and fulfilling? [A portfolio with low risks and high returns](https://en.wikipedia.org/wiki/Modern_portfolio_theory)? A flexible and strong material that's also easy to produce? [A fair taxation that remains efficient](https://academic.oup.com/restud/article-abstract/38/2/175/1527903) ? [A high quality LLM that is also fast and cost-efficient](https://artificialanalysis.ai/#summary). In all these cases, you're facing a multi-objective optimization problem, and you have to make trade-offs.

Of course, if you already know the exact weights you want to assign to each dimension (i.e., you know your utility function), you reduce the problem to a single objective optimization. This is because you can combine the dimensions with the weights into a single quantity to optimize (often called utility, cost, or fitness). In that case, you don't need Pareto at all.

But you're often faced with situations where your utility function is unknown or uncertain. In those situations, the Pareto front helps you eliminate objectively all the sub-optimal options. It won't reveal the one best option right from the outset, but you may now experiment with these efficient options and select the one that fits you the best.

### Acknowledgments

I've made some simplifying assumptions in this article to keep it readable for a large audience. In truth, the statistics that I presented are translated into derived in-game stats that are not always linear with the base statistics. Additionally, there are 4 speed stats and 4 handling stats for all gears (except for the driver), but I decided to simply average those. I've also completely hidden the functional form of the utility function, which can play a great role. To get access to more details behind this article or if you just like my work and want to see more in the future, please consider [donating some coins](https://ko-fi.com/antoinemayerowitz).

### Credits

Super Mario Wiki [Mario Kart 8 Deluxe in-game statistics](https://www.mariowiki.com/Mario_Kart_8_Deluxe_in-game_statistics)

Henry H. [Mario Kart and the Pareto Frontier](https://hinnefe2.github.io/python/tools/2015/09/21/mario-kart.html), 2015
