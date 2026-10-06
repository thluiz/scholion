---
url: "http://samizdat.mines.edu/howto/HowToBeAProgrammer.html"
captured_at: "2012-06-04T12:07:10-03:00"
title: "How to be a Programmer: A Short, Comprehensive, and Personal Summary"
domain: "samizdat-mines-edu"
---

# A Short, Comprehensive, and Personal Summary

## Chapter�2.�Beginner

## Personal Skills

### Learn to Debug

Debugging is the cornerstone of being a programmer.
The first meaning of the verb *to debug* is to remove errors, but
the meaning that really matters is  *to see into the execution of a program by examining it*.
A programmer that cannot debug effectively is blind.

Idealists that think design, or analysis, or
complexity theory, or whatnot, are more fundamental are not
working programmers. The working programmer does not live in an ideal world.
Even if you are perfect, your are surrounded by and must
interact with code written by major software companies, organizations
like GNU, and your colleagues. Most of this code is imperfect and
imperfectly documented. Without the ability to gain visibility into
the execution of this code the slightest bump will throw you permanently.
Often this visibility can only be gained by experimentation,
that is, debugging.

Debugging is about the running of programs, not programs themselves.
If you buy something from a major software company, you usually don't
get to see the program. But there will still arise places where the
code does not conform to the documentation (crashing your entire machine
is a common and spectacular example), or where the documentation is mute.
More commonly, you create an error, examine the code you
wrote and have no clue how the error can be occurring. Inevitably, this
means some assumption you are making is not quite correct, or some
condition arises that you did not anticipate. Sometimes the magic trick
of staring into the source code works. When it doesn't, you must debug.

To get visibility into the execution of a program you must be able to
execute the code and observe something about it. Sometimes this is visible,
like what is being displayed on a screen, or the delay between two events.
In many other cases, it involves things that are not meant to be visible,
like the state of some variables inside the code, which lines of code
are actually being executed, or whether certain assertions hold across a
complicated data structure. These hidden things must be revealed.

The common ways of looking into the ‘innards’ of an executing program can be categorized as:

- Using a debugging tool,
- Printlining --- Making a temporary modification to the program,
  typically adding lines that print information out, and
- Logging --- Creating a permanent window into the programs
  execution in the form of a log.

Debugging tools are wonderful when they are stable and available, but the
printlining and logging are even more important.
Debugging tools often lag
behind language development, so at any point in time they may
not be available. In addition, because the debugging tool may subtly change the way
the program executes it may not always be practical.
Finally, there are some kinds of debugging, such as checking
an assertion against a large data structure, that require writing code
and changing the execution of the program.
It is good to know how to use debugging tools when they are stable,
but it is critical to be able to employ the other two methods.

Some beginners fear debugging when it requires modifying
code. This is understandable---it is a little like exploratory
surgery. But you have to learn to poke at the code and make it jump;
you have to learn to experiment on it, and understand that nothing that
you temporarily do to it will make it worse. If you feel this fear,
seek out a mentor---we lose a lot of good programmers at the delicate
onset of their learning to this fear.

### How to Debug by Splitting the Problem Space

Debugging is fun, because it begins with a mystery. You think it should
do something, but instead it does something else.
It is not always quite so simple---any
examples I can give will be contrived compared to what sometimes happens
in practice. Debugging requires creativity and ingenuity. If there is a
single key to debugging is to use the
 *divide and conquer* technique on the mystery.

Suppose, for example, you created a program that should do
ten things in a sequence. When you run it, it crashes.
Since you didn't program it to crash, you now have a mystery.
When out look at the output, you see that the first seven
things in the sequence were run successfully. The last three are
not visible from the output, so now your mystery is smaller:
‘It crashed on thing #8, #9, or #10.’

Can you design an experiment to see which thing it crashed on? Sure.
You can use a debugger or we can add printline statements (or the equivalent
in whatever language you are working in) after #8 and #9.
When we run
it again, our mystery will be smaller, such as
‘It crashed on thing #9.’
I find that bearing in mind exactly what the mystery is at any point
in time helps keep one focused. When several people are working
together under pressure on a problem it is easy to forget what the
most important mystery is.

The key to divide and conquer as a debugging technique
is the same as it is for algorithm design: as long as you do a
good job splitting the mystery in the middle, you won't have to
split it too many times, and you will be debugging quickly.
But what is the middle of a mystery? There is where
true creativity and experience comes in.

To a true beginner, the
space of all possible errors looks like every line in the source code.
You don't have the vision you will later develop to see the other
dimensions of the program, such as the space of executed lines, the
data structure, the memory management, the interaction with foreign code,
the code that is risky, and the code that is simple.
For the experience programmer, these other
dimensions form an imperfect but very
useful mental model of all the things that can go wrong. Having that
mental model is what helps one find the middle of the mystery effectively.

Once you have evenly subdivided the space of all that can go wrong, you
must try to decide in which space the error lies. In the simple case
where the mystery is: ‘Which single unknown line makes my program crash?’,
you can ask yourself:
‘Is the unknown line executed before or after this line that
I judge to be executed in the about the middle of the running program?’
Usually you will not be so lucky as to know that the error
exists in a single line, or even a single block.
Often the mystery will be more like: ‘Either there is a pointer in that
graph that points to the wrong node, or my algorithm that adds
up the variables in that graph doesn't work.’ In that case you may
have to write a small program to check that the pointers in the graph
are all correct in order to decide
which part of the subdivided mystery can be eliminated.

### How to Remove an Error

I've intentionally separated the act of examining a program's
execution from the act of fixing an error. But of course,  *debugging*
does also mean removing the bug.
Ideally you will have perfect understanding of the code and will
reach an ‘A-Ha!’ moment where you perfectly see the error and
how to fix it. But since your program will often use
insufficiently documented systems
into which you have no visibility,
this is not always possible. In other cases
the code is so complicated that your understanding cannot be
perfect.

In fixing a bug, you want to make the smallest change that
fixes the bug. You may see other things that need improvement;
but don't fix those at the same time. Attempt to employ
the scientific method of changing one thing and only one thing
at a time. The best process for this is to be able to easily
reproduce the bug, then put your fix in place, and then rerun the
program and observe that the bug no longer exists. Of course,
sometimes more than one line must be changed, but you should
still conceptually apply a single atomic change to fix the
bug.

Sometimes, there are really several bugs that look like one.
It is up to you to define the bugs and fix them one at a time.
Sometimes it is unclear what the program should do
or what the original author intended. In this
case, you must exercise your experience and judgment and assign
your own meaning to the code. Decide what it should do,
and comment it or clarify it in some way and then make the
code conform to your meaning. This is an intermediate or
advanced skill that is sometimes harder than writing the
original function in the first place, but the real world
is often messy. You may have to fix a system you cannot
rewrite.

### How to Debug Using a Log

*Logging* is the practice of writing a system so that it produces a
sequence of informative records, called a  *log*.  *Printlining* is just producing a simple, usually temporary, log.
Absolute beginners must understand and use logs because their
knowledge of the programming is limited; system architects must
understand and use logs because of the complexity of the system.
The amount of information that is provided by the log should be configurable,
ideally while the program is running.
In general, logs offer three basic advantages:

- Logs can provide useful information about bugs that are hard
  to reproduce (such as those that occur in the production environment but
  that cannot be reproduced in the test environment).
- Logs can provide statistics and data relevant to
  performance, such as the time passing between statements.
- When configurable, logs allow general information to be
  captured in order to debug unanticipated specific problems
  without having to modify and/or redeploy the code just to deal
  with those specific problems.

The amount to output into the log is always a compromise
between information and brevity.
Too much information makes the
log expensive and produces  *scroll blindness*, making it hard
to find the information you need.
Too little information and it may not
contain what you need.
For this reason, making what is output configurable is
very useful.
Typically, each record in the log will identify its position in
the source code, the thread that executed it if applicable,
the precise time of execution, and, commonly, an additional useful piece
of information, such as the value of some variable, the amount of
free memory, the number of data objects, etc.
These log statements are sprinkled
throughout the source code but are particularly at major functionality
points and around risky code.
Each statement can be assigned a level
and will only output a record if the system
is currently configured to output that level.
You should design the log statements to address
problems that you anticipate.
Anticipate the need to measure performance.

If you have a permanent log, printlining can now be done in terms
of the log records, and some of the debugging statements will
probably be permanently added to the logging system.

### How to Understand Performance Problems

Learning to understand the performance of a running system
is unavoidable for the same reason that learning debugging is.
Even if the
code you understand perfectly precisely the cost
of the code you write, your code will
make calls into other software systems
that you have little control over or visibility into.
However, in practice
performance problems are a little different and a little easier
than debugging in general.

Suppose that you or your customers
consider a system or a subsystem to be too slow.
Before you try to make it faster,
you must build a mental model of why it is slow.
To do this you can use a profiling tool or a
good log to figure out where the time or other
resources are really being spent.
There is a famous dictum that 90% of the time will be
spent in 10% of the code.
I would add to that the importance
of input/output expense (I/O) to performance issues.
Often most of the time is spent in I/O in one way or another.
Finding the expensive I/O and the expensive 10% of
the code is a good first step to building your mental model.

There are many dimensions to the performance of a
computer system, and many resources consumed.
The first resource to measure is  *wall--clock time*,
the total time that passes for the computation.
Logging wall-clock time is particularly valuable because it can inform
about unpredictable circumstance that arise in situations where other profiling is impractical.
However, this may not always represent the whole picture.
Sometimes something that
takes a little longer but doesn't burn up so many processor seconds will
be much better in computing environment you actually have to deal with.
Similarly, memory, network bandwidth, database or other server accesses
may, in the end, be far more expensive than processor seconds.

Contention for shared resources that are synchronized can
cause deadlock and starvation.
Deadlock is the inability to proceed because of
improper synchronization or resource demands.
Starvation is the failure to schedule a component properly.
If it can be at all anticipated,
it is best to have a way of measuring this contention
from the start of your project.
Even if this contention does not occur,
it is very helpful to be able to assert that with confidence.

### How to Fix Performance Problems

Most software projects can be made with relatively little effort
10 to 100 times
faster than they are at the they are first released.
Under time-to-market pressure,
it is both wise and effective to choose a solution that
gets the job done simply and quickly, but less efficiently
than some other solution. However, performance is a part
of usability, and often it must eventually be considered more carefully.

The key to improving the performance of a very complicated
system is to analyze it well enough to find the
 *bottlenecks*, or places where most of the resources are consumed.
There is not much sense
in optimizing a function that accounts for only 1% of the
computation time.
As a rule of thumb you should think carefully before doing
anything unless you think it is going to make the system or
a significant part of it at least twice as fast.
There
is usually a way to do this. Consider
the test and quality assurance effort that your change
will require.
Each change brings a test burden
with it, so it is much better to have a few big changes.

After you've made a two-fold improvement in something, you need
to at least rethink and perhaps reanalyze to discover the
next-most-expensive bottleneck in the system,
and attack that to get another two-fold improvement.

Often, the bottlenecks in performance will be an example of
counting cows by counting legs and dividing by four, instead
of counting heads. For example, I've made errors such as
failing to provide a relational database system with a proper
index on a column I look up a lot, which probably made it
at least 20 times slower.
Other examples include doing
unnecessary I/O in inner loops, leaving in debugging
statements that are no longer needed, unnecessary memory
allocation, and, in particular, inexpert use of libraries and
other subsystems that are often poorly documented with respect
to performance. This kind of improvement is sometimes called
 *low-hanging fruit*, meaning that it can be easily picked to
provide some benefit.

What do you do when you start to run out of low-hanging fruit?
Well, you can reach higher, or chop the tree down. You can continue
making small improvements or you can seriously redesign a system or
a subsystem. (This is a great opportunity to use your skills as
a good programmer, not only in the new design but also in convincing
your boss that this is a good idea.)
However, before you argue for the redesign
of a subsystem, you should ask yourself
whether or not your proposal will
make it five to ten time better.

### How to Optimize Loops

Sometimes you'll encounter loops, or recursive functions, that take
a long time to execute and are bottlenecks in your product.
Before you try to
make the loop a little faster, but spend a few minutes considering
if there is a way to remove it entirely.
Would a different algorithm do?
Could you compute that while computing something else?
If you can't find away around it, then you can
optimize the loop.
This is simple; move stuff out. In the end,
this will require not only ingenuity but also an understanding of
the expense of each kind of statement and expression.
Here are some suggestions:

- Remove floating point operations.
- Don't allocate new memory blocks unnecessarily.
- Fold constants together.
- Move I/O into a buffer.
- Try not to divide.
- Try not to do expensive typecasts.
- Move a pointer rather than recomputing indices.

The cost of each of these operations depends on your specific
system. On some systems compilers and hardware do these things
for you. Clear, efficient code is better than code that requires
an understanding of a particular platform.

### How to Deal with I/O Expense

For a lot of problems, processors are fast compared to the cost of
communicating with a hardware device. This cost is usually
abbreviated I/O, and can include network cost, disk I/O,
database queries, file I/O, and other use of
some hardware not very close to the processor.
Therefore building a fast system is often more a question of improving
I/O than improving the code in some tight loop, or even improving an algorithm.

There are two very fundamental techniques to improving I/O: caching
and representation. Caching is avoiding I/O (generally avoiding
the reading of some abstract value) by storing a copy of that value
locally so no I/O is performed to get the value.
The first key to caching is to make it crystal clear which data
is the  *master* and which are  *copies*. There is only one
master---period.
Caching brings with it the danger that the copy is sometimes can't
reflect changes to the master instantaneously.

Representation is the approach of making I/O cheaper by representing
data more efficiently. This is often in tension with other demands, like human readability and portability.

Representations can often be improved by a factor of two or three
from their first implementation. Techniques for doing this
include using a binary representation instead of one that is human readable,
transmitting a dictionary of symbols along with the data so that
long symbols don't have to be encoded, and, at the extreme, things
like Huffman encoding.

A third technique that is sometimes possible is to improve the
locality of reference by pushing the computation closer to the data.
For instance, if you are reading some data from a database and
computing something simple from it, such as a summation, try to
get the database server to do it for you. This is highly dependent
on the kind of system you're working with, but you should explore it.

### How to Manage Memory

Memory is a precious resource that you can't afford to run out of.
You can ignore it for a while but eventually you will have to
decide how to manage memory.

Space that needs to persist beyond the scope of a single subroutine
is often called  *heap allocated*.
A chunk of
memory is useless, hence  *garbage*, when nothing refers to it.
Depending on the system you use,
you may have to explicitly
deallocate memory yourself when it is about to
become garbage.
More often you may be able to use a system
that provides a  *garbage collector*.
A garbage collector
notices garbage and frees its space without
any action required by the programmer.
Garbage collection is wonderful:
it lessens errors and increases code
brevity and concision cheaply.
Use it when you can.

But even with
garbage collection, you can fill up all memory with garbage. A
classic mistake is to use a hash table as a cache and forget to
remove the references in the hash table.
Since the reference remains,
the referent is noncollectable but useless.
This is called a  *memory leak*.
You should look for and fix memory leaks early.
If you have long running
systems memory may never be exhausted in testing
but will be exhausted by the user.

The creation of new objects is moderately expensive on any system.
Memory allocated directly in the local variables of a subroutine, however,
is usually cheap
because the policy for freeing it can be very simple.
You should avoid
unnecessary object creation.

An important case occurs when you can define an upper bound on the number
of objects you will need at one time. If these objects all take up the
same amount of memory, you may be able to allocate a single block of memory,
or a buffer, to hold them all. The objects you need can be allocated and
released inside this buffer in a set rotation pattern, so it is sometimes
called a ring buffer. This is usually faster than heap allocation.

Sometimes you have to explicitly free allocated space so it can be
reallocated rather than rely on garbage collection. Then you must apply
careful intelligence to each chunk of allocated memory and design a way
for it to be deallocated at the appropriate time. The method may
differ for each kind of object you create. You must make sure that
every execution of a memory allocating operation is matched by a memory
deallocating operation eventually. This is so difficult that programmers often
simply implement a rudimentary form or garbage collection,
such as reference counting, to do this for them.

### How to Deal with Intermittent Bugs

The intermittent bug is a cousin of the
50-foot-invisible-scorpion-from-outer-space
kind of bug. This nightmare occurs so rarely that it is hard to observe,
yet often enough that it can't be ignored.
You can't debug because you can't find it.

Although after 8 hours you will start to doubt it,
the intermittent bug has to obey the same laws of logic everything else does.
What makes it hard is that it occurs only under unknown conditions. Try to
record the circumstances under which the bug does occur,
so that you can guess at
what the variability really is. The condition may be related to data values,
such as ‘This only happens when we enter  *Wyoming* as a value.’
If that is not
the source of variability, the next suspect should be
improperly synchronized concurrency.

Try, try, try to reproduce the bug in a controlled way.
If you can't reproduce it, set a trap
for it by building a logging system, a special one if you have to,
that can log what you guess you need when it really does occur.
Resign yourself to that if the bug only occurs
in production and not at your whim, this is may be a long process.
The hints that you get from the log may not provide
the solution but may give you enough information to
improve the logging.
The improved logging system may take a long time to be put into production.
Then, you have to wait for the bug to reoccur to get more information.
This cycle can go on for some time.

The stupidest intermittent bug I ever created was in a multi-threaded
implementation of a functional
programming language for a class project.
I had very carefully
insured correct concurrent evaluation of the functional program,
good utilization of all the CPUs available (eight, in this case).
I simply forgot to synchronize
the garbage collector. The system could run
a long time, often finishing whatever task I began,
before anything noticeable went wrong.
I'm ashamed to admit I
had begun to question the hardware before
my mistake dawned on me.

At work we recently had an intermittent bug that took us several
weeks to find. We have multi-threaded application servers in
Java™ behind Apache™ web servers.
To maintain fast page turns,
we do all I/O in small set of four separate threads that are different
than the page-turning threads. Every once in a while these would
apparently get ‘stuck’ and cease doing anything useful, so far as
our logging allowed us to tell, for hours. Since we had four threads,
this was not in itself a giant problem---unless all four got stuck.
Then the queues emptied by these threads would quickly fill up
all available memory and crash our server. It took us about a
week to figure this much out, and we still didn't know what caused
it, when it would happen, or even what the threads where doing when
they got ‘stuck’.

This illustrates some risk associated with third-party
software. We were using a licensed piece of code that removed
HTML tags from text. Due to its place of origin we affectionately
referred to this as ‘the French stripper.’ Although we had the
source code (thank goodness!) we had not studied it carefully
until by turning up the logging on our servers we finally realized
that the email threads were getting stuck in the French stripper.

The stripper performed well except on some long and unusual kinds of texts.
On these texts, the code was quadratic or worse. This means
that the processing time was proportional to the square of the length
of the text.
Had these texts occurred commonly, we would have found the bug
right away. If they had never occurred at all, we would never have
had a problem. As it happens, it took us weeks to finally understand
and resolve the problem.

### How to Learn Design Skills

To learn how to design software, study the action of a mentor by
being physically present when they are designing. Then study
well-written pieces of software. After that, you can read some books on the latest design techniques.

Then you must do it yourself. Start with a small project.
When you are finally done, consider how the design failed or
succeeded and how you diverged from your original conception.
They move on to larger projects, hopefully in conjunction with
other people. Design is a matter of judgment that takes years
to acquire. A smart programmer can learn the basics adequately in
two months and can improve from there.

It is natural and helpful to develop your own style, but remember
that design is an art, not a science. People who write books on
the subject have a vested interest in making it seem scientific.
Don't become dogmatic about particular design styles.

### How to Conduct Experiments

The late, great Edsger Dijkstra has eloquently explained that Computer Science
is not an experimental science[ExpCS] and doesn't
depend on electronic computers.
As he puts it referring to the 1960s[Knife],

> ...the harm was done: the topic became known as
> “computer science”---which, actually, is like referring to
> surgery as “knife science” --- and it was firmly implanted
> in people's minds that computing science is about
> machines and their peripheral equipment.

Programming ought not to be an experimental science,
but most working programmers do not have the luxury of
engaging in what Dijkstra means by computing science.
We must work in the realm of experimentation, just as some,
but not all, physicists do. If thirty years from now
programming can be performed without experimentation, it
will be a great accomplishment of Computer Science.

The kinds of experiments you will have to perform include:

- Testing systems with small examples to verify that they
  conform to the documentation or to understand their response
  when there is no documentation,
- Testing small code changes to see if they actually fix
  a bug,
- Measuring the performance of a system under two
  different conditions due to imperfect knowledge of there
  performance characteristics,
- Checking the integrity of data, and
- Collecting statistics that may hint at the solution to difficult or hard-to-repeat bugs.

I don't think in this essay I can explain the design of experiments;
you will have to study and practice. However, I can offer two
bits of advice.

First, try to be very clear about your hypothesis, or the assertion
that you are trying to test. It also helps to write the hypothesis
down, especially if you find yourself confused or are working with
others.

You will often find yourself having to design a series of
experiments, each of which is based on the knowledge gained from
the last experiment. Therefore, you should design your experiments
to provide the most information possible. Unfortunately, this
is in tension with keeping each experiment simple---you will
have to develop this judgment through experience.

## Team Skills

### Why Estimation is Important

To get a working software system in active use as quickly as possible
requires not only planning the development,
but also planning the documentation,
deployment, marketing.
In a commercial project it also requires sales and finance.
Without predictability of the
development time, it is impossible to plan these effectively.

Good estimation provides predictability.
Managers love it,
as well they should. The fact that it is impossible, both
theoretically and practically, to predict accurately how long it
will take to develop software is often lost on managers.
We are
asked to do this impossible thing all the time, and we must face
up to it honestly. However, it would be dishonest not to admit
the impossibility of this task,
and when necessary, explain it. There is a lot of room for
miscommunication about estimates, as people have a startling
tendency to think wishfully that the sentence:

> I estimate that, if I really understand the problem, it
> is about 50% likely that we will be done in five weeks
> (if no one bothers us during that time).

really means:

> I promise to have it all done five weeks from now.

This common interpretation problem requires that you
explicitly discuss what the estimate means with
your boss or customer as if they were a simpleton.
Restate your assumptions, no matter how obvious they seem to you.

### How to Estimate Programming Time

Estimation takes practice. It also takes labor. It takes so
much labor it may be a good idea to estimate the time it will
take to make the estimate, especially if you are asked to
estimate something big.

When asked to provide an estimate of something big,
the most honest thing to
do is to stall.
Most engineers are enthusiastic and eager
to please, and stalling certainly will displease the stalled.
But an on-the-spot estimate probably won't be accurate and honest.

While stalling, it may be possible to consider doing or prototyping
the task. If political pressure permits, this is the most accurate
way of producing the estimate, and it makes real progress.

When not possible to take the time for
some investigation, you should first establish the meaning of the
estimate very clearly. Restate that meaning as the first and
last part of your written estimate. Prepare a written
estimate by deconstructing the task into progressively smaller
subtasks until each small task is no more than a day;
ideally at most in length.
The most important thing
is not to leave anything out. For instance, documentation,
testing, time for planning, time for communicating with other
groups, and vacation time are all very important. If you spend
part of each day dealing with knuckleheads, put a line item for
that in the estimate. This gives your boss visibility into what
is using up your time at a minimum, and might get you more time.

I know good engineers who pad estimates implicitly,
but I recommend that you do not. One of the results
of padding is trust in you may be depleted. For instance,
an engineer might estimate three days for a task that
she truly thinks will take one day. The engineer may
plan to spend two days documenting it, or two days working
on some other useful project. But it will be detectable
that the task was done in only one day (if it turns out that way),
and the appearance of slacking or overestimating is born.
It's far better to give proper visibility into what you are
actually doing. If documentation takes twice as long
as coding and the estimate says so, tremendous advantage
is gained by making this visible to the manager.

Pad explicitly instead. If a task will probably take one
day---but might take ten days if your approach doesn't
work---note this somehow in the estimate if you can; if not, at
least do an average weighted by your estimates of the probabilities.
Any risk factor that you can identify and assign an
estimate to should go into the schedule. One person is
unlikely to be sick in any given week. But a large
project with many engineers will have some sick time;
likewise vacation time. And what is the probability of
a mandatory company-wide training seminar? If it can
be estimated, stick it in.
There are of course, unknown unknowns, or  *unk-unks*.
Unk-unks by definition cannot be estimated individually.
You can try to create a global line item for all unk-unks,
or handle them in some other way that you communicate to your boss.
You cannot, however, let your boss forget that they exist, and it is
devilishly easy for an estimate to become a schedule without
the unk-unks considered.

In a team environment, you should try to have the
people who will do the work do the estimate, and you
should try to have team-wide consensus on estimates.
People vary widely in skill, experience, preparedness,
and confidence. Calamity strikes when a strong programmer
estimates for herself and then weak programmers are held
to this estimate.
The act of having the whole team agree
on a line-by-line basis to the estimate clarifies the team
understanding, as well as allowing the opportunity for
tactical reassignment of resources (for instance, shifting
burden away from weaker team members to stronger).

If there are big risks that cannot be evaluated, it is your
duty to state so forcefully enough that your manager does
not commit to them and then become embarrassed when the risk occurs.
Hopefully in such a case whatever is needed will be done to decrease the risk.

If you can convince your company to use  *Extreme Programming*, you
will only have to estimate relatively small things, and this is
both more fun and more productive.

### How to Find Out Information

The nature of what you need to know determines how you should find it.

If you need information *about concrete things* that are
objective and easy to verify, for example the latest
patch level of a software product, ask a large number of people
politely by searching the internet for it or by posting on
a discussion group.
Don't search on the internet for anything that smacks
of either opinion or subjective interpretation:
the ratio of drivel to truth is too high.

If you need *general knowledge about something subjective* the
history of what people have thought about it, go to the library
(the physical building in which books are stored). For example,
to learn about math or mushrooms or mysticism, go to the library.

If you need to know *how to do something that is not trivial* get two
or three books on the subject and read them. You might learn how
to do something trivial, like install a software package, from the
Internet. You can even learn important things, like good programming
technique, but you can easily spend more time searching and sorting
the results and attempting to divine the authority of the results than
it would take to read the pertinent part of a solid book.

If you need *information that no one else could be expected to know*
for example, ‘does this software that is brand new work on gigantic
data sets?’, you must still search the internet and the library.
After those options are completely exhausted, you may design
an experiment to ascertain it.

If you want an opinion or a value judgment that takes into account
some unique circumstance, talk to an expert.
For instance, if you want
to know whether or not it
is a good idea to build a modern database management system
in LISP, you should talk to a LISP expert and a database expert.

If you want to know *how likely it is* that a faster algorithm for
a particular application exists that has not yet been published,
talk to someone working in that field.

If you want to make a *personal decision that only you can make*
like whether or not you should start a business,
try putting into writing a list of arguments for and against the
idea. If that fails, consider divination.
Suppose you have studied the idea from all angles,
have done all your homework, and worked out all the consequences
and pros and cons in your mind, and yet still remain indecisive.
You now must follow your heart and tell your brain to shut up.
The multitude of available divination techniques are very useful
for determining your own semi-conscious desires, as they each present a complete
ambiguous and random pattern that your own subconscious will assign meaning to.

### How to Utilize People as Information Sources

Respect every person's time and balance it against your own.
Asking someone a question accomplishes far more than just
receiving the answer. The person learns about you, both by
enjoying your presence and hearing the particular question.
You learn about the person in the same way, and you may
learn the answer you seek. This is usually far more important than your question.

However, the value of this diminishes the more you do it.
You are, after all, using the most precious commodity
a person has: their time.
The benefits of communication
must be weighed against the costs. Furthermore, the
particular costs and benefits derived differ from person
to person. I strongly believe that an executive of 100
people should spend five minutes a month talking to each person
in her organization, which would be about 5%
of their time. But ten minutes might be too much, and five
minutes is too much if they have one thousand employees.
The amount of time you spend talking to each person in your
organization depends on their role (more than their position).
You should talk to your boss more than your boss's boss,
but you should talk to your boss's boss a little. It may
be uncomfortable, but I believe you have a duty to talk a
little bit to all your superiors, each month, no matter what.

The basic rule is that everyone benefits from talking to you a little bit,
and the more they talk to you, the less benefit they derive.
It is your job to provide them this benefit, and to get the benefit
of communicating with them, keeping the benefit in balance with the time spent.

It is important to respect your own time. If talking to
someone, even if it will cost them time, will save you a
great deal of time, then you should do it unless you think
their time is more valuable than yours, to the tribe, by that factor.

A strange example of this is the summer intern. A summer
intern in a highly technical position can't be expected
to accomplish too much; they can be expected to pester the
hell out of everybody there. So why is this tolerated?
Because the pestered are receiving something important from the intern.
They get a chance to showoff a little. They get a chance to hear
some new ideas, maybe; they get a chance to see things from
a different perspective. They may also be trying to recruit
the intern, but even if this is not the case there is much to gain.

You should ask people for a little bit of their wisdom and
judgment whenever you honestly believe they have something to say.
This flatters them and you will learn something and teach them
something. A good programmer does not often need the advice of
a Vice President of Sales, but if you ever do,
you be sure to ask for it. I once asked to listen in on a few sales
calls to better understand the job of our sales staff.
This took no more than 30 minutes but I think that small effort made
an impression on the sales force.

### How to Document Wisely

Life is too short to write crap nobody will read;
if you write crap,
nobody will read it.
Therefore a little good documentation is best.
Managers often don't understand this,
because even bad documentation gives them a false sense of security
that they are not dependent on their programmers.
If someone absolutely insists that you write truly useless
documentation, say ``yes'' and quietly begin looking for a better job.

There's nothing quite as effective as putting an accurate estimate
of the amount of time it will take to produce good documentation
into an estimate to slacken the demand for documentation.
The truth is cold and hard: documentation, like testing,
can take many times longer than developing code.

Writing good documentation is, first of all, good writing.
I suggest you find books on writing, study them, and practice.
But even if you are a lousy writer or have poor command of the
language in which you must document, the Golden Rule is all you really need:
``Do unto others as you would have them do unto you.''
Take time to really think about who will be reading your
documentation, what they need to get out of it, and how you
can teach that to them. If you do that, you will be an above
average documentation writer, and a good programmer.

When it comes to actually documenting code itself, as opposed
to producing documents that can actually be read by non-programmers,
the best programmers I've ever known hold a universal sentiment:
write self-explanatory code and only document code in
the places that you cannot make it clear by writing the code itself.
There are two good reasons for this.
First, anyone who needs to see code-level documentation
will in most cases be able to and prefer to read the code anyway.
Admittedly, this seems easier to the experienced programmer than
to the beginner.
More importantly however, is that the code
and the documentation cannot be inconsistent if there is no documentation.
The source code can at worst be wrong and confusing.
The documentation, if not written perfectly, can lie, and that is a thousand times worse.

This does not make it easier on the responsible programmer.
How does one write self-explanatory code? What does that even mean? It means:

- Writing code knowing that someone will have to read it;
- Applying the golden rule;
- Choosing a solution that is straightforward,
  even if you could get by with another solution faster;
- Sacrificing small optimizations that obfuscate the code;
- Thinking about the reader and spending some of your precious time to make it easier on her; and
- Not ever using a function name like ``foo'',``bar'', or ``doIt''!

### How to Work with Poor Code

It is very common to have to work with poor quality code
that someone else has written. Don't think too poorly of them,
however, until you have walked in their shoes. They may
have been asked very consciously to get something done
quickly to meet schedule pressure. Regardless, in order to work
with unclear code you must understand it. To understand it
takes learning time, and that time will have to come out
of some schedule, somewhere, and you must insist on it.
To understand it, you will have to read the source code.
You will probably have to experiment with it.

This is a good time to document, even if it is only for yourself,
because the act of trying to document the code will force you
to consider angles you might not have considered, and the
resulting document may be useful. While you're doing this,
consider what it would take to rewrite some or all of the code.
Would it actually save time to rewrite some of it?
Could you trust it better if you rewrote it?
Be careful of arrogance here. If you rewrite it,
it will be easier for you to deal with, but will it
really be easier for the next person who has to read it?
If you rewrite it, what will the test burden be?
Will the need to re-test it outweigh any benefits that might be gained?

In any estimate that you make for work against code you didn't
write, the quality of that code should affect your
perception of the risk of problems and unk-unks.

It is important to remember that abstraction and encapsulation,
two of a programmer's best tools, are particularly applicable
to lousy code. You may not be able to redesign a large block
of code, but if you can add a certain amount of abstraction to
it you can obtain some of the benefits of a good design without
reworking the whole mess. In particular, you can try to wall off
the parts that are particularly bad so that they may be redesigned
independently.

### How to Use Source Code Control

Source code control systems let you manage projects effectively.
They're very useful for one person and essential for a group.
They track all changes in different versions so that no code is
ever lost and meaning can be assigned to changes.
One can create throw-away and debugging code with confidence
with a source code control system, since the code you modify
is kept carefully separate from committed, official code that
will be shared with the team or released.

I was late to appreciate the benefits of source code control
systems but now
I wouldn't live without one even on a one-person project.
Generally they are necessary when you have team working on the same code base.
However, they have another great advantage: they encourage thinking about
the code as a growing, organic system.
Since each change is marked as a
new revision with a new name or number, one begins to think of the
software as a visibly progressive series of improvements.
I think this is especially useful for beginners.

A good technique for using a source code control system is to stay
within a few days of being up-to-date at all time.
Code that can't be finished in a few days is checked in,
but in a way that it is inactive and will not be called,
and therefore not create any problems for anybody else.
Committing a mistake that slows down your teammates is
a serious error; it is often taboo.

### How to Unit Test

Unit testing, the testing of an individual piece of coded
functionality by the team that wrote it, is a part of coding,
not something different from it. Part of designing
the code is designing how it will be tested.
You should write down a test plan, even if it is
only one sentence. Sometimes the test will be simple:
``Does the button look good?'' Sometimes it will be complex:
``Did this matching algorithm return precisely the correct matches?''

Use assertion checking and test drivers whenever possible.
This not only catches bugs early, but is very useful later
on and lets you eliminate mysteries that you would otherwise have to worry about.

The Extreme Programming developers are writing extensively on
unit testing effectively; I can do no better than to recommend their
writings.

### Take Breaks when Stumped

When stumped, take a break. I sometimes meditate
for 15 minutes when stumped and the problem magically
unravels when I come back to it. A night's sleep
sometimes does the same thing on a larger scale.
It's possible that temporarily switching to any
other activity may work.

### How to Recognize When to Go Home

Computer programming is an activity that is also a culture.
The unfortunate fact is that it is not a culture that values
mental or physical health very much.
For both cultural/historical reasons (the need to work at
night on unloaded computers, for example) and because of
overwhelming time-to-market pressure and the scarcity of
programmers, computer programmers are traditionally overworked.
I don't think you can trust all the stories you hear, but
I think 60 hours a week is common, and 50 is pretty
much a minimum. This means that often much more than that is required.
This is serious problem for a good programmer, who is responsible not
only for themselves but their teammates as well.
You have to recognize when to
go home, and sometimes when to suggest that other people go home.
There can't be any fixed rules for solving this problem, anymore
than there can be fixed rules for raising a child,
for the same reason---every human being is different.

Beyond 60 hours a week is an extraordinary effort for me, which
I can apply for short periods of time (about one week), and
that is sometimes expected of me.
I don't know if it is fair
to expect 60 hours of work from a person;
I don't even know if 40 is fair.
I am sure, however, that it is stupid to work so much
that you are getting little out of that extra hour you work.
For me personally, that's any more than 60 hours a week.
I personally think a programmer should exercise noblesse oblige
and shoulder a heavy burden.
However, it is not a programmer's
duty to be a patsy.
The sad fact is programmers *are* often asked to be patsies in order
to put on a show for somebody, for example a manager trying to
impress an executive.
Programmers often succumb to this because they are
eager to please and not very good at saying no.
There are four defenses against this:

- Communicate as much as possible with everyone in the company so that
  no one can mislead the executives about what is going on,
- Learn to estimate and schedule defensively and explicitly and give
  everyone visibility into what the schedule is and where it stands,
- Learn to say no, and say no as a team when necessary, and
- Quit if you have to.

Most programmers are good programmers, and good programmers
want to get a lot done. To do that, they have to manage
their time effectively. There is a certain amount of
mental inertia associated with getting warmed-up to a
problem and deeply involved in it. Many programmers find
they work best when they have long, uninterrupted blocks of
time in which to get warmed-up and concentrate.
However, people must sleep and perform other duties.
Each person needs to find a way to satisfy both their human
rhythm and their work rhythm. Each programmer needs to do
whatever it takes to procure efficient work periods, such
as reserving certain days in which you will attend only the most critical
meetings.

Since I have children, I try to spend evenings with them sometimes.
The rhythm that works best for me is to work a very long day,
sleep in the office or near the office (I have a long commute
from home to work) then go home early enough the next day to spend
time with my children before they go to bed. I am not comfortable
with this, but it is the best compromise I have been able to work out.
Go home if you have a contagious disease. You should go home if
you are thinking suicidal thoughts. You should take a break
or go home if you think homicidal thoughts for more than a
few seconds. You should send someone home if they show
serious mental malfunctioning or signs of mental illness
beyond mild depression. If you are tempted to be
dishonest or deceptive in a way that you normally are not
due to fatigue, you should take a break. Don't use cocaine
or amphetamines to combat fatigue. Don't abuse caffeine.

### How to Deal with Difficult People

You will probably have to deal with difficult people.
You may even be a difficult person yourself.
If you are the kind of person who
has a lot of conflicts with coworkers and authority figures,
you should cherish the independence this implies,
but work on your interpersonal skills without sacrificing your intelligence or principles.

This can be very disturbing to some programmers who
have no experience in this sort of thing and whose previous
life experience has taught them patterns of behavior that
are not useful in the workplace.
Difficult people are
often inured to disagreement and they are less affected
by social pressure to compromise than others.
The key is to respect them appropriately,
which is more than you will want to but not as much as they might want.

Programmers have to work together as a team.
When disagreement arises, it must be resolved somehow,
it cannot be ducked for long. Difficult people
are often extremely intelligent and have something very useful to say.
It is critical that you listen and understand the difficult
person without prejudice caused by the person.
A failure to communicate is often the basis of disagreement
but it can sometimes be removed with great patience.
Try to keep this communication cool and cordial, and don't
accept any baits for greater conflict that may be offered.
After a reasonable period of trying to understand, make a decision.

Don't let a bully force you to do something you don't agree with.
If you are the leader, do what you think is best.
Don't make a decision for any personal reasons, and be prepared
to explain the reasons for your decision. If you are a teammate
with a difficult person, don't let the leader's decision have any
personal impact. If it doesn't go your way,
do it the other way whole-heartedly.

Difficult people do change and improve.
I've seen it with my own eyes, but it is very rare.
However, everyone has transitory ups and downs.

One of the challenges that every programmer but especially
leaders face is keeping the difficult person fully engaged.
They are more prone to duck work and resist passively than others.
