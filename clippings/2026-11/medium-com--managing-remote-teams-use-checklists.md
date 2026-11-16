---
url: "https://medium.com/javascript-scene/managing-remote-teams-use-checklists-301aae93e7a5"
captured_at: "2026-11-16T06:16:58+00:00"
title: "Managing Remote Teams — Use Checklists | by Eric Elliott | JavaScript Scene | Medium"
domain: "medium-com"
---

Managing Remote Teams — Use Checklists
Eric Elliott
5 min read
·
Mar 25, 2020

Image- Smoke Art Cubes to Smoke — MattysFlicks — (CC BY 2.0)

On remote teams, conveying team norms is a different process from in the office. Office workers can usually stroll to another desk and ask somebody a question whenever one comes up. On remote teams, your team members may work at different times, or be busy with family errands in the middle of the workday (and that’s OK — people should work when they can be most productive).

So how should remote workers communicate the team’s practices and procedures when they can’t just shout, “Hey, how do we do code reviews around here?”

Checklists.

I’ve been using checklists for years. In software development we have many of them, like the SOLID principles on object-oriented design.

But it wasn’t until I read “The Checklist Manifesto” that I realized the true power of checklists, and started making them standard operating procedures on my software teams.

The book describes a study which is particularly relevant today, because as I type this, the world is suffering from the worst global disaster since World War II: The COVID-19 pandemic. The study was conducted by Stephan Luby with support from Proctor & Gamble to test the effectiveness of anti-bacterial soap, and it delivered incredible results: The incidence of various diseases fell 35% — 52%.

But what’s really interesting about this study is that the kind of soap that was used didn’t make a big difference, and the people already had and used soap. The difference was that the study instructions included two checklists — When to wash hands:

Before preparing food or feeding it to others
After sneezing our coughing
After wiping an infant
After using a bathroom

Most people were already washing their hands after using a bathroom, but they weren’t doing it properly. The checklist also included instructions:

Use soap.
Wet both hands completely.
Rub the soap until it forms a thick lather covering both hands completely.
Wash hands for at least 20 seconds [not included in this study, but we know now it takes at least 20 seconds to break down viral bugs including Coronavirus so I’m putting it here for posterity].
Completely rinse the soap off.

It was not the particular soap used — any soap is effective. It was the checklists that prevented illness. The checklists changed behaviors and taught people how and when to properly wash their hands.

If you talk to members of my teams, you’ll discover that we create checklists for lots of things. The best checklists are:

[ ] Short enough to memorize
[ ] Only include the key points

If they get too long, conformance to the checklist drops, as people begin to see checklist points as optional suggestions.

Here are some real examples of the checklists we commonly use on our teams. A few of these (like FIRST and RAIL) are widely used and developed externally. Several others (including 5 Questions, RITE Way, Test Timing, and both CI/CD lists) were developed by me, but inspired by common industry best practices:

Code Review Checklist

Before merging a pull request, check that the following have been considered:

[ ] Related issue is linked
[ ] Meets all of the stated functional requirements
[ ] Demo video
[ ] PR is small enough (otherwise, break it up)
[ ] Code is behind the appropriate feature toggle
[ ] Code is readable
[ ] Code is tested
[ ] The features are documented
[ ] Files are located and named correctly
[ ] Error states are properly handled
Code Test Checklist (RITE Way)

In quality software, developers must deliver tests which automatically prove that the code works. To test the RITE Way, each test should be:

[ ] Readable
[ ] Isolated (units and tests)/Integrated (for integration tests)
[ ] Thorough
[ ] Explicit
Test Timing Checklist
[ ] Unit tests run in under 10 seconds
[ ] Functional tests should run in under 10 minutes
[ ] CI/CD checks should run in under 10 minutes
5 Questions Every Unit Test Should Answer
[ ] What is the component under test?
[ ] What is its expected behavior (in human readable form)?
[ ] What is its actual output?
[ ] What is its expected output?
[ ] How do you reproduce a test failure? (Double check that the answers to the above answer this question).

Which is unsurprisingly similar to the bug report checklist, because all failing unit tests should be good bug reports.

Bug Report Checklist

Each bug report should include:

[ ] Description (including location)
[ ] Expected output
[ ] Actual output
[ ] Instructions to reproduce
[ ] Environment (browser/OS versions, extensions)
[ ] Bonus: Screenshot/screencast demonstrating the bug
Component Checklist (FIRST)

Components should follow the FIRST principles:

[ ] Focused
[ ] Independent
[ ] Reusable
[ ] Small
[ ] Testable
Software User Interface (UI) Performance Checklist (RAIL)

Software UIs should conform to the RAIL performance model:

[ ] Respond to user interaction in under 100ms
[ ] Animation frames should draw in under 10ms
[ ] Idle time processes should be batched in blocks of less than 50ms
[ ] Load in under 1 second
Continuous Delivery Preparedness Checklist
[ ] A minimum of 80% of the code is covered by unit tests.
[ ] All critical user workflows are covered by functional tests.
[ ] All critical integrations are covered by integration tests.
[ ] A feature toggle system exists to toggle features on and off in the production environment. All unfinished features are toggled off by default.
CI/CD Checklist
[ ] Each commit to master must first pass through a Pull Request (PR) process. Merging must be blocked until checks pass.
[ ] Each pull request must be peer reviewed before merging into the master branch.
[ ] Each pull request must pass a full suite of automated tests configured to stop the integration process if any tests fail.
[ ] Each commit triggers its own sandboxed build for testing, demonstration and verification. The build link is added to the code review data.
[ ] After all checks pass, merging is unblocked.
[ ] The author of the pull request must OK the merge (or be personally responsible for merge).
[ ] Merging should trigger automatic production deployment of the newly integrated code. Hence, the master branch should always reflect the production product build.

Eric Elliott is the author of the books, “Composing Software” and “Programming JavaScript Applications”. As co-founder of EricElliottJS.com and DevAnywhere.io, he teaches developers essential software development skills. He builds and advises development teams for crypto projects, and has contributed to software experiences for Adobe Systems, Zumba Fitness, The Wall Street Journal, ESPN, BBC, and top recording artists including Usher, Frank Ocean, Metallica, and many more.

He enjoys a remote lifestyle with the most beautiful woman in the world.
