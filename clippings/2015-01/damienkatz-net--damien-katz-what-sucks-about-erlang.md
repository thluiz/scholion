---
url: "http://damienkatz.net/2008/03/what_sucks_abou.html"
captured_at: "2015-01-24T06:58:54-03:00"
title: "Damien Katz: What Sucks About Erlang"
domain: "damienkatz-net"
---

### What Sucks About Erlang

There are the languages everyone complains about, and there are the languages no one uses.

Having said that, it's time to whine about my favorite language I use quite extensively. Erlang, I love ya, but we need to have a word.

**Basic Syntax**

Erlang is based originally on Prolog, a logic programming language that was briefly hot in the 80's. Surely you've seen other languages based on Prolog, right? No? Why not? Because Prolog sucks ass for building entire applications. But that hasn't deterred Erlang from stealing it's dynamite syntax.

The problem is, unlike the C and Algol based languages, Erlang's syntax does away with nested statement terminators and instead uses expression separators everywhere. Lisp suffers the same problem, but Erlang doesn't have the interesting properties of a completely uniform syntax and powerful macro system to redeem itself. Sometimes a flaw is really a strength. And sometimes it's just a flaw.

Because Erlang's expression terminators vary by context, editing code is much harder than conventional languages. Refactoring -- cutting and pasting and moving code around -- is particularly hard to do without creating a bunch of syntax errors.

Consider this code:

```
blah(true) ->
  foo(),
  bar();
blah(false) ->
  baz().
```

Lets say I want to reorder the branches:

```
blah(false) ->
  baz();
blah(true) ->
  foo(),
  bar().
```

Or change the order which `foo()` and `bar()` are called.

```
blah(true) ->
  bar(),
  foo();
blah(false) ->
  baz().
```

What's the problem? Note in each example the bar() lines, they have a different character ending each line: `bar();` `bar(),` `bar().`

In Algol based languages the statement terminators are the same everywhere (usually semi-colon, newline or both). The Javascript version:

```
function blah(flag) {
  if (flag) {
    bar();
    foo();
  } else {
    baz();
  }
}
```

Erlang expression separators vary context to context and it's simply more mental work to get right.

**If Expressions**

You might think `if` branching as something that no language could ever get wrong. Doesn't seem possible does it? I was young once too.

The first problem is that every time an `if` executes it should match at least one of the conditional expression branches. When it does not, an exception is thrown.

In this example:

```
if
X == foo ->
   foo();
X == bar ->
   bar()
end
```

X must be `foo` or `bar`, or an `if_clause` exception is thrown.

This sorta makes some sense since the `if`'s aren't statements like in C language family, they are more like the C ternary operator `(x == foo ? foo() : bar())` and so *must* return a value to the caller.

The problem is it prevents simple code like this:

```
if
Logging ->
  log("Something happened")
end
```

Because if Logging is false, the `if` throws an `if_clause` exception!

Instead you are forced to do something like this:

```
if
Logging ->
  log("Something happened");
true -> ok
end
```

The only purpose of the `true -> ok` line is to give it an else condition to match. That weird taste in the back of your throat? It's probably vomit.

Erlang `if`s could be so much more useful if it would just return a sensible default when no conditionals match, like an empty list `[]` or the `undefined` atom. But instead it blows up with an exception. If Erlang were a side-effect free functional language, such a restriction would make sense. But it's not side effect free, so instead it's idiotic and painful.

It gets worse. You cannot even *call user defined functions* in `if` conditional expressions! For example, this won't even compile because of the call to user defined `should_foo(X)`:

```
should_foo(X) ->
  X == foo.
 
bar() ->
  if
  should_foo(X) ->  % compile error on this line!
    foo();
  true -> ok
  end.
```

This limitation is due to Erlang's "when clause" pattern matching engine, which needs certain guarantees from the expressions for static optimization. Erlang allows a subset of the built-in functions (BIFs) in conditional expressions, but no user defined functions can be called whatsoever.

How can a language have butchered the `if` and still be useful? Well, fortunately `case` expressions in Erlang are powerful and damn useful, and a decent substitute for most uses of `if`:

```
case should_foo(X) of
true -> foo();
false -> ok
end
```

But like `if` expressions, `case` expression also have the limitation that it must match at least one conditional or an exception is thrown. Bleh.

**You Say String of Characters, I Say List of Integers**

The most obvious problem Erlang has for applications is sucky string handling. In Erlang, there is no string type, strings are just a list of integers, each integer being an encoded character value in the string.

It's not all bad. It has the benefit of taking the same built-in list operations, libraries and optimizations and reusing them for string processing. But it also means you can't distinguish easily at runtime between a string and a list, and especially between a string and a list of integers.

From the Erlang Console you get this:

```
1> [100,111,103] == "dog".
true
```

Erlang string operations are just not as simple or easy as most languages with integrated string types. I personally wouldn't pick Erlang for most front-end web application work. I'd probably choose PHP or Python, or some other scripting language with integrated string handling.

**Functional Programming Mismatch**

Erlang has been a great fit for CouchDB, a network database server. Once I got over Erlang's weirdness and accepted its warts, I almost couldn't imagine using anything else. So much of the code seems to *want* to be expressed in a recursive, functional manner and the lightweight, shared nothing concurrency is a great match for network servers and database internals. The code is typically much more compact, elegant and reliable than it would be in more conventional languages.

But when it came time to write the test suite code for CouchDB, I found Erlang to be needlessly cumbersome, verbose and inflexible.

Immutable variables in Erlang are hard to deal with when you have code that tends to change a lot, like user application code, where you are often performing a bunch of arbitrary steps that need to be changed as needs evolve.

In C, lets say you have some code:

```
int f(int x) {
  x = foo(x);
  x = bar(x);
  return baz(x);
}
```

And you want to add a new step in the function:

```
int f(int x) {
  x = foo(x);
  x = fab(x);
  x = bar(x);
  return baz(x);
}
```

Only one line needs editing,

Consider the Erlang equivalent:

```
f(X) ->
  X1 = foo(X),
  X2 = bar(X1),
  baz(X2).
```

Now you want to add a new step, which requires editing every variable thereafter:

```
f(X) ->
  X1 = foo(X),
  X2 = fab(X1),
  X3 = bar(X2),
  baz(X3).
```

Erlang's context dependent expression separators and immutable variables end up being huge liabilities for certain types of code, and the result is far more line edits for otherwise simple code changes. For the CouchDB test suite I could feel the syntax fighting me at every turn. When I switched over to writing the tests in Javascript, things just flowed faster and edits were easier.

Erlang wasn't a good match for tests and for the same reasons I don't think it's a good match for front-end web applications.

**Records**

The "records" feature provides a C-ish structure facility, but it's surprisingly limited and verbose, requiring you to state the type of the record for each reference in the code.

Not once for each variable binding, but you must state the variable's type each and every place a member of the variable record is referenced.

```
-record(foo, {
    a=0,
    b=0,
    c=0}).
 
bar(F) ->
  baz1(F#foo.a),
  baz2(F#foo.b),
  F#foo{c=F#foo.c + 1}.
```

Each of those `F#foo` is a statement that says "I'm a record variable of type `foo`". And it's not enough to say it once. We must say it over and over again each time we use it.

Here is a more idiomatic use of records, which uses pattern matching to extract members into local variables:

```
bar(#foo{a=A,b=B,c=C}=F) ->
  baz1(A),
  baz2(B),
  F#foo{c=C + 1}.
```

Which is still noisy compared to the equivalent in C:

```
struct foo {
  int a;
  int b;
  int c;
}
 
foo bar(foo f) {
  baz1(f.a);
  baz2(f.b);
  f.c += 1;
  return f;
}
```

Another problem is records often feel like a tacked-on hack. They are compile-time static and record members cannot be added or removed at runtime, and don't fit with Erlang's otherwise dynamic nature.

Records are a compile time feature -- not a VM feature -- and are statically compiled down to regular tuples, with the first slot holding the record name atom, and each slot N + 1 corresponding to the Nth entry in record declaration. At compile time the record member references are converted to integer offsets for tuple operations.

The most noticeable problem is they aren't usable from the REPL command line, it won't accept record syntax without special steps and it still doesn't show you result records in record syntax. Same when debugging and dumping stack traces and symbols, the records always look like the tuples they are under the covers, requiring you to mentally decode which tuple slot corresponds to a record member. Erlang records give you most of the penalties of static typing with very little of the benefit.

**Give me memory, or give me death!**

***Update: On OS X with the most recent Erlang VM (R12B-1, emulator version 5.6.1), I can no longer reproduce this problem. Yay!***

With CouchDB we discovered the hard way how Erlang handles memory allocation errors from the OS:

`exit(1);`

When the VM cannot get memory from the OS, it just commits hara-kiri. It doesn't just kill the virtual Erlang "process" that needs the memory. It kills the whole VM, taking along any child OS processes with it. But at least it's an honorable death.

See for yourself, try this at the Erlang console:

```
Eshell V5.5.3  (abort with ^G)
1> <<0:429967295>>.    
beam(722,0xa000d000) malloc: *** vm_allocate(size=1782579200) failed (error code=3)
[....snip stack trace....]
Crash dump was written to: erl_crash.dump
eheap_alloc: Cannot allocate 1781763260 bytes of memory (of type "heap").
Abort trap
```

So no problem you might think, given Erlang's robust, fail-fast and restart nature, it will restart itself automatically and barely miss a beat. Well, that's what I thought, but then I'm generally a positive guy.

Nope, Erlang won't restart itself automatically, that's something you have to build all by yourself. The only solution we've found is to create a parent watchdog process to monitor the VM and restart it if it crashes.

The built-in "heart" child OS process, whose job it is to monitor for an unresponsive Erlang VM and restart it, is also killed when the VM exits. So we have to roll our own "restart the dead VM" solution and deal with cross-platform issues providing something I'm still shocked Erlang can't handle itself.

**Code Organization**

The only code organization offered is the source file module, there are no classes or namespaces. I'm no OO fanatic (not anymore), but I do see the real value it has: code organization.

Every time time you need to create something resembling a class (like an OTP generic process), you have to create whole Erlang file module, which means a whole new source file with a copyright banner plus the Erlang cruft at the top of each source file, and then it must be added to build system and source control. The extra file creation artificially spreads out the code over the file system, making things harder to follow.

What I wish for is a simple class facility. I don't need inheritance or virtual methods or static checking or monkey patching. I'd just like some encapsulation, the ability to say here is a hunk of data and you can use these methods to taste the tootsie center. That would satisfy about 90% of my unmet project organization needs.

**Uneven Libraries and Documentation**

Most of core Erlang is well documented and designed, but too many of the included modules are buggy, overly complex, poorly documented or all three.

The Inets httpd server we've found incredibly frustrating to use in CouchDB and are discarding it for a 3rd party Erlang HTTP library. The XML processor (Xmerl) is slow, complicated and under documented. Anything in Erlang using a GUI, like the debugger or process monitor, is hideous on Windows and pretty much unusable on OS X. The OTP build and versioning system is complicated and verbose and I still don't understand why it is like it is.

And crufty. I know Erlang has been evolving for real world use for a long time, but that doesn't make the cruftyness it's accumulated over the years smell any better. The coding standards in the core Erlang libraries can differ widely, with different naming, argument ordering and return value conventions. It's tolerable, but it's still there and you must still deal with it.

**Erlang Really Sucks?**

Yes, in all the ways I just described and more that I didn't.

But also no. Erlang is amazing in ways it would [take a whole book to describe properly](http://www.pragprog.com/titles/jaerlang). It's not a toy built to satisfy the urges of academics, it's used in successful, real world products. But there is a good chance that Erlang just is not a good match for your uses. This list isn't meant to put down Erlang, but as an honest assessment of it's weaknesses, which I think aren't discussed enough.

Posted March 9, 2008 3:46 PM
