---
url: "https://leveluppp.ghost.io/loop-optimizations-in-various-compilers/"
captured_at: "2021-02-12T06:38:04-03:00"
title: "Loop Optimizations in C#"
domain: "leveluppp-ghost-io"
---

# Loop Optimizations in C# (and various other compilers)

This post comprises infographics showing various loop optimizations that happen in C# (dotnet) and other languages.

#### [LevelUp++](https://leveluppp.ghost.io/author/bartosz/)

9 Feb 2021
• 4 min read

![photo-1500322095253-b2c00f31fa54](leveluppp-ghost-io--loop-optimizations-in-csharp/05bb6356317e9acb9b9e7fbe37e316a9.jpg)

This post comprises infographics showing various loop optimizations that happen in C# (dotnet).

I've also tested simple loops in GO and Rust, but they need more tests, and separate posts will be made for these compilers; Go and Rust's tests will be in the bonus section of this article.

**Warning**: Compilers improve with time. Therefore, most graphics will contain the compiler version.

Let's start with C# and two of its primary optimizations:

- Loop Cloning
- Loop Hoisting

### Loop Cloning:

Loop cloning is a very clever technique that will try to avoid array bounds checking when we loop on some unspecified range:

![obraz-4.png](leveluppp-ghost-io--loop-optimizations-in-csharp/7a509ee0f4fca694a1a37d814437a593.png)

To solve this problem, the compiler will clone the loop, and slow and a fast path will get generated:

![obraz-19.png](leveluppp-ghost-io--loop-optimizations-in-csharp/038427c384591257e32aa9a36d4b88ba.png)

This allows us to get rid of all of the bounds checking in the fast path.

### Loop Hoisting:

Hoising will move expressions that can be computed once out of the loop into a temporary variable (register) and resue it.

So a loop:

![obraz-6.png](leveluppp-ghost-io--loop-optimizations-in-csharp/f5b1dcb14fb4a351771632a72dbc84e1.png)

Will get converted to:

![obraz-7.png](leveluppp-ghost-io--loop-optimizations-in-csharp/a7defd60a2a672af57d2343f95666a91.png)

### C# Compound vs Non-Compund Assigment:

![obraz.png](leveluppp-ghost-io--loop-optimizations-in-csharp/1b321ad111440cbbea90b89a482da2d3.png)

It turns out that compound assignment works differently than the non-compund one, and instead of using temp locals, it will instead emit a "dup" instruction in IL, which will duplicate the lvalue on the stack and prduce a pointer to this value.

![obraz-8.png](leveluppp-ghost-io--loop-optimizations-in-csharp/17f13b2e1d86f80ad5f57504a518508f.png)

This confuses the JIT compiler, and no optimizations (loop cloning, computation hoisting) are happening in such a loop.

If we look at the non-compound version in IL, we shall see this:

![obraz-9.png](leveluppp-ghost-io--loop-optimizations-in-csharp/002bd206c89c0c433a4d0e2f1cdafb0c.png)

### C# Try-Catch Blocks:

![obraz-1.png](leveluppp-ghost-io--loop-optimizations-in-csharp/930032ae17a0b8722f712e1fcc209fa6.png)

Loop optimizations such as cloning and hoisting will not happen in try-catch blocks.

Even if we have something that can be discarded in a try-catch block and meaningful computation after it, the loop will not be cloned.

![obraz-2.png](leveluppp-ghost-io--loop-optimizations-in-csharp/855f503e6b8665f1b7f11648672a1eda.png)

In this case, the empty try-catch will get removed, while the discard assignment will remain, and it will block loop cloning.

### C# Loop Optimizations are sensetive:

![obraz-3.png](leveluppp-ghost-io--loop-optimizations-in-csharp/3a473d0699cba458fe5adce95463706c.png)

If our range is slightly more complicated (like a computation) in the loop condition,  loop cloning will not happen, and the compiler will emit bounds check on every iteration.

### C# Loop Optimizations are tricky on Span<T>:

![obraz-10.png](leveluppp-ghost-io--loop-optimizations-in-csharp/bbadf279a66fcbe37efbe03cb25c49aa.png)

As you can see the compiler managed to figure out that the program will not crash in the fast case and removed all of the bounds checks. It's a good practice to create a slice and work on that slice since this will allow the compiler to make correct decisions.

### C# Prolog and Epilog:

![obraz-11.png](leveluppp-ghost-io--loop-optimizations-in-csharp/a23057ea0c773d174c69d505f038fcea.png)

**Prolog** means creating a stack frame for the function and putting all of the necessary function arguments on the stack with a proper state.

On the other hand, **Epilog** means cleaning up the stack from all of the locals that were produces and destroying the function frame.

While it's difficult to translate what a prolog and Epilog mean in user code (since a return statement is not necessary, an epilog), if we have too many returns from a function in a loop, optimizations will be off.

### C# Loop Cloning Tips:

As you can tell by now, loop cloning in C# can be very stingy and picky, so you have to hit the pattern exactly for it to work. So here's an infographic showing most of the things that you have to get right:

![obraz-14.png](leveluppp-ghost-io--loop-optimizations-in-csharp/1db8e0f678b4e878dd5a0947049dc816.png)

### [Bonus] GO Loop Optimizations:

![obraz-15.png](leveluppp-ghost-io--loop-optimizations-in-csharp/3d3517d4fe3a40249bc7868d3181fe4e.png)

In my simple tests, I hardly saw any advanced optimizations applied in the GO compiler. I'm told that this is a part of the philosophy of everything being simple in GO, both at the language level and the compiler level.

### [Bonus] Rust Loop Optimizations:

![obraz-16.png](leveluppp-ghost-io--loop-optimizations-in-csharp/01dd3b0be71f9126e80178cb8da3c666.png)

Rust produces tons of optimizations, and they are dependent on the range construction (and count). It will still emit bounds checks, but it will do loop unrolling, hoisting, and many more interesting tricks.

### [BONUS] Other Related (and Unrelated) Graphics:

![obraz-17.png](leveluppp-ghost-io--loop-optimizations-in-csharp/65079b6b1f0c06fd37ddef0bee7bdfec.png)

![obraz-18.png](leveluppp-ghost-io--loop-optimizations-in-csharp/e41ca12b35f56e715650d6d8463d8397.png)

### The End

This content took a while to create, so if you like it, please consider buying me a coffee

### Subscribe to LevelUp++

Get the latest posts delivered right to your inbox
