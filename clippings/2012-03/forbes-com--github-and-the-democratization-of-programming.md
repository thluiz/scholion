---
url: "http://www.forbes.com/sites/venkateshrao/2012/03/27/github-and-the-democratization-of-programming/"
captured_at: "2012-03-30T14:19:43-03:00"
title: "GitHub and the Democratization of Programming - Forbes"
domain: "forbes-com"
---

# GitHub and the Democratization of Programming

Over the past few months, I’ve received one comment several times: “I didn’t expect to read something like this on *Forbes.*” To me the comment reflects a rather unfortunate and growing divide between the worlds of technology and business. The two worlds are getting increasingly intertwined, but at the same time, business people are getting increasingly disconnected from technology. As a result, their intuitions about technological evolution are getting weaker, and people with pure business backgrounds are getting blindsided with increasing frequency by technology developments they didn’t see coming.

So I’ve decided I am going to start posting more about under-the-hood technology subjects and why they matter to the world of business. First up, an interview with [Chris Wanstrath](https://github.com/defunkt) , co-founder and CEO of [GitHub](https://github.com/) . Chris and I started chatting over email after I wrote my post, *[The Rise of Developeronomics](http://www.forbes.com/sites/venkateshrao/2011/12/05/the-rise-of-developeronomics/) ,* and I decided it would be interesting to turn our conversation into an interview.

[![29495ca6218553903ddc0a7254478dcd.jpg](forbes-com--github-and-the-democratization-of-programming/29495ca6218553903ddc0a7254478dcd.jpg)](http://blogs-images.forbes.com/venkateshrao/files/2012/03/chrisWanstrath.jpg)

If you are the typical business-oriented *Forbes* reader and don’t normally follow behind-the-scenes technology news, you may have never heard of GitHub. It is a programming and code-sharing community built around [Git](http://en.wikipedia.org/wiki/Git_(software)) , a source code control system developed by Linus Torvalds of Linux fame, and among technologists, sometimes viewed as a more important contribution to technology.

Source code control systems are somewhat abstruse pieces of software for managing code, so why should business people, especially mainstream ones, care?

It’s because software culture evolves around tools that are hidden from public view, and as code becomes increasingly critical to everyday life, everybody, programmer or not, needs to develop an appreciation for how the world of software works. Code unfortunately is especially hard to understand, since the processes that create it are so abstract, unlike assembly lines, railway yards or blast furnaces. Most non-engineers don’t realize, for instance, that the programming that goes into a toy robot takes an order of magnitude more time and effort than the mechanical and electrical engineering. Code is the hidden 9/10ths of the technology iceberg today.

The big message that emerged for me, from the conversation with Chris, was this: *programming is being democratized.* Many people have been saying this in recent months. Lifehacker for instance, recently included coding in their list post, [Top 10 Essential DIY Skills That Aren’t As Hard as You Think](http://lifehacker.com/5896102/top-10-essential-diy-skills-that-arent-as-hard-as-you-think) . But Chris’s version of the message is particularly interesting because of his privileged view from what is increasingly the center of the programming universe, both professional and amateur. So here we go.

*Q: [Sourceforge](http://sourceforge.net/) [an older programmer community] grew around the previous generation of version control systems like CVS and Subversion. GitHub has grown around Git. Are there social differences between the two communities that can be attributed to the design philosophies of the revision-control systems that inspired them?*

A: Absolutely. CVS and SVN are centralized version control systems – you can’t really do anything without a central server. If you want to see or make a change, you need a server. If you want to grab your friend’s code, you need a server.

Git is different. It’s a distributed version control system, meaning you don’t need a server – you have everything you need locally. You can make changes on an airplane. You can grab code from a friend at a coffee shop over wifi. Servers are optional. Everyone has the ability to share code with anyone else using Git.

And that’s exactly what GitHub is all about: sharing code. Working with other people. It’s not about creating big projects or looking official, it’s about getting your code into the hands of a stranger, friend, or co-worker.

It’s also so much easier and faster to create a project using Git that people end up doing it more. GitHub hosts everything from small config files and tiny experiments to major open source projects. The range is incredible.

*Q: Since GitHub is becoming a place where programmers find work, not just a  place where they store their code, how should hiring managers think about  the difference between GitHub on the one hand, and sites like LinkedIn, oDesk and the various job-hunting sites?*

A: GitHub is a great way to see what people have been working on. Not what they say they’ve been working on, but the actual projects they’ve contributed to. In many ways it’s like a portfolio or resume.

Like a portfolio or resume, GitHub works best for evaluating candidates. Once you have someone interested, or once you’ve found someone you’d like to hire, check out their GitHub profile. See what they’ve been doing. See who they follow and what they’re interested in.

If you want to hire someone to code JavaScript, GitHub is an excellent way to see what sort of JavaScript projects they’re interested in or working on.

*Q: The scarcity of developers is creating interesting dynamics, like the hackathon tradition of “idea generators” pitching their ideas to coders and designers, rather than the latter being “interviewed” by non-technical types. Is this power shift temporary, or here to stay?*

A: What we’ll see in the future is more people who aren’t programmers learning to code. Authors, lawyers, bankers – all kinds of people who don’t write code for a living will learn how to. They’ll automate repetitive tasks and build their own apps.

The “idea generators” will bring their ideas to life on their own. They’ll be the ones building the prototypes, pitching with demos instead of slides.

It’s already happening. But as software continues to become more important, coding is going to become more mainstream.

*Q: There is a lot of debate about the difference between 10x developers and average ones. Is this phenomenon real, and are there visible patterns of social organization on GitHub that can be attributed to the 10x effect?*

A: I don’t buy the 10x theory. I’ve known horrible programmers who were prolific. I’ve known great programmers who were slow but thorough.

In my experience the best developers are all curious, passionate people. They care about their craft and want to make something great. They’re always looking for ways to improve themselves and their code. It’s how they go from novice to expert – by constantly learning.

*Q: There is a whole alternative universe of code out there, centered around things like Microsoft’s TFS and the world of corporate application lifecycle management. What is the relationship between the GitHub world and this other universe?*

A: We’re trying to make life better for everyone developing software. Whether you’re working in a massive corporation with workflows decades old or you’re an idea generator creating a prototype on nights and weekends, we want GitHub to make your life easier.

Our GitHub Enterprise ([https://enterprise.github.com](https://enterprise.github.com/) ) product was created to help us spread GitHub to more people. So whether you’re stuck behind a firewall or have full access to the web, we want GitHub to work for you.

In other words: we see only one world, and that’s the world where people build awesome software.

*Q: If programming is going to get more mainstream, to what extent will it be due to programming itself becoming easier, and to what extent will it be due  to changes in education? Will other aspects of being a doctor or lawyer become easier or will everybody just have to work harder and acquire programming skills in addition to their other skills?*

A: It’s going to get easier for people to get started, definitely. Part of that is changing education. Sites like [Codecademy](http://www.codecademy.com/) are making it more accessible and more fun to learn programming. You don’t even need to sign up to start learning.

Part of it is the increasing influence of software in our lives. Someone who may not care about creating a web page might really want to create an iPhone app. The more we interact with software, the more opportunities there are for us to get excited and want to figure out how it works.

*Q: What changes are currently happening in both software engineering and education that provide hints of what things will look like in say 20 years? Do you actually see doctors doing app development on the side on GitHub or something? Or are there are other signs?*

A: The professions that are going to get the most out of programming in the near future are those that spend a large amount of time in front of a computer. Writers, customer support, even teachers. These people can customize their web browser or even write small apps to help their workflow – things programmers do every day to make their lives easier.
