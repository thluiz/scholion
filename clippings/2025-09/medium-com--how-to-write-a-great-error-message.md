---
url: "https://medium.com/@thomasfuchs/how-to-write-an-error-message-883718173322"
captured_at: "2025-09-01T16:13:03+00:00"
title: "How to write a great error message"
domain: "medium-com"
---

[

![Thomas Fuchs](https://miro.medium.com/v2/resize:fill:64:64/0*Xzv0nSsE62vJOEsd.jpg)

](https://medium.com/@thomasfuchs?source=post_page---byline--883718173322---------------------------------------)

7 min read

Aug 30, 2015

\--

Imagine being in an office. In your cubicle. You’ve worked long hours this week for an upcoming product introduction. You’re tired and cranky, and you just want the weekend to _finally_ arrive.

But first you have to try if the homepage for the new product works fine on _Windows 10_. No problem, you think, your trusty Mac laptop has software installed that allows you to run Windows.

You fire up the software, and when Windows politely asks you to update with several intrusive notifications, you say, _sure_, go ahead.

And then you see this.

Something something

That would be _almost_ amusing, if it wasn’t for the deadline for the product.

Well, you say, let’s blow off some steam and share that screenshot with the world — or at least, with the Twitter world.

Excitedly you drag the screenshot into the _Mac Twitter client_, and hit the _Tweet_ button. Then this happens:

Press enter or click to view image in full size

_Those pesky media ids are at it again!_

When you finally come to your senses after contemplating the _Weltschmerz_ of the universal suffering brought upon humanity by lazy programmers and designers who don’t think — _you_ _think_ perhaps some great food will help.

An excellent plan! Thanks to the awesome power of millions of dollars of venture capital and hordes of mustache-twirling techno-hipsters spending the best years of their youth in swanky San Francisco loft offices, let’s order burrito delivery!

But first, just answer this one important philosophical question that _Postmates_ has for you, out of the blue and with no context.

Press enter or click to view image in full size

I tapped “No”. I’m really not.

> _What goes into an actually useful error message or dialog?_

After this dramatization of events that actually happened to me last week, let’s have a look at what a great error message should be like.

Let’s see what _people that should know better\*_ think about this. Apple has been at the forefront of user interface design for many years, and while they’ve been slacking off recently (perhaps no one throws cameras at the designers anymore), they do have some good things to say.

Here’s what the [OS X Human Interface Guidelines](https://developer.apple.com/library/mac/documentation/UserExperience/Conceptual/OSXHIGuidelines/WindowAlerts.html#//apple_ref/doc/uid/20000957-CH44-SW1) tell you about alerts:

Press enter or click to view image in full size

> **Write an alert message that describes the alert situation clearly and succinctly.** An alert message such as “An error occurred” is mystifying to all users and is likely to annoy experienced users. _(…)_ **Write informative text that elaborates on the consequences and suggests a solution or alternative.** Give as much information as necessary to explain why the user should care about the situation. _(…)_ Informative text is best when it includes a suggestion for fixing the problem. _(…)_ **Express everything in the user’s vocabulary.** An alert is an especially bad place to be cryptic or to use esoteric language, because the arrival of an alert can be very unsettling. _(…)_ It’s a good idea to avoid using OK for the default button. The meaning of OK can be unclear even in alerts that ask if users are sure they want to do something. For example, does OK mean “OK, I want to complete the action” or “OK, I now understand the negative results my action would have caused”?

We’re getting somewhere now. Heck, they even have great article on [terminology and wording](https://developer.apple.com/library/mac/documentation/UserExperience/Conceptual/OSXHIGuidelines/TerminologyWording.html#//apple_ref/doc/uid/20000957-CH15-SW1).

> In the same way that it’s best to work with a professional graphical designer on the icons and images in your app, it’s best to work with a professional writer on your app’s user-visible text.

Your job as product manager, designer or developer of an app is to recognize that _writing copy in your app is not something that you can just do on the side._ **It’s just as important as having the application work correctly and the user interface being easy and efficient to use.**

\*_Nobody is perfect. But at least they try most of the time, which is appreciated._

> And here are the usual suspects…

Let’s review some real-world error messages and see if they’re making the cut or not.

Oh, Windows phone. Sorry, but _“We are currently unable to check for updates.”_ doesn’t cut it. _Why is the phone currently unable to check for updates? And what can the user do about it?_

The actual answer to this particular problem: the phone clock wasn’t set to right date, which made the SSL certificates on the update server not validate, which led to the message. After setting the clock, all was good.

_Why isn’t the error message something like_ “For security reasons, we couldn’t check if an update is available. This can happen when your phone’s time and date isn’t correct. Check your time and date settings and try again!”_. Or even better yet, make sure that your operating system actually automatically sets the time and date?_

Seriously Google, who cares? Why is this an alert (_please note that this is not the native iOS location authorization alert_) that stops people from whatever they’re doing (_using your browser_)? How is this ok? Who thinks it’s a good idea to ship this?

It’s perfectly fine to ask people if they want to turn on sending in their location; it makes sense for a search engine. _But don’t abuse operating-system level mechanisms that are meant to indicate serious problems or issues to users that need an immediate decision._

Press enter or click to view image in full size

Nope, nope, nope. Why does an obscure setting that should just default to what 99% of all other software is doing (cancel) require a modal alert?

Yes, I know that some of Adobe’s software has “ESC” as default for committing changes — however, even so it can just be a setting elsewhere. Power-users who’ll be irked by this have an easy time figuring it out. Another solution, as an alternative to a modal alert, is to default to canceling, but show a little _“Did you mean to commit with ESC? Click here to set as default and undo cancelation.”_ bar on the bottom of the window. This _doesn’t need to be_ a modal alert.

Be a bit more decisive about your defaults, Adobe. _Your users can take it._

> The most important take-away:  
> The best error message is the one that never shows up

For every single one of the examples above you could actually **avoid showing an error at all**. _I’m just not entirely sure about Windows 10 setup, but then again it seems that it is unsure of itself_.

*   As for the Twitter error, explain what’s wrong with an attachment when you add it to the Tweet. Or better yet, fix the problem, and ask if the fix is ok. _I was cheating a bit: I actually added a high-resolution (10,000 pixel wide) image, and Twitter has resolution limits for images. Why not tell me before I try to upload? Why not resize the upload on the client so it’s within acceptable limits? You could resize and show a little non-modal message, something like “Note: This image has been resized so it can be included in your Tweet.”_
*   The Postmates alert: if it doesn’t even say what it is about, it clearly isn’t important enough to even show it. _Nothing bad happened when I tapped “No”._
*   The Windows phone update message: have your operating system figure out the time and date automatically. _You know, you’re connected to cell networks and the Internet._ [_The technology to do this (NTP) is 30+ years old._](https://tools.ietf.org/html/rfc778)
*   Google Chrome begging to spy on you just a little bit more: Seriously, just show a banner on top of the search results or something. _You don’t need to invade our privacy that desperately._
*   Photoshop: ship with sane defaults. _You can tell people about customization options with an undoable action banner\* or a tutorial instead._

_\*A good example is Gmail’s “Undo sending?” banner that will show up after sending an email. This is a lot better than, say, showing a modal alert with “Do you really want to send this email?”_

I knew you’d ask, so I made a little checklist for you to print and hang on the wall of _that cubicle_. Just read it when you’re thinking about adding an alert to your application.

## The 3 most important things when writing error messages

1.  **Don’t abuse alerts for upselling or showing superfluous information**. People will stop reading the messages that are actually important.
2.  **Don’t just assume people know about the context of a message**. They might toggle between apps and see your message days after it happened. Always include enough information for users to make sense of it.
3.  Use a **friendly, non-technical**, non-threatening tone of voice.

**_TL;DR Write actionable error messages that laypeople can understand.\*_**

_\*Not sure if they do? Show them to a non-technical person and ask them to explain it back to you._

Press enter or click to view image in full size

Medium, you could do better, too!

_Do you want to be_ **_more productive_**_, earn more with_ **_less work_** _and have time for all those_ **_fun side projects_**_? This story and more first appeared on the_ [**_Noko Time Tracking Productivity blog_**](https://nokotime.com/)**_._** _Head on over!_
