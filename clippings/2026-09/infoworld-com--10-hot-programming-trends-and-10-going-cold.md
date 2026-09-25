---
url: "https://www.infoworld.com/article/2259240/10-hot-programming-trends-and-10-going-cold.html?ref=dailydev"
captured_at: "2026-09-25T22:35:34+01:00"
title: "10 hot programming trends — and 10 going cold"
domain: "infoworld-com"
---

![Peter Wayner](https://www.infoworld.com/wp-content/uploads/2026/09/2405-0-08029400-1789981324-peterwayner_crop-100796877-orig.jpg?quality=50&strip=all&w=150)

Contributing Writer

feature

Dec 30, 202412 mins

Tides ebb and flow. Pendulums swing. Ideas come and go, especially in programming, where the technologies and techniques for creating software continuously evolve.

Some programming languages, libraries, platforms, and tools become hot and irresistible. When they’re mentioned, everyone at the planning meeting jumps on the table and cheers. Others lose steam or fall from favor, drawing sighs or blank looks. Everyone stares at their shoes. Maybe they were impossibly hot just last week, but that was then and this is now.

In the interest of advancing the art, here is a list of trends we’ve noticed. They’re arranged in pairs because often the rise of one approach goes hand in hand with the fall of another. As a wise philosopher once wrote, “For every thing that is given, something is taken.” For every yin, there’s a yang.

This list is far from absolute. Just because all of the world is in love with one technique doesn’t mean that the opposite’s day is over. Nor does it mean that all of us must flock to one side of the boat and capsize it. Just because an idea is out of fashion doesn’t mean that it has lost all value.

And just because a notion is celebrated doesn’t mean that we should rip apart our code base or shred our technology stack just to conform to some trend. As Polonius counseled in Hamlet, “This above all: to thine own self be true.”

Keep all of this in mind as you contemplate these 10 programming trends that are on the rise and 10 that are on the wane.

## Hot: Repatriation  
Not: Cloud bills

The cloud once seemed like a perfect solution for too many headaches. Someone else would manage the racks, the air conditioning, the network, and everything else. All we had to do was type in a credit card number and they would send us a bill for the machines that were priced in pennies. You can’t even buy penny candy anymore but the cloud companies still believe in using the digits to the right of the decimal point.

Alas, the CFO soon discovered that those pennies add up. Quickly. And as cloud bills soared, companies began looking for ways to bring them back under control.

The process now has a buzzword, “[repatriation](https://www.infoworld.com/article/3628746/cost-conscious-repatriation-strategies.html),” and many teams are filling out spreadsheets and thinking about it seriously. It makes the most sense for workloads that are stable and consistent. The jobs that spike or run intermittently may be best left in a cloud that will let you spin up machines for intermittent periods.

Companies that move some or all of their workloads back to servers that are on premises are saving huge amounts of money. Of course, they now have all of the headaches too — but at least the cloud bills are under control.

## Hot: AI partners  
Not: Human pair programming

It’s hard to miss all of the AI-driven tools that are now available to programmers. [GitHub Copilot](https://www.infoworld.com/article/3609013/github-copilot-everything-you-need-to-know.html), JetBrains’ AI Assistant, and IntelliCode are just some of the most prominent. And those are the specialized models. I also get very smart answers from general-purpose [large language models](https://www.infoworld.com/article/3709489/large-language-models-the-foundations-of-generative-ai.html) like [Google Gemini](https://www.infoworld.com/article/3625953/gemini-code-assist-tools-target-developer-productivity-from-within-ides.html) or [ChatGPT](https://www.infoworld.com/article/3543614/chatgpt-o1-preview-excels-at-code-generation.html). Innovation continues and we don’t know just how far these language models will go.

There are limitations. For every 100 right answers that an LLM has given me, I’ve gotten probably 30 or 40 that were wrong in some minor and sometimes major way. The worst were the ones that hallucinated an API call that didn’t exist and will never exist because of some architectural limitation. I spent a few hours poring through the regular documentation wondering if it was a spelling error.

Pair programming with two humans seems to be fading for reasons aside from the rise of AIs. Maybe it’s the pain of synchronizing two schedules. Perhaps it’s the rise of remote working. It might just be that it’s too much socialization for the typical introverted programmer.

But can the AI notice your totally radical and slyly subversive t-shirt just like a human pair programmer? Can the AI hit the ball in the company softball game? The unique charms of a human coding buddy may not matter if the AI supports asynchronous workflow and WFH culture.

## Hot: Rust  
Not: C/C++

For the longest time, programmers turned to the [C language](https://www.infoworld.com/article/3402023/why-the-c-programming-language-still-rules.html) or its cousin [C++](https://www.infoworld.com/article/3688923/c-23-language-standard-declared-feature-complete.html) for the fastest software. These languages are still the model of transparency and efficiency. The compiler turns each keystroke into concise machine code that runs like the wind. 

Alas, making it easy for humans to write fast code also makes it easy for humans to make mistakes. Sometimes that blazingly fast code will include a glitch or a bug that will crash your machine. Even the best C or C++ programmers can create software with deeply rooted bugs that are difficult to pinpoint, much less fix. This may be why the [coding geniuses at the White House](https://www.infoworld.com/article/2336216/white-house-urges-developers-to-dump-c-and-c.html) got President Biden to explicitly warn the country against using C or C++. 

The White House offered a suggestion: embracing memory safe languages like [Rust](https://www.infoworld.com/article/3218074/what-is-rust-safe-fast-and-easy-software-development.html). The creators of Rust took a careful look at what could go wrong when programmers wrote thread-juggling, concurrent code. They developed data models that prevent some of the worst kinds of pernicious bugs as threads compete for control of different corners of complex data structures. Then they baked them into Rust so that programmers who followed the memory-safe model could avoid some of the worst and most dangerous hidden failure modes. 

So now Rust is hot. Programmers are seeing other Rust developers produce faster concurrent code that is safer and more stable. So they’re putting in the extra time to learn the best ways to use the concepts of memory-safe borrowing to create the software that can juggle bazillions of bytes among dozens of threads. They’re producing better code and that’s ultimately what drives popularity.

## Hot: Wasm  
Not: Interpreters

Humans write high-level code and compilers turn it into the basic instructions that are executed by the CPU. But just when should this compilation take place?

For the last few decades, the idea of shipping the human-readable code to the user’s machine has gained favor. As browsers became more capable, programmers spent more and more time crafting [JavaScript](https://www.infoworld.com/article/3441178/what-is-javascript-the-full-stack-programming-language.html) that could be deployed directly to the user’s computer. Once it was just for testing some form submissions. Today, people write entire productivity suites and ship the source code.

In the last few years, a new and simple language called [WebAssembly](https://www.infoworld.com/article/3291780/what-is-webassembly-the-next-generation-web-platform-explained.html), or Wasm for short, has been drawing attention. Now developers hit the compile button and pop out a bunch of code that’s much smaller and faster. The Wasm is also much closer to the CPU’s instruction set, so it can be prepared for execution in less time. There’s no need for complex optimizations and just-in-time [compiler](https://www.infoworld.com/article/3685673/what-is-a-compiler-how-source-code-becomes-machine-code.html) tricks.

Developers are also enjoying the fact that they can easily compile other languages (C++, [Cobol](https://www.infoworld.com/article/3539057/what-is-cobol-cobol-programming-explained.html), [Python](https://www.infoworld.com/article/3204016/what-is-python-powerful-intuitive-programming.html), Rust, etc.) to Wasm, allowing them to use something other than JavaScript to create software that runs in a browser. Server-side teams also are embracing Wasm for [microservices](https://www.infoworld.com/article/3445043/what-are-microservices-your-next-software-architecture.html) and even some macro services. It’s becoming an easy way to distribute complex and feature-rich code.

## Hot: CPUs  
Not: GPUs

It’s not that the GPUs are out of fashion — it’s that they’re so expensive. As Yogi Berra once said about a popular New York restaurant, “It’s so crowded nobody goes there anymore.” So people are benchmarking their workloads and penciling out the costs. If the GPU is 20 times faster, but 30 times more expensive, it makes sense to stick with regular old processors. Many of the latest Arm chips are designed to make some of the [machine learning](https://www.infoworld.com/article/3214424/what-is-machine-learning-intelligence-derived-from-data.html) run as fast as possible. It’s not a scientific decision but an economic one.

## Hot: Zero-knowledge proofs  
Not: Digital signatures

People aren’t abandoning the assurance that comes from digital signatures — they’re recognizing that zero-knowledge proofs can offer more privacy and more complex semantics. Digital signatures are an all-or-nothing proposition that just asserts that some bag of bits is unchanged. Zero-knowledge proofs can reassure others about complex data relationships, all without revealing the data itself. Yes, they’re mathematically and computationally more complex, but they can still save on computation time and space down the road. Several of the newest [blockchains](https://www.infoworld.com/article/2334641/a-quick-guide-to-blockchain.html) like Arbitrum or Polygon are leveraging this power to bring down transaction costs.

## Hot: Trustworthy ledgers  
Not: Turing-complete ledgers

It’s dangerous to read too much into the complex and chaotic world of cryptocurrencies, but for the last several years [Bitcoin](https://www.infoworld.com/article/2184127/bitcoin-for-beginners-part-2-bitcoin-as-a-technology-and-network.html) has grown in value faster than [Ethereum](https://www.infoworld.com/article/2336054/intro-to-ethereum-smart-contracts.html). The first is a relatively simple system that largely tracks the ownership of coins. It’s possible to do more than just transfer coins with the Bitcoin protocol and some talk about adding back more opcodes to Script, the language used to encode transactions, but the few extra features are hardly ever used. Most of the energy goes into maintaining a stable ledger.

Ethereum is more complex. The digital contracts tracked by the Ethereum blockchain can be Turing-complete, an amazing feat of engineering. Programmers can take all of their algorithms and run them in the Ethereum sandbox, which carefully meters the computation and defends against bugs like endless loops.

While dreamers talk about constructing elaborate software empires on the various chains running the Ethereum protocol, the developers in the trenches are trying to minimize how much they do “on chain.” When every transaction costs Eth and the costs of cryptocurrencies drift up, it becomes more pragmatic to move more of the workload “off chain,” where it runs on a regular, old computer running a regular, old operating system.

There are workarounds. There are now dozens of chains running Ethereum or Ethereum-like protocols and their gas costs can be much lower. But many programmers still find that they don’t need much more than a trustworthy ledger for many tasks. The relative costs of the two systems are a rough indicator of general demand. While this is always clouded by the hype and foolish dreams, it still can be a gauge for just what the people need from the systems.

## Hot: GraphQL  
Not: REST

It’s not as if [REST](https://www.infoworld.com/article/3706031/what-is-rest-the-de-facto-web-architecture-standard.html) is dead. It’s just that we want to do more with the [API](https://www.infoworld.com/article/3269878/what-is-an-api-application-programming-interfaces-explained.html), and [GraphQL](https://www.infoworld.com/article/3269074/what-is-graphql-better-apis-by-design.html) is a way to do it. GraphQL returns the data in [JSON](https://www.infoworld.com/article/3222851/what-is-json-a-better-format-for-data-exchange.html), just like REST. GraphQL starts off with an HTTP POST, just like many REST calls. It’s just that the GraphQL syntax allows you to specify very complex queries with only a few keystrokes. This makes it simpler for programmers to ask for just what they want, and it reduces the amount of server-side work that must be done when someone wants a slightly different API.

## Hot: Static site generators  
Not: Single-page apps

Remember when URLs pointed to web pages filled with static text and images? Then the single-page web apps came along and replaced them all with some clever JavaScript that would fetch the content dynamically, without refreshing the entire page. Guess what? The pendulum is swinging back and all of the cool kids are building [static site generators](https://www.infoworld.com/article/2259201/what-is-a-static-site-generator-static-website-tools-explained.html). There are dozens of them. It’s like a hybrid. You put all of the data in one pile and then you write some code that sticks the data into some templates. You end up with one HTML file for each static URL, which corresponds to each row in your table of data.

The kids think these static sites are superfast and they are. Just don’t tell them that the old dynamic systems like WordPress and Drupal worked much the same way, by keeping caches filled with static pages generated with the latest data.

## Hot: Database configuration  
Not: Software programming

Long ago, programmers used to joke that they didn’t know what programming would look like in the next century, but they knew it would be called [Fortran](https://www.infoworld.com/article/2337114/fortran-popularity-rises-with-numerical-and-scientific-computing.html). This joke was so funny they would fall out of their orange Naugahyde chairs and break their slide rules. Then they would go back to configuring a database.

We’re still building databases today but what we think of as a “database” is now many times more sophisticated and powerful. The off-the-shelf databases will synchronize themselves across continents while offering a flexible tradeoff between consistency and speed. Much of the [serverless](https://www.infoworld.com/article/3406501/what-is-serverless-serverless-computing-explained.html) revolution is based on the realization that many of the cloud data stores are now so powerful that we only need to write a few if-then-else clauses to build a pretty cool web app.

![Peter Wayner](https://www.infoworld.com/wp-content/uploads/2026/09/2405-0-08029400-1789981324-peterwayner_crop-100796877-orig.jpg?quality=50&strip=all&w=250)

Contributing Writer

Peter Wayner is a contributing writer to InfoWorld. He has written extensively about programming languages (including Java, JavaScript, SQL, WebAssembly, and experimental languages), databases (SQL and NoSQL), cloud computing, cloud-native computing, artificial intelligence, open-source software, prompt engineering, programming habits (both good and bad), and countless other topics of keen interest to software developers. Peter also has written for mainstream publications including The New York Times and Wired, and he is the author of more than 20 books, mainly on technology. His work on mimic functions, a camouflaging technique for encoding data so that it takes on the statistical characteristics of other information (an example of steganography), was the basis of his book, Disappearing Cryptography. Peter’s book Free for All covered the cultural, legal, political, and technical roots of the open-source movement. His book Translucent Databases offered practical techniques for scrambling data so that it is inscrutable but still available to make important decisions. This included some of the first homomorphic encryption. In his book Digital Cash, Peter illustrates how techniques like a blockchain can be used establish an efficient digital economy. And in Policing Online Games, Peter lays out the philosophical and mathematical foundations for building a strong, safe, and cheater-free virtual world.

## More from this author
