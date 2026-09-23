---
url: "https://24ways.org/2016/we-need-to-talk-about-technical-debt/"
captured_at: "2026-09-23T17:29:31+01:00"
title: "We Need to Talk About Technical Debt ◆ 24 ways"
domain: "24ways.org"
---
We Need to Talk About Technical Debt

Harry Roberts

5 December 2016
Published in Code
6 comments

In my work with clients, a lot of time is spent assessing old, legacy, sprawling systems and identifying good code, bad code, and technical debt.

One thing that constantly strikes me is the frequency with which bad code and technical debt are conflated, so let me start by saying this:

Not all technical debt is bad code, and not all bad code is technical debt.

Sometimes your bad code is just that: bad code. Calling it technical debt often feels like a more forgiving and friendly way of referring to what may have just been a poor implementation or a substandard piece of work.

It is an oft-misunderstood phrase, and when mistaken for meaning 'anything legacy or old hacky or nasty or bad', technical debt is swept under the carpet along with all of the other parts of the codebase we'd rather not talk about, and therein lies the problem.

We need to talk about technical debt.

What We Talk About When We Talk About Technical Debt

The thing that separates technical debt from the rest of the hacky code in our project is the fact that technical debt, by definition, is something that we knowingly and strategically entered into. Debt doesn't happen by accident: debt happens when we choose to gain something otherwise-unattainable immediately in return for paying it back (with interest) later on.

An Example

You're a front-end developer working on a SaaS product, and your sales team is courting a large customer – a customer so large that you can't really afford to lose them. The customer tells you that as long as you can allow them to theme your SaaS application according to their branding, they are willing to sign on the dotted line… the problem being that your CSS architecture was never designed to incorporate theming at all, and there isn't currently a nice, clean way to incorporate a theme into the codebase.

You and the business make the decision that you will hack a theme into the product in two days. It's going to be messy, it's going to be ugly, but you can't afford to lose a huge customer just because your CSS isn't quite right, right now. This is technical debt.

You deliver the theme, the customer signs up, and everyone is happy. Except you (and the business, because you are one and the same) have a decision to make:

Do we go back and build theming into the CSS architecture as a first-class citizen, porting the hacked theme back into a codified and formal framework?
Do we carry on as we are? Things are working okay, and the customer paid up, so is there any reason to invest time and effort into things after we (and the customer) got what we wanted?

Option 1 is choosing to pay off your debts; Option 2 is ignoring your repayments.

With Option 1, you're acknowledging that you did what you could given the constraints, but, free of constraints, you'd have done something different. Now, you are choosing to implement that something different.

With Option 2, however, you are avoiding your responsibility to repay your debt, and you are letting interest accrue. The problem here is that…

your SaaS product now offers theming to one of your customers;
another potential customer might also demand the ability to theme their instance of your product;
you can't refuse them that request, nor can you quickly fulfil it;
you hack in another theme, thus adding to the balance of your existing debt;
and so on (plus interest) for every subsequent theme you need to implement.

Here you have increased entropy whilst making little to no attempt to address what you already knew to be problems.

Your second, third, fourth, fifth request for theming will be hacked on top of your hack, further accumulating debt whilst offering nothing by way of a repayment. After a long enough period, the code involved will get so unwieldy, so hard to work with, that you are forced to tear it all down and start again, and the most painful part of this is that you're actually paying off even more than your debt repayments would have been in the first place. Two days of hacking plus, say, five days of subsequent refactoring, would still have been substantially less than the weeks you will now have to spend rewriting your CSS to fix and incorporate the themes properly. You've made a loss; your strategic debt ultimately became a loss-making exercise.

The important thing to note here is that you didn't necessarily write bad code. You knew there were two options: the quick way and the correct way. The decision to take the quick route was a definite choice, because you knew there was a better way. Implementing the better way is your repayment.

Good Debt and Bad Debt

Technical debt is acceptable as long as you have intentions to settle; it can be a valuable solution to a business problem, provided the right approach is taken afterwards. That doesn't, however, mean that all debt is born equal. Just as in real life, there is good debt and there is bad debt.

Good debt might be…

a mortgage;
a student loan, or;
a business loan.

These are types of debt that will secure you the means of repaying them. These are well considered debts whose very reason for being will allow you to make the money to pay them off—they have real, tangible benefit.

A business loan to secure some equipment and premises will allow you to start an enterprise whose revenue will allow you to pay that debt back; a student loan will allow you to secure the kind of job that has the ability to pay a student loan back.

These kinds of debt involve a considered and well-balanced decision to acquire something in the short term in the knowledge that you will have the means, in the long term, to pay it back.

Conversely, bad debt might be…

borrowing $1,000 from a loan shark so you can go to Vegas, or;
taking out a payday loan in order to buy a new television.

Both of these kinds of debt will leave you paying for things that didn't provide you a way of earning your own capital. That is to say, the loans taken did not secure anything that would help pay off said loans. These are bad debts that will usually provide a net loss. You really are only gaining the short term in exchange for a long term financial responsibility: i.e., was it worth it?

A good litmus test for debt is to compare the gains of its immediate benefit with the cost of its long term commitment.

The earlier example of theming a site is a good debt, provided we are keeping up our repayments (all debt is bad debt if you don't). A calculated decision to do something 'wrong' in the short term with the promise of better payoffs later on.

Bad Technical Debt

The majority of my work is with front-end development teams—CSS is what I do. To that end, the most succinct example of technical debt for that audience is simply:

!important

All front-end developers know the horrors and dangers associated with using !important, yet we continue to use it. Why?

It's not necessarily because we're bad developers, but because we see a shortcut. !important is usually implemented as a quick way out of a sticky specificity situation. We could spend the rest of the day refactoring our CSS to fix the issue at its source, or we can spend mere seconds typing the word !important and patch over the symptoms.

This is us making an explicit decision to do something less than ideal now in exchange for immediate benefit. After all, refactoring our CSS will take a lot more time, and will still only leave us with the same outcome that the vastly quicker !important solution will, so it seems to make better business sense.

However, this is a bad debt. !important takes seconds to implement but weeks to refactor. The cost of refactoring this back out later will be an order of magnitude higher than it would be to have done things properly the first time. The first !important usually sets a precedent, and subsequent developers are likely to have to use it themselves in order to get around the one that you left.

So many CSS projects deteriorate because of this one simple word, and rewrites become more and more imminent. That makes it possibly the most costly 10 bytes a CSS developer could ever write.

Bad Code

Now we've got a good idea of what constitutes technical debt, let's take a look at what constitutes bad code. Something I hear time and time again in my client work goes a little like this:

We've amassed a lot of technical debt and we'd like to get a strategy in place to begin dealing with it.

Whilst I genuinely admire their willingness to identify and desire to fix problems in their code, sometimes they're not looking at technical debt at all—sometimes they're just looking at bad code, plain and simple.

Where technical debt is knowing that there's a better way, but the quicker way makes more sense right now, bad code is not caring if there's a better way at all.

Again, looking at a CSS-specific world, a lot of bad code is contributed by non-front-end developers with little training, appreciation, or even respect for the front-end landscape. Writing code with reckless abandon should not be described as technical debt, because to do so would imply that…

the developers knew they were implementing a sub-par solution, but…
the developers also knew that a better solution was out there, which…
implies that it can be tidied up relatively simply.

Developers writing bad code is a larger and more cultural problem that requires a lot more effort to fix. Hopefully—and usually—bad code is in the minority, but it helps to be objective in identifying and solving it. Bad code usually doesn't happen for a good enough reason, and is therefore much harder to justify.

Technical debt often represents ability in judgement, whereas bad code often represents a gap in skills.

Takeaway

Take time to familiarise yourself with the true concepts underlying technical debt and why it exists. Understand that technical debt can be good or bad. Admit that sometimes code is just of poor quality.

Understanding these points will allow you to make better calls around what you might need to refactor and when, and what skills gaps you might have in your team.

Sometimes it's okay to cut corners if there is a tangible gain to be had in the immediate term.
Technical debt is okay provided it is a sensible debt and you have intentions to pay it off.
Technical debt is not necessarily synonymous with bad code, and bad code isn't necessarily technical debt. Technical debt is code that was implemented given limited knowledge or resource, with the understanding that you would need to repay something in future.
Technical debt is not inherently bad—failure to make repayments is. Periodically, it is justifiable—encouraged, even—to enter a debt in order to fulfil a more pressing matter. However, it is imperative that we begin making repayments as soon as we are capable, be that based on newly available time or knowledge.
Bad code is worse than technical debt as it represents a lack of knowledge or quality control within a team. It needs a much more fundamental fix.

ABOUT THE AUTHOR

With a client list including Google, Unilever, and the United Nations, Harry is an award-winning Consultant Front-end Architect who helps organisations and teams across the globe to plan, build, and maintain product-scale UIs.

A Google Developer Expert, he writes on the subjects of CSS architecture, performance, and scalability at csswizardry.com; develops and maintains inuitcss; authored CSS Guidelines; and Tweets at @csswizardry.
