---
url: "https://spin.atomicobject.com/reviewing-code-new-dev/?ref=dailydev"
captured_at: "2026-09-25T20:50:59+01:00"
title: "Code Review: A New Developer’s Guide"
domain: "spin-atomicobject-com"
---

As a new developer recently out of college, many parts of the job fall under “[what your computer science classes didn’t teach you](https://spin.atomicobject.com/computer-science-program/).” For me in my first few months working at Atomic Object, that was how to participate in reviewing code in a meaningful and productive way. 

Code review is part of a typical software development workflow that allows a team of developers to review and critique their teammate’s code before its merge or release. While teams conduct code reviews depending on their preferences and norms, the general goals remain the same. That is, to ensure high-quality code that meets team standards, find bugs, and increase visibility across the team, among others. 

For developers with less experience, code review can be a daunting task. Not only are you opening your own work up to critique, but you’re expected to provide feedback and constructive criticism to your (often more senior) colleagues. 

One of Atomic Object’s [core values](https://atomicobject.com/culture) is Teach and Learn, and over my first few months at Atomic, I’ve participated in many pull request reviews and learned a lot from my colleagues about best practices for doing so. Compiling what I learned from these experiences and asking some other developers about their approaches to pull requests and reviews, I wrote a new developer’s guide to code review. By sharing the knowledge I’ve gained over my first few months as a developer, I hope to help demystify the process of code review. I’ll also give some tips on how to contribute meaningfully to your team’s code review process. 

## Writing a Good Pull Request

A good code review starts with good code — or at least readable code. To ensure you get the best feedback possible, ensure your code is free of commented-out code blocks and debugging statements (console.log lovers, I’m looking at you). Moreover, if your work includes changes to the logic of the code, it should also include meaningful, passing unit tests directly related to the functions you worked on.  

When publishing a pull request, it’s important to detail the changes you made to the code and their purpose. A truly helpful pull request, however, includes more than a description of what was changed. You should also include testing instructions for those reviewing your code. 

Testing instructions should include the steps necessary to get to the correct state of the feature, and if relevant, any details on the data/examples you may have used to test your work. There is a healthy balance, however, to these instructions. Your instructions should be prescriptive regarding code set-up but not limiting to the reviewer. Code reviewers should be able to follow your instructions while also having the freedom to do their own exploratory testing. That may reveal bugs and edge cases that would otherwise go unnoticed. 

## Effectively Reviewing Pull Requests

The second half of a successful code review is the actual reviewing of changes and [pull requests](https://spin.atomicobject.com/pull-request-feedback/). While intimidating at first, learning to effectively critique your teammate’s code and offer suggestions benefits the entire team in the long run. 

### Run and Test

The first thing you must do when reviewing a colleague’s pull request is properly run and test their code. This can differ depending on the project or company, but you must be able to see the code run to test it effectively. If you need help replicating the code state or if the developer’s instructions were unclear, contact them and see if you can pair on testing the work. Don’t forget to run their unit tests and make sure they pass. (And point it out if they haven’t written any tests.) 

When testing others’ code, it is most helpful to test like a user. This means going through the typical actions that a user might take and identifying pain points or bugs present within that workflow. As mentioned before, test their changes beyond the instructions they may have left for you in a pull request. Test meaningfully, considering edge cases that may have been missed in the code. 

### Delivering Feedback

If you do find bugs or an inconsistency with the acceptance criteria, it’s important to think about [the way you deliver that feedback](https://spin.atomicobject.com/providing-feedback-new-developers/). First, check your assumptions at the door. Don’t assume that the behavior you encounter while testing code is incorrect. Instead, try offering instructions to reproduce the state that you found the potential issue in. Then, ask if it’s expected behavior. For example: 

“While testing your PR, I took actions x and y from the landing page and got z. Is that expected behavior?”  

Also,  leave room for personal preferences in coding style, so long as they don’t break the code or style expectations for a client. If your colleague writes an “if” statement slightly differently than you, you might consider taking a step back and not leaving a PR comment about it. 

The mode of feedback is important as well. It’s good to have notes and a paper trail for issues and fixes. However, it’s also kind to reach out in person with potential concerns or bugs. You could even suggest walking through them together. It’s much more effective to take 10 minutes to sort out assumptions and look at potential bugs side by side than to have a conversation in the comments of a pull request. If you want to keep track of the questions and decisions made during a conversation for posterity’s sake, you can always leave notes in the comments of the pull request after your conversation. 

## Keep the Team in Mind

In the end, remember that this is your teammate’s work that you’re reviewing. The effort you put into reviewing code reflects the care you have about your team’s success and product. This also applies to receiving feedback during a PR review. It’s freeing to accept feedback as a way to improve the work you’re doing as a team rather than a reflection on you as a person or your skills as a developer.

Anxiety about reviewing other’s code or having your own code reviewed is natural, especially as a new developer. But, it’s helpful to remember that feedback is vital to improving your software and to your professional growth as well as that of your team. Happy code reviewing!
