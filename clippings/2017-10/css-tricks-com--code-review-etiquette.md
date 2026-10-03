---
url: "https://css-tricks.com/code-review-etiquette/"
captured_at: "2017-10-30T12:43:29-03:00"
title: "Code Review Etiquette | CSS-Tricks"
domain: "css-tricks-com"
---

# Code Review Etiquette

[code review](https://css-tricks.com/tag/code-review/)

Code reviews are a big part of writing software, especially when working within a team. It is important to have an agreed-upon etiquette for reviewing code within a team. A code review is a critique and a critique can often feel more personal than the code writing itself. A sloppy, under-researched, or insensitive code critique can cause difficulties between team members, reduce overall team productivity, and diminish code quality over time. This post will briefly define code reviews, describe some common mistakes, and provide some quick tips for improving a code review process.

### [#](https://css-tricks.com/code-review-etiquette/#article-header-id-0)What are code reviews?

Code reviews are the process of sharing code so that other engineers can review it. Code reviews can happen verbally during [pair programming](https://en.wikipedia.org/wiki/Pair_programming) sessions, or through reviewing code on websites like [CodePen](https://codepen.io/) and [GitHub](https://github.com/). Mainly, code reviews happen in tools like GitHub when engineers submit [pull requests](https://help.github.com/articles/about-pull-requests/).

Critiques are hugely beneficial. Convening engineers to discussions about code ensure that they're on the same page, regardless of whether it's in person or by sharing comments. Also, a review can help catch small mistakes in code or comments—like spelling and it can help newer or more junior coders learn the codebase. When done well, regular code reviews have nothing but benefits for all involved.

A common goal for code reviews is to make code changes as minimal and clear as possible so that the reviewer can easily understand what has changed and what is happening in the code. If code reviews are smaller, they're more frequent — potentially several a day — and more manageable.

Reviewing code should be a part of every developer's workflow. Senior reviewers are given the opportunity to teach/mentor, and even learn something new from time to time. Junior reviewers can grow and often help ensure code readability through the questions they ask. In fact, junior engineers are usually the best team members to ensure code readability.

For an engineer who works alone, asking for feedback from outsiders — at meet-ups, GitHub, Open Source Slack Channels, Reddit, Twitter, etc — can allow the solo coder the opportunity to participate in a code review process.

If we could all agree on an established process and language for reviewing code, then maintaining a positive environment for creative and productive engineering is easier. A code review etiquette benefits everyone — whether working alone or within a team.

### [#](https://css-tricks.com/code-review-etiquette/#article-header-id-1)Harsh code reviews can hurt feelings

> Seeing bugs and issues continue to roll in and being mentally unable to address them has led to feelings of failure and depression. When looking at the moment project, I could only see the negatives. The bugs and misnomers and mistakes I had made. It led to a cycle of being too depressed to contribute, which led to being depressed because I wasn't contributing.
>
> - [Tim Wood](https://medium.com/@timrwood/moment-endof-term-522d8965689), creator of Momentjs

There are many online comments, posts, and tweets by prolific engineers expressing that their feelings have been hurt by code reviews. This doesn't directly mean that reviewers are trying to be mean. Feeling defensive is a normal, quite *human* reaction to a critique or feedback. A reviewer should be aware of how the pitch, tone, or sentiment of their comments could be interpreted but the reviewee — see [Occam's Razor](https://simple.wikipedia.org/wiki/Occam%27s_razor).

Although reviewing code is very beneficial, a poor or sloppy review can have the opposite outcome. Avoid criticism without providing context. In other words, take the time to explain why something is wrong, where it went wrong, and how to avoid the mistake moving forward. Showing this level of respect for the reviewee strengthens the team, improves engineering awareness, and helps to provide agreed-upon technical definitions.

### [#](https://css-tricks.com/code-review-etiquette/#article-header-id-2)Quick tips for improving code review etiquette

Code is logical in nature. It is easy to pinpoint code that is incorrect or could be improved, just like it is easy to notice spelling *misteaks*. The human condition, when looking at and discussing logical things (like code), is to disregard the feelings of other people. This causes feelings to get hurt and a loss of focus on learning and collaboration.

Improving *code review etiquette*, because of the human condition, is difficult! Here is a quick list of things that I've done, said, seen, or received, that are easy wins in the art of Code Review Etiquette.

#### [#](https://css-tricks.com/code-review-etiquette/#article-header-id-3)Remove the person

Without realizing it, engineers can neglect the difference between insightful critique and criticism because of [personal relationships in communication](http://dictionary.cambridge.org/us/grammar/british-grammar/pronouns/pronouns-personal-i-me-you-him-it-they-etc).

The lines below dissect a code review comment of a theoretical `function` where it is suggested that there is an opportunity to return out of the function early.

**You and I:** Using *you* or *I* is probably not offensive intentionally, so don't worry. However, over time, involving the person *can* start to feel less positive—especially if vocal tones are ever added.

> You should return out of this function early

**We:** Using `we` is inclusive and a safe way to say something more directly without making someone feel defensive. However, if the person speaking says `we`, and has not worked on the code at all, it may seem falsely inclusive and insensitive.

> We should return out of this function early

**No personal reference:** Without personal reference, conversation or review will closely communicate the problem, idea, or issue.

> Return out of this function early

Notice how the amount of text needed to communicate the same thing without using personal references takes fewer words and has greater clarity. This helps with human interaction, separates code discussion from personal discussion, and fewer words are needed to communicate the same idea.

#### [#](https://css-tricks.com/code-review-etiquette/#article-header-id-4)Keep passionate conversations quiet

Passion is an important motivator for improving. Passion that is critical in nature can be very considerate and motivating. Feedback that is critical in nature is most useful if the person receiving the critique is engaged. This sort of communication comes up a lot during architectural conversations or when discussing new products.

Feedback that is critical in nature is most useful if the person receiving the critique is engaged. **Note:** the person receiving the information **must** be engaged with the critique.

Imagine this comment when stated with exaggerated physical movement, more excited vocal tone, and higher volume.

> There are 8 web fonts used in this mock which may affect page load speed or even certain tracking metrics that could be caused by new race conditions!

Then, imagine a similar comment, even terser but stated with a calm demeanor, slower delivery, and a normal vocal volume — followed by a question.

> There are 8 web fonts used in this mock. This will affect page load speed and possible tracking metrics because of potential race conditions. How can this be improved?

Notice how the comments above are almost the same. The second comment is even more direct. It states a problem as a fact and then requests feedback.

An important thing to remember when being passionate is taking on a quieter tone. This is a physical decision — not a social one. Passionate language can be the same, and perceived very differently, based on the orientation of the communicator's tone. If physical tone (body language), vocal tone, vocal pitch, and vocal volume remain gentle, it is observed that it is much more likely for an audience to remain engaged — even if the critique is critical in nature.

If the tone is aggressive in nature (exaggerated physical movement, more excited vocal tone, higher volume), the actual words used can be gentle in nature, but the audience can feel very differently. This communication can lead to embarrassment, a disengaged audience, and even loss of respect.

Aggressive communication is common with passionate communication because the human condition wants to protect ideas that we're passionate about. So, don't worry about it *too* much if you observe that your audience is disengaged when discussing something that you're passionate about. The key is to remember that if you can create perceived gentle communication, it will be easier for your audience to remain engaged — even if they are not initially in agreement.

#### [#](https://css-tricks.com/code-review-etiquette/#article-header-id-5)Don't review the author, review the code

Following the conversation above, the act of pointing, within written conversation or actual body language, in almost any situation is not optimal for good communication. It changes the focal point of the conversation from the context of the conversation to a person or a thing.

The response below provides a comment and then a link. In the context of the code review, the second part of the comment and link takes the reader out of the context of the code review, which is confusing.

```
// Return out of this function earlier
// You need to learn about functional programming
```

The comment below provides a comment, and then a pseudo-code suggestion.

```
/* 
  return early like this:
*/
const calculateStuff = (stuff) => {
  if (noStuff) return
  // calculate stuff
  return calculatedStuff
}
```

In the two examples above, the first example causes the reader to go far beyond the issue. The conversation is more abstract—even [existential](https://www.merriam-webster.com/dictionary/existential). The second example refers directly to the issue and then provides a pseudo code snippet that relates directly to the comment.

It is best to only comment on contextually specific items when reviewing code. Broad comments lead to a loss of context. If broader discussions must happen, they should happen outside of code reviews. This keeps the code review clear and scoped to the code that is being reviewed.

#### [#](https://css-tricks.com/code-review-etiquette/#article-header-id-6)Right and wrong can change

Developers almost always want to re-write things. It is natural to break problems down into tasks in real-time to address today's situation. However, focusing on the *who's* and *why's* of a product's history is important to conceptualize because great context is gained. 'History repeats itself' is an important phrase to remember when critiquing products or when a product you've written is critiqued. There is always a great amount of knowledge to be gained from historical context.

[JavaScript](https://en.wikipedia.org/wiki/JavaScript#History) was made in a week, considered a hacky scripting language, and then became the [most](https://stackify.com/trendiest-programming-languages-hottest-sought-programming-languages-2017/) [widely](https://stackify.com/trendiest-programming-languages-hottest-sought-programming-languages-2017/) [used programming language](https://stackify.com/trendiest-programming-languages-hottest-sought-programming-languages-2017/) in the world. [Scalable Vector Graphics (SVGs)](https://en.wikipedia.org/wiki/Scalable_Vector_Graphics) were supported in 1999, pretty much forgotten about, and now, they continue to [gain popularity](https://w3techs.com/technologies/details/im-svg/all/all) for the new opportunities they provide. Even the [World Wide Web](https://en.wikipedia.org/wiki/World_Wide_Web) (the Internet) was meant for document sharing with little anticipation of the current result today. All of these technologies are important to remember when considering software and engineering—as logical and predictable results are supposed to be, success is often derived from unexpected results! Be open!

### [#](https://css-tricks.com/code-review-etiquette/#article-header-id-7)Some resources and tools that can help with code review etiquette

- [Alexjs](http://alexjs.com/): a tool for catching insensitive, inconsiderate writing by [Titus Wormer](https://github.com/wooorm)
- [Grammarly](https://app.grammarly.com/): an extension to help improve communication in browsers
- [Write Good](https://github.com/btford/write-good): a cli and text editor plugin by [Brian Ford](https://github.com/btford) to help improve communication in text editors and shells
- [Awesome Writing Tools](https://github.com/heartly/awesome-writing-tools/): an [Awesome List](https://github.com/sindresorhus/awesome) of tools for improving writing.

### [#](https://css-tricks.com/code-review-etiquette/#article-header-id-8)Conclusion

The list above includes general, high-level things that can help with positive engagement when talking about, reviewing, or reading about code—*code review etiquette*.

I am a hypocrite. I have made all the mistakes that I advise *not* to do in this article. I am human. My goal here is to help others avoid the mistakes that I have made, and to perhaps encourage some behavior standards for reviewing code so that engineers can more openly discuss code with less worry about being hurt or hurting others.
