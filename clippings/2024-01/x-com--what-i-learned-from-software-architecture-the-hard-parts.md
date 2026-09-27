---
url: "https://x.com/milan_milanovic/status/1742095333499310164?s=20"
captured_at: "2024-01-02T08:07:48+00:00"
title: "Dr Milan Milanović (@milan_milanovic) on X"
domain: "x-com"
---

𝗪𝗵𝗮𝘁 𝗜 𝗹𝗲𝗮𝗿𝗻𝗲𝗱 𝗳𝗿𝗼𝗺 𝘁𝗵𝗲 𝗦𝗼𝗳𝘁𝘄𝗮𝗿𝗲 𝗔𝗿𝗰𝗵𝗶𝘁𝗲𝗰𝘁𝘂𝗿𝗲: 𝗧𝗵𝗲 𝗛𝗮𝗿𝗱 𝗣𝗮𝗿𝘁𝘀

I recently read the book "𝗦𝗼𝗳𝘁𝘄𝗮𝗿𝗲 𝗔𝗿𝗰𝗵𝗶𝘁𝗲𝗰𝘁𝘂𝗿𝗲: 𝗧𝗵𝗲 𝗛𝗮𝗿𝗱 𝗣𝗮𝗿𝘁𝘀" by Neal Ford, Mark, Richards, Pramod Sadalage & Zhamak Dehghani. The book is mainly related to breaking monolith applications into microservices and could be an excellent companion to the book "Monolith to Microservices," by Sam Newman.

The book emphasizes the step-by-step approach of breaking down monolith, with different patterns for each step, and balancing tradeoffs for those patterns. The book is titled "Hard Parts," yet most of the concepts in the book are familiar.

Here are 𝘁𝗵𝗲 𝘁𝗵𝗶𝗻𝗴𝘀 𝗜 𝗹𝗶𝗸𝗲𝗱 from the book:

1. The most essential architecture skill is how to make decisions and balance trade-ffs

2. Advice on how to do a modern tradeoff analysis:

🔹 Find what parts are entangled together.

🔹 Analyze how they are coupled to one another.

🔹 Assess tradeoffs by determining the impact of change on interdependent systems

3. The main modularity drivers are:

🔹 Speed-to-market, achieved by architectural agility, i.e., the ability to respond quickly to a change.

🔹 Scalability, where the need for more scalability support increased user activity

🔹 Fault tolerance, the ability of an application to fail and continue to operate

4. Breaking down monolith with the two methods:

🔹 Component-based decomposition (if monolith is modular): it applies different refactoring patterns for extracting components to form a distributed architecture in an incremental way

🔹 Tactical forking (if the monolith is a big ball of mud): copy the whole monolith and remove the part not needed

5. Sizing components

🔹 Calculate the total number of statements (with ;) with a given component—the ideal size of 1 to 2 standard deviations from the average component size.

Here are 𝘁𝗵𝗲 𝘁𝗵𝗶𝗻𝗴𝘀 𝗜 𝗺𝗶𝘀𝘀𝗲𝗱 in the book:

1. Although the book is abstract (as expected from architects), it doesn't go into any implementation details or technologies or mention architectural patterns.

2. The book follows Sysops SAGA's fictional story, whereas a real-life example would be more worthwhile. In this way, some things would sound artificial or forced.

3. I need to catch the data, as the book makes many assumptions. As it is not backed with any real-life project (pricing, etc.), we are still determining what metrics we would get.

4. I missed the structured approach. It started well with essential concepts, such as modularity and decomposition, and then twelve immediately into components and pulled apart data. Then, it went to service granularity and reuse patterns and data ownership and access patterns later.

#softwaredesign
