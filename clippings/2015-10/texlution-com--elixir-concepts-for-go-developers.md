---
url: "https://texlution.com/post/elixir-concepts-for-golang-developers/"
captured_at: "2015-10-19T10:00:13-03:00"
title: "Elixir concepts for Go developers"
domain: "texlution-com"
---

# Elixir concepts for Go developers

**Disclaimer:**
This is not a getting started guide. I've only played with the language and I'm by no means an expert, so take what I write with a grain of salt. My goal is to condense the highlights of a few hours in research into something you can consume in a few minutes to help you decide if Elixir could be of any interest to you.

### What is Elixir

[Elixir](http://elixir-lang.org/) is an emerging new language that runs in the BEAM, the Erlang virtual machine. It has complete Erlang interoperability and shares the same building blocks, but it does it with a Ruby-like syntax and tons of syntactic sugar. It was created by [José Valim](https://twitter.com/josevalim), core Rails contributor. And it is attracting lots of both rubyists and erlangers(?) in its attempt to combine [the power of Erlang with the joy of Ruby](https://www.youtube.com/watch?v=lww1aZ-ldz0).

### Soft immutability

Elixir tries to be a proper functional language, and in proper functional languages data is immutable. Once you have set a variable you can not change it. This has great benefits but can be tricky for people with imperative mindsets like mine. Usually you are supposed to work around that with recursion and function calls, but Elixir brings some middle ground offering a form of soft immutability in which you can reuse variable names.

```
Interactive Elixir  
iex a  

iex a  "what?"
"what?"
```

That looks like mutation, but it’s not. It’s actually syntactic sugar for `a1=1` and `a2="what?"`. Anything that gets passed a reference to the first `a` will keep getting `1`. As you can also see Elixir is dynamically typed and has a REPL, although the language itself is compiled.

### Pattern matching

Elixir like Erlang and many other functional languages has [pattern matching](https://en.wikipedia.org/wiki/Pattern_matching). This is a killer feature that radically changes the way your code looks. In Elixir, the `=` operator is actually used for “matching” what it has in both sides.

```
Interactive Elixir  
iex a  

iex b  

iex a  c   b "I am a teapot"
  "I am a teapot"
iex c
"I am a teapot"
iex a  c   b "I am a teapot" # try to match b = 7
 MatchError no match of right hand side value:   "I am a teapot"
iex a  c   b "I am a teapot" # rebind a = 2
  "I am a teapot"
```

The program will try to match a sequence of “patterns” until one *clicks*, binding variables along the way. This reduces massively the need for if/else. Think of it as **switch statements on steroids**. But it goes beyond that, you can (and wil) use it do declare different behavior in functions depending on which pattern signature the input parameters match.

```
is_three  
            -> IOputs "yes, this is the number 3"
  num        -> IOputs "no, this is the number "
  num more  -> IOputs "no, those are 2 numbers,  and "

iex is_three
yes this is the number 

iex is_three
no this is the number 

iex is_three 
no those are  numbers
```

### Atoms

The equivalent of an iota-indexed constant in Go, and what other programming languages call symbol. They are used all over the place to label what is what and patten match against them.

```
iex imanatom
imanatom
iex imanatom a  imanatom 
imanatom 
iex imanatom a  anotheratom 
 MatchError no match of right hand side value anotheratom 

iex IOputs "hello world"
hello world
ok
```

Many functions will return the atom `:ok` along with results to indicate success, or `:error` with a message otherwise, so you can pattern match the results to decide what do to in different scenarios.

### Processes vs Goroutines

Processes in Elixir/Erlang are the equivalent of Goroutines in Go, lightweight threads of execution independent from the system’s thread. But Elixir implements Erlang’s [actor model](https://en.wikipedia.org/wiki/Actor_model) in which **the lightweight threads are the main entity which is directly addressable**. When you spawn an Elixir process you get a PID that you can use to send messages to that process, the process can pattern match the messages received to decide what it is and what to do.

This is Elixir’s actor-based hello world:

```
ex parent  self
#PID<0.57.0>
iex spawn_link ->  send parent  "hello world" 
#PID<0.60.0>
iex receive   contents -> IOputs contents 
hello world
```

The channel of communication is completely transparent to the processes, and in fact multiple VMs can be connected in a mesh network so you can send messages transparently to other processes in any other computer in your network. Multiple processes can be bundled in *process groups* allowing you to send messages to the whole group in order to distribute the load. Since the network is transparent to the processes, there is no debate microservices vs monolith, you can switch between the 2 models with minimal effort.

This actor model contrasts with Go’s [CSP](https://en.wikipedia.org/wiki/Communicating_sequential_processes) model, in which the communication channel is the main addressable entity and the goroutines are anonymous and can not be addressed directly.

### Supervisors

Supervisors are processes that watch over *your* processes so they get restarted if the crash for some reason. They also allow you to start and stop inflight parts of your program. To get the idea, if we had a function that counted numbers and we wanted to supervise it, a dummy Go supervisor implementation would be something like:

```
package main

import 
	"fmt"
	"time"

  
	// Instead of: go count(3)
	 supervisorcount 

	select 

 countto  
	 i   i <= to i 
		fmtPrintf"i=%d\n" i
		timeSleeptimeSecond
	

	panic"pretend that something broke"

 supervisorfn  args  
	 
		 
			defer  
				 err  recover err   
					fmtPrintln"panic recovered"
				
			
			args
		
		fmtPrintln"restarting process"
		timeSleeptimeSecond
	
```

This is of course an extreme oversimplification. Elixir/Erlang supervisors are built-in, much more sophisticated, allowing for different restart policies, etc. They are usually combined in “supervision trees”, so your applications keeps several levels of resiliency.

### Structs and Protocols

Structs in Elixir look similar to Structs in Go, although deep down are just syntactic sugar around maps. They give Elixir a certain object-oriented flavor, while keeping the functional spirit. You can pattern match struct properties against each other like you would do with map values.

Protocols are similar to Go interfaces, and protocol implementations the struct methods. Elixir, like Go, seems to follow the [composition over inheritance](https://en.wikipedia.org/wiki/Composition_over_inheritance) principle.

### The pipe |> operator

Oh, my! While Go holds the spirit of the unix pipes Elixir literally has pipes in the language. And it makes such a big difference in readability, specially in a functional language. All the `|>` operator does is take the value in the left and use it as the first argument of the function in the right.

So something like this:

```
toStringmultiplyByfetchANumber
```

Can be written like:

```
fetchANumber |> multiplyBy |> toString
```

Bringing back the order of execution to the reading direction. This is again just syntactic sugar. Actually, [it’s a macro](https://github.com/elixir-lang/elixir/blob/v1.1.1/lib/elixir/lib/kernel.ex#L2563) that you could have created yourself.

### Macros

Macros are syntactic sugar à la carte. The macro system goes beyond simple templates, Elixir programs are internally represented as lisp-esque three-element tuples {function, metadata, arguments}, and you can have access to your own AST at compile time.

```
iex quote  sum  
    
iex quote    
: context: Elixir import: Kernel  
iex quote  IOputs "hello"
:  :__aliases__ alias: false  :puts  "hello"
```

This makes Elixir a great language for meta programming and [DSLs](http://elixir-lang.org/getting-started/meta/domain-specific-languages.html). You can extend the language with whatever you think is missing. While you are encouraged to not abuse macros and only use them to attack new problem domains, the so-called **“What if I could just..” Driven Development** (WIICJDD) is just too tempting.

### Standard library and the OTP

Elixir’s has a nice and clean standard library, in contrast to Erlang’s standard library which is vast but PHP-esque in its inconsistency. But the crown jewel is the Open Telecommunications Platform, a library made for the distributed systems of the telco industry.

The OTP is a collection of very well thought out building blocks for resilient distributed systems. It is to an extent what made Erlang so special. In it you can find the aforementioned supervisors, release management, monitoring, generic server implementations, a distributed key-value store, and even a distributed relational database built on top of it.

### Phoenix

[Phoenix](http://www.phoenixframework.org/) was created by [Chris McCord](https://twitter.com/chris_mccord), another rubyist, and it’s a high productivity web framework that aims to be the Rails of Elixir. It’s a full featured framework with [Plug](http://www.phoenixframework.org/docs/understanding-plug), an specification for middleware interfaces, at the core of everything. Accompanied by [Ecto](http://www.phoenixframework.org/docs/ecto-models), an ORM-ish database access layer. It tries to mimic Rails’ productivity focus, but it’s not a Rails clone, leveraging instead Elixir/OTP’s features. It tries to go even beyond the web with the use of [Phoenix Channels](http://www.phoenixframework.org/docs/channels), a built-in socket library with a plugable transport layer that already has JavaScript, Swift, ObjC, C# and Java integrations.

As I mentioned before, BEAM is the VM where Elixir runs. Don’t be scared by the words *virtual machine*, **it’s very different from the JVM**. It has a very low memory footprint, it doesn’t have noticeable garbage collection pauses and it’s designed relatively performant. It shines when it comes to slow latency, and sits somewhere half way between Java/Go and Python/Ruby when it comes to raw computing performance. It will, for example, happily run in your raspberry pi. If deployment worries you, don’t be. The OTP provides “release artifacts”, self-contained packages with all dependencies includes that you just need to scp to the server and run like you would with a Go binary.

### Final thoughts

Personally I find Elixir very interesting. For someone like me who has failed to grok anything more functional than JavaScript, it looks like a great opportunity to study that paradigm while still feeling at home. Pattern matching and the pipe operator make for declarative code both easy to read and write. It is also an opportunity to study the OTP and the lessons learned after many years of building resilient distributed systems.

I can see it taking part of the market of the many Ruby shops jumping from Ruby to Go just for the performance boost. That being said, I don’t see myself using this in a team building a big application, at least not without a pre-commit hook forbidding macro definitions. I wrote before [about Go](https://texlution.com/post/why-go-is-doomed-to-succeed/) and how it’s a good thing that it doesn’t let some people *express themselves*. Elixir and WIICJDD represents the other end of the spectrum, with its macro system being the ultimate freedom of speech tool.

I wanted to come up with a witty metaphor about José Valim being Willy Wonka covering Erlang with enough sugar to make it look tasty and open everyone’s appetite, macros being the chocolate factory and me wondering how many developers will fall into the chocolate river despite the warnings. I could not articulate anything decent but you can see where I’m going. Perhaps I’m wrong though, the language is too new to tell.

I think to understand Elixir’s design goals you need to look at the background of the people behind it and what problems they faced in their careers. AFAIK neither Valim nor McCord were Erlang developers trying to create a better Erlang, they are both rubyists working in web development agencies [[see notes](https://texlution.com/post/elixir-concepts-for-golang-developers/#note-1)], and what they try to achieve is to have a better Ruby without its notorious scalability shortcomings by piggybacking on Erlang’s distributed goodies [[see notes](https://texlution.com/post/elixir-concepts-for-golang-developers/#note-2)]. Bringing with them a few erlangers along the way. While the language itself aims to a broad scope, I think is important to keep that in perspective.

If you’re sold and actually want learn the language, aside from the [official getting started guide](http://elixir-lang.org/getting-started/introduction.html) I can fully recommend this 3 hour long workshop by Chris McCord: [All Aboard The Elixir Express!](https://www.youtube.com/watch?v=5kYmOyJjGDM) and [its repo](https://github.com/chrismccord/elixir_express).

##### Note-1: *Oct 17, 2015*

It has been pointed out to me that [Plataformatec](http://plataformatec.com.br/), José Valim’s employer and the company backing Elixir’s development, does much more than web development and their business covers backend development, SOA, ETLs, etc.

##### Note-2: *Oct 17, 2015*

My comment about the authors trying to make Elixir a better Ruby is just my personal impression. This is what Valim has to say about about Elixir being a better Ruby:

> I wouldn’t classify Elixir as a better Ruby. Sure, Ruby was my main language before Elixir, but part of my work/research on creating Elixir was exactly to broaden this experience as much as possible and get some mileage on other ecosystems so I didn’t bring a biased view to Elixir. It is not (a better) Ruby, it is not (a better) Erlang, it is its own language.

Posted on Oct 16, 2015
**Tags**  
[ [elixir](https://texlution.com/tags/elixir) ] [ [golang](https://texlution.com/tags/golang) ] [ [dev](https://texlution.com/tags/dev) ]
