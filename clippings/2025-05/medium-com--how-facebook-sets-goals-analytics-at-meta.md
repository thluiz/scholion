---
url: "https://medium.com/@AnalyticsAtMeta/how-facebook-sets-goals-94cee1c7f44f"
captured_at: "2025-05-23T15:49:24+00:00"
title: "How Facebook Sets Goals - Analytics at Meta - Medium"
domain: "medium-com"
---

[

![Analytics at Meta](https://miro.medium.com/v2/resize:fill:64:64/1*9IKlJavI2QSn7CpKVee5uA.png)

](https://medium.com/@AnalyticsAtMeta?source=post_page---byline--94cee1c7f44f---------------------------------------)

7 min read

Nov 22, 2024

\--

_Author: Morgan Henry_

At Meta, we are committed to achieving our mission of giving people the power to build community and bring the world closer together. To do this, we set goals with each organization that align with our strategy and help us measure progress towards our mission. Typically these goals are on an annual or six month (half-year, or just ‘half’) basis. Within the Facebook team alone, goaling is a multi-month effort involving thousands of people, so it pays to have process and tooling in place to make sure everyone stays aligned.

In this article, we’ll explore Facebook’s “goal map” and how it helps us ensure we’re all working together effectively toward achieving our mission. While this post details Facebook’s approach specifically, many other organizations within Meta have adopted a similar approach.

**First, some basic terminology**

*   **Goals** are statements about what we want to achieve
*   **Goal metrics** are the best proxies to allow us to measure progress to the goals
*   A goal metric **target** is a specific number or threshold of the metric that the team is striving to hit in a particular time frame (typically within a half)

**What is a Goal Map?**

A goal map is simply a visual representation of an org’s vision, goals the org needs to hit to achieve that vision, and metrics that measure progress toward those goals. The goal map is _not_ an org chart (especially because multiple teams can contribute to the same goals), but it should in some way reflect each business unit’s goals and how they contribute to the broader organization.

Connecting these concepts to the toy example in the diagram above, MyChefApp’s vision is to bring the world closer together through cooking. MyChefApp’s leadership has crafted a strategy to help the app achieve their vision, and it has 4 pillars:

*   Enable everyone to express their love of cooking
*   Enable everyone to get inspired by new recipes
*   Enable everyone to build connections with other food lovers
*   Enable everyone to have a high-quality experience on the product

The 4 pillars of the strategy also serve as the app-level goals (remember, goal in _words_!) The team measures progress against these goals via a suite of app metrics including Number of Recipes Cooked and Comments per Post. Collectively, growth in these metrics reflect whether the app is making progress toward its vision. Finally, teams within MyChefApp have team-level goal metrics that directly relate to app-level goal metrics– we’ll discuss why this is important in the next section.

**How Do We Use the Goal Map?**

The Facebook goal map has three primary use cases:

1.  **Illustrate the relationship between team goals, org-level goals, and the mission.** Arguably the most important use case for the goal map in an organization as large and complex as Facebook is to drive alignment between a product team’s goals and the org’s strategy and priorities. Team-level goals (including the metrics that we use to measure progress against those goals) ladder up to org-level goals & metrics and, ultimately, to the Facebook-level goals.  
    — You might wonder why teams can’t just take on the same metrics that the overall org is responsible for. Let’s use daily active users (DAU) as one example metric that Facebook might care about. In practice, this metric is very hard to move with statistical significance in a single experiment, and even team units of 10–20 engineers may not be able to influence it over the course of a six month measurement period. In order to unblock operational decision making on individual experiments and workstreams, teams will take on goal metrics that are strongly hypothesized or proven to influence the app-level goal metric in the long term.  
    — For instance, the Marketplace team (which is part of Facebook team) might choose to goal on Marketplace DAU instead of overall Facebook DAU.
2.  **Provide visibility into work happening across the org.** The goal map helps us identify areas of potential collaboration, or overlap, between teams that are working toward the same goal.  
    — From the toy example above, we know that Marketplace team is aiming to drive Facebook DAU via their work on Marketplace DAU. Imagine that, via the goal map, the Marketplace team sees that the Notifications team is also working on projects that should ladder up to Facebook DAU. The two teams can now proactively identify opportunities for joint work that might drive that shared goal metric, such as personalized notifications for new listings near me on Marketplace.
3.  **Serve as a framework for teams to consider when prioritizing projects, requests, and resources.** The goal map can drive intentional conversations and work to evaluate whether workstreams _really_ ladder up to the app outcomes we care about.  
    — Expanding upon our example, imagine that one team within the Marketplace org uses Marketplace Messages as a goal metric. Marketplace Messages have a correlational relationship with Marketplace DAU. However, over time the team learns that increasing Marketplace messaging does not predict increased Facebook DAU very well. Digging deeper, they learn that the increase in messages is not leading to actual sales because the messages are being sent by scammers who do not actually intend to buy the product. This is a bad experience for sellers (and for _real_ buyers!) which leads to worse retention down the road. In this example, the team would evaluate alternative goal metrics that are still actionable but better correlated to good user experiences.  
    — Relatedly, a partner team whose work is regressing Marketplace Messages but growing Facebook DAU should not be blocked from launching these experiences, as they are directly growing the app-level outcome we care about.

**How Do We Prioritize Among Goals?**

At Meta, we use a system called **goal tiering** to help teams get aligned on relative prioritization of metrics across the full suite of goal metrics. This system also informs how we adjudicate tradeoffs across the company (for instance, between Facebook and Instagram).

While most of this post is focused on goal metrics that we directly optimize for (i.e. Tier 1 and Tier 2 in the schema above), we also have a number of health or **countermetrics** in our goal map.

Countermetrics provide a control for known levers that move the goal metric but aren’t central to our mission. These metrics prevent teams from compromising on things like quality, integrity, or cannibalizing other parts of the app in service of their goal. In some cases, we are willing to regress the countermetric, but we set precise bounds on how _much_ we are willing to regress (i.e., guardrails). Within Facebook, we have countermetrics for categories such as performance and reliability (for example, startup time or number of crashes).

**How Do We Set Goal Targets?**

We set and measure progress toward goal targets through a combination of needs (how much progress do we need to make towards our goal in this half to support our strategy & mission) and resources (given current priorities and resourcing, how much progress can we confidently make towards the goal in this half). These are also sometimes referred to as “top-down” and “bottom-up” inputs, respectively.

At Facebook, we aspire to set **50/50 goals**. This means we try to set goal targets that we have a 50% chance of achieving, and at the company or organization level, we should hit only about half of the goal targets that we set. We do this not to set ourselves up for failure, but rather to ensure that we have the appropriate level of ambition to encourage big bets while also grounding our expectations in reality.

Generally, target-setting requires two inputs: **(1)** an idea of what would happen to the metric if all of our engineers went home, and **(2)** some assumptions about how much those engineers can achieve if they work on the product roadmap. This is where forecasting comes in. Typically, we first produce a forecast for the “organic” trend of a given metric– again, what would happen if we did nothing to improve the product– and then add in some assumptions about how much impact we can have in the given timeframe, also known as “product impact”. For more details, you can read about the art and science of Forecasting @ Meta [here](https://medium.com/@AnalyticsAtMeta/forecasting-meta-balancing-art-and-science-92526e1ae36c).

**How do we measure progress toward goal targets?**

There are three primary ways we measure progress to goal targets at Facebook:

*   **Longitudinal tracking:** watching the overall metric value over time, typically within a half or a year
*   **Long-term or Short-term Holdouts**: A “holdout” is an experiment with a holdout group (control) and production group (test) that is designed to measure a team or product’s impact. The holdout group is typically a small group of users (<10% of eligible population) who do not see a product, feature or its iterations even after they are shipped to everyone else. The test group may contain many features or treatments and, unlike a typical experiment, its subjects’ experience may change over time as treatments are added.  
    — **\[uncommon\] Long term** holdouts measure the cumulative impact of a product or feature for ~years. These are hard to justify (because of the poor user experience) and hard to maintain, so they are not used frequently for goaling  
    — **\[common\] Short term** holdouts that stay open for one half — enable us to comprehensively measure impact of a team’s work on the goal metrics within a half so we can monitor goal performance (aka team impact) and decompose topline longitudinal trends

Outside of this framework, we also have some milestone/ship goals which may not move app-level metrics in the short-term, but rather ladder more directly to the strategy (for example, launching a new feature or undertaking an infrastructure migration).

**Conclusion**

We’ve established a goal map along with a suite of other tools & processes to support progress against our mission & vision in an organization as large and complex as Facebook. Whether your team is large or small, these tools can help you drive accountability across teams and, ultimately, realize better results at the company level.
