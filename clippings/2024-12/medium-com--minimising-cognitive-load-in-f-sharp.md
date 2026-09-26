---
url: "https://medium.com/@michaeljwinch/minimising-cognitive-load-in-f-2d4baa94b740"
captured_at: "2024-12-25T19:53:39+00:00"
title: "Minimising cognitive load in F# - Michael Winch - Medium"
domain: "medium-com"
---

## Steps you can take when your brain don’t work too good

[

![Michael Winch](https://miro.medium.com/v2/resize:fill:88:88/1*fCbZlZ_QHpmYJE0gfUz3TA.jpeg)

](https://medium.com/@michaeljwinch?source=post_page---byline--2d4baa94b740--------------------------------)

5 min read

Dec 8, 2024

\--

As humans, there are many things we’re great at. Rationalising buying that game on your wishlist. Finding any excuse not to finish your blog post. Letting that pan soak. One thing we’re not so good at is holding lots of information in our heads at once.

[Cognitive load](https://github.com/zakirullin/cognitive-load) is a big problem when understanding code, especially code you didn’t write. The best thing you can do to combat it is to simplify your code, but what does that look like in F#?

Photo by [Mathew Schwartz](https://unsplash.com/@cadop?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

## Move implementation detail into its own function

If a function needs to do multiple things like filter a list of items by some predicate then reduce them by another predicate, make those predicates their own functions and just compose them.

It’s a lot easier to understand

let income =  
    transactions  
    |> List.filter Transaction.isCredit  
    |> List.map \_.Amount  
    |> List.reduce Amount.sum

than it is to understand

let income =  
    transactions  
    |> List.filter (fun x -> x.Amount.Value > 0m)  
    |> List.map \_.Amount  
    |> List.reduce (fun acc x -> acc + x.Value)

and you don’t need to know much about the types to know whats happening.

## Use modules for code separation

Let’s have another look at that last example.

|> List.filter Transaction.isCredit

Part of what made it easier to understand was the usage of a `Transaction` module. By putting functions that operate on a domain type in a module named after it, you inherently know what its final input is and therefore how you can compose it.

It also makes it a lot easier to find, so you don’t have to go looking around to see if there’s an existing function as you can just type `Transaction.` and let autocomplete do the rest for you.

This feels very natural to use as it’s how all of the list/option/result/anything functions are organised.

## Use custom operators sparingly

If used locally or for a commonly known purpose it’s fine, but otherwise it makes the code harder to understand.

// This is fine  
let toDomain dto =  
    let (!!) str = if String.isNullOrEmpty str then None else Some str  
    { Id = dto.Id  
      Name = !!dto.Name  
      Description = !!dto.Description }

// This is a tad cruel  
let toDomain dto =  
    { Id = dto.Id  
      Name = !!dto.Name  
      Description = !!dto.Description }

## Use active patterns to simplify match statements

Match statements often lie at the heart of the complexity of a feature. Therefore understanding them is key to understanding the functionality as a whole.

The simplest match statements to understand aren’t those with few cases, they are ones where the matched case is easy to convert from code to business meaning. This is dependent on your business scenario and isn’t often avoidable.

What you can do though, is to use active patterns to simplify the match statements.

// Before  
let notify (lastNotified: DateTime option) (today: DateOnly) =  
    match lastNotified with  
    | None -> sendNotification ()  
    | Some lastNotified  
        when DateOnly.FromDateTime lastNotified < today.AddDays -1 ->  
          sendNotification ()  
    | Some \_ -> ()

// After  
let notify (lastNotified: DateTime option) (today: DateOnly) =  
    match lastNotified with  
    | NeverNotified  
    | NotifiedBeforeYesterday -> sendNotification ()  
    | NotifiedTodayOrYesterday -> ()

The resulting code still does all the same work, but as a reader the first thing you care about is ‘what does this do?’, not ‘how does it do it?’ and this removes the need to understand the implementation detail.

## Name properly!!!

This one isn’t F# specific but I have to stress this as it’s so easy to get wrong — and I still do regularly.

A well named function/variable/type/anything makes your code so much easier to understand. It doesn’t matter if the variable name is long, it’s much better to have a long variable name that’s clear than a short one that’s ambiguous.

If you’re unsure about how to name something there’s no shame in asking a colleague.

## Create more types (or less?)

It can be tricky to find the right balance between reusing types and creating types for an overly specialised purpose. Scott Wlaschin‘s ‘_Domain Modelling Made Functional_’ rightly demonstrates how types should be used to model the domain, but it can be easy to fall into the trap of over-modelling. Sometimes a value can just be an int, not everything needs to be a DU.

Consider what matters most for your domain and where the risks lie.

## Use computation expressions

CEs can simplify code by removing the necessity for maps and binds dotted around.

I like to use [FsToolkit.ErrorHandling](https://github.com/demystifyfp/FsToolkit.ErrorHandling) and [AsyncWriterResult](https://github.com/totallymoney/AsyncWriterResult) but you can make your own!

// Before  
let accounts = listAccounts customerId  
let transactions = listTransactions customerId

AsyncResult.zip accounts transactions  
|> Async.map (Result.bind (fun (acts, txs) -> calculateBalance acts txs))

//After  
asyncResult {  
    let! accounts = listAccounts customerId  
    and! transactions = listTransactions customerId

    return! calculateBalance accounts transactions  
}

## Point-free? Try point-fewer!

Point-free programming can be very succinct (and better yet, satisfying), but it can sometimes make it harder to understand the code.

Take this example:

// Before  
|> Map.map (fun \_ -> List.map \_.Amount >> Amount.sum)

// After  
|> Map.map (fun \_ transactions -> transactions |> List.map \_.Amount |> Amount.sum)

We’re using composed functions to sum some amounts. In the real world we have multiple types with an `Amount` property, so it’s unclear what it’s operating on. By writing it out in full, we take the guessing out of the equation.

let concatKebab = connect "-"  
// val concatKebab: (string -> string -> string)

let concatKebab2 prefix suffix = connect "-" prefix suffix  
// val concatKebab2: prefix: string -> suffix: string -> string

Partial application has a similar issue. Here we have a function partially applying the first argument, giving us a type hint `string -> string -> string` — which isn’t wrong, but also isn’t very helpful! Simply writing in the variables explicitly makes it easier to find out exactly what it’s doing.

So much of what we do becomes second nature so it’s good to take a closer look at our habits from time to time. That’s enough blog post for today, my brain is warm.
