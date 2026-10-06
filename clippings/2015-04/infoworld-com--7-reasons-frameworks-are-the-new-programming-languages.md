---
url: "http://www.infoworld.com/article/2902242/application-development/7-reasons-why-frameworks-are-the-new-programming-languages.html"
captured_at: "2015-04-01T11:17:59-03:00"
title: "7 reasons why frameworks are the new programming languages"
domain: "infoworld-com"
---

# 7 reasons why frameworks are the new programming languages

In the 1980s, the easiest way to start a nerd fight was to proclaim that your favorite programming language was best. C, Pascal, Lisp, Fortran? Programmers spent hours explaining exactly why their particular way of crafting an if-then-else clause was superior to your way.

That was then. Today, battles involving syntax and structure are largely over because the world has converged on a few simple standards. The differences between the semicolons, curly brackets, and whatnot in C, Java, and JavaScript are minor. Interesting debates about typing and closures still exist, but most are moot because automation is closing the gap. If you don't like specifying a data type, there's a good chance the computer will be able to infer exactly what you meant. If your boss wants JavaScript but you like Java, a cross-compiler will convert all of your statically typed Java into minified JavaScript, ready to run in a browser. Why fight when technology has our backs?

**[ Find out how to handle the real-world problems faced by developers, with InfoWorld's [professional programmer's business survival guide](http://www.infoworld.com/resources/60833/it-jobs/professional-programmers-business-survival-guide#tk.ifw-infsb). | Keep up with hot topics in app dev with InfoWorld's [Application Development newsletter](http://www.infoworld.com/newsletters/signup.html#tk.ifw-infsb). ]**

Today, the interesting action is in frameworks. When I sat down with other faculty members at Johns Hopkins University to plan out a new course, frameworks dominated the conversation. Is Angular better than Ember? Is Node.js all that?

We designed a survey course that would explore the architecture of the most important software packages that are the foundation of the Internet. This was the center of the action, worthy of a survey course that would explore the architecture of the most important software packages girding today’s Internet.

In this sense, frameworks are the new programming languages. They are where the latest ideas, philosophies, and practicalities of modern-day coding are found. Some flame out, but many are becoming the new fundamental building blocks of programming. Here are seven facets fueling the framework trend -- and making frameworks the new favorite hotbed for nerd fights.

### Most coding is stringing together APIs

There was a time when writing software meant deploying all of your knowledge of the programming language to squeeze the most out of the code. It made sense to master the complexity of pointers, functions, and scope -- the quality of the code depended on doing the right thing. These days automation handles much of this. If you leave worthless statements in the code, don't worry. The compiler strips out dead code. If you leave pointers dangling, the garbage collector will probably figure it out.

Plus, the practice of coding is different now. Most code is now a long line of API calls. There's occasional reformatting of the data in between API calls, but even those jobs are usually handled by other APIs. A lucky few get to write clever, bit-banging, pointer-juggling code for the guts of our machines, but most of us work with the higher layers. We simply run pipe between APIs.

Because of this, it's more important to understand how an API behaves and what it can do. Which data structures does it accept? How do the algorithms behave when the data set grows larger? Questions like these are more central to today’s programming than ones about syntax or language. Indeed, there are now a number of tools that make it simple to call a routine in one language from another. It's relatively simple to link C libraries to Java code, for instance. Understanding the APIs is what matters.

### The shoulders of giants are worth standing on

Imagine you've become a disciple of Erlang or another new language. You decide it offers the best platform for writing a stable, bug-free app. This is a nice sentiment, but it could take years for you to rewrite all the code available for Java or PHP into your latest language of choice. Sure, your code could turn out to be dramatically better, but is that worth the extra time?

Frameworks let us leverage the hard work of those who came before us. We may not like the architecture they chose and we may argue over implementation details, but it's more efficient to stifle our complaints and find a way to live with the differences. It's so much easier to inherit all the good and the bad of the code base through a framework. Taking the macho route by writing everything yourself in your favorite new language rather than one of its more popular frameworks won’t allow you to enjoy the cream of your new choice as quickly as it would to simply defer to the framework makers and their APIs.

### Knowing the architecture is what matters, not the syntax

When most of the coding is stringing together API calls, there's not much advantage in learning the idiosyncrasies of the language. Sure, you could become an expert on how Java initializes static fields in the objects, but you would be much better off figuring out how to leverage the power of Lucene or JavaDB or some other pile of code. You could spend months grokking the optimizing routines of Objective-C compilers, but learning the ins and outs of the latest Apple core library will really make your code scream. You'll get much further learning the picky details of the framework than the syntax of the language on which the framework rests.

Most of our code spends most of its time in the inner loops of libraries. Getting the details of the language correct can help, but knowing what's going on in the libraries can pay off dramatically.

### Algorithms dominate

Learning a programming language can help you juggle the data stashed in the variables, but that only takes you so far. The real hurdle is getting the algorithms correct, and those are usually defined and implemented by the frameworks.

Many programmers understand it's dangerous and wasteful to spend time re-implementing standard algorithms and data structures. Sure, you might be able to tune it a bit to your needs, but you risk making subtle mistakes. Frameworks have been widely tested over the years. They represent our collective investment in a software infrastructure. There aren't many examples of when it makes sense to “go off the grid,” toss aside the hard work of others, and build an algorithmic cabin with your own two hands.

The right approach is to study the frameworks and learn how to use them to your best advantage. If you choose the wrong data structure, you could turn a linear job into one that takes a time that's a quadratic function of the input size. That's a big hassle once you go viral.

*Página 2*

Page 2 of 2

### Compilers and smart IDEs correct your syntax

Am I supposed to put a semicolon after the last statement in a block? Is the semicolon a "separator" or a "terminator"? Language designers have spent a long time crafting parsers that enforce these rules and -- guess what -- I don't care. There was a time a decade or so when I did care, but now the IDEs do the work for me. They're constantly watching my back and telling me when I screw up. I let them do the thinking for me and spend my time pondering the big questions about my code. The IDE is the peon, the programming assistant that handles those petty details.

Automation has saved us from the tedium of programming syntax. Oh sure, they don't do everything for us. We still need to have a vague idea of which punctuation to deploy. But most of the time, the details about the languages don't matter.

The IDEs also help with frameworks, but only the little details. They'll remind us the parameters for the function call, and they'll even check to see whether the data is the right type. After that, we're supposed to know which functions to use and how to plug them together. This is where our mind focuses when the syntax doesn't matter so much -- toward the higher-level methods and functions that will help surface solutions more expediently.

### Syntax is disappearing with visual languages

While this has been predicted for many years, it's slowly happening with some -- though not all -- code. Some programming continues to be very textual, but some is becoming more visual, which means the underlying computer language doesn't matter as much.

GUI builders are the easiest places to see this. You can drag and drop user interface widgets all day and night without worrying about whether it's C or Java or anything else. The details are coded in visual boxes.

Tools like AndroidBuilder make it possible to drag and drop much of the layout, and AndroidBuilder will dutifully write the XML and Java stubs needed to make the code work. It's hard to argue that visual languages are going to be the future, especially after they failed repeatedly to realize the prophecy, but the tools are growing more visual when they can be. This means languages are a bit less powerful or important.

### Code is law

Computer languages are largely agnostic. They're designed to be open, accepting, and almost infinitely malleable. They're meant to do whatever you want. Sure, sometimes you need to use a few extra characters because of the syntax, but those are merely keystrokes. After that, it's mainly if-then-elses, plus occasional clever bits. All of the language will still help you get the results you want the way you want to get them. If there are strictures, they're designed to keep your code as bug-free as possible, not limit what you can do.

Frameworks are where the power lies. This is where architects can decide what is allowed and what is inherently forbidden. If the architect doesn't want something to happen, the magic function call is missing from the API. If the architect likes the idea, there are usually multiple function calls and plenty of supporting tools. This is why Larry Lessig, the Harvard law professor, likes to say, "Code is Law."

The frameworks establish the rules for their corner of the Internet and you must live within them once you choose them. Some blogging platforms encourage linking with others through AJAX calls and some don't support them. That's why you must investigate carefully and choose wisely. It's ultimately why frameworks dominate every part of our lives, even those few moments when we're not programming.

### Related articles
