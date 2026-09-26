---
url: "http://www.andreavallotti.tech/en/2017/09/there-and-back-again/"
captured_at: "2026-09-27T00:41:02+01:00"
title: "There and Back Again"
domain: "andreavallotti-tech"
---

For those who loves Tolkien, the title could seem uppish. After all, I traveled 7.600 km, much more than Bilbo and fellowship, I met people I could hardly understand, and I talked to a dragon… Ok, the latter is not true, but let me believe so 😃

Jokes aside, I spent the first six months of this year in Indianapolis, USA. In this period, I had the chance to appreciate how lively Indiana’s tech community is. I attended two conferences, [Indy.Code](https://indycode.amegala.com/) and [AgileIndy conference](http://agileindy.org/conference/), and several meetups: [Agileindy](https://www.meetup.com/agileindy/), [Indy Software Artisans](https://www.meetup.com/indysa/), [Agile Games](https://www.meetup.com/Agile-Games/), [Indy .NET Consortium](https://www.meetup.com/Indy-NET-Consortium/), etc.

[Functional programming](https://en.wikipedia.org/wiki/Functional_programming) is one of the topics that mostly caught my attention. For three main reasons: the approach I’ve never really deepen; the potential of this paradigm; and the passion conveyed by [Dave Fancher](https://davefancher.com/).

One of the most interesting feature of functional programming (FP) is surely the immutability of the “variables” (it would be more correct call them “immutable”), and how it leads to a different structure of source code w.r.t. object oriented programming (OOP).

In order to highlight the differences between those two approaches on this specific aspect, I had implemented the same application twice: first using C# (OOP) and then using F# (FP). The application simply had to:

*   read a bank account from a database, given the owner’s name;
*   allow the user to input an amount to withdraw and show the new balance;
*   ask confirmation to the user, and save the new balance on the DB only in case of affirmative answer;
*   cycle the above operations.

The complete examples’ source code is available on [GitHub](https://github.com/VenomAV/OOPComparedToFP.git).

## C#

First of all I defined the model of the bank account.

BankAccount.cs

1  
2  
3  
4  
5  
6  
7  
8  
9  
10  
11  
12  
13  
14  
15  
16  
17  
18  
19  
20  
21  

public class BankAccount  
{  
    public BankAccount()  
    {  
    }  
  
    public BankAccount(string owner, decimal balance)  
    {  
        Owner = owner;  
        Balance = balance;  
    }  
  
    public int Id { get; private set; }  
    public string Owner { get; private set; }  
    public decimal Balance { get; private set; }  
  
    public void Withdraw(decimal amount)  
    {  
        Balance -= amount;  
    }  
}  

The class is really simple. The `Id` property is useful just to work with Entity Framework for database persistence. I will just skip all the EF-related code since it is not significant for the sake of this post.

After that I developed the application which satisfies the requirements above.

Program.cs

1  
2  
3  
4  
5  
6  
7  
8  
9  
10  
11  
12  
13  
14  
15  
16  
17  
18  
19  
20  
21  
22  
23  
24  
25  
26  
27  
28  
29  
30  
31  
32  
33  
34  
35  
36  
37  
38  
39  
40  
41  
42  
43  
44  
45  
46  
47  
48  
49  
50  
51  
52  
53  

using System;  
using System.Linq;  
  
class Program  
{  
    static void Main(string\[\] args)  
    {  
        using (BankAccountContext context = new BankAccountContext())  
        {  
            while (TryWithdrawFromAccount(context)) ;  
        }  
    }  
  
    private static bool TryWithdrawFromAccount(BankAccountContext context)  
    {  
        string owner;  
        BankAccount bankAccount;  
  
        Console.Write("Type owner (or 'q' to exit): ");  
        owner = Console.ReadLine();  
        if (owner == "q")  
        {  
            return false;  
        }  
        bankAccount = context.BanckAccounts.FirstOrDefault(ba => ba.Owner == owner);  
        if (bankAccount != null)  
        {  
            WithdrawFromAccount(context, bankAccount);  
        }  
        return true;  
    }  
  
    private static void WithdrawFromAccount(BankAccountContext context,  
        BankAccount bankAccount)  
    {  
        Console.WriteLine($"{bankAccount.Owner} has {bankAccount.Balance}$");  
  
        Console.Write("How much you want to withdraw? ");  
        bankAccount.Withdraw(decimal.Parse(Console.ReadLine()));  
  
        if (ConfirmWithdraw(bankAccount) == "y")  
        {  
            context.SaveChanges();  
        }  
    }  
  
    private static string ConfirmWithdraw(BankAccount bankAccount)  
    {  
        Console.Write($"{bankAccount.Owner} new balance will be " +  
            $"{bankAccount.Balance}. Confirm operation? \[y/n\] ");  
        return Console.ReadLine();  
    }  
}  

The `Main` method just instantiate the EF context, while all the application logic is implemented in `TryWithdrawFromAccount` and `WithdrawFromAccount`. The application’s most important parts are:

*   the loading of bank account at line _25_;
*   the withdraw of the required amount at line _39_;
*   and the confirmation request with the persistence of the account at lines _41-44_.

Coding was easy. When running the application, everything works fine if the user confirms the withdraw. On the other hand, if the user doesn’t confirm the withdraw and ask again the balance of the same account, the application behaves as shown below.

![Console screenshot](https://res.cloudinary.com/andreavallotti/image/upload/blog/images/there-and-back-again/BankAccountCSharp.png "Esecuzione del programma C#")

The error stands out for those who usually works with EF: even if the new balance is persisted only if the user confirms, line _41_, the instance `bankAccount` has been already modified and it belongs to the EF context which is disposed only when the application is closed. That’s why the second time the user asks for the Alice’s balance, the displayed value is modified and not the original as one could expect.

With few changes, shown below, the application behaves in the expected way.

Program.cs

1  
2  
3  
4  
5  
6  
7  
8  
9  
10  
11  
12  
13  
14  
15  
16  
17  
18  
19  
20  
21  
22  
23  
24  
25  
26  
27  
28  
29  
30  
31  
32  
33  
34  
35  
36  
37  
38  
39  
40  
41  
42  
43  
44  
45  
46  
47  
48  

private static bool TryWithdrawFromAccount(BankAccountContext context)  
{  
    string owner;  
    BankAccount bankAccount;  
  
    Console.Write("Type owner (or 'q' to exit): ");  
    owner = Console.ReadLine();  
    if (owner == "q")  
    {  
        return false;  
    }  
    bankAccount = TryGetBankAccountByOwner(context, owner);  
    if (bankAccount != null)  
    {  
        WithdrawFromAccount(context, bankAccount);  
    }  
    return true;  
}  
  
private static void WithdrawFromAccount(BankAccountContext context,  
    BankAccount bankAccount)  
{  
    Console.WriteLine($"{bankAccount.Owner} has {bankAccount.Balance}$");  
  
    Console.Write("How much you want to withdraw? ");  
    bankAccount.Withdraw(decimal.Parse(Console.ReadLine()));  
  
    if (ConfirmWithdraw(bankAccount) == "y")  
    {  
        UpdateBankAccount(context, bankAccount);  
    }  
}  
  
private static BankAccount TryGetBankAccountByOwner(BankAccountContext context,  
    string owner)  
{  
      
    return context.BanckAccounts.AsNoTracking()  
        .FirstOrDefault(ba => ba.Owner == owner);  
}  
  
private static void UpdateBankAccount(BankAccountContext context,   
    BankAccount bankAccount)  
{  
      
    context.Entry(bankAccount).State = System.Data.Entity.EntityState.Modified;  
    context.SaveChanges();  
}  

In order to work with the domain object without polluting the EF context the bank account has been detached from the context (method `AsNoTracking` at line _38_), and attached back just after the user confirmation (line _46_).

Now let see how the application can be implemented in F#.

## F#

Also in this case I immediately defined the domain model. It consists of a [record](https://docs.microsoft.com/en-us/dotnet/fsharp/language-reference/records) and a `withdraw` function which, following the immutability principle, creates a copy of the original record with the new balance.

BankAccount.fs

1  
2  
3  
4  
5  
6  

module BankAccount  
  
type BankAccount \= {Id:int; Owner:string; Balance:decimal}  
  
let withdraw = fun bankAccount (amount:decimal) ->  
  ({ bankAccount with Balance = bankAccount.Balance - amount })  

After that I implemented the data access functions which, relying on the F# Data Provider for SQL Server, and the same database used for the C# example, simply map the `BankAccount` record with the DB fields.

DataAccess.fs

1  
2  
3  
4  
5  
6  
7  
8  
9  
10  
11  
12  
13  
14  
15  
16  
17  
18  
19  
20  
21  
22  
23  
24  
25  
26  
27  
28  
29  
30  

module DataAccess  
  
open Microsoft.FSharp.Data.TypeProviders  
open BankAccount  
  
\[<Literal>\]  
let connectionString = "Data Source=(localdb)\\mssqllocaldb;Initial Catalog=BankAccounts;Integrated Security=True"  
  
type dbSchema \= SqlDataConnection<connectionString>  
  
let tryGetBankAccountByOwner =  
  fun (db:dbSchema.ServiceTypes.SimpleDataContextTypes.BankAccounts) owner ->  
    (query { for ba in db.BankAccounts1 do  
             where (ba.Owner = owner);  
             select {  
               Id = ba.Id;  
               Owner = ba.Owner;  
               Balance = ba.Balance  
             }  
           } |> Seq.tryHead)  
  
let updateBankAccount =  
  fun (db:dbSchema.ServiceTypes.SimpleDataContextTypes.BankAccounts) bankAccount ->  
    (query { for ba in db.BankAccounts1 do  
             where (ba.Id = bankAccount.Id);  
             select ba  
           } |> Seq.iter(fun ba ->  
                             ba.Owner <- bankAccount.Owner;  
                             ba.Balance <- bankAccount.Balance)  
     db.DataContext.SubmitChanges())  

It is worth noting that, with this approach, the application code is naturally detached from the database.

Finally, I created a console application which is really similar to the C# one.

Program.fs

1  
2  
3  
4  
5  
6  
7  
8  
9  
10  
11  
12  
13  
14  
15  
16  
17  
18  
19  
20  
21  
22  
23  
24  
25  
26  
27  
28  
29  
30  
31  
32  
33  
34  
35  
36  

module Program  
  
open System  
open BankAccount  
open DataAccess  
  
let printConfirmWithdraw = fun bankAccount ->  
  printf "%s new balance will be %M. Confirm operation? \[y/n\] "  
    bankAccount.Owner bankAccount.Balance  
  
let confirmWithdraw =  
  fun bankAccount amount -> amount |> withdraw bankAccount |> printConfirmWithdraw  
                            Console.ReadLine()  
  
let withdrawFromAccount = fun db bankAccount ->  
  (printfn "%s has %M$" bankAccount.Owner bankAccount.Balance  
   printf "How much you want to withdraw? "  
   let amount = Console.ReadLine() |> decimal  
   match confirmWithdraw bankAccount amount with  
     | "y" -> amount |> withdraw bankAccount |> updateBankAccount db  
     | \_ -> ())  
  
let tryWithdrawFromAccount = fun db ->  
  printf "Type owner (or 'q' to exit): "  
  match Console.ReadLine() with  
    | "q" -> false  
    | owner -> (match tryGetBankAccountByOwner db owner with  
                  | None -> ()  
                  | Some bankAccount -> withdrawFromAccount db bankAccount  
                true)  
  
\[<EntryPoint>\]  
let main argv =  
  let db = dbSchema.GetDataContext()  
  while tryWithdrawFromAccount(db) do ()  
  0  

Like before the `main` function manages the DB connection (line _34_) and the application logic is entirely implemented in the `tryWithdrawFromAccount` and `withdrawFromAccount` functions. The application’s most important parts are:

*   the loading of bank account at line _27_;
*   the withdraw of the required amount at line _20_;
*   and the confirmation request with the persistence of the account at lines _20_.

In this case, everything works. On the other hand, coding was harder just because I am more used to OOP.

## Conclusions

Developing this simple application, the immutability naturally helps me to clearly define the seams between read/write of the data and the elaboration of those data. As I pointed out with the C# samples, the same level of separation can be achieved also with OOP.

The main difference between the two approaches is that in order to write good code with the OOP paradigm you have to be disciplined, while in order to write ugly code with the functional paradigm you have to be fairly undisciplined 😃 On the other hand, the object oriented programming is probably more intuitive w.r.t. the FP which is basically more formal.

There are several other features which are debated between FP and OOP: source code readability, source code verbosity, performance, etc. If I will experiment more on these aspects, I will share the results.
