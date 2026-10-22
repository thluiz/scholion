---
title: "A brief introduction to BEAM"
date: '2020-10-22T10:02:39-03:00'
category: webclip
summary: 'This primer explains BEAM as the virtual machine that executes Erlang code, distinguishes it from ERTS, and shows how registers, calls, tuples, exceptions, and receive are represented in BEAM instructions.'
tags: ["beam", "erlang", "virtual-machine", "jit"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "A brief introduction to BEAM – A Blog from the Erlang/OTP team – The Erlang/OTP team at Ericsson, the implementors and maintainers of Erlang/OTP."
    url: "http://blog.erlang.org/a-brief-BEAM-primer/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-10/blog-erlang-org--a-brief-introduction-to-beam.md"
    kind: repo
---

This primer explains BEAM as the virtual machine that executes Erlang code in ERTS. It distinguishes BEAM from ERTS, then uses small examples to show how BEAM instructions represent registers, function calls, data creation, exceptions, and receive loops.

## Reading notes

- BEAM is the virtual machine that executes user code in the Erlang Runtime System, and it should not be confused with ERTS itself.
- BEAM has no notion of processes, ports, or ETS tables; it only executes instructions.
- It is a register machine with two main kinds of registers, X and Y.
- X registers are used for temporary data and for passing arguments between functions.
- Y registers belong to a stack frame and keep values alive across calls.
- Control flow uses test instructions and fail labels such as {f,Index}.
- Function arguments are passed left to right in X registers, and results return in {x,0}.
- The examples show tail recursion compiled with call_only and body recursion compiled with allocate, call, deallocate, and return.
- The live register count on an instruction tells the garbage collector which X registers must be preserved.
- After a call, only {x,0} is preserved, so other X registers are not safe to use.
- Tuples are created with test_heap and put_tuple2, while other compound terms may use special instructions that can trigger garbage collection.
- The exception example shows try, try_end, try_case, and rethrowing with bif,raise.
- receive is described as the one construct that may loop until a matching message arrives, using loop_rec, loop_rec_end, wait, and remove_message.
- The post ends by pointing to genop.tab for brief descriptions of BEAM instructions.
