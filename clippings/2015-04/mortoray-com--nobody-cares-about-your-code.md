---
url: "http://mortoray.com/2015/04/20/nobody-cares-about-your-code/"
captured_at: "2015-04-22T17:08:55-03:00"
title: "Nobody cares about your code"
domain: "mortoray-com"
---

# Nobody cares about your code

Nobody cares about your code. It was quite a shocking moment when I learned this in my programming career. I would take great care in polishing my code only to find out nobody actually cares. It’s not the code that counts, it’s the product. Knowing that makes you more productive and improves the appreciation of your work.

### Code is a tool

As programmers our job is not to write code. Our job is to supply software that provides some feature somebody needs. Coding is the primary tool we use to do this. But it’s just a tool. We don’t say a carpenter’s job is to use a hammer. Their job is to create something with their tools.

Some of our processes can however mislead us into thinking code is the product. Do we see refactoring as a way to get better code, or to get a better product? Portray it as code improvement and we find no manager ever wants to give us time to do it. Show how it leads to fixing a defect, or implementing a feature, and suddenly there is time for it.

Our software will be evaluated as a whole front and foremost. For every line of code we write we must keep that in mind. If the product is unappealing there is simply no reason to look further. It doesn’t matter if we think we’re using our tools well. If the resulting product isn’t good, then we’ve basically failed to do our job.

This is not to say the code may not be valuable, or even reviewed as part of a requirements check. Security and [fault tolerance](http://mortoray.com/2012/12/23/of-faults-and-errors-whos-to-blame/) are best approached with good craftsmanship and the correct libraries. Indeed, it’s our job here to make the relevant bits of the code stand out and keep the rest uninteresting. The quicker a reviewer can get in and out of our code the happier they will be.

> Code as a tool is incidentally why it’s important to know several languages and have used many frameworks. It’s why knowing math or complexity theory is useful, but [not required](http://mortoray.com/2015/03/24/complexity-theory-isnt-required-to-be-a-programmer/). It’s why IDEs can be both amazing and terrible traps at the same time. Our flexibility as a programmer is directly related to our toolset diversity.

### Features dominate

Think of a meeting with the product manager, or customer. How do we communicate with these people? Do we tell them how many classes, or lines of code we’ve created? Do we give them details about the deployment scripts, our [exception strategy](http://mortoray.com/2012/03/08/the-necessity-of-exceptions/), or database schema?

Unfortunately the answer is often yes, we do. And look at their faces when we do this. They’re bored, disinterested, and looking to move on. We’ve just recited a bunch of details which are of zero value to the product owners. It’s not that they don’t understand, they just don’t care.

Just imagine if our graphic designer started giving details about the layers they used in Photoshop. How many objects they created, the gradient stops used on the brushes, or the cool automation scripts they’ve written. We don’t care. We just want to know if graphic assets are done or not.

We should be communicating the status of features: import is now complete, but XYZ support is still lacking; it’s now working on most phones, but model Q still jitters; we’ve got the client app running and usable, though still quite spartan. These are the interesting details to our manager, or customer. These details tell them something they can act on; something to aid them in their planning.

### The library is worthless

I’ve seen many questions online about protecting source code. A programmer does client work and reuses their own private library. Now that client wants the code and the programmer is uncertain. They don’t want to just give away this valuable library code.

Consider first why a client actually requests the source code? Maybe they want the assurance that they can continue building their product even if the programmer disappears. Maybe they want the ability to audit the product for security or legal purposes. The code in and of itself is not what they want. It’s just another asset needed to fulfil some other activity.

Though creating a library may be [the right thing to do](http://mortoray.com/2015/02/25/invented-here-syndrome/), that doesn’t give it inherent value. The library is likely only valuable to us in that it lets us develop our projects faster. It may be the most important part of our business in fact, but another programmer may casually discard it as uninteresting.

What if our library is truly special? If we honestly believe that then we can make the library the product. We can share the code, or even sell the code, and see what happens. Just bear in mind that very few code products are even moderately successful.

> It’s a worthwhile exercise for any programmer to do this. Just to realize the truth about how little other programmers care about our work. Think about your own project. When you picked a library was it because the code was awesome, or because the features were great? Did you even look at the source code after you installed it?

### Yes, but…

Doesn’t this give us liberty to write crappy code? No, it doesn’t. Quality workmanship is necessary to produce a quality product. It doesn’t matter that nobody actually cares about the code, it’s still a vital tool in getting the job done. [Perfectionism is a curse](http://mortoray.com/2015/04/15/using-a-hack-stifling-the-perfectionist-and-moving-on/), but we simply can’t meet the requirements if we use the tools ineffectively.

To use the carpentry analogy again, a dull hammer will pound a nail in just as well as a shiny one. A rusted hammer however may break and injure somebody.

Our goal as a programmer is to polish the product, not the code. If we wish to be effective in our role we must be addressing the features, not the tools. We need to understand the true source of value in our product.

[About these ads](http://wordpress.com/about-these-ads/)
