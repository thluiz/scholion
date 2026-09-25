---
url: "https://rethinkingsoftware.substack.com/p/why-scrum-is-stressing-you-out?ref=dailydev"
captured_at: "2026-09-25T20:33:33+01:00"
title: "Why Scrum is Stressing You Out"
domain: "rethinkingsoftware-substack-com"
---

[

![](https://substackcdn.com/image/fetch/$s_!HFtT!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F425a6a46-92a5-4ef8-ae44-41f04138fe59_1024x1024.jpeg)

](https://substackcdn.com/image/fetch/$s_!HFtT!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F425a6a46-92a5-4ef8-ae44-41f04138fe59_1024x1024.jpeg)

Programming today is stressful — way more stressful than I remember it in the 90s and early 2000s when I was just starting out. Back then, things would get crazy around deadlines, but at other times, I recall feeling pretty even. These days, however, the pressure seems omnipresent.

Naturally, I'm interested in doing away with this feeling of pressure, for the sake of my health as well as my productivity. So, I've given a fair bit of thought to why things have gotten so bad (at least for me if not for others) in the last couple decades.

I don’t think it’s due to stiff competition, shifting markets, or even tight deadlines—those have always existed. But one significant change has occurred in my daily work routine: I’ve been forced to start working in sprints (usually 1-2 weeks) instead of spending larger chunks of time on larger projects. This shift has had some unfortunate consequences.

Why would sprints be more stressful? Aren't they just more frequent, shorter deadlines as opposed to the occasional really big one? Doesn’t this save you from having to crunch at the end of a project? This reasoning seems logical, but it overlooks some important details in the real, lived experience of today's software developers. Here's how I think sprints are doing us wrong:

Sprints are problematic for the simple fact that they never let up. Sprints are not simply shorter deadlines, encountered sporadically as you move along. They are forever repeating, back-to-back deadlines. Waterfall was structured around genuine deadlines and real-world events that demanded focused attention. You worked hard to get something working, then you were done. High pressure was followed by low pressure. Sprints, on the other hand, are fake deadlines, invented for the sake of a process. Since they are contrived, they have no natural breaks or resting periods. There is no time to breathe, no time to collect yourself.

If you were to graph programmer stress levels over time in a traditional Waterfall approach versus a sprint-based Scrum model, it might look something like this:

[

![](https://substackcdn.com/image/fetch/$s_!JCar!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0f1d20c4-97a8-4970-9d9b-151b0dea3616_984x826.png)

](https://substackcdn.com/image/fetch/$s_!JCar!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0f1d20c4-97a8-4970-9d9b-151b0dea3616_984x826.png)

While Waterfall causes higher spikes in stress, sprints impose a more constant, medium-level stress. The difference lies between higher short-term stress and medium, long-term stress. While no stress is entirely comfortable, our bodies are better equipped to handle short-term stress. In fact, short-term stress can be healthy and make us stronger. Think of how going to the gym stresses your muscles for an hour or two, allowing them to build back stronger—as long as you give them time to rest. Long-term stress, however, is more insidious. Prolonged stress wreaks the most havoc on your body over time.

> …some of the reasons stress can be positive in these situations is that it’s short-term and it’s helping you get through a challenge you know you can handle.
> 
> Experiencing stress over the long-term, however, can take a real physical and mental toll on your health. Research has shown a connection between stress and chronic problems like [high blood pressure](https://www.webmd.com/hypertension-high-blood-pressure/default.htm), [obesity](https://www.webmd.com/diet/obesity/features/am-i-obese), [depression](https://www.webmd.com/depression/default.htm), and more.  
> — _What Does Stress Do to the Body?_ [WebMD](https://www.webmd.com/balance/stress-management/stress-and-the-body)

If a development team were to sit down and decide to deliver code every two weeks, based on a process of their own design—one that made sense to them and suited their circumstances—that would be one thing. But sprints in a Scrum-like process don’t work that way. Every aspect of a sprint is prescribed: its duration, its meetings, its tasks, and even the roles of its participants. You might think that choosing your own process wouldn’t make much of a difference, but research tells a different story. Autonomy—the ability to direct one’s own work—plays a significant role in how work is experienced.

Consider, for example, a study with male mice divided into groups: some were subjected to involuntary running periods, while others had the autonomy to control their own exercise. Even though both groups ran the same distance (the amount of running was distance-matched), the mice that were forced to run exhibited distinct signs of stress, fear, and discomfort (poor little fellas!).

> We find a broad response of 140 regulated brain regions that are shared between voluntary wheel running and treadmill running, while 32 brain regions are uniquely regulated by wheel running and 83 brain regions uniquely regulated by treadmill running. In contrast to voluntary wheel running, forced treadmill running triggers activity in brain regions associated with stress, fear, and pain.
> 
> https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10943479/

And it makes sense, doesn’t it? No one likes being told what to do—it ruins the experience. It strips away your intrinsic motivation and, worse yet, it hinders your ability to adjust, experiment, and improve. Even the toughest conditions can be endured if there’s hope for change, but forced compliance takes away all control and robs you of that hope. In Scrum, programmers are like those mice subjected to involuntary effort, forced to run on treadmills of our bosses' making—one sprint after another, after another.

For more insight into the benefits of autonomy in the workplace, I recommend _Drive_ by Daniel H. Pink.

Another stressful aspect of sprints in a Scrum-like environment is that they often leave you feeling unprepared for the next task. This happens because no time is set aside for proper engineering prep work. There's far more to a task than simply typing out a solution. As DeMarco and Lister wisely observe:

> If you are charged with getting a task done, what proportion of your time ought to be dedicated to actually doing the task? Not 100 percent. There ought to be some provision for brainstorming, investigating new methods, figuring out how to avoid doing some of the subtasks, reading, training, and just goofing off.  
> — _Peopleware_, Tom DeMarco and Timothy Lister

When a sprint begins, the expectation is that the time for preparation has passed, and only implementation remains. Scrum seems to assume you can simply "bang it out" like assembling a piece of IKEA furniture—just pull the next instruction manual from the backlog and follow the steps. In reality, it’s more like being dropped into the jungle without a map or provisions, with only two weeks to find your way out. You’re starting from ground zero every time, and the clock is ticking.

You might hope to get a few helpful tips on how to approach your work during Scrum planning meetings or grooming sessions, but even in the best planning environment, these discussions rarely provide more than superficial guidance. The real, substantive insights only come once the actual work begins. Preparation and execution can’t be separated—thinking and doing are intertwined. When we try to divide them, we create stress.

As many of you are well aware, most Scrum implementations are a hybrid of Waterfall and Scrum. As a result, there’s always a Waterfall-like, big-bang deadline quietly lurking in the background. The business side just can’t help itself. ("We have to market things!" "We need to inform customers about what's coming!" "We have to make promises at conventions!" "That's just the reality!") And when that big deadline inevitably arrives, the work from previous sprints is rarely enough to deliver on what was promised. The pressure mounts, Scrum gets suspended, and you’re left with your very own Agile-flavored death march that looks something like this:

[

![](https://substackcdn.com/image/fetch/$s_!EEgt!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F58c5a0eb-48e4-43b5-9f92-ca1350826a7f_1068x826.png)

](https://substackcdn.com/image/fetch/$s_!EEgt!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F58c5a0eb-48e4-43b5-9f92-ca1350826a7f_1068x826.png)

In this scenario, you get the worst of both worlds. Stress levels start high and only escalate as a major release approaches.

**Conclusion**

With sprints, there are no breaks, little autonomy, and insufficient time to prepare. No wonder developers today seem more stressed! The process is ill-suited to the nature of their work, and they are powerless to change it. The only remedy is to restore autonomy and professionalism to software development. Let developers control both their craft and their process. Treat them as respected peers, not replaceable cogs in a machine. However, achieving these conditions will likely require grassroots efforts by engineers, either through building more ethical organizations or transitioning to freelance work. Keep an eye out for articles from _Rethinking Software_ to help you navigate these paths.
