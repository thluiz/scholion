---
url: "http://t-machine.org/index.php/2007/09/03/entity-systems-are-the-future-of-mmog-development-part-1/"
captured_at: "2014-05-05T08:43:57-03:00"
title: "Entity Systems are the future of MMOG development – Part 1 | T-machine.org"
domain: "t-machine-org"
---

# Entity Systems are the future of MMOG development – Part 1

[57 Replies](http://t-machine.org/index.php/2007/09/03/entity-systems-are-the-future-of-mmog-development-part-1/#comments "Comment on Entity Systems are the future of MMOG development – Part 1")

A few years ago, entity systems (or component systems) were a hot topic. In particular, [Scott Bilas](http://www.drizzle.com/~scottb/) gave [a great GDC talk](http://www.drizzle.com/~scottb/gdc/game-objects.ppt) on using them in the development of Dungeon Siege. The main advantages to entity systems were:

- No programmer required for designers to modify game logic
- Circumvents the “impossible” problem of hard-coding all entity relationships at start of project
- Allows for easy implementation of game-design ideas that cross-cut traditional OOP objects
- Much faster compile/test/debug cycles
- Much more agile way to develop code

I first started using entity systems in anger back in 2001-2003, when I was working on MMOG server middleware. We were targetting the few most painful problems in MMOG development, one of which was the difficulty of constantly changing your game logic after launch, which led us to entity systems. I learnt then that entity systems were an almost perfect solution to massively speeding up the development time for most MMOG’s, and for also allowing almost unrestrained re-writing of fundamental game features post-launch with very little effort.

That last issue is critical to the success of an MMOG: once an MMOG is launched successfully, its long term success or failure depends more upon the ability of the dev team to evolve that game into a better game month after month than upon anything else.

I learned a lot from that first run-in with them, more about the things that go wrong and what makes developing with entity systems particularly hard than about the things that went right. We also discovered that performance could easily become a major issue – although they are very flexible and dynamic, the lack of pre-compiled lookups and optimizations can make runtime performance disappointingly (unacceptably) poor. Why? Mainly because of the amount of indirection and checks needed to run even a single method call (but I’ll go into detail on that problem, and how to fix it, a bit later).

I moved on, and didn’t think about them again, until last year. In 2006 I joined the Operation Flashpoint 2 team as the lead network programmer, where we trying to make an MMO-FPS on an unprecedented scale, and I discovered that the programming team was considering an entity-system to drive the whole game. The attractions for the OFP2 team were different – mainly around the improvements to memory management they could get from it, and the stream-oriented coding (which is essential for PS3 development) – but it turned out to be something of a silver bullet for the “MM” and “O” parts of the MMOFPS. As the network programmer, discovering that an entity system was going to be the interconnect for all other subsystems was a huge relief: the entity system meant I could implement the complex latency hiding and prediction techniques with minimal interference with the coding of all the rest of the game systems. When you’ve got 20+ programmers on a team, you really don’t want to be placing yourself in a position where you’re going to have to redesign code for all of them just to make it “network friendly”.

whilst I was working on OFP2, I got in touch with Scott, and exchanged ideas on what the future might hold for entity systems, including additional uses for them, and on how to share this knowledge more widely. He encouraged me to start a blog (and, actually, a year later that was one of the main reasons I even started this blog, [T=Machine](http://tmachine1.dh.bytemark.co.uk/blog/)), so I figured now was a good time to start (finally) writing about those entities :).

And to blame Scott for the existence of this blog…

Since then, I’ve been thinking a lot off and on about entity systems and their appropriateness for use in MMOG development (again!). Only this time around – thanks to OFP2 and some of the issues it threw up – I had a much better idea how to use them to increase performance rather than reduce it, and had come across some other major problems that they conveniently solve. Most obviously, they work wonders for PS3 development. Knowing how PS3′s fundamental architecture works, I can’t immediately see how you’d want to use anything other than a full entity system for game development. There’s so much horsepower in that beast that you can certainly write games many different ways, but it’s particularly well-suited to this approach.

As it stands, I’m beginning to think that next-generation MMOG’s are going to be practically impossible to develop unless based heavily around a core entity-system. “practically” being the key word – unless you’re willing to spend $100 million for your development…

“Anything is possible”, of course, so there’ll be many exceptions to that – but I think any team that doesn’t go this route is going to suffer a lot because of it.

I think most people would agree. But … recent discussions on game-industry mailing lists – and the experiences I had within games companies with programmers who were much better at programming than I was – made me realise that there’s a lot of ignorance over these systems, and many people aren’t getting anywhere near the full potential of them. So, if you’re interested, read on…

I’ll do this in a series of posts (it’s going to take some time to write it all up!), but it’ll go something approximately like this:

ADDENDUM:

- [Entity System on Android phones – a concrete example using Java](http://t-machine.org/index.php/2010/05/09/entity-system-1-javaandroid/)

EDIT, December 2007 – You may also want to take a look at [Mick West’s introduction to entity systems for game development](http://cowboyprogramming.com/2007/01/05/evolve-your-heirachy/), it’s a shorter read than my posts, but narrower in scope.

NB: as I post the other parts, I’ll update the list above to link to them.

## Did this post help you?

You can say “thank you” by giving me your email address, and letting me contact you next time I make a game of my own:

This entry was posted in [computer games](http://t-machine.org/index.php/category/computer-games/ "View all posts in computer games"), [entity systems](http://t-machine.org/index.php/category/entity-systems/ "View all posts in entity systems"), [games design](http://t-machine.org/index.php/category/games-design/ "View all posts in games design"), [massively multiplayer](http://t-machine.org/index.php/category/massively-multiplayer/ "View all posts in massively multiplayer"), [networking](http://t-machine.org/index.php/category/networking/ "View all posts in networking"), [system architecture](http://t-machine.org/index.php/category/system-architecture/ "View all posts in system architecture") on [September 3, 2007](http://t-machine.org/index.php/2007/09/03/entity-systems-are-the-future-of-mmog-development-part-1/ "8:38 pm") by [adam](http://t-machine.org/index.php/author/adam/ "View all posts by adam").
