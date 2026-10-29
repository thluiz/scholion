---
url: "https://en.wikipedia.org/wiki/The_Mythical_Man-Month#The_second-system_effect"
captured_at: "2015-09-21T16:01:56-03:00"
title: "The Mythical Man-Month - Wikipedia, the free encyclopedia"
domain: "en-wikipedia-org"
---

# Wikipedia, the free encyclopedia

### The mythical man-month

See also: [Combinatorial explosion](https://en.m.wikipedia.org/wiki/Combinatorial_explosion "Combinatorial explosion")

Brooks discusses several causes of scheduling failures. The most enduring is his discussion of [Brooks's law](https://en.m.wikipedia.org/wiki/Brooks%27s_law "Brooks's law"): *Adding manpower to a late software project makes it later*. [Man-month](https://en.m.wikipedia.org/wiki/Man-month "Man-month") is a hypothetical unit of work representing the work done by one person in one month; Brooks's law says that the possibility of measuring useful work in man-months is a myth, and is hence the centerpiece of the book.

Complex programming projects cannot be perfectly partitioned into discrete tasks that can be worked on without communication between the workers and without establishing a set of complex interrelationships between tasks and the workers performing them.

Therefore, assigning more programmers to a project running behind schedule will make it even later. This is because the time required for the new programmers to learn about the project and the increased communication overhead will consume an ever increasing quantity of the calendar time available. When *n* people have to communicate among themselves, as *n* increases, their output decreases and when it becomes negative the project is delayed further with every person added.

- Group intercommunication formula: *n*(*n* − 1) / 2
- Example: 50 developers give 50 · (50 – 1) / 2 = 1225 channels of communication.

### No silver bullet

Main article: [No Silver Bullet](https://en.m.wikipedia.org/wiki/No_Silver_Bullet "No Silver Bullet")

Brooks added *"No Silver Bullet — Essence and Accidents of Software Engineering"*—and further reflections on it, *"'No Silver Bullet' Refired"*—to the anniversary edition of *The Mythical Man-Month*.

Brooks insists that there is no one [silver bullet](https://en.m.wikipedia.org/wiki/Silver_bullet "Silver bullet") -- "there is no single development, in either technology or management technique, which by itself promises even one [order of magnitude](https://en.m.wikipedia.org/wiki/Order_of_magnitude "Order of magnitude") [tenfold] improvement within a decade in productivity, in reliability, in simplicity."

The argument relies on the distinction between [accidental complexity](https://en.m.wikipedia.org/wiki/Accidental_complexity "Accidental complexity") and [essential complexity](https://en.m.wikipedia.org/wiki/Essential_complexity "Essential complexity"), similar to the way [Amdahl's law](https://en.m.wikipedia.org/wiki/Amdahl%27s_law "Amdahl's law") relies on the distinction between "strictly serial" and "parallelizable".

### The second-system effect

The second-system effect proposes that, when an architect designs a second system, it is the most dangerous system they will ever design, because they will tend to incorporate all of the additions they originally did not add to the first system due to inherent time constraints. Thus, when embarking on a second system, an engineer should be mindful that they are susceptible to over-engineering it.

### The tendency towards irreducible number of errors

The author makes the observation that in a suitably complex system there is a certain irreducible number of errors. Any attempt to fix observed errors tends to result in the introduction of other errors.

### Progress tracking

Brooks wrote "Question: How does a large software project get to be one year late? Answer: One day at a time!" Incremental slippages on many fronts eventually accumulate to produce a large overall delay. Continued attention to meeting small individual milestones is required at each level of management.

### Conceptual integrity

To make a user-friendly system, the system must have conceptual integrity, which can only be achieved by separating architecture from implementation. A single chief architect (or a small number of architects), acting on the user's behalf, decides what goes in the system and what stays out. The architect or team of architects should develop an idea of what the system should do and make sure that this vision is understood by the rest of the team. A novel idea by someone may not be included if it does not fit seamlessly with the overall system design. In fact, to ensure a user-friendly system, a system may deliberately provide *fewer* features than it is capable of. The point is that, if a system is too complicated to use, then many of its features will go unused because no one has the time to learn how to use them.

### The manual

The chief architect produces a manual of system specifications. It should describe the external specifications of the system in detail, *i.e.*, everything that the user sees. The manual should be altered as feedback comes in from the implementation teams and the users.

### The pilot system

When designing a new kind of system, a team *will* design a throw-away system (whether it intends to or not). This system acts as a "pilot plant" that reveals techniques that will subsequently cause a complete redesign of the system. This second, *smarter* system should be the one delivered to the customer, since delivery of the pilot system would cause nothing but agony to the customer, and possibly ruin the system's reputation and maybe even the company.

### Formal documents

Every project manager should create a small core set of formal documents defining the project objectives, how they are to be achieved, who is going to achieve them, when they are going to be achieved, and how much they are going to cost. These documents may also reveal inconsistencies that are otherwise hard to see.

### Project estimation

When estimating project times, it should be remembered that programming products (which can be sold to paying customers) and programming systems are both three times as hard to write as simple independent in-house programs.[3](https://en.m.wikipedia.org/wiki/Second-system_effect#cite_note-3) It should be kept in mind how much of the work week will actually be spent on technical issues, as opposed to administrative or other non-technical tasks, such as meetings, and especially "stand-up" or "all-hands" meetings.

### Communication

To avoid disaster, all the teams working on a project should remain in contact with each other in as many ways as possible—e-mail, phone, meetings, memos etc. Instead of assuming something, implementers should ask the architect(s) to clarify their intent on a feature they are implementing, before proceeding with an assumption that might very well be completely incorrect. The architect(s) are responsible for formulating a group picture of the project and communicating it to others.

### The surgical team

Much as a surgical team during surgery is led by one surgeon performing the most critical work, while directing the team to assist with less critical parts, it seems reasonable to have a "good" programmer develop critical system components while the rest of a team provides what is needed at the right time. Additionally, Brooks muses that "good" programmers are generally five to ten times as productive as mediocre ones.

### Code freeze and system versioning

Software is invisible. Therefore, many things only become apparent once a certain amount of work has been done on a new system, allowing a user to experience it. This experience will yield insights, which will change a user's needs or the perception of the user's needs. The system should, therefore, be changed to fulfill the changed requirements of the user. This can only occur up to a certain point, otherwise the system may never be completed. At a certain date, no more changes should be allowed to the system and the code should be frozen. All requests for changes should be delayed until the *next* version of the system.

### Specialized tools

Instead of every programmer having his own special set of tools, each team should have a designated tool-maker who may create tools that are highly customized for the job that team is doing, *e.g.*, a code generator tool that creates code based on a specification. In addition, system-wide tools should be built by a common tools team, overseen by the project manager.

### Lowering software development costs

There are two techniques for lowering software development costs that Brooks writes about:

- Implementers may be hired only after the architecture of the system has been completed (a step that may take several months, during which time prematurely hired implementers may have nothing to do).
- Another technique Brooks mentions is not to develop software at all, but simply to buy it "[off the shelf](https://en.m.wikipedia.org/wiki/Commercial_software "Commercial software")" when possible.
