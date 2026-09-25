---
url: "https://scottarbeit.com/blog/advent-of-code-2023-a-random-walk-in-the-direction-of-functional-enlightenment"
captured_at: "2026-09-25T20:38:17+01:00"
title: "F# Advent of Code 2023: A random walk in the direction of functional enlightenment"
domain: "scottarbeit-com"
---

> (image by [Simon Berger](https://unsplash.com/@8moments), shared on [Unsplash](https://unsplash.com/photos/leafless-trees-hxMdsEaiSyE))

_I'm pleased to have the Friday-of-Christmas-weekend slot for F# Advent Calendar 2023. That means I know a lot of you will have some time to unwind with a longer read. I hope you enjoy._ 😉

* * *

> _Je n'ai fait celle-ci plus longue que parce que je n'ai pas eu le loisir de la faire plus courte._
> 
> I have made this \[letter\] longer than usual because I have not had the time to make it shorter.
> 
> \- Blaise Pascal, _Provincial Letters_, 1656 [1](#fn:1)

* * *

Hi! I'm Scott. (Hi Scott.) And I've been struggling to think of something interesting to write about for F# Advent of Code 2023.

I mean, I love F#. It's my favorite programming language, ever. It's been the vehicle for me to learn how to think functionally about programming, after two decades of object-oriented\[ish\] programming. And I've never seen a language like this where _almost everyone_ who starts using it regularly, loves it, too.

I know I could do some _Using F# with <insert technology here>!_ posts. And I probably should. I've written around 24,000 lines of F# code for my version control system, [Grace](https://github.com/scottarbeit/grace), for almost three years now, and it uses things like Dapr, Dapr Actors, CosmosDB, Azure Storage, Spectre.Console, and more. I've got some interesting, functional code in there that I could talk about. (I think.) But none of that felt like the right thing to write about.

Anyway, one of the things I've learned about getting unstuck creatively is that sometimes it's best to start just by espressing something about what's present for you, what's going on in your life, right now.[2](#fn:2)

What's going on for me is: I'm working through some of the early code from Grace, figuring out how to rewrite it so it doesn't suck, and stumbling through the bugs I've found because of it.

So, that's what I'll share with you today: some not-great code I wrote a while back, why it's not great, how I'm fixing it, and what that might say about my development with F# and functional programming.

* * *

> _Anything worth doing is worth doing poorly, at first._
> 
> – Brian Tracy, many others

* * *

* * *

> _You don’t have to be great to start. But you have to start to be great._
> 
> – Zig Ziglar

* * *

My hope is that by sharing this part of my journey, I can free you to get started in your own journey with a new programming language (especially F#!).

I started writing an entire version control system when I didn't quite know what I was doing. You can start, too.

### A little bit about Grace

This post isn't meant to be about Grace, but just to give the tiniest bit of context for what's coming:

Grace is a new, modern, cloud-native version control system. It is multi-tenant, centralized, and relies on PaaS products like Azure Blob Storage and AWS S3 for storing versions of files. Because it's centralized, Grace needs to ensure that when commands like `grace switch` or `grace rebase` are run, that the existing state of the branch is saved and uploaded before changes are made to the working directory.[3](#fn:3)

And, yes, it's really fast.

### What I'm working on right now

* * *

> _What the hell?!?_
> 
> – Me, looking at code I wrote a couple of years ago

* * *

Like you'd expect in a version control system, Grace has a command - `grace switch` - that lets you switch to another branch in your repo, and will update your working directory with the current contents of that other branch.

Grace also has a background agent mode - `grace watch` - that maintains a live connection to the server, enabling 2-way communication and local and server-side event processing, and that watches your working directory for changes and automatically uploads after every save-on-disk, allowing most of the more common Grace commands to run incredibly fast.

There's plenty of overlap between those two use cases. Both `grace switch` and `grace watch` have to:

*   understand the current contents of the working directory,
*   make sure that the current contents are uploaded to the server,
*   update the local object cache that holds recent versions of the files in the repo, and
*   update the local Grace Status file that holds the state of the branch.

That means that they share some function calls, of course.

Also, if you run `grace switch` while `grace watch` is running, `grace watch` has to be aware of it and ignore the changes in the working directory until the switch is complete.

The code for `grace watch` is about two years old. `grace switch` came right around the same time, maybe a month or two later. At the time, I wasn't very good at some important things. To make it worse, I was in a hurry writing it. 🤦🏼‍♂️

### The problem (It's me. Hi.)

* * *

> _<stares at monitor, blinking>_
> 
> – Me, looking at code I wrote a couple of years ago

* * *

There's a lot that I hadn't yet learned about thinking functionally. When I look at it now, some of the code is clearly, "yeah, had no clue how to do that." Some of it is, "Awww... that's cute. At least I tried." Some of it is, "I need to come up with better names for those functions."

In the "had no clue" department, you'll find some of my code for Grace's command-line interface (CLI), specifically, the way I'm trying to interleave work being done, like calls to the server, or writing new local files, with UI updates (updating progress bars) that reflect the progress of completing the command.

As I was writing it, I _knew_ it wasn't great. It all looked like the [Pyramid of Doom](https://fsharpforfunandprofit.com/posts/computation-expressions-intro/) \[towards the middle of the article\] that our friend Scott Wlaschin warned us about, that I knew I should avoid, but couldn't figure out how to, and didn't have the time to deeply work through. It _worked_, but it wasn't anything I was proud of. I haven't deeply dived into this part of Grace in a long time, and I knew it would be a challenge to get back into it.

### Let's fix... something

I decided some weeks ago to start by rewriting `grace switch` to be more idiomatically functional, to clean it up as the first example of how to do it for the rest of the CLI commands. This was kind-of stupid, because it's the longest bit of code in all of the CLI commands, it's complex, and would be the most difficult to do. But it was deliberate: if I could make it work for `grace switch` I could make it work for the rest.

#### Before

The "before" code starts [here](https://github.com/ScottArbeit/Grace/blob/c5657f56b56cd67b865f2abe33991b04efa91e62/src/Grace.CLI/Command/Branch.CLI.fs#L1200), and runs for 342 lines. I won't quote it here, and I don't expect anyone to actually read it or comprehend the logic, but if you glance at it, you'll notice how deeply indented the code gets. At its longest, the indentation is -------------------------------------------------------------------- _this_ long. Ugh.

What's worse is that because Grace has multiple output modes – Normal, Json, Verbose, Minimal, and Silent – I duplicated most of the code in this function: once for when I'm showing output, and once for when I'm not. (DRY? Pfft.) That means that if I find a bug, I have to remember to fix it twice. Making a long story short, the logic is:

```
if showOutput then
    // Imagine lots of code with all of the steps to switch branches,
    //   with crazy levels of indentation, 
    //   and then show some output
else
    // Imagine almost exactly the same code,
    //   with crazy levels of indentation, 
    //   and then show little-to-no output
```

It's not my finest work.

#### After

After extracting the work steps into separate functions, it's much easier to understand and deal with.

Let's start with the main part of the new `grace switch` handler function. In the local function `generateResult`, look! monadic bind! With that defined, we check if we should show output, and either create those progress bars, or not:

```
let generateResult (progressTasks: ProgressTask array) =
    task {
        let! result = 
            (showOutput, parseResult, switchParameters)
            |> validateIncomingParameters
            >>=! getCurrentBranch progressTasks[0]
            >>=! readGraceStatusFile progressTasks[1]
            >>=! scanForDifferences progressTasks[2]
            >>=! getNewGraceStatusAndDirectoryVersions progressTasks[3]
            >>=! uploadChangedFilesToObjectStorage progressTasks[4]
            >>=! uploadNewDirectoryVersions progressTasks[5]
            >>=! createSaveReference progressTasks[6]
            >>=! getLatestVersionOfNewBranch progressTasks[7]
            >>=! UpdateWorkingDirectory progressTasks[8]

        match result with
            | Ok _ -> return 0
            | Error error ->
                logToAnsiConsole Colors.Error $"{error}"
                return -1
    }

if showOutput then
    return! progress.Columns(progressColumns)
            .StartAsync(fun progressContext ->
            task {
                let t0 = progressContext.AddTask($"[{Color.DodgerBlue1}]{UIString.getString GettingCurrentBranch}[/]", autoStart = false)
                let t1 = progressContext.AddTask($"[{Color.DodgerBlue1}]{UIString.getString ReadingGraceStatus}[/]", autoStart = false)
                let t2 = progressContext.AddTask($"[{Color.DodgerBlue1}]{UIString.getString ScanningWorkingDirectory}[/]", autoStart = false)
                let t3 = progressContext.AddTask($"[{Color.DodgerBlue1}]{UIString.getString CreatingNewDirectoryVersions}[/]", autoStart = false)
                let t4 = progressContext.AddTask($"[{Color.DodgerBlue1}]{UIString.getString UploadingFiles}[/]", autoStart = false)
                let t5 = progressContext.AddTask($"[{Color.DodgerBlue1}]{UIString.getString SavingDirectoryVersions}[/]", autoStart = false)
                let t6 = progressContext.AddTask($"[{Color.DodgerBlue1}]{UIString.getString CreatingSaveReference}[/]", autoStart = false)
                let t7 = progressContext.AddTask($"[{Color.DodgerBlue1}]{UIString.getString GettingLatestVersion}[/]", autoStart = false)
                let t8 = progressContext.AddTask($"[{Color.DodgerBlue1}]{UIString.getString UpdatingWorkingDirectory}[/]", autoStart = false)

                return! generateResult [| t0; t1; t2; t3; t4; t5; t6; t7; t8 |]
            })
else
    // If we're not showing output, we don't need to create the progress tasks.
    return! generateResult [| emptyTask; emptyTask; emptyTask; emptyTask; emptyTask; emptyTask; emptyTask; emptyTask; emptyTask |]

```

I even created a custom monadic bind function and operator for it!

```
let bindTaskResult (result: Task<Result<'T, 'TError>>) (f: 'T -> Task<Result<'U, 'TError>>) =
		(task {
				match! result with
				| Ok returnValue -> return (f returnValue)
				| Error error -> return Error error |> returnTask
		}).Unwrap()

/// Custom monadic bind operator for the nested monad Task<Result<'T, 'TError>>.
let inline (>>=!) (result: Task<Result<'T, 'TError>>) (f: 'T -> Task<Result<'U, 'TError>>) =
		bindTaskResult result f
```

And instead of all of it in one huge function, here's a sample of some of that logic broken down into a smaller function that's easy to understand, with fewer places for bugs to hide, that handles its own output. This is the part that checks for changes in your working directory:

```
// 2. Scan the working directory for differences.
let scanForDifferences (t: ProgressTask) (showOutput, parseResult: ParseResult, parameters: CommonParameters, currentBranch: BranchDto) =
    task {
        t |> startProgressTask showOutput
        let! differences = 
            if currentBranch.SaveEnabled then
                scanForDifferences newGraceStatus
            else
                List<FileSystemDifference>() |> returnTask
        t |> setProgressTaskValue showOutput 100.0
        return Ok (showOutput, parseResult, parameters, currentBranch, differences)
    }
```

### Mission Accomplished!

So, yay! Cleaner code, easier to maintain, less duplication. Winning!

### uhh...

But... not exactly. After I refactored the code and started testing it, I found some bugs, and those bugs go all the way back to when I wrote `grace watch` and `grace switch` in the first place. Some of those bugs have now been fixed. A few remain that I'm tracking down.

All of them have the same root causes: an early, less-developed sense of what good functional programming looks like, and a lack of careful thinking, reflected in a lack of carefully-written code.

### For instance...

> _Why is this happening? Better add some_
> 
> `logToConsole $"...stuff..."`.
> 
> – Me, debugging code I wrote a couple of years ago

In Services.CLI.fs, I have a function called `getNewGraceStatusAndDirectoryVersions`. You can see it [here](https://github.com/ScottArbeit/Grace/blob/c5657f56b56cd67b865f2abe33991b04efa91e62/src/Grace.CLI/Command/Services.CLI.fs#L536).

It's almost 200 lines long. That may or may not sound like a lot to you, but, to me, now used to F# and thinking in terms of small, single-purpose, composable functions, it's a lot, it's probably too much, and it's a code smell.

In my first job out of college, in 1991, as a mainframe COBOL programmer for AT&T, I remember the senior programmer on the team telling me, "Most people can only hold about a screenful of code in mind at any given time," and that was back when we used 24 x 80 character green-screen monitors!

That same senior programmer had worked on that code for its entire six-year existence, and had previously worked on the system it replaced for many years. When I asked him questions about the code, like why a certain module was written the way it was, he would look up, scratch his chin, and start into a story like "well, about four or five years ago, there was this requirement..." or "in the old system, about ten years ago, <something>... and we never cleaned that up." It was _always_ a story, and almost always something that, if you didn't have the context from that story, would be much more difficult to understand.

That experience led me to one of my most important rules for programming:

**Never write code that you have to tell a story about.**

200-line functions are not good for comprehensibility or maintainability. They invite subtle bugs. They're hard to debug when you've never seen them before. (And, apparently, even when I wrote it myself.) If you get asked about why they are they way they are, you probably have to tell a story, and that's not good.

My story for `getNewGraceStatusAndDirectoryVersions`: _I wasn't very good at this when I wrote it._ 🤷🏼‍♂️

Also, the function name itself is a code smell. If your function name has "and" in it, that's a good sign that it's doing too many things and should be broken down into smaller pieces.

That's exactly what I'm working on: refactoring `getNewGraceStatusAndDirectoryVersions` and some of its related functions that are called both by `grace watch` and `grace switch`. It's a slog. I was trying to think in functions back then, but they're not shaped well, they do too much, and they're just hard to understand. I don't want to tell that story. I don't want to leave that for the next maintainer, who could be Future Me.

(You may have noticed that I still have that name for a smaller function in my refactored `grace switch` code, and I'll be looking at that, too.)

### My development in F#

So where am I in my F# journey?

Well, I've gotten a much better sense of "how big is too big?" and "how complex is too complex?" when creating and refactoring functions. I might write a first-draft of a new function that's a bit long, but I immediately start breaking it down into smaller parts that are easier to understand, so I don't have to tell any stories for someone else to maintain the code.

As I showed above, I've figured out how to use monads in interesting ways to help write concise, easy-to-understand code.

I'm comfortable thinking about functions as first-class language constructs that can be passed as parameters, and I've gone through all of the phases of "I still use classes because I'm still embedded in OO thinking" to "I never use classes because I'm cool like that" to "I use classes where it makes sense".

And I'm 100% willing to dive in and rewrite some of the less elegant, older code that gets in the way of moving forward quickly.

Some of Grace is really clever and well-written, if I do say so myself. For instance, the way I do parameter validations in Server API endpoints is kind-of neat. I create an array of function calls that check the values passed in, return a custom error if they fail, and I execute them before I run the "real" action of the endpoint. It took a bit to figure out the right pattern, but once I did, repeating if for all of the API endpoints has been easy. Here's an example, from the endpoint to [set the name of an organization](https://github.com/ScottArbeit/Grace/blob/c5657f56b56cd67b865f2abe33991b04efa91e62/src/Grace.Server/Organization.Server.fs#L144-L165):

```
let validations (parameters: SetOrganizationNameParameters) (context: HttpContext) =
    [| Guid.isValidAndNotEmpty parameters.OwnerId InvalidOwnerId
       String.isValidGraceName parameters.OwnerName InvalidOwnerName
       Input.eitherIdOrNameMustBeProvided parameters.OwnerId parameters.OwnerName EitherOwnerIdOrOwnerNameRequired
       Guid.isValidAndNotEmpty parameters.OrganizationId InvalidOrganizationId
       String.isValidGraceName parameters.OrganizationName InvalidOrganizationName
       Input.eitherIdOrNameMustBeProvided parameters.OrganizationId parameters.OrganizationName EitherOrganizationIdOrOrganizationNameRequired
       String.isNotEmpty parameters.NewName OrganizationNameIsRequired
       String.isValidGraceName parameters.NewName InvalidOrganizationName
       Organization.organizationExists parameters.OwnerId parameters.OwnerName parameters.OrganizationId parameters.OrganizationName OrganizationDoesNotExist
       Organization.organizationIsNotDeleted parameters.OwnerId parameters.OwnerName parameters.OrganizationId parameters.OrganizationName OrganizationIsDeleted |]
```

`validations` here is a function that takes in a parameter object, and the HttpContext, and returns `ValueTask<Result<unit, OrganizationError>> array`. With that in place, when I run the validations, I can use a utility function `allPass` to say:

```
let validationResults = validations parameters context
let! validationsPassed = validationResults |> allPass
```

* * *

I have some small but nice utility functions to serialize and deserialize objects, using Grace's custom [JsonSerializerOptions](https://github.com/ScottArbeit/Grace/blob/c5657f56b56cd67b865f2abe33991b04efa91e62/src/Grace.Shared/Constants.Shared.fs#L18-L48):

```
/// Serializes an object to JSON, using Grace's custom JsonSerializerOptions.
let serialize<'T> item =
    JsonSerializer.Serialize<'T>(item, Constants.JsonSerializerOptions)

/// Serializes an object to JSON and writes it to a stream, using Grace's custom JsonSerializerOptions.
let serializeAsync<'T> stream item =
    task {
        return! JsonSerializer.SerializeAsync<'T>(stream, item, Constants.JsonSerializerOptions)
    }

/// Deserializes a JSON string to a provided type, using Grace's custom JsonSerializerOptions.
let deserialize<'T> (s: string) =
    JsonSerializer.Deserialize<'T>(s, Constants.JsonSerializerOptions)

/// Deserializes a stream of JSON to a provided type, using Grace's custom JsonSerializerOptions.
let deserializeAsync<'T> stream =
    task {
        return! JsonSerializer.DeserializeAsync<'T>(stream, Constants.JsonSerializerOptions)
    }
```

These let me say things like

```
    let json = serialize myThing
    let myThing = deserialize<MyThing> json
		
    logToConsole $"DirectoryVersion: {serialize directoryVersion}"

    override this.ToString() = serialize this
```

etc. really easily wherever I need to.

* * *

There's much more in Grace's code that I'd show you, but, the details aren't important for this.

I still have lots more to learn about F# and about functional programming.

I've never used [statically-resolved type parameters (SRTP)](https://learn.microsoft.com/en-us/dotnet/fsharp/language-reference/generics/statically-resolved-type-parameters). I've never used or created a [type provider](https://learn.microsoft.com/en-us/dotnet/fsharp/tutorials/type-providers/). I've never created a [custom computation expression (CE)](https://chat.openai.com/share/983151de-64ac-4ded-8b4d-220606495559), and I still don't have an intuitive grasp of when creating and using one would improve my code. I have a basic understanding of [category theory](https://www.youtube.com/playlist?list=PLbgaMIhjbmEnaH_LTkxLI7FMa2HsnawM_), but I'd love to deepen that and use more of the patterns from category theory where they make sense in my code. I've never written Haskell, and knowing Haskell, and being able to compare it to F#, would, no doubt, be helpful.

I say all of that to say: I'm not at the beginning of my journey in F# anymore. And I'm far from the end of it. I'm solidly in the middle, and that means that I'm good enough to be creative and concise, and to feel good about the code I'm writing now.

And, probably, one day, I'll look back on the code I write in 2024 and think, "I can do that better now."

### We've all come a long way

Debugging and refactoring that older code over the last few weeks has been a trip. It's like visiting a younger version of myself.

Even though that code isn't as elegant as I'd like it to be, I'm still proud that I wrote it.

And you should be proud of where you are in your journey. If you're a programmer (and if you've read this far, you probably are) then you've had your experience of starting knowing nothing, writing and shipping code even though you weren't very good at it yet, and consistently improving, maybe even approaching mastery with the languages and tools you use.

I'm proud that I stuck with F#.

I'm proud that I'm still working on Grace.

I'm proud that I can see the progress I've made, and it gives me proof that I can still learn completely new things, move from beginner to experienced to mastery, and continue to develop both my art and craft.

So can you. I hope you will.

* * *

* * *

1.  See [https://en.wikiquote.org/wiki/Blaise\_Pascal#Quotes](https://en.wikiquote.org/wiki/Blaise_Pascal#Quotes).[↩](#fnref:1)
    
2.  When I say "right now," I mean: I'm interrupting my programming to write the first draft of this blog post on December 20th, 10:00 PM, two days before publishing it.[↩](#fnref:2)
    
3.  Yes, this means there's no `grace stash`, you don't need it.[↩](#fnref:3)
