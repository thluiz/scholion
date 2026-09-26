---
url: "https://spakhm.com/claude-code?utm_source=tldrai"
captured_at: "2026-01-08T17:09:34+00:00"
title: "Thoughts on Claude Code - Slava Akhmechet"
domain: "spakhm-com"
---

*   [home](https://spakhm.com/)
*   subscribe → [rss](https://spakhm.com/feed.rss) | [email](https://spakhm.com/subscribe.html)

Many programmers complain AI is good for quickly throwing up some CRUD apps but not much else. When someone points out this isn’t true, everyone (rightly) asks for examples. There aren’t many posts with detailed examples online, so I thought I’ll offer some from a project I wrote this Christmas.

Over the winter break I started building [Beep](https://github.com/coffeemug/beep-lang)– an imaginary programming language I wanted to get out of my head and into working code (if only to exorcise it so I stop thinking about it). I had two weeks and wanted to get as much as possible done, so I wrote everything in cooperation with Claude Code/Opus 4.5.

(The word “cooperation” isn’t incidental. I picked it carefully because it accurately describes the experience of working with Claude as if you had a programming partner.)

## Example I: lexical scope shadowing

Beep supports lexical scoping. You can say this and it will work:

```
let x = 1

def foo()
  x  # `foo` can see `x`
end

foo()
```

A very simple way to implement this is to put `x: 1` in a map of bindings and reference this map from `foo` at function definition time. When `foo` is called it can look up the value of `x` in this map.

Beep also supports shadowing. You can do the following and it will work too:

```
let x = 1, y = 1

def foo()
  [x, y]
end

let x = 2

def bar()
  [x, y]
end

foo() # returns [1, 1]
bar() # returns [2, 1]
```

A simple way to implement this is to have a singly-linked list of binding maps. Every time you see a `let` you make a new bindings map and link it to the previous one. In the example above the interpreter goes through the following steps:

1.  See `let x = 1, y = 1`, make a bindings map and put `x: 1, y: 1` in it.
2.  See `def foo`, reference map in step `1` from `foo` definition.
3.  See `let x = 2`, make a new bindings map, put `x: 2` in it. Link this map to the map we made in step `1`.
4.  See `def bar`, reference map in step `3` from `bar` definition.
5.  User calls `foo()`. The interpreter follows the reference to the first map, looks up `x` and `y`, and returns the values `[1, 1]`.
6.  User calls `bar()`. The interpreter follows the reference to the second map, looks up `x` and `y`. Finds `x: 1`, but can’t see `y`, so it follows the chain to the first map. Finds `y: 1` and returns the values `[2, 1]`.

One problem with this approach is that it’s not obvious how to keep track of the most recent map. Consider this example:

```
let x = 1

def foo()
  x            # x is 1 here
  let x = 2
  x            # x is 2 here
  let x = 3
  x            # x is 3 here
end

foo()

x              # x is 1 again
```

There are three `let` statements. Every time we see one, we create a new map that points to the previous one and make it the new “current”. When we see `end` we have to go back to the first map and make it current again. But how do we keep track of how many maps to go back?

I considered two approaches:

1.  Keep a stack of integers in the interpreter state. Every time the interpreter enters a block (like a function definition), we push zero on this stack. Whenever there is a let, we increment the counter on top of the stack. At block exit, we drop as many maps as we’ve counted and pop the top count off the stack. This approach is simple, introduces a runtime cost (which doesn’t matter in a toy interpreter), and makes the interpreter more complicated.
    
2.  Do a separate pass to transform the AST to introduce this information statically. This pass would transform the example above into this:
    
    ```
    let x = 1 in
      def foo()
        x              # x is 1 here
        let x = 2 in
          x            # x is 2 here
          let x = 3 in
            x          # x is 3 here
          end
        end
      end
    
      x                # x is 1 again
    end
    ```
    
    Old school languages would do this explicitly in the grammar, but I didn’t want to offload this on the user in Beep. Implementing the pass is essentially taking the first approach but running it once at parse time.
    

I asked Claude Code for advice, and it suggested two more approaches:

1.  The same thing as above, but rather than a separate pass, do the transformation straight in the parser. Claude immediately gave me a correct diff to make this change. While I ended up not choosing this approach, it’s simple, and something I wouldn’t have thought of myself.
2.  Stop keeping track of the latest bindings frame in explicit interpreter state. Instead have `eval` return the value _and_ the new frame. Most AST nodes would return the same frame as they got, but `let` node would return a new one. This would make the host programming language stack automagically take care of the problem.

This latter option is the one I chose. I’m pretty sure I would have seen it myself without Claude, but this required a large mechanical refactor, and I guess my brain subconsciously recoiled from it. Of course I wouldn’t have to do the refactor myself. I asked Claude Code and it did the refactor perfectly (see commit [4a022a04](https://github.com/coffeemug/beep-lang/commit/4a022a04ef308c7d71331c47f9fc2eb14332a3f9)). I can just _do_ big mechanical refactors now without worrying about it, but it takes time to retrain your subconscious to get used to the capabilities of new tools.

## Example II: dynamic scope mutation

Another feature of Beep is dynamic scoping. Dynamically scoped variables are prefixed by the `$` sigil. Consider this example:

```
def foo()
  $x
end

def bar()
  let $x = 1
  foo()       # returns 1
end

bar()         # returns 1
foo()         # error, $x is not defined
```

Dynamically scoped variables are extremely useful to introduce state at the bottom of the stack and have everyone on the stack see it. For example, a web server can put configuration in a dynamic variable, and have every request handler see it without having to explicitly pass the state. This is useful anywhere you’d consider using global variables, but much safer. It doesn’t pollute the global namespace, it’s scoped to your calls, and is much easier to make thread safe. Dynamically scoped variables are a much better version of global variables (or what people sometimes used to use singletons for).

I implemented dynamically scoped variables using a second linked list of binding frames, and then bumped into a question. Should these variables be mutable? My intuition was that you shouldn’t be able to assign to `$x` in `foo` because that would introduce spooky action at a distance– anyone deep on the call stack would be able to change your variable without your knowledge. But I also thought you should be able to assign to it in `bar`. In other words: you can only assign to dynamic variables you introduced yourself.

But how would the interpreter know to do this? Somehow it would have to keep track of where dynamically scoped variables were introduced. This seemed kind of complicated and I felt lazy to reason it out, so I asked Claude Code. Claude suggested a very simple and elegant plan– add a set to each lexical binding frame; every time you see a dynamically scoped variable declaration, put it in the set. Everything else is already taken care of by existing machinery. I asked Claude to implement this, and again it made a perfect working diff (I broke it into commits [6694c8ad](https://github.com/coffeemug/beep-lang/commit/6694c8ada66e0e956020819acccd2cfe658080ef) and [a09c3af8](https://github.com/coffeemug/beep-lang/commit/a09c3af8b685dc5c1e830c9598e2ec227621285f)).

This is almost certainly something I would have eventually seen myself, but it would have taken me some time to reason it out. When you’re first learning about a new field, working through solutions yourself helps you get better. But when you’re already pretty familiar with the problem space, you can often recognize a great solution when you see one, and it can let you pierce the heart of the problem much more efficiently than if you did it yourself. For me this was obviously the case here.

## Example III: parser combinator hackery

About a year ago I wrote [ts-parsec](https://www.spakhm.com/ts-parsec)– a type-safe parser combinator library in typescript. I know the library inside out so it’s easy to write throwaway parsers, and type safety provides for great ergonomics. At least that was the idea. In practice, when grammars get slightly complicated I can find myself spending hours wrangling the type system to get it to type check.

`ts-parsec` is not a popular library– it has 13 github stars and 395 weekly npm downloads. And yet, Claude is _much_ better at using it than I am. I suppose there are enough parser combinator libraries in its training set, but `ts-parsec` is idiosyncratic enough and different enough from similar libraries that using it requires non-trivial understanding of the details.

Beep’s [parser.ts](https://github.com/coffeemug/beep-lang/blob/f149bfcc120a882020d42479bc7bc29fc68f147f/src/runtime/parser.ts) file is the part of the codebase I don’t care about. If Beep ever escapes the toy stage, I’ll throw away `parser.ts` and either rewrite it using a mature parser generator, or write the parser by hand. So for parsing I would just give Claude pretty high level instructions. For example:

> I want to introduce let expressions of the form `let x = 1, $y = 2`. Add these to the parser and the AST, don’t worry about evaluating them yet.

Claude Code would just do it. The `let` form is fairly simple, but anyone who’s done parsing knows it can get very complicated. Without getting too deep into it, PEG parser combinator libraries like `ts-parsec` that combine lexing and parsing into one step can make some things difficult. You need a deep understanding of the parsing library and the grammar to get things to work.

For example, `struct` is a Beep keyword to define records:

```
struct Person
  name, age
end
```

But `ts-parsec` is eager, so if you type `structure` the parser consumes `struct` first, and then throws a parsing error. When I’d find bugs like that I’d tell Claude to fix them, and it would do it effortlessly.

If you look at [parser.ts](https://github.com/coffeemug/beep-lang/blob/f149bfcc120a882020d42479bc7bc29fc68f147f/src/runtime/parser.ts) the code isn’t well-structured. The order of parser combinators is unintuitive and the code is hard to read. Part of the reason is that parser combinator code can just be like that. But a bigger reason is that I deliberately abandoned caring about code quality here, and Claude Code/Opus 4.5 doesn’t magically produce a well-structured codebase by default.

Still, I was very impressed with Claude’s performance. It took an obscure little library in an idiosyncratic domain (parsers) with a lot of obscure type system hackery, and solved nearly every problem at least an order of magnitude faster than I would myself, despite being the library’s author.

## Counterexample: newline sensitivity

I wanted Beep grammar to separate statements using newlines, or statements on the same line using semicolons:

```
def foo()
  1
  2
  3
  4; 5
end
```

`ts-parsec` didn’t initially support this. The reader had two modes: drop or keep all whitespace. Claude Code got in a loop where it was trying different approaches, none of which could plausibly work because the underlying library didn’t have sufficient support to make this possible. Claude looked into `ts-parsec`, understood that support for keeping newlines is missing, but couldn’t quite make the leap to tell me explicitly to solve the problem. I then changed `ts-parsec` reader to support a third mode– `keep_newlines`. Once I made the change, Claude Code trivially modified the grammar to support newline-separated statements.

In most newline-sensitive languages the grammar lets you put `;\n` to end a statement. For example in Javascript you can say:

```
1
2

1;
2
```

This encourages proliferation of styles. Some codebases end each line with a newline, others with a semicolon, and some mix both. I didn’t want to defer these decisions to a linter, and instead decided to encode them in Beep. So I asked Claude to change the grammar to make `;\n` illegal. Again Claude Code got stuck– it tried various approaches, each of which broke something else, and it could never quite get out of that loop. After a while I just fixed the grammar myself.

I bumped into another endless loop when I tried to publish a new version of `ts-parsec`. Mine is under `@spakhm/ts-parsec`, which is called a “scoped” package. There was some npm authentication issue that I was too lazy to figure out, so I asked Claude for advice. It kept giving me various suggestions, none of which worked, until I finally buckled down, RTFM, and figured out the issue myself.

These were the only three examples in this project where the problem was too difficult for Claude Code. The last time I tried it (pre-Opus 4.5) I bumped into these kinds of problems much more often. With Opus 4.5 the difficulty bar to hit a failure mode is higher, and the frequency even on harder problems is lower. But it does sometimes get stuck on simple things like the incantation to publish scoped npm packages.

## Closing thoughts

Many people fear AI will leave them behind. I don’t share this fear. Adjusted for range of capabilities, this is arguably the most intuitive technology ever devised. You talk to it in your native language and it does what you want. You don’t need a class on Claude Code– it’s easier to learn than VS Code! It maybe takes 30 minutes to learn your way around the interface, and over the next day or two it recedes in the background and becomes so natural, you forget you’re using it all. And as it gets smarter, it will understand you better. You don’t have to get better at using AI. AI will get better at being used by you.

(There are also geopolitical fears and economic and science fiction end-of-the-world scenarios. I think there are strong reasons to be optimistic about those too, though I’m less confident on this. I’ll keep this post from devolving into an opinion piece on these topics since I’m out of my depth here.)

Another theme is that AI is all slop and bad code. I don’t share this view either. It’s true that producing bad PRs at scale is easier than ever, and we’ll have to get better at solving this problem. For this project I didn’t use Claude Code as a vibe-coding machine, but rather as a precise code surgery robot and as a partner to bounce design ideas. In this mode Claude made the quality of the codebase _better_ than it otherwise would have been. Claude lowered the barrier to annoying refactors which made codebase hygiene and paying off technical debt easier. It also lowered the cost of brainstorming ideas so I found myself picking cleaner solutions than I would have reached for on my own.

Beep functionality is currently uneven, so progress is hard to judge. It already has reasonably advanced features like user-defined types, methods, closures, and different scoping modes, but is missing some basic functionality like conditionals and loops. I can say with certainty that without Claude there is no way I would have gotten as far as I did in two weeks, interrupted often by holiday events and family obligations. Even more interesting is that were I working alone, the project would have taken a different shape. I would have done simple things first and left more complex features for later. Claude Code led me to frontload complex features because it makes this easy and fun, and because in the back of my mind I always know should I need to implement a simple feature, it’s only a few minutes away with Claude.

**EDIT:** conditionals and loops [now work](https://github.com/coffeemug/beep-lang/blob/master/examples/fizzbuzz.beep).

I’d put the problems in this post at a “good undergraduate” level. They’re accessible to maybe top 5% of CS students at a median US university, and to 85% of CS students at an Ivy. I am _not_ saying Claude Code is a good undergraduate– it’s a different thing altogether. It can do refactors at superhuman speed but can’t publish to npm. What I _am_ saying is that if you’re working at this level of difficulty, Claude Code is a phenomenal coding companion. Setting aside all the productivity arguments, it dramatically amplifies what’s fun about coding by eliminating much of what’s annoying. I would not want to go back to a world without it.

Jan 05, 2026
