---
url: "http://blogs.msdn.com/b/windowsappdev/archive/2012/07/11/creating-metro-style-apps-that-stand-out-from-the-crowd.aspx"
captured_at: "2012-07-13T11:10:44-03:00"
title: "Creating Metro style apps that stand out from the crowd - Windows 8 app developer blog - Site Home - MSDN Blogs"
domain: "blogs-msdn-com"
---

### Creating Metro style apps that stand out from the crowd

Rate This  
[anexo ausente][anexo ausente][anexo ausente][anexo ausente][anexo ausente][anexo ausente][anexo ausente][anexo ausente][anexo ausente][anexo ausente]

[Windows 8 Team](http://blogs.msdn.com/414389/ProfileUrlRedirect.ashx)

Windows 8 Team

5,420 Points122

Recent Achievements

Blog Party StarterBlogger IIIBlogger II

[View Profile](http://social.msdn.microsoft.com/profile/windows%208%20team/?ws=usercard-hover)

Wednesday, July 11, 2012 6:17 PM

- Comments[12](http://blogs.msdn.com/b/windowsappdev/archive/2012/07/11/creating-metro-style-apps-that-stand-out-from-the-crowd.aspx#comments)

When you submit your app into the Store, there will no doubt be other apps in your category that will compete for people’s attention. Being able to crisply showcase the differentiation points in your offerings and staying focused on delivering the core scenarios that you are best at are crucial to a successful Metro style app that will stand out from the crowd.

Windows 8 provides a set of [design patterns](http://msdn.microsoft.com/en-us/library/windows/apps/hh770552.aspx), [common controls](http://msdn.microsoft.com/en-us/library/windows/apps/hh465424#ui_controls), and built-in platform functionalities such as [contracts](http://msdn.microsoft.com/en-us/library/windows/apps/hh465424#contracts_and_capabilities) that can help you focus on what you are best at. For example, just to name a few: the [app bar](http://msdn.microsoft.com/en-US/library/windows/apps/hh465302) is a common control that helps people focus on your content and minimize distractions; the [touch pattern](http://go.microsoft.com/fwlink/?LinkId=242592) prescribes a set of gestures that are used consistently in platform controls, such as swiping from the edge to bring up the app bar, so that people can focus on confidently use your app without having to learn new interfaces; the [Share contract](http://msdn.microsoft.com/en-US/library/windows/apps/hh465251) is the glue that lets two apps work together so that users can accomplish more with your content.

This post is a little different from some of the other posts – rather than talking about coding patterns, we talk about design patterns that you can use in your planning process. I introduce an example app, Food with friends, and start by answering the question that is key to standing out from the crowd: “What is my app best at in its category?”. Then I illustrate some practical steps to designing the app’s structure and layout to highlight the core scenarios and differentiation points that it is best at. This is the first in a series of occasional posts that will come over the next few months. The later posts will continue to use this app as an example and walk through ways that you can take advantage of these various aspects of the Windows 8 platform to create experiences that feel immersive, crafted, fast, and fluid.

Let’s get started!

### Example: Food with friends

Say we are building an app that helps people find restaurants. Let’s look at the design process for this app.

#### 1. Identifying the differentiation points

We will start by identifying a focus that will allow to differentiate ourselves from other competitors in the restaurant and dining category:

**My app is the best in its category at *helping users and their friends find a restaurant to eat at tonight.***

The unique point of view of this app is on helping users *and their friends* and dining *tonight*. This app will revolve around getting friends to agree on a place to eat, and will focus on bubbling up friends’ preferences so a user can take them into account when making decisions. This emphasis makes our app stand out from other generic apps in the same category that may simply be providing local restaurant listings.

This “best-at” statement describes the reasons why user will want to buy this app and not a competitor’s in the same category. We will be referring back to it many times as we make design trade-offs and decide on which feature set and platform functionalities to use.

Given this, let’s call this app *Food with friends*.

#### 2. Picking the right scenarios

Next, let’s identify the core scenarios our app will focus on based on our best-at statement. In the process of brainstorming and selecting scenarios, there may be a great number of interesting ones that we could support (such as seeing nutritional value of dishes). But to actually deliver the unique, differentiated, best-in-class experience that our best-at statement promises, we must say no to them if they don’t tie back to our vision. Based on that, here are the core scenarios that this app will be great at:

- Find restaurants that I want to eat at
- Find restaurants that my friends want to eat at
- Make dinner plans for tonight with friends

We want to start by thinking about scenarios that describe why people want to use the app, before we start thinking about features, which are how they will achieve those goals. Each of our scenarios will encompass a number of features. When we know what the core scenarios are, we can then think about features that will enable those scenarios. We will get to more details on feature selection and design in the next post, but here are some examples of possible features:

- Find restaurants that I want to eat at:
- - Browse restaurants on a map or in a list
  - Search by name or keyword
  - Filter/Sort by category, price and rating
  - Add/remove restaurants to/from wishlist

#### 3. Creating the landing experience

The landing page is the key to any Metro style app. It is your chance to tell your user what your app is best at. When users open your app you want them to immediately understand what your app’s core scenarios are and how they deliver unique values. A good landing page motivates users to open the app by always providing new and up to date content, and convinces them to stick around and spend more time in the app. It is like a hub, the center of interest and shows the best of the app.

Designing a great hub is about creating a layout that optimizes for bringing content and functionality to people in an easy to explore way. Typical navigation in apps or on the web involves showing a default section of an app, and then relies on users choosing to go to a new section from a navigation bar or table of contents. The trouble with this pattern is that it doesn’t encourage exploration. In order for people to decide to click a tab and navigate to a new section, they need to believe that there is something in there that would be interesting or useful to them. If there are no interesting sections, they’ll switch to another app. For example, this newsreader app uses a tab-based design where people land in a single section, but then have to consciously make a decision to navigate to other sections of the app just based on the name. You cannot tell if any of those 4 other sections are interesting until you switch to it:

Instead, convert this to a hub and simply add panning, which requires no hard decision from users at all, and they will *see* why the content or functionality of the app is interesting to them.

By laying out the app so it’s easy to explore, we show users why they should stick around. We show them the full breadth of what our app is best at.

So with that in mind, let’s start with a basic hub layout using the Visual Studio Grid project template ([XAML](http://msdn.microsoft.com/en-us/library/windows/apps/xaml/Hh768232(v=win.10).aspx), [HTML](http://msdn.microsoft.com/en-us/library/windows/apps/hh758331.aspx#grid_project_template_for_metro_style_apps)). Its landing page (the groupedItemsPage) has a number of sections and selected items from each one:

We want this page to really represent the best-at statement of: *My app is the best in its category at helping users and their friends find a restaurant to eat at tonight*. The first step is to make each section of our hub represent one of our three core scenarios. Each core scenario must be represented (though there could be multiple sections that tie back to a scenario):

|  |  |
| --- | --- |
| **1. Tonight** | Focuses on making dinner plans for tonight with friends |
| **2. Friends’ wishlists** | Focuses on finding restaurants that my friends want to eat at |
| **3. My wishlist** | Focuses on finding restaurants that I want to eat at |
| **4. All Restaurants** | Also focuses on finding restaurants that I want to eat at |

The order of the sections is strategic. The reason tonight is first is because it is the most relevant section to what is going on *right now* and so it is likely to change every time you open the app. Info about tonight is also a great candidate for live tile content because it’s fresh, personal and relevant. This lineup means that if people see what is happening tonight on the app’s live tile on the Start screen, they can open the app and see the content they just saw on the live tile right on the hub page. Your app should reward users for opening the app with info that’s new and most important to them. For more on live tiles take a look at Kevin Michael Woley’s [Creating a great tile experience](http://blogs.msdn.com/b/windowsappdev/archive/2012/04/16/creating-a-great-tile-experience-part-1.aspx) post.

Next we put Friends’ wishlists, and then My wishlist – these are in that order for two reasons:

- The focus of Food with friends is on my friends – that’s the differentiator, and is what Food with friends does that nobody else does in quite the same way.
- Like the Tonight section, others will update their wishlists while a user is away from the app and so it can change often. It contains info user doesn’t know, while they are more familiar with their own wishlists and so it is less critical to explore it.

We put All restaurants at the end. We expect users to go to this section only when they want to manage their wishlist, but according to our best at statement, most of the time users will be making decisions about where to go *tonight* which means most of the time they will be looking at the wishlists that are already there and at the suggestions for tonight. Having it at the end also provides a nice benefit that the section can expand as long as you like, without pushing off other content. You may be concerned that All restaurants is so far over, but don’t be. Quickly jumping through a list is what [Semantic Zoom](http://msdn.microsoft.com/en-us/library/windows/apps/hh465319) is for.

#### 4. Designing the sections

A key to designing a section to optimize it for its corresponding scenario. It doesn’t need to be a uniform grid of tiles across the whole hub! This is where we can get creative, demonstrate how our app is different from others and bring forward what our app is best at. We also don’t have to show all items in a given section on the landing page because that may be overwhelming. Instead we may want to only bubble up a curated set of items that are the most relevant and up-to-date. For example, we show only the top friends under Friends’ wishlist, and the most recently added restaurants under My Wishlist.

For this app, the first section, Tonight, is all about deciding with your friends where to eat *tonight*. Because this requires collaboration between your friends and you, this is best as a discussion:

My friend’s wishlist is all about *my friends* and what they want, so in that section, let’s really make it about the people!

For my wishlist, it’s about the restaurants that I’m most interested in going to, so we bring the restaurant forward:

And lastly, All restaurants is about navigating the giant collection of restaurants that is out there, so let’s present some of the most popular ones that users might be interested in, and then present categories for easy browsing. With all these parts in place, you can now see how the app’s hub landing page now looks:

A crucial part to delivering a differentiated experience is expressing your product’s brand. This is a topic that deserves its own post, so stay tuned for a deeper dive into layout and visual design tips and techniques that will help your brand’s personality shine through while still maintaining a look and feel consistent with the platform it is created for. For now, let’s take a look at a simple example:

#### 5. Laying out the rest of your app

Now that we have our landing page, it is really easy to lay out the rest of the app.

We know that not all of the sections in the hub were exhaustive, so we need pages entirely dedicated to showing the full set of content for each section. The groupDetailPage in the Visual Studio Grid template is designed for this purpose. We tailor the layout of the [ListView](http://msdn.microsoft.com/en-us/library/windows/apps/xaml/Hh780650(v=win.10).aspx) on that page to best suit the content type.

My friend’s wishlist:

My wishlist:

All restaurants:

We also know that there are two core entities reflected on the hub: restaurants and people. That means we need two variants of the item detail page (itemDetailPage in the Grid project template) where users can see info on an item when they tap/click it:

When designing each page, it is just as critical to continue to think about what each page is trying to be best at, and how it contributes to helping your app deliver on its “best at” statement.

#### 6. Navigating the UI

Now that we have the various pages, all we need to do is provide the user a way to move between them. Navigating the UI is quite unlikely the thing that any app is designed to be best at. We can apply existing [navigation patterns](http://msdn.microsoft.com/en-us/library/windows/apps/hh761500.aspx) that users already know so they can quickly get to our app’s content and functionality. In this example, we use the Grid project template, which follows the hierarchical system pattern. For example, tapping a tile takes you to the item’s detail page. Tapping a section header in the hub takes you to that section. Tapping back takes you to where you just came from (not up). Much of this is built into the Grid project template. In a future post, we will go into more depth on the implementation and tips for building more advanced in-app navigation.

#### Summary

Figuring out what you are best in its category at is the first and most important step to creating great Metro style app that will stand out from the crowd. As we have seen, identifying and focusing on the differentiation points influences many foundational decisions that you will make around your content structure, landing experience, page layout, and navigation. In future posts, we will continue to build on this and show how you can use the Windows 8 platform to make your app the best in its category. To review some of the resources that are mentioned in this post, take a look at the content on [http://design.windows.com](http://design.windows.com/).

-- Bonny Lau, Senior Program Manager, Windows

![fe3562413883fd118347d60e153f99d1.jpg](blogs-msdn-com--creating-metro-style-apps-that-stand-out-from-the-crowd/fe3562413883fd118347d60e153f99d1.jpg)
