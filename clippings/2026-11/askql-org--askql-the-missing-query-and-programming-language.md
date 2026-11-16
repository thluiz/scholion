---
url: "https://askql.org/press-release"
captured_at: "2026-11-16T03:53:56+00:00"
title: "AskQL - the missing query and programming language"
domain: "askql-org"
---

Since software development is always slower than expected, xFAANG offers an Open Source solution we have all been waiting for. AskQL - a complete query and programming language. “It is asynchronous by default, processes only immutable data and is entirely based on the functional programming paradigm” - says Marcin Hagmajer, AskQL creator.

“Using AskQL flexible distributed software can be delivered easier and faster, compared to other currently existing solutions” \- underlines Hagmajer. Indeed, this technology eliminates the need to create multiple API endpoints - with the AskVM (Ask Virtual Machine) set up only one endpoint needs to be created. This might be especially important for frontend and backend integration. How can one endpoint be enough, you might be wondering. Well, that’s where the real potential of AskQL reveals itself.

## Powerful query programming

AskQL allows developers to ask the service any complex questions about the data. Queries are made with AskScript, a simple, human-friendly programming language. AskScript is reported to have a low learning curve for those who already know JavaScript or GraphQL, though beginning coders shall also find AskScript easy to pick up.

**Client**

![](https://askql.org/images/computer.svg)

**AskScript**

query { meaningOfLife }

**AskCode**

q(computeAnswerToTheMeaningOfLife)

![](https://askql.org/images/arrow-right-2.svg)

![](https://askql.org/images/arrow-left-2.svg)

**Query Result**

**JSON**

**AskCode**

q(computeAnswerToTheMeaningOfLife)

![](https://askql.org/images/arrow-right-2.svg)

![](https://askql.org/images/arrow-left-2.svg)

**Query Result**

**JSON**

**Server**

![](https://askql.org/images/askVM.svg)

**AskVM**

meaningOfLife: 42

Queries are sent to and interpreted by AskVM, a secure sandbox environment installed on the server side. AskVM processes each request individually and decides which resources to give access to, based on the schemas and security policies defined by the developer.

AskQL standard library is created in AskCode in order to make it ultimately lightweight. It contains all necessary functions, but you can also write your own contributions to the GitHub repository, as AskQL has been published under MIT license.

## “The ancestors”

The AskQL author and architect Marcin Hagmajer admits that, in creating the new query language JavaScript and GraphQL fortes were distilled. Even though JavaScript has been criticized for being a multi-paradigm language, its popularity and versatility is unquestionable. AskQL takes a lot of its structures, while leaving out the confusing elements.

The community was also truly astonished in 2015 when Facebook published the open source tool called GraphQL. This groundbreaking discovery of the decade eclipsed REST API for several years.

## AskQL philosophy and design

AskQL is to GraphQL what GraphQL has been to REST API. Hagmajer asked himself this question: “Why not execute the program on the server, and just retrieve the specific data the frontend is asking for?”. This called for the design of a new query language that would implement the functionalities of a programming language. Hagmajer also wanted it to be flexible and lightweight, so bearing in mind the Occam’s razor he decided to build it of mere functions. He heard the voice of the Haskell’s Ghost echoing in his flat in Warsaw, Poland, when he was explaining the concept to the xFAANG team.

[xFAANG Ltd.](http://xfaang.com/) is a newly established software company he co-founded, which hires only top IT specialists from companies such as Facebook, Amazon, Apple, Netflix and Google (FAANG). xFAANG developers had eagerly picked up on the idea and created the foundations of AskQL in less than a month, hosting its public release on the 25th of May, 2020.

Check out [AskQL GitHub repository](https://github.com/xFAANG/askql) and feel free to submit pull requests of your own! You can also share your opinion on [AskQL Discord channel](https://discord.gg/pYdzypH). Your feedback will be very helpful to the community.

AskQL. Write flexible distributed software easier and faster than ever.

Landing page: [https://askql.org/](https://askql.org/)

Docs: [https://www.notion.so/AskQL-Documentation-cd065c579d0c44d381ddddc4682f5736](https://www.notion.so/AskQL-Documentation-cd065c579d0c44d381ddddc4682f5736)

GitHub: [https://github.com/xFAANG/askql](https://github.com/xFAANG/askql)

Discord Community: [https://discord.gg/pYdzypH](https://discord.gg/pYdzypH)

Video: [https://www.youtube.com/watch?v=A2i2oyBwdAc](https://www.youtube.com/watch?v=A2i2oyBwdAc)

[Em Português](https://askql.org/press-release-pt)
