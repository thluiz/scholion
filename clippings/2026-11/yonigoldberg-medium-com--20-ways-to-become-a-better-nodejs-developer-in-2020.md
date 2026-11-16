---
url: "https://yonigoldberg.medium.com/20-ways-to-become-a-better-node-js-developer-in-2020-d6bd73fcf424"
captured_at: "2026-11-16T17:51:05+00:00"
title: "20 ways to become a better Node.js developer in 2020"
domain: "yonigoldberg-medium-com"
---

20 ways to become a better Node.js developer in 2020
Yoni Goldberg
22 min read
·
Dec 10, 2019

Don’t be that ‘screwdriver guy’, enrich your toolbox, diversify yourself
Short Intro

I’ve compiled below 20 skills, technologies and considerations on choosing between them. Picking the right tools became one of our greatest challenges — the Node.js ecosystem has matured and present attractive options in almost every field. Vanilla or TypeScript? Ava, Mocha or Jest? Express, Fastify or Koa? or maybe Nest? should I include ES6 modules in my next project or stick to good-old ‘require’? Mixing and matching among all of those require deep familiarity with the consequences. These rich set of tools and paradigms also encourages you to tiptoe into unexplored territory. I hope that the next bullets will inspire you to enrich your toolbox and diversify yourself.

My name is Yoni Goldberg, I’m an independent Node.js consultant, the co-author of Node.js best practices, and JavaScript testing best practices. I work with customers in US & Europe on planning, testing and hardening their apps.

Reviewed & improved by Bruno Scheufler

1. Use TypeScript features thoughtfully

TypeScript is exploding: the amazing chart here that shows x5 increase in TypeScript PRs remove any doubt, researches tell that it prevents errors and the community is in love. Though some voices still doubt it (check out this great and well-reasoned post by Eric Elliott) it’s clear that TypeScript has won. Now what? if you look carefully under the hype, TypeScript actually brings two mutual-exclusive offerings to the table: type-safety (including better docs and intellisense) and advanced design constructs. Many teams use TypeScript for better type safety yet unintentionally, without any proper planning, also use its fancy features —generics, abstract classes, interfaces, namespaces, etc. These teams change their design style from vanilla JavaScript to fancy OOP unintentionally due to the ‘law of the instruments’ — a cognitive bias that involves using the tooling in hand whether they are the right choice for the mission or not. In other words, if ‘abstract class’ exists in the toolbox — developers will use it. If you do favor the aforementioned coding techniques— that’s fair, go with this. Just don’t change your code and design style for the wrong reasons

Examples:

Type Inference can help in reducing TypeScript verbosity and make it look more like vanilla JavaScript
Type aliases are an alternative simple and leaner way for defining constructs (comparing with interfaces).
Using TypeScript for encapsulation? access modifiers are coming soon to vanilla JS
2. Modernize your testing toolbox. Ava & Jest are changing the game

Big things are happening in the testing field. According to the recent state of js survey, developers` satisfaction from testing tools increases more than any other domain. A revolution is happening on test runners as well as the good old veteran Mocha and Jasmine are losing the top for the new sophisticated kids in town Jest and Ava. Thanks to the modern approach they bring, it’s possible to test more, cover more ground and find more bugs. Why?

Speed — modern test runners are faster thanks to the multi-process execution model. They also apply advanced optimizations like learning tests stats over time and prioritizing slow tests to run first. This is not only about test runners, but other tools also boost test speed: fake in-memory database allow testing with DB without the involvement of IO, some npm packages offer a local and in-memory version of popular cloud services. To name a few examples.
Outstanding developer experience — modern test runners and tools are designed to accompany the coding experience and provide valuable insights. For example, should a test fail, Jest and Ava will not just report a failure rather extract the related code from the unit under test. Thanks to this, developers get much richer context which leads to a faster resolution

Some of the traditional tools were designed for CI or for occasional test execution. In times where teams deploy once a day, discovering a bug after 4 hours is not good enough. Modern tooling allows running tests, including component tests with DB, constantly even during coding. This approach allows for testing more layers and more use cases earlier and it’s called ‘shift left’ — read more about it below

Examples:

AVA & Jest are the new sophisticated kids in town
mongodb-memory server is amazing for testing with MongoDB server — it installs, instantiates and configures a local and real Mongo with in-memory engine
Cypress makes E2E testing, including backend’s API related tests, a delightful experience
aws-sdk-mock fakes many AWS services
3. Plan your ES6 modules usage strategy. See, it’s a bit tricky

The long-awaited ES6 modules were unflagged recently, so you might be tempted to use it right away. They bring great opportunities to Node land like a modern syntax for importing modules, compatibility with frontend syntax (important for package maintainer that need to support both Node and browser runtime) and asynchronous modules resolution that opens the door for top-level async-await and better tree shaking. Cool. However, there are some implications that one must be aware of before jumping on the ESM wagon: not all the supporting features are implemented yet. For example, it’s unclear yet how test doubles libraries like Sinon and Jest can ‘mock’ such modules so your wagon might break on the side of the road with smoke.

Given all of these considerations, what’s your strategy: jump straight into the ESM water and work around the issues? or use ESM with babel/TS as a safety net? maybe keep on with gold old common js ‘require’ but avoid incompatible syntax like usage of __filename, __dirname, JSON resolution, and others? there are no strict answers here but at least we strive to ask the right questions

Thanks to Gil Tayar for these great insights

Examples:

Differences Between ES Modules and CommonJS from the official Node.js docs
The ESM roadmap and features that are not implemented yet
Great post on ESM syntax and status
4. Meet the latest JavaScript features that are turning green soon

I’m not a big fan of chasing for every new language feature, sometimes these shiny toys work against the code simplicity and clarify. From time to time, however, some really valuable Javascript features are presented so it’s worthwhile watching the TC39 proposal list and node.green to identify attractive new features that fit your coding style

Examples:
Optional chaining is at stage 4 and part of Node.js 13.3 behind a flag. This one is going to catch a lot of popularity. Some love it, others don’t
Private methods and fields are at stage 3 (active proposals) so if you’re opting for TypeScript only for encapsulation — now there is one more option to choose from
Nullish coalescing (stage 4) will finally put a stop to our nasty habit of checking for nulls & undefined using the !variableName syntax (which also includes zero and therefore is error-prone)
Promise.any is the latest edition to the promise.{something} family, unlike all the others (promise.all, promise.settleAll, promise.race) it will abort should any Promise resolve or reject. This is one of the final nails in the coffin of Promises helper libraries like ‘async’ and ‘BlueBird’
5. Experiment architectures outside of your comfort zone. Note how GraphQL is disrupting the traditional models

Great techniques exist in different paradigms that you can embrace without changing your architecture. Also, most companies have a variety of different apps/microservices types like data-driven search and reporting apps, others based on heavy logic and some are just streams of data. Why apply the same treatment to these different requirements? If all you have is a screwdriver, every challenge starts looking like a screw.

Ensure you’re familiar with layered architectures like n-tiers, DDD, Hexagonal/Onion/Clean. They look very different but their primary principle is smilar — isolating the domain (i.e. core data schema and business logic) from the surrounding tech (e.g. APIs, DB). Introduce yourself also to streaming style architectures which see a great increase in popularity. Then, spend some time with data-driven architectures that are best implemented nowadays with GraphQL frameworks.

Speaking of GraphQL, it’s interesting how some of its flavors disrupt the traditional separation between API and data-access layers, instead of repeating similar code and schemas twice these frameworks allow to declaratively define the entire app with one schema. This approach will greatly boost the go-to-market for data-driven apps which are not likely to embed complex logic.

Examples:

This video by Dev Mastery about Clean Architecture is a gem. It also includes a starter example dev-mastery comments-api
node-api-boilerplate is a great starter with DDD mindset
Prisma server allows backend-less data-driven app
Apollo server is GraphQL-first framework for building apps that is centered around Graph schemas
express-graphql brings GraphQL merit without forcing to quit the comfy Express environment
6. Check out the winner of the 2019 oscar — Nest.js

After years of Express life, we need a little nest (js). With such amazing growth, you simply can’t ignore it. I would argue that Nest.js is the most remarkable thing that happened to Node.js in 2018/2019— for the first time, we have a full-fledge consensus framework like Java Spring and Python Django. Until 2018, teams without strong design skills had to architect their backends, spend a great time on plumbing and invent the wheel. Being one who engages with ~15 projects every year, believe me, I’ve seen so many types of wheels. Too many. My friend and colleague Gil Tayar funnily adapt the Anna Karenina principle to software: ‘All happy projects are alike; each unhappy project is unhappy in its own way.’

Unlike Express & co., Nest.js brings a full-fledged, batteries-included, framework (e.g. handles the data access layer, validation, etc). Its design style is highly ‘inspired’ by Angular — opinionated, TypeScript-based and embodies heavy modularization constructs. That said, it still offers great flexibility in choosing it’s sub-frameworks. Given all these goodies, I have no single doubt that teams doing their first steps with Node.js will move way faster with Nest.js rather with minimalist Express approach.

With all it’s greatness, it’s not flawless. One may doubt, is the heavy modularized Angular approach that was designed to ease the pain of huge frontend codebase suits the backend needs? aren’t we jumping too far from minimal Express to a huge and such an opinionated framework? are all of these heavy modularity features needed in a world of small Microservices? or the equivalent, isn’t it promoting monoliths (“I can easily handle 30,000 LOC in my code base”)?

At least we now have an option to choose from.

Examples:

Nest.js official docs
Quick ‘getting started’ example
Quick overview of its philosophy and features
I learned Nest.js using this course which I highly recommend (no affiliation of course)
7. Apply gradual deployment techniques like feature-flagging, canary or traffic shadowing

Have you heard about the epic Cloudflare downtime where a developer who wanted to experiment some feature in production rendered a big part of the internet down? Nothing will boost your confidence and speed than knowing that your deployment engine catches errors before your users do. A bunch of techniques will provide this magic. Each one achieves this in its own way but the overall idea is the same — serve the next version to a limited group of users and measure whether it seems stable. Going with this approach, we actually separating the deployment phase from the release phase. Some say it’s as important as testing, I suggest than anything that measures our pipeline is a TEST.

What are these techniques? Canary is the most well-known and simple. It tunes the routing so the next version is deployed and served to a group of users, starting from users are more likely to tolerate bugs (e.g. office employee, non-paying customers) and as the confidence grows it serves to more and more users. This might sound complex, but frameworks such as istio for K8S and AWS serverless handle most of the heavy lifting work. The next technique, feature flagging, is more powerful but also demands to get your hand dirty. It basically suggests wrapping a feature code with condition criteria that tell which users should benefit this new feature. Usually, it also comes with a dashboard for product managers to turn on and off features. This allows non-technical users to be part of the party and also support finer-grained advanced criteria. For example, using flags you may activate some experimental feature only for users from a specific city, on a specific machine instance that has a specific browser. One last super-interesting technique to look for is traffic shadowing which I’ll leave you to read about.

The value of these techniques is immense: unlike code-testing which demands great effort all the time, tuning your routers for canary deployment only happens once(!) and it also ‘test’ you code under realistic production environment. Learn about this fascinating world and plumb one of this technique into your pipeline

Examples:

fflip is a minimalist and free feature flagging for Node.js
Unleash is a rich feature flagging including a dashboard for product folks
it’s easy to mess your code with feature flagging, read some best practices first
Kubernetes istio greatly ease canary deployment set up
With AWS serverless setting a canary is a breeze
Intro to traffic shadowing
8. Shift your testing left — test more things and sooner

The shift left concept puts forward a sensible claim — the later a bug is discovered, the pricier it is to fix it. Consider a case where you discover a performance issue late on a staging environment, after short analysis it turns out that the fundamental DB data model must be changed — this is likely to incur significant code changes. Some researchers claim it might cost up to x640 times more when a bug is discovered too late on production. In plain words, the traditional model where a developer is focused on unit testing only and then weeks later the QA performs realistic E2E and advanced tests is slow and pricy. This well-known diagram brings this point home safely.

Test more things sooner, discover bugs early. How can we translate this idea into tangible development tasks? run a diversified set of tests as part of every commit and even during coding: component/api tests with real (in-memory?) DB just like you run unit tests, tests with realistic production input using dedicated property-based libraries, apply security scanners, run performance load tests and more. See below a list with dozens of tests one can run across the pipeline

Examples:

Fast-check npm package for property-based testing allows invoking your units/API with many input permutations
Check our framework and tools for scanning docker containers for CVEs like snyk, Trivy, Quay
Tuning your real DB for in-memory operation without IO will make it practical to run api/component tests instantly almost like unit tests: this is how you would tune PostgreSQL (here is a ready-to-use dockerized version), mongodb-memory server will install and configure a local and real Mongo with in-memory engine.
9. Shift your testing right — test in/with production

‘Testing in production’ is a mega-trend in the testing community. It’s based on an idea called ‘shift-right’, which suggests that traditional tests on development and staging environment are less realistic and probably won’t prevent enough issues. The modern production has so many moving parts and parties, so many issues are likely to occur or get discovered only in production. Consequently, many tests must be conducted on the production environment itself for monitoring purposes but also to better test the future versions (e.g. serve some small traffic to the next version). The most straightforward production test is monitoring but many other advanced techniques exist like traffic shadowing, a/b tests (as a technical measure), load testing, tap-compare, soak testing and others.

So should we shift left or right? both. A modern approach for software delivery is not just thinking about tests rather about a pipeline. Given that many phases exist until the next version is served to the user — planning, development, deployment, release — each one is another opportunity to realize issues, stop, or build accumulating confidence. Code testing is a significant step on the pipeline, but plugging other tests into the pipeline will provide more confidence.

Examples:

Masterpiece post: Testing in production the safe way
My short video on traffic shadowing test with Node.js
YouTube — Running E2E tests in production with Node.js
10. Be ready to use your new async pocket knife — worker threads

The most popular Node.js interview question might vanish soon: ‘is Node.js really single-threaded?’. As of version 11.7, we welcome a new family member in the async toolbox — worker thread. This tool, unlike any other, can address a very painful blindspot in Node. If 100% of the requests are CPU-intensive — no web framework, including Go & Java ones, can help tame this beast. However, a more popular workload is when only 1–10% of requests grabs the CPU for long time — most of the non-Node frameworks will prevent this automatically (thread per request). Node.js couldn’t — when serving 1000 req/sec, it’s enough for 1 to be CPU-intensive so all the other 999 suffer. There was no remedy to this pain, child process for examples are too slow to spin-up and can’t share memory. Good news, this is now tamable: worker threads can spin-up a dedicated event loop so the main one will remain snappy.

Now for some bad news — worker threads are not a lightweight thread that one spawn in no-time on demand. They actually duplicate the entire engine so it can become quite slow until they start running CPU-bounded requests will suffer additional delay. For this reason, consider a thread-pool (link below)

Examples:

Quick hello-world
An exhaustive intro to worker threads
The official doc is quite short and beneficial for skimming through the API
Thread pool implementation example
11. Deepen your Docker and Kubernetes understanding. It highly affects your Node.js code.

The DevOps storm means different things to different teams. For some, it is about making Dev perform also Ops work (e.g. being on-call), for others it’s more of a recommendation to plan early for production. At a minimum, it’s expected from developers to understand the production run-time as it highly affects the coding decisions and patterns. Mostly the decisions that sit on the intersection between Dev and Ops.

Few examples: it’s a well-known practice to ensure all outgoing requests are being replayed upon failures (the circuit breaker pattern), this can be done both on the infrastructure level using K8S Istio, or at the code itself using dedicated packages. Which one would you prefer and why? interesting choice, isn’t it? Let’s discuss other scenarios — K8S might kill and relocate pods, when it sends a kill signal the webserver might handle 2000 users. When a pod just crashes, they will quickly become angry 2000 users unless you implement a graceful and thoughtful shutdown. What is the grace period? well, this requires some Kubernetes learning, right? Sometimes the kill signals from K8S won’t even reach to your code if you use ‘npm start’ command, why? this requires some understanding of how Docker processes and signals are managed (the 1st link below will answer this question). One other interesting challenge is settling two contradicting things — how can test tools run within Docker containers during the pipeline but then removed before production? One last interesting example is configuring the allowed memory per container, given that v8 recently stopped limiting the heap size which will now keep growing as needed, this might interfere with K8S resource limits (common best practice) — make a decision and align the Node.js side with the K8S side

all of these challenges call you to dig deeper into the fascinating world of Docker clusters (or Serverless if you wish)

Examples:

A masterpiece video by Bret Fisher on Node.js Docker best practices. Don’t miss this one!
istio circuit breaker vs npm code-level circuit breaker
Nice article on managing Node.js memory in a containerized environment by Ravali Yatham
12. Security: Learn to think like an attacker by skimming through vulnerable code examples

If you can’t think like an attacker, you can’t think like a defender. In 2020, you shouldn’t outsource the defense work to third-party companies or rely solely on static security scanners: The amount of attack types is overwhelming (The development pipeline and NPM are the latest trends). Developers training is the key — bake security DNA into yourself and your team and add a security touch to everything. A useful way to deepen your security understanding is to go through examples of vulnerable code and attack vectors. See below few example links that might greatly help

Examples:

NodeGoat is a project that intentionally embodies security weaknesses for educational purposes. Don’t miss this doc page with attack examples
Read my list of Node.js Security best practices which contain 23+ attack ideas including JavaScript code examples
Conduct a monthly threats analysis meeting where the team tries to look at the application design and propose attacks. sound boring? not necessarily if you add some gamification and reward members that find an exploit, or run a competition between a blue team that designs a module vs the read team which tries to find exploits
13. Learn at least one: ELK or Prometheus

Monitoring is a crucial set up that should be well hardened and demands cooperation between Ops and Dev. No monitoring solution can be perfect without developers' involvement. These two popular monitoring systems, ELK and Prometheus, sound like sys admin toys but in fact, developers can learn a lot by configuring them. In any case, the mandatory activity for developers is being involved in exposing the metrics.

Ops folks know nothing about the event loop and how to monitor it (npm package does this), only you can propose and implement this important metric. Only developers can suggest the right V8 monitoring limits alerts. Developers might even write automated tests to ensure that when application errors are thrown — the right metrics are incremented. One another valuable activity is custom applicative metrics — coding some measurement of user activities can be very efficient in tracking production anomalies. Consider an e-commerce app, if the number of purchases is tracked and it suddenly drops dramatically in production — this is likely to imply some underlying issue

Examples:

A post about first steps with Prometheus and Node.js
Prometheus client library for Node.js — a great resource to learn about the metrics that are exposed by default
A post about first steps with Node.js & ELK
A comprehensive overview of ELK
Read about the 4 monitoring ‘Golden signals’
Read Google Site Reliability Engineering book, or at least the chapter on monitoring
14. Use machine learning as a black-box product

This bullet is targeted for machine learning (ML) newbies who work for products that don’t rely heavily on ML. If you aren’t one of those — feel free to step forward to the next bullet. So you’re like me clueless about ML, that’s fair, we intentionally chose not to build expertise on this field. Still, we can do much better if we just understand common ML needs and solutions so we consume those once a need arise. The JavaScript ML world has matured to a point where there are many stable libraries that can produce great value without intimate knowledge of the implementation. If we just understand WHAT they’re doing (+ how to configure )— we gain a special hammer to our toolbox. When this might prove to be valuable? say you sit in a meeting and the product manager mention something about organizing data (e.g. customers) into groups — suggest using cluster algorithms. Feeding the data into an adequate library might be enough to extract great insights. Often you’ll need to gain more knowledge to configure it correctly — that’s fair, hire an expert, become an expert, at least you knew where to start and structured the solution path. Does someone now ask about recommending things to the user? classify things? Find similarities between texts? predict? analyze audio or image? there is a lib for each one of those — pull out your weapon at the right moment

Obviously, better delve into the details and read the manuals. In no way, I’m suggesting a careless use of technologies. What I do propose however is that becoming familiar with the high-levels is better than knowing nothing and can build the motivation to keep exploring. Should I used ML taxonomy wrong above — please understand, I’ve just started my ML journey

Examples:

ml.js — a swiss army knife of machine learning tools
Brain.js specializes in neural networks, has great docs and a free video course
Natural brings the world of NLP into Node land: text comparison and similarities, sentiment analysis, text classification and more
15. Sleep >7 hours a night. This matters far more than any technology you use and scientifically prooved to make you a better developer

This comes from Hillel Wayne and it’s one of the best tweets I’ve encountered in the last year :

your sleep quality and stress level matter far, far more than the languages you use or the practices you follow. Nothing else comes close: not type systems, not TDD, not formal methods, not ANYTHING.

It’s packed with examples and researches — I urge you to visit there and dig into those pearls of wisdom

Examples:

Many software paradigms are not proven to be useful — TDD research here, clean architecture link. Other examples can be found within the Tweet
Research: No clear evidence that a chosen programming language makes a different
Research: Chronically getting less than 7 hours of sleep causes dramatic degradation on all mental tests
16. Quit Express, it’s aged and not maintained properly. Fastify and Koa are great candidates in 2020

Did you remember to wrap all your Express routes with try-catch, then move to the next() method and finally return some appropriate status to the user? If no, your process will crash without a trace. If yes, you just spent a great time on plumbing straight-forward pieces that add no value to your business. Isn’t this what frameworks are here for? Though Fastify & Koa won’t handle all the error paths for you (e.g. uncaught exceptions) they address this with a modern approach that requires less effort. They both also natively support async routes. Those are just a few examples where a modern and maintained framework could do better for you.

The last commit to the Express project was pushed somewhere 6 months ago… Since then Fastify & Koa saw dozens of builds and they keep improving. It’s frankly not appropriate for the Node.js ecosystem to rely heavily on a library that doesn’t keep in step with the times.

That said, most of the community tools and docs rely on Express. I hope to see community leaders, course makers, bloggers creating more content on its modern alternatives.

Examples:

Fastify
Koa
17. Revisit these bullets from last year — some are still highly relevant

I’ve published a similar post in 2019 and many of the bullets seem important also in 2020. Here are some specific recommendations:

Examples:

Bullet number #4 — “Plan how to utilize Async-Hooks to reach better tracing and context”
Bullet number #11 — “Have a package update strategy. A lesson learned in 2018: updating too soon is a dangerous practice”
Bullet number #17 — “Deepen your Linux OS understanding, focus on the anatomy of a Linux process”
Bullet number #18 — “Dive deeper into the Node.js internals”
18. Enrich your CI with automated quality tools

Our journey for quality and safe deploys is usually centered around testing. The caveat of code-based testing (E.g. unit tests) is their price — every new functionality demands writing more testing code. This usually pays off but still painful. Some tools like linters, scanners, and static analyzers offer a different deal — for a one-time setup they will discover bugs forever. This is a great opportunity for lowering the price of building confidence, almost a free lunch. The list of tools is growing every year so keep following and enrich your CI — below I’ve included a few examples of modern tools.

Examples:

Scan Docker containers for CVEs using tools like snyk, Trivy, Quay
lockfile-lint will detect attempts to inject malicious dependencies using the npm lock file (e.g. edit a dependency URL within the lockfile)
swagger-express-validator will ensure that your routes conform to the swagger schema
eslint-plugin-import is an outstanding linter that performs dozens of checks on module and dependencies resolution. For example, it can warn when import/require is not at the beginning, disallow mutable exports with var or let, discoverextraneous packages that aren't declared with package.json and much more
commitlint will enforce semantic commits which then can lead to automatic semantic versioning of Microservice and packages
dependency-cruiser is a CLI tool that allows declaring flexible policies on allowed and disallowed dependencies. Using this you can craft custom rules like what licenses are allowed, allowed paths and more
19. Enrich your mindset, diversify your toolbox

We often surround ourselves with favorite technologies and ignore alternatives based on prejudice. Here are some typical sentences I hear in my network: ‘Functional programming is not practical’, ‘REST API is dead, ‘TDD is not for me’, ‘ORMs are evil’, ‘TypeScript is too verbose’.

These are false-dichotomies — it’s not a binary question, all these paradigms embody many different ideas, and still, we tend to pick all or ignore all. For example, Functional Programming currying and monads feel weird? that’s fair, consider other more mainstream FP ideas like pure functions. Ignoring TypeScript because OOP is not your style? maybe use only its type system and stick to vanilla JS objects and functions. Cherry-pick ideas and features, not a package.

How exactly do I plan to diversify my stack in 2020? I’ll probably use Fastify for the web layer, with a mix of REST and GraphQL. The data access layer will constitute some lightweight ‘ORM’ but only for migrations and connection pooling (no dichotomy, I’m picking the right ORM features for me). As for the DB, I plan to use a relational DB mixed with JSON columns. My coding style is based on simple and flat vanilla JavaScript objects — but I usually mix it with some classes when appropriate and keep most of my functions pure. The overall architecture style will be centered around Microservices but maybe in a monorepo — I’m not obliged to pick all the Microservice bells and whistles, right?. As of testing, I definitely want to run TDD-style iterations of refactoring for my code, but not necessarily code the tests first — I pick the TDD features that suit my style. What type of testing? mostly component tests (i.e. api) but mix this with unit testing to cover parts with heavy logic.

By no mean, I suggest that this is the best stack. It is, however, a diversified stack that mixes and matches multiple ideas from many paradigms. Obviously assemble your own stack, just don’t be afraid of tiptoeing into unexplored territory and get inspiration from many sources of wisdom.

p.s. I’m not advocating for becoming a jack of too many trades. Actually mastering some technologies is important. My point is being pragmatic and open to great ideas. Don’t be “that screwdriver guy”, enrich your mindset, diversify your toolbox

20. Get inspiration from these great 5 starter projects

Starter (boilerplate) projects are a genuine source for knowledge — just skim through the code for 10–20 min and get many ideas to embrace. I’ve packed here below some quality starters, each brings some unique approach so you enrich your mindset with new paradigms

Examples:

node-api-boilerplate is a great showcase for DDD with an application layer that demonstrates organizing code by feature
dev-mastery comments-api is an excellent translation of clean architecture to Node.js and it comes with this super explainer video
Typescript-starter won’t teach you any architecture concepts but a nice showcase for TypeScript set up with modern libraries and great docs
nodejs-api-starter is the starter for those who seek a real-world GraphQL implementation including errors and auth
bulletproof-nodejs is a well-known starter that uses the 3-tier folder structure which is my personal and recommended way of structuring a Node.js app

Thank You.
