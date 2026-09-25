---
url: "https://toreaurstad.blogspot.com/2024/10/partition-methods-for-collections-in-c.html?m=1&utm_source=newsletter.csharpdigest.net&utm_medium=newsletter&utm_campaign=using-windows-error-reporting-in-net&_bhlid=f27099d53236b8833e46834f463dd985bcc3801d"
captured_at: "2026-09-25T21:38:52+01:00"
title: "Partition methods for collections in C#"
domain: "toreaurstad-blogspot-com"
---

This article will look at some partition methods for collections in C#, specifically List<T>, ConcurrentDictionary<TKey, TValue> and Dictionary<TKey, TValue>

Definition of partitioning: Partitioning consists of splitting up a collection {n1, n2, .. nk } into partitions of size P = C , where C is a positive constant integer. The last partition will consist of \[0, C\], the last C elements.

Example: A list of 100 elements will be partition by size 30, giving four partitions : 1: 0-29 2: 30-59 3: 60-89 4: 90-99

Note that partition 4 only got 9 elements.

Let's head over to some code.

The partition methods are the following :

```


using System;
using System.Collections.Concurrent;
using System.Collections.Generic;
using System.Linq;

public static class CollectionExtensions
{

    public static IEnumerable<IList<T&t;> Partition<T>(this IList<T> source, int size)
    {
        for (int i = 0; i < Math.Ceiling(source.Count / (double)size); i++)
        {
            yield return new List<T>(source.Skip(i * size).Take(size));
        }
    }

    public static IEnumerable<Dictionary<TKey, TValue&t;> Partition<TKey, TValue>(this IDictionary<TKey, TValue> source, int size)
    {
        for (int i = 0; i < Math.Ceiling(source.Keys.Count / (double)size); i++)
        {
            yield return new Dictionary<TKey, TValue>(source.Skip(i * size).Take(size));
        }
    }

    public static IEnumerable<ConcurrentDictionary<TKey, TValue> Partition<TKey, TValue>(this ConcurrentDictionary<TKey, TValue> source, int size)
    {
        for (int i = 0; i < Math.Ceiling(source.Keys.Count / (double)size); i++)
        {
            yield return new ConcurrentDictionary<TKey, TValue>(source.Skip(i * size).Take(size));
        }
    }

}

```

These three methods are very similar. An example usage is shown below. We partition a ConcurrentDictionary, for example one consisting of 200,000 key value pairs into partitions by size 50,000. This will produce a total of four partitions which are then processed at parallell.

Make note that even though you can partition a ConcurrentDictionary into multiple concurrent dictionaries consist after partitioning, the simpler approach code at the bottom of the method was quicker when I tested it out. There are a lot of pitfalls when it comes to concurrent programming.

The key takeaway from this article was how you can partition a collection into multiple partitions, this will enable you to do "Divide and Conquer" strategy when it comes to collections to partition labor among several threads in parallell.

```


	static int Enumerate(ConcurrentDictionary<int, int> dict)
	{
		//var stopWatch = Stopwatch.StartNew();

		var dicts = dict.Partition(dict.Count / 4).ToList();

		//Console.WriteLine(dicts.ElementAt(0).Count());
		//Console.WriteLine($"Partitioning took: {stopWatch.ElapsedMilliseconds} ms");

		int total = 0;

		Parallel.For(0, 4, (i) =>
		{
			int subTotal = 0;
			var curDict = dicts.ElementAt(i);
			//int count = curDict.Count;
			//Console.WriteLine($"Number in curDict : {count}");
			foreach (var item in curDict)
			{
				Interlocked.Add(ref subTotal, item.Value);
			}
			Interlocked.Add(ref total, subTotal);
		});

		return total;
        
        //Simpler approach :

		//int expectedTotal = dict.Count;

		//int total = 0;
		//Parallel.ForEach(dict, keyValPair =>
		//	 {
		//		 //int count = dict.Count;
		//		 Interlocked.Add(ref total, keyValPair.Value);
		//	 });
		//return total;
	}

```
