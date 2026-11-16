---
url: "https://zdnet.com/article/microsoft-heres-why-we-love-programming-language-rust-and-kicked-off-project-verona"
captured_at: "2026-11-16T04:01:22+00:00"
title: "Microsoft: Here’s why we love programming language Rust and kicked off Project Verona"
domain: "zdnet-com"
---

Watch More

Microsoft has explained why it’s pursuing ‘safe systems programming’ through efforts like its experimental Rust-inspired Project Verona language and its [exploration of the Rust programming language for Windows code written in C++](https://www.zdnet.com/article/microsofts-rust-experiments-are-going-well-but-some-features-are-missing/). 

The short answer is that Microsoft is trying to eliminate memory-related bugs in software written in languages like C++, according to Microsoft Rust expert Ryan Levick. These bugs cost a lot to fix and make up a large share of Patch Tuesday hassles. Levick has now offered more insights into Microsoft’s efforts behind safe systems programming. 

Systems programming includes coding for platforms like Windows, Xbox, and Azure, as opposed to programming applications that run on them. 

**SEE:** [**Hiring Kit: Python developer**](https://www.techrepublic.com/resource-library/whitepapers/hiring-kit-python-developer/?ftag=CMG-01-10aaa1b) **(TechRepublic Premium)**

Key systems programming languages include C++, Google-backed Go, and Mozilla-created Rust, but Rust and Go are ‘memory-safe’ languages while C++ is not. Other languages are memory safe, such as Swift and Kotlin, but they aren’t for systems programming.

The thing for Microsoft is that it writes a lot of its platform software in C++ and sometimes still in C. While it works hard to address memory issues, the company says it has “reached a wall”. 

“We can’t really do much more than we already have. It’s becoming harder and harder and more and more costly to address these issues over time,” says Levick, who joined Microsoft via its [acquisition of Wanderlist, which has become Microsoft To Do](https://www.zdnet.com/article/microsofts-wunderlist-successor-to-do-hits-public-preview/). He [gave a rundown of Microsoft’s safe systems programming efforts](https://mybuild.microsoft.com/sessions/61de34c5-b111-4ece-928f-541854875862?source=sessions) in a session at Build 2020 this week.  

Levick has been working with the Microsoft Security Response Center, the group at Microsoft that deals with security bugs across all its platforms, from Windows to Azure.    

As he explains, the whole software industry is turning out more code than ever and more code means more bugs, which demands a new approach. 

“That software by and large is getting safer and better, but people are writing so much more software that getting a little bit safer and better isn’t enough,” he said.  

“Over time, the number of bugs we introduce in the software – and this isn’t just the Microsoft software thing, this is the software industry as a whole – it’s increasing. 

“One particularly interesting part about what we found at Microsoft is [that 70% of our very serious, mission-critical bugs](https://www.zdnet.com/article/microsoft-70-percent-of-all-security-bugs-are-memory-safety-issues/) that happen in our software deal with memory safety and incorrect usage of memory.”

One piece of Microsoft’s answer to memory-related bugs is [Project Verona](https://github.com/microsoft/verona/blob/master/docs/faq.md), a [new safe infrastructure programming language being developed by Microsoft Research](https://www.zdnet.com/article/microsoft-opens-up-rust-inspired-project-verona-programming-language-on-github/), which takes cues from Rust and is [being supported by](https://www.zdnet.com/article/microsoft-were-creating-a-new-rust-based-programming-language-for-secure-coding/) Microsoft’s lead maintainer of the C# programming language, Mads Torgersen.

**SEE:** [**Programming language Rust’s adoption problem: Developers reveal why more aren’t using it**](https://www.zdnet.com/article/programming-language-rusts-adoption-problem-developers-reveal-why-more-arent-using-it/)

Levick says Project Verona is “completely memory safe” but that Microsoft still isn’t sure what the project will become. 

“We don’t want to constrain it down to being production-ready today because that’s not the point. So we need to look out to the industry to see what the best alternative to C++ is. And it turns out that language is a language called Rust.”

“We’re looking to adopt that language to make our system software at Microsoft more safe and reliable.”     

“When you’re programming in Rust you don’t have to worry about a whole host of issues that you do have to worry about.” That’s attractive, because in theory, Microsoft could get rid of 70% of its most serious bugs, which are also expensive to fix.  

The other project Microsoft [turned to Rust for is Krustlet](https://www.zdnet.com/article/microsoft-why-we-used-programming-language-rust-over-go-for-webassembly-on-kubernetes-app/), a ‘kubelet’ from the Azure team that lets developers run multiple WebAssembly modules (Wasm) in Kubernetes, the Google-backed open-source tool for managing Docker containers. 

While Rust has a steep learning curve, the Azure team behind Krustlet preferred Rust over Go because Rust was able to pick up bugs that Go could not. 

### More on Microsoft and programming language Rust

![Liam Tung](https://www.zdnet.com/wp-content/uploads/sites/3/liam-tung.jpg?w=64)

Liam Tung

Contributing Writer

Liam Tung is an Australian business technology journalist living a few too many Swedish miles north of Stockholm for his liking. He gained a bachelor's degree in economics and arts (cultural studies) at Sydney's Macquarie University but hacked (without Norse or malicious code for that matter) his way into a career as an enterprise tech, security, and telecommunications journalist with ZDNET Australia. These days Liam is a full-time freelance technology journalist who writes for several Australian publications, including the Sydney Morning Herald online. He's interested primarily in how information technology impacts the way businesses and people communicate, trade, and consume. [See full bio](https://www.zdnet.com/meet-the-team/lt-999f7/)
