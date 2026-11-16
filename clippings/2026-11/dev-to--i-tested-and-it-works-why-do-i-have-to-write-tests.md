---
url: "https://dev.to/briwa/me-i-tested-and-it-works-why-do-i-have-to-write-tests-4292"
captured_at: "2026-11-16T18:45:52+00:00"
title: "Me: \"I tested and it works, why do I have to write tests?\""
domain: "dev-to"
---

I started out programming in PHP and Javascript when I was studying in university. Back then, I knew nothing about any kinds of software testing. The only way to make sure that the code works is to test them manually in the browser. I would imagine that bigger companies with more complex software would have a dozen of people lining up in front of their software interface, testing them manually.

I remember there was even a spreadsheet, filled with rows of use cases, with checkboxes to tick before launch. Even with that, the bugs still appeared. When I shipped the code, I did manual testing on several cases that I was aware of, but there is no way I could test _all_ the possible cases that the app would allow. It was one of the most counter-productive moments in my development career.

Then I discovered [software testing](https://en.wikipedia.org/wiki/Software_testing#Testing_levels). It was such a blessing. The way it covers use cases systematically, maintain the app stability, and how it is done automatically with Continuous Integration truly amazed me. No more spreadsheet with millions of rows, and I can ship code with more confidence.

* * *

In my opinion, the concept of testing is still hard to accept to some, even now. I can understand that this is mostly fear of change; trying to get people out of the comfort zone of "I coded it and it works" is not an easy task. I remember a few arguments against testing:

*   "I have confidence in my code, it won't break."
*   "I tested all the use cases, they're fine."
*   "You can review my code, point out the flaws, and if there's none it should be good to go."

All the arguments came from the "human" factor of the developer: their code confidence, their manual testing skills, their flawless code. And it is important; nothing to take away from that. Software testing, on the other hand, covers the cases when the "human" factor is failing. Nobody is perfect, mistakes are bound to happen and we learn from the experience. When you write the code, or even when people review the code, and some use cases/flaws are being overlooked, the test might be able to point that out.

And not just about maintaining stability and the quality of the code. Tests define the specification of the code. I was just being dense, but it just occurred to me as to why tests are called "specs" in the first place. When writing tests, it is made very clear from the start on what the code can and cannot do. Recently, I even started developing a habit of browsing the test folder of a library to find out what it does when I can't find them in their API/demo page, and it does really help.

* * *

Even with all the good stuff about testing being laid out, getting people on-boarded is definitely another problem. I can see how people are still treating tests as "something that would allow me to merge PRs". Some would probably still say "the feature works and I tested it, we can merge it first and I'll write the test later". Others would complain that "lots of tests failing because I changed one line of code".

In my opinion, they are missing the big picture. If you make changes on the code, of course you have to make all tests passing because you're making sure that your code is still within the specification of the code (the test). If you add a new code, you have to add tests because you're adding new specifications to the software. If you're shipping a code without a test, that would mean you're shipping code without a specification; nothing is set in stone about what works and what doesn't, including bugs.

There are reasons why most open source repositories are taking tests very seriously: because they care so much about their code stability. One single bug could put lots of people at stake, the devs and its users. PRs with failing builds or no tests wouldn't even be reviewed. I would say it shouldn't be that much different compared to our own (for-profit, maybe?) projects. It might be hard to convince clients/stakeholders that testing is important, but at least it shouldn't be made that hard for the devs.

* * *

This article might not apply to you. I am aware that there are many practices that integrate testing into their workflow (e.g. [Agile](https://www.thoughtworks.com/agile-project-management)), and a lot of companies have already been doing that. But, if it does apply to you, I hope this article provides another point of view of what testing is and why it is important, and maybe you can finally get rid of that giant checkbox-ridden spreadsheet.

As always, thanks for reading my article!

* * *

Cover image by [Glenn Carstens-Peters](https://unsplash.com/@glenncarstenspeters?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/@glenncarstenspeters?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText).
