---
url: "https://x.com/oliverjumpertz/status/1420729273518903300"
captured_at: "2021-07-29T13:43:43+00:00"
title: "Thread de @oliverjumpertz: I've been a software architect for most of my professional life, and system design has alw…"
domain: "x-com"
---

Thread de Oliver Jumpertz (@oliverjumpertz), 42 tweets.

## 1/42

I've been a software architect for most of my professional life, and system design has always been my bread and butter.

Here are 7 steps that I would advise you to follow to ace your system design interview.

They will bring you further than ever, promised.

A thread. ↓

([tweet](https://x.com/oliverjumpertz/status/1420729273518903300), 2021-07-29 12:53 UTC)

## 2/42

0. Foreword

As a software architect and tech lead, I had the chance to interview some very bright engineers throughout my career.

I've also interviewed quite a few times myself.

This approach is the one that I would use to design a system.

([tweet](https://x.com/oliverjumpertz/status/1420729274567434245), 2021-07-29 12:53 UTC)

## 3/42

I highly believe that this approach is the one you should use in your interviews, as it's an incremental and organized workflow.

Your goal is that your interviewers understand what you design.

This enables them to follow along as you design.

([tweet](https://x.com/oliverjumpertz/status/1420729275418873862), 2021-07-29 12:53 UTC)

## 4/42

1. Clarify the requirements

Ask questions and a lot of them.

Try to find out what exactly the interviewer expects from you.

Try to narrow it down as far as possible to the exact scope of the problem.

Even if the question is to (re)design an existing system, ask.

([tweet](https://x.com/oliverjumpertz/status/1420729276458946567), 2021-07-29 12:53 UTC)

## 5/42

The amount of questions you could ask is nearly endless, but here are some ideas for you:

- Are there multiple frontends (App + Website + more)?
- Are there regulatory requirements?
- Do we need our own auth, or can we leverage an existing one (like Facebook/Google, etc.)?

([tweet](https://x.com/oliverjumpertz/status/1420729277432143872), 2021-07-29 12:53 UTC)

## 6/42

- Are there other consumers than the known clients planned for our APIs?
- Do we need third-party integrations?
- Do we want to incorporate a data lake for analysis?
- Any requirements on data consistency?

([tweet](https://x.com/oliverjumpertz/status/1420729278329769986), 2021-07-29 12:53 UTC)

## 7/42

2. Define system interfaces

Define all APIs that the system will need.

Explain what each API is for as detailed as possible, so the interviewer can jump in and tell you if you got a requirement wrong.

If you got something wrong, no problem, adjust accordingly.

([tweet](https://x.com/oliverjumpertz/status/1420729279223115776), 2021-07-29 12:53 UTC)

## 8/42

To give you a general idea, take a platform like Instagram, for example, which will need APIs to:

- Upload and view images,
- Retrieve the feed
- Store and retrieve comments for an image
- Store and retrieve likes
- Manage your profile

([tweet](https://x.com/oliverjumpertz/status/1420729280129081347), 2021-07-29 12:53 UTC)

## 9/42

- Manage people's followers
- Store and retrieve stories
- Manage story reactions
- etc.

([tweet](https://x.com/oliverjumpertz/status/1420729281005621250), 2021-07-29 12:53 UTC)

## 10/42

As you see, existing systems are already pretty large, so it makes sense, and it's absolutely okay to ask your interviewer if you should really lay out everything you could think of or if you should only focus on one part of the existing system.

([tweet](https://x.com/oliverjumpertz/status/1420729281735499776), 2021-07-29 12:53 UTC)

## 11/42

-> Illustrating system interfaces

You can, for example, start with a use case diagram, which is a great way to identify and showcase possibly needed APIs.

([tweet](https://x.com/oliverjumpertz/status/1420729282603667460), 2021-07-29 12:53 UTC)

## 12/42

3. Estimate the scale of the system

Give estimates to the scale of the system and communicate them clearly.

Once again, if you got a requirement wrong, the interviewer can tell you, and you can adjust.

If not, the interviewer can better understand your design decisions.

([tweet](https://x.com/oliverjumpertz/status/1420729283945893891), 2021-07-29 12:53 UTC)

## 13/42

You don't need to give an exact estimate here.

Throw a number in the room which you find reasonable.

In the case of well-known platforms, inform yourself before the interview.

The numbers for Instagram, Facebook, etc., are all out there on the internet.

([tweet](https://x.com/oliverjumpertz/status/1420729284830838791), 2021-07-29 12:53 UTC)

## 14/42

Regarding numbers, we talk about:

- Active daily / monthly users
- being transformed to an estimate about how many API requests/s your system should be able to handle

([tweet](https://x.com/oliverjumpertz/status/1420729285715824643), 2021-07-29 12:53 UTC)

## 15/42

If you interview at an organization that has such a well-known platform, you can impress your interviewer if you have the numbers at hand.

This shows that you are really interested in the company and have done your homework.

([tweet](https://x.com/oliverjumpertz/status/1420729286567370756), 2021-07-29 12:53 UTC)

## 16/42

You don't have to memorize those numbers exactly, it's not even about 1 or 2 million more or less, but you shouldn't be off by hundreds of millions.

Being off by such a large amount could lead to design decisions you would not have made otherwise.

([tweet](https://x.com/oliverjumpertz/status/1420729287456567297), 2021-07-29 12:53 UTC)

## 17/42

4. Define the data model

Define the data model of the system, and define how data flows.

Ask how detailed this step should be and if your interviewer requires it at all.

If it's required, also explain and maybe visualize how data flows between the components of the system.

([tweet](https://x.com/oliverjumpertz/status/1420729288425414656), 2021-07-29 12:53 UTC)

## 18/42

Leverage relational models where applicable, but don't forget that there are other types out there, as well, like documents, graphs, and many more.

Try to use the most appropriate ones for the entity at hand.

([tweet](https://x.com/oliverjumpertz/status/1420729289419464708), 2021-07-29 12:53 UTC)

## 19/42

It might, for example, make sense to leverage graphs for friendship-like relationships or follower relations, as well.

If you find such a graph model fitting, use and model the entity accordingly.

([tweet](https://x.com/oliverjumpertz/status/1420729290279301121), 2021-07-29 12:53 UTC)

## 20/42

Don't forget to lay out how the entities move through the system.

For example:

The feed service fetches a user from the user service.

The user entity thus travels from the user service to the feed service, and maybe even further.

([tweet](https://x.com/oliverjumpertz/status/1420729291160100866), 2021-07-29 12:53 UTC)

## 21/42

You don't have to come up with the exact solution that the engineers of an existing platform came up with.

That's not what the interview is about.

Add the properties you may find fitting and which are just enough to fulfill the requirements.

([tweet](https://x.com/oliverjumpertz/status/1420729292011474954), 2021-07-29 12:53 UTC)

## 22/42

Your users, for example, will most likely need a forename, a name, an ID, an email address, and so on.

Common thought can already bring you far here.

If you are really unsure, ask your interviewer.

It's their job to give you hints in such a case.

([tweet](https://x.com/oliverjumpertz/status/1420729292921745411), 2021-07-29 12:53 UTC)

## 23/42

-> Illustrating entities and data flow

You can use a UML class diagram, draw a box with properties in it, or list the properties of an entity to describe the data.

![imagem](https://pbs.twimg.com/media/E7dxus-WYAEfteD?format=jpg&name=orig)

([tweet](https://x.com/oliverjumpertz/status/1420729293802459146), 2021-07-29 12:53 UTC)

## 24/42

To illustrate the data flow, you can use simple illustrations to showcase how the data flows for certain operations.

![imagem](https://pbs.twimg.com/media/E7dxu8oXoAAkV8j?format=jpg&name=orig)

([tweet](https://x.com/oliverjumpertz/status/1420729295069122565), 2021-07-29 12:53 UTC)

## 25/42

5. Draw a high-level design

Most systems only have a few crucial components that make up the core of the system.

Try to identify them and draw boxes for the five most important ones, and visualize their interactions.

([tweet](https://x.com/oliverjumpertz/status/1420729296289738755), 2021-07-29 12:53 UTC)

## 26/42

Especially in modern microservice environments, services communicate with each other (a lot).

If service A needs some data managed by service B, you already have two boxes and one arrow to draw to illustrate that communication.

([tweet](https://x.com/oliverjumpertz/status/1420729297216675842), 2021-07-29 12:53 UTC)

## 27/42

Remember: If you have already modeled the data flow of certain entities, reuse this information here.

([tweet](https://x.com/oliverjumpertz/status/1420729298114256899), 2021-07-29 12:53 UTC)

## 28/42

-> Illustrating the high-level design

Once again, a simple illustration with some boxes and some arrows, including descriptions, is enough to showcase the design you have in mind.

![imagem](https://pbs.twimg.com/media/E7dxvQnXEAoTLVZ?format=jpg&name=orig)

([tweet](https://x.com/oliverjumpertz/status/1420729298902831105), 2021-07-29 12:53 UTC)

## 29/42

6. Design components in detail

Explicitly ask if you should focus on specific components for this step.

If not, choose the three most important ones and visualize/explain how they should work and what they should do in detail.

A good interviewer will guide you.

([tweet](https://x.com/oliverjumpertz/status/1420729300223922182), 2021-07-29 12:53 UTC)

## 30/42

Take an image service, for example, that is one of the core components of an Instagram-like system.

It offers an API to retrieve images, which is handled by an internal implementation.

([tweet](https://x.com/oliverjumpertz/status/1420729301088014339), 2021-07-29 12:53 UTC)

## 31/42

To store images, it needs access to some kind of storage handled by another internal implementation.

Lay all that out, draw diagrams to illustrate your ideas, and help the interviewer understand what you are designing.

([tweet](https://x.com/oliverjumpertz/status/1420729301968773125), 2021-07-29 12:53 UTC)

## 32/42

-> Illustrating detailed components

You could try to resemble a UML component diagram to illustrate a detailed service view, for example.

([tweet](https://x.com/oliverjumpertz/status/1420729302904152066), 2021-07-29 12:53 UTC)

## 33/42

7. Explicitly state bottlenecks

Every system and every design has its limits.

If there are bottlenecks in your system (and there will always be), state them explicitly.

Give detailed explanations about what affects them and how you could mitigate them.

([tweet](https://x.com/oliverjumpertz/status/1420729304187613184), 2021-07-29 12:53 UTC)

## 34/42

This step requires the most knowledge about the components you used to design your system.

You'll have to know, for example, when relational databases fall behind NoSQL storages noticeably or in which situations certain message brokers are not the best choice anymore.

([tweet](https://x.com/oliverjumpertz/status/1420729305089331205), 2021-07-29 12:53 UTC)

## 35/42

Maybe a relational model was good for the anticipated scale of the system, but migration becomes a pain at some point?

([tweet](https://x.com/oliverjumpertz/status/1420729305982808068), 2021-07-29 12:53 UTC)

## 36/42

You can be pretty creative in this step, but once again, you need to know the advantages and disadvantages of components and also the design principles you built your system upon.

([tweet](https://x.com/oliverjumpertz/status/1420729306746134531), 2021-07-29 12:53 UTC)

## 37/42

Sometimes interviewers will also jump in and give you hints or state a bottleneck they found explicitly.

That's your chance to discuss it with the interviewer and find a solution together.

([tweet](https://x.com/oliverjumpertz/status/1420729307635322887), 2021-07-29 12:53 UTC)

## 38/42

You don't have to be able to recall each and every disadvantage, but be able to state the most important ones.

([tweet](https://x.com/oliverjumpertz/status/1420729308482609162), 2021-07-29 12:53 UTC)

## 39/42

8. Thread end

That's it for this thread. 

I hope you found something useful in it for you. 

If you enjoyed reading this thread, drop a like, retweet the first tweet, and follow me (
@oliverjumpertz
) for more content like this.

([tweet](https://x.com/oliverjumpertz/status/1420729309271150592), 2021-07-29 12:53 UTC)

## 40/42

Woohooo, glad you like this one, Meet!

([tweet](https://x.com/oliverjumpertz/status/1420734390963949580), 2021-07-29 13:14 UTC)

## 41/42

Hehe, already released one last week that included what I had for interviews until then, but might definitely do another one, soon!

([tweet](https://x.com/oliverjumpertz/status/1420734764647059459), 2021-07-29 13:15 UTC)

## 42/42

Awww, This means a lot to me, thank you! 

Just doing my very best.

([tweet](https://x.com/oliverjumpertz/status/1420735758290259970), 2021-07-29 13:19 UTC)

## Respostas do autor na conversa

Tweets do mesmo autor na conversa, publicados depois da thread (em geral respostas a comentários).

---

System design is mandatory knowledge for any senior role.

([tweet](https://x.com/oliverjumpertz/status/1420753550636818435), 2021-07-29 14:30 UTC)

---

The larger the company the more likely you are to be confronted with system design on any level. Sometimes it's not about a whole system but the architecture of the app and the systems interfacing with it.

([tweet](https://x.com/oliverjumpertz/status/1420753950064594954), 2021-07-29 14:31 UTC)

---



([tweet](https://x.com/oliverjumpertz/status/1420763206755045377), 2021-07-29 15:08 UTC)

---

Hey Faheem, my friend, I am super happy that this series does help you, and especially this thread!

([tweet](https://x.com/oliverjumpertz/status/1420763422157774858), 2021-07-29 15:09 UTC)

---

Glad to hear that!

([tweet](https://x.com/oliverjumpertz/status/1420763661128196100), 2021-07-29 15:10 UTC)

---

Thank you for this awesome feedback, Manoj!

([tweet](https://x.com/oliverjumpertz/status/1420763805231947791), 2021-07-29 15:11 UTC)

---

Woohooo, thanks a lot, Krishnaa! This makes me a happy creator!

([tweet](https://x.com/oliverjumpertz/status/1420786327176556546), 2021-07-29 16:40 UTC)

---

Thank you, Gaurav!

([tweet](https://x.com/oliverjumpertz/status/1420786648338599938), 2021-07-29 16:41 UTC)

---

Awesome to hear, thanks a lot, mate!

([tweet](https://x.com/oliverjumpertz/status/1420786895857061895), 2021-07-29 16:42 UTC)

---

Thank you!

([tweet](https://x.com/oliverjumpertz/status/1420787065780850690), 2021-07-29 16:43 UTC)

---

WoohooX awesome to hear this, Vitto, really glad you like this!

([tweet](https://x.com/oliverjumpertz/status/1420803998593003535), 2021-07-29 17:50 UTC)

---

This makes me happy, Kashish!

([tweet](https://x.com/oliverjumpertz/status/1420805517732192268), 2021-07-29 17:56 UTC)

---

Still not bad!  Great move!

([tweet](https://x.com/oliverjumpertz/status/1420810616646811649), 2021-07-29 18:17 UTC)

---

Whoaw, thank you, Hamza! Glad my content delivers what you look for!

([tweet](https://x.com/oliverjumpertz/status/1420823677113937923), 2021-07-29 19:08 UTC)

---

Hope this helps:


https://
get.oreilly.com/ind_software-a
rchitecture-patterns.html
…

Links: https://t.co/q47Dptc05S

([tweet](https://x.com/oliverjumpertz/status/1420993980565708801), 2021-07-30 06:25 UTC)

---

It'll take more than one book, though.

It's a lot about trying things out, learning what works and what doesn't.

Every system is different, and there is usually not "the correct" approach.

([tweet](https://x.com/oliverjumpertz/status/1420994099277181058), 2021-07-30 06:26 UTC)

---

My pleasure

([tweet](https://x.com/oliverjumpertz/status/1420994311156649986), 2021-07-30 06:26 UTC)

---

Thanks a lot, Fred!

([tweet](https://x.com/oliverjumpertz/status/1420994728200478722), 2021-07-30 06:28 UTC)

---

https://
interviewing.io/recordings/Jav
a-Google-1/
…


https://
youtube.com/watch?v=IWvbPI
YQPFM
…


https://
youtube.com/watch?v=057Rs6
CgJnY
…

Links: https://t.co/XJkfPugToc, https://t.co/x6pFXctRf2, https://t.co/jWIEwH649I

([tweet](https://x.com/oliverjumpertz/status/1420995287506735104), 2021-07-30 06:30 UTC)

---

Thank you for this, Chetan! I am super happy you like it!

([tweet](https://x.com/oliverjumpertz/status/1420996354990563328), 2021-07-30 06:35 UTC)
