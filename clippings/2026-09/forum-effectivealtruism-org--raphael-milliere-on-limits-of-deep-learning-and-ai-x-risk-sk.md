---
url: "https://forum.effectivealtruism.org/posts/TecosAABRtPhaNdrL/raphael-milliere-on-the-limits-of-deep-learning-and-ai-x"
captured_at: "2026-09-25T19:17:49+01:00"
title: "Raphaël Millière on the Limits of Deep Learning and AI x-risk skepticism"
domain: "forum-effectivealtruism-org"
---

_(crossposted from_ [_LessWrong_](https://www.lesswrong.com/posts/HzCFRvrHYFsCixWRs/raphael-milliere-on-generalization-compositionality-and)_)_

I interviewed Raphaël Millière, a Presidential Scholar in Society and Neuroscience at Columbia University about his critic of “[scaling maximalism](https://twitter.com/raphaelmilliere/status/1526568402600480768)” and his takes on AGI. This is part of an on-going effort where I talk to people who are skeptical of existential risk from AI so that everyone can better steelman their arguments (cf. [why you might want to talk to skeptics](https://forum.effectivealtruism.org/posts/BqokXcCQrvkk2BktH/blake-richards-on-why-he-is-skeptical-of-existential-risk)).

## Why I Interviewed Raphaël

Although we disagree on most topics, Raphaël follows closely current state of the art research in deep learning, is impressed by current advances, yet still completely disregards existential risk from AI. The reasons for his (supposedly contradictory) beliefs are related to the potential limitations of deep learning in terms of understanding, compositionality and generalization, which are shared by popular AI skeptics such as Gary Marcus or François Chollet.

_Below are some quotes of Raphaël said during his interview. You can find them in full context_ [_here_](https://theinsideview.ai/raphael)_._

## Three levels of Generalization, the Wozniak Test

> Maybe one distinction that's helpful there, is again from François Chollet's [paper](https://arxiv.org/abs/1911.01547) on the measure of intelligence, which I quite like, is this distinction between, I think it distinguishes between three levels of generalization.
> 
> *   So you have **local generalization**, which is a narrow form of generalization that pretends to generalize to known unknowns. So within a specific task. So that can be just, for example, you have a classifier that classifies pictures of dogs and cats, and then you can generalize to unseen examples, at test time, that it hasn't seen during training. So that's local generalization is just within domain known unknowns in a specific task.
> *   Then there is what he calls **broad generalization**, that's generalizing to unknown unknowns within a broad range of tasks. So the examples he gives there would be level five self-driving or there was the Wozniak test, which was proposed by Steve Wozniak, which is building a system that can walk into a room, find the coffee maker and brew a good cup of coffee. So these are tasks or capacities that require adapting to novel situations, including scenarios that were not foreseen by the programmers where, because there are so many edge cases in driving, or indeed in walking into an apartment, finding a coffee maker of some kind and making a cup of coffee. There are so many potential edge cases. And, this very long tail of unlikely but possible situations where you can find yourself, you have to adapt more flexibly to this kind of thing.
> 
> And so that requires this broader generalization. And then there is a value question about this level two from Chollet about where do current models fit? Can we say that current language models are capable of some kind of project generalization because of their few-shot learning capacities? I suspect Chollet would say no, because **there is a difference between being able to perform tasks that you haven't been explicitly trained to do, which is what's happening with few-shot learning**.
> 
> \[...\]
> 
> And given the training set of GPT-3 and PaLM, that includes a bunch of text talking about arithmetic and involving math problems and so on, you might very reasonably say that arithmetic tasks are not really out of distribution, right? **They're within the training set. So I suspect Chollet I would say we're not yet at broad generalization.**

## Contra Scaling Maximalism

> You hear people talking about scaling laws as if it's plotting model size or dataset size against intelligence as if we had some kind of metric of intelligence, but it's just measuring  autoregressive, the loss of autoregressive models or the decreasing loss, right? So as they're predicting the next token and that's at best a proxy for some perhaps slightly narrow in shorter sense of intelligence. **We can't readily extrapolate from that to some kind of scaling law about something like human general intelligence**. So that's the first point I want to make. We have to be careful that **these plots are specifically about improvements in the predictions of autoregressive transformers**. 
> 
> And then there are the other things that you mentioned that, the scaling maximalists tend to go quickly over things like changes to the architecture. And one point that I made in my thread on that was that **if you take the scaling is all you need view literally, it's literally false or absurd** because even of the various recent models that have led people to lend more credence to that view, such as DALLE-2 Gato, PaLM, Imagen, and others, **all of these required some at least minor architectural innovation or minor tweaks to existing architecture**. So they did require some changes to the architecture. They're not just scaling transformers and seeing what happens. So that's one point.
> 
> And then the other point you made is about **the kind of data you fit to the model and how perhaps how you format your data, what different modalities you include, how you serialize it, how you fit it to the model, all of this matters a lot.** And the Gato paper, for example, shows some innovation in that respect as well. **There's some innovative ways to serialize, both discrete and continuous data**. So button presses, joint torques, text, images, in a way that is suitable to be fed to a transformer.
> 
> \[...\]
> 
> **You can't just learn anything if you don't have some kind of inductive bias**. The real question is how much inductive bias and how much prior knowledge \[the model\] needs. That's also the crux of the disagreement between Gary and Yann LeCun.

## What Would Make Him Change His Mind on Scaling

> I think if Raphaël from the future showed me **something that's basically similar to current transformers can reach human level at some of the hardest benchmarks we have today, such as Chollet's** [**ARC challenge**](https://github.com/fchollet/ARC)**, all of the** [**BIG bench**](https://github.com/google/BIG-bench) **tasks, things like the** [**Winoground**](https://arxiv.org/abs/2204.03162) **benchmark** that came roughly about like compositional and vision language models.
> 
> If you can do all of this just by having massive models with minimal changes to the architecture that would give me pause, certainly. I think that would give me pause and perhaps lead me to have more faith in emergent features of transformer models at scale.

## On Goalpost Moving

> "The first thing I would say is that it's perfectly consistent to be impressed by what something is doing, and yet cogently discuss the remaining limitations of that thing. Right? Otherwise, we'd just be like, "Oh, okay, pack it up guys. We have DALL·E 2, that's all we need. There is no further improvement we can obtain in AI research. This is the pinnacle of artificial intelligence." No one is saying this. So, come on. If we want progress, the basic first step is to lucidly evaluates the limitations of current systems.
> 
> My personal view on this is that **we are making progress towards more general intelligence**. And I like to think of this as in this more relativistic or relational terms, **we are increasing the generality of the generalization capacities of models** we've been talking about this in this very podcast awhile back. **But we haven't yet reached the kind of extreme generalization that humans are capable of**. And these two things are very consistent with one another, right?"

20

More posts like this

43

What were mistakes of AI Safety field-building? How can we avoid them while we build the AI Welfare?

63

Blake Richards on Why he is Skeptical of Existential Risk from AI

161

"No-one in my org puts money in their pension"
