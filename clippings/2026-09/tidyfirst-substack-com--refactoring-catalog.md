---
url: "https://tidyfirst.substack.com/p/refactoring-catalog?ref=dailydev"
captured_at: "2026-09-25T21:37:01+01:00"
title: "Refactoring Catalog"
domain: "tidyfirst-substack-com"
---

As I write Tidy Together? I’m finding a long list of refactorings I want to cover. Currently for every refactoring I write I find two more I want to write. I’m praying this process converges at some point.

A couple of points:

*   All of the refactorings work bi-directionally, supporting my contention that structure changes are generally reversible. There’s a bias—I extract functions more often than I inline them—but mastery requires using the transformation either way with equal ease.
    
*   The refactorings most naturally cluster according to whether they change the way state is accessed & logic is invoked or whether they change the way state & logic are arranged, interface or implementation.
    

The checked off refactorings have been drafted & sent to paying subscribers for review.

\- Global <-> local state

✅ Constructor <-> Builder

\- Constructor <-> Factory

✅ Method with boolean param <-> 2 methods open, close, (and maybe switch)

depends on how the method is used

\- Common parameter <-> constructor parameter + field

✅ Extract/inline parameter cluster

\- Index access <-> Named access

\- Collection mutation <-> mutation methods

\- Narrow/widen parameter (if you pass foo.x & foo.y, just pass foo. If you only use foo.x, just pass foo.x. Clever trick with extracting everything but the destructuring & then inline)

\- Increase/decrease visibility/scope

\- Literal <-> Constant

\- Flag field <-> subclasses

\- Flag field <-> delegate

\- Move Code To/From Data

\- Boolean in Constructor <-> Subclasses

\- Conditional in code <-> conditional in constructor or factory

✅ Extract/inline fields

\- Static <-> instance

\- Extract/inline function/method

\- Extract/inline method object

\- Move code up/down the call tree (field assignment, conditionals, ???)
