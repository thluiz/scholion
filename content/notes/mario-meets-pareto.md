---
title: "Mario meets Pareto"
date: '2026-08-12T15:48:51+01:00'
category: webclip
summary: 'The article shows how Mario Kart 8 build selection becomes a multi-objective optimization problem and how the Pareto front removes dominated options without choosing a final winner.'
tags: ["pareto-front", "multi-objective-optimization", "mario-kart-8"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Mario meets Pareto"
    url: "https://www.mayerowitz.io/blog/mario-meets-pareto?utm_source=braze&utm_medium=email&utm_campaign=the-overflow-newsletter&lid=rfks4gm0nq3h"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-08/mayerowitz-io--mario-meets-pareto.md"
    kind: repo
---

The article uses Mario Kart 8 builds to show that picking a driver, kart body, tires, and glider is a trade-off problem. Speed alone does not identify the best build, so the same reasoning extends to acceleration and other stats.

It explains dominated options, defines the Pareto front as the set of efficient choices, and shows how the idea scales from two dimensions to three with mini turbo. The article also notes that the frontier only filters out suboptimal builds, while the final choice still depends on the weights a player assigns to each stat.

## Reading notes

- In Mario Kart 8, each build combines a driver, body, tires, and glider, and each part affects statistics like speed and acceleration.
- Some options are duplicates, but even after removing them there are still thousands of possible builds.
- A build is not optimal if it is dominated by another option on the stats being considered.
- Koopa Troopa is used as an example of a dominated driver because other drivers can beat it on speed or acceleration for the same value of the other stat.
- The set of efficient, non-dominated choices is called the Pareto front.
- Not every point on the Pareto front is equally good, because the final choice depends on the balance a player wants between the stats.
- The article extends the same method to full builds and shows that 585 builds with unique speed and acceleration properties reduce to 14 efficient options.
- Mini turbo is added as a third important statistic, and the Pareto frontier is generalized to more than two dimensions.
- The frontier grows quickly as dimensions increase, which makes the decision harder.
- The build used by top players is Peach, Teddy Buggy, roller tires, and cloud glider, and it lies on the frontier when speed, acceleration, and mini turbo are optimized.
- The same multi-objective trade-off appears in meals, jobs, portfolios, materials, taxation, and LLM performance.
- If the weights for each dimension are known, the problem can be reduced to a single objective.
- When those weights are unknown or uncertain, the Pareto front helps remove objectively suboptimal options while leaving the final preference choice open.
