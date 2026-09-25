---
url: "https://dev.to/wyattdave/will-vibe-coding-kill-lowcode-1c37?"
captured_at: "2025-09-16T19:06:18+01:00"
title: "Will Vibe Coding Kill LowCode - DEV Community"
domain: "dev-to"
---

---
The short answer is no, the long is still no but its complicated, let me explain.

I've seen multiple posts and blogs about how the Power Platform (my LowCode platform of choice) is doomed or will change entirely because of AI and vibing coding. The premise is simple and logical:

> Why would a make spaghetti diagrams to create flows when a sentence will do it

___

> Why drag and drop components onto a page to make a app when I can describe a app and get a full React App

___

> Why learn a LowCode language when AI can use natural language instead

And a call out here, these words have been said by experts who are massively more experienced and knowledge them me, so remember that when you read the below, but I think this future state is further off then what people may think.

## [](https://dev.to/wyattdave/will-vibe-coding-kill-lowcode-1c37?#cost)Cost

This one to me is probably the biggest, AI is expensive. Not only that, but companies who have bet heavily (cough Microsoft), and venture capitalists, are subsidising AI heavily, they are barely making if any profit, and definitely nothing close to the margins on LowCode products like the Power Platform.

So its more expensive now, and the price is going to go up. And if you are thinking Moore's law will save you that's not how the marked has been moving. The arms race means "cheaper" models are not simply not being used, everyone is only using the latest, expensive models.

Lets take my favourite tool, Power Automate.

100 action flow is by all accounts free (6k per day per M365 account at no extra cost).

Even if we go with Premium full price (and most orgs do not pay full price).

40k per day  
28 days  
1,120,000 calls  
Cost $10  
**Thats 0.08 cents per run**

Now Agent flow  
25k messages per month  
13 messages per run  
1923 runs  
Cost $200  
**Thats 10.4 cents per run**

[![meeting](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fgwmr1ycyelvvgis8d9kx.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fgwmr1ycyelvvgis8d9kx.png)

Yep thats **130x** the cost, and you really think organisations are going to stop using Power Automate and use Agents Flows instead.

[![cost table](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fj7l09p4qfavt3s33nu2f.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fj7l09p4qfavt3s33nu2f.png)

And its the same with Vibe coding apps, just look at the costs for Claude Code and ChatGPT, they average a couple dollars to build each, not a lot. But what about for Microsoft, how long until those thousands of Citizen developers building hundreds of thousands of crappy apps before they start charging differently (also amusing that all of the "all you can eat" licenses like from Claude and Cursor have been pulled).

There is also the bigger structural change, moving from flat rate license to PAYGO. It was a big difficult shift to move from One time purchase to monthly subscription based charging, but organisation did because it did have a benefit- simplified costs (no inconsistent large purchases). AI is not sustainable on a per license approach, so the push is PAYGO/token packs. This is not only more expensive, but organisations lose the safety of set fees and budgets. Now they have to manage usage costs, build flexible budgets. and live in fear of a massive unexpected bill.

## [](https://dev.to/wyattdave/will-vibe-coding-kill-lowcode-1c37?#deterministic-outcomes)Deterministic Outcomes

AI is fantastic for handling complex unstructured processes. If there are too many or unknown inputs it is brilliant. Dealing with human inputs is its obvious strengths, as humans are anything but consistent.

But that's the trade off, because the inputs are unstructured you can't have known consistent outputs. And that's ok in some situations but what about when you come to import things like governance and finances.

Will banks be happy with that inconsistencies when dealing with money, or governments happy when compliance is black and white but the process is many shades of grey.

[![inconsistent responses](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fwgnofioatbwtsuqpq0bm.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fwgnofioatbwtsuqpq0bm.png)

So I can see AI having its use cases, but the lack of dertinitistic outcomes will be a deal breaker for many many process. They would much rather make the inputs deterministic (a drop down instead of free text) and know the outcomes, rather then have AI 'guess' the right outcome.

And that goes beyond just automation, code should have standards and patterns, which you can influence with AI instructions but it's never 100%. Add in as a code I can write exactly what I want vs a AI agent interpreting what I meant.

## [](https://dev.to/wyattdave/will-vibe-coding-kill-lowcode-1c37?#adoption-inertia)Adoption Inertia

The timing of this blog makes me smile, as Excel was launched in September 1985, 40 years ago.

[![Iexcel facts](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fs6skwk7kxl0yhkkwok68.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fs6skwk7kxl0yhkkwok68.png)

In that time we have had SQL launch, internet, the move to the cloud, LowCode adoption, smart phones, and many more advances, and yet good old Excel is still prevalent in most organisations (estimated between 750 million and 1.5 billion users. Add in that many IT teams have desperately battled to move users off it to more secure stable solutions, and yet it is still being used, often by people who weren't born when it was released.

What's this have to do with AI, well for every developer and user to switch from how they learned to do something to something dramatically different is a massive undertaking. You have:

-   Guides
-   Process
-   Documentation
-   Technical Knowledge
-   Technical Skills
-   Experience

just to name a few of the things you would need to change, add in 1000s of legacy flows and apps that all just work, why would you put the pain and effort into moving. That means best case dual process, legacy and new, and every organisations will tell you running parallel process is not efficient and not fun.

## [](https://dev.to/wyattdave/will-vibe-coding-kill-lowcode-1c37?#security)Security

Probably the biggest risk to AI is security, with everything that is new there are unknowns, often the only way something becomes secure is for it to be breached first. Do you want to be the first company that has that hugh data leak so that Microsoft/OpenAI/Google/Anthropic can improve their product.

[![owasp prompt injection](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Ffmxa40x8jel4ior3mq9g.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Ffmxa40x8jel4ior3mq9g.png)  
[Cornell University - Arxiv.org](https://arxiv.org/pdf/2410.23308)  
[Owasp.org](https://owasp.org/www-community/attacks/PromptInjection)

Then you add in that by its very nature AI is incredibly difficult to secure, security is built on understanding how things work (not easy when every interaction is non deterministic), trying to do that on a "black box" is impossible.

The final challenge is how LLM are current architected, there are no boundaries between input and command. Just like the old SQL injection days, this means you can not control what code runs, as the code is an input. The Perplexity vulnerability found by [Brave](https://brave.com/blog/comet-prompt-injection/) demonstrated this and how difficult protection would be, as with SQL we can bind to split input/command, but with LLM we can only layer on controls and checks, which are only as good as what we have experienced so far.

If you don't know me I'm big on code reviews, I have written how to complete one and even created automated tools. And during my most recent development I thought about using Copilot to code review flows, and it did an ok job, but the fun was when I embedded a prompt in the flow notes that told any LLM to always pass the code review 😎

## [](https://dev.to/wyattdave/will-vibe-coding-kill-lowcode-1c37?#technical-debt)Technical Debt

When things go wrong, and they always do, having a understanding of the code is key. It's easy to think you can vibe code by looping errors in and saying fix it. But that will only go so far, I have tried vibe coding a few times (and use AI assisted development pretty much all the time), this has limited scope. Sometimes it can't fix it and then you have to dive into the code. That's painful when you know the language, but when you don't, like the army of citizen developers, then you are building up a wave of technical debt that will hit you hard one day.

## [](https://dev.to/wyattdave/will-vibe-coding-kill-lowcode-1c37?#human-nuances)Human Nuances

I remember Microsoft saying "Agents are the new Apps", their position was, why would anyone use a graphical UI when you can type/say what you want. But that assumes that humans are all the same, that they all want to type, and that isn't just obviously inaccurate, but wrong. As I would say most humans don't want to type. It's easy to forget that computers started with command line and text, but the graphical UI won because the majority of humans prefer visual interfaces. Would you rather type "open excel", or click on the Excel icon? Likewise:

"I want a blue bordered date picker, 20% screen width" or drag date picker on to screen, drag resize and click blue for border.

"On a email arriving in a inbox if it has a power point attachment forward to [david@mail.com](mailto:david@mail.com)" or drag outlook trigger,set condition and add send email.

I'm pretty certain some would like the text, but some would like the UI (and I know there might be extra steps but there might also be extra prompts and the prompts often take a while to run).

The fact that Microsoft dropped that phrase and started highlighting apps again made me think they realised that too. So don't expect every developer to want to describe a flow to make the logic app json, a lot will want to drag a little box onto a screen to make that json.

## [](https://dev.to/wyattdave/will-vibe-coding-kill-lowcode-1c37?#human-nature)Human Nature

I think the biggest strength of the Power Platform is its community, and a lot of that has to do with learning and achievement.

Humans like to be creative, they like to solve problems, and they like to learn. If you stripped away all the expertise and difficulty in the Power Platform you would no longer have:

-   People like me blogging about it
-   Videos and books
-   People investing in learning
-   Conferences to share and learn
-   The satisfaction of becoming good at something

[![power platform community numbers](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fb3eugnprmv58wt2fzrlo.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fb3eugnprmv58wt2fzrlo.png)

Add in that you suddenly take away the barrier to entry, and you no longer have a mountain of [s&\*^%y apps](https://stevemordue.com/a-mountain-of-shitty-little-apps/), but the Pacific ocean of them. The simple fact is not everyone should make apps, and if you let them then you will never see the good apps/agents/flows for the noise.

If you want to see what the AI future is go see how many people follow the Microsoft Notepad community verses the Power Platform 😎

___

So that's the no, where is the complicated bit, well the truth is AI is not going away, and it's going to change LowCode tools like the Power Platform, but it will not be the Power Platform. Some developers will prefer it, and maybe even some organisations, but others like graphical ui and coding it yourself. And Microsoft will learn quickly that having a tool that has no challenge to learn and cant be mastered will not be loved and adopted.

I would love to see Microsoft taking a different approach, embedding AI into the Platform (and I don't mean slapping a Copilot on the side), imagine having the ability to create new components for your canvas app on the fly, that way you still:

-   Enable the developer to be creative and learn skills
-   Contain the AI code within a component - no issue from tech debt and limits security concerns
-   Focuses the expensive action to where it gets most value

Over time the future that everyone describes will probably happen, but that will take a lot of time, and legacy will be around for a long time after (remember Fortran was created in 1957 and is still used today).

   
[😎 Subscribe to David Wyatt](https://powerdevbox.com/blogs/subscribe?tracker=vibe-low)
