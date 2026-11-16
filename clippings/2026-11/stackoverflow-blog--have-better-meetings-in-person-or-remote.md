---
url: "https://stackoverflow.blog/2020/04/30/have-better-meetings-in-person-or-remote"
captured_at: "2026-11-16T03:13:09+00:00"
title: "Have better meetings—in person or remote"
domain: "stackoverflow-blog"
---

Many software engineers have a limited understanding of what business problem the software they build solves and what exactly it needs to do. For example, I work on a management system for vehicle parking contracts. However, because I know very little about how parking contracts work or parking management in general, I rely on a business analyst and a product owner to relay what exactly needs to be done.

Going from a business need to a working feature requires the product owner to ask for something from the business analyst, the business analyst to present it to the developers, and finally, for the developer implementing the feature to have the same understanding as the group.

This system is functional in an in-person meeting. Hand motions, spontaneous drawings on the board, and the self-contained nature of the conversation make it so that one can muddle through. People can jump in and ask for a spontaneous clarification of an acronym someone used or quickly insert their point during a pause because you can listen and think at the same time. Once someone has finished talking, the next already has a response.

When working remotely, much of this is lost. An in-person meeting forces people to pay attention, so eventually, the entire messy conversation reaches the end. All responses are immediate and distractions are minimized. When a question is asked, it must at least be acknowledged immediately. Fewer distractions exist to pull someone away for a few minutes. It is harder to fall asleep.

On my project, the product owner and most of the key stakeholders work in a completely different building, coming by only once every two weeks for sprint planning. Any clarifications to tasks, changes in priorities, or new client requirements outside of planning must be communicated through email or chat. Since the coronavirus outbreak, we are now an entirely remote team and must hold a four hour long meeting with 15 people over video chat. Here are some things I have learned before and during that transition.

An in-person meeting allows for quick colleague-to-colleague side chats that clarify what the meeting is about before it starts. It encourages off-hand comments, which gives clues to what is on everyone’s mind. But on video calls, there is only one audio channel, so asking quick questions of the person sitting beside you is impossible.

Many times during remote meetings, I fail to understand why the meeting exists, what needs to be achieved, or what the basic topic even is. Last week, I was on a call for a half hour and contributed nothing simply because I did not know why we were there.

To fix this, consider writing a 50-100 word meeting summary and asking people to read it at the start of the meeting. Alternatively, spend the first one or two minutes outlining what must be accomplished in the meeting. That will help ensure everyone is on the same page and understands why they are there. This is a good practice for any meeting, but crucial when all the informal ways of learning about the meeting disappear.

For months, I did not learn very much about the contract management system beyond what was part of my assigned areas of work. I failed to meaningfully engage beyond the code I had to write.

The problem with that approach is that terminology that has a very specific meaning to the product owner and business analyst can have a completely different meaning to you. For my project, “permit” and “contract” are two very distinct concepts and nothing I do relates to the company definition of “permit.” However, I kept referring to the contracts as “parking permits” as that is what I am used to a parking contract being called.

That frequently led to emails and chat messages where myself and the non-technical chat members spent a good 20 minutes referring to completely different aspects of the project. We only broke out of that infinite loop once someone was confident enough to ask whether we were talking about the same thing.

You don’t need to become an expert of the domain, but do your best to align your usage of words with how they are defined within the company. As much as jargon can inhibit understanding for newer people, it is still extremely helpful when dealing with an established team.

In-person conversation can wander, weave, and avoid defined breaks because the other people get to react to it in real-time. When you start talking, the person you are talking to can immediately process what you are saying and think of what they want to say in reply.

With text communication, people only start reading what you are saying once you have completed it and sent it. When you are ending your thought process, your readers are merely beginning.

In addition to the delay this can cause conversations, it also causes conversations to lose their line of thought. Several times, I have tried to ask some fairly complex and lengthy questions in chat and while I was busy writing my answer, the conversation had moved on to an entirely different topic. My error was in writing out my question as one lengthy block of text rather than a rapid series of messages.

If there are multiple people in a fast-moving chat conversation, try to keep your messages to a single sentence each. This allows it to flow more like an in-person conversation rather than just bouncing emails back and forth. Replies can call out what point the person replying to is addressing, and distinct thoughts are easier to recognize.

Many concepts in software engineering have quirky names or names which have entirely different meanings outside software engineering. In a non-technical context, a “design pattern” involves colors and arrangements of flower designs.

As an example, consider how I explain one-to-one vs one-to-many relationships and the relative complexity in their implementation. Changing a feature from having one of an item to several of an item often requires a large amount of developer time. Non-technical people are often surprised at how expensive such a seemingly simple change is and want an explanation for why. What I tell them is that one to one is like having one parent with one child at the zoo. One to many is like having three children with one parent at the zoo, which is a great deal more complicated.

When trying to form an analogy, consider things that would be generally known in the group you are talking to. Start with corporate practices and existing contracts. In my current role, the local zoo is one of our clients, which is one of the reasons I chose that example.

20 questions is a game that computers can play for a reason. The possible scope of a topic can be dramatically narrowed with the help of questions that demand nothing but a true or false answer. When looking for clarification, use this method. Simple questions such as “does this need to be completed by Friday?” or “is this a customer facing feature?” can be the difference between confusion and rapid understanding.

During our last sprint, one feature loaded quite slowly to the point that a customer might think the webpage had gotten stuck. While there were many ways to fix it, fundamentally the two choices were to add a loading indicator of some sort so that the customer knows to wait a few moments or dedicate effort to making the feature run more quickly.

Conversations on such issues usually end up discussing the many solutions just below those two categories. We discussed everything from how we might optimize the SQL queries to ways to reduce the API call count to generating a call profile with option one to all the different types of spinners and messages that were possible with option two.

After five minutes of not really getting anywhere in terms of making a decision, I told the product owner that the two fundamental choices were implementing a spinner at around three hours of work or redoing the backend to work faster at a cost of a half a week of work. That settled the choice in 30 seconds because completing the related component within the sprint without removing other features was a high priority. The conversation then zoomed in on the details of the spinner. Had I not done this, the conversation could easily have lasted 30-40 minutes.

Those who work on larger teams may have someone dedicated to user interface design or user experience who might be doing this already. My team does not. Any UI development must be done by either one of the developers (usually me) or the business analyst. As much as mockups are outside the job description and not part of the formal workflow for features, they have proven quite valuable.

Last week, I was tasked with moving a button for a specific client. The button’s default position is on the left side of the page and fairly far down. The client wanted it moved to the right and substantially upward as the right side has a lot of white space. The part that got communicated to me was that the button should move to the right.

It was assumed by the person giving me the instructions that moving the button to the right was a general instruction open for me to interpret, not a specification. I took it as a specification, so I moved the button along the x-axis to the far bottom of the other side.

This is a simple problem that will be easy to fix, but the client must now wait an additional two weeks for it to be resolved in the next release.

The mockups do not need to be complex or done in a professional way. I mostly just use a combination of Snipping Tool, Microsoft Paint, and the Google Chrome developer tools to tweak existing components so they can be screenshotted and used. Does it look like a grade five collage? Sometimes. Do they serve the purpose of clarifying where stuff goes? Absolutely.

There are often several distinct conversations within every meeting that could have existed by themselves. If you think of a meeting as the code for a piece of software, code that can exist by itself should usually be turned into a function with a return statement at the end.

The same approach is helpful in meetings. As a topic is being wrapped up, spend 30 seconds summarizing the decision made and the action items. That summary ensures that everyone actually knows what was concluded and gives them an opportunity to object if something is incorrect. Otherwise, any errors will be discovered in the sprint review after the work has already been completed.

Like many of you, meetings and messy conversations are not my favorite part of the job and can become excruciatingly irritating if they carry on forever or lead to misunderstandings that cause work to need to be redone. Having these conversations remotely exacerbates many of these issues, but hopefully, these tips can keep you productive and not stuck on Skype.
