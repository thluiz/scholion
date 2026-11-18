---
url: "https://blog.ploeh.dk/2019/09/30/10x-developers/"
captured_at: "2026-11-18T13:54:03+00:00"
title: "10x developers"
domain: "blog-ploeh-dk"
---

_Do 10x developers exist? I believe that they do, but not like you may think._

The notion that some software developers are ten times (10x) as productive as 'normal' developers is decades old. Once in a while, the discussion resurfaces. It's a controversial subject, but something I've been thinking about for years, so I thought that I'd share my perspective because I don't see anyone else arguing from this position.

While I'll try to explain my reasoning, I'll make no attempt at passing this off as anything but my current, subjective viewpoint. Please leave a comment if you have something to add.

### Perspective [#](#11f6ec960f694758892bff549eb79d59 "permalink")

Meet Yohan. You've probably had a colleague like him. He's one of those software developers who gets things done, who never says no when the business asks him to help them out, who always respond with a smile to any request.

I've had a few colleagues like Yohan in my career. It can be enlightening overhearing non-technical stakeholders discuss software developers:

**Alice:** Yohan is such a dear; he helped me out with that feature on the web site, you know...

**Bob:** Yes, he's a real go-getter. All the other programmers just say no and look pissed when I approach them about anything.

**Alice:** Yohan always says yes, and he gets things done. He's a real 10x developer.

**Bob:** We're so lucky we have him...

Overhearing such a conversation can be frustrating. Yohan is your colleague, and you've just about had enough of him. Yohan is one of those developers who'll surround all code with a `try-catch` block, because then there'll be no exceptions in production. Yohan will make changes directly to the production system and tell no-one. Yohan will copy and paste code. Yohan will put business logic in database triggers, or rewrite logs, or use email as a messaging system, or call, parse, and run HTML-embedded JavaScript code on back-end servers. All 'because it's faster and provides more business value.'

Yohan is a 10x developer.

You, and the rest of your team, get nothing done.

You get nothing done because you waste all your time cleaning up the trail of garbage and technical debt Yohan leaves in his wake.

Business stakeholders may view Yohan as being orders of magnitude more productive than other developers, because most programming work is invisible and intangible. Whether or not someone is a 10x developer is highly subjective, and depends on perspective.

### Context [#](#57c36b775bca4e848cadf50182028191 "permalink")

The notion that some people are orders of magnitude more productive than the 'baseline' programmer has other problems. It implicitly assumes that a 'baseline' programmer exists in the first place. Modern software development, however, is specialised.

As an example, I've been doing test-driven, ASP.NET-based C# server-side enterprise development for decades. Drop me into a project with my favourite stack and watch me go. On the other hand, try asking me to develop a game for the Sony PlayStation, and watch me stall.

Clearly, then, I'm a 10x developer, for the tautological reason that I'm much better at the things that I'm good at than the things I'm not good at.

Even the greatest [R](https://en.wikipedia.org/wiki/R_\(programming_language\)) developer is unlikely to be of much help on your next [COBOL](https://en.wikipedia.org/wiki/COBOL) project.

As always, context matters. You can be a great programmer in a particular context, and suck in another.

This isn't limited to technology stacks. Some people prefer co-location, while others work best by themselves. Some people are detail-oriented, while others like to look at the big picture. Some people do their best work early in the morning, and others late at night.

And some teams of 'mediocre' programmers outperform all-star teams. (This, incidentally, is a phenomenon also [sometimes seen](https://en.wikipedia.org/wiki/UEFA_Euro_1992) in professional [Soccer](https://en.wikipedia.org/wiki/Association_football).)

### Evidence [#](#34e113a19c8040b0bcb38f7abf1b532d "permalink")

Unfortunately, as I explain in my [Humane Code](https://cleancoders.com/video-details/humane-code-real-episode-1) video, I believe that you can't measure software development productivity. Thus, the notion of a 10x developer is subjective.

The original idea, however, is decades old, and seems, at first glance, to originate in a 'study'. If you're curious about its origins, I can't recommend [The Leprechauns of Software Engineering](https://blog.ploeh.dk/ref/leprechauns-sw-eng) enough. In that book, Laurent Bossavit explains just how insubstantial the evidence is.

If the evidence is so weak, then why does the idea that 10x developers exist keep coming back?

### 0x developers [#](#6988798f60bf4622808b58a3e7f55bce "permalink")

I think that the reason that the belief is recurring is that (subjectively) _it seems so evident_. Barring confirmation bias, I'm sure everyone has encountered a team member that never seemed to get anything done.

I know that I've certainly had that experience from time to time.

The first job I had, I hated. I just couldn't muster any enthusiasm for the work, and I'd postpone and drag out as long as possible even the simplest task. That wasn't very mature, but I was 25 and it was my first job, and I didn't know how to handle the situation I found myself in. I'm sure that my colleagues back then found that I didn't pull my part. I didn't, and I'm not proud of it, but it's true.

I believe now that I was in the wrong context. It wasn't that I was incapable of doing the job, but at that time in my career, I absolutely loathed it, and for that reason, I wasn't productive.

Another time, I had a colleague who seemed incapable of producing anything that helped us achieve our goals. I was concerned that I'd [flipped the bozo bit](https://en.wikipedia.org/wiki/Bozo_bit) on that colleague, so I started to collect evidence. Our Git repository had few commits from that colleague, and the few that I could find I knew had been made in collaboration with another team member. We shared an office, and I had a pretty good idea about who worked together with whom when.

This colleague spent a lot of time talking to other people. Us, other stakeholders, or any hapless victim who didn't escape in time. Based on these meetings and discussions, we'd hear about all sorts of ideas for improvements for our code or development process, but nothing would be implemented, and rarely did it have any relevance to what we were trying to accomplish.

I've met programmers who get nothing done more than once. Sometimes, like the above story, they're boisterous bluffs, but most often, they just sit quietly in their corner and fidget with who knows what.

Based on the above, mind you, I'm not saying that these people are necessarily incompetent (although I suspect that some are). They might also just find themselves in a wrong context, like I did in my first job.

It seems clear to me, then, that there's such a thing as a _0x developer_. This is a developer who gets zero times (0x) as much done as the 'average' developer.

For that reason it seems evident to me that 10x developers exist. Any developer who regularly manages to get code deployed to production is not only ten times, but infinitely more productive than 0x developers.

It gets worse, though.

### −nx developers [#](#fe07476743704027acab9c7b949bc3a4 "permalink")

Not only is it my experience that 0x developers exist, I also believe that I've met more than one _−nx developer_. These are developers who are _minus n times_ 'more' productive than the 'baseline' developer. In other words, they are software developers who have negative productivity.

I've never met anyone who I suspected of deliberately sabotaging our efforts; they always seem well-meaning, but some people can produce more mess than three colleagues can clean up. Yohan, above, is such an archetype.

One colleague I had, long ago, was so bad that the rest of the team deliberately compartmentalised him/her. We'd ask him/her to work on an isolated piece of the system, knowing that (s)he would be assigned to another project after four months. We then secretly planned to throw away the code once (s)he was gone, and rewrite it. I don't know if that was the right decision, but since we had padded all other estimates accordingly, we made our deadlines without more than the usual overruns.

If you accept the assertion that −nx developers exist, then clearly, anyone who gets anything done at all is an _∞x developer_.

### Summary [#](#8257729b743641d0afa1c2ddbfe1b0df "permalink")

10x developers exist, but not in the way that people normally interpret the term.

10x developers exist because there's great variability in (perceived) productivity. Much of the variability is context-dependent, so it's less clear if some people are just 'better at programming' than others. Still, when we consider that people like [Linus Torvalds](https://en.wikipedia.org/wiki/Linus_Torvalds) exist, it seems compelling that this might be the case.

Most of the variability, however, I think correlates with environment. Are you working in a technology stack with which you're comfortable? Do you like what you're doing? Do you like your colleagues? Do you like your hours? Do you like your working environment?

Still, even if we could control for all of those variables, we might still find that some people get stuff done, and some people don't. The people who get anything done are ∞x developers.

Employers and non-technical start-up founders sometimes look for the 10x unicorns, just like they look for _rock star developers_.

> "To really confuse recruiters, someone should make a programming language called Rockstar."

The above tweet inspired [Dylan Beattie](http://www.dylanbeattie.net/) to create [the Rockstar programming language](https://codewithrockstar.com/).

Perhaps we should also create a _10x_ programming language, so that we could put _certified Rockstar programmer, 10x developer_ on our resumes.
