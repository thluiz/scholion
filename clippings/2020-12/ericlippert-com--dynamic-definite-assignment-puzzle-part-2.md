---
url: "https://ericlippert.com/2018/11/19/a-dynamic-definite-assignment-puzzle-part-2/"
captured_at: "2020-12-31T09:12:28-03:00"
title: "A dynamic definite assignment puzzle, part 2 | Fabulous adventures in coding"
domain: "ericlippert-com"
---

# A dynamic definite assignment puzzle, part 2

Posted on [November 19, 2018](https://ericlippert.com/2018/11/19/a-dynamic-definite-assignment-puzzle-part-2/ "9:15 am")

Sorry for that unexpected interlude into customer service horrors; thanks for your patience and let’s get right back to coding horrors!

So as not to bury the lede: **the C# compiler is correct to flag the program from the last episode as having a definite assignment problem.** Thanks to everyone who participated in the discussion in the comments.

Particular mentions go out to Jeffrey L. Whitledge who sketched the solution mere moments after I posted the problem, C# architect Neal Gafter who posted a concise demonstration, and former C# compiler dev Chris Burrows who slyly pointed out on Twitter that he “solved the puzzle”. Indeed, he solved it nine years ago *when he designed and implemented this logic in the compiler*.

The reasoning the compiler has to go through here is rather arcane, so let’s dig into it.

First off, let’s remind ourselves of the fundamental rule of `dynamic` in C#. We identify all the places in the program where the compiler deduces that the type of a thing is `dynamic`. Imagine that you then replaced that type judgment with *the actual runtime type of the thing*. The behaviour of the program with `dynamic` should be the same as the behaviour of the imaginary program where the compiler knew the runtime type.

This means that the compiler has to assume that the control flow of a program containing `dynamic` could be *any control flow possible for any runtime type, including types that are legal but extremely weird.* So let’s make an extremely weird type or two and see what happens.

I’ve already discussed in this blog how operator overloading works for the `&&` operator. Briefly, the rules in C# are:

- if `left` is `false` then `left && right` does not evaluate `right`, and has the same value as `left`
- otherwise, `left && right` evaluates both operands and has the same value as `left & right`

Obviously those rules work for `bool`; to overload `&&`, we therefore need a way to evaluate whether `left` is false or not, and a way to determine the value of `left & right`. The “operator true” and “operator false” operators tell you whether a given value is logically true or logically false, and both must be provided if you provide either. Let’s look at an example, but we’ll make it a crazy example!

classCrazy  
{  
publicstaticbooloperatortrue(Crazyc)  
{  
Console.WriteLine(“operator true”);  
returntrue;  // Um…  
}  
publicstaticbooloperatorfalse(Crazyc)  
{  
Console.WriteLine(“operator false”);  
returntrue;// Oh dear…  
}  
publicstaticCrazyoperator&(Crazya,Crazyb)  
{  
Console.WriteLine(“operator &”);  
returna;  
}  
}

This is obviously weird and wrong; this program says that all instances of `Crazy` are logically `true`, and also all of them are logically `false` (because “is this false?” returns `true`) and also if we `&` two of them together, we get the first unconditionally. But, whatever, this is a legal program. If we have

Crazyc=GetCrazy()&&GetAnother();

The code generated will be the moral equivalent of:

Crazyc1=GetCrazy();  
Crazyc=Crazy.operator\_false(c1)?  
  c1:  Crazy.operator\_&(c1,GetAnother());

But of course at runtime for this particular program we will always say that `c1` is `false`, and always just take the first operand without calling `GetAnother()`.

Already we’ve got a very strange program, but maybe it is not entirely clear how this produces a code path that has a definite assignment error. To get that, we need a second super-weird class. This one overloads equality — C# requires you to overload equality and inequality in pairs as well — and instead of returning a Boolean, it returns, you guessed it, something crazy:

classWeird  
{  
publicstaticCrazyoperator==(Weirdp1,Weirdp2)  
{  
Console.WriteLine(“==”);  
returnnewCrazy();  
}  
publicstaticCrazyoperator!=(Weirdp1,Weirdp2)  
{  
Console.WriteLine(“!=”);  
returnnewCrazy();  
}  
publicoverrideboolEquals(objectobj) => true;  
publicoverrideintGetHashCode() => 0;  
}

Maybe now you see where this is going, but we’re not quite there yet. Suppose we have

Weirdobj=newWeird();  
stringstr;  
if(obj !=null&&GetString(outstr))

What’s going to happen? `Weird` overrides `!=`, so this will call `Weird.operator_!=`, which returns `Crazy`, and now we have `Crazy && bool`, which is not legal, so the program will not compile. But what if we make `Crazy` convertible **from** `bool`? Then it will work! So add this to `Crazy`:

publicstaticimplicitoperatorCrazy(boolb)  
{  
Console.WriteLine(“implicit conversion from bool “+b);  
returnnewCrazy();  
}

Now what does if(obj !=null&&GetString(outstr)) … mean?  Let’s turn it into method calls. This thing all together is:

Crazyc1=Weird.operator\_!=(obj,null);  
boolb1=Crazy.operator\_false(c1);// it is true that it is false  
Crazyc2 = b1 ?   
  c1 : // This is the branch we take  
Crazy.operator\_implicit(GetString(outstr));  
if(c2) …

But wait a minute, is `if(c2)` legal? Yes it is, because `Crazy` implements `operator true`, which is then called by the `if` statement, and it returns `true`!

We have just demonstrated that it is possible to write the program fragment

if(obj !=null&&GetString(outstr))  
Console.WriteLine(obj + str);

and have the consequence get executed even if `GetString` is never called, and therefore `str` would be read before it was written, and therefore this program must be illegal. And indeed, if you remove the definite assignment error and run it, you get the output

```
!=
operator false
operator true
```

In the case where `obj` is `dynamic`, the compiler must assume the worst possible case, no matter how unlikely. It must assume that the `dynamic` value is one of these weird objects that overloads equality to return something crazy, and that the crazy thing can force the compiler to skip evaluating the right side but still result in a true value.

What is the moral of this story? There are several. The most practical moral is: **do not compare any `dynamic` value to null!** The correct way to write this code is

if((object)obj !=null&&GetString(outstr))

And now the problem goes away, because `dynamic` to `object` is always an identity conversion, and now the compiler can generate a null check normally, rather than going through all this rigamarole of having to see if the object overloads equality.

The moral for the programming language designer is: **operator overloading is a horrible horrible feature that makes your life harder.**

The moral for the compiler writer is: **get good at coming up with weird and unlikely possible programs, because you’re going to have to do that a lot when you write test cases.**

Thanks to Stack Overflow contributor “NH.” for the question which prompted this puzzle.
