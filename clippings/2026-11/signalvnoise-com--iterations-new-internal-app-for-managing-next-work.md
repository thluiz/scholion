---
url: "https://signalvnoise.com/posts/2659-iterations-a-new-internal-app-for-managing-what-we-work-on-next"
captured_at: "2026-11-16T03:20:50+00:00"
title: "Iterations, a new internal app for managing what we work on next"
domain: "signalvnoise-com"
---

What should we work on next and who’s going to do it? We recently created a new internal app called **Iterations** to answer that question. It’s for 1) managing our internal requests about which features/bugs to work on next and 2) helps us create teams/iterations to get them done (using our [team-based way of working](http://37signals.com/svn/posts/2640-another-round-of-lessons-learned-from-our-new-team-based-way-of-working)).

![screen](https://37assets.37signals.com/svn/iterations_launchpad_done.png) _A completed feature request._

**The problem**  
Before Iterations, we kept ideas for what to do next all over the place: in our heads, dumped into [Backpack](http://www.backpackit.com/?source=svn_post), on pet lists kept individually, in [Campfire](http://www.campfirenow.com/?source=svn_post) team rooms, etc.

Even when we did manage to collect ideas, the list(s) would quickly become unmanageable. Ideas ranged from tiny fixes to large-scale multi-term projects. It wasn’t clear who added each idea, and many were in the form of feature requests — not scoped to an iteration.

**Collecting ideas**  
So we made Iterations in order to create an easy place to jot down a quick idea — even if it isn’t fully formed — and then let a team build on it from there. Iterations would also make it easier to expose small, slack-type projects that are ripe for doing when someone has a short window of downtime.

![screen](https://37assets.37signals.com/svn/iterations_completed.png) _Viewing multiple requests at once. In this case, it’s completed items._

With v1 of Iterations, each member of our team can:

*   Share an idea for something they’d like to be worked on
*   Discuss ideas that have been posted
*   Show support with a +1 for the ideas they like
*   Indicate interest in working on an iteration
*   See what other people are interested in working on
*   Form iteration teams
*   See what is currently being worked on and what is done

Iterations shows who proposed the idea, who supports the idea, and who is interested in working on it. There is space for discussion of details, implementations, and scope. Similarly, it shows which projects aren’t viable and which ideas can be dismissed.

![screen](https://37assets.37signals.com/svn/iterations_suggest_new.png) _Suggesting a new iteration._

![avail](https://37assets.37signals.com/svn/Available-iterations.png)  
_Avatars for each person who supports an idea shows the amount of interest in an iteration._

**A new way of assembling teams**  
It also transforms the way we assemble teams. It lets people align themselves with the ideas they’re most excited to work on. The process of creating teams becomes more organic.

When a designer or programmer offers to work on something, they can see who else might want to work on that same iteration and form a team to do it. Similarly, a newly formed team might use Iterations at the start of a term to see which projects the members of the team have previously shown interest in and find common ground.

![+1](https://37assets.37signals.com/svn/iterations_plus1.png) _Finding common ground._

**A working history**  
Iterations also keeps a history of proposed iterations. The stream of discussion as an idea forms and a team takes it on winds up being especially useful for 1) iterations that end but without launching anything or 2) when an exploration results in something we don’t want to further pursue.

**From chalkboard to screen**  
The core of the app was designed in-person in a team room during our last company meetup. Here are a couple of chalkboard shots from those sessions:

![chalk](https://37assets.37signals.com/svn/IMG_0723.JPG) _Early modeling and UI discussion._

![chalk](https://37assets.37signals.com/svn/IMG_0725.JPG) _Our first sketch of the comment and actions UI. The heart button eventually became “+1”._

And an additional sketch after the meeting:

![draft](https://37assets.37signals.com/svn/iterations%20UI%20idea.png) _Further explorations of the comment UI._

**So far, so good**  
We built Iterations in about a week and have been using it since early September. So far it has been a great addition to the set of apps we use every day. Rarely does a day go by that someone hasn’t made a new suggestion or supported another. Right now Iterations shows 6 iterations in-progress, 15 completed, and dozens available for teams to pick up. We’ve even continued to tweak the app post-launch adding integration with our [Backpack](http://www.backpackit.com/) Journal and [Campfire](http://www.campfirenow.com/) rooms.

![CF](https://37assets.37signals.com/svn/iterations_campfire.png)  
_Iterations integrates with Campfire._

Iterations helps us better understand what people are working on, what people want to work on, and what’s important. It’s turned disparate ad-hoc to-do lists into nicely scoped iterations that are ready to go.

(Will we be releasing this to the public? We’re busy focusing on other things right now. It’s unlikely we’ll put the work into polishing this up enough to be a product, but we can’t say for sure.)
