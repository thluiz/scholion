---
url: "https://garymarcus.substack.com/p/how-o3-and-grok-4-accidentally-vindicated?r=8tdk6&utm_campaign=post&utm_medium=web&triedRedirect=true"
captured_at: "2025-08-12T15:23:37+01:00"
title: "How o3 and Grok 4 Accidentally Vindicated Neurosymbolic AI"
domain: "garymarcus-substack-com"
---

---
[Machine learning](https://en.wikipedia.org/wiki/Machine_learning), the branch of AI concerned with tuning algorithms from data, is an amazing field that has changed the world — and will continue doing so. But it is also filled with closed-minded egotists with too much money, and too much power.

This is a story, in three acts, spanning four decades, about how many of them tried, ultimately unsuccessfully, to keep a good idea, [neurosymbolic AI](https://en.wikipedia.org/wiki/Neuro-symbolic_AI), down—only to accidentally vindicate that idea in the end.

§

For those who are unfamiliar with the field’s history, or who think it began only in 2012, AI has been around for many decades, split, almost since its very beginning, into two different traditions.

One is the [neural network](https://en.wikipedia.org/wiki/Connectionism) or “connectionist” tradition which goes back to the 1940s and 1950s, first developed by Frank Rosenblatt, and popularized, advanced and revived by Geoffrey Hinton, Yann LeCun, and Yoshua Bengio (along with many others, including most prominently, Juergen Schmidhuber who rightly feels that his work has been under-credited), and brought to current form by OpenAI and Google. Such systems are statistical, very loosely inspired by certain aspects of the brain (viz. the “nodes” in neural networks are meant to be abstractions of neurons), and typically trained on large-scale data. Large Language Models (LLMs) grew out of that tradition.

The other is the symbol-manipulation tradition, with roots going back to Bertrand Russell and Gottlob Frege, and John von Neumann and Alan Turing, and the original godfathers of AI, Herb Simon, Marvin Minsky, and John McCarthy, and even Hinton’s great-great-great-grandfather [George Boole](https://en.wikipedia.org/wiki/George_Boole). In this approach, symbols and variables stand for abstractions; mathematical and logical functions are core. Systems generally represent knowledge explicitly, often in databases, and typically make extensive use of (are written entirely in) classic computer programming languages. All of the world’s software relies on it.

For thirty years, I have been arguing for a reconciliation between the two, [neurosymbolic AI](http://www.apple.com/)_._ The core notion has always been that the two main strands of AI—neural networks and symbolic manipulation—_complement_ each other, with different strengths and weaknesses. In my view, neither neural networks nor classical AI can really stand on their own. We _**must**_ find ways to bring them together.

After a thirty-year journey, I believe that neurosymbolic AI’s moment has finally arrived, in part from an unlikely place.

_§_

In her bestseller _[Empire of AI](https://karendhao.com/)_, Karen Hao crisply sets the stage.

She begins by neatly distilling the _scientific_ tension.

> _Hinton and Sutskever continued \[after their seminal 2012 article on deep learning\] to staunchly champion deep learning. Its flaws, they argued, are not inherent to the approach itself. Rather they are the artifacts of imperfect neural-network design as well as limited training data and compute. Some day with enough of both, fed into even better neural networks, deep learning models should be able to completely shed the aforementioned problems. "The human brain has about 100 trillion parameters, or synapses," Hinton told me in 2020._
> 
> _"What we now call a really big model, like GPT-3, has 175 billion. It's a thousand times smaller than the brain._
> 
> _"Deep learning is going to be able to do everything," he said._
> 
> _Their modern-day nemesis was Gary Marcus, a professor emeritus of psychology and neural science at New York University, who would testify in Congress next to Sam Altman in May 2023. Four years earlier, Marcus coauthored a book called Rebooting AI, asserting that these issues were inherent to deep learning. Forever stuck in the realm of correlations, neural networks would never, with any amount of data or compute, be able to understand causal relationships-why things are the way they are-and thus perform causal reasoning. This critical part of human cognition is why humans need only learn the rules of the road in one city to be able to drive proficiently in many others, Marcus argued._
> 
> _Tesla's Autopilot, by contrast, can log billions of miles of driving data and still crash when encountering unfamiliar scenarios or be fooled with a few strategically placed stickers. Marcus advocated instead for combining connectionism and symbolism, a strain of research known as neuro-symbolic AI. Expert systems can be programmed to understand causal relationships and excel at reasoning, shoring up the shortcomings of deep learning. Deep learning can rapidly update the system with data or_ _represent things that are difficult to codify in rules, plugging the gaps of expert systems. "We actually need both approaches," Marcus told me._

She goes on to point out that the field has become an intellectual monoculture, with the neurosymbolic approach largely abandoned, and massive funding going to the pure connectionist (neural network) approach:

> _Despite the heated scientific conflict, however, the funding for AI development has continued to accelerate almost exclusively in the pure connectionist direction. Whether or not Marcus is right about the potential of neurosymbolic Al is beside the point; the bigger root issue has been the whittling down and weakening of a scientific environment for robustly exploring that possibility and other alternatives to deep learning._
> 
> _For Hinton, Sutskever, and Marcus, the tight relationship between corporate funding and AI development also affected their own careers._

Hao then captures OpenAI’s sophomoric attitude towards fair scientific criticism:

> _Over the years, Marcus would become one of the biggest critics of OpenAI, writing detailed takedowns of its research and jeering its missteps on social media. Employees created an emoji of him on the company Slack to lift up morale after his denouncements and to otherwise use as a punch line. In March 2022, Marcus wrote a piece for Nautilus titled "Deep Learning Is Hitting a Wall”, repeating his argument that OpenAI's all-in approach to deep learning would lead it to fall short of true AI advancements. A month later, OpenAI released DALL-E 2 to immense fanfare, and Brockman cheekily tweeted a DALL-E 2-generated image using the prompt "deep learning hitting a wall.” The following day, Altman followed with another tweet: "Give me the confidence of a mediocre deep learning skeptic." Many OpenAI employees relished the chance to finally get back at Marcus._

But then again, as the saying goes, he who laughs last, laughs loudest.

§

For all the efforts that OpenAI and other leaders of deep learning, such as Geoffrey Hinton and Yann LeCun, have put into running neurosymbolic AI, and me personally, down over the last decade, the cutting edge is finally, if quietly and without public acknowledgement, tilting towards neurosymbolic AI.

This essay explains what neurosymbolic AI is, why you should believe it, how deep learning advocates long fought against it, and how in 2025, OpenAI and xAI have accidentally vindicated it.

And it is about why, in 2025, neurosymbolic AI has emerged as the team to beat.

It is also an essay about sociology.

§

The essential premise of neurosymbolic AI is this: the two most common approaches to AI, neural networks and classical symbolic AI, have complementary strengths and weaknesses. Neural networks are good at learning but weak at generalization; symbolic systems are good at generalization, but not at learning.

Since my first book in 2001, [The Algebraic Mind](https://mitpress.mit.edu/9780262632683/the-algebraic-mind/), I have been arguing that three ideas drawn from classical symbol-manipulation are indispensable:

-   “Algebraic” systems such as algorithms, equations, and computer code, in which variables, and operations over those variables can be explicitly specified. In the equation, _y_ = 3_x_ + 2, _x_ and _y_ are variables, and one can instantiate (fill in) those variables with particular values, for example computing that _y_ = 11 if _x_ is set to 3. That sort of abstraction is the essence of computer programs. (Much of my empirical work as a cognitive scientist went toward showing that humans, even infants, could do something analogously algebraic).
    
-   Systems for explicitly representing structured, symbolic representations such that, for example, _horse rides astronaut_ systematically mean something different from _astronaut rides horse,_ and such that wholes can in general be predicted compositionally as a function of their parts.
    
-   Database-like systems for distinguishing individuals from kinds. In 2001, in the above-mentioned book, I warned that in their absence, hallucinations would emerge as a form of overgeneralization, which I warned was “an inevitable downside”. A quarter century later, hallucinations remain ubiquitous. Within a neural network substrate, the problem still has not been solved.
    

These three requirements might sound obvious—especially to someone trained in both computer science and cognitive science—but for decades the field of neural networks tried to make do without them.

Instead, until very recently, the consistent move by mainstream machine learning had been to try to derive all that is needed from data, without any recourse at all to symbolic systems such as traditional computer code, databases, etc., aiming to replace explicit representation with black boxes.

Over the years, many in the machine learning field derided attempts to use symbolic tools, often ridiculing them (without genuine argument) as being “not biologically plausible” or somehow (never really specified) in-principle ineffective.

§

Most iconic and influential among the detractors of neurosymbolic approaches has been Geoffrey Hinton.

Hinton has repeatedly argued that the pursuit of symbol-manipulation—even in the context of hybrid neurosymbolic models—is a huge scientific mistake. In a 2015 [workshop](https://sites.google.com/site/krr2015/home/schedulehttps:/sites.google.com/site/krr2015/home/schedulehttps:/sites.google.com/site/krr2015/home/schedulehttps:/sites.google.com/site/krr2015/home/schedule) at Stanford, for example, Hinton gave a talk that claimed that classical AI symbols were “as incorrect as the belief that a lightwave can only travel through space by causing disturbances in the luminiferous aether.”

Another time, in 2018, Hinton [told an audience of the G7](https://x.com/tabithagold/status/1070736319901519876?s=61) to great laughs that hybridizing neural networks and symbolic systems (which is to say neurosymbolic AI) was [as foolish as sticking electricity onto a gas engine instead of just making an electric car](https://x.com/tabithagold/status/1071189769499996161?s=61), arguing that “all progress recently \[has come from\] sucking in data, not from people putting programs inside.”

(Some of this was driven by a scrabbling over funding, with Hinton alleging that investing in classical AI, and, by extension, hybrid neurosymbolic models, would be “a disaster.”)

§

Hinton’s long-time hostility against any role at all for symbols has, in my judgement, cost the field dearly. Ideas that were were only discovered in the last couple years (e.g., some discussed later in this essay) may have been discovered much later than they might otherwise have been.

Many other important ideas have likely also yet to be discovered, precisely because the Hinton path has distracted immense resources from other ideas, fostering an intellectual monoculture that, in the words of Emily Bender, has been “sucking the oxygen from the room.”

First among the big players to look more broadly was Google DeepMind, which wisely has not taken Hinton’s dogma overly seriously. AlphaFold, AlphaProof, and AlphaGeometry [are all successful neurosymbolic models](https://open.substack.com/pub/garymarcus/p/alphaproof-alphageometry-chatgpt?utm_campaign=post&utm_medium=web). We would likely have more of such innovation already, if Hinton had not so insistently shaped the modern landscape in such a narrow-minded way.

To the extent that we are stuck for now with untrustworthy LLMs that nobody can quite control, rapidly enshittifying the internet with [botshit](https://open.substack.com/pub/garymarcus/p/botshit-gone-wild?r=8tdk6&utm_campaign=post&utm_medium=web&showWelcomeOnShare=false) and [replacing humans with systems that can’t be relied on](http://www.apple.com/), it is in part because we have spent too much energy pursuing the pure neural net black box approach, and not enough into looking at alternatives. We are drowning in a sea of mediocre prose precisely because LLMs, the backbone of virtually all current sytems, lack the underlying representational wherewithal to do better.

Yet nearly all funding has been aimed simply at making them larger.

§

Despite the often open hostility of Hinton and many of his followers, I have always stuck to my guns, never arguing that we should dispense with deep learning (a commonly-repeated strawman) but always calling, instead, for a _hybrid_ of deep learning and symbols.

In my 2018 [Deep Learning: A Critical Appraisal](https://arxiv.org/abs/1801.00631) for example, I wrote

> _Despite all of the problems I have sketched, I don’t think that we need to abandon deep learning._
> 
> _Rather, we need to reconceptualize it: not as a universal solvent, but simply as one tool among many, a power screwdriver in a world in which we also need hammers, wrenches, and pliers, not to mentions chisels and drills, voltmeters, logic probes, and oscilloscopes._

As we will see in a moment, people are finally pursuing a tool-driven, neurosymbolic vision like this — and getting better results than they were able to get with pure neural networks.

People tend to remember that paper for its criticism. There was a long discussion of the weakness of models that that were then-current, including their difficulties in out-of-domain generalization, with abstraction, and with reasoning, and their overreliance on massive data.

But one of the main points of the paper was its call for the integration of neural networks and symbols:

> _Another place that we should look is towards classic, “symbolic” AI, sometimes referred to as GOFAI (Good Old-Fashioned AI). Symbolic AI takes its name from the idea, central to mathematics, logic, and computer science, that abstractions can be represented by symbols. Equations like f = ma allow us to calculate outputs for a wide range of inputs, irrespective of whether we have seen any particular values before; lines in computer programs do the same thing (if the value of variable x is greater than the value of variable y, perform action a)._
> 
> _By themselves, symbolic systems have often proven to be brittle, but they were largely developed in \[an\] era with vastly less data and computational power than we have now. The right move today may be to integrate deep learning, which excels at perceptual classification, with symbolic systems, which excel at inference and abstraction. One might think such a potential merger on analogy to the brain; perceptual input systems, like primary sensory cortex, seem to do something like what deep learning does, but there are other areas, like Broca’s area and prefrontal cortex, that seem to operate at much higher level of abstraction. The power and flexibility of the brain comes in part from its capacity to dynamically integrate many different computations in real-time._

§

The leaders of deep learning hated me for challenging their baby, and couldn’t tolerate any praise for the paper. When an influential economist Erik Brynjolfsson (then at MIT) complimented the article on Twitter, (“Thoughtful insights from @GaryMarcus on why deep learning won't get us all the way to artificial general intelligence”), Hinton’s long time associate Yann LeCun tried to contain the threat, immediately replying to Brynjolffson publicly that the paper was “Thoughtful, perhaps. But mostly wrong nevertheless.”

LeCun was never able to articulate his concerns, but his remark wasn’t about the science. Instead, it was a signal to thefield that my views should be rejected; literally hundreds of people piled on. (Few seem to have noticed the irony that came a few years later, when LeCun ultimately came around to making almost exactly the same points I was making then, declaring, e.g., that [pure LLMs are not an adequate route to AGI, and emphasizing their limits in reasoning](https://youtu.be/4__gg83s_Do?si=ZizMmCqmHiAZRUTW&utm_source=MTQxZ).)

§

The story was similar when my 2022 article [Deep Learning is Hitting a Wall](https://archive.ph/6hEYS) came out. The first part of the paper was negative argument against a hypothesis that was then popular: “[Scale is all you need](https://subcriticalappraisal.com/2022/AGI-Scale-Is-All-You-Need/).”

I argued that scaling as it was then defined (pretraining data and compute) alone was insufficient to solve challenges with reasoning, misalignment and hallucinations. (Spoiler alert: it still hasn’t.)

The second part was an argument that neurosymbolic AI might be a way out of this mess:

> _Early pioneers, like John McCarthy and Marvin Minsky, thought that one could build AI programs precisely by extending these techniques, representing individual entities and abstract ideas with symbols that could be combined into complex structures and rich stores of knowledge, just as they are nowadays used in things like web browsers, email programs, and word processors. They were not wrong—extensions of those techniques are everywhere (in search engines, traffic-navigation systems, and game AI). But symbols on their own have had problems; pure symbolic systems can sometimes be clunky to work with, and have done a poor job on tasks like image recognition and speech recognition; the Big Data regime has never been their forté. As a result, there’s long been a hunger for something else._
> 
> _That’s where neural networks fit in \[solving problems from data where rules are hard to construct\]…_
> 
> _To me, it seems blazingly obvious that you’d want both approaches in your arsenal._
> 
> _… “hybrid models” that incorporate elements of both deep learning and symbol-manipulation… To think that we can simply abandon symbol-manipulation is to suspend disbelief._

Animosity, rather than genuine intellectual engagement, was again the main result. Thousands of people, from Altman to Musk, insulted me and the paper (Hao listed two of the many examples). LeCun wrote on Facebook, in May 2022, a few months before he turned against LLMs, “Not only is Al not "hitting a wall", cars with Al-powered driving assistance aren't hitting walls, or anything else, either.” Musk circulated [a meme that mentioned me which featured a cartoon of deep learning-powered robot smashing over walls and buildings](https://x.com/elonmusk/status/1796795162028335377?s=61). (An accidental forewarning of all the damage that recklessly-rolled out LLMs have started to cause?)

§

Three years later, the pure scaling of pretraining data (and compute, which is to say more and more GPUs) simply hasn’t worked. The specific obstacles that I dwelled on, with respect to hallucinations, misalignment and reasoning errors, have not been overcome.

This started to became clear in November. One of the first insiders to publicly acknowledge it was Marc Andreesen, who said in a November 2024 interview that multiple models were “[sort of hitting the same ceiling on capabilities](https://observer.com/2024/11/vc-andreessen-horowitz-ai-models-hitting-wall/)”; Microsoft CEO Satya Nadella [soon more or less acknowledged the same](https://garymarcus.substack.com/p/satya-nadella-and-the-three-stages) (“in the last … weeks there \[has been\] a lot of debate \[on whether we\] have we hit the wall with scaling laws”).

§

What _has_ worked—to some degree—is importing some of the ideas from neurosymbolic AI, including using purely symbolic algorithms as a direct part of the workflow.

OpenAI quietly began doing this to some degree in 2023 with a system called “[code interpreter](https://beebom.com/chatgpt-code-interpreter/)”, in which LLMs (themselves neural networks) call (purely symbolic) Python interpreters. This is literally “putting programs inside”; exactly what Hinton said was a huge mistake. And they are _innately_ building in that capacity, rather than learning it.

Sometimes, not always, when a system like o3 calls Python, the symbolic code is actually reported explicitly:

```
from PIL import Image, ImageDraw
# Grid size for 60 fruits
rows, cols = 6, 10 #6 × 10= 60

radius = 45
spacing = 25

canvas_width - cols * (2 * radius + spacing) + spacing
canvas_height = rows * (2 * radius + spacing) + spacing

img = Image.new ("RGB", (canvas_width, canvas_height), "white")
draw = ImageDraw. Draw(img) 

# Colors
apple_color = (220,0,0)#deepred
…
```

As leading machine learning expert Francois Chollet [explained last year on X, such systems are manifestly neurosymbolic](https://x.com/fchollet/status/1802785277758591054?s=61),

> “Obviously combining a code interpreter (which is a symbolic system of enormous complexity) with an LLM is neurosymbolic. AlphaGo was neurosymbolic as well. These are universally accepted definitions.”

Recent “reasoning” models borrow even more from classic symbolic approaches, such as techniques like search and conditionally iterating through multiple solutions, and aggregating the results, techniques that traditional networks had long eschewed, in favor of a single feed-forward pass through a neural net.

From what I can tell, most modern models also make heavy use of data augmentation that involves (_inter alia_) running systems of symbolic rules and training on their outputs, a far cry from the original notion of training on naturalistically-observed data and then inducing whatever needed to be learned. (Details on how all this is implemented are sketchy, with companies like OpenAI saying almost nothing about implementation. DeepSeek has been a notable exception, explicitly acknowledging the use of symbolic rules in generating their training data.)

GPT-2 was a pure LLM; with no direct use of symbol-manipulation. A lot of models since then haven’t been. GPT-4 probably wasn’t (I suspect it included some symbolic filters in its guardrails), and o3, when it invokes code interpreter and symbolically-executed control structures certainly isn’t.

Intriguingly, o3 itself seems to know (pardon my anthropomorphic shorthand) a bunch about this, recognizing that it needs to draw on the (symbolic) code interpreter for certain kinds of problems:

[

![](https://substackcdn.com/image/fetch/$s_!8vW8!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F82c14711-5019-49f3-a057-2bda8470c064_1463x1200.png)

](https://substackcdn.com/image/fetch/$s_!8vW8!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F82c14711-5019-49f3-a057-2bda8470c064_1463x1200.png)

§

Both informal experimentation and a number of recent quantitative results make it abundantly clear that current generative AI systems perform better when they avail themselves of symbolic tools. (Again, per Chollet, when you combine an LLM with a symbolic tool, you have a neurosymbolic system.)

The much-discussed Apple paper was one hint: the authors explicitly forced LLMs to do various tasks, such as Tower of Hanoi, without recourse to using code (symbolic by definition), and it’s under that scenario that they found breakdowns, such as failures on Hanoi with 8 rings.

Another research group, explicitly responding to the Apple paper, showed how you could [get much better performance on problems like Hanoi by having models like o3 explicitly invoke code](https://arxiv.org/pdf/2506.18957).

I have found similar results in my own informal experiments, when looking at algorithmic processes. ChatGPT (which doesn’t as far as I can tell) currently use Code Interpreter, struggles mightily to draw crosswords grids, as Haym Hirsch recently noted, making weird errors like reporting that 4 down here is “REACT” when it as actually an illegal word, “RCRCT”:

```
S T A R T 
T R A C E
A C O R N 
R E A C T 
T E N T S
```

In contrast, o3, when it draws on symbolic code (which it sometimes displays explicitly) can build crossword grids like this far faster than I could (short of my writing my own code).

> ```
> T R A S H
> R E P A Y
> A P P L E
> S A L O N
> H Y E N A
> ```

§

The results that seal the deal came a few nights ago, at the launch of Grok 4, perhaps the largest and most expensive model in history. (Elon Musk claims it used 100 times the compute of Grok 2.)

This graph (of a challenging benchmark known as Humanity’s Last Exam) is without question one of the most vindicating things I have ever seen:

[

![](https://substackcdn.com/image/fetch/$s_!X-UT!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0216b312-7b2b-4fac-9de3-630c4eeabec0_1884x1089.jpeg)

](https://substackcdn.com/image/fetch/$s_!X-UT!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0216b312-7b2b-4fac-9de3-630c4eeabec0_1884x1089.jpeg)

Why? Two things can be seen.

First, the lower set of data (yellow dots) represent a strong test of the pure scaling hypothesis. Although the units on the X axis aren’t made clear, it’s quite clear that _pure scaling_ _of training data and computer is reaching a point of diminishing returns, a long way from peak possible performance_. Contrary to lots of talk from previous years, increasing compute alone is not driving some miraculous exponential explosion into superintelligence.

Second, _adding symbolic tools (orange dots) dramatically improves performance._

(Scaling test time is also, as far as I understand it, drawing on classic symbolic techniques for iteration and aggregation.)

You can see this in other benchmarks, too. On this math competition, adding symbolic tools make a big difference:

[

![](https://substackcdn.com/image/fetch/$s_!Ep9L!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fad041574-c0ba-4960-b8d4-37734a243122_916x1059.jpeg)

](https://substackcdn.com/image/fetch/$s_!Ep9L!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fad041574-c0ba-4960-b8d4-37734a243122_916x1059.jpeg)

In short, although LLMs are still far from perfect, enhancing them with symbolic tools, once an anathema, makes a huge difference. Between the strong success of DeepMind’s series of neurosymbolic hybrids (AlphaGo, AlphaFold, AlphaProof, AlphaGeometry, etc.) and the more recent results in which LLMs have been enhanced with python and other tools to dramatic effect, we can safely conclude that neurosymbolic AI is on track to be a major part of AI’s future.

§

None of which means we are close to AGI. There are many ways to put together symbols and neural nets. I am not at all convinced we have the right one.

Bolting code interpreters onto LLMs has value, but whether it gets us to AGI is a different matter. A neurosymbolic substrate for AI by itself ([as I argued in 2020](https://arxiv.org/abs/2002.06177)) is likely to be **necessary but not sufficient**. [Advances in neurosymbolic AI are likely to be just one part of a larger picture](https://arxiv.org/abs/2002.06177). As Peter Voss has argued (and I agree) we need far more integration than a mere bolt-on would provide. Including LLMs _somewhere_ in the next evolution of AI makes sense to me, but leaving them at the core may be a mistake.

Models like o3 are far better than non-code-interpreter systems on some tasks but not all (for now o3 is actually worse than o1 on hallucinations) and effective for some tasks, but not others. Core problems like “symbol-grounding” have not been systematically solved, for example. Explicit cognitive models ([as I discussed recently in this newsletter](https://garymarcus.substack.com/p/generative-ais-crippling-and-widespread?r=8tdk6)) are also likely to be essential, yet remain very much underexplored. Reasoning is still unreliable; spatial reasoning is a long way from solved, as [Fei-Fei Li has recently argued](https://spectrum.ieee.org/fei-fei-li-world-labs). We still also (just as I argued in 2020) lack [proper ways of building and inferring symbolic world/cognitive models on-the-fly](https://arxiv.org/abs/2002.06177). And we may need more [discipline in how we tie semantics to the symbolic components of our systems](https://cs.nyu.edu/~davise/papers/McDTarskianSemantics.pdf). There is likely still a great deal of work left to be done.

Reality is maybe a bit like a [cartoon I recently posted on X](https://x.com/garymarcus/status/1944059904534229090?s=61). A hiker climbs across a mountain range, impressively far along (“you are here”), but nowhere near the highest peak (“AGI”). We have made some progress; we still likely have a long way to go.

§

Still, even at our current vantage point, having solved some problems but by no means all, there are several lessons we can draw:

-   Systems that draw on code interpreter, and hence by definition are neurosymbolic, often outperform those that lack symbolic tools, at least in a bunch of tasks. **This is confirmation of the value of neurosymbolic AI.**
    
-   Hinton’s admonition against using symbolic AI was extraordinarily misguided, and probably delayed discovery of useful tools like Code Interpreter by years. Largely because of Hinton’s influence, the field still talks about neurosymbolic AI as if it were a dirty word. That’s likely holding back the science.
    
-   It’s likely that OpenAI, Anthropic and others are already doing more neurosymbolic AI than they actually make public. They still pretend it’s all “a model” but that model uses all kinds of tricks and mixtures with tools, code generation etc.
    
-   A lot of recent improvements are likely coming from improvements in using symbolic tools, rather than scaling. Massive infrastructure investments like Stargate are likely based on misleading impressions of what is actually driving progress.
    
-   It would appear that it is only recently, in desperation, as scaling started to reach diminishing returns, that mainstream machine learning began to broaden its vistas.
    
-   Where the field is getting stuck now is likely on how to scale these new, neurosymbolic tools and how to make models “understand” when to use what and how to logically combine the context. This is why so called “code agents” inevitably fall apart as soon as one gives them a more complex task which requires reasoning.
    
-   The code construction itself is still produced by a system that is [highly dependent on similarity to training examples](https://arxiv.org/pdf/2410.06235). In easy, familiar cases, the results can be astonishing. In problems that diverge from easy and familiar cases, the constructed code can be buggy, or altogether flawed. As Phil Libin put it to me, “trying to improve the results \[of o3\] by continuing to talk with it rarely works after the first few prompts… It’s either gonna get it right in 5 minutes, or never.”
    
-   Neurosymbolic AI is not one thing, but many. o3’s use of neurosymbolic AI is very different from AlphaFold’s use of neurosymbolic AI. Very little of what has been tried has been discussed explicitly, and because the companies are often quite closed about what they are doing, the public science of neurosymbolic AI is greatly impoverished.
    
-   Getting to AGI will likely take still more breakthroughs. The best way to foster them is to have an intellectually open attitude. It would be great if we could see more of that.
    

§

_Why_ was the industry so quick to rally around a connectionist-only approach and shut out naysayers? Why were the top companies in the space seemingly shy about their recent neurosymbolic successes?

Nobody knows for sure. But it may well be as simple as money. The message that we can simply scale our way to AGI is incredibly attractive to investors because it puts money as the central (and sufficient) force needed to advance.

Admitting that they need to rely on neurosymbolic tools would pierce the scaling narrative.

§

So here’s where we are: pure LLMs can’t reliably apply algorithms (vindicating the line of argument I first developed in the 1990s); if you enhance them with symbolic processes—yielding neurosymbolic systems—they often give better results.

OpenAI, without any sort of of public acknowledgement whatsoever, has accidentally vindicated neurosymbolic AI.

Fostering its further development may be among the best things that companies, researchers, and governments can do. Investors, take note.

_**Gary Marcus** has been pushing for neurosymbolic AI throughout his career, since the early 1990s, and could not be more thrilled to see it start to blossom._
