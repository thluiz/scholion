---
url: "https://web.archive.org/web/20200808061719id_/https://killalldefects.com/2020/01/21/dotnet-linq-groupby-in-depth/"
captured_at: "2026-11-16T08:00:46+00:00"
title: "LINQ GroupBy in Depth - Kill All Defects"
domain: "web-archive-org"
---

Let’s talk about how LINQ’s `GroupBy` method makes grouping data in C# easy. We’ll start basic and then go over every available overload of the `GroupBy` method to explore advanced use cases.

`GroupBy` allows you to quickly group collections of related data by specific properties on your data. The grouped data is then arranged by sub-collections of items in those groups.

_Note: LINQ provides variants of each method in this article that work with either `IEnumerable` or `IQueryable`. These methods are otherwise identical, so for the purposes of this article we will ignore the difference in data source type._

## Simple Grouping

Let’s take a look at a sample involving a small data set of books:

![](https://i1.wp.com/killalldefects.com/wp-content/uploads/2020/01/BooksJson.png?resize=385%2C512&ssl=1)

Assuming I have this data loaded into a collection of `IEnumerable<Book>` called `books`, I can then use `GroupBy` to group items by various properties by specifying the _key selector_.

For example, I’ll group by author by using `books.GroupBy(b => b.Author)`

This results in an `IEnumerable<IGrouping<string, Book>>`. Don’t let that return type scare you – it just means a collection of groups where each group is based on a string value (whatever value your key selector returned) and contains `Books` objects.

If _that_ is a mouthful, let’s look at the following:

![](https://i0.wp.com/killalldefects.com/wp-content/uploads/2020/01/BooksGroupedJson.png?fit=680%2C1024&ssl=1)

Essentially, we split our collection into multiple sub-collections, and each one of those has a `Key` property of whatever type we grouped on, and itself serves as an `IEnumerable<T>` that allows us to enumerate over the items in the group.

* * *

## GroupBy Element Selectors

If we you don’t want the entire body of the grouped item in the sub collection, you can use the overload that also takes in an _element selector_. The element selector is just a function that selects the part of the object that the grouped element will contain.

For example, if in our earlier example I did `books.GroupBy(b => b.Author, b.Title)`, I would get a collection of groups by author that then contained only string values for titles by that author:

![](https://i2.wp.com/killalldefects.com/wp-content/uploads/2020/01/BooksTitlesGrouped.png?resize=392%2C284&ssl=1)

Admittedly, the results here look a little odd when serialized to JSON. This is because the group key is _not_ included in the serialized results and so we don’t see the author listed. Rest assured that you could still getting at the author by looking at the `Key` property of each group.

* * *

## Result Selectors

Now we’ve seen how to work with key and value selectors, let’s introduce a third type of selector: _result selectors_.

Result selectors let you customize the generated collection. Instead of working with an `IGrouping<TKey, TValue>` you can effectively project the collection into whatever shape you’d like it to be in.

Let’s use this to address the serialization quirk we saw with the last example:

![](https://i0.wp.com/killalldefects.com/wp-content/uploads/2020/01/BookGroupProject.png?fit=770%2C156&ssl=1)

Here we select the author and title for key and value, like we did before, but now we project each group into a new anonymous type, setting an Author property to the key of each group and setting the groups collection to the collection of title values.

The end JSON is much more useful for representing our group:

![](https://i0.wp.com/killalldefects.com/wp-content/uploads/2020/01/BooksByAuthor.png?resize=409%2C450&ssl=1)

I should point out an important point here – with this overload, we are no longer returning an `IEnumerable<IGrouping<TKey, TValue>>` but rather an `IEnumerable<TProjected>` where `TProjected` is whatever the result of our result selector is.

* * *

## Equality Comparer

The last possible parameter to `GroupBy` is an equality comparer. Comparers are used when determining which group an item belongs in and can be helpful to use if you have data that is not being grouped properly.

For example, let’s say that your data has a few rows with different casing for the same author:

*   Michael Crichton
*   michael crichton
*   Michael CRichton

We can pass in an `IEqualityComparer<TKey>` that will be used to compare various key values. Since our key, author, is a string value, we need an `IEqualityComparer<string>`.

Thankfully, .NET ships with several of these built in to the `StringComparer` class. In our case, we’ll use `StringComparer.CurrentCultureIgnoreCase` to compare our authors:

![](https://i1.wp.com/killalldefects.com/wp-content/uploads/2020/01/BookComparer.png?w=770&ssl=1)

Using the comparer in this way will ignore any casing differences between author entries.

* * *

You may be wondering which key value is used if multiple values can compare to the same group. The answer is that LINQ uses the first value encountered in that group as the official group key. This means that even if you use a `StringComparer` to ignore casing differences, you could still wind up with a key value that might not match the ideal formatting.

This is why I would advocate that if you consider using an `IEqualityComparer` you should also think about cleaning up and normalizing your data source instead.

That said, if you need to group elements on some criteria other than reference equality, implementing a custom `IEqualtyComparer` can be the way to go. I would expect, however, that these cases would be few and far between.

* * *

## Closing Thoughts

Before writing this article, I found the `IGrouping` result too inconvenient to work with and iterate over and largely avoided LINQ `GroupBy` syntax.

Upon fully exploring this method and its overloads, I think there are a number of compelling reasons to use `GroupBy`, particularly the variant that allows you to project groups into custom objects and formats.

If you still have questions or would like to learn more about the material in question, take a look at [MSDN’s documentation on the GroupBy method](https://docs.microsoft.com/en-us/dotnet/api/system.linq.enumerable.groupby).

Whether `GroupBy` joins your set of tools you frequently use or not, it is a powerful and capable component of LINQ and a tool to keep in mind.
