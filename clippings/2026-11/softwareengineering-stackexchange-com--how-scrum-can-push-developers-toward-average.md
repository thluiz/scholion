---
url: "https://softwareengineering.stackexchange.com/questions/410482/how-do-i-prevent-scrum-from-turning-great-developers-into-average-developers"
captured_at: "2026-11-16T05:30:38+00:00"
title: "management - How do I prevent Scrum from turning great developers into average developers? - Software Engineering Stack Exchange"
domain: "softwareengineering-stackexchange-com"
---

I found this also happened in my team although he may have exaggerated the situation a little bit.

Scrum is a way to take a below average or poor developer and turn them into an average developer. It's also great at taking great developers and turning them into average developers.

Everyone just wants to take something easy off the board that you can get done in a day so you have something to report in tomorrow's daily scrum. It's just everyone trying to pick the low hanging fruit. There's no incentive to be smart and to take time to think about solutions, if nothing is moving across what are you even doing? You're letting the team down! The velocity is falling!

I think if you have hard problems to solve you solve them by giving them to smart people then leaving them alone. You don't constantly harass them every day demanding to know what they did yesterday and what they plan to do today. With daily updates where is the incentive for the smart people to work on the hard problems? They now have the same incentive as the junior developer; find the easiest tickets to move across the board.

Sometimes I will want to just be alone and think about a solution for a few days. If I do that though I'd have nothing to say at the scrum. So instead I'll pick the user story where the colour on a front end was the wrong shade of green or a spelling mistake! See, I knocked out 2 stories in one day, before lunch! Go me!

...

I don't fully agree with his words. E.g., I agree with one comment said, it's not that they (managers) don't trust them, it's that they don't get things done without constant supervision.

When a great developer becomes an average developer there are always multiple reasons, but I do find daily scrum could be one of reasons. So how do I prevent this side-effect of scrum meetings?

I also realized it is easier said than done, but I like to see how others see this problem.

----- update -----

After reading all the answers I have got so far I realize I need to add some information to make my question more relevant.

But before I am getting into that, I want to repeat the words Martin Maat gave in his answer, "The mere fact that so many people feel the need to say something about it is an indicator of the frustration Scrum causes."

I totally agree! When I first asked the question I already expected some answers would be "oh, you don't do scrum right!"

Some corrections I want make to my original question are,

I used the word "great developer" and I probably should just say a decent/good developer because I have seen that sidetracked answers. Besides, throughout my career I never work with great developers, so I shouldn't use that in the first place. What I meant was I see from time to time that scrum has made a good developer perform less well.
Some answers focus on the sentence "it's that they don't get things done without constant supervision" and believed that was a micromanaging issue. But this was not my case, e.g. I don't micromanage. The problem I experienced (again from time to time) is good/tech-savvy developers are not necessarily business-savvy ones. Sometimes they will focus on perfecting their technical solution too much without realizing we have a product to deliver in the end. Other times it is a cross-function feature that needs coordination, especially each team may have its own priority/schedule. That is why they need supervision. But I guess I shouldn't just copy the word "constant supervision" from the original post and should not use constant in the first place. But again, if someone argues that "great developers" and "great team" don't do that, I have no counterargument then.
One answer said "the daily scrum somehow turned into a competition who has completed the most tickets". I never experienced that. A mature team does not do that (a mature is not necessarily a great team though). Has anyone experienced that?
For those suggested me to read the agile manifesto, my counterargument is this was a long book review I wrote in 2008 (12 years ago) for the book "The Enterprise and Scrum (Developer Best Practices)" by scrum cofounder Ken Schwaber. I listed my review here, not to show off, but to show (1) I believe I have done scrum long enough to see its strength and weakness. (2) I know what agile is about.
managementteamscrum
asked May 22, 2020 at 7:45
Qiulang 邱朗

Answer by Matthew Gaiser:

Don't let Scrum become the process which overwhelms everything else

My friends and I, who are part of Scrum teams are not fans of it. The reason is that in being the one process which has a dedicated process manager, it usually bends and breaks every other process to it and becomes this overarching process where you do nothing consistently except Scrum rituals and making those Scrum rituals seem successful.

The problems with Scrum are:

The sprint (the two week part) comes first. Because there is someone at the end of the two weeks asking about whether we got what we committed to done, getting tickets to "done" gets prioritized. It means that corners get cut to get the tickets finished. My team doesn't unit test or code review as the sprint ends. On my friend's team, he has thrown in if statements to deal with bugs QA found rather than actually finding the root cause of errors to get the tickets done. This two-week focus can lead to the infinite defects methodology. Obviously in Scrum it needs to pass the product owner, but unless they obsess over edge cases, a lot easily slips through and the developer is not encouraged to consider that very deeply. Scrum and infinite defects can be good friends because the infinite defects approach lets velocity be artificially high as long as bugs are found after the sprint and therefore counted as new work. You could have an ever higher velocity by constantly generating new bugs.
Everyone can see your productivity day by day and it becomes an easy evaluation metric. Having a public task board means everyone can see how quickly you are doing stuff, including management. There are key people in my organization who consider me very productive mostly because of how quickly I have moved tickets relative to other people. When developers are judged on that basis, a lousy implementation that passes QA and a well-tested, well-architected implementation are equivalent. That is where stars can be reduced to seeming average as that board + velocity becomes how developers are judged and becomes what they focus on.
Teams do not actually self organize usefully in many cases. Scrum goes on about "self-organizing teams." I wrote another answer about this.. In summary, team members are going to do things the way they prefer/are incentivized to do and unless that adds up to a useful team, lots of things do not get done and team members just keep marching on over the mess. Teams might self organize if they all have the same goal and incentives. The problem is, that is rarely true. One guy wants a promotion. Another is studying for a degree on the side. A third is upskilling to go to another company. Another just doesn't want to have arguments so agrees to anything and lets the codebase become a mess. A lot of good design requires the developers to sit down and hash out how a thing should work. In Scrum, you need to clear tickets and there is no real check on the quality of the work as "done" or "not done" is decided by a usually non-technical project owner. That incentivizes going into a void and focusing on outputting code.
Tickets/user stories rapidly become architecture. Because the developers are independently working away on each ticket sequentially, the architecture rapidly begins to mirror the tickets. The tickets are typically 1-2 sentence user stories. Ticket driven architecture rapidly gets messy simply because more code gets piled on as required.
The high level of developer independence means each developer takes different approaches. Consider sorting of an object. You can do that in the frontend in JS, in the backend in Java, or in the SQL itself and if you are time-constrained, you will choose whichever method you can most easily implement. While it is not necessarily wrong, it makes debugging a heck of a lot harder as more places need to be checked.
Standup is effectively "update management". The notion that standup is for developers is absurd. Does anyone actually wait until 9AM to report a problem or are they going to just ask in the group chat immediately? In practice, it is someone higher up the food chain keeping tabs on how fast things are moving so they can ask about it later in the day.

Great developers are usually defined by their ability to develop robust code. Unless the product owner is technical, Scrum massively devalues that as the product owner isn't evaluating the code. It is feature driven and "it runs" is a functional standard for the provided user stories.

Great developers are usually defined by their ability to write code which has value both now and in the future. Scrum projects think of everything in two week periods. There is no future.

Great developers are usually defined as those who can solve tough problems. Scrum encourages picking work that can easily be done and rapidly churned out at a steady pace. A tough problem is a developer being slow on getting the tickets done.

Great developers are often sought out for advice and for second opinions. But any time doing that is less time spent churning out tickets, so their velocity falls.

Even if you get a situation where you are not formally judged on the points completed (which will not happen if management is mostly interacting during Scrum rituals as that is all they have to see regarding progress), people are still going to compete for attention and rewards.

To resolve this, I would eliminate both individual velocity scores, the presence of management at standup (otherwise developers are strongly incentivized to always have good news), and would tell management that they second they praise a dev or give them a raise based on ticket volume, they radically change behavior. Ideally, the product owner would also not be a direct manager and thus someone the devs are incentivized to look good for during sprint review and sprint planning.

The problem is, you are fighting the nature of Scrum as it primarily cares about velocity. What gets measured is what gets focused on and what Scrum measures is speed of output with the output judged from the user side only by the product owner. That metric does not value many behaviors associated with great developers.

Answer by nvoigt:

How do I prevent scrum from turning great developers into average developers?

By doing it correctly. All those horror stories I read, being it yours or the other answers, only tell me one thing: those people did not do it correctly. And I get it, it's hard. It's super easy to slap down some rules and have them followed, but that is not Scrum. Scrum is forming a self-organizing team. That does not work with every person and it does not work in every constellation. But it is the foundation and everything you see is the result of not actually being a team.

Just imagine 11 people being handed a soccer manual and being told practice is every day for fifteen minutes around 10 AM in conference room #5. Do you think that is what makes a good soccer team? But what if those 11 people were really good, professional players? Still no team? No. Even Christiano Ronaldo would be getting "average" sooner or later with that kind of "team". But that's not soccer's fault. It's just not how you build a team.

Scrum builds on the fact that you are a team. In a team, it does not matter whether you got "a ticket done" yesterday. In a team, you agree on what your goal is (i.e. definition of done) and then strive to reach it. Together.

A great developer does not get one bit less great if they talk with their team for 5 minutes a day. A great developer will become uninterested if they are forced into a poorly managed process that has a daily meeting where they report to their manager whether they got a ticket done or not.

Having a daily report meeting where you tell a manager what you did yesterday and try to fit in some arbitrary performance scheme is not Scrum. It's a well known anti-pattern. Someone might call it Scrum and say the Scrum guide says you should meet daily, but it would be just as much real Scrum as the People's Democratic Republic is actually a democratic republic for the people.

Just like team sports, Scrum needs the participants to be a team. If they are just participants that look to boost their own standing by showing off how many story points they did or how many goals they scored, they will always lose the day to a team that works together instead of next to each other or against each other.

So how do you prevent Scrum from turning great developers into average ones? Hire team players. Great, average, does not matter, because a real team will beat a random collection of supposedly "great" participants any day. I'm not saying that's easy. But that's what Scrum is about.

Answer by meriton:

Scrum is a process framework defined in the official scrum guide, which says, among other things, the following things about the daily scrum:

The Daily Scrum is a 15-minute time-boxed event for the Development Team.

The structure of the meeting is set by the Development Team.

The Scrum Master ensures that the Development Team has the meeting, but the Development Team is responsible for conducting the Daily Scrum.

The Daily Scrum is an internal meeting for the Development Team. If others are present, the Scrum Master ensures that they do not disrupt the meeting.

Let's compare that to the experience you cite:

Everyone just wants to take something easy off the board that you can get done in a day so you have something to report in tomorrows daily scrum.

Report to whom? The people attending a daily scrum are the other developers (and the scrum master, but he only cares about process, not progress).

In practice, this means that you'd be informing your fellow team members of where you are so they can coordinate their work with you. You shouldn't be reporting, because that implies a degree of hierarchy that should not exist within a scrum team.

if nothing is moving across what are you even doing? You're letting the team down! The velocity is falling!

Who is saying that? I can't imagine a fellow developer saying that, the scrum master should not care because he is not responsible for progress, and outsiders (such as the product owner, or management) should not be disrupting the meeting!

Whatever this is is, it is not scrum.

Scrum instructs the scrum master to prevent this from happening. If this behavior were allowed, whoever is being reported to would start directing the work of the team, violating the fundamental scrum principle that

Self-organizing teams choose how best to accomplish their work, rather than being directed by others outside the team

The reason scrum insists on that is the following:

Scrum users must frequently inspect Scrum artifacts and progress toward a Sprint Goal to detect undesirable variances. Their inspection should not be so frequent that inspection gets in the way of the work. Inspections are most beneficial when diligently performed by skilled inspectors at the point of work.

That is, scrum acknowledges that of all the people involved in the project, the development team knows most about developing software, and politely asks management to let the experts work.

So when you say:

I think if you have hard problems to solve you solve them by giving them to smart people then leaving them alone

scrum agrees wholeheartedly and goes to great lengths to give teams this autonomy.

But since there is no scrum police, everybody can call their process scrum even when it is not. And since "agile" sounds cool, many companies do, and thus give scrum a bad name.

In summary, the best way to prevent dysfunctional scrum is to read the scrum guide, and actually do what it says.

Answer by Llewellyn:

I'd like to present a counterpoint to most of the answers. As a software developer, I've thrived in Agile teams.

Working with a crossfunctional team gave me a better understanding of the features we were building and how they were going to benefit the users. I have used this understanding to explain to management why one bug might need to be fixed now, while another is much less important, why we need to refactor legacy code before we can start implementing the desired feature, or how the company would benefit from having better test coverage. And on the other hand, sometimes, a quick-and-dirty prototype is exactly what you need, but it's hard to make that decision if you don't understand where the requests are coming from.
Being involved in project planning (meetings or backlog grooming) gave me the chance to raise technical concerns and/or to suggest small modifications that would achieve the same goal (or close enough) in a slightly different (e.g. less risky) way.
Getting frequent updates on how my colleagues are doing gave me the opportunity both to help out/mentor junior developers and to learn from more experienced colleagues.
Having short release cycles gave me the chance to update the architecture early on as soon as it became clear we were going to need some changes rather than having to rebuild everything from scratch at a much later time. Frequent testing meant that bugs and undocumented edge cases got discovered early and were easier to fix.
I've made good use of each and every retrospective to raise pain points and suggest improvements, e.g. with respect to meeting efficiency, documentation, or (lack of) tools and trainings.

Scrum is a framework that's supposed to allow for faster project cycles, so the product can be adjusted to changing requirements. At any given moment, you're going to focus on a small slice of the entire product, ideally something that could be shipped on its own. But none of that absolves you from doing your duty as an experienced software developer. You've been in the planning meetings, you can check the backlog, and you know what the overall vision is. All of this means is that you should have a good idea of where the project is headed, and you can use this knowledge when you plan the architecture even for the current Sprint. You'll want to avoid investing a lot of time into something far ahead in the future, but there's nothing wrong with laying the foundations for an extensible, modular system that works well for what you need right now and will also support the planned future additions.

I'll admit that all of this only works if management is playing along. If management is essentially ignoring the developers, there are fixed deadlines to be achieved with a predefined scope, or it's a dog-eat-dog environment instead of a team focused on achieving the same goal, if planning ahead and thinking out of the box are not appreciated, then yes, eventually you'll give up and resort to just doing the assigned tasks. I've been there. But don't blame that on Scrum.

With the right team and managers who trust the experts they hired, Scrum can give that extra push to elevate a good team into a great one.

Answer by Martin Maat:

Lots of answers already, yet I cannot resist. The mere fact that so many people feel the need to say something about it is an indicator of the frustration Scrum causes.

First, the motivation to introduce Scrum is never coming from experienced developers, it is always coming from management that feels it is losing control. Then they typically cherry pick some concepts from the book and plant them into the team. False start immediately.

As the creators of Scrum state themselves: following Scrum rules by the book is good to get your team out of a ditch but you should not stick to them religiously as you progress. This is lost on most teams because there will be a Scrum master that typically is not the most capable developer and he will only get more serious about the process in time because he finally found something he is good at.

Thus the pull to the average works on multiple levels: not just individually but also on the team level.

Only strong teams can survive Scrum and use it to their advantage instead of being suppressed by it. It is not impossible but the environment is working against it, most teams will be effected in one negative way or another.
