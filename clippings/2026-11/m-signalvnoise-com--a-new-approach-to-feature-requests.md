---
url: "https://m.signalvnoise.com/a-new-approach-to-feature-requests"
captured_at: "2026-11-16T03:19:34+00:00"
title: "A New Approach to Feature Requests"
domain: "m-signalvnoise-com"
---

A few months ago, I got this email from a customer:

> It would be wonderful if there was a way to tag/assign forwarded emails to specific task lists within client projects. The “email forwards” section is really cumbersome on large scope client projects where we have lots of balls in the air at once.

It’s pretty straightforward. Our app doesn’t have this feature and they would like it to be added. It’s a feature request. Our support team sees a dozen or so feature requests every day.

Deciding how to handle feature requests like this one is tough. Do you track every single one? Are you only focused on some subset?

And most importantly — how do you turn a customer email into something usable for your product teams? That’s the end goal — something usable by others in the company.

* * *

Early in our days at Basecamp, we would literally “read them, throw them away, and forget them”.

> “It sounds blasphemous but the ones that are important will keep bubbling up anyway. Those are the only ones you need to remember. Those are the truly essential ones. Don’t worry about tracking and saving each request that comes in. Let your customers be your memory. If it’s really worth remembering, they’ll remind you until you can’t forget. “ — [Getting Real](https://basecamp.com/books/getting-real)

When you’re a company with a few people in it, it works. Everyone is pitching in to answer customer emails so you’re bouncing into that support queue often. Once the company gets bigger though, that approach doesn’t work as well.

As Basecamp the company grew, and our support team grew, we tried tagging all of those feature request emails.

Idea for the calendar? Tag it. Feature request for the message board? Tag it.

But now what? You can go to the product team and say “We’ve seen a 5% increase in customers requesting a grid calendar. “ But how is that helpful information? Just the raw data doesn’t really help. And our support team couldn’t really put together a story from those tagged emails.

That means the product team has to dig through those tagged emails and hope to see any usable information from the customers in those tag emails. It slows things down at best and at worst, leaves the product team without anything to go on.

There’s got to be a better way, right?

That’s the version I want to share with you today. Here’s how we handle feature requests at Basecamp right now.

* * *

When a feature request comes in, we start with this question — where does it fit in Basecamp the product?

From that answer, there’s three general paths forward for that request:

*   We’re not going to do it — requests like translations, Gantt charts, time tracking.
*   We’d like to — ideas like Clientside improvements or Dropbox linking. These are ones we’ve built out in previous versions or have talked about a bit before.
*   We don’t know — ones like turn a message into a to-do, out-of-office setting, more keyboard shortcuts. Maybe we’ll explore them down the road. ¯\\\_(ツ)\_/¯

#### Path One — We’re not going to do it.

If we’re not going to do it, we tell the customer so. This sets expectations up front and lets the customer know if they need to explore an integration, use a workaround, or consider switching to a different product.

For example, a customer might request the Basecamp UI in Spanish. That’s not one we have intentions of doing so there’s no need to track it, tag it, or anything else other than tell the customer we don’t have plans to do that.

#### Paths two and three — We might at some point.

For the other two paths, we want more information. As the support team, it’s our job to give the product team enough information to make decisions around building a new feature.

It’s kinda like being a detective. We go out and investigate the situation a customer is when they email us their feature request. We talk with people involved, detail the facts, and then bring all of this back to the product team. Once they know the facts, the product team can start thinking through our options.

I want to take you through an actual customer interview that started with “I need X” and ended with a new feature in Basecamp.

* * *

[Basecamp 3](https://basecamp.com/svn) launched without a grid calendar. You know, the ones that look like Google Calendar, Outlook, etc. We had an agenda style list view of events in projects. And you could always subscribe to an iCalendar feed if you really wanted to see it in a grid calendar using Google Cal or such. But there wasn’t a grid calendar in Basecamp 3 itself.

Naturally, customers emailed us asking about it, especially ones that had used a prior version of Basecamp where a calendar was included. Each week, we’d see emails asking “Where’s the grid calendar in Basecamp 3?”.

From the product team’s view, a grid calendar is tough. It took us months to build one in the Basecamp 2. With Basecamp 3, it was looking like many months of work, which is way outside of our [normal six to eight week work cycle](https://m.signalvnoise.com/svn3/how-we-set-up-our-work). And customers expect your grid calendar to be as good as all the others out there — so you need color coding, week and day view, invites, integrations, repeating options, event length options, etc.

It’s a lot of work. But we have to build it because it feels like everyone’s asking for it, right?

So let’s investigate! It’s kinda like flipping the detective mode switch. I needed to find someone that needed a grid calendar right then and find out everything I could about what they were really trying to do.

#### The Interview

Meet Annie (name changed to protect the innocent). Annie is a psychologist that works with a team doing in-office client sessions as well as field work. She’s used Basecamp for about a month when she emails us.

> Hi. I’m wondering if besides the scheduler is there a way to look at a whole calendar that has everything on it at a glance? Like a week at a glance or a month at a glance or even a day at a glance. Otherwise I have to look at each schedule. And I don’t want to have to constantly open my calendar or have to sync each event created by others to my calendar. Help. Much needed feature.

Perfect — I’ve got my first witness in the “I need a grid calendar” case. I set up a call with her to find out more.

Now with the call, it’s structured around the idea of a [Jobs-to-be-Done](http://jobstobedone.org/) interview. I’m not looking for the feature she’s seeing in her mind. Instead, I want to know everything I can about the situation that led up to her emailing us. I want to know what “job” she needed that grid calendar for. And I want to put all of this on a timeline as best as I can. That way I can say this happened, then this, which made this happen, and that’s when she emailed us.

So we’re on the call.

**First question** — “what was going on an hour ago when you decided to send us that email with your calendar idea in it?”

Annie said she had just added an event in Basecamp to book a meeting room for a client session. She had to drive into the office to do that.

On our timeline — I’ve added a new piece of information.

![](https://m.signalvnoise.com/assets/svn3/images/2018/01/1eAv7fxGEooW3DP3lFWgvhA.jpeg)  

**Second question** — “Why did you drive to the office to do that?”

Annie said she needed to look at the wall calendar to see what rooms were open for that client session. There’s eight rooms. That’s eight open spots a day for clients.

![](https://m.signalvnoise.com/assets/svn3/images/2018/01/1Is41uHw7MfItmW9y31xUIw.jpeg)  

**Third question** — “Wait, wall calendar? What’s that?”

Annie said they used to have a company secretary that handled client appointments. But for cash flow reasons, they had to let her go. In her place, they tried using Basecamp for client sessions but couldn’t easily see what dates/times/rooms were open. So they painted a 12ft x 6ft wall with whiteboard paint, drew out a grid, and now use it as a calendar for scheduling. They still add the events to Basecamp for the reminders.

![](https://m.signalvnoise.com/assets/svn3/images/2018/01/1tPRRwZ3wYqzmRUIKBKAhFw.jpeg)  

**Fourth question** — “Have you had to do this before — driving into the office to look for an open spot? If you have, what made this time different than the others?”

Annie said she’s done this before but this day was supposed to be her off day. Plus, she was frustrated because she got to the office, looked at the wall calendar, and saw all eight spots were booked so the client would have to wait until next week.

![](https://m.signalvnoise.com/assets/svn3/images/2018/01/1JWxfmizgRXjgZLuK02FsDg.jpeg)  

Whew — what a timeline!

Think about that — even though her client meetings were in Basecamp, she had to drive into the office, on her day off, and physically look at this giant 12ft by 6ft whiteboard wall only to find out it was a wasted trip since the rooms were all booked.

I’d probably drop an email to the support team then too.

#### The Results

From Annie’s interview, we found out the feature request for a grid calendar isn’t all about this massive calendar tool. It doesn’t have integrations. It can’t do recurring events. It doesn’t sync with your phone or another computer.

But notice what it does really well — it shows space. It’s all about seeing open spots and how busy things are on a given day. That’s something our agenda list view in Basecamp can’t show you.

But is Annie alone in how she uses this? Or does this happen with other customers too?

Back to the queue to find more witnesses for the case!

When I interviewed more customers, the same pattern kept appearing. Jeff needed to see open spots to decide if his team could fit in new client work that week. Shirley needed to see which designers were available and which were spread too thin.

Through these interviews, we found the job customers had. In their language, it was all about a grid calendar. But once you dig in, it was all about seeing space on the calendar. It wasn’t the need for a full blown calendar app. Just something to see the space.

With those details, we could write up a pitch for a new feature. It was picked up for [one of our cycles](https://m.signalvnoise.com/svn3/how-we-set-up-our-work). A team of three people built out the new schedule in about seven weeks. And it fit what our customers were really needing.

![](https://m.signalvnoise.com/assets/svn3/images/2018/01/1jTN23bdTlZKPgcE0qjNJ1A.png)  

#### It’s Ongoing Research

For us, these interviews happen each week. Usually 2–3 a day if we can. A feature request email comes in and we try to schedule a call with that customer for the same day. With it fresh in their memory, they can really provide details about the situation and put us in their shoes at that moment.

So that’s how we approach feature requests. Find a customer with a feature request, interview them, repeat those interviews until you can see patterns. With that information, [a pitch](https://m.signalvnoise.com/svn3/how-we-set-up-our-work) can be written and then the feature created.

[https://basecamp.com/svn](https://basecamp.com/svn)

* * *

_For more on this approach, make sure to check out Ryan Singer and Chris Spiek’s_ [_Demand Thinkin_](https://demandthinking.com/)_g episodes._
