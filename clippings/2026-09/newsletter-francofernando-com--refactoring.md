---
url: "https://newsletter.francofernando.com/p/refactoring?ref=dailydev"
captured_at: "2026-09-25T18:08:05+01:00"
title: "Refactoring"
domain: "newsletter-francofernando-com"
---

[

![](https://substackcdn.com/image/fetch/$s_!H5AQ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe43f9255-eb13-45ab-a9e0-2b513cf924f0_1000x639.webp)

](https://substackcdn.com/image/fetch/$s_!H5AQ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe43f9255-eb13-45ab-a9e0-2b513cf924f0_1000x639.webp)

Hi Friends,

Welcome to the 95th issue of the Polymathic Engineer newsletter.

This week, we will talk about something that every developer needs to deal with: code refactoring.

The outline will be as follows:

*   Why is refactoring important
    
*   Practice refactoring
    
*   How to avoid common pitfalls
    
*   Leverage your IDE
    

Project-based learning is the best way to build technical skills. [CodeCrafters](https://app.codecrafters.io/join?via=FrancoFernando) is an awesome platform to practice interesting projects such as building your version of Redis, Kafka, HTTP server, SQLLite, and even Git from scratch.

[Sign up, and become a better software engineer](https://app.codecrafters.io/join?via=FrancoFernando).

Refactoring is an important part of coding, but it is often underestimated since it can make or break the long-term success of a software project.

_But why is it so important?_

First, refactoring is about maintaining and improving the health of your codebase. As a project grows and evolves, it's natural for the code to become more complex. If you don't do regular refactoring, this complexity can quickly become a mess that is hard to understand, maintain, and extend.

Think of refactoring as a regular exercise for your code. Just as you would expect to stay fit with consistent workouts, you can only expect your codebase to remain clean and efficient with refactoring efforts.

Well-refactored code is easier to read and understand, directly affecting how quickly new team members get up to speed and how efficiently other developers can work.

When the code is well-structured and free of unnecessary complexity, it's much easier to maintain. This means fewer bugs, quicker fixes when issues arise, and less time spent understanding what a specific piece of code does.

It is also much easier to add new features to code that has been refactored. You are more likely to find places where it makes sense to add new features without breaking existing code.

While not the primary goal, refactoring can often lead to performance improvements. As you simplify and streamline your code, you might uncover more efficient ways of accomplishing tasks.

As with many other skills, refactoring improves with practice. The more you practice it, the better you become.

The best way to become proficient is to make refactoring a regular part of your coding routine.

A good approach is to start with your own code. Once you completed a task and your code works, read through all the changes with a critical eye. Look for pieces of code that could be more expressive or easier to understand. When you spot something you can improve, make the change.

You can also use code reviews as inspiration. When people review your code or when you check other code reviews, pay attention to comments suggesting improvements.

Code review comments often highlight opportunities for refactoring, even in parts of the code not directly changed. If you spot something worth refactoring, you can talk about that with your team and volunteer to do the job.

Another approach you can use is to create a refactor backlog. While reading code, you can take notes of inconsistencies, hard-to-understand parts, inconsistent naming, or apparent duplications. In this sense, unit tests are often a golden opportunity since developers usually add tests following an established style without improving it.

From time to time, you can discuss your observations with other team members, get their feedback, and decide which refactoring makes sense. Once you build your list of refactoring, you can work on it alongside your regular tasks.

Do it when you have some downtime, like while waiting for code reviews or between tasks. After each refactor, seek feedback from others and repeat the process.

By consistently practicing refactoring, you not only make the codebase better but also learn more about the system and make your teammates like you more. If you work in a healthy team, people will appreciate your efforts to improve the code quality.

When doing refactoring, it's crucial to pause and think about avoiding some potential pitfalls. The following considerations could save you and your team headaches and a significant amount of time:

*   **Resist the urge to rewrite everything.** It's tempting to think you can replace all the existing code with better code, but you should avoid rewriting everything from scratch. Remember that the existing code has been tested, reviewed, and used in production. Reusing as much code as possible is important since it may contain workarounds and bug fixes you're unaware of.
    
*   **Make incremental changes.** Instead of a single big change, make many small, incremental improvements. With this approach, it's easier to figure out how the changes affect the system by getting feedback from tests. It is easier to deal with a few test failures at a time than with hundreds of failures after a big change.
    
*   **Maintain tests.** After each iteration, you should check that existing tests still pass and add new tests if the current ones don't sufficiently cover your changes. Don't discard old tests without careful consideration since they might be covering edge cases you haven't thought about.
    
*   **Keep personal preferences in check.** Your personal coding style preferences or the belief that you could do a better job than the previous developer are not valid reasons for restructuring. Stay humble, and always remember that humans make mistakes.
    

Most modern IDEs have built-in features that can make refactoring much more efficient and error-free. Learning how to use these features is a good time investment.

Simple operations like renaming variables, changing signatures, and extracting logic into their own functions are time-consuming and risky to do manually. But they become quick and safe with the help of the IDE.

Exploring your IDE's menu and learning the keyboard shortcuts for these operations will save you time in the long run.

Instead of changing a variable name manually throughout your code, use the rename feature so you're sure not to miss any occurrences. Similarly, if you want to split up a big function, use the "extract method" tool to make a new function with your chosen code.

You can make changes quickly and with more trust without slowing down your development process too much if you use the refactoring tools in your IDE.

Here are some interesting articles I read this week:

*   [Not All Features Are Equal](<http://Not All Features Are Equal>) by [Raul Junco](https://open.substack.com/users/98661477-raul-junco?utm_source=mentions)
    
*   [Become Bronze, Become Tough](https://newsletter.memesmotivations.com/p/m-and-ms-become-bronze-become-tough) by [Louie Bacaj](https://open.substack.com/users/95150107-louie-bacaj?utm_source=mentions)
    
*   [Intro to OAuth 2](<http://Intro to OAuth 2>) by [Saurabh Dashora](https://open.substack.com/users/97484183-saurabh-dashora?utm_source=mentions)
    
*   [My strategy against distractions as a software engineer working in an open-floor office](<http://My strategy against distractions as a software engineer working in an open-floor office>) by [Fran Soto](https://open.substack.com/users/170998285-fran-soto?utm_source=mentions)
