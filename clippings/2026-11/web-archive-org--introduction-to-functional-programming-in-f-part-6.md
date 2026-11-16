---
url: "https://web.archive.org/web/20201108124458id_/https://www.softwarepark.cc/blog/2019/12/22/introduction-to-functional-programming-in-f-part-6"
captured_at: "2026-11-16T15:51:12+00:00"
title: "Introduction to Functional Programming in F# - Part 6 — Softwarepark"
domain: "web-archive-org"
---

**Introduction**

Welcome to the sixth post in this introductory series on functional programming in F#. In this post we will introduce the basics of reading and parsing external data using sequences and the Seq module and how we can isolate code that talks to external services to make our codebase as testable as possible.

**Setting Up**

Copy the following data into a file. I have created a file called "customers.csv" and have stored it into "D:\\temp".

```
CustomerId|Email|Eligible|Registered|DateRegistered|Discount
John|john@test.com|1|1|2015-01-23|0.1
Mary|mary@test.com|1|1|2018-12-12|0.1
Richard|richard@nottest.com|0|1|2016-03-23|0.0
Sarah||0|0||
```

Now create a console application in a new folder.

```
dotnet new console -lang F#
```

Now we are ready to start.

**Solving the Problem**

We are going to use features of the built-in System.IO classes, so first we need to open the package;

```
open System.IO
```

and then we need a function that takes a path as a string and returns a collection of strings from the file;

```
let readFile path = // string -> seq<string>
    seq { use reader = new StreamReader(File.OpenRead(path))
          while not reader.EndOfStream do
              yield reader.ReadLine() 
    }
```

There are a few new things in this simple function!

seq is called a Sequence Expression. The code inside the curly brackets is creating a sequence of strings. seq creates a sequence of { 1; 2; 3; 4; 5 }.

StreamReader implements the IDisposable interface. F# deals with that by using the 'use' and 'new' keywords.

'yield' adds that item to the sequence.

Now we need to write some code in the main function to call our readFile function and output the data to the Terminal window;

```
@"D:\temp\customers.csv"
|> readFile 
|> Seq.iter (fun x -> printfn "%s" x)
```

You must leave the '0' at the end of the main function.

Seq is the sequence module which has a wide range of functions available, similar to List and Array. Seq.iter will iterate over the sequence and returns unit.

The code in Program.fs should now look like this;

```
open System.IO

let readFile path = // string -> seq<string>
    seq { use reader = new StreamReader(File.OpenRead(path))
          while not reader.EndOfStream do
              yield reader.ReadLine() 
    }

[<EntryPoint>]
let main argv =
    @"D:\temp\customers.csv"
    |> readFile 
    |> Seq.iter (fun x -> printfn "%s" x)
    0
```

Run the code by typing 'dotnet run' in the Terminal.

To handle potential errors from loading a file, we are going to add some error handling to the readFile function;

```
let readFile path = // string -> Result<seq<string>,exn>
    try
        seq { use reader = new StreamReader(File.OpenRead(path))
              while not reader.EndOfStream do
                  yield reader.ReadLine() 
        }
        |> Ok
    with
    | ex -> Error ex
```

To handle the change in the signature of the output from the readFile function, we will introduce a new function;

```
let import path =
    match path |> readFile with
    | Ok data -> data |> Seq.iter (fun x -> printfn "%A" x)
    | Error ex -> printfn "Error: %A" ex.Message
```

and replace the code in the main function with;

```
import @"D:\temp\customers.csv"
```

Run the program to check it still works.

Now we want to create a type to read in the data;

```
type Customer = {
    CustomerId : string
    Email : string
    IsEligible : string
    IsRegistered : string
    DateRegistered : string
    Discount : string
}
```

and create a function that takes a sequence of strings as input and returns a sequence of Customer;

```
let parse (data:string seq) = // seq<string> -> seq<Customer>
    data
    |> Seq.skip 1 // Ignore the header row
    |> Seq.map (fun line -> 
        match line.Split('|') with
        | [| customerId; email; eligible; registered; dateRegistered; discount |] -> 
            Some { 
                CustomerId = customerId
                Email = email
                IsEligible = eligible
                IsRegistered = registered
                DateRegistered = dateRegistered
                Discount = discount
             }
        | _ -> None
    )
    |> Seq.choose id // Ignore None and unwrap Some
```

There are some new features in this function:

'Seq.skip 1' will ignore the first item in the sequence as it is not a Customer.

The Split function creates an array of strings. We then pattern match the array and get the data which we then use to populate a Customer. If you weren't interested in all of the data, you can use '\_' for those parts. We have now met the three primary collection types in F#; List (\[..\]), Seq (seq ) and Array (\[|..|\]).

'Seq.choose id' will ignore any item in the sequence that is None and will unwrap the Some items to return a sequence of Customers.

We also need to add a function to output the sequence of customer to the Terminal window;

```
let output data =
    data 
    |> Seq.iter (fun x -> printfn "%A" x)
```

and add this function to the Ok path in the import function;

```
let import path =
    match path |> readFile with
    | Ok data -> data |> parse |> output
    | Error ex -> printfn "Error: %A" ex.Message
```

The next stage is to extract the code from the map in the parse function to its own function;

```
let parseLine (line:string) : Customer option =
    match line.Split('|') with
    | [| customerId; email; eligible; registered; dateRegistered; discount |] -> 
        Some { 
            CustomerId = customerId
            Email = email
            IsEligible = eligible
            IsRegistered = registered
            DateRegistered = dateRegistered
            Discount = discount
        }
    | _ -> None
```

and modify the parse function to use the parseLine function;

```
let parse (data:string seq) =
    data
    |> Seq.skip 1
    |> Seq.map (fun x -> parseLine x)
    |> Seq.choose id
```

We can simplify this function by removing the lambda;

```
let parse (data:string seq) =
    data
    |> Seq.skip 1
    |> Seq.map parseLine
    |> Seq.choose id
```

Whilst we have improved the code a lot, it is difficult to test without having to load a file. In addition, the signature of the readFile function is 'string -> Result<seq,exn>' which means that it could easily have been a Url to a webservice rather than a path to a file on disk.

To make this testable and extensible, we can use Higher Order Functions and pass a function as a parameter into the import function;

```
let import (fileReader:string -> Result<string seq,exn>) path =
    match path |> fileReader with
    | Ok data -> data |> parse |> output
    | Error ex -> printfn "Error: %A" ex.Message
```

This means that we can now pass any function with this signature into the import function.

This signature is quite simple but they can get quite complex, so we can create a type signature and use that instead;

```
type FileReader = string -> Result<string seq,exn>
```

and replace the function signature in import with it;

```
let import (fileReader:FileReader) path =
    match path |> fileReader with
    | Ok data -> data |> parse |> output
    | Error ex -> printfn "Error: %A" ex.Message
```

We can also use it like an Interface in the readFile function but it does mean modifying our code a little;

```
let readFile : FileReader =
    fun path ->
        try
            seq { use reader = new StreamReader(File.OpenRead(path))
                  while not reader.EndOfStream do
                      yield reader.ReadLine() }
            |> Ok
        with
        | ex -> Error ex
```

We need to make a small change to our call in main to tell it to use the readFile function;

```
import readFile @"D:\temp\customers.csv"
```

If we use import with readFile regularly, we can use partial application to create a new function that does that for us;

```
let importWithFileReader = import readFile
```

To use it we would simply call;

```
importWithFileReader @"D:\temp\customers.csv"
```

The payoff for the work we have done using Higher Order Functions and Type Signatures is that we can easily pass in a fake function for testing like the following;

```
let fakeFileReader : FileReader =
    fun _ ->
        seq {
            "CustomerId|Email|Eligible|Registered|DateRegistered|Discount"
            "John|john@test.com|1|1|2015-01-23|0.1"
            "Mary|mary@test.com|1|1|2018-12-12|0.1"
            "Richard|richard@nottest.com|0|1|2016-03-23|0.0"
            "Sarah||0|0||"
        }
        |> Ok

import fakeFileReader "_"
```

or any other function that satisfies the Type Signature.

**Final Code**

What we have ended up with is the following;

```
open System.IO

type Customer = {
    CustomerId : string
    Email : string
    IsEligible : string
    IsRegistered : string
    DateRegistered : string
    Discount : string
}

type FileReader = string -> Result<string seq,exn>

let readFile : FileReader =
    fun path ->
        try
            seq { use reader = new StreamReader(File.OpenRead(path))
                  while not reader.EndOfStream do
                      yield reader.ReadLine() }
            |> Ok
        with
        | ex -> Error ex

let parseLine (line:string) : Customer option =
    match line.Split('|') with
    | [| customerId; email; eligible; registered; dateRegistered; discount |] -> 
        Some { 
            CustomerId = customerId
            Email = email
            IsEligible = eligible
            IsRegistered = registered
            DateRegistered = dateRegistered
            Discount = discount
        }
    | _ -> None

let parse (data:string seq) =
    data
    |> Seq.skip 1
    |> Seq.map parseLine
    |> Seq.choose id

let output data =
    data 
    |> Seq.iter (fun x -> printfn "%A" x)

let import (fileReader:FileReader) path =
    match path |> fileReader with
    | Ok data -> data |> parse |> output
    | Error ex -> printfn "Error: %A" ex.Message

[<EntryPoint>]
let main argv =
    import readFile @"D:\temp\customers.csv"
    0
```

In a future post, we will extend this code by adding data validation.

**Conclusion**

In this post we have looked at how we can import data using some of the most useful functions on the Seq module, Sequence Expressions and Type Signatures.

In the next post we will look at another exciting F# feature - Active Patterns.

If you have any comments on this series of posts or suggestions for new ones, send me a tweet (@ijrussell) and let me know.

[Part 5](https://www.softwarepark.cc/blog/2019/10/11/introduction-to-functional-programming-in-f-part-5) [Table of Contents](https://www.softwarepark.cc/blog/2020/8/9/introduction-to-functional-programming-in-f-table-of-contents) [Part 7](https://www.softwarepark.cc/blog/2019/12/22/introduction-to-functional-programming-in-f-part-7)
