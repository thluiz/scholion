---
url: "https://almad.blog/essays/no-bugs-just-todos"
captured_at: "2026-11-16T03:49:06+00:00"
title: "There Are No Bugs, Just TODOs"
domain: "almad-blog"
---

One of my life’s traumas is the bug trackers, the issue trackers, the project management tools. The toolset that completes the version control log to form the development equivalent of [double-entry bookkeeping](https://en.wikipedia.org/wiki/Double-entry_bookkeeping).

As with its accounting equivalent, those tools are actually useful indeed. While we collectively learned to avoid the CEO MBAs that run a company only based on its accounting books and disregard the underlying business, I think we haven’t learned to avoid managers who only run software development through tickets and disregard the underlying software delivery.

Issue tracking became an industry, its software gained consciousness and started becoming a social network, apparently optimizing engagement and time spent in a product as opposed to helping you get things done. This is often coupled with people whose job security is tied to making sure projects are complicated enough to require a project manager[1](#fn:1) to run them and the amount of resulting paperwork is mind-boggling. The wide-spread acceptance of this state is what brought Jira creators public.

I can’t disprove the existence of reasonably-configured and fast Jira, but I am yet to experience it—and I’ve been trying hard. In one of my jobs, we pushed Trello[2](#fn:2) to the limits and in response, the corporate veterans were pushing for Jira hard. I’ve been ensured the product is now a completely different thing I remember. Well, few months (and some well-paid, fine-tuned configurations) later, I saw the same turn-based accounting strategy that I remembered.

This is not to blame any particular product, but rather what people ask from it.

## The Minimal Skeleton

I think there are relatively few properties that are needed in an issue and relatively few rules to make the handling efficient.

### Ownership

Critically, the issue needs to find its way to someone who can get it done. This is usually done by putting it to the correct board, but can be tricky in larger companies and often needs a reliable triage by someone from within engineering.

This is _not_ a “component” attribute that I passionately dislike. If “components” are created by engineers, they are often arbitrary, they don’t survive refactoring and can lead to dilution of responsibilities over time. If they are created by product owners, they correspond to customer perception and not necessarily to the internal structure, and the translation layer is needed. [3](#fn:3)

Assign to a single person[4](#fn:4). If you don’t know who that is, there should be no owner and there should be a clearly assigned person (we used current oncall agent) to process them and assign accordingly.

### Position In a Queue

This is the single most important thing for a project organization. **Every team must have a single ordered queue of tasks**. A lot of project management chaos arises when an engineer has multiple queues to pick from.

It happens often and in opaque form. Of course noone intentionally scatters tasks around. But in practice, there is planning that assigns tickets in priority buckets (like high, medium, low) with unclear sorting inside them. Then a high-priority customer ticket comes in. Then there is an incident. And then we have the internal bug tracker, but also a list of Github issues, and we decided to do both at once. Also, I just got an email from our marketing guy about a typo on our page. Does this paragraph feel confusing? Exactly!

Have a way to put all of those into a single place and make sure _every single one of them is prioritized relatively_. When sitting down to computer and achieving flow, there should be one top item just looking at them to pick up.

If the flow is more complicated, there should be an algorithm that everybody should agree on. An example may be:

1.  If there is downtime, it’s the top priority of everyone affected
2.  If there is an incident, it’s the top priority for an on-call agent
3.  My deployed issue waiting for my verification
4.  Reviewed pull request waiting for deployment
5.  My pull request with completed code review that requested changes
6.  Outstanding pull request waiting for code review
7.  Customer escalation received through email. For valid ones, create incident and delegate to on-call. For invalid ones, reply, apologize and provide customer support link
8.  Top issue in the sprint backlogs
9.  Any issue in the “when engineers have time” backlog

### State

This is where things go ugly. The possible ticket states are often designed by architects and not by people who are actually going to use the thing. I’ve seen a map of issue state transitions that definitely looked Turing-complete.

I advise to start with the “Todo”, “Doing” and “Done” triad and only add more if absolutely required. Moving issues from one state to another needs to be associated with an explicit action. If you add more states, make sure that you have an explicit agreement with everyone that the _latest-stage ticket has the highest priority_ unless you want to get all tickets stuck in the most boring stage, such as “verification”.

### Task Breakdown

Every ticket with a state should correspond to a single deployment (which is not large in the continuous delivery environment). If it’s larger, it should be broken down into a sub ticket and the relationship between those two should be recorded.

## The Anti-Patterns

That’s it. If you really scale, you may need a few more…but fewer than you think. While the following attributes are common, they most definitely shouldn’t.

### Priority

**There is no absolute priority of an issue, only a relative priority to other issues**. Once you start assigning priorities from a list, anything else than “Highest” is a passive-aggressive[5](#fn:5) way of saying “No”.

If priority is just an attributed with a list of values, it becomes the most abused field very quickly. Sooner or later, you will also start adding additional “really highest highest immediate” priorities, also known as “CEO called”.

Resist the temptation.

### Ticket Type

The type is usually a list that contains values like “Enhancement”, “Bug”, “Task” and “Documentation”. My question would be: why do you want to have this information and what is it going to be used for?

The “Type” field led to one of the most unproductive discussions of my life. The “it’s not a bug, it’s a feature” saying means I am probably not alone. **We collectively shouldn’t care**. When people scream “this is a bug”, it is irrelevant what it is caused by. It is a scream of a significant expectation mismatch. The team should work on resolving it, regardless of whether it was caused by a developer diverging from the designed intent or because of the original intent going wrong.

The most significant pushes for this field I have experienced from:

*   Perfectionists who like to procrastinate by sorting things While I support everyone in having hobbies, it is unfortunate if the team suffers because of it. Find a way to agree on the usefulness and help the perfectionists manage the imperfections. I recommend buying them a portable zen garden to compensate.
    
*   Top-level managers who like pie charts. This is often to compare the quality of the teams by comparing the number of defects they create. The only thing that remains is to tie your bonuses to it and you can make “this is a feature, not a bug” saying your official company anthem[6](#fn:6). In a less dysfunctional and more valid case, it is to estimate “how much effort we are burning for upkeep versus developing new things”, which I find valid in certain circumstances—but then “upkeep” and “new” should be the ticket types.
    
*   Customers. “Bug” is used to mean either “high priority” or “your fault, fix it and don’t even try to bill us”.
    

Whenever the push comes, pay attention and dig out the actual root cause for the request which is better resolved by other means.

### Software Version

Tracking the version makes sense for shipped libraries and on-premise packages. It makes no sense for continuously delivered SaaS.

For assessing whether the bugreport still makes sense, the reporting date is usually enough.

### Severity

Severity begs to be perceived as equal to a priority. But severity is very different for different roles and its priority is always a decision on relative priorities that take laboriousness into account.

Consider a typo in a text on a page. How do you handle it when it’s in the middle of the page? When it’s in the main call to action on a landing page? When it’s fixed trivially and when does it require five-person approval and an access to a 3^rd^ party system?

This is usually duplicate to priority.

### The Ticket Swamp

The most challenging thing is to have an issue hygiene. Saying “no” is hard, but without it, the issue system becomes an unmanageable mess. **The system should be designed to encourage closing issues aggressively and easily**. This is ultimately the appeal of Kanban boards: the goal to have is the lowest time possible for an issue to be open and to provide an incentive to prune the queue aggressively.

Otherwise the amount of tickets becomes unmanageable and starts to resemble a swamp. You carefully walk in only to be sucked, never to resurface again.

One way to recover is to automatically close tickets after a certain period of time. This may be a subtle way of saying “no”, but I think it has its place, especially if we are talking about public trackers.

There is one good argument in its favor: the software continuously changes and hence old issues may be invalid. In order to put them into a sprint, they need to be checked—in some cases, that’s actually more work than the issue itself.

Giving up is a reasonable response in order to keep having _a tracker_ instead of _a database_.

## The Separation of Internal Support

In order for this to work, there needs to be a separate system for handling questions for the development team from the rest of the company[7](#fn:7).

This is crucial for communication culture. What I’ve seen as an alternative is to write a message to a random engineer or their team lead, which leads to abuse. It’s important to make that channel more responsive and reliable than any other individual inbox.

The other alternative is to open badly-specified development tickets. This road leads to a swamp. It’s easy to overpower the team’s ability to triage all tickets, at which point the whole queue is going to be ignored and you have Ticket Swamp on steroids.

_Thanks to Steven Mizell for editing and feedback._

## Responses

*   Translations available: [Russian](https://web.archive.org/web/20200801092406/https://howtorecover.me/net-oshibok-prosto-todo)
*   There is a surprisingly decent [discussion at Hacker’s News](https://news.ycombinator.com/item?id=23428398) and [even reddit](https://www.reddit.com/r/programming/comments/gx7sdf/there_are_no_bugs_just_todos/)

## Other resources

*   Basecamp crew released the [shape up methodology](https://basecamp.com/shapeup) that may resonate with you
*   Although the name may confuse you, approach outlined in this article is very consistent with [the Zero Bugs policy](https://www.xolv.io/blog/zero-bug-software-development/)

* * *

1.  For the record, I actually worked with an _excellent_ project manager once. His defining trait was an understanding that he is the oil that makes the wheels whirl, not the largest and the most important wheel in the center. This of course made him one of the most respected colleagues. I had troubles repeating this memorable experience. On a more serious note, I’ve been asked to back this up and sure, all I can do is anecdotal evidence. Yet I do believe this is actually a property of _any_ job position: people rarely want their job to disappear. The moment you create a job position, it tends to metastasize. Create a dedicated $technology ninja position and observe [↩︎](#fnref:1)
    
2.  Basically an equivalent of a whiteboard for post-its with vertical lanes [↩︎](#fnref:2)
    
3.  They should ideally match, yet they often deviate long term [↩︎](#fnref:3)
    
4.  For larger teams, that can be a team account, but in that case, it is team leader responsibility to go through all team owned tickets regularly and delegate them [↩︎](#fnref:4)
    
5.  In US English, this is called “polite” [↩︎](#fnref:5)
    
6.  Seems absurd? Well, I’ve also seen “story points are abstract, specific to the team and incomparable, so let’s put the burndown charts of all teams on this single large display in the hallway, you know, _obviously only_ to let teams know how they are standing, no other hidden agenda implied” totally [↩︎](#fnref:6)
    
7.  Even Jira creators acknowledge that need, hence Jira-SD [↩︎](#fnref:7)
