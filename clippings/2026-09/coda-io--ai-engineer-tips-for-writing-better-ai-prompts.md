---
url: "https://coda.io/blog/ai/ai-engineer-tips-ai-prompts?canvas_id=&lid=w9ff75a7j2wf"
captured_at: "2026-09-24T23:14:49+01:00"
title: "An AI engineer’s tips for writing better AI prompts"
domain: "coda-io"
---

AI

· 6 min read

We’ve all had a bit of time now to get used to using consumer AI tools like ChatGPT, and many of us are using them daily to answer simple questions and generate content. As [enterprise AI](https://coda.io/blog/ai/enterprise-ai-vs-consumer-ai) enters the picture, using AI for more complex work tasks will soon become the norm, too. This unlocks a whole new level of value—and one of the best ways to maximize it is to optimize not only what you ask the AI to do, but also _how_ you ask. I’m an engineer working on Coda’s turnkey AI platform, [Coda Brain](https://coda.io/blog/about-coda/introducing-coda-brain), so I’m intimately familiar with how prompts work and what’s happening in the background. Better AI prompts lead to higher precision, increased efficiency, and a more tailored experience. Let me share four tips for crafting effective prompts, especially when you’re using AI for [more than just simple answers.](https://coda.io/blog/ai/enterprise-ai-more-than-answer-questions)

[

## 1\. Know that more is more (details, that is).

](#3efc89142877)

The more details and context you include in your initial prompt, the better the outcome will be—especially when asking AI to generate content. Large language models (LLMs) are designed to please by following instructions, so the more information you give it, the more it will try and weave that into its answer. For example, let’s say we’re asking AI to help us write a happy birthday email for our teammate, Jane. A basic prompt would be something like “Help me write an email to Jane to say happy birthday.” With this prompt, you’ll get a good enough message to customize further, but you might find it to be a little bland and robotic. The tone may also not be what you were hoping for—sometimes the sentiments can seem trite or even sarcastic.

![](https://sanity-images.imgix.net/production/ead3ae936ea90b157639678206b13c08af36bfa4-1156x742.png?w=2000&auto=format%2Ccompress)

A better prompt might be something like, “Help me write a short 30th birthday email to my teammate and project manager, Jane. She’s going to Palm Springs to celebrate and recently adopted a puppy called Rex, so be sure to mention that in the email.” The email will be a much more specific draft, with fewer edits needed to personalize it.

![](https://sanity-images.imgix.net/production/d432acd87eb48b1c663b9a9fbdc84db6060c48ca-1178x784.png?w=2000&auto=format%2Ccompress)

One thing to note is that while more detail is good, there is such as thing as _too_ much detail in a prompt. For example, if you write several pages of detailed instructions, there is no guarantee that the result will abide by all or even a high percentage of them—keeping it to a few lines will get you a better result.

[

## 2\. Ask your AI to adopt a persona.

](#e607e32991d1)

Asking your AI to adopt a persona can help immensely in getting a response in the tone you’re hoping for. By narrowing your prompt to a persona or situation, you’re refining the AI’s understanding to match more closely with actual patterns it has seen across multitudes of training data. The resulting responses should therefore be more accurate to your scenario. You can easily try this out by asking for your response as if from a pirate, or imagining you’re an overzealous IT manager messaging Jane before her trip:

![](https://sanity-images.imgix.net/production/9e3086637750a0580607523532750d44a657901f-1396x742.jpg?w=2000&auto=format%2Ccompress)

But, more practically, a persona can be especially helpful for giving the AI context when asking for feedback. For example, imagine asking AI for feedback on your product requirements document (PRD) to find potential considerations you might have missed in your plan. Rather than just “Give me feedback on this PRD,” you could ask the AI something like “You’re a CPO at a startup that needs to double its revenue this year. You particularly care about customer experience and attracting enterprise clients. Give me feedback on this PRD for a new potential feature.” The feedback it gives will be much more targeted and specific this way.

[

## 3\. Provide examples of what you want.

](#5cf33f9e217b)

If you’re using AI for a repetitive data task, you likely need highly consistent results. In this case, specifying the desired format of the answer and including some realistic examples will guide the AI to generate better responses. For example, imagine you have a table of customer messages about your latest product release and want a quick view of the sentiment. You can use [Coda’s AI columns](https://help.coda.io/en/articles/7988177-coda-ai-features#h_ce9d30ee6e) to do this automatically by just writing, for example, “Find sentiment in @<email column>.” But an even better prompt would be something like “Analyze the sentiment @<email column>. Return positive, neutral, or negative.” And an _even better_ prompt would include examples, like this:

![](https://sanity-images.imgix.net/production/4c6f992d34270e7f846cb009186c11a4319e0f62-1135x511.png?w=2000&auto=format%2Ccompress)

As with the “giving more details” tip above, this works because LLM behavior is tuned to follow instructions. When you give it direction—like a structure to follow—it will try and adhere to it as much as possible. The more examples, the better it gets at following the pattern. It might seem like more work up front, but it’s worth doing so that you get exactly what you need the first time without going back and forth with additional prompts.

[

## 4\. Break down complex tasks.

](#b84493e50d09)

The things AI can do are pretty astounding, but no AI is perfect. When you’re using AI to perform more complex tasks, it can be helpful to break it down into steps to increase the accuracy of its response. Let’s take our PRD example again, and imagine we’re pitching to build a new desktop app. Assuming you’re using an enterprise AI like [Coda Brain](https://coda.io/product/coda-brain) that has access to your own data (not just the general internet), that might look something like this:

1.  You ask “Find previous explorations about a desktop app.” Coda Brain finds all previous writeups about a desktop app and summarizes them for you.
2.  You then ask Coda Brain to retrieve data to back up your pitch. For example, “Show me customer feedback about desktop apps,” and Coda Brain will bring back data from your connected tools. That might be win/loss data logged in Salesforce, or customer messages from Intercom.
3.  Next, you ask “Find a template for a PRD.” Coda Brain delivers your company’s usual PRD template (or a selection, if you have multiple).
4.  Finally, you ask Coda Brain to do a first draft of the PRD using the template and data it found, which you can then edit as needed.

Clearly, Coda Brain has saved you a ton of time and effort in this example. But it would be difficult to ask for this all-in-one prompt, so breaking it down like this helps to get what you need. For some tasks that have more linear steps, you can also ask AI to break down the task itself, so you can see what it’s going to do. For example, you might ask “Tell me the top 10 reasons to use Coda over another tool for project management. First, tell me the steps you’re going to take to do so.” The AI will share its process, which you can check or adjust before telling it to proceed.

![](https://sanity-images.imgix.net/production/7636ce3cd2d9c03b4260622159626c24fea1fbc4-1170x604.png?w=2000&auto=format%2Ccompress)

We actually built Coda Brain to automatically show you the steps it’s taking as it’s working. For example, if you ask “Show me sales opportunities over $10k,” you would be able to see that it first went to Salesforce, then which table it chose, which filters it applied, and so on. You can then adjust this if needed—say if it included all opportunities but you only wanted ones from the USA, or if you wanted it to fetch data from a different tool instead. This approach, called “human-in-the-loop”, means you can better trust the output and easily fine-tune it to fit your specific needs.

[

## There’s no such thing as the perfect prompt.

](#898066a0e654)

In summary, adding detail, adopting personas, providing examples, and breaking down complex tasks in your prompts goes a long way to getting more accurate and relevant AI responses. However, it’s important to remember that—due to the complexities and nuances of work—there are always going to be times when AI doesn’t quite hit the mark. It’s good practice to always proofread and “touch up” AI-generated content, no matter how good your prompt is. Try these techniques out and let me know how you get on! If you’re ready to explore the full potential of enterprise AI with Coda Brain, [sign up for our private preview](https://coda.io/contact/sales/coda-brain) and step into the future of work. Or, you can learn more about [Coda AI here](https://coda.io/product/ai).
