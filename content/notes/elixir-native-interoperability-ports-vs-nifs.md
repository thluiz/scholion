---
title: "Elixir Native Interoperability – Ports vs. NIFs"
date: '2015-05-07T13:16:59-03:00'
category: webclip
summary: 'The page compares two Elixir/Erlang interoperability mechanisms for serial device access. NIFs are faster and simpler but can crash the VM; ports are safer and more flexible but use awkward STDIN/STDOUT messaging.'
tags: ["elixir", "erlang", "interoperability", "nifs"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Elixir Native Interoperability – Ports vs. NIFs"
    url: "http://spin.atomicobject.com/2015/03/16/elixir-native-interoperability-ports-vs-nifs/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-05/spin-atomicobject-com--elixir-native-interoperability-ports-vs-nifs.md"
    kind: repo
---

The page compares ports and NIFs as two simple ways to connect Elixir to native code on the Erlang VM. It uses serial device access as the example and frames the choice around speed, safety, and how much native complexity leaks into Elixir code.

NIFs load a dynamic library and let Elixir call native functions directly. They are fast, simple, and easy to debug, but a crash in the C library crashes the whole VM and the native code can pull imperative details into functional code. Ports run an external native process over STDIN and STDOUT, with message passing between the Elixir process and that process. They are safer, easier to trap for errors, and more flexible, but communication is awkward. The page also shows how Mix can be extended to build C code and how the examples use Arduino sketches and C helpers for parsing commands and serial I/O.

## Reading notes

- NIFs are presented as native functions loaded from a dynamic library and called like ordinary Elixir functions.
- The listed NIF benefits are fast implementation, no context switch, and simple debugging.
- The listed NIF drawbacks are safety risk, a NIF-specific C library, and native imperative code leaking into Elixir code.
- The page says a crash in the C library crashes the entire Erlang VM.
- Ports communicate with an external native process over STDIN and STDOUT.
- A port creates a connected process that uses message passing with the external native process.
- The listed port benefits are safety, error trapping, flexible communication, and no need for external Erlang or Elixir specific libraries.
- The listed port drawback is awkward STDIN and STDOUT communication.
- The examples use two Arduino sketches, one sending random text blocks and another acting as a loopback.
- The page shows integrating a Makefile into Mix so native code can be built and cleaned alongside Elixir code.
- The port example opens the compiled C program in priv_dir and sends commands with Port.command/2.
- The port example uses packet mode with a 2 byte length indicator.
- The NIF example loads the C library on module load with :erlang.load_nif/2.
- The NIF example wraps public functions so the data is converted into the types expected by the C code.
- The C NIF code uses erl_nif.h to convert between ERL_NIF_TERM values and C data types.
- The page notes that enif_send could send messages to an Elixir pid, but doing so would require threading and add safety concerns.
