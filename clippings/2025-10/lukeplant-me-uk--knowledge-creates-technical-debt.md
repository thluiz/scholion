---
url: "https://lukeplant.me.uk/blog/posts/knowledge-creates-technical-debt/?utm_source=tldrnewsletter"
captured_at: "2025-10-21T18:15:15+01:00"
title: "Knowledge creates technical debt - lukeplant.me.uk"
domain: "lukeplant-me-uk"
---

---
The term [technical debt](https://en.wikipedia.org/wiki/Technical_debt), now used widely in software circles, [was coined to explain a deliberate process where you write software quickly to gain knowledge](https://www.youtube.com/watch?v=pqeJFYwnkjE), and then you have to use that knowledge gained to improve your software.

This perspective is still helpful today when people speak of technical debt as only a negative, or only as a result of bad decisions. Martin Fowler’s [Tech Debt Quadrant](https://martinfowler.com/bliki/TechnicalDebtQuadrant.html) is a useful antidote to that.

A consequence of this perspective is that technical debt can appear at any time, apparently from nowhere, if you are unfortunate enough to gain some knowledge.

If you discover a better way to do things, the old way of doing it that is embedded in your code base is now “debt”:

-   you can either live with the debt, “paying interest” in the form of all the ways that it makes your code harder to work with;
    
-   or you can “pay down” the debt by fixing all the code in light of your new knowledge, which takes up front resources which could have been spent on something else, but hopefully will make sense in the long term.
    

This “better way” might be a different language, library, tool or pattern. In some cases, the better way has only recently been invented. It might be your own personal discovery, or something industry wide. It might be knowledge gained through the actual work of doing the current project (which was Ward Cunningham’s usage of the tem), or from somewhere else. But the end result is the same – you know more than you did, and now you have a debt.

The problem is that this doesn’t sound like a good thing. You learn something, and now you have a problem you didn’t have before, and it’s difficult to put a good spin on “I discovered a debt”.

But from another angle, maybe this perspective gives us different language to use when communicating with others and explaining why we need to address technical debt. Rather than say “we have a liability”, the knowledge we have gained can be framed as an opportunity. Failure to take the opportunity is an opportunity cost.

The “pile of technical debt” is essentially a pile of **knowledge** – everything we now think is bad about the code represents what we’ve learned about how to do software better. The gap between what it is and what it should be is the gap between what we used to know and what we now know.

And fixing that code is not “a debt we have to pay off”, but an investment opportunity that will reap rewards. You can refuse to take that opportunity if you want, but it’s a tragic waste of your hard-earned knowledge – a waste of the investment you previously made in learning – and eventually you’ll be losing money, and losing out to competitors who will be making the most of their knowledge.

Finally, I think phrasing it in terms of knowledge can help tame some of our more rash instincts to call everything we don’t like “tech debt”. Can I really say “we now **know**” that the existing code is inferior? Is it true that fixing the code is “investing my knowledge”? If it’s just a hunch, or a personal preference, or the latest fashion, maybe I can both resist the urge for unnecessary rewrites, and feel happier about it at the same time.

_This is my personal blog, and does not necessarily reflect the opinions of my clients/employer or my church._
