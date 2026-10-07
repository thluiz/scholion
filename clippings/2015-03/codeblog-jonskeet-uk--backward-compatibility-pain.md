---
url: "http://codeblog.jonskeet.uk/2015/03/02/backward-compatibility-pain/"
captured_at: "2015-03-04T11:41:45-03:00"
title: "Backward compatibility pain"
domain: "codeblog-jonskeet-uk"
---

# Backward compatibility pain

I’ve been getting a bit cross about backward compatibility recently. This post contains two examples of backward incompatibilities in .NET 4.6, and one example of broken code which isn’t being fixed due for backward compatibility reasons.

Let me start off by saying this post is not meant to be seen as an attack on Microsoft. I suspect that some people will read that first sentence as “This post is an attack on Microsoft, but I don’t want to say so.” It really isn’t. With my naturally positive disposition, I’m going to assume that the people behind the code and decisions in the examples below are smart people who have more information than I do. Their decisions may prove annoying to me personally, but that doesn’t mean those decisions are bad ones for the world at large.

The purpose of this post is partly just because I think readers will find it interesting, and partly to show how there are different things to consider when it comes to backward compatibility in APIs.

# Example 1: Enumerable.OrderByDescending is broken

`OrderByDescending` is broken when three facts are combined unfortunately:

- `IComparer.Compare` is allowed to return *any* integer value, including `int.MinValue`. The return value is effectively meant to represent one of three results:
  - the first argument is “earlier than” the second (return a negative integer)
  - the two arguments are equal in terms of this comparison (return 0)
  - the first argument is “later than” the second (return a positive integer)
- `-int.MinValue` (the unary negation of `int.MinValue`) is still `int.MinValue`, because the “natural” result would be outside the range of `int`. (Think about `sbyte` as being in the range -128 to 127 inclusive… what would `-(-128)` in `sbyte` arithmetic return?)
- `OrderByDescending` uses unary negation to attempt to reverse the order returned by an “ascending” comparer.

I’ve [blogged about this before](http://codeblog.jonskeet.uk/2011/01/25/reimplementing-linq-to-objects-part-39-comparing-implementations/), but for the sake of completeness, here’s an example showing that it’s broken. We use a custom comparer which delegates to a normal string comparer – but only ever returns `int.MinValue`, `0` or `int.MaxValue`. Just to reiterate, this is an entirely legitimate comparer.

|  |  |
| --- | --- |
|  | `using` `System;`  `using` `System.Collections.Generic;`  `using` `System.Linq;`  `class` `OrderByDescendingBug`  `{`  `static` `void` `Main()`  `{`  `var` `comparer =` `new` `MaximalComparer<``string``>(Comparer<``string``>.Default);`  `string``[] input = {` `"apples"``,` `"carrots"``,` `"dougnuts"``,` `"bananas"` `};`  `var` `sorted = input.OrderByDescending(x => x, comparer);`  `Console.WriteLine(``string``.Join(``", "``, sorted));`  `}`  `}`  `class` `MaximalComparer<T> : IComparer<T>`  `{`  `private` `readonly` `IComparer<T> original;`  `public` `MaximalComparer(IComparer<T> original)`  `{`  `this``.original = original;`  `}`  `public` `int` `Compare(T first, T second)`  `{`  `int` `originalResult = original.Compare(first, second);`  `return` `originalResult == 0 ? 0`  `: originalResult < 0 ?` `int``.MinValue`  `:` `int``.MaxValue;`  `}`  `}` |

We would *like* the result of this program to be “doughnuts, carrots, bananas, apples” but on my machine (using .NET 4.6 from VS2015 CTP6) it’s “carrots, dougnuts, apples, bananas”.

Naturally, when I first discovered this bug, I [filed it in Connect](https://connect.microsoft.com/VisualStudio/feedback/details/634949/orderbydescending-fails-in-linq-to-objects-when-a-comparer-returns-int-minvalue). Unfortunately, the bug has been marked as closed. This comment was logged in 2011:

> Swapping arguments in the call to comparer.Compare as you point out would be the most straightforward and general way to support this. However, while well-behaved implementations of comparer.Compare should handle this fine, there may be some implementations out there with subtle bugs that are not expecting us to reverse the order in which we supply these arguments for a given list. Given our focus on runtime compatibility for the next release, we won’t be able to fix this bug in the next version of Visual Studio, though we’ll definitely keep this in mind for a future release!

## Fast, backward compatible, correct – pick any two

The clean solution here – reversing the order of the arguments – isn’t the only way of correcting it. We could use:

|  |  |
| --- | --- |
|  | `return` `-Math.Sign(original.Compare(x, y));` |

This still uses unary negation, but now it’s okay, because `Math.Sign` will only return -1, 0 or 1. It’s very slightly more expensive than the clean solution, of course – there’s the call to `Math.Sign` *and* the unary negation. Still, at least it works.

What I object to here is the pandering to *incorrect* code (implementations of `IComparer` which don’t obey its contract, by making assumptions about the order in which values will be passed) at the expense of *correct* code (such as the example above; the use of `int.MinValue` is forced here, but it can crop up naturally too – in a far harder-to-reproduce way, of course). While I can (unfortunately) believe that there are implementations which really are that broken, I don’t think the rest of us should have to suffer for it. I don’t think we should have to suffer at all, but I’d rather suffer a slight piece of inefficiency (the additional `Math.Sign` call (which may well be JIT-compiled into a single machine instruction – I haven’t checked) than suffer the current correctness issue.

# Example 2: `TimeZoneInfo` becomes smarter in .NET 4.6

A long time ago, Windows time zones had no historical information – they were just a single pair of rules about when the zone started and stopped observing daylight saving time (assuming it did at all).

That improved over time, so that a time zone had a set of adjustment rules, each of which would be in force for a certain portion of history. This made it possible to represent the results of the [Energy Policy Act of 2005](http://en.wikipedia.org/wiki/Energy_Policy_Act_of_2005#Change_to_daylight_saving_time) for example. These are represented in .NET using [`TimeZoneInfo.AdjustmentRule`](https://msdn.microsoft.com/en-us/library/system.timezoneinfo.adjustmentrule), which is slightly under-documented and has [suffered from some implementation issues](http://codeblog.jonskeet.uk/2014/09/30/the-mysteries-of-bcl-time-zone-data/) in the past. (There’s also the matter of the data used, but I treat that as a different issue.)

Bugs aside, the properties of `TimeZoneInfo` and its adjustment rules allowed an interested developer (one wanting to expose the same information in a different form for a [better date/time API](http://nodatime.org/), as one *entirely* arbitrary example) to predict the results of the calculations within `TimeZoneInfo` itself – so the value returned by a call to [`TimeZoneInfo.GetUtcOffset(DateTime)`](https://msdn.microsoft.com/en-us/library/bb396378) could be predicted by looking at the standard UTC offset of the time zone, working out which rule was in effect for the specified `DateTime`, working out if that rule means that DST was being observed at the time, and adjusting the result accordingly.

As of .NET 4.6, it appears this will no longer be the case – not in a straightforward manner. One aspect of inflexibility in `TimeZoneInfo` is being eliminated: the inability to change standard offset. In the past, if a time zone changed its understanding of “standard time” ([as the UK did between 1968 and 1971](http://en.wikipedia.org/wiki/British_Summer_Time#Periods_of_deviation), for example), that couldn’t be cleanly represented in the `TimeZoneInfo` data model, leading to some very odd data with “backward” DST offsets to model the situation as nearly as possible.

Now, it seems that each adjustment rule also “knows” the difference between its standard offset and that of the zone as a whole. *For the most part, this is a good thing.* However, it’s a pain for anyone who works with `TimeZoneInfo.AdjustmentRule` directly, as the information simply isn’t available on the rule. (This is only a CTP of .NET 4.6, of course – it might become available before the final release.)

Fortunately, one can *infer* the information by asking the zone itself for the UTC offset of one arbitrary point in the adjustment rule, and then compare that with what you’d predict using just the properties of `TimeZoneInfo` and `AdjustmentRule` (taking into account the fact that the start of the rule may already be in DST). So long as the rule performs its internal calculations correctly (and from what I’ve seen, it’s now a lot better than it used to be, though not *quite* perfect yet) we can predict the result of `GetUtcOffset` for all other `DateTime` values.

It’s not clear to me why the information isn’t just exposed with a new property on the rule, however. It’s a change in terms of what’s available, sure – but anyone using the new implementation directly would have to know about the change anyway, as the results of using the exposed data no longer match the results of `GetUtcOffset`.

# Example 3: `PersianCalendar` and leap years

If you thought the previous two examples were obscure, you’ll love this one.

[`PersianCalendar`](https://msdn.microsoft.com/en-us/library/system.globalization.persiancalendar) is changing in .NET 4.6 to use a more complicated leap year formula. The currently *documented* formula is:

> A leap year is a year that, when divided by 33, has a remainder of 1, 5, 9, 13, 17, 22, 26, or 30.

So `new PersianCalendar().IsLeapYear(1)` has always returned `true` – until now. [It turns out](https://github.com/dotnet/coreclr/issues/353) that Windows 10 is going to support the Persian Calendar (also known as the [Solar Hijri calendar](http://en.wikipedia.org/wiki/Solar_Hijri_calendar)) in certain locales, and it’s going to do so “properly” – by which I mean, with a more complex leap year computation. This is what’s known as the “astronomical” Persian calendar and it follows the algorithm described in [Calendrical Calculations](http://www.amazon.com/Calendrical-Calculations-Nachum-Dershowitz/dp/0521702380). The BCL implementation is going to be consistent with that Windows calendar, which makes sense.

It’s worth noting that this calendar has the same leap year pattern as the “simple” one for over 320 years around the modern era (Gregorian 1800 to Gregorian 2123) so it’s really only people dealing with long-past dates in the Persian calendar who will notice the difference. Of course, I noticed because I have a unit test checking that my implementation of the Persian calendar in Noda Time is equivalent to the BCL’s implementation. It was fine until I installed Visual Studio 2015 CTP6…

As it happens, there’s *another* Persian calendar to consider – the “arithmetic” or “algorithmic” Persian calendar proposed by Ahmad Birashk. This consists of three hierarchical cycles of years (either cycles, subcycles and sub-subcycles or cycles, grand cycles and great grand cycles depending on whether you start with the biggest kind and work in, or start at the smallest and work out).

For Noda Time 2.0, I’m now going to support all three forms: simple (for those who’d like compatibility with the “old” BCL implementation), astronomical and arithmetic.

# Conclusion

Backwards compatibility is hard. In all of these cases there are reasons for the brokenness, whether that’s just brokenness against correctness as in the first case, or a change in behaviour as in the other two. I think for localization-related code, there’s probably a greater tolerance of change – or there should be, as localization data changes reasonably frequently.

For the second and third cases, I think it’s reasonable to say that compatibility has been broken in a reasonable cause – particular for the second case, where the time zone data can be *much* more sensible with the additional flexibility of changing the UTC offset of standard time over history. It’s just a shame there’s fall-out.

The changes I would make if I were the only developer in the world would be:

- Fix the first case either by ignoring broken comparer implementations, or by taking the hit of calling `Math.Sign`.
- Improve the second case by adding a new property to `AdjustmentRule` and publicising its existence in large, friendly letters.
- Introduce a new class for the third case instead of modifying the behaviour of the existing class. That would certainly be best for *me* – but for most users, that would probably introduce more problems than it solved. (I suspect that most users of the Persian calendar won’t go outside the “safe” range where the simple and astronomical calendars are the same anyway.)

One of the joys of working on Noda Time 2.0 at the moment is that it’s a new major version and I *am* willing to break 1.x code… not gratuitously, of course, but where there’s good reason. Even so, there are painful choices to be made in some cases, where there’s a balance between a slight ongoing smell or a clean break that might cause issues for some users if they’re not careful. I can only imagine what the pain is like when maintaining a large and mature codebase like the BCL – or the Windows API itself.
