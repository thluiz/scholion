---
url: "https://stephenbussey.com/2020/05/06/my-experiences-writing-real-time-phoenix.html"
captured_at: "2026-11-16T04:04:29+00:00"
title: "My Experiences Writing Real-Time Phoenix"
domain: "stephenbussey-com"
---

The initial itch to write a book formed over a couple of weeks around October of 2018. Of course, I was very naïve at the time. I thought that a book could be written in three weeks if one simply battened down the hatches and got it done—surely it would be done by Christmas. This may be true for some people, but the reality for me was quite different. This post goes through many of the different aspects of my writing journey.

I’m sure that everyone has a very different journey when writing a book, so take mine with a grain of salt. I’m hoping that you will find it useful if you’re thinking about writing, or maybe this post will help plant that seed. Maybe you’re just curious at the process of writing.

This post will be a bit longer than usual as I want to make sure that the different aspects are explained in-depth.

There is a 50% off code at the end of this post that is good until May 17, 2020. It’s the best deal you’re going to find!

## Why I Decided to Write

I was working on a project to extract the “live feed” feature out of the SalesLoft Rails monolith. The actual API surface and moving parts are very simple, so this was a good candidate for a rewrite into a Phoenix-backed application. I spent a couple of weeks on the implementation and things were going well—it was time to roll it out.

Despite the initial speed of developing the application, the rollout process took about 5 months. This was due to all of the little things that I took for granted coming to light. To be clear, the issues I ran into were not things that Phoenix lacked. Instead, they were the little nuances of writing a real-time app that I just didn’t know about. For example, I brought down the main application at least twice by overwhelming the monolith with thousands of simultaneous requests from the Elixir backend. (If you read the book, this is an example of an unintentional data pipeline, from Chapter 6.)

I emerged from that project with a lot more Elixir knowledge and a good primer for how to write real-time apps. I was pretty convinced that my experiences on the project would be good to share with the world. I wrote some blog posts about it and got good reception on those, but I kept seeing people running into similar issues on Slack and the Forums. This cemented the idea as a good one for writing about. After writing a few more real-time features for SalesLoft, I knew it would be a good time to write.

## Time to Find a Publisher

It seems that there are only a few major publishers in the Elixir world. The most prominent ones are Pragmatic Bookshelf and Manning Publications. Each publisher has an ideas email where you can shoot them an idea and they’ll let you know if they want a formal proposal or not. I submitted first to Pragmatic and…the results were bad. I tried a few more times with them but I just couldn’t make it work. However, my call with Manning seemed to go well and I sent them a formal proposal.

Writing a proposal is hard work. It was really the first dive into the book’s content that I took. I wrote pretty extensive outlines (I think something like 12 pages of just outlining) and had great feedback from the ten reviewers. The process of doing the proposal was one of the most valuable early stage things that I did though, because it forced me to flesh out my idea more and to realize what would and would not work. Despite the good feedback from Manning, I still really wanted to try to get something going with Pragmatic.

I ran into Bruce Tate at Lonestar Elixir 2019. I asked him about writing and explained where I was at in the process with Manning. He gave me some great advice on how to tweak my initial proposal that I sent to Pragmatic:

_**Focus on what you can do with the technology, and less on the technology itself.**_

My initial proposal was all about WebSocket and writing apps with them. This was a bad proposal. He got me to flip this a bit into building scalable real-time systems (the final product vs the technology used).

The new short-form proposal was well-received by the team. I was asked to send a formal proposal, which involves writing a meaty chapter from the book. This ended up being thirty pages of content. They reviewed this and it was accepted! I was going to write with Pragmatic! I was actually on the ski chairlift with my dad when the call from Bruce came in about it. I was so happy that I’m pretty sure I cried a bit.

The process between Lonestar Elixir to a signed contract was only about three weeks. I was incredibly impressed by Pragmatic’s speed here, and knew it would be a sign of a good relationship.

## The First Few Weeks

I was sent credentials to the Pragmatic build system, my book’s repository, a guide on how to write in their style (written using the same formatting as their books of course), and an introduction to my editor—Jackie. Everything came together quickly, so this felt very surreal and I wasn’t sure where to start.

They coached through the beginning of the writing process. I put together a more built-out outline for every chapter and stubbed out chapters with some basic flow information. The initial ask was to put together chapters 2-4, with a sync up on style and writing after each. I buckled down and got to writing. I was given a bit of guidance (and had the writing style guide), but was told to predominately just stay in my own style for these initial chapters.

The first chapters were difficult to write, to say the least. More difficult, however, was going through the chapters with Jackie and figuring out how to make them better. Each chapter would receive about fifty comments, so there was a lot to deal with. Like a PR, it is difficult to sent multiple weeks worth of work to someone else and have it broken down line by line. To anyone that hits this wall, it’s tough to deal with. Just keep learning, taking notes, adjusting, and pressing forward.

One humorous anecdote during the initial weeks is that I sent Jackie an initial timeline which had me finished with the book in August, only a few months out. She let me know that this was quite ambitious and to basically double or triple that estimate to get to the final book. Engineers are always under or over estimating, it seems.

## The Form of a Technical Book

One of the things that I hear most often when discussing writing a book is, “I could never do that, I can’t write 6 pages let alone 25, then 10+ chapters!” It is true that books are long and take time, but there’s a formula that honestly really helps out with the writing process.

Every single one of my chapters, without fail, started with a basic outline that went 2 levels deep. The top heading would be the section’s title in the table of contents, and subheadings would be solely for breaking down content for the reader. Establishing this outline in a single sitting let me really clearly construct where I wanted the chapter to go, without anything context switching me away from it. I would note things that I wanted to especially hit on, as well. Once the outline was written, I would walk away from writing for the day.

Each time that I sat down to write, I would start by establishing which of the subsections I wanted to write before calling it for the day. This gave me a goal that I could push for. To be honest, I wasn’t super great at hitting this all of the time, which I’ll touch on in the next section. I would try to complete a subheading in a single sitting to ensure continuity in my thoughts.

When writing a subheading, it follows a pretty predictable formula again and again. There is an introduction paragraph that goes into what the section will be about. This sets the expectations for the reader. There are then 3-5 meaty paragraphs going over the content of the section. Sometimes the section would get broken down into another level of headings, if it was an especially meaty one. There is then a final paragraph that sets the reader up for the next section they’re going to read.

This formula repeats for every section and every chapter of the entire book. I think that writing this way really helped me push through any mental barriers, and it also gives the reader knowledge of what they’re going to learn in the chapter and the sections of the chapter.

A chapter follows this same formula. There is an introduction section of roughly four paragraphs. This is followed by the various sections (as mentioned above), and then a “Wrapping Up” section that closes out the chapter, and more importantly preps the reader for the next chapter. When you write this way, all of a sudden hitting 20+ pages per chapter doesn’t seem so bad.

## The Long Haul

I was getting a pretty good rhythm going. Jackie was pleased with my writing, ability to quickly address feedback, and to reduce the number of repeat mistakes I would make. The number of times that I would get a chapter back from review, and the number of comments in the review, started to drop for each chapter. At the beginning, it would take at least three review rounds with 50, 35, 10 comments or so. By the end, it would take maybe two review rounds of 20, 5 comments.

However, I also hit a pretty big mental wall. I made good progress on Part 1 of the book (6 chapters), and started on Part 2. Part 2 was so much harder because the project that we make in the book continues for the rest of the book. It turns out that writing a coherent and useful example that spans many chapters is really hard. I went from giving Jackie a chapter every two weeks to about one every four weeks. That wasn’t good.

Writing during this time would often involve me sitting down at my computer and either doing nothing or doing very little for two hours. I felt pretty defeated, but I just couldn’t get it going. Another thing that I noticed is that I had a really hard time starting a new chapter, but I would push through a chapter pretty quickly once I started it. This is all pretty synonymous with burnout, which I’m sure there was a bit of.

The thing that saved me the most during this time was ElixirConf 2019. I was doing a training on real-time application development there, and I wanted to have the book in a beta release by then. A beta release is reserved for books that are ~60% done and have a good velocity to the finish. I pushed really hard to get the necessary chapters done for the beta release and was successful at it. Pragmatic really did me some favors during this time, though, as another author gave up their beta spot by two weeks to help make sure that mine hit the goal. I appreciated that a ton.

This long haul definitely ties into the hardest thing, for me, that happened when writing.

## The Hardest Part of Writing a Book

The hardest part of me writing this book was not the technical or writing aspect of it. Instead, it was the gnawing feeling that I should be writing. Hanging out with friends on the weekend? (You should really be writing right now.) Christmas party for work? (Don’t drink much, you need to hit that writing goal, and you took a different day off.) Cycling on my Tuesday night ride? (You need to get done early so you can get an hour of writing in.) Basically everything that I did came with this feeling in the back of my head. Even if I wasn’t planning on writing that night, it was still prevalent. I only didn’t feel this way when I had just completed a chapter and sent it to Jackie.

I put this here mainly as a warning and for something to consider if you’re looking to write a book. I haven’t really talked to many other authors about this feeling, so I’m curious if you wrote a book and the same thing happened to you. I have never felt this experience when it came to coding or other work, so it was new for me.

## Refactoring

I have typically not been great at refactoring my writing. I will proofread this post once and ship it. I think it’s important to not get bogged down in the little nuances, as the alternative can be paralyzing and make it difficult to deliver content. However, this is clearly not how a book works.

The story I want to share here is about chapter 3, 4, and 5 of the book. Believe it or not, these chapters started life as a single chapter. It was quite the monster, coming in at nearly 45 pages. The sample chapter that I wrote is closest to these chapters, which is part of why it may have ended up this way.

I worked hard with my editor to find all of the seams in the monster chapter to see how it could be broken apart. Doing this involves changing almost all of the transition text (introduction and transition paragraphs in the earlier described form) and also requires checking continuity. So it’s not a small thing. I was also able to expand more on the content in these chapters because they no longer were crammed in way too tight. I am proud of the final result of this work, though, as I’ve gotten compliments on the way that the material in these chapters is delivered.

I felt this same satisfaction anytime that I removed content. Removing content from a book is great, as it usually means that the concept can be described more simply and more succinctly somewhere else. Or it means that the content wasn’t important and that the reader no longer has to deal with carrying it in their head.

Jackie was great at helping me see opportunities for refactoring my chapters. It’s her job to deliver a well-flowing book, and she does a great job at coaching through that.

## Shipping The Book

The first release of the book came in August 2019 with the Beta release. This was definitely a big success for me, as it gave me motivation to keep pushing forward and also vetted the content with errata submissions. The final version released in April and has been available on [Amazon](https://www.amazon.com/gp/product/1680507192) and [Pragmatic Bookshelf](https://pragprog.com/book/sbsockets/real-time-phoenix).

I’m very happy with the final result. I’ve gotten some unsolicited praise from people that I’ve never met on the way that the book flows and the information presented in it. I think that there is always room for improvement, but it is important to be satisfied with a job well done.

![Steve Bussey holding Real-Time Phoenix](https://stephenbussey.com/images/holding-book.jpg)

## Thanks

Many people helped make this book possible. In particular, a decent number of technical reviewers contributed to vetting the material and helping to reduce the number of errors. This book would not have been the same without their suggestions and reviews. A large thanks to each of you: Amos King, Ben Olive, Chris Keathley, Dan Dresselhaus, Grant Powell, Gábor László Hajba, Johanna Larsson, John Oxford, Ray Gesualdo, Stefan Turalski, and Ulisses H. F. de Almeida.

I also want to thank the community and maintainers of libraries. Phoenix is amazing and brings me joy. Part of the reason for this is that it is so well-maintained by Chris McCord and others who contribute to it. Chris and others also contributed with their one-one conversations and forum posts.

## What’s Next?

Who knows, especially right now. I’m hoping to be able to continue trainings and presentations around the content in the book at conferences and meetups once things get back to normal. While I enjoyed the experience, I can say for sure that I’m not writing another book for a little bit. :)

I’m excited to get back into writing some greenfield software. I have a few ideas in my mind that I’m excited to flesh out more over the next few months.

## A Discount for the Weekend

There is a discount that is active on Pragmatic right now. You can get the Real-Time Phoenix ebook for 50% off, which is insane. You will not get a better price for as long as I can anticipate.

You can use the coupon code **Frameworks2020** for 50% off. This expires on May 17, 2020, although I’m not sure at what time. Purchase the book on [Pragmatic Bookshelf](https://pragprog.com/book/sbsockets/real-time-phoenix) with this coupon code to redeem your 50% off! You can see which other books are available for this deal in the [Pragmatic Newsletter](https://media.pragprog.com/newsletters/2020-05-11.html).
