---
url: "http://www.infoworld.com/article/2891806/application-development/7-timeless-lessons-of-programming-graybeards.html"
captured_at: "2015-03-10T11:46:10-03:00"
title: "7 timeless lessons of programming ‘graybeards’"
domain: "infoworld-com"
---

# 7 timeless lessons of programming ‘graybeards’

In one episode 1.06 of the HBO series "Silicon Valley," Richard, the founder of a startup, gets into a bind and turns for help to a boy who looks 13 or 14.

The boy genius takes one look at Richard and says, “I thought you’d be younger. What are you, 25?”

“26,” Richard replies.

“Yikes.”

**[ Find out how to handle the real-world problems faced by developers, with InfoWorld's [professional programmer's business survival guide](http://www.infoworld.com/resources/60833/it-jobs/professional-programmers-business-survival-guide#tk.ifw-infsb). | Keep up with hot topics in app dev with InfoWorld's [Application Development newsletter](http://www.infoworld.com/newsletters/signup.html#tk.ifw-infsb). | Have a tech story to share? If we publish it in the [Off the Record blog](http://www.infoworld.com/author/Anonymous/), we'll send you a $50 American Express gift cheque -- and keep you Anonymous. Send it to [offtherecord@infoworld.com](http://www.infoworld.com/article/2891806/application-development/7-timeless-lessons-of-programming-graybeards.htmlmailto:offtherecord@infoworld.com). ]**

The software industry venerates the young. If you have a family, you're too old to code. If you're pushing 30 or even 25, you're already over the hill.

Alas, the whippersnappers aren't always the best solution. While their brains are full of details about the latest, trendiest architectures, frameworks, and stacks, they lack fundamental experience with how software really works and doesn't. These experiences come only after many lost weeks of frustration borne of weird and inexplicable bugs.

Like the viewers of “Silicon Valley,” who by the end of episode 1.06 get the satisfaction of watching the boy genius crash and burn, many of us programming graybeards enjoy a wee bit of schadenfraude when those who have ignored us for being “past our prime” end up with a flaming pile of code simply because they didn’t listen to their programming elders.

In the spirit of sharing or to simply wag a wise finger at the young folks once again, here are several lessons that can't be learned by jumping on the latest hype train for a few weeks. They are known only to geezers who need two hexadecimal digits to write their age.

### Memory matters

It wasn't so long ago that computer RAM was measured in megabytes not gigabytes. When I built my first computer (a Sol-20), it was measured in kilobytes. There were about 64 RAM chips on that board and each had about 18 pins. I don't recall the exact number, but I remember soldering every last one of them myself. When I messed up, I had to resolder until the memory test passed.

When you jump through hoops like that for RAM, you learn to treat it like gold. Kids today allocate RAM left and right. They leave pointers dangling and don't clean up their data structures because memory seems cheap. They know they click on a button and the hypervisor adds another 16GB to the cloud instance. Why should anyone programming today care about RAM when Amazon will rent you an instance with 244GB?

But there's always a limit to what the garbage collector will do, exactly as there's a limit to how many times a parent will clean up your room. You can allocate a big heap, but eventually you need to clean up the memory. If you're wasteful and run through RAM like tissues in flu season, the garbage collector could seize up grinding through that 244GB.

Then there's the danger of virtual memory. Your software will run 100 to 1,000 times slower if the computer runs out of RAM and starts swapping out to disk. Virtual memory is great in theory, but slower than sludge in practice. Programmers today need to recognize that RAM is still precious. If they don't, the software that runs quickly during development will slow to a crawl when the crowds show up. Your work simply won't scale. These days, everything is about being able to scale. Manage your memory before your software or service falls apart.

### Computer networks are slow

The marketing folks selling the cloud like to pretend the cloud is a kind of computing heaven where angels move data with a blink. If you want to store your data, they're ready to sell you a simple Web service that will provide permanent, backed-up storage and you won't need to ever worry about it.

They may be right in that you might not need to worry about it, but you'll certainly need to wait for it. All traffic in and out of computers takes time. Computer networks are drastically slower than the traffic between the CPU and the local disk drive.

Programming graybeards grew up in a time when the Internet didn't exist. FidoNet would route your message by dialing up another computer that might be closer to the destination. Your data would take days to make its way across the country, squawking and whistling through modems along the way. This painful experience taught them that the right solution is to perform as much computation as you can locally and write to a distant Web service only when everything is as small and final as possible. Today’s programmers can take a tip from these hard-earned lessons of the past by knowing, like the programming graybeards, that the promises of cloud storage are dangerous and should be avoided until the last possible millisecond.

### Compilers have bugs

When things go haywire, the problem more often than not resides in our code. We forgot to initialize something, or we forgot to check for a null pointer. Whatever the specific reason, every programmer knows, when our software falls over, it’s our own dumb mistake -- period.

As it turns out, the most maddening errors aren’t our fault. Sometimes the blame lies squarely on the compiler or the interpreter. While compilers and interpreters are relatively stable, they're not perfect. The stability of today’s compilers and interpreters has been hard-earned. Unfortunately, taking this stability for granted has become the norm.

It's important to remember they too can be wrong and consider this when debugging the code. If you don't know it could be the compiler's fault, you can spend days or weeks pulling out your hair. Old programmers learned long ago that sometimes the best route for debugging an issue involves testing not our code but our tools. If you put implicit trust in the compiler and give no thought to the computations it is making to render your code, you can spend days or weeks pulling out your hair in search of a bug in your work that doesn’t exist. The young kids, alas, will learn this soon enough.

*Página 2*

Page 2 of 2

### Speed matters to users

Long ago, I heard that IBM did a study on usability and found that people's minds will start to wander after 100 milliseconds. Is it true? I asked a search engine, but the Internet hung and I forgot to try again.

Anyone who ever used IBM's old green-screen apps hooked up to an IBM mainframe knows that IBM built its machines as if this 100-millisecond mind-wandering threshold was a fact hard-wired in our brains. They fretted over the I/O circuitry. When they sold the mainframes, they issued spec sheets that counted how many I/O channels were in the box, in the same way car manufacturers count cylinders in the engines. Sure, the machines crashed, exactly like modern ones, but when they ran smoothly, the data flew out of these channels directly to the users.

I have witnessed at least one programming whippersnapper defend a new AJAX-heavy project that was bogged down by too many JavaScript libraries and data flowing to the browser. It's not fair, they often retort, to compare their slow-as-sludge innovations with the old green-screen terminals that they have replaced. The rest of the company should stop complaining. After all, we have better graphics and more colors in our apps. It’s true -- the cool, CSS-enabled everything looks great, but users hate it because it’s slow.

### The real Web is never as fast as the office network

Modern websites can be time pigs. It can often take several seconds for the megabytes of JavaScript libraries to arrive. Then the browser has to push these multilayered megabytes through a JIT compiler. If we could add up all of the time the world spends recompiling jQuery, it could be thousands or even millions of years.

This is an easy mistake for programmers who are in love with browser-based tools that employ AJAX everywhere. It all looks great in the demo at the office. After all, the server is usually on the desk back in the cubicle. Sometimes the "server" is running on localhost. Of course, the files arrive with the snap of a finger and everything looks great, even when the boss tests it from the corner office.

But the users on a DSL line or at the end of a cellular connection routed through an overloaded tower? They're still waiting for the libraries to arrive. When it doesn't arrive in a few milliseconds, they're off to some article on TMZ.

### Algorithmic complexity matters

On one project, I ran into trouble with an issue exactly like Richard in "Silicon Valley" and I turned to someone below the drinking age who knew Greasemonkey backward and forward. He rewrote our code and sent it back. After reading through the changes, I realized he had made it look more elegant but the algorithmic complexity went from `O(n)` to `O(n^2)`. He was sticking data in a list in order to match things. It looked pretty, but it would get very slow as `n` got large.

Algorithm complexity is one thing that college courses in computer science do well. Alas, many high school kids haven't picked this up while teaching themselves Ruby or CoffeeScript in a weekend. Complexity analysis may seem abstruse and theoretical, but it can make a big difference as projects scale. Everything looks great when `n` is small. Exactly as code can run quickly when there's enough memory, bad algorithms can look zippy in testing. But when the users multiply, it's a nightmare to wait on an algorithm that takes `O(n^2)` or, even worse, `O(n^3)`.

When I asked our boy genius whether he meant to turn the matching process into a quadratic algorithm, he scratched his head. He wasn't sure what we were talking about. After we replaced his list with a hash table, all was well again. He's probably old enough to understand by now.

### Libraries can suck

The people who write libraries don't always have your best interest at heart. They're trying to help, but they're often building something for the world, not your pesky little problem. They often end up building a Swiss Army knife that can handle many different versions of the problem, not something optimized for your issue. That's good engineering and great coding, but it can be slow.

If you're not paying attention, libraries can drag your code into a slow swamp and you won't even know it. I once had a young programmer mock my code because I wrote 10 lines to pick characters out of a string.

"I can do that with a regular expression and one line of code," he boasted. "Ten-to-one improvement." He didn't consider the way that his one line of code would parse and reparse that regular expression every single time it was called. He simply thought he was writing one line of code and I was writing 10.

Libraries and APIs can be great when used appropriately. But if they're used in the inner loops, they can have a devastating effect on speed and you won't know why.

### Related articles

[Peter Wayner](http://www.infoworld.com/author/Peter-Wayner/) — Contributing Editor

Peter Wayner is contributing editor at InfoWorld and the author of more than 16 books on diverse topics, including open source software, autonomous cars, privacy-enhanced computation, digital transactions, and steganography.

[*From CIO:* 8 Free Online Courses to Grow Your Tech Skills](http://www.cio.com/article/2847396/it-skills/8-free-online-courses-to-grow-your-tech-skills.html#tk.cross_2cio_intrcpt)
