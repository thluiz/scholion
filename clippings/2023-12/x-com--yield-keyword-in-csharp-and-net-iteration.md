---
url: "https://x.com/mwaseemzakir/status/1736621427900436567?s=20"
captured_at: "2023-12-18T05:36:27+00:00"
title: "Muhammad Waseem (@mwaseemzakir) on X"
domain: "x-com"
---

Have you heard about yield keyword, yield keywords works with return and break statement like:

yield return;
yield break;

Yield is used for custom statefull iteration over .NET collections.

Let me explain with an example. Suppose you want to check even numbers b/w 1-1000

Scenario 1 : One solution would be iterate over all numbers and keep saving in a list and then let the caller know about that list by returning it

Scenario 2 : Second solution could be keep iterating and let the caller know at the same time which number is even or odd.

So in second scenario yield comes into action and helps us. It basically return an IEnumerable.

After C# 8 we have facility of IAsyncEnumerable as well.

We have some restrictions with yield:

1) Methods with ref, in and out parameter are not allowed to use yield.

2) Lambda expressions and anonymous methods can not contain yield.

Additionally yield works on lazy pattern, list would not be retrieved until one iterates with for loop or uses ToList.

How often do you use them in code ?

If you have enjoyed this post, you would love to read my Weekly .NET Newsletter where I send a weekly update about C# or .NET every Saturday.

Join with 8600+ : https://lnkd.in/dNHxJGRG

Repost ♻️ if this post is helpful.
