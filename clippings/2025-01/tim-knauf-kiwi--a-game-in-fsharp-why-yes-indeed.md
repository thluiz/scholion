---
url: "https://tim.knauf.kiwi/blog/posts/2024/truffle-wizard-game-in-fsharp/"
captured_at: "2025-01-13T23:57:07+00:00"
title: "A Game in F#? Why, yes indeed."
domain: "tim-knauf-kiwi"
---

The making of Truffle Wizard

December 7, 2024

_Thanks Sergey Tihon for running the 2024 [F# Advent Calendar](https://sergeytihon.com/2024/10/26/f-advent-calendar-in-english-2024/)! This post is my contribution._

### What the heck is a Truffle Wizard?

[Truffle Wizard](https://timknauf.itch.io/truffle-wizard) is a short incremental game with truffles, clicking and _almost definitely_ no forbidden magic. You can play it in your web browser, on desktop or mobile.

An unusual thing about Truffle Wizard is that it doesn’t use a classic ‘gaming’ language, like C++, C# or even Lua. Nor does it use a ‘web’ language like Javascript or TypeScript. **Truffle Wizard is written in the functional language F#.** This is the story about how that came to be\*, and my experience with developing a game entirely in a functional language.

Spoiler #1: it was a very positive experience!

Truffle Wizard is open source! So if anything in this post arouses your curiosity, [check out the repository](https://hg.sr.ht/~timknauf/truffle) to see how the (truffle) sausage is made.

_\* My honest heart compels me to tell you that I’ve simplified some of my timeline here for the sake of clarity!_

### Who is this for?

This post is aimed at two audiences:

1.  Game developers who have learned a little about functional programming, see the appeal, but are wondering whether it could ever be applied to games _(this was me a few months back)_
2.  F# aficionados, who love the language but aren’t sure whether they can confidently recommend it as a language for game development

Spoiler #2: I think the answer is a qualified yes to both!

### My background

I’ve been making video games of various sorts since the early-mid naughties (goodness!). In my day job, I’ve been in Unity shops for over a decade now, immersed in C#. Before then, I slung Objective-C in the early days of the iPhone, and before _that_, I was part of the last big wave of Flash developers – and one of the seemingly few who enjoyed writing ActionScript 3!

For hobby projects, I love the creative constraints of [PICO-8](https://www.lexaloffle.com/pico-8.php) and its cousin [Picotron](https://www.lexaloffle.com/picotron.php); Lua is the scripting language of choice for both of those. Way back in the mists of time, I was sole developer for what we’d now call a web app, writing Rails-flavoured Ruby as best I could.

### Glimpses of functional beauty

Looking at those programming languages, you’ll note that not one of them is what we’d call a ‘functional’ language! Games have grown up wedded to the object-oriented tradition, and that’s been my world for my entire career.

But I’ve long had an awareness that objects, with behaviour all bound up with state, aren’t the only way to express yourself to a computer! I remember really enjoying learning some Haskell at university. Some of my classmates hated it – why not just tell the computer what you want instead of having to express it as a maths equation? (Their words, not mine!) For myself, I couldn’t see how I could apply this paradigm to my first love, game development, but I _did_ see the beauty of purely transforming data, even if the ‘zen of Haskell’ eluded me.

I mean, how can you not love the inscrutable beauty of this?

```
qs [] = []
qs (x:z) = qs [y|y <- z, y<x] ++ [x] ++ qs [y|y <- z, y >=x]
```

### The impetus: reasoning about state

I have this long-running side project idea that I keep returning to – a strategy game. (Truffle Wizard is not that game, but I’ll get to that, I promise!) The design is simulation-heavy, with a proper economy and a bunch of feedback loops.

Some months back I decided that I decided that it was high time to actually make a prototype of that game. I got stuck in with Picotron, and made some good progress with a little Lua-based strategy engine.

Lua is an _extremely_ flexible language, and I wouldn’t want to just lump it in with classic object-oriented languages. Yet despite its flexibility – or maybe because of it?! – development on the project started to feel more and more painful.

I had a good think about what was going on.

My colleagues will tell you that I’m, ah, _very keen_ on being able to “reason about state”. What does this mean? Basically, I want to be able to “run the code in my head” with at least reasonable confidence. I want to be able to look at a running game that I (or we) have written, and have some chance of understanding:

1.  the internal state it's in,
2.  how it arrived at that state, and
3.  the state it will be in next, for any given action the player might take.

Writing game code that allows us to do that is surprisingly hard! Games are state machines at heart, but usually (in my experience) they’re state machines with a _truckload_ of possible states, and an almost infinite variety of ways you can move from one state to another.

So I’ve developed this mini obsession with well-defined state that moves through well-defined transitions. Ideally, each state is cleanly derived from a) a player action and b) a previous state. Why, it almost sounds like we could plug those two things into some sort of well-defined formula that could derive the new state. Some sort of state-deriving… **function**?!

### Slow down to speed up

So, my strategy game side project? That sort of systems-heavy game design isn’t my native tongue (though I am a keen learner!). The code was getting away from me, even in the early prototype. I was finding it hard to reason about the next ‘tick’ of the simulation; how exactly would the state change, and why? In a surely related problem, my data structures were getting hard to hold in my head. I bolted on types ad-hoc with [Lua language server annotations](https://github.com/LuaLS/lua-language-server/wiki/Annotations), but now I had what felt like a ton of boilerplate type annotations to manage.

Possibly worst of all, I needed to be extremely careful lest I set up a state mutation, in a way I wouldn’t be able to track or remember later. Lua can support immutable data structures – like I said, it’s flexible! – but its idioms push you towards big ol’ key-value stores. Keys may be present or may be nil, values are expected to change – and Lua APIs, libraries and code samples are all set up with those expectations. For me, it requires a lot of discipline to write Lua in a different mode to that!

If you know anything about functional programming, you’ll be smiling as you read my summarised list of complaints:

*   “It’s hard to reason about my state!”
*   “Detailed types are helpful but now I’m writing loads of boilerplate definitions!”
*   “Yikes, it’s easy to accidentally mutate state!”
*   _Bonus complaint! “Despite my best intentions, I’m doing many null checks.”_

I really believe that Lua is a great language for games: it’s an all-purpose multi-tool that is, has been, and should continue to be used across most game genres. But if I wanted to get serious about learning to design and program systemic games (and I did!), it felt like my opportunity to research and learn whether there might, for me, be a different way. I don’t like abandoning work-in-progress, but as a wise colleague once said, “sometimes you have to slow down to speed up.”

### F# for Fun and Profit

At this point I could have reached for C# and Unity. I know them very well from my day job! But around the time I was having these thoughts, I was drawn back to a site that I had browsed with interest in the past, but couldn’t quite see how it could apply to me: Scott Wlaschin’s wonderful [F# for Fun and Profit](https://fsharpforfunandprofit.com/). In particular, the thought of [Railway-Oriented Programming](https://fsharpforfunandprofit.com/rop/), also known as “happy path programming”, just seemed so _delightful_:

```
let executeUseCase =
  receiveRequest
  >> validateRequest
  >> canonicalizeEmail
  >> updateDbFromRequest
  >> sendEmail
  >> returnMessage
```

_Yes, I realise that I’ve just used the word delightful to describe an email validation workflow. I stand by it! Delightful it is!_

Upon seeing this, and others like it, my brain lit up. It’s so, well, easy to reason about! I guess it’s not beautiful zen code like the Haskell example; this speaks more of elegant pragmatism. And that’s an important thing I realised about the F# community and the F# style, actually: as best I can tell, yes, the community does enjoy **elegance**, and the language’s design encourages that. But it’s also a **pragmatic** language for people who like to ship things. Holding both those things together works really well for me!

So, I got to thinking: what if all my state transitions could be defined right out in the open? What if rich types could be omnipresent, but inferred 95% of the time? Could I have immutable by default, and also never have to do another null check? Sign me up, surely!

### For games, though?

But could this be applied to game development? Well, maybe it could! C# rules the .NET ecosystem, but I could see that F# still gets plenty of support both from Microsoft and the open-source community. My understanding is that F# can do _nearly_ everything C# can do, with many tricks of its own.

It felt too intimidating to dive back into my full strategy game project while trying to learn a new language. I’m big on creative constraints, and so I ‘dreamed smaller’. I knew that I should still do a systemic game, with an economy – that was the impetus for this whole learning journey, after all! But what could be a small enough project, yet still meaningfully a game?

Ah, of course: a [clicker](https://en.wikipedia.org/wiki/Incremental_game). I could even do it without graphics. And that simplified clicker concept is what eventually became Truffle Wizard!

Could I build a simple incremental game with all the game logic in a functional language – specifically, F#? And could I do it while sticking to what I understood as idiomatic F#: pure functions, algebraic types, immutable state?

### Choosing the engine

#### Unity: a mild disappointment

Early experiments with Unity were a little disappointing. You can build a .NET assembly from F#, and Unity will accept it just fine. But Unity is so, so mutable and object-oriented at its heart. It felt like there was a deep mismatch, which I’d be constantly having to shim – or perhaps treat Unity purely as a renderer for state created in F#? Either way, it didn’t feel like I’d be working to what I’ve come to see as Unity’s strengths: component-based design and an editor-heavy workflow.

#### Raylib: very promising

I moved from heavyweight to bantamweight: Raylib, specifically the supremely awkwardly-named [Raylib-CsLo](https://github.com/NotNotTech/Raylib-CsLo) .NET bindings. I’m still learning about Raylib, but I’m already a big fan. For a lot of side-project type games, it could be a total sweet spot, and I wondered if it might be right for Truffle Wizard.

My initial proof-of-concept with Raylib saw me using imperative-style C# to instruct Raylib: run the Raylib render loop, poll the inputs etc. Then F# ran the game’s systemic ‘core’: a separate .NET assembly, running the game logic. I did it this way because I assumed I would have to! Surely, I thought, with F# being so functional, it’s going to do a poor job of running an imperative loop?

I’m delighted to say that I was wrong – very wrong! Unity has that deeply object-heavy approach, but from what I’ve seen so far, Raylib isn’t like that at all. I found that I could drive Raylib’s core loop in slightly _fewer_ lines of F# than I had used for C#.

Raylib does have some state of its own to set up, but once that’s done, you can generate your game state cleanly and immutably, then just ‘feed’ that to Raylib imperatively each frame. So far, it’s worked beautifully.

For my next side project, I intend to jump right back in with Raylib. I really think F# + Raylib could make a great marriage, and I’m excited to try it for future side projects.

#### Fable and Feliz: the right fit for _this_ project

But you don’t have to be very observant to notice that Truffle Wizard doesn’t use Raylib. It’s not even using a traditional game engine at all. It’s running on a web stack.

Why did I turn away from Raylib, which was looking so promising? Truffle Wizard’s “magical spreadsheet” look amused me _(okay, I’m easily amused)_, and it made a great gameplay constraint to stop my design ideas from spiralling out of control. On the other hand, it _almost immediately_ became an awkward fit for a traditional, single-screen, non-scrolling game view. I had to hand-manage the UI, and had no idea what I would do when the table got big enough to spill off the bottom of the screen. Implement a bunch of my own scrolling routines, I guess?

So I had some needs: presenting tables of data with many small bits of writing, flexible scrolling, and a helpful UI framework wouldn’t hurt. Hmm, I think I know a platform where those needs might be met!

So yes, I started looking at what might be available to me for “F# on the web”.

Enter the incredible [Fable](https://fable.io/). Fable is, among other things, a very sophisticated F#-to-Javascript compiler (transpiler?). You’re able to write F#, some magic happens, and a full Javascript-powered web app pops out the other end. Add to that [Feliz](https://github.com/Zaid-Ajaj/Feliz), which gives you the power of React, while letting you continue to write idiomatic F#, largely pretending that the giant web stack underneath you doesn’t exist.

This type of “tower of technologies” isn’t normally my happy place for a side project! I feel like I get enough “towers of technologies” in my day job, so having a bunch of layers I didn’t understand made me nervous. But in practice, I didn’t run into _any_ problems – the web stuff ‘just worked’, and continued to just work. Huge kudos to the creators; obviously incredible work has gone on behind the scenes there! (And thank goodness for me, because I generally try to learn just one hard new thing at a time!)

### Game logic in F#

Finally, we reach the nuts and bolts of how my game loop actually runs in F#. I use the [Elmish](https://elmish.github.io/elmish/) style borrowed from the [Elm](https://elm-lang.org/) language\*, which is conceptually beautifully simple:

1.  An `init` function produces a starting state **state**
2.  A `dispatch` function routes a **message**
3.  An `update` function takes the existing state and a message, and produces a **new state**
4.  A `render` function turns the state into what the player sees: a **view**

I highly, highly recommend this model, and I’ll try to explain why as I go.

I don’t think you need to literally use the Elmish package, by the way. While I need to do some more experimentation, I think a simple hand-rolled ‘Elmish style’ architecture would probably work just fine, at least to the level that games need.

_\* Why didn’t I implement Truffle Wizard in Elm? I think that would have been a fine choice, actually! I persisted with F# because that was the language I had set out to learn, and because I think there’s so much potential for F# to marry up with other technologies, post-Truffle Wizard._

#### The state

The important thing to understand about the state data structure is that it contains _every single tiny little piece of state the game ever needs_, all in the one place.

If that sounds awful, it might help to think of it this way: your game, written in any language, is going to need all that state anyway. You’re just collecting it all into the one place. Also (and I think this is key!), you’re not tracking a hundred ‘usually nil’ fields. Here’s the entire State type for Truffle Wizard:

```
type State = {
    Tick: TickCount
    Inventory: Inventory
    Unlocks: Unlocks;
    SaveLog: string;
    View: ViewState;
}
```

Of course, some of those are data structures in their own right, but thanks to F#'s [discriminated unions](https://fsharpforfunandprofit.com/posts/discriminated-unions/) – AKA [“enums on steroids”](https://danielbachler.de/2020/12/23/what-i-wish-i-knew-when-learning-fsharp.html) – state only ever contains the data that it actually needs at any given time.

A side benefit of keeping State in one place is that saving and loading games is suspiciously easy! I mean, this tiny function is basically the entire save system:

```
let save state =
    let saveData = state |> toSaveDto |> serialize
    localStorage.setItem (keyName, saveData) |> ignore
    { state with SaveLog = "Saved to local storage" }
```

#### Dispatching messages

I won’t dwell on this one too long, partly because I’m not sure that I understand the internal details of how dispatches are routed by Feliz and Elmish! But in use, dispatch functions are nice and simple to deploy from your view code. Here’s the relevant line for one of the first actions you take in the game, harvesting a truffle:

```
prop.onClick (fun _ -> dispatch (Produce resource))
```

That `prop` is a React button – “Rootle for Truffles”. `Produce` is a message (or you can think of it as a command) and `resource` is the resource in question – in this case, a truffle.

Truffle Wizard also runs autonomously, of course – that’s part of its whole deal. To do this, the game sets up a timer, to send itself a `Tick` message every 250 milliseconds:

```
JS.setInterval
    (fun _ -> dispatch (onTick DateTime.Now))
    250
```

And then later, I set up a `subscribe` function, which dispatches the `Tick` message to the update function:

```
let subscribe model =
    [ ["timer"], timer Tick ]
```

_I’m gliding over some details on scheduled Javascript callbacks because, er, I haven’t actually grokked how Fable handles the interop! Please check out the [main module](https://hg.sr.ht/~timknauf/truffle/browse/src/Main.fs) to see how those two snippets fit together, and be aware that it was adapted from example code. Fortunately, for many types of game, if you can receive a timing callback and/or a ‘new frame’ callback, you may not need much more._

#### The update function

The update function has to take existing state – the entire state of the game – plus a message, then return a new state. You might think that would make for a crazy-complicated function, right? It took a bit of thinking it through, but eventually I was able to land on what I think is a lovely, easy-to-follow core update logic:

```
function
| Produce resource -> modifyInventory (incrementResource resource)
| BuildGenerator resource -> modifyInventory (incrementGenerators resource)
| BuildStorageFacility resource -> modifyInventory (incrementStorageFacilities resource)
| Venture adventure -> modifyInventory (haveAdventure adventure)
| Tick _ -> tryTick
| Save -> Persistence.save
| Load -> Persistence.load
| Reset -> reset
| Menu RequestReset -> requestReset
| Menu CancelReset -> cancelReset
| Menu Show -> showMenu
| Menu Hide -> hideMenu
```

Even if you have no clue how F# works, I think you could speak with some confidence about what’s going on there.

(If you’re wondering, “but will this scale?!”, I think the answer is probably, “yes!” I would start by delegating to sub-functions. For instance, the four `Menu`\-related messages there could be collapsed into one, delegated to a menu-processing function.)

F#'s `with` keyword gives the power to generate a new state while still preserving immutability. Here’s a bit of code I consider a bit ugly – yet it still gets its state-update job done in a safe way that I find easy to reason about:

```
let tryTick state =
    // Autosave every 2 seconds
    let shouldAutoSave = (not Cheat.manualSaves) && state.Tick % 8L = 0L
    let state = if shouldAutoSave then Persistence.save state else state
    
    let cadence = 4L / (Effects.generatorMultiplier state.Inventory)
    let inventory = if state.Tick % cadence = 0L then tickGenerators state.Inventory else state.Inventory
    { state with Inventory = inventory; Tick = state.Tick + 1L }
```

That `with` at the end is saying, “make a copy of the existing state, please, but with the modifications I’m about to give you.”

#### The render function

Again there’s a single function for the view: `render`. It takes a state and a dispatcher function, and returns a view.

What does “return a view” mean? Elmish isn’t opinionated about that; the idea is that you build up a data structure describing how to display your game, and hand it off to whatever ‘engine’ your game uses to display stuff. For Truffle Wizard, I build up a hierarchy of DOM elements using Feliz, as shown in this function which renders each of the table rows:

```
let resourceRow state dispatch resource =
    [
        Html.tr [
            prop.children (
                [renderProduceCell; renderStorageCell; renderGeneratorCell]
                |> List.map (fun f -> f resource state dispatch)
            )
        ]
    ]
```

Feliz takes care of the details for me, thank goodness. Presumably React then does some differential DOM magic, and the end result is that a `<tr>` table row element shows up in your browser.

_(If I do go back to Raylib next, I’ll have to figure out what a ‘good’ render data structure looks like there. Currently, I assume that I could build up a list of rendering function calls – somehow – and then get Raylib to just run through the list from top to bottom, calling them all. But we shall see!)_

### Short aside: ChatGPT

I have to call out ChatGPT as a very capable\* “F# advisor”. Learning the language with this on hand felt very different to the last time I learned a new technology. Asking, _“I’ve written this F# code and it works, but I suspect it’s not idiomatic; can you offer suggestions?”_ produced helpful answers, and I believe it’s lead to my code being more concise and yes, more idiomatic.

This is way better than the results I tend to get for Unity questions. My assumption is that the training data for the LLM just includes a lot of high-quality answers from the wise F# community! (I’ll leave the implications of the Unity training data as an exercise for the reader…)

_\* With the ‘4o’ model. I’m sure ‘4o-mini’ is good for some things, but it seems to be rubbish at F#._

### Did I achieve Railway-Oriented Programming?

There are _occasional_ nice moments in Truffle Wizard’s code where the data ‘flows’, piped from line to line, processed from one form to another. But no, I haven’t yet internalised the lessons of Railway-Oriented Programming – there are a lot of places in my code that look inelegant, at least to my eye.

But I think that’s okay! Even with my amateur use of F#'s rich set of features, I found I could introduce, prototype and (if I needed to) remove systems with ease. I could refactor with so little fuss that I sometimes couldn’t believe a refactor had happened at all. Bugs were rare, and generally I already knew exactly what line to change the moment I saw them in-game.

And most importantly for me, I found the gameplay state _so easy to reason about_. Ah, bliss.

### What’s next?

Will my next side project game use F#? Almost certainly! Working with it on this project was honestly a joy. I’m trying to think of something to complain about, but nothing is coming to mind!

I’m particularly keen to dive back into Raylib and put some of my theories to the test.

Further in the future, I note that Fable can compile not just into Javascript, but other languages as well. Now, if there were to be a Lua compilation target, I would be able to write in F# for my beloved PICO-8 and Picotron. Sadly, adding this to Fable myself is currently a bit beyond me, but a dev can dream!

### Thanks!

If you’ve read this far, thank you! This was my first longer-form technical blog post. I really appreciate your attention.

_Special thanks to Calum Spring for your detailed feedback on the draft version._
