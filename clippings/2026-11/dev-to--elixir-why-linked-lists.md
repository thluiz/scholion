---
url: "https://dev.to/edisonywh/-elixir--why-linked-lists--1e9d"
captured_at: "2026-11-16T01:41:16+00:00"
title: "[ Elixir | Why Linked Lists? ]"
domain: "dev-to"
---

I've always thought data structures are cool, but you know what's cooler? Seeing them in the wild!

While going through Elixir's doc, I saw that Elixir uses linked lists under the hood for their linear data structure. I thought this was cool, but something struck me; I understood arrays and linked lists, but I had no idea how it relates to programming languages and it's bothered me ever since and I _need_ to find out _why_ linked list was used, hence this article!

So back to the article, from what I've found so far, there are three reasons as to why Elixir does this (and I could be totally wrong, feel free to correct me!). Let's go through one by one:

## [](#immutable-data)Immutable Data

In Elixir, (most functional languages actually), data are immutable. This is an important first step to understanding why linked lists is used, so let's explore this.

> Immutable means that once a data is declared, it _cannot_ be mutated/changed anymore.

Assuming you know how arrays work under the hood (check out [my other article](https://dev.to/edisonywh/how-arrays-work-the-way-arrays-work-3bpg) if you want a refresher). Let's take a look at what happens if we try to implement immutability with an array!

Array is defined as a continous block of memory. The problem with this is that, an array of 5 elements is still just ONE array, and when we are adding/deleting an element, we are MUTATING it. How can we use immutability with arrays then? It's not impossible, but let's look at why that's not practical.

If we want to enforce true immutability in arrays, this means that we need to make a full copy of the old array everytime we want to add/delete in the array.

Which means, if you have an array of size 5, if you want to add a new item to the array, your memory usage is instantly doubled (because you need to keep the old array as is, and you also need to make a new array of same elements). And that's just space complexity, there's also time complexity that we need to think about!

A linked list doesn't have the same constraint, as the nodes are all stored separately in memory, which means we don't really need to worry about space/time complexity while adding/delete nodes in list.

This gives us our first reason as to why it uses a list, however that's not the whole story - here's where recursive structural/tail sharing jumps in and everything starts making sense.

## [](#recursive-structure)Recursive structure

Did you notice that linked lists are recursive by definition?

For example, `A -> B -> C -> D` is a linked list, but so is `B -> C -> D`, `C -> D` and so on, and each linked list is just a _sub_ structure of another linked list!

Well that wasn't very exciting on its own, but this is vital to the next piece of puzzle!

> _Fun Fact: The recursive nature coupled with the fact that datas have to be immutable (so you can't have a loop counter) is why functional languages are usually associated with recursions - they kinda have to!_

## [](#structuraltail-sharing)Structural/Tail Sharing

So, we know linked lists are recursive in nature. Combined with the immutable nature of the language, we know that the data can never change.

This is interesting, because now we can confidently say that `A -> B -> C -> D` is a different list from `B -> C -> D` (even though one recursively contains the other one), and because we have that guarantee (along with the fact that a list CAN'T change), we don't have to define the same datas twice, and **we can reuse existing linked lists!** This is called **Structural sharing**.

Awesome isn't it? Let's look at an example.

e.g:  

```
list = [5,6,7,8]
list_one = [1 | list]
list_two = [2 | list]
```

Enter fullscreen mode Exit fullscreen mode

Now we have THREE different lists! `list`, `list_one` and `list_two`, but all of them share the same reference (the tail) and the only difference between them is the head pointer.

This means that there will be a total of 6 elements in memory. Adding to list has low memory cost, while retaining the immutability that we desire.

Reusable baby!

[![Baby smiling gif](https://i.giphy.com/media/fqygzR9D6j2uc/giphy.gif)](https://i.giphy.com/media/fqygzR9D6j2uc/giphy.gif)

If you want to read a little more, you can look into [Trie trees](https://en.wikipedia.org/wiki/Trie) which have the exact same concepts of sharing datas/prefixes!

### [](#garbage-collection-amp-caching)Garbage Collection & Caching?

These two I'm not quite sure, but I've heard that linked lists are good for GCs and that tail sharing makes a good candidate for locality of reference/caching (I don't get how, because they aren't stored in the same places). Would appreciate if someone wants to chime in!

## [](#closing-note)Closing Note

Sidenote, in actuality it's not as much about Elixir since it compiles down to Erlang, but also not much about Erlang because all functional programming does pretty much same thing, but this is what prompted my curiousity hence the ties to Elixir.

While writing this article, I found that I had to write in depth on how arrays work before I was able to dive into the Elixir part, so I've published that as [another article over here](https://dev.to/edisonywh/how-arrays-work-the-way-arrays-work-3bpg) instead; do read that to gain a better understanding on what the tradeoff is!

I also did not really talk about Big O notations because I felt they might add unnecessary reading _time_ and _complexity_ to the article, but they're pretty vital and fundamental to computer science, so I suggest you brush up a little on them.

If you're a podcast kind-of person, there's the [BaseCS](https://www.codenewbie.org/basecs) by CodeNewbie, co-hosted by Vaidehi Joshi and Saron.

If you want to read though, Vaidehi Joshi's blogpost version (which is what inspired the podcast I believe) is great too on [BaseCS Medium](https://medium.com/basecs).

As for video, [MyCodeSchool](https://www.youtube.com/playlist?list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P) is beyond amazing and is pratically where I learned everything that I know now, highly recommended!

Other than that, hope you guys enjoyed the article as much as I enjoyed writing it!

## [](#sources)Sources

[https://elixir-lang.org/getting-started/basic-types.html#linked-lists](https://elixir-lang.org/getting-started/basic-types.html#linked-lists) - The piece that prompted this article
