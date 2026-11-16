---
url: "https://dev.to/mlimonczenko/top-10-web-accessibility-standards-every-developer-should-know-5cih"
captured_at: "2026-11-16T01:33:19+00:00"
title: "Top 10 Web Accessibility Standards Every Developer Should Know"
domain: "dev-to"
---

_Article originally published at [Books on Code](https://booksoncode.com/articles/web-accessibility-standards)._

You know that web accessibility standards are important. As a web developer on your team, you want to be knowledgable and committed to applying the most impactful web accessibility standards so that you can create better experiences for everyone.

There is a problem though: the Web Content Accessibility Guidelines (WCAG) are crazy long. The depth of each rule is overwhelming, and with each mind-numbing paragraph you read, you feel farther and farther away from the true goal: creating great experiences for everyone.

At the end of the day, we want to be developing web apps for _people_, not rules. And instead of facing overwhelm, we should be able to pinpoint real changes we can make to our products and websites that we can make _right now_.

While these top web accessibility standards are obviously not an exhaustive list, I hope they give you a starting point to begin thinking about and implementing accessibility standards today.

## [](#overview)Overview

These top web accessibility standards are drawn from the hands-down best book on Web Accessibility, _Practical Web Inclusion and Accessibility_(2019) by Ashley Firth. The book is designed with not any one role in mind, because web accessibility standards are best championed by an entire team. That said, I believe the book is particularly valuable in the hands of a web developer. The book includes many code snippets and simple instructions for developers to implement web accessibility standards.

The book is also designed to help you think critically about solving problems for _people_. As such, the book organizes around various disabilities, both permanent and temporary, with _disability_ defined as people in relationship to the world they interact with. These chapters include blindness, low vision and color blindness, motor disabilities, deafness and hard of hearing, cognitive impairments, mental health, and more, acknowledging that there are still cases outside of the book's coverage.

The crux of the book is about empathy rather than rules or systems, which is the philosophy I take in prioritizing the top skills you see below.

## [](#top-standards-for-blindness)Top Standards for Blindness

> Contrary to common belief, visual impairments need not be a barrier to using the Internet. If websites are well designed, it is easy to include users with sight loss, who can have just as rich an online experience as anyone else.
> 
> \--- Practical Web Inclusion and Accessibility

The following web accessibility standards are particularly beneficial to those who experience blindness. The blind interact with the web typically through screenreading or braile software.

### [](#1-use-semantic-markup-and-landmark-aria-roles)1: Use Semantic Markup and Landmark ARIA Roles

A `div` does not give context to the content it contains, yet we use the `div` all the time. For someone using screenreading software, jumping through a sea of `div`s, they don't have a sense for where they are on the page.

Am I in the beginning, middle, or end?

Am I in a modal or a form?

We have two solutions to offer context to the user: semantic markup and ARIA roles.

**Semantic markup** are tags like `header`, `section`, `main`, `nav`, and `footer`. Tags like `header`, `main`, and `footer` are tags that you can easily add to about any web page.

**ARIA roles** provide context similar to semantic markup. The difference: you can add an attribute to any tag, including a `div`.

For example, `<div role="navigation"></div>` is equivalent to `<nav></nav>`.

For a list of landmark ARIA roles and other ARIA roles, see [Landmark Roles](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/ARIA_Techniques#Landmark_roles) on the MDN Docs site.

### [](#2-include-alt-tags-on-images)2\. Include alt tags on images

Alt tags are valuable for many types of users, and they help users understand what they are unable to perceive.

In my experience user testing with visually impaired user, for example, I worked with a user able to see a large, colorful hero image, but without alt text, they could only wonder what that image was showing.

Writing good alt text can easily be misunderstood, because alt text authors can be tempted to label an image rather than perceive the image.

For official guidelines about alt text, see [Alternative Text](https://webaim.org/techniques/alttext/) on the WebAIM website.

### [](#3-add-a-lang-attribute)3\. Add a Lang Attribute

The `lang` attribute is often forgotten, but it is vital for a user to experience a page on a screenreading device in the language it is intended. A `lang` attribute is placed on the `html` tag. For English, you can set the value to `en`. But you can get even more specific with script and region subtags.

For example:

`<html lang="en">\   ...\   </html>`

For more information about the `lang` attribute, see [lang](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/lang) in the MDN Web Docs.

### [](#4-create-a-skip-to-main-content-link)4: Create a "Skip to main content" link

You can include a link at the top of your document to allow a screenreader user to opt to skip common, repetitive content like the logo and main navigation. The user can instead go straight to your main content. Every time your user goes to a new page, you can improve their experience by giving them an easy navigation option instead of go through the same 'welcome sequence'. This is convenient, like the option of skipping the intro to a series you stream on Netflix.

You can visually hide this link using CSS, but the link is visible when users navigate to it using a keyboard.

To add this link, see the following example:

#### [](#html)HTML:

`<a class="skip-to-content" href="#content">Skip to main content</a>\   <main id="content">...</main>`

#### [](#css)CSS:

`.skip-to-content {\   position: absolute;\   top: -400px;\   }`

## [](#top-standards-for-low-vision-and-color-blindness)Top Standards for Low Vision and Color Blindness

> Because there are so many types and combinations of visual impairment, sometimes there is simply not a one-size-fits-all solution for users. Low vision is one of the rare areas of accessibility where fixing one barrier can actually create another for a different user.
> 
> \--- _Practical Web Inclusion and Accessibility_

Users with low vision or color blindness can be extremely diverse. In my own experience working with low vision users, I found users who both looked at the screen at a magnified size as well as used a screenreader for re-enforcement. In that light, I knew the importance of consistency between the screen and the screenreader.

Despite the varied disabilities users experience, the following web accessibility standards are particularly beneficial for those with low vision or color blindness.

### [](#5-use-relative-units-and-not-pixels-for-font-size)5\. Use Relative Units and Not Pixels for Font Size

Using fixed measurements like pixels can be detrimental to those using magnification. Text sized with pixels will ignore user preferences. If 14px font size is too small, zoom in and it is still too small.

Instead, use measurements like `rem` or `em`. These measurements factor user preference and will allow for a more flexible reading experience.

### [](#6-test-for-color-contrast-and-text-size)6\. Test for Color Contrast and Text Size

High color contrast and text size can improve the experience for all of us, and yet as a way of de-emphasizing text, we still use small text sizes and light-gray-on-white text in our designs. As a rule, we should aim for high contrast and experiment with bumping up our base font size and prioritize readable fonts.

My go-to contrast checker is [Contrast Ratio](https://contrast-ratio.com/).

### [](#7-dont-use-color-alone-to-indicate-status)7\. Don't use Color Alone to Indicate Status

In many designs, colors like red and green are used to indicate status. If these are the only indicators, those with a common type of color blindness may not perceive the difference or find it challenging. It is easier for someone with a red-green deficiency to tell the difference between a light green and a dark red. However, indicating status with a light green _and_ light red may be more difficult to differentiate.

You can use indicators in additionn to color. For example, icons can also serve as an indicator.

## [](#top-web-accessibility-standards-for-motor-disabilities)Top Web Accessibility Standards for Motor Disabilities

> Have you ever tried using a website without a mouse? It's harder than you might think, particularly when trying to perform actions across multiple pages such as signing up for or purchasing something. Some users that have motor disabilities often only use a keyboard to interact with a computer\[.\]
> 
> \--- _Practical Web Inclusion and Accessibility_

The following web accessibility standards are helpful for those who experience motor disabilities and use a keyboard to navigate a web page.

### [](#8-use-focus-styles)8\. Use Focus Styles

By default, an element has a blue glow around it when you use the `tab` button, but many designers might decide to remove this style because they may feel it looks unpleasant. The focus indicator can be removed altogether by using the CSS style `*: focus { outline: 0; }`.

As you can imagine, removing the focus presents a big problem. Having a clear focus style is invaluable, so take considerations for creating both a tasteful and obvious focus indicator. As a developer, it's important to `tab` through your app and notice when focus indicators are not obvious.

Also pay attention to overlays like modals. Make sure that the close button is obvious and accessible using a keyboard.

### [](#9-avoid-content-that-appears-on-hover)9\. Avoid Content that Appears on Hover

In elements such as a drop-down navigation, the hover state is triggered as the area of focus on a keyboard. But there's a problem: when you move off the top-level item, the menu collapses.

In addition, screenreaders do not read content if they have `visibility: hidden` or `display: none` set. If a drop-down navigation is in use, make the element appear invisible but remain visible to screenreaders. You can do this in the same way you would the "Skip to main content" link with absolute positioning. If you solve the problem in this way, keyboards can still reach the content, but it remains invisible. A way to solve this issue is by allowing the menu to expand permanently on click.

## [](#top-standards-for-deafness-and-hard-of-hearing)Top Standards for Deafness and Hard of Hearing

> At a glance, these users experience similar access needs --- auditory information must be communicated in alternative ways. In reality, there is far more to it, and it's important to remember that different deaf users have different preferences about how they receive this information.
> 
> _\--- Practical Web Inclusion and Accessibility_

### [](#10-add-captions-and-caption-actions-using-the-track-element)10\. Add Captions and Caption Actions Using the Track Element

In HTML, you have a lot of control over your captions. Using the HTML `track` element, you can add multiple subtitles files to video in different languages. A common file format for captions is `.vtt` or Web Video Text Tracks Format. For more information about the `track` tag, see [: The Embed Text Track element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/track) in the MDN web docs.

You are also able to style your captions with CSS. The cue rule, which you can target like `video::cue` or `audio::cue` allows you to style the captions themselves.

When you write your captions, it's valuable to keep in mind actions as well as dialog. You can indicate actions with square brackets. For example, `[spits drink]`.

## [](#learn-more-about-web-accessibility-standards)Learn More About Web Accessibility Standards

These ten web accessibility standards are a great set of standards that will allow your site to drastically improve the experience for others today, but there is a lot more to learn, especially when it comes to complex site interactivity with forms and online checkout experiences.

The book, _Practical Web Inclusion and Accessibility_, covers far more. The book is worth the investment if you are looking for web accessibility standards that are both easy-to-understand and implement.

If you liked this article, share this article with your team. Start the conversation to drastically improve the experience of your website or web app. After all, web accessibility is best implemented with the whole team.

Also if you liked this article and have interest in learning and growing as a developer through technical books, keep that learning journey going by signing up for the [Books on Code](https://booksoncode.com/) newsletter.
