---
url: "https://infoq.com/presentations/Null-References-The-Billion-Dollar-Mistake-Tony-Hoare"
captured_at: "2026-11-16T02:13:31+00:00"
title: "Null References: The Billion Dollar Mistake"
domain: "infoq-com"
---

[InfoQ Homepage](https://infoq.com/ "InfoQ Homepage") [Presentations](https://infoq.com/presentations "Presentations") Null References: The Billion Dollar Mistake

View Presentation

Speed:

01:01:58

![Presentation Slides](https://imgopt.infoq.com/fit-in/1288x0/filters:quality\(80\)/presentations/Null-References-The-Billion-Dollar-Mistake-Tony-Hoare/en/slides/slide0.jpg)

## Summary

Tony Hoare introduced Null references in ALGOL W back in 1965 "simply because it was so easy to implement", says Mr. Hoare. He talks about that decision considering it "my billion-dollar mistake".

## Bio

Sir Charles Antony Richard Hoare, commonly known as Tony Hoare, is a British computer scientist, probably best known for the development in 1960, at age 26, of Quicksort. He also developed Hoare logic, the formal language Communicating Sequential Processes (CSP), and inspired the Occam programming language.

## About the conference

QCon is a conference that is organized by the community, for the community.The result is a high quality conference experience where a tremendous amount of attention and investment has gone into having the best content on the most important topics presented by the leaders in our community. QCon is designed with the technical depth and enterprise focus of interest to technical team leads, architects, and project managers.

## Key Takeaways

*   Null references have historically been a bad idea
*   Early compilers provided opt-out switches for run-time checks, at the expense of correctness
*   Programming language designers should be responsible for the errors in programs written in that language
*   Customer requests and markets may not ask for what's good for them; they may need regulation to build the market
*   If the billion dollar mistake was the null pointer, the C gets function is a multi-billion dollar mistake that created the opportunity for malware and viruses to thrive

## Show notes

*   00:45 Thesis: historically, null references have been a bad idea.
*   02:15 Null references were created in 1964 - how much have they cost? Less or more than a billion dollars?
*   03:20 Whilst we don't know, the amount is probably in the order of an (American) billion - more than a tenth of a billon, less than ten billion.

**History of programming languages**

*   03:35 A little on the history of the idea. Tony started as a programmer with Elliot's \[Ed: Elliot Brothers, London Ltd\] in 1960, and was asked to design a new programming language.
*   04:10 In the library was a 23-page booklet entitled "Report on the international language ALGOL60";, edited by Peter Naur.
*   04:30 Used as a basis for the new language, but left out the complicated parts such as "if"; and "then";.
*   05:00 Most software was still written in machine code (including the complier).
*   05:25 Most assembly was simple enough to understand that when it went wrong, it could be diagnosed by following through to find out what the fault was.

**Towards a high level language**

*   05:40 Using a high level language meant you couldn't step through the machine code.
*   05:50 The Elliot's machine had 4096 locations, with a length of 4 7/8 bytes long (39 bits), although other machines had different sizes (IBM's had 36 bits.
*   06:30 To shield customers from implementation details, customers were told the errors in terms of the high level programming language, instead of a hexadecimal core dump.
*   07:10 In order to implement error messages, an array had a check to verify whether its reference was in the bounds.
*   08:00 Adding checks to arrays added space and time to the program; on Tony's first machine it ran at less than 2k operations per second (500 micro seconds per operation, and two such tests for each array bounds).
*   08:40 No undetected array errors, and customers didn't know they could trade off safety for speed.
*   09:30 The Java language has, after 30 years, decided to replicate the decision to bounds checking arrays. \[Ed: other languages, like Python, handle this as well\].

**Record oriented programming**

*   10:20 Introduced the concept of an object, which could be referred to with a pointer.
*   10:30 With pointers, it is possible to wreak havoc with the program you are trying to test \[Ed: this is the single biggest cause of security failures in modern day code\].
*   10:55 If a floating point value or integer is used as a pointer accidentally, and the value it is pointing to is updated, then it will just as likely update the program which may then crash or cause problems now or in the future. \[Ed: these days, virtual memory and page mapping takes away some of the problems about editing program code, but these weren't present in the computers of that era.\]
*   12:00 As a given, when invoking a function with a pointer required the type of the pointer to be declared.
*   13:30 The type of the program can be compile time checked from the static types.
*   13:45 Many years later Tony discovered that some of these ideas had been integrated for the first time, although previous examples came from both Doug Rossier's Plex and Simula.

**Records avoid subscript errors**

*   14:35 The great thing about record handling is that you don't need to have a subscript error, because you cannot construct a pointer that points to something that doesn't exist, and a whole set of errors cannot occur and do not need to be checked at run-time.
*   15:50 Later, we asked the customers whether they wanted the option to be able turn off the type checking in production. It's a bit like wearing a life jacket when you are practicing drills, but then taking it off the ship was sinking. The customers decided to not switch off the type checking.
*   17:00 We produced a compiler that would translate Fortran programs to Algol programs. It was a disaster, and no Fortran user would use it.
*   18:00 The reason that they couldn't use it was because they couldn't use any of their programs. Within a few milliseconds of running it would come up with a subscript error. The error wasn't wanted as they just wanted the code to run.

**Type checking as standard**

*   19:00 Things have changed a bit - mainstream programming languages like Java now have subscript checking as standard, type-checked object oriented programming.
*   19:30 And then I went and invented the null pointer. You either have to check every reference, or you risk disaster.
*   19:45 Fortran programmers preferred to risk disaster; in fact, experience disaster, rather than check subscripts.
*   20:00 I didn't know it a the time, but my friend Edsger Dijkstra thought the null reference was a bad idea. He said:
*   20:20 "If you have a null reference, then every bachelor who you represent in your object structure will seem to be married polyamocursly to the same person Null".
*   20:55 It brings back the same question whether you want to run your code quickly (without checks) or safely (with checks).

**Disjoint unions and discrimination test**

*   21:10 I did know there was a solution based on the idea of discrimination of objects belong to a disjoint union class; that is, two sets in which there are no members in common. For example a Vehicle class that has subtypes Car and Bus; the Car may have a luggage carrying capacity property while the Bus has a person carrying capacity. You would then have a discrimination test and do different operations based on whether it was a Bus or a Car.
*   23:40 The size of the program grows with the number of discrimination clauses and number of types. This allows null to be represented as a different class, which can then be passed in to functions.
*   24:30 The types of the pointer could then be implemented as a union of either a pointer to the null type, or a pointer to the type.
*   25:20 This leads to implementation problems; what happens if you assume that a pointer is a Bus but change that pointer to a Car instead?
*   25:55 One of the things you want is to be able to know in a high level language is that when it is created, all of its data structure is initialised. In this case, a null reference can be used to indicate that the data is missing or not known at this time. In fact, it's the only thing that can be assigned if you have a pointer to a particular type.
*   26:35 If you don't want to use null, you have to implement a sublanguage for representing how to initialise objects of the right type. If the data structure is a tree-based representation, this is achievable if you create the leaves first because they can be fully created.
*   27:10 It isn't possible to create a cyclic structure using this technique; if there's a cycle in the data structure you can start with a null pointer and then assign it once the rest of the cycle has been completed.

**Introducing null**

*   27:40 This led me to suggest that the null value is a member of every type, and a null check is required on every use of that reference variable, and it may be perhaps a billion dollar mistake.
*   28:00 Modern languages such as C# or Spec# and even Java are introducing the idea of non-null reference parameters, and compile time checking which verifies that they cannot possibly have null values.
*   28:50 The issues of overloading and inheritance make it a lot more difficult to do these when null references were originally created.
*   29:20 The movement must have been made based on the fact that null references were an expensive mistake.

**Programming languages should be responsible for their users**

*   30:20 A programming language designer should be responsible for the mistakes made by programmers using the language. It is a serious activity; not one that should be given to programmers with 9 months experience with assembly; they should have a strong scientific basis, a good deal of ingenuity and invention and control of detail, and a clear objective that the programs written by people using the language would be correct. free of obvious errors and free of syntactical traps.
*   31:40 This was the idea that led me to the idea of using proof and formal verification of programs as logical and mathematical models, is a method of conducting research into the design of good programming languages. I wasn't too optimistic in 1969 would actually be using proofs to guarantee correctness of programs.
*   32:20 By looking at the programming language and whether programs written would be possible to prove the programs written in the language gives an objective measure of how easy it would be to verify the program later. If the understanding of applying a rule locally has to depend on global knowledge of the program then you haven't done a good job in creating the programming language, and you don't need your customers to tell you that.
*   33:30 In fact customers don't tell you - it's very easy to persuade your customers that anything that goes wrong is their fault rather than yours.
*   33:40 I rejected that - programming language design is a serious scientific engineering activity, and we should begin to take responsibility for the mistakes that our users make.

**Designing for safety**

*   33:55 It's beginning to happen again - the Java programming language and its successors have all used avoidance of error as one of the criteria in the detail ed design of new features of the language, and I'm delighted to give them a great deal of credit for that - but it is only one criteria, and it is only one.
*   34:35 The most important criteria is backwards compatibility of everything that has gone before, with the millions or billions lines of code that have been written.
*   34:55 Every commercial language has to make concessions for commercial and historical reasons; but gradually, ideas change, programmers get more interested in provable correctness; production techniques, languages, checkers, analytic tools, test case generators and so on that are going to help them get their programs correct.

**Safe at any speed?**

*   35:40 The analogy that I draw is with agricultural pollution and vehicle security. When Ralph Nader first started publishing "Unsafe at any speed", what he was saying had no connection with the marketplace - customers were not asking for reliability or safety as one of their vehicles.
*   36:20 But gradually, customers started to demand reliability and safety, with the aid of law making and legal constraints requiring basic levels of safety to be included in every vehicle sold.
*   36:50 There is a possibility that the marketplace will move the reliability of programs and the language in which they&'re expressed.
*   37:15 For many professional engineers, they do have ideals and do pursue them in preference to not pursuing them whenever the opportunity arises. The commercial imperative that requires greater attention paid to the formal correctness of the programs is the virus.
*   37:50 The virus (or malware, or worm) does dreadful things by reaching the parts of the program that it doesn't usually reach. It is no longer applicable to test the cases that are likely to arise, the virus will attack the places that are not likely to arise, and so need just the same level of testing.
*   38:35 It forces you to get the while program correct, not just the ones that will be used by customers, the code that will be used by viruses needs to be checked too.
*   38:45 And that can't be done by testing, it has to be done by analysis.
*   38:55 Analysis of the source code, type-checking techniques are the simplest, but more sophisticated reasoning techniques are being used to high volume code to check that it doesn't contain any naughty things like null reference dereferencing.

**Introduction of the virus**

*   39:30 So if I am responsible for a billion dollar mistake; and I bring it up because other designers are much more responsible.
*   39:40 The designers of C - one can definitely quantify. The buffer overflow is a direct result of the C language gets fnction that doesn't check the bounds of the string input. That allowed the early viruses to get in by overwriting the return values of the code.
*   40:10 These simple viruses taught the world how to write malware. Without this very simple entry point, it is quite possible that nobody would ever have thought to look for the more subtle kind of thing which are now being exploited every day by people who are now motivated, skilled, and whose profession and income it is to write botware, malware.
*   40:45 If it hadn't been for the gets routine in C, we might have had no malware.
*   40:55 Now one virus - the CodeRed virus - was estimated to have cost the world economy 4 billion dollars, because it brought down all the networks, and the interruption to business and all the ordinary banking, other business was estimated to cost that amount. There was another one later as well.
*   41:30 And that was more than the Millennium bug, which was estimated a little less than 4 billion dollars.

## Companies mentioned

*   Elliot Brothers (London) Ltd

## People mentioned

*   Peter Naur
*   Doug Rossier
*   Edsger Dijkstra
*   Ralph Nader

## Languages mentioned

*   Algol60
*   Occam
*   Plex
*   Simula
*   Fortran
*   C#
*   Spec#
*   C

## Products mentioned

*   [ACM Turing Award speech](http://www.webcitation.org/65BW96PjQ)

## See more presentations with show notes

Recorded at:

[![QCon is a conference that is organized by the community, for the community.The result is a high quality conference experience where a tremendous amount of attention and investment has gone into having the best content on the most important topics presented by the leaders in our community. QCon is designed with the technical depth and enterprise focus of interest to technical team leads, architects, and project managers.](https://res.infoq.com/presentations/Null-References-The-Billion-Dollar-Mistake-Tony-Hoare/en/promoimage/qcon_logo3.jpg)](http://qconsf.com/sf2009/?utm_source=infoq&utm_medium=listing&utm_campaign=listingpresentations)

Aug 25, 2009
