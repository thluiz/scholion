---
title: "Why and How to Avoid Hamburger Menus"
date: '2015-05-29T09:10:06-03:00'
category: webclip
summary: 'The article argues that hamburger or sidebar menus hide navigation, reduce efficiency, clash with iOS patterns, and make state harder to see. It recommends reviewing IA and using visible navigation instead.'
tags: ["hamburger-menu", "mobile-ux", "information-architecture", "navigation"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Why and How to Avoid Hamburger Menus - Louie A. - Mobile UX Design"
    url: "https://lmjabreu.com/post/why-and-how-to-avoid-hamburger-menus"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-05/lmjabreu-com--why-and-how-to-avoid-hamburger-menus.md"
    kind: repo
---

The article says hamburger or sidebar menus create several problems: they hide options by default, make navigation slower, clash with platform patterns like iOS, and make item state harder to understand at a glance. It also notes that hiding navigation for screen space is often a misunderstanding of how people actually perceive interfaces.

## Reading notes

- Sidebar menus hide their contents until people open them, so discoverability drops.
- The pattern adds friction because people must open the menu before reaching their destination.
- On iOS, a burger menu conflicts with the back button and other standard navigation patterns.
- It is harder to show item-specific state or notifications when navigation options are hidden.
- Saving screen space should not come at the cost of navigation or basic HCI principles.
- The article says the general rule is to avoid this pattern, with only rare exceptions.
- IRCCloud is given as a case where the pattern can make sense because the main screen does not need a hierarchical navigation stack.
- Even there, the article says the interface is overloaded and the information architecture should be reconsidered.
- The proposed alternative is to review the information architecture and use visible navigation, such as tabs or a toolbar.
- Visible tabs let state appear directly, keep items instantly accessible, and avoid navigation gesture conflicts.
- For websites on mobile, the article recommends showing navigation in the header as a list instead of hiding it.
- If there are more than five tabs, the article suggests using the last tab for extra options or a scrollable toolbar for actions.
