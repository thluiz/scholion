---
url: "https://x.com/milan_milanovic/status/1721837211794997519"
captured_at: "2023-11-12T06:26:21+00:00"
title: "Thread by @milan_milanovic: 𝗪𝗼𝗿𝗸𝗶𝗻𝗴 𝗘𝗳𝗳𝗲𝗰𝘁𝗶𝘃𝗲𝗹𝘆 𝗪𝗶𝘁𝗵 𝗟𝗲𝗴𝗮𝗰𝘆 𝗖𝗼𝗱𝗲 In his book \"Working Effectively With Legacy Code,\" M…"
domain: "x-com"
---

Thread by Dr Milan Milanović (@milan_milanovic), 2 tweets.

## 1/2

𝗪𝗼𝗿𝗸𝗶𝗻𝗴 𝗘𝗳𝗳𝗲𝗰𝘁𝗶𝘃𝗲𝗹𝘆 𝗪𝗶𝘁𝗵 𝗟𝗲𝗴𝗮𝗰𝘆 𝗖𝗼𝗱𝗲

In his book "Working Effectively With Legacy Code," Michael Feathers wrote about dealing with legacy software. Even though it's a bit outdated (from 2004.), there are some excellent points inside that still hold their value. This book offers us confidence that we can employ focused, incremental unit testing and refactoring to improve the testability, comprehension, and extensibility of legacy software while implementing and delivering new functionality.

The author defines legacy code as "𝘤𝘰𝘥𝘦 𝘸𝘪𝘵𝘩𝘰𝘶𝘵 𝘵𝘦𝘴𝘵𝘴." This implies that if the code doesn't have tests, it's challenging to ensure that changes to the code will only introduce unintended side effects or break existing functionality.

He lists four reasons to change software:

 𝗔𝗱𝗱𝗶𝗻𝗴 𝗮 𝗳𝗲𝗮𝘁𝘂𝗿𝗲
 𝗙𝗶𝘅𝗶𝗻𝗴 𝗮 𝗯𝘂𝗴
 𝗜𝗺𝗽𝗿𝗼𝘃𝗶𝗻𝗴 𝘁𝗵𝗲 𝗱𝗲𝘀𝗶𝗴𝗻 (𝗶.𝗲., 𝗿𝗲𝗳𝗮𝗰𝘁𝗼𝗿𝗶𝗻𝗴)
 𝗢𝗽𝘁𝗶𝗺𝗶𝘇𝗶𝗻𝗴 𝗿𝗲𝘀𝗼𝘂𝗿𝗰𝗲 𝘂𝘀𝗮𝗴𝗲

He says that regardless of how the code is altered, we must always uphold other behaviors we do not plan to change. 

The main contribution of this book is the Legacy Code Change Algorithm:

𝟭. 𝗜𝗱𝗲𝗻𝘁𝗶𝗳𝘆 𝘁𝗵𝗲 𝘁𝗮𝗿𝗴𝗲𝘁𝗲𝗱 𝗹𝗲𝗴𝗮𝗰𝘆 𝗰𝗼𝗱𝗲: Identify change points (Seams) for the target change or new code addition and Find test points where the code's behavior can be sensed.

𝟮. 𝗚𝗲𝘁 𝘁𝗮𝗿𝗴𝗲𝘁𝗲𝗱 𝗹𝗲𝗴𝗮𝗰𝘆 𝗰𝗼𝗱𝗲 𝗶𝗻𝘁𝗼 𝗮 𝘁𝗲𝘀𝘁 𝗵𝗮𝗿𝗻𝗲𝘀𝘀 𝗮𝗻𝗱 𝗰𝗼𝘃𝗲𝗿 𝘄𝗶𝘁𝗵 𝘁𝗲𝘀𝘁𝘀: Break dependencies (very carefully and often without sufficient tests) and get the targeted legacy code into a test harness and cover targeted legacy code with (characterization) unit tests.

𝟯. 𝗔𝗱𝗱 𝗻𝗲𝘄 𝗳𝘂𝗻𝗰𝘁𝗶𝗼𝗻𝗮𝗹𝗶𝘁𝘆 𝘄𝗶𝘁𝗵 𝗻𝗲𝘄 𝘁𝗲𝘀𝘁𝘀 (by using the Test Driven Development (TDD) process).

𝟰. 𝗥𝗲𝗳𝗮𝗰𝘁𝗼𝗿 𝘁𝗲𝘀𝘁𝗲𝗱 𝗰𝗼𝗱𝗲 to remove duplication, clean up, etc.

He also suggests some techniques:

 𝗜𝗱𝗲𝗻𝘁𝗶𝗳𝘆𝗶𝗻𝗴 𝘀𝗲𝗮𝗺𝘀: Find places to change the behavior without modifying the code. Seams can be at the class, method, or function level and help you isolate parts of the code for testing and refactoring.

 𝗦𝗽𝗿𝗼𝘂𝘁 𝗺𝗲𝘁𝗵𝗼𝗱 𝗮𝗻𝗱 𝗦𝗽𝗿𝗼𝘂𝘁 𝗰𝗹𝗮𝘀𝘀: When adding new functionality, create a new method (Sprout method) or a new class (Sprout class) instead of modifying existing code. Unit tests it and identifies where to call that code from the existing code (the insertion point). Then, contact your code from the Legacy code.

 𝗪𝗿𝗮𝗽 𝗺𝗲𝘁𝗵𝗼𝗱 𝗮𝗻𝗱 𝗪𝗿𝗮𝗽 𝗰𝗹𝗮𝘀𝘀: When you need to modify the behavior of a method or class, create a new method or class that wraps the original one with the same signature. Rename the old method you want to wrap. Then, call the old method from the new method and put the new logic before/after the other method call.

#technology #softwareengineering #programming #techworldwithmilan #coding

![image](https://pbs.twimg.com/media/F-UxtXVWYAAZQME?format=jpg&name=orig)

([tweet](https://x.com/milan_milanovic/status/1721837211794997519), 2023-11-07 10:29 UTC)

## 2/2

To expand your knowledge and personal growth, subscribe to my free weekly newsletter with 18,000+ people: 
https://
newsletter.techworld-with-milan.com.

Links: https://t.co/MMCXxQQR4F

([tweet](https://x.com/milan_milanovic/status/1721837255738700058), 2023-11-07 10:29 UTC)
