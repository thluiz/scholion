---
url: "https://dev.to/rasheedmozaffar/understanding-iqueryable-in-c-4n37?ref=dailydev"
captured_at: "2026-09-25T00:49:26+01:00"
title: "Understanding IQueryable<T> in C#"
domain: "dev-to"
---

## [](#hi-there)Hi There! 👋🏻

You've probably used `IEnumerable<T>`, and most certainly used `List<T>` if you've coded in C# before. These two are very popular and are often presented early to you when you're learning the language. But have you heard of `IQueryable<T>`? This one is a little more advanced, but it's got so much power that you should know about, so you can make good use of it.  
Ladies and gents, we're going on a journey to demystify the `IQueryable` interface, so... Grab a coffee and let's get started! ☕️

## [](#whats-raw-iquyerablelttgt-endraw-)What's `IQuyerable<T>`? 🤔

The `IQueryable` interface is a cornerstone of LINQ, one of C#'s most powerful features. This interface is specifically designed for querying data from various sources that implement `IQueryable<T>`, such as SQL databases or in-memory collections like `List<T>`. What sets `IQueryable` apart are its compelling features that make it versatile and efficient for data querying.

Let's begin by highlighting the features of this interface that do give it this speciality and uniqueness.

## [](#1-deferred-execution)1: Deferred execution 🦥

Deferred execution, which happens to be a feature of `IEnumerable`, also inherited by `IQueryable`, is in simple words, delaying the execution of the query until the data is actually needed. Didn't click? Keep reading.

Let's look at this basic code snippet, to see what deferred execution means in a more hands-on way:  

```

List<FamousPerson> famousPeople =
[
    new FamousPerson(1, "Sandy Cheeks", false),
    new FamousPerson(2, "Tony Stark", true),
    new FamousPerson(3, "Captain Marvel", true),
    new FamousPerson(4, "Captain America", true),
    new FamousPerson(5, "SpongeBob SquarePants", false),
    new FamousPerson(6, "Hulk", false)
];

IQueryable<FamousPerson> famousAndCanFly = famousPeople
    .AsQueryable()
    .Where(x => x.CanFly);

foreach (var fp in famousAndCanFly)
{
    Console.WriteLine($"{fp.Name} can FLY!");
}

record FamousPerson(int Id, string Name, bool CanFly);

```

Enter fullscreen mode Exit fullscreen mode

I want you to copy the code, and use the debugger to see what the value of `famousAndCanFly` evaluates to. You might think it'll be a collection of 3 people, but actually it's not. You will see that the value doesn't carry any data, but once you step inside the `foreach` loop, the results are carried out. This is simply what deferred execution means, the execution is delayed until the data is actually needed (i.e the enumerating of the query results inside the `foreach` loop).

## [](#2-expression-trees)2: Expression trees 🌳

I've chained some additional query filters to the previous query, so now it looks like this:  

```

IQueryable<FamousPerson> famousAndCanFly = famousPeople
    .AsQueryable()
    .Where(x => x.CanFly);

famousAndCanFly = famousAndCanFly
    .Where(x => x.Id < 3);

famousAndCanFly = famousAndCanFly.
    Where(x => x.Name.Contains("s", StringComparison.OrdinalIgnoreCase));

Console.WriteLine(famousAndCanFly.Expression);

```

Enter fullscreen mode Exit fullscreen mode

It's just basic LINQ extension method calls here, but the thing to note is, the console log on the last line. What is the `Expression` property of `IQueryable`? This is basically a tree of expressions, which `IQueryable` puts together as you compose the query. It allows the data source provider, to grab the query expression tree, and translate it into something that can be used against that data source. For that reason, the data source provider has to provide an implementation for `IQueryable`.

If you were to run the previous code, it'd print something like this:  
`System.Collections.Generic.List1[FamousPerson].Where(x => x.CanFly).Where(x => (x.Id < 3)).Where(x => x.Name.Contains("s", OrdinalIgnoreCase))`

See, it's just a bunch of chained query expressions and where statements, which here in our case, the data source happens to be an in memory collection, and since it implements `IQueryable`, you can bet that it knows how to properly translate that into something the in-memory collection can understand.

## [](#examples-of-raw-iqueryable-endraw-functionality)Examples of `IQueryable` Functionality

I said earlier that `IQueryable` is a part of `System.Linq` namespace, and everything LINQ you can do with other collections, can be done on this interface too. From using `Where`, `OrderBy`, `Select` and literally anything else, you can keep on chaining method calls to compose the most complex query you could ever imagine. You're literally just confined by how much LINQ you know.  

```

var filtered = query.Where(x => x.Age > 30);

```

Enter fullscreen mode Exit fullscreen mode

```

var orderedDesc = query.OrderByDescending(x => x.Name);

```

Enter fullscreen mode Exit fullscreen mode

```

 var projected = query.Select(x => new { x.Name, x.Age });

```

Enter fullscreen mode Exit fullscreen mode

```

var firstOrDefault = query.FirstOrDefault();
var lastOrDefault = query.LastOrDefault();
var single = query.Single(); 

```

Enter fullscreen mode Exit fullscreen mode

## [](#3-so-much-optimization)3: So Much Optimization ⚙️

Because the query is structured into a **tree** of expressions, the provider (such as **Entity Framework Core**) can take that expression tree and translate it into a query language appropriate for the data store, such as **SQL** for **SQL Server** or **PostgreSQL**, or **LINQ** for in-memory data stores.

Since the translation is handled by the provider, it can optimize the query for better performance and efficiency. This optimization might involve translating the query into a more efficient SQL statement, applying indexes, or other database-specific optimizations. This allows you to query the data store efficiently without needing to manually optimize each query.

## [](#extending-iqueryable)Extending IQueryable

I was coding a repository for a blog project, and I wanted to add sorting, pagination, and filter by title to the `GetLatestPosts` method. Now while it's possible to cram them in the same method, it'd be much nicer if there's a way to place those methods into a centric place, and just chain call them to compose that perfect query. Enter Extension methods!

> ⚠️ Extension methods are not something specific to IQueryable only, they can be used to extend any type.

Before I show you the extension methods code, I'd like to show you the refactored code, and how the improved version actually looks like:  

```

public async Task<PaginatedReadOnlyCollection<Post>>
    GetLatestPostsAsync(int pageNumber, int pageSize, string? title, PostSortOption sortOption, CancellationToken cancellationToken)
{
    try
    {
        var query = db.Posts.AsQueryable();

        var filteredQuery = query.ApplyFilter(title);
        var sortedQuery = filteredQuery.ApplySorting(sortOption);

        var totalCount = await filteredQuery.CountAsync(cancellationToken);
        var posts = await sortedQuery
            .ApplyPagination(pageNumber, pageSize)
            .Execute(cancellationToken);

        var paginatedPosts = new PaginatedReadOnlyCollection<Post>(
            totalCount,
            pageNumber,
            pageSize,
            posts.AsReadOnly()
        );

        return paginatedPosts;
    }
    catch (OperationCanceledException)
    {
        logger.LogInformation("Loading posts was cancelled");
        return PaginatedReadOnlyCollection<Post>.Empty(pageNumber, pageSize);
    }
}

```

Enter fullscreen mode Exit fullscreen mode

This is a lot of code I know, but the main focus here is the 4 methods that aren't LINQ methods.  
`ApplyFilter(string)`, `ApplySorting(PostSortOption)`, `ApplyPagination(int, int)`, and `Execute(CancellationToken)`.

All these methods are extension methods I wrote to extend on `IQueryable<Post>`, which makes it much cleaner and more concise to write and compose large queries on the `Post` data model.

Here's the code inside `PostsQueryExtensions.cs` which hosts those extension methods we just discussed:  

```

public static class PostsQueryExtensions
{
    public static IQueryable<Post> ApplyFilter(this IQueryable<Post> query, string? title)
    {
        if (!string.IsNullOrEmpty(title))
        {
            query = query.Where(post => post.Title.Contains(title, StringComparison.OrdinalIgnoreCase));
        }

        return query;
    }

    public static IOrderedQueryable<Post> ApplySorting(this IQueryable<Post> query, PostSortOption sortOption)
    {
        return sortOption switch
        {
            PostSortOption.MostComments => query.OrderByDescending(p => p.Comments.Count),
            PostSortOption.MostLiked => query.OrderByDescending(p => p.LikeCount),
            PostSortOption.MostViews => query.OrderByDescending(p => p.Views),
            _ => query.OrderByDescending(p => p.PublishedOn)
        };
    }

    public static IQueryable<Post> ApplyPagination(this IQueryable<Post> query, int pageNumber, int pageSize)
    {
        return query
            .Skip((pageNumber - 1) * pageSize)
            .Take(pageSize);
    }

    public static async Task<List<Post>> Execute(this IQueryable<Post> query, CancellationToken cancellationToken)
        => await query.ToListAsync(cancellationToken);
}

```

Enter fullscreen mode Exit fullscreen mode

As you can see, all these methods extend on the query and return an updated version of it, essentially, composing the entire query before finally the `Execute` method pulls the trigger, and calls `ToListAsync` which in turn, grabs the results of the entire query and enumerates them such that the calling code can read and display the results.

## [](#conclusion)Conclusion ✅

In this post, we went over the `IQuyerable` interface, from the basics, highlighting key features of it, showing you code samples of how it's used, and lastly we saw how we can extend on this interface for a given data model so that we can facilitate and make writing complex querying code less redundant, more fluent and concise.  
I hope that post was a good introductory to this powerful interface, I hope it was useful and you ended up learning something!

If you got any feedback on the code provided in the post, please feel free to point them out!

## [](#thanks-for-reading)**Thanks for reading!**
