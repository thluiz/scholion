---
url: "https://olano.dev/blog/a-note-on-essential-complexity/?ref=dailydev"
captured_at: "2026-09-25T18:32:14+01:00"
title: "A Note on Essential Complexity"
domain: "olano-dev"
---

![](https://olano.dev/assets/img/labrea.jpg)

Depending on their personal needs and preferences, the level of abstraction with which they model the world, and where they sit in the idealism-cynicism spectrum, any of the following can be legitimately said to be _the job_ of software engineers:

*   Writing code.
*   Building and maintaining quality software.
*   Building and maintaining _good enough_ software _cost-effectively_.
*   Managing complexity.
*   Delighting users.
*   Solving problems.
*   Satisfying customer needs.
*   Making money for their employing organization or their customers.
*   Making money (for themselves).

There surely are more. Some of these goals can be abstracted, reduced to, or derived from others. Some are ultimately incompatible or contradictory, and can only coexist with others in tension. For example: we can assume (to some extent) that quality software will delight our users and make money for our employers. But we also need to sacrifice quality to stay within budget or introduce features that annoy users but generate profit.

Each goal proceeds from a particular way of modeling the world and our activity. As with any abstraction, they serve their purpose in the right context and become _false_ when applied outside of it; many problems in software development can be explained by such a skewed perspective, something I explored in a [previous post](https://olano.dev/blog/code-is-run-more-than-read). In the next discussion, let’s assume that _managing complexity_ is the main duty of a software engineer.

∗ ∗ ∗

Complexity is anything that makes it hard to understand and modify a system. In [_A Philosophy of Software Design_](https://web.stanford.edu/~ouster/cgi-bin/aposd.php), John Ousterhout explains why we should make it our main concern:

> If we want to make it easier to write software, so that we can build more powerful systems more cheaply, we must find ways to make software simpler. (…) Most of the code in any system is written by extending the existing code base, so your most important job as a developer is to facilitate those future extensions. Thus, you should not think of “working code” as your primary goal, though of course your code must work. Your primary goal must be to produce a great design, which also happens to work. This is strategic programming. (…) If software developers should always be thinking about design issues, and reducing complexity is the most important element of software design, then software developers should always be thinking about complexity.

The _urtext_ of the software complexity discussion is Fred Brooks’s [_No Silver Bullet_](https://worrydream.com/refs/Brooks_1986_-_No_Silver_Bullet.pdf). Brooks distinguishes between essence and accident in software, posing that complexity is an essential difficulty of software systems —one of the things currently bounding our productivity. In [_Out of the Tar Pit_](https://curtclifton.net/papers/MoseleyMarks06a.pdf), Moseley and Marks build on Brooks’s ideas, defining the better-known (and more tractable) types of complexity:

*   **Essential Complexity** is inherent in, and the essence of, the _problem_ (as seen by the _users_).
*   **Accidental Complexity** is all the rest —complexity with which the development team would not have to deal in the ideal world (e.g. complexity arising from performance issues and from suboptimal language and infrastructure).

The user’s point of view is key to the distinction:

> If there is any possible way that the team could produce a system that the users will consider correct without having to be concerned with a given type of complexity then that complexity is not essential. (…) One implication of this definition is that if the user doesn’t even know what something is (e.g. a thread pool or a loop counter — to pick two arbitrary examples) then it cannot possibly be essential by our definition.

Of course, any real-world implementation of the system will necessarily have to introduce _some_ accidental complexity. The goal of the software engineer, then, is to _minimize_ accidental complexity and _assist_ with essential complexity.

∗ ∗ ∗

Subtle semantic differences aside, both authors of _No Silver Bullet_ and _Out of the Tar Pit_ agree in that there’s an essence to a problem: something that engineers can’t change, that the system must conform to, and that contributes a type of complexity that cannot be escaped. From _No Silver Bullet_:

> Much of the complexity \[the software engineer\] must master is arbitrary complexity, forced without rhyme or reason by the many human institutions and systems to which his interfaces must conform. (…) In many cases the software must conform because it has most recently come to the scene. In others it must conform because it is perceived as the most conformable. But in all cases, much complexity comes from conformation to other interfaces; this cannot be simplified out by any redesign of the software alone.

Now, I want to challenge the notion that essential complexity is irreducible. The fact that we can’t remove it by changing software alone doesn’t mean that there’s nothing we can do about it. What if we were to attack the essence? What if the problem definition wasn’t outside of our purview? What if we could get the world to conform to the software, and not just the other way around? Brooks already hinted at this possibility:

> The buyer of a $2-million machine in 1960 felt that he could afford $250,000 more for a customized payroll program, one that slipped easily and nondisruptively into the computer-hostile social environment. Buyers of $50,000 office machines today \[1986\] cannot conceivably afford customized payroll programs; so they adapt their payroll procedures to the packages available. Computers are now so commonplace, if not yet so beloved, that the adaptations are accepted as a matter of course.

This doesn’t come as a surprise to us: we’ve been seeing for decades how human behavior (and user expectations) can be shaped by software: instant messaging, social media, content streaming —all drastically changed our everyday habits. If we admit that users can be made to adjust to the system —that software has the potential to change people and organizations—, then the problems that software solves for them can be redefined: the essence is not set in stone but open to discussion, part of what the engineer can work with.

We can thus simplify the goal of the software engineer from minimizing _accidental_ complexity and assisting with _essential_ complexity, to minimizing complexity _of any kind_. In his follow-up essay _“No Silver Bullet” Refired_, Brooks quotes a reader that perfectly synthesizes this stance:

> In my experience most of the complexities which are encountered in systems work are symptoms of organizational malfunctions. Trying to model this reality with equally complex programs is actually to conserve the mess instead of solving the problems.

Redefining the problem may seem like a cheating, but it’s just business as usual for senior engineers: _Why are we working on this? Do we really need it? What problem are we trying to solve? Who benefits from us solving it? What if, instead of X, we initially ship X1, which takes us 20% of the effort and provides 80% of the functionality?_

Strictly following Moseley and Marks’s definition, the fact that we can get the user (or the customer, or the product owner) to accept a change of requirements, implies that the removed complexity _wasn’t essential in the first place_. Instead, we made progress in uncovering the true essence of the problem. The point is that this progress required engineers to question assumptions and dissuade stakeholders; without their involvement, the unnecessary features would have become part of the problem specification, “ossified” into its essence.

∗ ∗ ∗

In general, given a complex component of a software system (or an organization), it can happen that:

*   The complexity is accidental, so we can remove it.
*   The complexity is essential and we need to keep it.
*   The complexity is essential but we could remove it by redefining the problem specification.
*   The knowledge to tell whether something is essential or not is lost, the customer or the product owner can’t tell, or there isn’t such an authority to make the call.

I frequently found the latter situation when working with legacy software, where the only specification is the system itself —bugs and unknowns included— and any observable feature, a _de facto_ functional requirement, essential to the problem. The conservative approach to maintaining such systems is limited to internal refactors; a more disruptive reduce-complexity-at-all-costs attitude would assume that anything is up for removal until proven otherwise. In [_Kill It with Fire_](https://nostarch.com/kill-it-fire), Marianne Bellotti describes resilience engineering along those lines:

> When we encountered systems that had been forgotten and we couldn’t figure out what they were doing, we would usually just turn them off and see what happened. (…) When we turned off a system, we waited for someone to complain. That person was either the system owner or the owner of a downstream dependency, but either way, we ended the experiment with more information about what the system was doing than we started with. (…) If no one complained, we tended to just leave the system off and move on.

Even if systems can’t be removed, the new information improves organizational understanding, which reduces complexity.

∗ ∗ ∗

Taking this argument to its extreme: engineers could envision simpler implementations of the systems, then persuade the owning organizations to make their processes converge with those implementations —doing with the organization that uses a system what the [Inverse Conway Maneuver](https://martinfowler.com/bliki/ConwaysLaw.html) tries to do with the organization that develops it. Left to their own devices, software engineers would act as the philosophical razor, removing the complexity of the world; automating employees —the engineers themselves included— out of a job; simplifying systems, along with the organizations that own them, out of existence.

Of course, this _reductio ad absurdum_ results from taking our initial premise beyond its reasonable limits. We started with the assumption that the software engineer’s sole purpose is to minimize complexity, ignoring, among other things, the economic interests that determine their work. This can serve as a reminder that, since our work indeed has the power to affect individuals and organizations, we shouldn’t wield it unconsciously, hiding behind the comfort of an abstraction. We occasionally need to leak out of our interface, into the unstructured mess that is the world.

* * *

_An earlier version of this post was [published in Spanish](https://olano.dev/blog/posdata-sobre-la-complejidad-esencial)._

* * *
