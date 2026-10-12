---
url: "https://mazenharake.wordpress.com/2010/10/31/9-erlang-pitfalls-you-should-know-about/"
captured_at: "2014-07-09T10:03:04-03:00"
title: "9 Erlang pitfalls you should know about | MazenHarake"
domain: "mazenharake-wordpress-com"
---

# 9 Erlang pitfalls you should know about

Mistakes are a pure time waste and I believe one should invest time in doing things thoroughly rather than messy. But since much of our work requires fast delivery times we must find tools to help us minimize the mistakes we do. We need to cover as much of the “mistake spectra” as we can and our most important tool in the end is going to be experience.

Here is a list of 9 mistakes which are easily made in Erlang that I consider to be important to know about. Some of them are really subtle in the sense that they don’t necessarily cause a problem at compile time or when tested. This makes them dangerous in live systems and can potentially be really big time hoggers but using good tests when knowing these pitfalls should help raise confidence in the system. The order of the list below doesn’t mean anything, it just to helps you count to 9

### 1. Forgetting the new state.

Imagine you have a gen\_server and that gen\_server handles a few handle\_calls and a state of some sort. At some point you want to manipulate the state and return it as the “new state” by returning it to the gen\_server. Consider the following example:

|  |  |
| --- | --- |
|  | `handle_call(cmd, _``From``,` `State``) ->;`  `...`  `NState` `= manipulate_state(``State``),`  `....`  `{reply, ok,` `State``#state{ last_update = now() }}.` |

The problem in this case is that it is sometimes easy to forget the new state when updating the state a second time on the last line (or several times). In the above example the state is updated with a time stamp right before the returning and this is done with the state `State` and not `NState`. This usually happens because one sees the two updates separately and when writing the last statement the previous update has been forgotten.

**Solution:**  Write shorter functions and update as much of the data you can in one place rather then “staged” updates.

### 2. Accidentally using pattern matching.

So lets say you have a function which binds some variables in the header. Usually this is something that represents a value which is related to what the function does. Inside the function however you can have more logic which binds more variables (e.g. by using pattern matching). This can present a problem because if you accidentally use the same variable but intended it to be a different one then you are pattern matching and not binding. Consider:

|  |  |
| --- | --- |
|  | `read_update_records(``Table``, N) ->`  `NewRecords` `=` `lists:map``(``fun` `foo/1,` `db:read``(``Table``, N)),`  `%% something, something...`  `case` `db:update``(``DbCon``,` `NewRecords``)` `of`  `{ok, N} ->`  `log("``Yay``, updated ~p number` `of` `records, [N])`  `{error,` `Reason``} ->`  `log(``"Fail!"``,[]),`  `exit({error,` `Reason``})`  `end``.` |

In this example lets say 10 records are read; they are manipulated and then written back. Assume for argument’s sake that the `N` variable returned is the number of records updated. Now usually this will be the same and thus no problems (`N` matches in all places) but that is just pure luck it is a somewhat weak assumption. One might get away with this but eventually it will probably fail. I have seen this type of bugs in production code which has lasted for months waiting for the right moment to strike; usually it comes at a time when one is celebrating your great success in creating a system with such an impressive uptime

Another example is that the \_`Variable` syntax is a valid variable and gets bound; the **only** difference is that the compiler doesn’t complain about them not being used so you might *think* they are safe. A variable \_`Variable` should not be confused with the “don’t-care-variable”. An example:

|  |  |
| --- | --- |
|  | `1> _Foo = 1.`  `1`  `2> _Foo = 2.`  `** exception error: no match of right hand side value 2`  `3> _ = 1.`  `1`  `4> _ = 2.`  `2` |

**Solution:**  Don’t give your variable names too generic names; ideally the code should be “self documenting” by the use of good variable names. Also: short functions and don’t re-use “Don’t-care” variables. If you run into this bug it is usually a good indicator that your functions are too big or doing too many things.

### 3. `"private property" -- "property" /= "private "`

This bites people who are not used to how Erlang handles strings. As you might know, strings are just lists and assuming two lists *A* and *B* then this case can be read like this:

*For each element in B, find it in A. If it exists in A then remove the first occurrence of it from A. Return the rest of A*.

If we assume `A = "private property"` and `B = "property"` then this means:

|  |  |
| --- | --- |
|  | `1>` `"private property"` `--` `"property"``.`  `"iva pert"` |

**Solution:**  Remember that strings are lists… it is as simple as that.

### 4. Guard tests silently fail

Exactly what the title says; be careful about this. An example:

|  |  |
| --- | --- |
|  | `1> F =` `fun``(``List``)` `when` `length(``List``) > 0 -> ok; (_) -> not_ok` `end``.`  `#``Fun``<erl_eval.6.13229925>`  `2> F([1,2]).`  `ok`  `3> F({1,2}).`  `not_ok` |

`length({1,2})` should result in a bad argument but it doesn’t. This also affects lists comprehensions and has surprised many

|  |  |
| --- | --- |
|  | `1> [ X || X <- [1, 2, foo, bar, 5, 6], X` `rem` `2 == 0 ].`  `[2,6]` |

Normally `foo rem 2` will result in a bad argument but in this case it is just skipped. This is a logical behaviour but sometimes not so obvious. I most often hear complains about this one when a set of corrupted data is being worked on and the guards silently fail not taking that failing piece of data into account. An example is that we want to update 10 rows in a database and we only update 9 it could turn out to be that one of the values we are iterating over is not an integer.

**Solution:**  Learn it, get over it

### 5. Returning arbitrary `{error, Reason}`

This is a very common mistake and is bound to cause problems at some point in time. This is one of the most apparent cases where the Let it crash philosophy applies but still even some experienced developers fail to recognize it. Ponder the following example: Assume that you have a function that does something in a database and for the sake of argument lets say that you have manipulate some data before you update the database E.g:

|  |  |
| --- | --- |
|  | `update_db_value(``Key``,` `Value``) ->`  `case` `db:connect``()` `of`  `{ok,` `Con``} ->`  `NValue` `= term_to_special_format(``Value``),`  `case` `db:write``(``Con``,` `Key``,` `NValue``)` `of`  `ok ->`  `ok;`  `{error,` `Reason``} ->`  `log(``Reason``),`  `db:disconnect``(``Con``),`  `{error, unable_to_write_value}`  `end``;`  `{error,` `Reason``}`  `log(``Reason``),`  `{error, unable_to_connect}`  `end``.` |

Now there are several things to consider; are you suppose to return the errors? Will they (the errors) be understood by the above layer? Are you writing a library and thus the above layer adjusts to you? etc…

If we assume that this code is under a management application and that this code is glue code then we could argue that returning arbitrary error messages is a bad idea. If you find ourself in a situation like this then you need to ask ourself if you don’t need to go back to specification and define what to do rather then just returning “error-something”.

Usually, however, the choice depends on higher layers since a crash will propagate. Tests might not be enough, for example 1) your stubs of the management application might accept the return values but the real one might not. 2) There might be too many cases where you haven’t considered returning an error tuple and your code becomes very inconsistent (sometimes crashing, sometimes not) or 3) You might be defining the wrong behaviour in code and thus there is an inconsistency between code and specification/design. In my humble opinion I think the following would be better (assuming the circumstances allow):

|  |  |
| --- | --- |
|  | `update_db_value(``Key``,` `Value``) ->`  `{ok,` `Con``} =` `db:connect``(),`  `db:write``(``Con``,` `Key``, term_to_special_format(``Value``)),`  `db:disconnect``(``Con``).` |

This particular point can be a subject for endless discussion so I’ll just stop here; my point is just simply: be careful about what you return from a function because error tuples don’t just disappear.

**Solution:**  [Read this](https://mazenharake.wordpress.com/2009/09/14/let-it-crash-the-right-way/) and don’t blindly return `{error, Reason}`

### 6. `#record{}` ambiguity in function clause and function body

When you write `#record{}` in a function body the compiler will replace that with a tuple of the same arity as there are number of fields in the record definition and put the different positions in the tuple to the default values which are also specified in the record definition.

|  |  |
| --- | --- |
|  | `-record(foo, { bar = 1, baz }.` |

in a function body becomes:

|  |  |
| --- | --- |
|  | `{foo, 1, undefined}` |

Now you might have expected it to be replaced the same way in a function clause… well no not really. When the `#record{}` notation is used in a function clause it is replaced by a set of guards which are used to match the function clause. However, any variable you bind in the function clause will however still bind to the actual tuple and the correct values. An example, consider this:

|  |  |
| --- | --- |
|  | `-``module``(foo).`  `-record(foo, { bar, baz }).`  `function() ->`  `r(#foo{}),`  `r(#foo{ bar = 1 }).`  `r(#foo{ baz = undefined } =` `Foo``) ->` `io:format``(``"1: bar == ~p~n"``,[``Foo``#foo.bar]);`  `r(#foo{ bar = 1 } =` `Foo``) ->` `io:format``(``"2: bar == ~p~n"``,[``Foo``#foo.bar]).` |

If we didn’t know better we would think the output would be

|  |  |
| --- | --- |
|  | `1: bar == undefined`  `2: bar == 1` |

but when we run the example it shows

|  |  |
| --- | --- |
|  | `1: bar == undefined`  `1: bar == 1` |

In the source code example above; line 4 is replaced with `r({foo, undefined, undefined}),` and logically matches the first clause of the `r/1` function on line 7. However on line 5 the line will be replaced with `r({foo, 1, undefined})` but it will still match on the first function clause on line 7. We would think that it should match on line 8 because of an assumption that the record in the function clause on line 7 is replaced with `{foo, undefined, undefined}` which is not what we were trying to match (namely `{foo, 1, undefined}`) thus line 7 doesn’t match and we go to line 8. So what is going on?

Well what happens is that the record, as mentioned, is replaced with different things at different places. In a function body the `#record{}` notation is just replaced with `{foo, undefined, undefined}` but in a function clause the function clause is extended with a series of guards. The guards that are specified are derived from what we wrote in code, the rest are not checked. E.g. `#foo{}` is replaced with guards to check that the argument passed is a tuple, that it is the same arity as specified and that the first element is the atom `foo` but it doesn’t check anything about element 2 or 3. This means that if we write `#foo{ biz = undefined }` it will add a guard to check that `biz == undefined` (or rather the position known as `biz`). Not including `biz` is not the same as including it and setting the value to undefined (even though that is usually the “default” value). This means that when you run the above example the second statement doesn’t have any affect since the value in position `bar` does not change the matching of the function on line 7.

To show my point more clear you can compile the module above like this:

|  |  |
| --- | --- |
|  | `$> erlc -S foo.erl` |

A part of the output file for me shows:

|  |  |
| --- | --- |
|  | `...`  `{function, r, 1, 4}.`  `{label,3}.`  `{func_info,{atom,foo},{atom,r},1}.`  `{label,4}.`  `{test,is_tuple,{f,3},[{x,0}]}.`  `{test,test_arity,{f,3},[{x,0},3]}.`  `{get_tuple_element,{x,0},0,{x,1}}.`  `{get_tuple_element,{x,0},1,{x,2}}.`  `{get_tuple_element,{x,0},2,{x,3}}.`  `{test,is_eq_exact,{f,3},[{x,1},{atom,foo}]}.`  `{test,is_eq_exact,{f,5},[{x,3},{atom,undefined}]}.`  `{move,{atom,foo},{x,1}}.`  `...`  `{label,5}.`  `{test,is_eq_exact,{f,3},[{x,2},{integer,1}]}.`  `{test,is_tuple,{f,6},[{x,0}]}.`  `{test,test_arity,{f,6},[{x,0},3]}.`  `{get_tuple_element,{x,0},0,{x,1}}.`  `{get_tuple_element,{x,0},1,{x,2}}.`  `{test,is_eq_exact,{f,6},[{x,1},{atom,foo}]}.`  `...` |

Note line 11 and 12 do not test the middle value (`{x, 2}`) thus this clause will match.

**Solution:**  N/A, just learn the difference and don’t make assumptions about record values in a function clause.

### 7. `gen_server`, `trap_exit` and `terminate/2`

The `terminate/2` callback function in `gen_server` is suppose to be considered the opposite of the `init/1` function; Setup/Tear down. The truth however isn’t that the `terminate/2` *always* runs, there are some preconditions that we need to be aware of.

If anything happens inside the gen\_server itself or it issues a stop-tuple as a return then `terminate/2` will always be called, which is logical. However if it is under a supervisor the documentation says:

> If the gen\_server is part of a supervision tree and is ordered by its supervisor to terminate, this function will be called with Reason=shutdown if the following conditions apply:
>
> - the gen\_server has been set to trap exit signals, and
> - the shutdown strategy as defined in the supervisor’s child specification is an integer timeout value, not brutal\_kill.

So in other words (but still very similar ones): *If the the gen\_server is shut down and it is **not** trapping exits then the `terminate/2` function will **not** be called*. This might seem strange to some because one always expects the gen\_server to get a chance to “clean up” after itself but if you think about it it is logical; if a process gets an exit signal it should die with the same reason if it didn’t trap the signal. The gen\_server code has a case clause which explicitly checks for exit signals and only then allows `terminate/2` to be called.

The last statement wasn’t entirely true though. The documentation further states that:

> Even if the gen\_server is not part of a supervision tree, this function will be called if it receives an ‘EXIT’ message from its parent. Reason will be the same as in the ‘EXIT’ message.

Note: *from its parent*. In other words what was written in the previous section only applies to exit messages coming from the gen\_server’s *parent* process which means that (if the processes is supervised) the supervisor is the parent. This means that if you start a gen\_server process and that process in turn starts another process (which it links to) and that second process crashes then the first gen\_server process will *die without calling `terminate/2`*, unless of course it traps exits and in this case it will only receive a message (received by `handle_info/2`).

All according to predictable behaviour but can be overlooked so think twice when it comes to restart strategies and trapping exits. E.g:

In the following examples I will use this module:

|  |  |
| --- | --- |
|  | `-``module``(gensrv).`  `-compile(export_all).`  `start_link(``BoolFlag``) ->` `gen_server:start_link``(``?MODULE``,` `BoolFlag``, []).`  `init(``BoolFlag``) ->`  `process_flag(trap_exit,` `BoolFlag``),`  `{ok, undefined}.`  `handle_call({spawn_link,` `BoolFlag``}, _, _) ->`  `{ok,` `Pid``} =` `gen_server:start_link``(``?MODULE``,` `BoolFlag``, []),`  `{reply, {ok,` `Pid``},` `Pid``}.`  `handle_info({``'EXIT'``, _``Pid``, _``Reason``},` `St``) ->`  `{noreply,` `St``}.`  `terminate(_``Reason``, _``St``) ->`  `ok.` |

If we use this module to first start a gen\_server and then spawn a linked process under it we can observe this behaviour previously described. The below example shows a gen\_server spawning another process and finally being ordered to shut down by its parent (the shell). In both processes `terminate/2` is called.

|  |  |
| --- | --- |
|  | `> process_flag(trap_exit, true).`  `false`  `> {ok,` `P1``} =` `gensrv:start_link``(true).`  `{ok,<0.389.0>}`  `> {ok,` `P2``} =` `gen_server:call``(``P1``, {spawn_link, true}).`  `{ok,<0.391.0>}`  `> exit(``P1``, shutdown).`  `true`  `(<0.389.0>) call` `gensrv:terminate``(shutdown,<0.391.0>)`  `(<0.391.0>) call` `gensrv:terminate``(shutdown,undefined)`  `> flush().`  `Shell` `got {``'EXIT'``,<0.389.0>,shutdown}`  `ok` |

In this following scenario we start the two processes like before but the second one doesn’t trap exits (so we can kill it using reason `shutdown` from the shell).

|  |  |
| --- | --- |
|  | `> {ok,` `P1``} =` `gensrv:start_link``(true).`  `{ok,<0.407.0>}`  `> {ok,` `P2``} =` `gen_server:call``(``P1``, {spawn_link, false}).`  `{ok,<0.409.0>}`  `> exit(``P2``, shutdown).`  `(<0.407.0>) call` `gensrv:handle_info``({``'EXIT'``,<0.409.0>,shutdown},<0.409.0>)`  `true`  `> exit(``P1``, kill).`  `true`  `> flush().`  `Shell` `got {``'EXIT'``,<0.407.0>,killed}` |

Here we can see that even if we do trap exits the first process won’t shut down because it wasn’t the parent process that sent the exit signal, it was the process it spawned. Since the first process is still alive we kill it off at the end.

This third scenario shows the common misunderstanding about the `terminate/2` function. In this example we start one gen\_server which in turn starts another one (just like before) but this time the first one doesn’t trap exit but the second one does:

|  |  |
| --- | --- |
|  | `> {ok,` `P1``} =` `gensrv:start_link``(false).`  `{ok,<0.422.0>}`  `> {ok,` `P2``} =` `gen_server:call``(``P1``, {spawn_link, true}).`  `{ok,<0.424.0>}`  `> exit(``P1``, shutdown).`  `true`  `(<0.424.0>) call` `gensrv:terminate``(shutdown,undefined)`  `> flush().`  `Shell` `got {``'EXIT'``,<0.422.0>,shutdown}`  `ok` |

Even though both processes exit with `shutdown` they have different behaviour because one is trapping exists the other one isn’t. The first process receives an exit signal (reason `shutdown`) from its parent (the shell) but is not trapping exit and thus just exists with the same reason. The second process gets notified that its parent (the first process) exited with reason `shutdown` and since it is trapping exits it calls `terminate/2`.

This is all logical behaviour if you consider how processes and links work in general the only exception here are the rules added by the OTP behaviour of “shut down” signals which are really just a convention using the `shutdown` reason in an ‘EXIT’ message. Clever but can be confusing.

So in short; always remember:

- If a gen\_server process self terminates (I.e. it returns stop or an exit occurs inside the callbacks) then `terminate/2` will always be called
- A gen\_server process will not have its `terminate/2` callback called if it is not trapping exits
- If a gen\_server process is not trapping exits but its child processes are; then the child processes will have their `terminate/2` functions called

**Solution:**  Always spawn processes under a supervisor. If you don’t then make sure your own “top-level” process traps exits and cleans up after itself.

### 8. Trying to use `record_info/2` in runtime

This pitfall will appear as an error when you compile but can waste time if you don’t know the idea behind `record_info/2`. Since records don’t really exists then their fields don’t exist either, well… not their names anyway. Records only exist in code but not in runtime; as mentioned before the records are simply just replaced with something else (tuples and/or guards). Record fields (as seen in code) don’t exist either and are only references for the compiler to do the right thing. This means that if we specify the record `-record(foo, { bar, baz })` and later use `#foo{ bar = 1 }` then the compiler uses the identifier `bar` to know in which position in the tuple it should put the value `1` in it does not *know* the name `bar` in runtime.

This can be tricky in the beginning because one might think that the “functions” `record_info(fields, Record) -> [Field]` and `record_info(size, Record) -> Size` can be used in runtime when they actually can not. These functions are simply replaced by the parse transformation made before compilation. In order for them to work the record has to be defined somewhere in the module (or header file) and the record name has to be given explicitly.

This example will not work:

|  |  |
| --- | --- |
|  | `get_record_info(``RecordName``) -> record_info(fields,` `RecordName``).` |

because during compile time the record name is not known and therefore it can not expand to anything.

This example will work:

|  |  |
| --- | --- |
|  | `get_record_info() -> record_info(fields, foo).` |

because it will simply be replaced (according to the record definition) to:

|  |  |
| --- | --- |
|  | `get_record_info() -> [bar, baz].` |

This also means that you can not make “dynamic” records and get their field names, it has to be known at compile time.

**Solution:**  Understand that records are not “objects” or runtime constructs; they are only syntactic sugar.

### 9. Using `and`/`or` when you mean `andalso`/`orelse`

`and` and `or` evaluate both sides before determining an expression’s truth value while `andalso` and `orelse` evaluates the left side first and depending on its value decides if it evaluates the right side. These are called short-circuit expressions but actually are just acting like one would normally expect.

Example:

|  |  |
| --- | --- |
|  | `> true or exit(1).`  `** exception exit: 1`  `> true orelse exit(1).`  `true`  `> false and exit(1).`  `** exception exit: 1`  `> false andalso exit(1).`  `false` |

**Solution:**  Only `and`/`or` or if there is an absolute reason to otherwise use `andalso`/`orelse`

### Conclusion

Test more thoroughly and don’t make too many assumptions.

Peace.

*EDIT: Fixed a few mistakes and spelling errors.*

[About these ads](http://en.wordpress.com/about-these-ads/)
