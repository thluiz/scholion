---
url: "https://quora.com/What-thought-process-would-lead-one-to-invent-object-oriented-programming/answer/Alan-Kay-11"
captured_at: "2026-11-16T05:31:12+00:00"
title: "Alan Kay's answer to What thought process would lead one to invent object-oriented programming? - Quora"
domain: "quora-com"
---

What thought process would lead one to invent object-oriented programming?
Alan Kay
Have designed a few programming languages
Author has 725 answers and 9M answer views
6y

(Per Paul Hudson: “Maybe Alan Kay would answer. Since he did!”)

Well, OK.

In 1992, I was asked to write a history of what I actually did by the ACM for their second “History Of Programming Languages” conference. There are several versions online, including at Bret Victor’s site: “The Early History Of Smalltalk”. This should satisfy those who want more detail.

For the purposes here for Quora, (a) I did coin the phrase “object oriented programming” for what I was working on in 1966, but (b) I thought of what I was doing was a kind of “rotation” and generalization of an idea I had seen in a variety of forms since my days as:

a biologist
then as a programmer in the Air Force starting in 1961: a way to make a “semantic file system”
then in the hardware of the B5000 computer
in the large, as processes in “multi-programmed” and “time-shared” operating systems
most startlingly in Ivan Sutherland’s Sketchpad
in a more prosaic practical form in Simula
and as done with entire computers on networks (as in the upcoming ARPAnet by my research community).

What hit me in Nov 1966 was ridiculously, absurdly simple: “that, if you can have enough computers which can intercommunicate, this is all you need to define anything that can be done on a computer by any other means”. This is because each computer is universal, etc.

Putting aside the practical difficulties — I was basically a lazy mathematician, so it was fairly easy to detach from the industrious pragmatist I had to be as a programmer — this was very attractive as an idea, because it scaled much better than the traditional ideas of procedures and data structures as building blocks.

And it was so much cleaner, and so much more amenable to whole systems designs.

And so amenable to thinking in terms of “designing and programming simulations”. This last was from the two systems I saw within a week of each other that pushed me over the edge: Sketchpad and the first Simula — both of which were essentially set up to simulate complex entities containing many interrelated processes.

Another very attractive feature of having everything being made from “semantic software computers intercommunicating via messaging” is that some ugly properties of “data” could not only be fixed, but even eliminated. For example, standard hardware and programming languages which map closely to them can give rise to simple arrays, but not to “data structures” that are just a little more complicated — like sparse matrices — and stacks and queues, etc. These are easy to do if these are instead “processes” and get to decide internally what the “assignment arrow” should mean.

And this can lead to something much nicer than “data” that still has state but no race conditions on it. For example, inside the object it can decide to version the histories if it wants, it can do “atomic transactions”, it can only allow viewing when all of its relationships are consistent. And many more. The data idea was always a bad one, and this new semantic building block would allow objects to progress through time — and “learn” etc. — but would be much safer.

And then there is the idea of simulation itself, where the whole idea of “data” and “state” starts to get eclipsed by “competent objects” that can cooperate, much more like biological cells and human societies can.

So, the thought processes that led to this were basically “systems thought processes” that were about being able to easily define systems of processes: any kinds of systems of any kinds of processes.

This will not resemble much of what most readers will associate with OOP — in the sense of language like C++, Java, etc.

Quite a bit of the disconnect is in point of view/perspective. C++ and Java etc. use objects mainly to define new things that are very like data structures, and the programming that is done is generally very data structure like (e.g. “setters” turn any kind of entity back into a data structure that can be imperatively munged by anyone). Technically, this is actually “Abstract Data Structures” and though a subset of what can be done with objects, is a divergence from the intent.

The picture I delineated above allows a good systems designer to design a good system and make it, even if very large. It’s obviously that much of the benefit of the idea will be lost if skilled systems design is not employed.

An important side point is that the strength and generality of the definitional aspects of this paradigm can be quite independent of programming style (this is the central key of what “simulation of systems” means).

An object can perfectly simulate a function, procedure, a data structure, etc., so everything old can be covered completely, but it can also simulate very smart agencies and agents, to provide much stronger ways of doing things.

The flaw in how things have played out is that very few in computing actually put in the effort to grok the implications of “universal scalable systems of processes”, and instead have clung to very old and poorly scalable ways to program.

At Parc, we got a tremendous boost in what we could conceive and write in very few lines of code because we tried to use as much as possible about what we understood about this new way to organize and program complex systems. (Today, there is more understood about this, but even the first time around, we were constantly amazed at what was possible.)
