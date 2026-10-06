---
url: "http://www.codeproject.com/Articles/39031/Making-DSLs-in-F"
captured_at: "2012-06-12T16:02:14-03:00"
title: "Making DSLs in F# - CodeProject"
domain: "codeproject-com"
---

## Contents

- [Introduction](http://www.codeproject.com/Articles/39031/Making-DSLs-in-F#Introduction)
  - [Source Code](http://www.codeproject.com/Articles/39031/Making-DSLs-in-F#SourceCode)
- [Problem Statement](http://www.codeproject.com/Articles/39031/Making-DSLs-in-F#ProblemStatement)
  - [End Users](http://www.codeproject.com/Articles/39031/Making-DSLs-in-F#EndUsers)
  - [Continuous Process Improvement](http://www.codeproject.com/Articles/39031/Making-DSLs-in-F#ContinousProcessImprovement)
- [Choosing a Language](http://www.codeproject.com/Articles/39031/Making-DSLs-in-F#ChoosingaLanguage)
- [First DSL Statement](http://www.codeproject.com/Articles/39031/Making-DSLs-in-F#FirstDSLStatement)
- [Handling Lists](http://www.codeproject.com/Articles/39031/Making-DSLs-in-F#HandlingLists)
- [Referencing with Strings](http://www.codeproject.com/Articles/39031/Making-DSLs-in-F#ReferencingwithStrings)
- [Greater Fluency](http://www.codeproject.com/Articles/39031/Making-DSLs-in-F#GreaterFluency)
- [Generating the Project](http://www.codeproject.com/Articles/39031/Making-DSLs-in-F#GeneratingtheProject)
- [Conclusion](http://www.codeproject.com/Articles/39031/Making-DSLs-in-F#Conclusion)

## Introduction

If you're like me, you are already fed up with people throwing the term ‘DSL’ around without showing a good example of how it’s done and where they are used – not to mention giving a decent, human-readable description of DSLs that doesn't allude to extraneous concepts (I'm talking about things like Oslo or MPS, mainly).

Okay, what on Earth is a DSL? A DSL is a way of defining domain-specific (you could say industry-specific, but it can be much narrower) logic using English instead of a programming language. The obvious benefit is that non-technical people can edit the DSL, without worrying about curly braces, semicolons, that sort of thing.

In this article, I'm going to show how to use the F# programming language to make a simple DSL that helps with software estimation. Just so you know, it’s a real-life example, with a more complex version of the DSL being used at our company. All right, let’s hit it!

Just to say upfront, this article doesn't present book-perfect F# code, the reason being that it doesn't really matter since F# code is our end-product. I can think of a dozen ways to improve the F# code presented, but, as I said, that’s not the purpose of this exercise.

### Source Code

The attached code is a single *.fs* file, since I would probably get flogged for posting a VS2010 solution. I hope you know what to do with it. To run it, you need to have Project 2007 installed on your machine – otherwise it won’t work. Good luck!

## Problem Statement

When someone wants software written, they typically contact a software development company with something called an RFP, short for “Request for Proposal”. Depending on the level of detail of this RFP, the code shop can either do a detailed estimate or give a ballpark figure. Barring cases of clients wanting dedicated teams or having vague requirements, the estimate the code shop makes is a fixed-price project timeline. Yeah, I know it doesn't sound particularly agile to people, but in situations where the prospective client has done lots of up-front design, it actually makes sense.

Anyway, someone has to do the estimate, i.e. partition the project into tasks, give them duration, assign resources (= people) to tasks, define milestones, et cetera. This sort of estimate can be done in a program such as Microsoft Project – a good choice in our case, since automating Office from an F# app is easy.

So why a DSL then? Well to be honest, you can probably do an estimate at the 10th of the time it takes to draw up the GANTT chart with all the reorderings and point-and-click mechanics of Project. Not only that, but typically you need to apply some sort of logic (i.e. use your brain, ugh!) to make sure the project plan is nice and balanced (I mean resource utilization and such). Having a DSL means you can optimize *and* autogenerate the plan. With a DSL, you can stick as much business logic into your planning procedure as you want – for example, if your company has a process database (this is CMMI Level 4-ish, btw), you could try validating the plan against empirical data.

Are you sold on the DSL idea for estimates? If not, here’s another boon: integration. You can integrate Project with other systems to get more value from existing data. For example, if you run Dynamics CRM, you can tweak resource pricing for a particular client in order to put better developers on the features *they* consider important. It all sounds very pompous and BI-ish, but that’s life of a code shop.

### End Users

In most code shops, barring a few exceptions, estimates are done by project managers (PMs). These guys are sometimes techies, sometimes not, so you can't expect them to know programming. But you can certainly expect them to be able to work with a DSL and then press some magic key to generate a project plan or otherwise involve their DSL scribblings in an estimation BI scenario.

### Continuous Process Improvement

At the risk of sounding cheeky, if you are constantly working on your (say) estimation DSL, improving it and tailoring it, it’s an excellent opportunity for improving your business processes. Think about it – as a code shop, you can use idle dev resources to improve the efficiency of your business. Is this great, or what? I think it is, anyway.

## Choosing a Language

With the problem out of the way, let’s think of a solution. You can certainly make a free-form DSL language and write a parser, but it’s kind of tedious. A simpler solution is to use a programming language which looks so English (no cultural bias here – feel free to use Japanese or any other language) that the end user won’t know the difference. Of course, some language syntax *will* creep into the DSL, but its level varies.

Popular languages for DSLs include Boo (which Ayende is trying to make popular), Ruby and F#. Boo is extremely powerful, and for cases where you need metaprogramming support (*not* our scenario), it’s fantastic. Ruby I know next to nothing about, so no comment. Now, F# is a popular language, and a first-class citizen of .NET infrastructure (as of VS2010 especially). So we're going to look at making an infrastructure in which PMs can easily write project estimates.

Let me issue a small disclaimer: being a language geared towards immutability, F# looks a bit weird when used with highly mutable concepts, such as a project which can accumulate tasks or milestones. This weirdness can be easily compensated by writing the DSL data structures in C# and then using them from F#. However, for this example, I'll use F# exclusively.

## First DSL Statement

I'll try to keep this simple. Let’s start by defining a project with a name and start date:

[anexo ausente] Collapse | [Copy Code](http://www.codeproject.com/Articles/39031/Making-DSLs-in-F#)

```
project "Write F# DSL Article" starts_on "16/8/2009"
```

The above is a completely legal F# statement. It’s basically a function call to a function called `project` which takes 3 parameters. The first parameter is a project name – no, you can't avoid the quotes here unless you want to parse stuff yourself. The second parameter is a dummy – a constant whose value is unimportant; its only purpose here is to make the spec readable and BDD-esque. You're welcome to expand the `starts_on` keyword into two separate parts, but I prefer not to overdo it, especially when there’s a risk of keywords creeping in. The third parameter is the project starting date as a string.

Believe it or not, the DSL uses OOP constructs in order to manage the constructed project. For example, we have a `Project` class which is our DSL representation of a project. It’s shown below. Skipping ahead a bit, make sure your types don't collide with other assemblies’ types. After all, Microsoft Project assemblies might just have a `Project` type too.

[anexo ausente] Collapse | [Copy Code](http://www.codeproject.com/Articles/39031/Making-DSLs-in-F#)

```
type Project() =
  [<DefaultValue>] val mutable Name : string
  [<DefaultValue>] val mutable Resources : Resource list
  [<DefaultValue>] val mutable StartDate : DateTime
  [<DefaultValue>] val mutable Groups : Group list
```

I did warn about the strange syntax, did I not? The above is F#’s way of making public fields. You'll notice also that I use `list` types instead of the `System.Collections.Generic` ones. It doesn't really matter what you use for the DSL so long as it works.

Our DSL will support just one project which will be at ‘global scope’, so to speak:

[anexo ausente] Collapse | [Copy Code](http://www.codeproject.com/Articles/39031/Making-DSLs-in-F#)

```
>let mutable my_project = new Project()
```

The naming convention is a bit *ad hoc* here save for the fact that, when we get to the end of the spec, we need a statement to actually do something and `my_project` is a nice identifier name for that action. But now, we can finally show the `project` statement from earlier.

[anexo ausente] Collapse | [Copy Code](http://www.codeproject.com/Articles/39031/Making-DSLs-in-F#)

```
let project name startskey start =
  my_project <- new Project()
  my_project.Name <- name
  my_project.Resources <- []
  my_project.Groups <- []
  my_project.StartDate <- DateTime.Parse(start)
```

There. I have probably revealed 90% of what DSL construction is like. You can close this article and go off exploring right now, since you already know how it all works. In the rest of this article, I'll be showing a few F# implementation details.

## Handling Lists

Work in projects is done by *resources* (not very gratifying, is it?). A resource is a particular person (“John”) with a particular job title (“Junior DBA”) and a particular hourly rate ($65). A project keeps references to resources via a `Resource list` (see, F# is human-readable). Let’s look at the definition of `Resource`:

[anexo ausente] Collapse | [Copy Code](http://www.codeproject.com/Articles/39031/Making-DSLs-in-F#)

```
type Resource() =
  [<DefaultValue>] val mutable Name : string
  [<DefaultValue>] val mutable Position : string
  [<DefaultValue>] val mutable Rate : int
```

I'm abusing F# once again, but at least the structure is easy to work with. Now, a resource definition is also part of our DSL, and might look as follows:

[anexo ausente] Collapse | [Copy Code](http://www.codeproject.com/Articles/39031/Making-DSLs-in-F#)

```
>resource "Dmitri" isa "Project Manager" with_rate 140
```

The above statement employs the same trickery as `project` except that it acts on an already-existing global variable `my_project`:

[anexo ausente] Collapse | [Copy Code](http://www.codeproject.com/Articles/39031/Making-DSLs-in-F#)

```
let resource name isakey position ratekey rate =
  let r = new Resource()
  r.Name <- name
  r.Position <- position
  r.Rate <- rate
  my_project.Resources <- r :: my_project.Resources
```

Resources and all other lists we use end up being listed *in reverse order*. It’s not a problem though – we reverse them when the time comes. If you don't like it, use `List<T>` instead.

## Referencing with Strings

The next concept of our DSL I want to introduct is a *group* of tasks. A group of tasks is typically done by one person to maintain, ahem, cognitive cohesion. We define a group as follows:

[anexo ausente] Collapse | [Copy Code](http://www.codeproject.com/Articles/39031/Making-DSLs-in-F#)

```
>group "Project Coordination" done_by "Dmitri"
```

To put things in context, let’s look at the `Group` class:

[anexo ausente] Collapse | [Copy Code](http://www.codeproject.com/Articles/39031/Making-DSLs-in-F#)

```
type Group() =
  [<DefaultValue>] val mutable Name : string
  [<DefaultValue>] val mutable Person : Resource
  [<DefaultValue>] val mutable Tasks : Task list
```

A group references a particular resource, which our DSL specifies only as a string. Problem? I don't think so:

[anexo ausente] Collapse | [Copy Code](http://www.codeproject.com/Articles/39031/Making-DSLs-in-F#)

```
let group name donebytoken resource =
  let g = new Group()
  g.Name <- name
  g.Person <- my_project.Resources |> List.find(fun f -> f.Name = resource)
  my_project.Groups <- g :: my_project.Groups
```

Notice how, unlike with LINQ, we don't have to call `Single()` after searching for the right resource.

## Greater Fluency

Last but not least, we define tasks. Now, isn't it great when you can say, for example, the following:

[anexo ausente] Collapse | [Copy Code](http://www.codeproject.com/Articles/39031/Making-DSLs-in-F#)

```
task "PayPal Integration" takes 2 weeks
```

In fact, you can. This type of fluency is achieved by judiciously defining timespan constants so that their values are *meaningful*. For example:

[anexo ausente] Collapse | [Copy Code](http://www.codeproject.com/Articles/39031/Making-DSLs-in-F#)

```
let hours = 1let hour = 1let days = 2let day = 2let weeks = 3let week = 3let months = 4let month = 4
```

The values do not matter so long as they are distinct. Now we can define a task…

[anexo ausente] Collapse | [Copy Code](http://www.codeproject.com/Articles/39031/Making-DSLs-in-F#)

```
type Task() =
  [<DefaultValue>] val mutable Name : string
  [<DefaultValue>] val mutable Duration : string
```

… and add it to the project:

[anexo ausente] Collapse | [Copy Code](http://www.codeproject.com/Articles/39031/Making-DSLs-in-F#)

```
let task name takestoken count timeunit =
  let t = new Task()
  t.Name <- name
  let dummy = 1 + count
  match timeunit with
  | 1 -> t.Duration <- String.Format("{0}h", count)
  | 2 -> t.Duration <- String.Format("{0}d", count)
  | 3 -> t.Duration <- String.Format("{0}wk", count)
  | 4 -> t.Duration <- String.Format("{0}mon", count)
  | _ -> raise(ArgumentException("only spans of hour(s), day(s), week(s) and month(s) are supported"))
  let g = List.hd my_project.Groups
  g.Tasks <- t :: g.Tasks
```

Notice that for each timespan, I slightly change the way the duration is phrased so that Project is capable of eating the spec. The dummy expression above tells F# that `count` is an integer – I could have defined it explicitly, of course, but I'm just too lazy. Oh, by the way, notice how easy it is for us to find the *current* (i.e., last) task. Because we're using F#, this task is actually *first* in the list, so we can just call `List.hd`.

## Generating the Project

We've got *everything* and are ready to generate the project. The following (somewhat cheesy) command does it:

[anexo ausente] Collapse | [Copy Code](http://www.codeproject.com/Articles/39031/Making-DSLs-in-F#)

```
prepare my_project
```

Now, I'm about to show you the *whole* `prepare` definition, which uses the Project API to make the, umm, project. Notice how succinct F# is:

[anexo ausente] Collapse | [Copy Code](http://www.codeproject.com/Articles/39031/Making-DSLs-in-F#)

```
let prepare (proj:Project) =
  let app = new ApplicationClass()
  app.Visible <- true
  let p = app.Projects.Add()
  p.Name <- proj.Name
  proj.Resources |> List.iter(fun r ->
    let r' = p.Resources.Add()
    r'.Name <- r.Position // position, not name :)
    let tables = r'.CostRateTables
    let table = tables.[1]
    table.PayRates.[1].StandardRate <- r.Rate
    table.PayRates.[1].OvertimeRate <- (r.Rate + (r.Rate >>> 1)))
  // make root task with project name
  let root = p.Tasks.Add()
  root.Name <- proj.Name
  // add groups
  proj.Groups |> List.rev |> List.iter(fun g -> 
    let t = p.Tasks.Add()
    t.Name <- g.Name
    t.OutlineLevel <- 2s
    // who is responsible for this group?
    t.ResourceNames <- g.Person.Position
    // add tasks
    let tasksInOrder = g.Tasks |> List.rev
    tasksInOrder |> List.iter(fun t' ->
        let t'' = p.Tasks.Add(t'.Name)
        t''.Duration <- t'.Duration
        t''.OutlineLevel <- 3s
        // make task follow previous
        let idx = tasksInOrder |> List.findIndex(fun f -> f.Equals(t'))
        if (idx > 0) then 
          t''.Predecessors <- Convert.ToString(t''.Index - 1)
      )
    )
```

Yep, we finally reverse those backward lists with `List.rev` – probably not the fastest operation in the world, but I don't care. All that matters is that the script runs and gives us the results we want – resource definitions, group names and tasks which are grouped and linked. What more could a PM ask for? (Quite a bit actually, but that’s another story.)

A complete project definition can therefore look like this:

[anexo ausente] Collapse | [Copy Code](http://www.codeproject.com/Articles/39031/Making-DSLs-in-F#)

```
project "F# DSL Article" starts "01/01/2009"
resource "Dmitri" isa "Writer" with_rate 140
resource "Computer" isa "Dumb Machine" with_rate 0
group "DSL Popularization" done_by "Dmitri"
task "Create basic estimation DSL" takes 1 day
task "Write article" takes 1 day
task "Post article and wait for comments" takes 1 week
group "Infrastructure Support" done_by "Computer"
task "Provide VS2010 and MS Project" takes 1 day
task "Download and deploy TypograFix" takes 1 day
task "Sit idly while owner waits for comments" takes 1 week
prepare my_project
```

## Conclusion

This article shows that making a DSL in F# is really simple. Of course, the thing about DSLs is they are *domain-specific*, so for the domain *you* choose you might encounter a lot more challenges. Have fun!
