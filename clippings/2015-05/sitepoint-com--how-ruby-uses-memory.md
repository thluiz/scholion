---
url: "http://www.sitepoint.com/ruby-uses-memory/"
captured_at: "2015-05-11T16:02:40-03:00"
title: "How Ruby Uses Memory"
domain: "sitepoint-com"
---

# How Ruby Uses Memory

Published May 11, 2015

![1430951585Fotolia_439366_Subscription_Monthly_M-300x225.jpg](sitepoint-com--how-ruby-uses-memory/f84c2418825626e254fc0ea82388cf3d.jpg)

I’ve never met a developer who complained about code getting faster or taking up less RAM. In Ruby, memory is especially important, yet few developers know the ins-and-outs of why their memory use goes up or down as their code executes. This article will start you off with a basic understanding of how Ruby objects relate to memory use, and we’ll cover a few common tricks to speed up your code while using less memory.

## Object Retention

The most obvious way that Ruby grows in memory usage is by retaining objects. Constants in Ruby are never garbage collected so if a constant has a reference to an object, then that object can never be garbage collected.

|  |  |
| --- | --- |
|  | `RETAINED` `= []`  `100_000``.times` `do`  `RETAINED` `<<` `"a string"`  `end` |

If we run this and debug with `GC.stat(:total_freed_objects)` it will return the number of objects that have been released by Ruby. Running this snippet before and after results in very little change:

|  |  |
| --- | --- |
|  | `# Ruby 2.2.2`  `GC``.start`  `before =` `GC``.stat(``:total_freed_objects``)`  `RETAINED` `= []`  `100_000``.times` `do`  `RETAINED` `<<` `"a string"`  `end`  `GC``.start`  `after =` `GC``.stat(``:total_freed_objects``)`  `puts` `"Objects Freed: #{after - before}"`  `# => "Objects Freed: 6` |

We have created 100,000 copies of `"a string"` but since we **might** use those values in the future, they can’t be garbage collected. Objects cannot be garbage collected when they are referenced by a global object. This goes for constants, global variables, modules, and classes. It’s important to be careful referencing objects from anything that is globally accessible.

If we do the same thing without retaining any objects:

|  |  |
| --- | --- |
|  | `100_000``.times` `do`  `foo =` `"a string"`  `end` |

The objects freed skyrockets: `Objects Freed: 100005`. You can also verify that the memory is much smaller, around 6mb compared to the 12mb when retaining a reference to the objects. Measure it yourself with the [get\_process\_mem gem](https://github.com/schneems/get_process_mem), if you like.

Object retention can be further verified using `GC.stat(:total_allocated_objects)`, where retention is equal to `total_allocated_objects - total_freed_objects`.

## Retention for Speed

Everyone in Ruby is familiar with DRY or “Don’t repeat yourself”. This is as true for object allocations as is is for code. Sometimes, it makes sense to retain objects to reuse rather than have to recreate them again and again. Ruby has this feature built-in for strings. If you call `freeze` on a string, the interpreter will know that you do not plan on modifying that string it can stick around and be reused. Here’s an example:

|  |  |
| --- | --- |
|  | `RETAINED` `= []`  `100_000``.times` `do`  `RETAINED` `<<` `"a string"``.freeze`  `end` |

Running this code, you’ll still get `Objects Freed: 6`, but the memory use is extremely low. Verify it with `GC.stat(:total_allocated_objects)`, only a few objects were allocated as `"a string"` is being retained and reused.

Instead of having to store 100,000 different objects, Ruby can store one string object with 100,000 references to that object. In addition to decreased memory, there’s also a decreased run time as Ruby has to spend less time on object creation and memory allocation. Double check this with [benchmark-ips](https://github.com/evanphx/benchmark-ips), if you want.

While this facility for de-duplicating commonly used strings is built into Ruby, you could do the same thing with any other object you want by assigning it to a constant. This is already a common pattern when storing external connections, like to Redis, for example:

|  |  |
| --- | --- |
|  | `RETAINED_REDIS_CONNECTION` `= Redis.``new` |

Since a constant has a reference to the Redis connection, it will never be garbage collected. It’s interesting that sometimes by being careful about retained objects, we can actually lower memory use.

## Short Lived Objects

Most objects are short lived, meaning shortly after their creation they have no references. For example, take a look at this code:

|  |  |
| --- | --- |
|  | `User.where(name:` `"schneems"``).first` |

On the surface, this looks like it requires a few objects to function (the hash, the `:name` symbol, and the `"schneems"` string. However, when you call it, many many more intermediate objects are created to generate the correct SQL statement, use a prepared statement if available, and more. Many of these objects only last as long as the methods where they were created are being executed. Why should we care about creating objects if they’re not going to be retained?

Generating a moderate number of medium and long lived objects will cause your memory to go up over time. They can cause the Ruby GC to need more memory if the GC fires at a moment those objects are still referenced.

## Ruby Memory Goes Up

When you have more objects being used than Ruby can fit into memory, it must allocate additional memory. Requesting memory from the operating system is an expensive operation, so Ruby tries to do it infrequently. Instead of asking for another few KB at a time, it allocates a larger chunk than it needs. You can set this amount manually by setting the `RUBY_GC_HEAP_GROWTH_FACTOR` environment variable.

For example, if Ruby was consuming 100 mb and you set `RUBY_GC_HEAP_GROWTH_FACTOR=1.1` then, when Ruby allocates memory again, it will get 110 mb. As a Ruby app boots, it will keep increasing by the same percentage until it reaches a plateau where the entire program can execute within the amount of memory allocated. A lower value for this environment variable means we must run GC and allocate memory more often, but we will approach our maximum memory use more slowly. A larger value means less GC, however we may allocate much more memory than we need.

For the sake of optimizing a website, many developers prefer to think that “Ruby never Releases memory”. This is not quite true, as Ruby does free memory. We will talk about this later.

If you take these behaviors into account, it might make more sense how non-retained objects can have an impact on overall memory use. For example:

|  |  |
| --- | --- |
|  | `def` `make_an_array`  `array = []`  `10_000_000``.times` `do`  `array <<` `"a string"`  `end`  `return` `nil`  `end` |

When we call this method, 10,000,000 strings are created. When the method exits, those strings are not referenced by anything and will be garbage collected. However, while the program is running, Ruby must allocate additional memory to make room for 10,000,000 strings. This requires over 500mb of memory!

![Screenshot 2015-04-13 21.32.23.png](sitepoint-com--how-ruby-uses-memory/9457b3f090a962db2720944c4d690a9a.png)

It doesn’t matter if the rest of your app fits into 10mb, the process is going to need 500mb of RAM allocated to build that array. While this is a trivial example, imagine that the process ran out of memory in the middle of a really large Rails page request. Now GC must fire and allocate more memory if it cannot collect enough slots.

Ruby holds onto this allocated memory for some time, since allocating memory is expensive. If the process used that maximum amount of memory once, it can happen again. The Memory will be freed gradually, but slowly. If you’re concerned about performance, it is better to minimize object creation hotspots whenever possible.

## In-Place Modification for Speed

One trick I’ve used to speed up programs and cut down on object allocations is by modifying state instead of creating new objects. For example, here is some code taken from the [mime-types](https://github.com/halostatue/mime-types) gem:

|  |  |
| --- | --- |
|  | `matchdata.captures.map { |e|`  `e.downcase.gsub(%r{[Xx]-}o,` `''``)`  `end` |

This code takes a [matchdata object](http://ruby-doc.org/core-2.2.1/MatchData.html) returned from the regex `match` method. It then generates an array of each element captured by the regex and passes it to the block. The block makes the string lowercase and removes some stuff. This looks like perfectly reasonable code. However, it happened to be called thousands of times when the `mime-types` gem was required. Each method call to `downcase` and `gsub` create a new string object, which takes time and memory. To avoid this, we can do in-place modification:

|  |  |
| --- | --- |
|  | `matchdata.captures.map { |e|`  `e.downcase!`  `e.gsub!(%r{[Xx]-}o,` `''``.freeze)`  `e`  `}` |

The result is certainly more verbose, but it is also much faster. This trick works because we never reference the original string passed into the block, so it doesn’t matter if we modify the existing string rather than making a new one.

Note: you don’t need to use a constant to store the regular expression, as all regular expression literals are “frozen” by the Ruby interpreter.

In-place modification is one place where you can really get into trouble. It’s really easy to modify a variable you didn’t realize was being used somewhere else, leading to subtle and difficult to find regressions. Before doing this type of optimization, make sure that you have good tests. Also, only optimize the “hotspots”, which is the code you’ve measured and determined creates an excessively large number of objects.

It would be a mistake to think that “objects are slow”. Correctly using objects can make a program easier to understand and easier to optimize. Even the fastest tools and techniques, when used inefficiently, will cause a slow down.

A good way to catch unnecessary allocations is with the [derailed\_benchmarks gem](https://github.com/schneems/derailed_benchmarks) on the application level. On a lower level, use the [allocation\_tracer gem](https://github.com/ko1/allocation_tracer) or the [memory\_profiler gem](https://github.com/SamSaffron/memory_profiler).

Note: I wrote the derailed\_benchmarks gem. Look at `rake perf:mem` for memory statistics.

## Good to be Free

As mentioned earlier, Ruby does free memory, though slowly. After running the `make_an_array` method that causes our memory to balloon, you can observe Ruby releasing memory by running:

|  |  |
| --- | --- |
|  | `while` `true`  `GC``.start`  `end` |

Very slowly, the memory of the application will decrease. Ruby releases a small amount of empty pages (a set of slots) at a time when there is too much memory allocated. The operating system call to `malloc`, which is currently used to allocate memory, may also release freed memory back to the operating system depending on the OS specific implementation of the malloc library.

For most applications, such as web apps, the action that caused the memory allocation can be triggered by hitting an endpoint. When the endpoint is hit frequently, we cannot rely on Ruby’s ability to free memory to keep our application footprint small. Also, freeing memory takes time. It’s better to minimize object creation in hotspots when we can.

## You’re Up

Now that you’ve got a good solid basis for understanding how Ruby uses memory, you’re ready to go out there and start measuring. Pick some of the tools I mentioned:

Then, go benchmark some code. If you can’t find any to benchmark, try to reproduce my results here. Once you’ve got a handle on that, try digging into your own code to find object creation hotspots. Maybe it will end up being in something you wrote or maybe it will be in a third party gem. Once you’ve found a hotspot, try to optimize it. Keep repeating this pattern: find hotspots, optimize them, and benchmark. It’s time to tame your Ruby.

---

If you enjoy tweets about Ruby memory statistics follow [@schneems](https://twitter.com/schneems).
