---
url: "https://itnext.io/10-refactorings-to-boost-your-clean-code-skills-3a1e142d63f3"
captured_at: "2023-01-02T23:45:40+00:00"
title: "10 Refactorings to Boost your Clean Code Skills - ITNEXT"
domain: "itnext-io"
---

I love refactoring. I love the process of cleaning the code bit by bit and eventually reaching a state that it’s easier for everyone who needs to read it later. Refactoring is all about taking small steps, and only with these small steps will something big emerge.

_\[Update 11.Nov.2022\] Now that the whole series is done, I’ve created_ [_a book for it_](https://leanpub.com/react-clean-code) _on leanpub. You can get a copy with_ [_this link for 30% off_](https://leanpub.com/react-clean-code/c/mYXp686cMFw1)_._

10 Refactorings

> _There are two ways of constructing a software design: One way is to make it so simple that there are obviously no deficiencies, and the other way is to make it so complicated that there are no obvious deficiencies._
> 
> C.A.R. Hoare

I have seen this happen to me so many times. Initially, the code was complicated, and I couldn’t see many potential improvements. But once I move the bits around, extract variables (or maybe later on inline it back), rename functions or change their signatures, and so on. Slowly, I may know how to make it with better design patterns or so.

So bad code is hard to understand. It uses different levels of abstraction in the same function and makes the reader have to switch contexts. We all know how good code looks, just as we know how bad code looks, but the problem is: how can we start with the bad code (by that, I mean the codebase you’re working on now) to something better?

To me, the answer is pretty clear: take some time to master these fundamental small refactorings and don’t mislead by their name or efforts. I know most of them are pretty straightforward and almost self-explaining, and it doesn’t look like a big deal. But once you mastered them and put them in your daily toolbox, you’ll find the power in them.

Video version of the article

## My top 10 refactorings

Most developers may have their own top 10, and here is the top 10 off my list of refactoring. They fit into two main categories: extract and move. An extraction can be used on variables, functions and types while moving I mean cross multiple files (like split module into other files or inline back).

## 1\. Extract Variable

Whenever you spot some expression that is either too long or needs a **concept** to hold, you need a variable. I’m not treating variable, field and constant as different refactorings in JavaScript or TypeScript normally; the only difference would be the scope of where to put them.

Extracting a variable

For the code snippet below, the empty string can be extracted as a variable named `separator` as that is what exactly it does. Also, the constant `13` can be extracted into `shift` or `offset` to indicate its meaning.

So nothing fancy. Actually, one important aspect of clean code is it should not raise any surprise to their reader. It should be plain and straightforward.

## 2\. Extract function

Functions are the most important building block in many programming languages, and also it’s a perfect place to put your business logic and expressions in. If you don’t pay close attention, it can easily go oversize or have too many things inside.

Although there is no such law for how many lines of code for the function body, I tend to make it small. If it goes too long, I extract sub-function from some statements to make them readable and easy to modify. _And the key here is how you would name your extracted functions_.

For example, the anonymous function inside the map can be extracted into a separate function, which in turn will be much easier to read and test (or be reused in other places).

Extract function

## 3\. Extract Parameter (Change Function Signature)

This happens pretty often during a big refactoring inside a function. When you need an internal state to be passed in from the outside world, and you don’t want to use a global constant at that point, you can extract a parameter first, and then in calling place pass in a variable (could be a global constant).

Extract Parameter

## 4\. Extract Type Definition

As the props list grows, it becomes difficult to read (and also it typically means your component is either doing too much or just drilling props to its children, which should be avoided by some further refactorings).

The fix is relatively easy. You extract the type as a type definition in TypeScript so that it can also be shared in other places (in tests or other modules, for example). I prefer to extract it and place it just before the location uses it. And when necessary I’ll move it to a `types.ts` file in the root level of the module.

Introduce a new type definition

## 5\. Slide Statements

Perhaps the simplest refactoring you could find, but sometimes it makes a huge difference. If you imagine source code in a file like arranging things on your desk or ordering books on your bookshelf.

Just thinking that _Philosopher’s Stone_ is between _UNIX Network Programming_ and _TCP/IP Guide_ on your shelf, what would you do? Yes, slide the _Philosopher’s Stone_ into its own section. We see that in the code all the time as well, so Slide Statements is a great technique that can make the code read more smoothly and more coherent.

Slide statements up and down

Furthermore, once you slide one or a few statements into a group, it is easier for you to extract another function with these blocks.

## 6\. Change Function Declaration

When a new behaviour is added, or existing behaviour is changed, we’ll need to update the function name to ensure the function name still reflects what it does.

It’s a frustrating experience to see a function called `formatDonationLabel`, but inside it does a few more things. Change Function Declaration does exactly that, and it will update all the references like in tests or other modules (event comments and documents).

Change function declaration

A better function name can save tons of time when debugging. Actually, the most important part of a function is that it encapsulates the **HOW** but represents only the **WHAT** — so that you don’t need to dive deep to figure out when you’re debugging the upper layer.

## 7\. Change Variable

The same thing applies to variables as well. There are many times I couldn’t think of a good name, so I would use a pretty general one, like `x` or `segment` as a placeholder, and once I made the change and got a better idea of what the variable was holding, I would change the variable name.

Change variable

## 8\. Move the Fields / Constants

Often when you slide statements up to the higher scope or extract a few utility functions, you will soon realise it may be good to move them into a place so other modules can use too. Also, I found even it’s not that commonly reusable, moving them to a separate file can make the current file short and concise, thus easier to read and understand.

Move fields / constants to another file

## 9\. Inline variable

This is definitely an awesome feature, and it’s the reverse action of extracting. It helps when you change your mind, and there is always a plan B for it — do the opposite.

Inline function / variable

In other cases, inline is a great option when you remove all the duplications, and there isn’t too much left for having a variable to hold a one-off expression.

## 10\. Change Signature

And then it comes to our last but not least one Change Signature. It’s actually a combination of several cases: change parameter order, add/remove parameters or change their types.

Change function signature

As it’ll update all the calling places, it’s safe in most cases if you’re programming with static-typed language.

## Bonus 1: ⌘ + T

When you have just started your refactoring journey, you may not know what refactorings are available for your case. Ask the IDE.

Command T

## Bonus 2: ⌘ + ⇧ + A

If you’re not sure what actions are available, just press `⌘ + ⇧ + A` and then you can search for a command to use. For example, I want to extract a component from JSX, but not sure what the shortcut is, so I `⌘ + ⇧ + A` first and then type `extract component` if there is a related command. I can then apply it to the code under the caret.

## Summary

I listed the 10 most commonly used Refactorings you should master (better to remember all these few shortcuts for them too). All for restructuring or redesigning the more complicated code is based on these small, trivial refactorings. Most of the time, after these tiny refactorings, you’ll notice something bigger that couldn’t be seen back then.

I’ve also created [a free 22 pages book](https://icodeit.ck.page/10-refactorings) for this, and you can also download [the PDF](https://icodeit.ck.page/10-refactorings).
