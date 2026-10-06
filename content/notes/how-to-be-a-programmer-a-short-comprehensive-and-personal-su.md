---
title: "How to be a Programmer: A Short, Comprehensive, and Personal Summary"
date: '2012-06-04T12:07:10-03:00'
category: webclip
summary: 'The chapter argues that programmers need strong debugging, performance, documentation, estimation, and teamwork habits, and that all of them depend on experimentation, judgment, and clear communication.'
tags: ["programming", "debugging", "teamwork", "estimation"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to be a Programmer: A Short, Comprehensive, and Personal Summary"
    url: "http://samizdat.mines.edu/howto/HowToBeAProgrammer.html"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-06/samizdat-mines-edu--how-to-be-a-programmer-a-short-comprehensive-and-personal-su.md"
    kind: repo
---

The chapter presents programming as practical work that depends on careful observation, small experiments, and steady judgment. It treats debugging as central, then extends the same mindset to performance, memory, intermittent bugs, and difficult code, always stressing that the programmer must understand what is actually happening in a running system.

## Reading notes

- Debugging is the cornerstone of being a programmer, and the key meaning here is seeing into program execution by examining it.
- The main ways to inspect an executing program are debugging tools, printlining, and logging.
- Beginners should not fear modifying code for debugging; experimentation is part of the work.
- Divide and conquer helps debugging by shrinking the mystery step by step.
- Fix bugs with the smallest change possible, and change one thing at a time when you can.
- Logs are valuable for hard-to-reproduce bugs, performance data, and configurable debugging in production.
- Performance work starts with a mental model built from profiling or logs, and often the biggest costs are in I/O.
- Bottleneck analysis matters more than small local optimizations, and major gains usually come from focusing on the expensive parts first.
- Loop optimization should begin by asking whether the loop can be removed entirely.
- I/O can often be improved through caching, better representation, or moving computation closer to the data.
- Memory must be managed carefully, since garbage collection helps but does not prevent leaks or unnecessary object creation.
- Intermittent bugs require recording conditions, reproducing the problem if possible, and improving logging when necessary.
- Design skills grow through mentoring, study, and doing small projects before larger ones.
- Programming often requires experimentation, even if theory should not depend on it.
- Good estimation gives predictability, but estimates must be stated with clear assumptions and risk factors.
- Useful estimates break work into small tasks and include testing, documentation, communication, vacation, and other real costs.
- Information should be sought from the right source: internet, library, books, experts, experiments, or people.
- People are information sources, but their time is limited and must be respected.
- Good documentation is focused, readable, and aimed at the reader; code should be self-explanatory whenever possible.
- Poor code still has to be understood, often through reading, experimenting, documenting, and sometimes adding abstraction around it.
- Source code control makes change safer and helps teams stay close to current work.
- Unit tests, assertion checks, and test drivers are part of coding, not separate from it.
- When stuck, taking a break can help.
- Programmers need to notice when work is becoming unhealthy and when to go home.
- Difficult people must be handled with respect, patience, and clear decisions, without letting conflict become personal.
