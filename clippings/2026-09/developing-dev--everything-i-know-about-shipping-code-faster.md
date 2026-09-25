---
url: "https://www.developing.dev/p/everything-i-know-about-shipping?ref=dailydev"
captured_at: "2026-09-25T21:56:02+01:00"
title: "Everything I Know About Shipping Code Faster"
domain: "developing-dev"
---

Two weeks ago, I shared Evan’s writing on [what helped him grow from Junior to Staff at Meta in 3 years](https://www.developing.dev/p/new-grad-to-staff-at-meta-in-3-years). His entire post hinges on that you need to blaze through your core responsibilities to free up time for growth.

The most common question I got after that post was how do you do that?

I interviewed Evan last week so you can hear the answer in his own words soon (aiming to share that next week). Before that, I wanted to share some thoughts since it’s one of the most important parts of growing your impact. Here’s everything I know about shipping more in less time.

Before you start writing code, you need to figure out what changes to make and where to make them. If you want to do this fast, you need to:

1.  **Become fluent at code search.** Most codebases are too large to keep in your head. When trying to find where to make changes, you could spend hours reading unfamiliar code which can be a huge time sink. If you’re good at code search, you should be able to find where to make a change in minutes. Learning code search and the relevant keyboard shortcuts is well worth the time investment.
    
2.  **Know who knows what.** Again, since codebases are too large for any one engineer to know entirely, you’ll need to rely on others to get up to speed in unfamiliar places. You need to learn who knows what (ask around or check the git blame) and you have to use your soft skills to get the information you need.
    
3.  **Learn how to query data.** I cringe when I see engineers asking data scientists to run simple queries for them. Delegation can be good but it can also add more waiting and overhead. If you can get answers for yourself you’ll be a lot faster in figuring out what direction to go in.
    

One of the most important parts of churning out code fast is to [write smaller, focused diffs](https://www.developing.dev/p/why-write-small-diffs). As your code changes get larger, the time to write, test, review, and merge them in goes up exponentially. Not to mention that the chance of catching bugs is much lower:

[

![](https://substackcdn.com/image/fetch/$s_!Rddy!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2ca4fe3c-6a86-48d4-91fc-1792653733aa_1098x474.png)

](https://substackcdn.com/image/fetch/$s_!Rddy!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2ca4fe3c-6a86-48d4-91fc-1792653733aa_1098x474.png)

Goal is to land \*working\* code fast

Once you get into a habit of writing small, encapsulated diffs you’ll find that proving your code works can actually take longer than writing it. There are three tactics that helped me test my code faster:

1.  **Batching test plans** - To make testing faster, I created large stacks of commits that were all loosely related on the same code path. I then ran tests covering the entire stack all at once. For a stack of 10 commits, I only paid the cost of testing once while making sure nothing broke.
    
2.  **Gating all changes** - I used [feature flags](https://www.optimizely.com/optimization-glossary/feature-flags/#:~:text=Feature%20flags%20\(also%20known%20as,the%20full%20lifecycle%20of%20features.) on every code change I made so that users couldn’t access code paths while I worked on them. That way I could land code as fast as I wanted without worrying about breaking anything. Then when I was ready to release the code, I would verify everything all at once by turning on the flag for a small population while monitoring it.
    
3.  **Copying existing test plans** - Writing code in unfamiliar places was often simple. But I didn’t know how to test it since I wasn’t familiar with the code path. What helped me move much faster was to look at the [git blame](https://git-scm.com/docs/git-blame) for existing test plans. If people document how they tested their code, you can just reuse their methodology to prove your code works.
    

Once I was fast at writing code, I was landing an average of five code changes per day to prod. After 1000+ commits, I learned that the bottleneck in landing code faster was no longer in writing and testing it. My bottleneck became waiting on code reviews. There are two ways to get code reviewed faster:

1.  **Reduce friction for the reviewer**. You want to make your code as easy as possible to review. I try to spoon-feed the reviewer by pointing out what to scrutinize and providing relevant context via comments. Also, another trick I’ve used is hinting with diff titles how fast my small changes would be to review (e.g. adding "\[easy\]" worked for me).
    
2.  **Get your code approved the first time it’s reviewed.** We spend a lot of time waiting for others to start reviewing the code. That waiting time doubles if you need even one iteration. Before you submit your code for review, preempt any potential feedback and thoroughly test your code. Also, discuss any ambiguous parts of your implementation with people in advance so there isn’t a bunch of thrash after you write it.
    

Writing software is social. You need to know how to smoothly cooperate with people and request review from them. If you’re a good collaborator, you’ll build trust so that people review your code faster. Aside from that, it’s also often helpful to educate people on what you’re working on. The most effective way I found to do that was by writing clear descriptions for each of my code changes. That way anyone who saw it could understand what I was doing and why I was doing it enough to review it.

Writing code requires deep focus since you need to juggle a lot of context. How deep in the call stack are you? What other code references your code? Getting all that loaded into your brain's working memory takes time. Every interruption makes you pay that cost again.

[

![No alt text provided for this image](https://substackcdn.com/image/fetch/$s_!1Nw_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7926f6aa-e780-4652-b6dc-bacbe060597a_828x465.jpeg "No alt text provided for this image")

](https://substackcdn.com/image/fetch/$s_!1Nw_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7926f6aa-e780-4652-b6dc-bacbe060597a_828x465.jpeg)

Therefore, reducing unnecessary distractions is one of the most impactful things you could do to be more productive. Thankfully, there’s a lot of tactics to preserving your flow state:

1.  **Use noise-canceling headphones**. When I first joined Meta they had a headphone stipend of $350. This felt like a pure luxury, however I soon realized it was a big productivity booster since it helped me focus. I’d recommend either AirPods or Bose QC35 headphones if you don’t have some.
    
2.  **Create focus blocks.** This means moving meetings around or canceling them in [favor of async communication](https://www.developing.dev/p/efficient-communication). The best possible schedule would be one with few meetings that are all clustered together. This will maximize your focus time for deep work.
    
3.  **Work when fewer people interrupt you.** I always found that I was most productive at night. A large part of that is because no one is asking me for anything at that time so there are no interruptions. If you’re a morning person, you could try the opposite where you get your focus work done in the morning.
    
4.  **Reduce noisy notifications.** Turn off notifications from unimportant channels. Keep your phone somewhere where you can check it occasionally but that doesn’t interrupt you. Checking your pings in batches is much more efficient and preserves your focus time.
    

There are also often technical solutions to getting work done faster. I’d recommend you audit your workflow and see what you’re waiting on (e.g. builds, tests, queries). Slow parts of your workflow are often opportunities to [make tools that help you move faster](https://www.developing.dev/p/tools-of-the-trade). The added benefit of building technical solutions is you can share these tools with others for leveraged impact.

[

![Is It Worth the Time?](https://substackcdn.com/image/fetch/$s_!RHLi!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcc6d2675-c3ea-4572-821d-bdde99363909_571x464.png "Is It Worth the Time?")

](https://substackcdn.com/image/fetch/$s_!RHLi!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcc6d2675-c3ea-4572-821d-bdde99363909_571x464.png)

Credit: XKCD 1205

No matter how much you optimize your workflow, there will always be some waiting. For those small fragments of time you should see if there are some tiny things you can get to. For me this meant cleaning up the code, replying to pings, or querying data. Whatever it is though, you shouldn’t just sit there while you’re waiting for builds. That time adds up and you can get much more done by interleaving small tasks while you wait.

If you do this right, you’ll free up that extra 30% time to enable the career growth that Evan talked about. I had a similar experience to him, but one other thing I did was work more hours. I enjoyed my work enough that I was probably averaging a natural extra 30% of work time. Coupling that with being more efficient helped me pursue many parallel growth opportunities.

I hope this was helpful, and look out for the conversation with Evan. We thought it’d be interesting to compare and contrast our paths to Staff at Meta in 3 years. He had a lot of interesting stories to share that he hasn’t talked about anywhere else yet.

If you’re interested you can sub to [my YouTube](https://www.youtube.com/@ryanlpeterman) to make sure you get it as soon as it’s available. It’ll also be available wherever you get your podcasts:

*   [Spotify](https://open.spotify.com/show/0MX9PyeCzDhdlyRv6slwIX)
    
*   [Apple Podcasts](https://podcasts.apple.com/gb/podcast/the-developing-dev/id1777363835)
    

Thanks for reading,  
Ryan Peterman
