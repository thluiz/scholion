---
url: "https://semaphoreci.com/blog/books-every-senior-engineer-should-read"
captured_at: "2022-04-07T20:26:27-03:00"
title: "10 Books Every Senior Engineer Should Read"
domain: "semaphoreci-com"
---

Engineers are natural readers. They take enormous pleasure in learning about new things, and books are the perfect medium to cover complex ideas in depth.

At Semaphore, we’ve picked our favorite books — books that have profoundly influenced our company’s engineering culture. This list contains a mixture of classic, timeless texts and a fair share of modern game-changing publications, aimed at senior engineers and devs. But you don’t have to be a senior engineer to benefit from the books on this list, anyone interested in software development would enrich their skillset by reading them.

We hope you enjoy reading this list as much as we enjoyed making it.

### _Extreme Programming Explained: Embrace Change (2nd Edition)_ by Kent Beck

[![](https://semaphore.io/wp-content/uploads/2022/04/xp.jpg)](https://www.amazon.com/Extreme-Programming-Explained-Embrace-Change/dp/0321278658)

The 90s were a defining era for software development. The dot-com boom created enormous pressure to release early and frequently. Productivity had never before been so critical for success in the IT industry.

A paradigm shift was needed, and Kent Beck delivered in 1999. [_Extreme Programming Explained_](https://www.amazon.com/Extreme-Programming-Explained-Embrace-Change/dp/0321278658) presented and refined every agile practice we take for granted today: pair programming, automated testing, Test-Driven Development, and the [10-minute continuous integration build](https://semaphore.io/blog/2017/03/02/what-is-proper-continuous-integration.html):

> “… I bought an ordinary kitchen timer and decreed that no design meeting could be longer than 10 minutes. I don’t believe the timer was ever used, but its visible presence reminded everyone to be aware of when a discussion had ceased being useful and had turned into a process for avoiding going and writing some code to get the answer for sure.”
> 
> Kent Beck

The second edition refines the original idea: stay aware, adapt, and change. There is no shame in changing. On the contrary, being prepared to change is a good engineering habit.

Kent doesn’t stop at the technical details. He discusses the social aspects of development: interacting with teammates and management, the work ethics programmers should follow, and how a flat hierarchy helps everyone work toward a common goal. This book has everything you need to make a sustainable XP team.

**Why should you read it**: this is a book that will challenge your view on software development in fewer than 200 pages.

### _Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation_ by Jez Humble and David Farley

[![](https://semaphore.io/wp-content/uploads/2022/04/cd.jpg)](https://www.amazon.com/Continuous-Delivery-Deployment-Automation-Addison-Wesley/dp/0321601912)

In this book, David Farley and Jez Humble take the principles of continuous integration introduced in [_Extreme Programming Explained_](#xp) to the next level. [_Continuous Delivery_](https://www.amazon.com/Continuous-Delivery-Deployment-Automation-Addison-Wesley/dp/0321601912) teaches you how to make release and deployment as trivial as pushing a button.

Jez and David’s message can sound counterintuitive at first glance: _“if it hurts, do it more frequently, and bring the pain forward”_. It’s tempting to put off the difficult parts of the development cycle, but doing that won’t make them easier. If integration is painful, do it every time someone checks in. If testing is painful, do it continually, rather than at the end. Bring the pain forward: do the hard things first and you’ll be forced to face the challenges and find solutions.

The book goes into great detail on building, structuring, and maintaining a delivery pipeline, including what kinds of tests to use, how to handle data, and how to evolve it as the project grows. While some of the tools used in the book are a bit dated, its ideas and principles are timeless. This is the definitive DevOps guide that will make you stop stressing about deployments.

**Why should you read it**: any team that has not read this book has not yet reached its maximum potential.

### _Remote: Office Not Required_ by Jason Fried and David Heinemeier Hansson

[![](https://semaphore.io/wp-content/uploads/2022/04/remote.jpg)](https://www.amazon.com/Remote-Office-Required-Jason-Fried/dp/0804137501)

If the pandemic has shown off something, it is that remote work is not the future, it’s the present. We’ve been forced into working from our homes with little time to adapt. In [_Remote_](https://www.amazon.com/Remote-Office-Required-Jason-Fried/dp/0804137501), Jason Fried and David Heinemeier Hansson show how Basecamp [became a 100% remote company](https://m.signalvnoise.com/how-basecamp-became-a-100-remote-company/).

The book sets out to disarm the common excuses against remote work: face-to-face communication **is not** irreplaceable and people **can** (and should) be trusted to be productive at home. The authors argue that offices, so-called “interruption factories”, are never where real work takes place.

**Why should you read it**: as a manager, this book shows you what a successful remote team looks like. As a worker, it goes into practices that help us collaborate remotely while staying clear of the pitfalls home offices can present.

### _The Mythical Man-Month_ by Frederick P. Brooks Jr.

[![](https://semaphore.io/wp-content/uploads/2022/04/month.jpg)](https://www.amazon.com/Mythical-Man-Month-Software-Engineering-Anniversary/dp/0201835959)

> _“How does a large project get to be one year late? One day at a time”._
> 
> Fred Brooks

You’ve probably read dozens of books about being a successful engineer, but how many failure stores have you read? [_The Mythical Man Month_](https://www.amazon.com/Mythical-Man-Month-Software-Engineering-Anniversary/dp/0201835959) shows the perils all complex projects must face.

The titular “man-month” represents the erroneous idea that you can accelerate a project by adding people to the team. As a manager of IBM’s OS/360 project, the author (Turing award-winner Frederick P. Brooks), observed that additional people caused the project to be further delayed instead. Brooke’s Law states that _“adding manpower to a late software project makes it later”_.

While you can dig a ditch faster by adding more arms to the task, some tasks (like software projects) do not benefit from adding more people to the mix: _“The bearing of a child takes nine months, no matter how many women are assigned. Many software tasks have this characteristic because of the sequential nature of debugging.”_ Essentially, the more complex the task, the more difficult it is to divide it into discrete, parallelizable tasks.

In this book, the author sets out to explain why software development is more like pregnancy than ditch-digging. His observations and insights into human nature offer invaluable lessons about managing the lifecycle of a complex project, managing communication in a team, planning, and estimating work timetables.

**Why should you read it**: it has been almost 50 years since this book was published and we are still making the same mistakes while managing software projects. This cautionary tale should be read at least once by all engineers.

### _Getting Real_

[![](https://semaphore.io/wp-content/uploads/2022/04/getting-real.png)](https://basecamp.com/books/getting-real)

[_The Mythical Man-Month_](#month) showed us how complex project management is. For the folks at Basecamp, prevention is better than a cure. [_Getting Real_](https://basecamp.com/books/getting-real) is a free ebook on how to keep projects simple.

Behind rallying cries such as “build less, build simple”, “be minimalist”, and “build the tool that suits your needs”, this book pushes us to skip many of the design stages and get to building as soon as possible.

> “How do you manage \[feature requests\]? You don’t. Just read them and throw them away… the ones that are important will keep bubbling up anyway.”

This is an ebook that reflects Basecamp’s philosophy of building and working. It emphasizes building unified teams, breaking down silos, trusting people to work independently, and avoiding meetings. It’s a set of rules that has worked for Basecamp and it may work for you. But even if it doesn’t, the core values behind these principles are worth learning.

**Why should you read it**: this is a no-nonsense, succinct book on building lean products with a remote team in the most direct way. Best of all, [it’s free](https://basecamp.com/books/getting-real)!

### _Designing Data-Intensive Apps_ by Martin Kleppmann

[![](https://semaphore.io/wp-content/uploads/2022/04/data-intensive.jpg)](https://www.amazon.com/Designing-Data-Intensive-Applications-Reliable-Maintainable/dp/1449373321)

Data is the lifeblood of every application. Knowing how to design and manage large datasets is a vital skill for any senior engineer, who will be tasked with scaling up a system sooner or later. Martin Klepmann’s [_Designing Data-Intensive Apps_](https://www.amazon.com/Designing-Data-Intensive-Applications-Reliable-Maintainable/dp/1449373321) is a definitive guide, covering everything from data models, SQL and NoSQL databases, message queues, distributed systems, and big data.

The book is primarily theory-based — you won’t find code or demos. At the same time, it’s a practical text that examines the tradeoffs of several types of data-processing technologies.

**Why should you read it**: if you develop applications that consume or process data of any type, this book will help you to balance the pros and cons of the available technology.

### _Site Reliability Engineering_

[![](https://semaphore.io/wp-content/uploads/2022/04/sre.jpg)](https://sre.google/sre-book/table-of-contents)

Software development has a hidden side that most technical books ignore: how to keep a system online once built. [_Site Reliability Engineering_](https://sre.google/sre-book/table-of-contents), a collection of essays by Google employees, remedies this omission.

Service Reliability Engineers (SREs) are the unsung heroes behind every successful product. SREs are highly specialized engineers charged with keeping systems alive, finding problems before they happen, doing post-mortems when something terrible inevitably happens, and taking care of all the _glue work_ needed to make sure it never happens again. They have the near-impossible task of scaling up platforms while keeping them reliable.

SRE is one of the available paths for a senior engineer, but even if that’s not your job description, the skills you can learn in this book will help you build more resilient products. If you’ve ever been on-call or organized an on-call rotation, you know how hard and demanding it is. This book gives tips that lead to reliable services and sustainable workloads over time.

**Why should you read it**: this is an invaluable manual on how the largest software company in the world manages risk and keeps systems running.

### _The Phoenix Project_ by Gene Kim, Kevin Behr, and George Spafford

[![](https://semaphore.io/wp-content/uploads/2022/04/phoenix.jpg)](https://www.amazon.com/Phoenix-Project-DevOps-Helping-Business/dp/0988262592)

[_The Phoenix Project_](https://www.amazon.com/Phoenix-Project-DevOps-Helping-Business/dp/0988262592) is unlike all other books on the list. It is the story of a fictional company called “Parts Unlimited” and its journey towards agile practices.

The book starts with a crisis. The CEO is stepping down after the stock price plummets; the company is bleeding money and falling behind competitors. Amid this crisis, Bill Palmer (the main character) is tasked to take on a project that shall make everything right again: the promising “Phoenix Program”.

For a change of pace from more technical reading, this book is excellent. Gene Kim, Kevin Behr, and George Spafford have created a thrilling story with entertaining dialogue and a satisfying conclusion. This is a business novel with a warning against hero figures in a company.

**Why should you read it**: this is a modern-day IT fable that should resonate with any seasoned engineer. If you’re tired of reading drier technical books, this is a perfect choice.

### _Building Microservices: Designing Fine-Grained Systems_ by Sam Newman

[![](https://semaphore.io/wp-content/uploads/2022/04/microservices.jpg)](https://www.amazon.com/Building-Microservices-Designing-Fine-Grained-Systems/dp/1491950358)

Cloud-native applications have made learning about microservices obligatory. New projects are beginning to extensively use microservices and it’s common to see monolith’s broken down into distributed systems. [_Building Microservices_](https://www.amazon.com/Building-Microservices-Designing-Fine-Grained-Systems/dp/1491950358), by Sam Newman from ThoughtWorks, will show you how to do both.

Full of concrete examples of organizations using microservices to scale their operations, this book discusses how to architect, build, deploy, secure, and monitor a distributed system.

**Why should you read it**: this is a comprehensive guide on microservices and distributed systems that stays away from buzzwords and gets to the heart of the matter.

### _Modern Software Engineering: Doing What Works to Build Better Software Faster_ by Dave Farley

[![](https://semaphore.io/wp-content/uploads/2022/04/modern-1.jpg)](https://www.amazon.com/-/es/David-Farley-ebook-dp-B09GG6XKS4/dp/B09GG6XKS4)

In the software industry, software engineering and coding are used interchangeably. The reality is that engineering is a lot more than just code. [_Modern Software Engineering_](https://www.amazon.com/-/es/David-Farley-ebook-dp-B09GG6XKS4/dp/B09GG6XKS4) attempts to reclaim the original meaning of the term: “_the application of an empirical, scientific approach to finding efficient, economic solutions to practical problems in software._”

After challenging academic theories, this book sets outs to find a rational, practical, and sustainable framework for software development. The author adopts an iterative, experimental-based approach, reminiscent of [Fred Brooks](#month) proposal to _“throw away a prototype”_. It’s an attitude that is not as common in software development as in other engineering fields, which makes this book even more valuable.

David shows how to make design decisions using concrete examples. The book covers essential aspects of the craft, such as abstraction, separation of concerns, and modularity to manage complexity. It complements [Continuous Delivery](#cd), rather than trying to replace it.

**Why should you read it**: this is a book that you wished existed when you started working in software development.

## Conclusion

Every top booklist reflects the values and experiences of its authors. Invariably, over the course of our careers we encounter books that deeply affect the way we think and work. These are the ones that did it for us at Semaphore.

🚀**Did you know we’re hiring? We’re looking for engineers of all ranks to be a part of Semaphore’s global team.** [More details on how to apply here](https://apply.workable.com/semaphore/).
