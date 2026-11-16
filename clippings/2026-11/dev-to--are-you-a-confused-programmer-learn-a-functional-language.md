---
url: "https://dev.to/pieohpah/are-you-a-confused-programmer-learn-a-functional-language-23f5"
captured_at: "2026-11-16T19:30:04+00:00"
title: "Are You a Confused Programmer? Learn a Functional Language"
domain: "dev-to"
---

[![Alt Text](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fry6vbbq24olhcftofdpv.jpg)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fry6vbbq24olhcftofdpv.jpg)

Full disclosure: I'm an easily confused programmer. My mind does not work like a whiteboard genius. I was born an artist, best at scribbling than anything else. I taught myself to become a programmer in a [visual language](https://processing.org/) because I was partial to the graphics it created and the clacking of the keyboard. I was more an artist and a writer than a programmer. I get confused easily when I read complex code, so I almost always prefer reading human-friendly documentation and comments over reading source code when possible.

I spent the last few years since [Recurse Center](https://medium.com/@jochasinga/mile-2-at-recurse-center-831ab9c276b2) on a programmer's sabbatical in which I wander about trying out any interesting languages I could get my hands on. It's a personal journey to find my _Thor's Hammer_. Some I stuck to for quite a while, the other I ditched almost right after I dipped in. Because each language is designed differently for a distinct way of thinking, I know I have to keep looking for the tool that suits me best.

Over the years, even before the search, I've worked with C++, Java, Python, and Go. Of all these, Go suits me best and empowers me with the fastest, most natural way to work. I was at my peak that I wrote my [first serious open-source library](https://github.com/reactivex/rxgo) in just over a month. However, I've soon realized that it was still lacking for me (I continued to use Go because of its tremendous productivity boost), so when I was accepted into Recurse Center, I decided to dabble into the uncharted territory of functional programming. I first started off with Lisp and Clojure, then went on to learn Ocaml and Haskell, which were daunting but very refreshing. Before I could get far, I landed a job in Silicon Valley where I had to uproot and move to the other coast to write code in JavaScript and Python for the next 3 years.

It took me years to realize that as a confused programmer, I was not an outlier. Most of the programmers out there are. Let's admit it, most of us aren't born wired to program, and that should be okay because programming is a learning journey, not an acquired gift. During my years as an engineer, I had created countless bugs in my JavaScript and Python code (more so in JavaScript) because of the fast-paced nature, lack of mentorship, best practices, and emphasis on unit testing of the company I worked for, but mainly because I was confused. I tended to abstract things when it was not necessary because abstractions made me less confused when I think about my code. It was stressful when I had a deadline to meet and I was reduced to a coding version of dice-rolling--trying out code blindly and repeatedly run it until it works. Because Python and JavaScript permitted me to run code even when it's unlikely to be correct, the "ship it" startup mentality became "f\*\*\* it, let's commit" (engineers were even encouraged to push code and fix it as it breaks in front of the users in a move-fast-and-break-things style I guess).

Fast-forward to now, I'm a sole founder building my own product and running my own company at the same time. It is both relaxing and nerve-racking. It's relaxing because now I don't have to follow the 9-to-5 rule of someone else, commute when I don't have to (this is also true for many in the face of COVID-19 lockdown), and learn whatever I want to.

As I'm building the core product, a [video checkout platform](https://referkit.io/) in Go and JavaScript, I'm also setting aside 10% of my time learning new languages like Crystal, Rust, and Haskell. I've more than once toyed with all these, but I never had the time (or the experience) to make them stick.

I dropped Crystal almost right away because of its Ruby-like syntax (it's also why I couldn't pick up Elixir, despite myself being productive in Erlang). I liked Rust, but I knew it would get in the way of me being productive long before I could get any ROI out of it. Then Haskell clicked. It was a mystique for me years ago when I first try to learn it, but years of programming in Ocaml, Erlang, and Lisp had built my skill up to the point that I'm beginning to enjoy it.

Functional languages (more so Haskell) have been infamously marked as only great for academicians and academic projects, like writing compilers. They have earned a bad name of being too "up there" to grok. Again, the human nature of evangelizing their own likings and throwing their pet-peeves under the bus has been at play. Most who don't grok functional programming are loud, and just like any negative news, they spread faster.

In my opinion, imperative and object-oriented languages like Ruby, Python, Java, and Go are confusing to the eyes and mind of an easily confused programmer like me. They are so confusing to me I'd normally need help from a serious intelligent IDE to be productive. For instance, in my Go codebase, I need to navigate everywhere to find variable and object references. It feels like a long film series with lots of episodes that once you pause and come back you'll need a recap to follow.

In functional programming, every bit of code is self-contained. It might be harder to understand what a certain expression is doing due to its high-level abstraction, but once it's understood it's final. There is very little magic in a functional language to confuse me, and with most state immutable I don't feel like creating new nuts and bolts just to make sure something persists.

For example, if there is only one feature of functional programming I can choose for all languages to have, it is pattern-matching. It gives programmers visuals of the data they are working with.  

```

{- 
 - `h:t` reads `h` cons `t`
 - which means it is a list 
 - of at least an element
 - in front and the rest.
 -}

-- Get the first element in the list.
firstElement (h:t) = Just h
firstElement []    = Nothing


-- Sum all elements in the list.
sumList (h:t) = h + sumList t
sumList []    = 0

```

Enter fullscreen mode Exit fullscreen mode

In Go, my most productive language so far, the equivalent of would be:  

```

// Get the first element in the list.
func firstElement(list []interface{}) interface{} {
    if len(list) == 0 {
        return nil
    }

    return list[0]
}

// Sum all int elements in the list.
func sumListOfInt(nums []int) int {
    sum := 0
    for _, num := range nums {
        sum += num
    }

        return sum
}

```

Enter fullscreen mode Exit fullscreen mode

The Go version is way more involved, especially when I'm the one reading.

The use of `interface{}` type in Go, as well as the deliberate `sumListOfInt` example function, should be noted here. It shows the weakness that comes with Go simplistic design compared to the sophisticate type system of Haskell, which I won't talk about here because it's off-topic.

I have no intention to start another flame war, hence I'm only comparing Haskell to the language I'm actively using and have a strong stake in. All I'm saying is contrary to the belief, functional programming is actually easier for an average programmer to reason with. It reads closer to English instruction as it doesn't require the programmer to be the register for the computer. To make this distinction super clear, take a look at a real-world task and how one might complete it in two different ways:

**Get to the grocery store and buy pasta, tomato pesto, and sausage.**

#### [](#imperative)Imperative

> From where you are, walk 20 yards until you see a junction, take a right and continue for another 0.5 miles. When you see a school to your right, continue for 10 yards and take the first crossing to the opposite side of the street. Walk another 2 blocks to the store.
> 
> When you're in the store, find pasta at the end of aisle #3, tomato pesto in aisle #4 at the middle, and head over the refrigerator to get the sausage.
> 
> ...

#### [](#functional)Functional

> Walk until you see a junction, take a right and walk until you see a school to the right, cross the street and continue until you see the store.
> 
> For all the aisles, get only the pasta and sauce, then go to the refrigerator to get the sausage.
> 
> ...

Functional programming helps programmers avoid being too specific and focus on the high-level instructions (the WHAT instead of HOW), because the specificities are what humans are generally bad at (don't believe me? Can you recall how far you first had to walk before hitting the junction without going back to the grocery store simulation?)

If you are someone like me who gets confused when facing a big pile of code, try learning a functional language like Haskell. It might be a perfect map to your mental model.

* * *

If you'd like to try reading my thoughts on non-programming topics, you can [subscribe to BETA School, my new blog](https://joechasinga.substack.com/).

[![Joe Chasinga Newsletter BETA School](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fnhx7l8n1ufgeoqlc3pc7.png)](https://joechasinga.substack.com/)
