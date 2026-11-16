---
url: "https://medium.com/@kevlinhenney/comment-only-what-the-code-cannot-say-dfdb7b8595ac"
captured_at: "2026-11-16T06:15:07+00:00"
title: "Comment Only What the Code Cannot Say | by Kevlin Henney | Medium"
domain: "medium-com"
---

Comment Only What the Code Cannot Say
The challenge is not to write comments for what code does not say, but to write comments for what code cannot say
Kevlin Henney
4 min read
·
Apr 29, 2020

A previous version of this article appeared in 97 Things Every Programmer Should Know

As with any other form of writing, there is a skill to writing good comments in code. And, as with any other form of writing, much of the skill is in knowing what not to write.

It has been said that the difference between theory and practice is greater in practice than it is in theory. This observation certainly applies to comments. In theory, the general idea of commenting code sounds like a worthwhile one: offer the reader detail, an explanation of what’s going on. What could be more helpful than being helpful? In practice, however, comments all too easily and all too often become a blight.

When code is ill-formed, compilers, interpreters, and other tools will be sure to object. If the code is in some way functionally incorrect, reviews, static analysis, tests, and day-to-day use in a production environment will flush out many bugs. A known bug is a call to action.

But what about comments? In The Elements of Programming Style, Kernighan and Plauger note that

A comment is of zero (or negative) value if it is wrong.

Incorrect comments, however, do not seem to raise the same sense of alarm as incorrect code. Such comments often litter and survive in a codebase in a way that coding errors never could. They provide a constant source of distraction and misinformation, a subtle but constant drag on a programmer’s time and attention.

What of comments that are not technically wrong, but add no value to the code? Such comments are noise. Comments that parrot the code offer nothing extra to the reader — stating something once in code and again in natural language does not make it any truer or more real. Although often interpreted simply as a principle of avoiding code duplication, DRY (Don’t Repeat Yourself) cautions more broadly against repeated expression of knowledge within a system.

If repeating the workings of code in comments is noisy, retaining code in comments is noisier. Commented-out code is not executable code, so it has no useful effect for either reader or runtime. A common justification for retaining commented-out code is that it might (in some indefinite future, for reasons unknown) become useful. Commented-out code, however, becomes stale very quickly. As time passes, it becomes increasingly less likely that uncommenting such code will be meaningful or even compilable — and be careful what you wish for: in the worst case, it will compile. Version-related comments and commented-out code try to address questions of versioning and history. These questions have already been answered (far more effectively) by version control tools.

A prevalence of noisy comments and incorrect comments in a codebase can instil a habit in programmers: a habit to ignore all comments, either by skipping past them or by taking active measures to hide them. Programmers are resourceful and will route around anything perceived to be damage: folding comments up; switching syntax colouring so that the comments and the background are the same colour; scripting to filter out comments. To save a codebase from such misapplications of programmer ingenuity — and to reduce the risk of overlooking any comments of genuine value — comments should be treated as though they were code. Each comment should add some value for the reader, otherwise it is waste that should be removed or rewritten.

What then qualifies as value? Comments should say something code does not and cannot say. Ask what problem the presence of a comment addresses, and ask if there’s another way to solve it. A comment explaining what a piece of code should already say is an invitation to change code structure or coding conventions so the code speaks for itself.

Instead of compensating for poor variable, method, class, or test names, rename them. Instead of commenting sections in long functions, extract smaller functions whose names capture the former sections’ intent. Instead of writing apologies and apologia, follow Kernighan and Plauger’s advice from the 1970s:

Don’t comment bad code — rewrite it.

Try to express as much as possible through code that means something to both the compiler and the programmer. Use language structure, identifiers, and idioms to communicate to the reader what you mean. Any shortfall between what you can express in code and what you would like to express in total becomes a plausible candidate for a useful comment. Comment what the code cannot say, not simply what it does not say.
