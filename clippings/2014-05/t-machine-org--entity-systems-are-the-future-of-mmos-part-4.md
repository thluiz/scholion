---
url: "http://t-machine.org/index.php/2008/03/13/entity-systems-are-the-future-of-mmos-part-4/"
captured_at: "2014-05-05T08:42:19-03:00"
title: "Entity Systems are the Future of MMOs Part 4 | T-machine.org"
domain: "t-machine-org"
---

# Entity Systems are the Future of MMOs Part 4

[30 Replies](http://t-machine.org/index.php/2008/03/13/entity-systems-are-the-future-of-mmos-part-4/#comments "Comment on Entity Systems are the Future of MMOs Part 4")

#### Massively Multiplayer Entity Systems: Introduction

So, what’s the connection between ES and MMO, that I’ve so tantalisingly been dangling in the title of the last three posts? ([start here if you haven’t read them yet](http://t-machine.org/index.php/2007/09/03/entity-systems-are-the-future-of-mmog-development-part-1/)).

The short answer is: it’s all about data. And data is a lot harder than most people think, whenever you have to deal with an entire system (like an MMO) instead of just one consumer of a system (like the game-client, which is the only part of an MMO that traditional games have).

Obviously, we need to look at it in a lot more detail than that. First, some background…

#### Massively Multiplayer Game Development 101

There’s a few key things you need to be aware of in MMO development. Many professional game developers know some or all of these already, but seeing as I’ve even met MMO developers who didn’t know them all, and much of what I’m going to say later on won’t make sense without it, I’m going to do a quick recap. Bear with me; I’ll have to do some gross generalization to keep this short (so it won’t be 100% true or accurate).

#### 1. The vast majority of the cost of MMO development is content

Content is:  
– quests (missions, storylines, scripted events)  
– 3D areas (meshes, textures and logic for: zones, dungeons, towns, landscapes)  
– loot (item graphics, drop rates, item stats, item abilities)

Content is NOT:  
– Fancy 3D graphics  
– Physics engines  
– AI  
– Core game rules

…which tend to make up the bulk of non-MMO games.

As Raph Koster (amongst others, but IIRC Raph was one of the first to come up with a clear concise description) pointed out close to 10 years ago, the rate at which players consume content vastly excedes the rate at which developers generate it – you have perhaps 50 people working purely on content generation on a modern MMO, and you have perhaps 500,000 people consuming it. The problem is, those 500,000 use Thottbot, so they \*share\* their discoveries, and consume at a rate proportional to the square of their number, whereas it’s generally produced at a rate more directly proportional to the number of developers.

There are many ways to work around this issue, but most of them end up producing or managing vast amounts of content (they just get more cunning in exactly how that content is generated).

#### 2. The vast majority of the development of an MMO takes place AFTER launch

The ten-year-old MMO’s have been releasing expansions and content updates every 6 to 18 months; modern MMO’s release new content every 3 to 12 months. “New content” in this context generally means entirely new 3D areas with entirely new quests and entirely new items, not to mention entirely new special abilities and new plotlines. i.e. complete “miniature MMOs”.  
The only bits you don’t need to keep rewriting are the technology, although nearly all MMOs have done minor updates throughout their lifetime, usually when a new expansion pack is released as a retail boxed product (if you buy and install the expansion, not only do you get the bonus content, but all the “old” content becomes higher resolution / more pretty / added sparkly bits). Although … I long wished there was more updating of tech, and three major MMOs are currently doing huge updates: Ultima Online (1997) [recently massively renovated their 10-year old graphics as Kingdom Reborn](http://www.uoherald.com/kingdomreborn/), Eve Online (2001) just completed their “shininess and detailed spaceships with added humanoids” update known as [Trinity](http://www.eve-online.com/trinity/), and Anarchy Online (2001) recently previewed [massive sweeping changes to their very poor detail and draw distance client](http://www.mmorpg.com/gamelist.cfm?GAMEID=10&SETVIEW=features&LOADFEATURE=1718&bhcp=1) (they say “the current engine was designed before there really were GPUs to utilize” but that is blatantly false as the GeForce had been on sale for almost 2 years when they launched, and the TNT,Voodoo, et al for years before that. Yes, I was bitter that when it launched the most recent hardware it supported was 5 years old :)). All represent major changes to the look and feel of the games – it’s hard to overestimate the visual impact of these. Runescape did their mega update (“Runescape 2″) a couple of years ago.

However … all are bringing games that were NOT cutting edge at launch up to a standard that is still well short of what is cutting edge now. This is important to understand: graphical quality is (according to what the successful MMO’s deploy) definitely not the main selling point for these games, unlike almost all other successful games you can possibly buy.

So … what is that “development” that takes place after launch? It’s content, not engine. And even when it’s engine (better graphics, better physics) it’s always a minimal improvement by the standards of standalone PC and console titles of the time.

For reference, many MMO’s after launch end up with LARGER development teams than they had in the 3-5 years of development leading up to the launch. All that extra content requires a lot of people (not to mention keeping all the old content working, updating it where it conflicts with new content, etc).

On top of all that, though, there is the issue of customer support. When you launch a traditional game, that’s it. Done. Over the last 15 years there’s been a trend towards launching occasional “patches” and even minor content updates – but mostly bugfixes – which, incidentally, I suspect has been largely driven by publishers learning from the MMOs: releasing a content patch for an old game is a good way to get extra marketing / publicity and increase some sales. Bethesda’s TES4/Oblivion even went as far as to [charge for the patches](http://en.wikipedia.org/wiki/The_Elder_Scrolls_IV:_Knights_of_the_Nine).

MMO’s require a lot more work than that: since MMO’s are all monetized off continuous play (i.e. the more each player plays, the more money the publisher makes), either through monthly subscriptions or through in-game commerce, it is imperative to keep all the players playing as long as possible. If a player plays your MMO for 12 months instead of 6, you’ll make twice as much profit; if they play your console title for 12 months instead of 6, you’ll make no more money and will probably cannibalize your sales of the sequel.

So. Total lifetime development cost is a lot more important, financially, to an MMO than the pre-launch development cost.

#### 3. The way the core logic works now is not how it will work forever

Sooner or later, you [nerf](http://www.urbandictionary.com/define.php?term=nerf).

Usually because you(r players) discover a disproportionately powerful game tactic in PvP that you didn’t think of which is unbalancing and ruining the game, and so you “have” to fix it.

Sooner or later, you choose to break every absolute rule of your game logic, because a new expansion wants to slightly redefine and “freshen” the core game.

And that means you have to be able to break every rule you ever hardcoded into the game-logic. Worse, it means you have to be able to handle the fallout (all the bugs that the change introduces, plus all the invisible bugs that were originally there but had no noticeable effect and now suddenly have visible effect, the new security holes, etc).

Since the ongoing development of the game (post launch) is greater than the initial development in scope and cost, over the lifetime of the game it is more important to make it easy to change the core logic – and to react to side effects of that change – than to be able to make the core logic easily in the first place.

#### 4. Even a moderately successful MMO generates gigabytes of data every 24 hours

The progress of every player of the MMO has to be uniquely independently tracked, so that the game can remember for each player which quests they’ve completed, which equipment they have, etc. With 100,000 players, that data racks up quickly. A lot of it can be thrown away every day (for instance, you don’t generally need the history of how many hitpoints you had at the end of every day), but a lot of it has to be kept forever (whether you completed a given quest, and for some quests how exactly you completed it).

However, the trend at the moment is towards keeping ALL this data, in the form of historical records of your personal game experience – e.g. the automatic “blog” that is created whilst you play Vanguard, which e.g. updates every time you level up, or kill a monster, or die, etc.

This latter kind of data alone is generated at the rate of around 30Gb every 24 hours.

And any of that data that gets used in-game (e.g. even if just referenced in a conversation with an NPC) has to be programmatically accessible.

Ultimately, MMOs have to store, retrieve, and update vast databases. There is a huge decades-old industry that specializes in providing software to manage databases of this size and larger, but [MMO developers don’t like SQL and Relational programming](http://t-machine.org/index.php/2008/02/21/gdc08-sql-considered-harmful/). This is a real problem – relational databases can handle the load, but relational programming is fundamentally incompatible with Object-Oriented programming. The net effect is that programmers who have to write their data to disk find it boring, difficult, and irritating to do – and that leads to mistakes and greatly increased bugs, as well as reduced functionality (because no-one wants to write or add to the code to add the new features more than they absolutely have to).

#### MMO Development Priorities

The net effect of these aspects of MMO development is that the long term profitability of an MMO can be greatly affected by a bunch of simple issues:

- How much effort is required to change the data used to describe an in-game item
- How much effort is required to add (or remove) new (old) types of in-game item
- How re-usable is the content
- How easy it is in practice (i.e. how much coding is needed) to re-use re-usable content
- How much specialist knowledge of the game code, overall game design, and details of the game systems is needed to modify the content and logic (can new team members be effective as the team who originally wrote the game pre-launch?)
- How exportable is the data generated by playing the game (progress, achievements, player-history, etc)
- How analysable is the game-data generated by playing (to make decisions about what to change, and check that game improvements have improed things)
- How modifiable the core-content is
- How easy it is to change individual rules and check the side-effects of the changes
- How many of all the above changes can be done WITHOUT requiring a programmer (can designers change code themselves? can artists?)
- How much can third-party specialist systems be utilised for server-side service provision

Leading to a few rules of thumb that are often adopted by commercial MMOs:

1. Use commercial databases for all persistent data-storage
2. Use Relational Databases and allow arbitrary general data requests
3. Implement as much as possible of the game-logic as raw data rather than as compiled data (and preferably as data rather than source code)
4. Use standard but simple to learn scripting languages where data isn’t expressive enough
5. Do lots and lots of testing during development
6. Do even more testing post-launch EVERY SINGLE TIME you consider changing ANYTHING on the live servers

Some of those aren’t very effective (too vague), others are horrifically expensive (it takes a lot of people to “test EVERYTHING” every time you make a change to a live game). None of them are great for performance in and of themselves (although they can be made highly performant, that requires extra work), and none of them are “programmer friendly” – in fact, they’re all deliberately programmer UNfriendly, being in there for the benefit of non-programmers.

NB: this is in no way a comprehensive or exhaustive list; I’m trying to give merely a flavour of the thing here for people who aren’t familiar with typical MMO dev processes. I don’t know any real MMO that faces only those challenges and uses only those rules of thumb, but they are indicative of what is used, and very very roughly explain why those things are used.

And so on to Entity Systems, and how they can affect the typical MMO development process by helping with problems or making the current solutions more programmer-friendly… (which is going to be Part 5. This is getting long enough already).

## Did this post help you?

You can say “thank you” by giving me your email address, and letting me contact you next time I make a game of my own:

## Next post

[This entry was posted in](http://t-machine.org/index.php/2009/10/26/entity-systems-are-the-future-of-mmos-part-5></a>Part 5</a></p>      </div><!-- .entry-content -->      <footer class=) [computer games](http://t-machine.org/index.php/category/computer-games/ "View all posts in computer games"), [databases](http://t-machine.org/index.php/category/databases/ "View all posts in databases"), [entity systems](http://t-machine.org/index.php/category/entity-systems/ "View all posts in entity systems"), [games design](http://t-machine.org/index.php/category/games-design/ "View all posts in games design"), [massively multiplayer](http://t-machine.org/index.php/category/massively-multiplayer/ "View all posts in massively multiplayer"), [programming](http://t-machine.org/index.php/category/programming/ "View all posts in programming"), [system architecture](http://t-machine.org/index.php/category/system-architecture/ "View all posts in system architecture") on [March 13, 2008](http://t-machine.org/index.php/2008/03/13/entity-systems-are-the-future-of-mmos-part-4/ "12:00 am") by [adam](http://t-machine.org/index.php/author/adam/ "View all posts by adam").
