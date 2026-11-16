---
url: "https://yegor256.com/2016/08/15/what-is-wrong-object-oriented-programming.html"
captured_at: "2026-11-16T02:42:32+00:00"
title: "What's Wrong With Object-Oriented Programming?"
domain: "yegor256-com"
---

Recently, I was trying to convince a few of my readers that [a better understanding of an object](https://yegor256.com/2016/07/14/who-is-object.html) in OOP would help us solve many problems in existing pseudo-object-oriented languages. Then, suddenly, the question came up: “_What problems?_” I was puzzled. I thought it was obvious that the vast majority of modern software written in modern OO languages is unmaintainable and simply a mess. So I Googled a bit, and this is what I found (in chronological order).

![Swingers (1996) by Doug Liman](https://yegor256.com/images/2016/08/swingers.jpg)

Swingers (1996) by Doug Liman

The list of quotes is sorted in chronological order, with the oldest on the top:

![Edsger W. Dijkstra](https://yegor256.com/images/2016/08/edsger-dijkstra.jpg)  
[**Edsger W. Dijkstra**](https://en.wikipedia.org/wiki/Edsger_W._Dijkstra) (1989)  
“TUG LINES,” Issue 32, August 1989  
“Object oriented programs are offered as alternatives to correct ones” and “Object-oriented programming is an exceptionally bad idea which could only have originated in California.”

![Alan Kay](https://yegor256.com/images/2016/08/alan-kay.jpg)  
[**Alan Kay**](https://en.wikipedia.org/wiki/Alan_Kay) (1997)  
[The Computer Revolution hasn’t happened yet](https://www.youtube.com/watch?v=oKg1hTOQXoY)  
“I invented the term object-oriented, and I can tell you I did not have C++ in mind.” and “Java and C++ make you think that the new ideas are like the old ones. Java is the most distressing thing to happen to computing since MS-DOS.” ([proof](https://www.cc.gatech.edu/fac/mark.guzdial/squeak/oopsla.html))

![Paul Graham](https://yegor256.com/images/2016/08/paul-graham.jpg)  
[**Paul Graham**](https://en.wikipedia.org/wiki/Paul_Graham_%28computer_programmer%29) (2003)  
[The Hundred-Year Language](https://www.paulgraham.com/hundred.html)  
“Object-oriented programming offers a sustainable way to write spaghetti code.”

![Richard Mansfield](https://yegor256.com/images/2016/08/richard-mansfield.jpg)  
**Richard Mansfield** (2005)  
[Has OOP Failed?](https://www.4js.com/files/documents/products/genero/WhitePaperHasOOPFailed.pdf)  
“With OOP-inflected programming languages, computer software becomes more verbose, less readable, less descriptive, and harder to modify and maintain.”

![Eric Raymond](https://yegor256.com/images/2016/08/eric-raymond.jpg)  
[**Eric Raymond**](http://www.catb.org/~esr/) (2005)  
[The Art of UNIX Programming](http://catb.org/esr/writings/taoup/html/unix_and_oo.html)  
“The OO design concept initially proved valuable in the design of graphics systems, graphical user interfaces, and certain kinds of simulation. To the surprise and gradual disillusionment of many, it has proven difficult to demonstrate significant benefits of OO outside those areas.”

![Jeff Atwood](https://yegor256.com/images/2016/08/jeff-atwood.jpg)  
[**Jeff Atwood**](https://blog.codinghorror.com/) (2007)  
[Your Code: OOP or POO?](https://blog.codinghorror.com/your-code-oop-or-poo/)  
“OO seems to bring at least as many problems to the table as it solves.”

![Linus Torvalds](https://yegor256.com/images/2016/08/linus-torvalds.jpg)  
[**Linus Torvalds**](https://en.wikipedia.org/wiki/Linus_Torvalds) (2007)  
[this email](https://harmful.cat-v.org/software/c++/linus)  
“C++ is a horrible language. … C++ leads to really, really bad design choices. … In other words, the only way to do good, efficient, and system-level and portable C++ ends up to limit yourself to all the things that are basically available in C. And limiting your project to C means that people don’t screw that up, and also means that you get a lot of programmers that do actually understand low-level issues and don’t screw things up with any idiotic “object model” crap.”

![Oscar Nierstrasz](https://yegor256.com/images/2016/08/oscar-nierstrasz.jpg)  
[**Oscar Nierstrasz**](https://en.wikipedia.org/wiki/Oscar_Nierstrasz) (2010)  
[Ten Things I Hate About Object-Oriented Programming](http://blog.jot.fm/2010/08/26/ten-things-i-hate-about-object-oriented-programming)  
“OOP is about taming complexity through modeling, but we have not mastered this yet, possibly because we have difficulty distinguishing real and accidental complexity.”

![Rich Hickey](https://yegor256.com/images/2016/08/rich-hickey.jpg)  
[**Rich Hickey**](https://github.com/richhickey) (2010)  
[SE Radio, Episode 158](https://www.se-radio.net/2010/03/episode-158-rich-hickey-on-clojure/)  
“I think that large objected-oriented programs struggle with increasing complexity as you build this large object graph of mutable objects. You know, trying to understand and keep in your mind what will happen when you call a method and what will the side effects be.”

![Eric Allman](https://yegor256.com/images/2016/08/eric-allman.jpg)  
[**Eric Allman**](https://en.wikipedia.org/wiki/Eric_Allman) (2011)  
[Programming Isn’t Fun Any More](http://queue.acm.org/blogposting.cfm?id=34658)  
“I used to be enamored of object-oriented programming. I’m now finding myself leaning toward believing that it is a plot designed to destroy joy. The methodology looks clean and elegant at first, but when you actually get into real programs they rapidly turn into horrid messes.”

![Joe Armstrong](https://yegor256.com/images/2016/08/joe-armstrong.jpg)  
[**Joe Armstrong**](http://joearms.github.io/) (2011)  
[Why OO Sucks](http://harmful.cat-v.org/software/OO_programming/why_oo_sucks)  
“Objects bind functions and data structures together in indivisible units. I think this is a fundamental error since functions and data structures belong in totally different worlds.”

![Rob Pike](https://yegor256.com/images/2016/08/rob-pike.jpg)  
[**Rob Pike**](https://en.wikipedia.org/wiki/Rob_Pike) (2012)  
[here](https://plus.google.com/+RobPikeTheHuman/posts/hoJdanihKwb)  
“Object-oriented programming, whose essence is nothing more than programming using data with associated behaviors, is a powerful idea. It truly is. But it’s not always the best idea. … Sometimes data is just data and functions are just functions.”

![John Barker](https://yegor256.com/images/2016/08/john-barker.jpg)  
[**John Barker**](https://www.linkedin.com/in/johnebgood) (2013)  
[All evidence points to OOP being bullshit](https://tanzu.vmware.com/content/blog/all-evidence-points-to-oop-being-bullshit)  
“What OOP introduces are abstractions that attempt to improve code sharing and security. In many ways, it is still essentially procedural code.”

![Lawrence Krubner](https://yegor256.com/images/2016/08/lawrence-krubner.jpg)  
[**Lawrence Krubner**](https://www.linkedin.com/in/krubner) (2014)  
[Object Oriented Programming is an expensive disaster which must end](http://www.smashcompany.com/technology/object-oriented-programming-is-an-expensive-disaster-which-must-end)  
“We now know that OOP is an experiment that failed. It is time to move on. It is time that we, as a community, admit that this idea has failed us, and we must give up on it.”

![Asaf Shelly](https://yegor256.com/images/2016/08/asaf-shelly.jpg)  
[**Asaf Shelly**](https://www.linkedin.com/in/asafshelly) (2015)  
[Flaws of Object Oriented Modeling](https://software.intel.com/en-us/blogs/2008/08/22/flaws-of-object-oriented-modeling/)  
“Reading an object oriented code you can’t see the big picture and it is often impossible to review all the small functions that call the one function that you modified.”

* * *

If you have something to add to this list, please post a comment below.
