---
url: "https://no-kill-switch.ghost.io/wiping-the-tech-debt-out-with-immutable-code/"
captured_at: "2020-10-25T21:09:26-03:00"
title: "Wiping the tech debt out with immutable code"
domain: "no-kill-switch-ghost-io"
---

# Wiping the tech debt out with immutable code

By [Sebastian Gebski](https://no-kill-switch.ghost.io/author/sebastian-gebski/)

Aug 3, 2016
4 min read

*Disclaimer: the idea of immutable code ain't mine - I've read/heard about it somewhere (can't recall precisely ;/) some time ago & it sticked with me.*

Code maintenance is already a huge problem & it won't get any better by itself. Software is everywhere - even mundane, basic everyday tools get "digital" & ... flawed. Two, three years ago I was encountering bugs (in software I use) occasionally (well, except of Windows itself ;>), now it's a daily bread'n'butter - I don't even have patience to report them. Bad news is that not only many new ones appear, but in many cases the old ones are not fixed for months & longer.

As part of the crusade for high code quality, software craftsmanship good practices are being actively promoted in the community, but the battle seems doomed - **tech debt (pretty much) always grows** - what we can impact is only the speed of this growth. Efforts made to reduce the debt explicitly ...

- ... tend to be very expensive while temporary
- ... are struggling with clear business justification for sponsors
- ... have no guarantee of success
- ... sometimes end up in a worse state than the initial one

# Wipe it out, like a boss

But maybe there's another way - instead of trying to reduce technical debt, **... reset it**?

If code's natural lifecycle is to get less readable, more tangled, too verbose & hard to modify, so in the end we're so very tempted with the urge to re-write it ... **why not do it then**?

It's the highest time to get to the point: what immutable code actually means (because, surprise-surprise, it's not meant to be 100% immutable ;P). Just to make sure it's clear - actually it doesn't have that much in common with immutable data structures, append-only data stores, etc.

> Immutable code is code that **gets re-written** each time devs feel it's necessary, regardless of the reason, e.g.:
>
> - bug to be fixed
> - change to be implemented
> - new/updated framework present

In simple words: each time when they are not happy with the code & agree that trivial, point changes won't help, they just re-write this piece of code, instead of updating it. Re-writing doesn't mean that old code has to be completely purged - it's up to devs what they want to keep..

Obviously this makes sense only if re-writing affects limited, properly isolated "component(s)" - hence some rules should be applied to keep the whole thing sane & safe:

1. code should be **organized around business domain model elements** (entities) - it's old code that's expected to vanish, model's supposed to stay
2. **code composition should be as "flat"** as possible -> no zillion layers, at least no visible publicly layers
3. "component" interactions have to happen via **well-defined, domain model-based interfaces** that do not rely on leaking implementation details
4. needless to say - "components" have to be **fine-grained**
5. most important: **dependencies - there can't be any except of interfaces** (mentioned above) - that applies to data-level dependencies as well

Yes, it sounds very *"microservice-ish"*. It wasn't the intention though.

# Pain and gain

This is a courageous model for **seasoned, experienced teams** with high development agility - there's no point in denying. It brings a bunch of significant risks:

- code is in very "fluid" state -> it requires very mature approach to deployment & automation (incl. testing)
- it puts a tremendous focus on quality of domain modelling -> poorly designed model will lead to bad API that may require breaking changes once code behind is being re-written
- flat composition of tiny, atomic components (;DDD) suggest increased number of cross-component interactions -> something that's always tricky to test & keep safe of regression
- refactoring extravaganza may get out of control w/o strong sponsor/product manager influence

These get sweeten by a solid dose of delicious treat:

- **"tribal knowledge problem" disappears** -> code portions to be analyzed are smaller & they can be easily replaced to suit the new maintainers; quite the opposite: devs have to learn the component to have it re-written
- **updating applications to newer versions** of libraries/frameworks gets far more natural & can be "blended" in time (as a side effect of re-writing efforts) - bah, you can even re-implement the component using different language / platform
- developers **get the "ease of coding" skill** -> they are getting far less afraid of "touching" code (especially legacy one), even if changes are more fundamental
- re-writing is a great opportunity to **remove old, dead code** that's not useful anymore (e.g. was created for the sake of generalization that no-one never asked for ...)

# Tapping my vials

What keeps me getting back to this idea of code immutability is ... **Elixir**. This language kinda encourages such approach due to its immanent characteristics:

- breaking functionality into communicated GenServer processes (that don't shared anything, etc.) is a standard, forced practice
- hot code swap (feature inherited from Erlang) is like a natural extension of component (in this case: process) in-place re-write
- Elixir's functional code is very concise (syntax-wise)
- Elixir's message-based communication is a very flexible & low-coupled interfacing mechanism

*Pic: Copyright (c) <http://www.banksidegallery.com/>*
