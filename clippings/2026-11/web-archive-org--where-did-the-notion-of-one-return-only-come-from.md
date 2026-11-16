---
url: "https://web.archive.org/web/20200607181758id_/https://softwareengineering.stackexchange.com/questions/118703/where-did-the-notion-of-one-return-only-come-from"
captured_at: "2026-11-16T08:11:49+00:00"
title: "Where did the notion of \"one return only\" come from?"
domain: "web-archive-org"
---

This notion of _Single Entry, Single Exit_ (SESE) comes from **_languages with explicit resource management_**, like C and assembly. In C, code like this will leak resources:

```
void f()
{
  resource res = acquire_resource();  // think malloc()
  if( f1(res) )
    return; // leaks res
  f2(res);
  release_resource(res);  // think free()
}
```

In such languages, you basically have three options:

*   Replicate the cleanup code.  
    Ugh. Redundancy is always bad.
    
*   Use a `goto` to jump to the cleanup code.  
    This requires the cleanup code to be the last thing in the function. (And this is why some argue that `goto` has its place. And it has indeed – in C.)
    
*   Introduce a local variable and manipulate control flow through that.  
    The disadvantage is that control flow manipulated through syntax (think `break`, `return`, `if`, `while`) is much easier to follow than control flow manipulated through the state of variables (because those variables have no state when you look at the algorithm).
    

In assembly it's even weirder, because you can jump to any address in a function when you call that function, which effectively means you have an almost unlimited number of entry points to any function. (Sometimes this is helpful. Such thunks are a common technique for compilers to implement the `this` pointer adjustment necessary for calling `virtual` functions in multiple-inheritance scenarios in C++.)

When you have to manage resources manually, exploiting the options of entering or exiting a function anywhere leads to more complex code, and thus to bugs. Therefore, a school of thought appeared that propagated SESE, in order to get cleaner code and less bugs.

* * *

However, when a language features exceptions, (almost) any function might be exited prematurely at (almost) any point, so you need to make provisions for premature return anyway. (I think `finally` is mainly used for that in Java and `using` (when implementing `IDisposable`, `finally` otherwise) in C#; C++ instead employs [RAII](https://stackoverflow.com/q/712639/140719).) Once you have done this, you _cannot_ fail to clean up after yourself due to an early `return` statement, so what is probably the strongest argument in favor of SESE has vanished.

That leaves readability. Of course, a 200 LoC function with half a dozen `return` statements sprinkled randomly over it is not good programming style and does not make for readable code. But such a function wouldn't be easy to understand without those premature returns either.

In languages where resources are not or should not be managed manually, there is little or no value in adhering to the old SESE convention. OTOH, as I have argued above, **_SESE often makes code more complex_**. It is a dinosaur that (except for C) does not fit well into most of today's languages. Instead of helping the understandability of code, it hinders it.

* * *

Why do Java programmers stick to this? I don't know, but from my (outside) POV, Java took a lot of conventions from C (where they make sense) and applied them to its OO world (where they are useless or outright bad), where it now sticks to them, no matter what the costs. (Like the convention to define all your variables at the beginning of the scope.)

Programmers stick to all kinds of strange notations for irrational reasons. (Deeply nested structural statements – "arrowheads" – were, in languages like Pascal, once seen as beautiful code.) Applying pure logical reasoning to this seems to fail to convince the majority of them to deviate from their established ways. The best way to change such habits is probably to teach them early on to do what's best, not what's conventional. You, being a programming teacher, have it in your hand. `:)`
