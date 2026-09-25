---
url: "https://www.howtogeek.com/habits-to-grow-to-become-a-better-programmer/?ref=dailydev"
captured_at: "2026-09-25T22:14:00+01:00"
title: "Become a Better Programmer: 7 Habits to Grow"
domain: "howtogeek-com"
---

[![4](https://static0.howtogeekimages.com/wordpress%2Fwp-content%2Fauthors%2F64ec9d39c2d32-pic%20square.jpg?fit=crop&w=90&h=90)](https://www.howtogeek.com/author/zunaid-ali/)

Published Jan 28, 2025, 8:30 AM EST

Zunaid Ali first became interested in technology after using a computer for the first time in 2006. He's been producing how-to content since 2018, reaching thousands of people in the process.

As a kid, Zunaid used to read tech tutorials and troubleshooting guides on popular blogs. That made him want to start his own writing career. After the coronavirus pandemic, he finally decided to jump into the tech writing world. Before joining How-To Geek, he had written for HecticGeek, Distroid, and UbuntuPIT, among others.

Zunaid first tried Linux when he wanted to learn Web Development in 2021. Due to his inexperience, he messed up his laptop trying to dual-boot Ubuntu with Windows. Frustrated, he went all-in with Linux and removed Windows completely. And that's when he fell in love with it. He's been actively experimenting with Linux since then.

After finding his first writing gig on Linux in April 2022, he decided to specialize in it so he could share his knowledge and insights with fellow open-source enthusiasts. He joined How-To Geek in September 2023 and has been writing as a freelance contributor since then.

Zunaid is currently pursuing his Bachelor's degree in Information & Communication Technology. When he's not writing, he's reading tech blogs, coding fun projects, or learning about new technologies. Other than Linux, he also has an interest in Android Development and Cybersecurity. He has experience in C/C++, Java, HTML/CSS/JavaScript, and Python. You can find some of his hobby projects on [his GitHub](https://github.com/rustybladez).

Are you a beginner programmer looking to go to the next level? Here are some of the best habits I adopted and how they made me not only a better programmer but also a better professional.

## 7 Start With a Strong Foundation

When I first started programming, I fell into the trap of rushing the basics and jumping straight to the more juicy stuff like frameworks and advanced tools. I wanted to build cool apps and shiny websites right away. So, I tried to skip the boring stuff as much as possible.

However, at some point, I realized something. I could copy-paste code and get it to work. But it was all spaghetti code, jumbled together, barely working without any optimization. I couldn't solve any problems on my own. Ultimately, I was forced to revisit the basics again and again.

One way to build this foundation is to challenge yourself with simple problems before diving into bigger projects. Platforms like [HackerRank](https://www.hackerrank.com/) and [CSES](https://cses.fi/problemset/) are great for this. Another essential part of building a foundation is learning one [programming language](https://www.howtogeek.com/838826/what-is-a-programming-language/) deeply before branching out.

## 6 Do More Thinking Than Writing Code

    ![A man using a laptop with a tip symbol in the center](https://static0.howtogeekimages.com/wordpress/wp-content/uploads/2024/04/a-man-using-a-laptop-with-a-tip-symbol-in-the-center.jpg?q=49&fit=crop&w=825&dpr=2)Credit: Lucas Gouveia / How-To Geek | [Gorodenkoff](https://www.shutterstock.com/image-photo/portrait-young-black-man-working-on-2324952215) / [Kolonko](https://www.shutterstock.com/image-vector/effective-thinking-concept-solution-bulb-icon-1165554163) / Shutterstock

Whenever you want to build something, you probably open the code editor and start writing code. We do this so that we can quickly see a tangible result. However, in my experience, I've seen that this often leads to messy, incomplete, or sometimes entirely wrong solutions.

A problem I faced a lot was when I was halfway in, I realized that I didn't take one case or another into account when coding the solution. I had to start over. If I had an overall high-level solution before writing the code, this wouldn't have happened.

Programming isn't just about writing code. It's about crafting a solution to a problem, often under some constraints. Like any complex problem, the best solution comes from clear, deliberate thinking. This is from one of my favorite books, [The Pragmatic Programmer](https://www.amazon.com/Pragmatic-Programmer-journey-mastery-Anniversary-dp-0135957052/dp/0135957052?tag=hotoge-20&ascsubtag=UUhtgUeUpU2009201&asc_refurl=https%3A%2F%2Fwww.howtogeek.com%2Fhabits-to-grow-to-become-a-better-programmer%2F&asc_campaign=Feed):

> In order to be a Pragmatic Programmer, we're challenging you to think about what you're doing while you're doing it...Never run on auto-pilot. Constantly be thinking, critiquing your work in real time.

One thing that has made me a better problem-solver is writing pseudocode before writing the actual code. For example, when designing a complex algorithm, I'll sketch a rough logical plan in plain English.

## 5 Learn From the Official Documentation

    ![A laptop with the Python download webpage open on Chrome.](https://static0.howtogeekimages.com/wordpress/wp-content/uploads/2024/08/52848278425_0515827579_o.jpg?q=49&fit=crop&w=825&dpr=2)Credit: Hannah Stryker / How-To Geek

When I first started programming, I avoided official documentation like the plague. It looked overwhelming, full of jargon, and honestly, a little boring. I preferred sticking to tutorials and YouTube videos. But as I started working on real-world projects, I realized that tutorials only scratched the surface. If I wanted to fully understand a language, framework, or tool, the official documentation was my best resource.

Official documentation is a user manual written by the people who created the language or tool you’re learning. Tutorials tend to focus on specific use cases, but documentation shows you the full capabilities of a technology, including features you may not have known existed.

For example, when I first learned Python, I relied heavily on tutorials to understand the basics. But when I started using libraries like pandas, I found myself needing more than just examples. The pandas documentation became my lifeline.

## 4 Write Clean Code

There's a running joke in the programming community. If your program runs, don't touch it. It's just a joke, though.

When I was getting started on programming, I tried [competitive programming](https://www.howtogeek.com/level-up-your-coding-try-a-competitive-coding-challenge/). Though I was enjoying it, I adopted many bad habits from it. In most cases, making the program work was the only thing that mattered. If the code ran without errors, I considered it a success, even if it was a tangled mess of variables and [magic numbers](https://en.wikipedia.org/wiki/Magic_number_\(programming\)). But as I started working on more real-world projects, I realized how crucial clean code is.

Clean code makes your programs easy to read, debug, and maintain. There are many best practices, principles, and conventions that go into this. For example, descriptive names for variables and functions, good documentation, consistent coding style, and more. Let's look at an example of ugly code.

```
def pro(s, x):

   i = 0

   for k in range(len(s)):

       i += s[k] * x[k]

   return i
```

It works. But can you make anything out of it? Probably not. Now have a look at the cleaner version:

```
def calculate_dot_product(vector_a, vector_b):

   dot_product = 0

   for index in range(len(vector_a)):

       dot_product += vector_a[index] * vector_b[index]

   return dot_product
```

This version is much more meaningful. That's how writing clean code can fully transform your projects.

## 3 Develop Strong Debugging Skills

    ![Google Edge poster of a programmer using computer with multiple screens.](https://static0.howtogeekimages.com/wordpress/wp-content/uploads/2024/12/google-edge-poster-of-a-programmer-using-computer-with-multiple-screens.jpg?q=49&fit=crop&w=825&dpr=2)Credit: [Google](https://fiber.google.com/cities/huntsville/)

No matter how much experience you gain as a programmer, [debugging](https://www.howtogeek.com/devops/debugging-with-gdb-getting-started/) is an inevitable part of the process. I’ve spent countless hours tracking down sneaky bugs that seemed to hide in plain sight. At first, debugging felt frustrating. Over time, I learned to approach it strategically.

The first step in debugging is to slow down and observe. I used to rush into my code, blindly changing lines, hoping something would work. It rarely did. Instead, start by asking questions. What is the program supposed to do? What is it doing? Where does behavior diverge?

There are several [tools and techniques that make debugging less daunting](http://www.howtogeek.com/devops/what-is-a-debugger-why-to-use-one-when-programming/). The `print()` statement is often the first line of defense. Another useful technique is rubber duck debugging, where you explain your code, step by step, to an inanimate object or a person. Often, simply articulating the problem out loud reveals the solution. I’ve solved bugs just by explaining them to myself.

## 2 Network With Other Programmers

When I first started programming, I thought of it as a solo journey. While programming often involves solitary focus, the moments where I grew the most came from connecting with other programmers.

I've joined many programming Facebook groups, [Discord servers](https://www.howtogeek.com/364075/how-to-create-set-up-and-manage-your-discord-server/), and subreddits (check out [r/learnprogramming](https://www.reddit.com/r/learnprogramming/).) When I'm facing problems, I can reach out for help. In my free time, I try to contribute to the community as well, so that beginners can get help just like I used to.

I once landed a programming gig solely through networking. It was one of the biggest projects I've worked on, and I learned a lot in the process. I've also met great programmers by attending hackathons and learned new things and strategies from them.

## 1 Build Something That Solves a Real-Life Problem

One of the most rewarding aspects of programming is the ability to turn ideas into tools that make life easier. You can watch tutorials or read books endlessly, but nothing compares to the learning you gain when you tackle a real-world problem. That’s when the theories, syntax, and algorithms truly come alive.

You can find [real-life projects](https://www.howtogeek.com/python-programming-for-beginners-lets-build-a-simple-quiz-app/) in many ways. What problems do you face? Can you solve them by building an app? Ask your friends and relatives about their problems. You can also go to [GitHub](https://www.howtogeek.com/github-is-the-best-place-for-free-and-open-source-software/) and [find open-source projects](https://www.howtogeek.com/want-to-contribute-to-open-source-software-heres-how-to-get-started/).

When I started learning Java backend using Spring Boot, I decided to make an agricultural system to automate many of the tasks. I learned about many things that I wouldn't have from tutorials.

* * *

When you're new to programming, it's easy to fall into traps and [make mistakes](https://www.howtogeek.com/things-i-wish-i-knew-when-i-first-learned-programming/). By adopting great habits and learning from experience, you can have a head start. That'll make you a better programmer.
