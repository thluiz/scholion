---
url: "http://www.infoworld.com/article/2883328/java/java-vs-nodejs-an-epic-battle-for-developer-mindshare.html"
captured_at: "2015-02-19T14:27:42-03:00"
title: "Java vs. Node.js: An epic battle for developer mind share"
domain: "infoworld-com"
---

# Java vs. Node.js: An epic battle for developer mind share

In the history of computing, 1995 was a crazy time. First Java appeared, then close on its heels came JavaScript. The names made them seem like conjoined twins newly detached, but they couldn't be more different. One of them compiled and statically typed; the other interpreted and dynamically typed. That's only the beginning of the technical differences between these two wildly distinct languages that have since shifted onto a collision course of sorts, thanks to Node.js.

If you’re old enough to have been around back then, you might remember Java’s early, epic peak. It left the labs, and its hype meter pinned. Everyone saw it as a revolution that would stop at nothing less than a total takeover of computing. That prediction ended up being [only partially correct](http://www.infoworld.com/article/2612433/java/java-forever--12-keys-to-java-s-enduring-dominance.html). Today, Java dominates Android phones, enterprise computing, and some embedded worlds like Blu-ray disks.

**[ Streamline your development of fast websites, rich APIs, and real-time apps with these [13 fabulous frameworks for Node.js](http://www.infoworld.com/article/2606426/application-development/153472-13-fabulous-frameworks-for-Node.js.html). | Keep up with hot topics in app dev with InfoWorld's [Strategic Developer](http://www.infoworld.com/blog/strategic-developer/) blog and [Application Development newsletter](http://www.infoworld.com/newsletters/signup.html). ]**

For all its success, though, Java never established much traction on the desktop or in the browser. People touted the power of applets and Java-based tools, but gunk always glitched up these combinations. Servers became Java’s sweet spot.

Meanwhile, what programmers initially mistook as the dumb twin has come into its own. Sure, JavaScript tagged along for a few years as HTML and the Web pulled a Borg on the world. But that changed with AJAX. Suddenly, the dumb twin had power.

Then Node.js was spawned, turning developers’ heads with its speed. Not only was JavaScript faster on the server than anyone had expected, but it was often faster than Java and other options. Its steady diet of small, quick, endless requests for data have since made Node.js more common, as Web pages have grown more dynamic.

While it may have been unthinkable 20 years ago, the quasi-twins are now locked in a battle for control of the programming world. On one side are the deep foundations of solid engineering and architecture. On the other side are simplicity and ubiquity. Will the old-school compiler-driven world of Java hold its ground, or will the speed and flexibility of Node.js help JavaScript continue to gobble up everything in its path?

### Where Java wins: Rock-solid foundation

I can hear the developers laughing. Some may even be dying of heart failure. Yes, Java has glitches and bugs, but relatively speaking, it's the Rock of Gibraltar. The same faith in Node.js is many years off. In fact, it may be decades before the JavaScript crew writes nearly as many regression tests as Sun/Oracle developed to test the Java Virtual Machine. When you boot up a JVM, you get 20 years of experience from a solid curator determined to dominate the enterprise server. When you start up JavaScript, you get the work of an often cantankerous coalition that sometimes wants to collaborate and sometimes wants to use the JavaScript standard to launch passive-aggressive attacks.

### Where Node wins: Ubiquity

Thanks to Node.js, JavaScript finds a home on the server and in the browser. Code you write for one will more than likely run the same way on both. Nothing is guaranteed in life, but this is as close as it gets in the computer business. It's much easier to stick with JavaScript for both sides of the client/server divide than it is to write something once in Java and again in JavaScript, which you would likely need to do if you decided to move business logic you wrote in Java for the server to the browser. Or maybe the boss will insist that the logic you built for the browser be moved to the server. In either direction, Node.js and JavaScript make it much easier to migrate code.

### Where Java wins: Better IDEs

Java developers have Eclipse, NetBeans, or IntelliJ, three top-notch tools that are well-integrated with debuggers, decompilers, and servers. Each has years of development, dedicated users, and solid ecosystems filled with plug-ins.

Meanwhile, most Node.js developers type words into the command line and code into their favorite text editor. Some use Eclipse or Visual Studio, both of which support Node.js. Of course, the surge of interest in Node.js means new tools are arriving, some of which, like [IBM’s Node-RED](http://nodered.org/) offer intriguing approaches, but they're still a long way from being as complete as Eclipse. WebStorm, for instance, is a solid commercial tool from JetBrains, linking in many command-line build tools.

Of course, if you're looking for an IDE that edits and juggles tools, the new tools that support Node.js are good enough. But if you ask your IDE to let you edit while you operate on the running source code like a heart surgeon slices open a chest, well, Java tools are much more powerful. It's all there, and it's all local.

### Where Node wins: Build process simplified by using same language

Complicated build tools like Ant and Maven have revolutionized Java programming. But there's only one issue. You write the specification in XML, a data format that wasn't designed to support programming logic. Sure, it's relatively easy to express branching with nested tags, but there's still something annoying about switching gears from Java to XML merely to build something.

### Where Java wins: Remote debugging

Java boasts incredible tools for monitoring clusters of machines. There are deep hooks into the JVM and elaborate profiling tools to help identify bottlenecks and failures. The Java enterprise stack runs some of the most sophisticated servers on the planet, and the companies that use those servers have demanded the very best in telemetry. All of these monitoring and debugging tools are quite mature and ready for you to deploy.

### Where Node wins: Database queries

Queries for some of the newer databases, like CouchDB, are written in JavaScript. Mixing Node.js and CouchDB requires no gear-shifting, let alone any need to remember syntax differences.

Meanwhile, many Java developers use SQL. Even when they use the Java DB (formerly Derby), a database written in Java for Java developers, they write their queries in SQL. You would think they would simply call Java methods, but you’d be wrong. You have to write your database code in SQL, then let Derby parse the SQL. It's a nice language, but it's completely different and many development teams need different people to write SQL and Java.

### Where Java wins: Libraries

There is a huge collection of libraries available in Java, and they offer some of the most serious work around. Text indexing tools like Lucene and computer vision toolkits like OpenCV are two examples of great open source projects that are ready to be the foundation of a serious project. There are plenty of libraries written in JavaScript and some of them are amazing, but the depth and quality of the Java code base is superior.

### Where Node wins: JSON

When databases spit out answers, Java goes to elaborate lengths to turn the results into Java objects. Developers will argue for hours about POJO mappings, Hibernate, and other tools. Configuring them can take hours or even days. Eventually, the Java code gets Java objects after all of the conversion.

Many Web services and databases return data in JSON, a natural part of JavaScript. The format is now so common and useful that many Java developers use the JSON formats, so a number of good JSON parsers are available as Java libraries as well. But JSON is part of the foundation of JavaScript. You don't need libraries. It's all there and ready to go.

### Where Java wins: Solid engineering

It's a bit hard to quantify, but many of the complex packages for serious scientific work are written in Java because Java has strong mathematical foundations. Sun spent a long time sweating the details of the utility classes and it shows. There are BigIntegers, elaborate IO routines, and complex Date code with implementations of both Gregorian and Julian calendars.

JavaScript is fine for simple tasks, but there’s plenty of confusion in the guts. One easy way to see this is in JavaScript’s three different results for functions that don't have answers: `undefined`, `NaN`, and `null`. Which is right? Well, each has its role -- one of which is to drive programmers nuts trying to keep them straight. Issues about the weirder corners of the language rarely cause problems for simple form work, but they don't feel like a good foundation for complex mathematical and type work.

### Where Node wins: Speed

People love to praise the speed of Node.js. The data comes in and the answers come out like lightning. Node.js doesn't mess around with setting up separate threads with all of the locking headaches. There's no overhead to slow down anything. You write simple code and Node.js takes the right step as quickly as possible.

This praise comes with a caveat. Your Node.js code better be simple and it better work correctly. If it deadlocks, the entire server could lock up. Operating system developers have pulled their hair out creating safety nets that can withstand programming mistakes, but Node.js throws away these nets.

### Where Java wins: Threads

Fast code is great, but it's usually more important that it be correct. Here is where Java’s extra features make sense.

Java's Web servers are multithreaded. Creating multiple threads may take time and memory, but it pays off. If one thread deadlocks, the others continue. If one thread requires longer computation, the other threads aren’t starved for attention (usually).

If one Node.js request runs too slowly, everything slows down. There's only one thread in Node.js, and it will get to your event when it's good and ready. It may look superfast, but underneath it uses the same architecture as a one-window post office in the week before Christmas.

There have been decades of work devoted to building smart operating systems that can juggle many different processes at the same time. Why go back in time to the ’60s when computers could handle only one thread?

### Where Node wins: Momentum

Yes, all of our grandparents' lessons about thrift are true. Waste not; want not. It can be painful to watch Silicon Valley’s foolish devotion to the “new” and “disruptive,” but sometimes cleaning out the cruft makes the most sense. Yes, Java can keep up, but there's old code everywhere. Sure, Java has new IO routines, but it also has old IO routines. Plenty of `applet` and `util` classes can get in the way.

### Where both win: Cross-compiling from one to the other

The debate whether to use Java or Node.js on your servers can and will go on for years. As opposed to most debates, however, we can have it both ways. Java can be cross-compiled into JavaScript. Google does this frequently with Google Web Toolkit, and some of its most popular websites have Java code running in them -- Java that was translated into JavaScript.

There's a path in the other direction, too. JavaScript engines like [Rhino](https://developer.mozilla.org/en-US/docs/Mozilla/Projects/Rhino) run JavaScript inside your Java application where you can link to it. If you're really ambitious, you can [link](http://rbackhouse.blogspot.com/2011/03/using-google-v8-javascript-engine-in.html) in [Google’s V8 engine](https://code.google.com/p/v8/).

Voilà. All of the code can link to each other harmoniously and you don't need to choose.

### Related articles
