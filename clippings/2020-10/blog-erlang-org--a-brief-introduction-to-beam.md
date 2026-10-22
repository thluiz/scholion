---
url: "http://blog.erlang.org/a-brief-BEAM-primer/"
captured_at: "2020-10-22T10:02:39-03:00"
title: "A brief introduction to BEAM – A Blog from the Erlang/OTP team – The Erlang/OTP team at Ericsson, the implementors and maintainers of Erlang/OTP."
domain: "blog-erlang-org"
---

# A brief introduction to BEAM

October 20, 2020 · by John Högberg .

This post is a brief primer on BEAM, the virtual machine that executes user
code in the Erlang Runtime System (ERTS). It’s intended to help those new to
BEAM follow an upcoming series of posts about the JIT in OTP 24, leaving
implementation details for later.

BEAM is often confused with ERTS and it’s important to distinguish between the
two; BEAM is just the virtual machine and it has no notion of processes, ports,
ETS tables, and so on. It merely executes instructions and while ERTS has
influenced their design, it doesn’t affect what they do when the code is
running, so you don’t need to understand ERTS to understand BEAM.

BEAM is a register machine, where all instructions operate on named registers.
Each register can contain any Erlang term such as an integer or a tuple, and it
helps to think of them as simple variables. The two most important kinds of
registers are:

- `X`: these are used for temporary data and passing data between functions.
  They don’t require a stack frame and can be freely used in any function, but
  there are certain limitations which we’ll expand on later.
- `Y`: these are local to each stack frame and have no special
  limitations beyond needing a stack frame.

Control flow is handled by instructions that test a certain condition and
either move on to the next instruction or branch to its *fail label*, noted by
`{f,Index}`. For example `{test,is_integer,{f,7},[{x,0}]}.` checks if `{x,0}`
contains an integer and jumps to label 7 if it doesn’t.

Function arguments are passed from left to right in `X` registers, starting at
`{x,0}`, and the result is returned in `{x,0}`.

It’s easier to explain how this fits together through example, so let’s walk
through a few:

```
sum_tail(List) ->
    sum_tail(List, 0).

sum_tail([Head | Tail], Acc) ->
    sum_tail(Tail, Head + Acc);
sum_tail([], Acc) ->
    Acc.
```

Let’s use `erlc -S` to look at the instructions one by one:

```
%% sum_tail/1, entry label is 2
{function, sum_tail, 1, 2}.

  %% Marks a jump target with the label 1.
  {label,1}.

    %% Special instruction that raises a function_clause
    %% exception. Unused in this function.
    {func_info,{atom,primer},{atom,sum_tail},1}.

  {label,2}.
    %% The meat of the function starts here.
    %%
    %% Our only argument - List - is in {x,0} and
    %% since sum_tail/2 expects it to be the first
    %% argument we can leave it be. We'll pass the
    %% integer 0 as the second argument in {x,1}.
    {move,{integer,0},{x,1}}.

    %% Tail call sum_tail/2, whose entry label is 4.
    {call_only,2,{f,4}}.

%% sum_tail/2, entry label is 4
{function, sum_tail, 2, 4}.
  {label,3}.
    {func_info,{atom,primer},{atom,sum_tail},2}.
  {label,4}.

    %% Test whether we have a non-empty list, and jump to
    %% the base case at label 5 if we don't.
    {test,is_nonempty_list,{f,5},[{x,0}]}.

    %% Unpack the list in the first argument, placing the
    %% head in {x,2} and the tail in {x,0}.
    {get_list,{x,0},{x,2},{x,0}}.

    %% Add the head and our accumulator (remember that the
    %% second function argument is in {x,1}), and place
    %% the result in {x,1}.
    %%
    %% A fail label of 0 means that we want the
    %% instruction to throw an exception on error, rather
    %% than jump to a given label.
    {gc_bif,'+',{f,0},3,[{x,2},{x,1}],{x,1}}.

    %% Tail-call ourselves to handle the rest of the list,
    %% the arguments are already in the right registers.
    {call_only,2,{f,4}}.

  {label,5}.
    %% Test whether our argument was the empty list. If
    %% not, we jump to label 3 to raise a function_clause
    %% exception.
    {test,is_nil,{f,3},[{x,0}]}.

    %% Return our accumulator.
    {move,{x,1},{x,0}}.
    return.
```

Simple enough, isn’t it?

I glossed over one little detail though; the mysterious number `3` in the
addition instruction. This number tells us how many `X` registers hold live
data in case we need more memory, so they can be preserved while the rest are
discarded as garbage. As a consequence, it’s unsafe to refer to higher `X`
registers after this instruction as their contents may be invalid (in this case
`{x,3}` and above).

Function calls are similar; we may schedule ourselves out whenever we call or
return from a function, and we’ll only preserve the function arguments/return
value when we do so. This means that all `X` registers except for `{x,0}` are
invalid after a call even if you knew for certain that the called function
didn’t touch a certain register.

This is where `Y` registers enter the picture. Let’s take the previous example
and make it body-recursive instead:

```
sum_body([Head | Tail]) ->
    Head + sum_body(Tail);
sum_body([]) ->
    0.
```

.

```
{function, sum_body, 1, 7}.
  {label,6}.
    {func_info,{atom,primer},{atom,sum_body},1}.
  {label,7}.
    {test,is_nonempty_list,{f,8},[{x,0}]}.

    %% Allocate a stack frame with a single Y register.
    %% Since this instruction may need more memory, we
    %% tell the garbage collector that we currently have
    %% one live X register (our list argument in {x,0}).
    {allocate,1,1}.

    %% Unpack the list, placing the head in {y,0} and
    %% the tail in {x,0}.
    {get_list,{x,0},{y,0},{x,0}}.

    %% Body-call ourselves. Note that while this kills all
    %% X registers, it leaves Y registers alone so our
    %% head is still valid.
    {call,1,{f,7}}.

    %% Add the head to our return value and store the
    %% result in {x,0}.
    {gc_bif,'+',{f,0},1,[{y,0},{x,0}],{x,0}}.

    %% Deallocate our stack frame and return.
    {deallocate,1}.
    return.

  {label,8}.
    {test,is_nil,{f,6},[{x,0}]}.

    %% Return the integer 0.
    {move,{integer,0},{x,0}}.
    return.
```

Notice how the call instruction changed now that we’re in a stack frame? There
are three different call instructions:

- `call`: ordinary call as in the example. Control flow will resume at
  the next instruction when the called function returns.
- `call_last`: tail call when there is a stack frame. The current frame will
  be deallocated before the call.
- `call_only`: tail call when there is no stack frame.

Each of these have a variant for calling functions in other modules (e.g.
`call_ext`), but they’re otherwise identical.

So far we’ve only looked at using terms, but what about creating them? Let’s
have a look:

```
create_tuple(Term) ->
    {hello, Term}.
```

.

```
{function, create_tuple, 1, 10}.
  {label,9}.
    {func_info,{atom,primer},{atom,create_tuple},1}.
  {label,10}.
    %% Allocate the three words needed for a 2-tuple, with
    %% a liveness annotation of 1 indicating that {x,0}
    %% is alive in case we need to GC.
    {test_heap,3,1}.

    %% Create the tuple and place the result in {x,0}
    {put_tuple2,{x,0},{list,[{atom,hello},{x,0}]}}.
  
    return.
```

This is a bit magical in the sense that there’s an unseen register for memory
allocations, but allocation is rarely far apart from use and it’s usually
pretty easy to follow. The same principle applies for lists ([consing](https://en.wikipedia.org/wiki/Cons)),
floats, and funs as well following [PR 2765](https://github.com/erlang/otp/pull/2765).

More complicated types like maps, big integers, references, and so on are
created by special instructions that may GC on their own (or allocate outside
the heap in a “heap fragment”) as their size can’t be statically determined in
advance.

Now let’s look at something more uncommon: exceptions.

```
exception() ->
    try
        external:call()
    catch
        throw:example -> hello
    end.
```

.

```
{function, exception, 0, 12}.
  {label,11}.
    {func_info,{atom,primer},{atom,exception},0}.
  {label,12}.
    {allocate,1,0}.
  
    %% Place a catch tag in {y,0}. If an exception is
    %% raised while this tag is the most current one,
    %% the control flow will resume at {f,13} in this
    %% stack frame.
    {'try',{y,0},{f,13}}.

    {call_ext,0,{extfunc,external,call,0}}.

    %% Deactivate the catch tag before returning with the
    %% result from the call.
    {try_end,{y,0}}.

    {deallocate,1}.
    return.

  {label,13}.
    %% Uh oh, we've got an exception. Kill the catch tag
    %% and place the exception class in {x,0}, the error
    %% reason/thrown value in {x,1}, and the stack trace
    %% in {x,2}.
    {try_case,{y,0}}.

    %% Return 'hello' if the user threw 'example'
    {test,is_eq_exact,{f,14},[{x,0},{atom,throw}]}.
    {test,is_eq_exact,{f,14},[{x,1},{atom,example}]}.
    {move,{atom,hello},{x,0}}.
    {deallocate,1}.
    return.

  {label,14}.
    %% Otherwise, rethrow the exception since no catch
    %% clause matched.
    {bif,raise,{f,0},[{x,2},{x,1}],{x,0}}.
```

By now you’ve probably noticed how the control flow only moves forward; just
like Erlang itself the only way to loop is through recursion. The one exception
to this is the receive construct, which may loop until a matching message has
been received:

```
selective_receive(Ref) ->
    receive
        {Ref, Result} -> Result
    end.
```

.

```
{function, selective_receive, 1, 16}.
  {label,15}.
    {func_info,{atom,primer},{atom,selective_receive},1}.
  {label,16}.
    {allocate,1,1}.

    %% We may be scheduled out while waiting for a
    %% message, so we'll preserve our Ref in {y,0}.
    {move,{x,0},{y,0}}.

  {label,17}.
    %% Pick the next message from the process' message box
    %% and place it in {x,0}, jumping to label 19 if the
    %% message box is empty.
    {loop_rec,{f,19},{x,0}}.
  
    %% Does it match our pattern? If not, jump to label 18
    %% and try the next message.
    {test,is_tuple,{f,18},[{x,0}]}.
    {test,test_arity,{f,18},[{x,0},2]}.
    {get_tuple_element,{x,0},0,{x,1}}.
    {test,is_eq_exact,{f,18},[{x,1},{y,0}]}.

    %% We've got a match, extract the result and remove
    %% the message from the mailbox.
    {get_tuple_element,{x,0},1,{x,0}}.
    remove_message.
    {deallocate,1}.
    return.

  {label,18}.
    %% The message didn't match, loop back to handle our
    %% next message. Note that the current message remains
    %% in the inbox since a different receive may be
    %% interested in it.
    {loop_rec_end,{f,17}}.

  {label,19}.
    %% Wait until the next message arrives, returning to
    %% the start of the loop when it does. If there's a
    %% timeout involved, it will be handled here.
    {wait,{f,17}}.
```

There’s not much more to it, and if you feel comfortable following the examples
above you should have no problems with the JIT series.

If you’re curious about which instructions there are, you can find a brief
description of every instruction in [genop.tab](https://github.com/erlang/otp/blob/master/lib/compiler/src/genop.tab).
