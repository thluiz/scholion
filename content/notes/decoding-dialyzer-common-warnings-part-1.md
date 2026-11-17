---
title: "Decoding Dialyzer - Part 1"
date: '2026-11-17T15:00:51+00:00'
category: webclip
summary: 'Explains two common Dialyzer warnings (`no_return` and `call`), how they arise from a simple Elixir bug, what success typings vs contracts mean, and how to fix the issue.'
tags: ["elixir", "dialyzer", "typespecs"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Decoding Dialyzer - Part 1"
    url: "https://devonestes.com/decoding-dialyzer"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/devonestes-com--decoding-dialyzer-common-warnings-part-1.md"
    kind: repo
---

Dialyzer can be hard to interpret but is useful for finding bugs and incorrect typespecs. The text walks through two of the most common and important warnings using a small Elixir example with a simple bug that triggers multiple Dialyzer messages. It contrasts the clearer `dialyxir` 1.0.0-style formatting with the older Erlang-style output.

The example shows a function that calls `concat/2` with arguments in the wrong order. This leads Dialyzer to report that a function never returns and that a particular function call will always fail. The explanation covers why literals let Dialyzer prove the failure, how `no_return` and `call` warnings are related, and how success typings differ from user-written contracts. The fix is to call the function with arguments that match its spec.

## Reading notes

- Dialyzer is described as tricky to understand but effective at spotting bugs and inaccurate typespecs.
- The goal is to explain several common Dialyzer warnings, their causes, and ways to resolve them.
- The author uses `dialyxir` 1.0.0-rc4 and shows both new Elixir-formatted and old Erlang-formatted warnings.
- The new `dialyxir` 1.0.0 formatting is said to be much more helpful than the original.
- A small Elixir module `Test` is introduced with `concat/2` and `call_concat/0` and a typespec for each.
- In the example, `concat/2` expects an `atom()` and a `String.t()`, but `call_concat/0` calls it as `concat("string", :atom)`.
- That code contains one obvious bug (argument order/type mismatch), yet Dialyzer emits two warnings.
- The author notes that one bug frequently causes multiple Dialyzer warnings.
- Grouping warnings by related cause is suggested as more effective than tackling each in isolation.
- The first warning discussed is `no_return`, presented with its new-style formatted message.
- The message says `Function call_concat/0 has no local return`, meaning the function never returns successfully.
- The explanation states this implies any call to `call_concat/0` will always raise an exception.
- Two situations that cause this are listed: functions that always raise on purpose, and ones that always raise unintentionally.
- If a function intentionally always raises, the warning can be resolved by annotating its spec with `:: no_return()`.
- The second situation is where Dialyzer is most helpful because it indicates a serious bug.
- Dialyzer can be certain about this bug in the initial example because it knows the values are a string and an atom literal.
- A second version of the code changes `call_concat/0` to `call_concat/2` with typed arguments instead of literals.
- In that second version, Dialyzer no longer emits a `no_return` warning.
- Dialyzer instead produces a different warning for that variation but cannot prove a guaranteed exception.
- The text explains that Dialyzer only issues `no_return` when it can determine argument types with full confidence, often via literals.
- The `no_return` warning alone does not clearly indicate where the underlying bug is located.
- The next warning, `call`, helps locate the problematic function invocation.
- The `call` warning is shown for the original code on the line calling `Test.concat("string", :atom)`.
- The message states this call will never return, and displays the success typing and the contract for `concat/2`.
- New formatting is presented as much clearer than the old, more cryptic Erlang-style representation.
- The warning explains that calling `concat/2` with the given arguments will always fail.
- It identifies the call as the likely source of the bug, even though earlier `no_return` warned about a different function.
- The text notes there is no explicit link between the `no_return` and `call` warnings in the output.
- The `no_return` warning references `call_concat`, while the `call` warning references `concat`.
- At a glance the two warnings appear separate, yet they arise from the same underlying issue.
- A practical tip is given: Dialyzer warnings are grouped by file and ordered by line number.
- If a `no_return` warning appears and a nearby `call` warning follows in the same file, they are likely related.
- The `call` warning states the attempted use of `concat/2` "is never going to work".
- The text explains the difference between success typing and contract for a function.
- Success typing is described as the minimum requirements Dialyzer has inferred to avoid failure.
- A contract is described as a programmer-written requirement for using the function.
- The author notes humans often make mistakes in contracts, and Dialyzer’s inference may be less specific.
- The suggestion is to choose whichever of the two (success typing or contract) is more strict when deciding correct usage.
- In the example, `String.t()` is more strict than `binary`, so `concat` should be called with strings, not arbitrary binaries.
- To resolve the warning, the function must be used according to its spec.
- The fix in this case is to change `concat("string", :atom)` to `concat(:atom, "string")` so types and order match.
- After changing the call, rerunning Dialyzer results in no more warnings.
- The resolution confirms that the bug has been found and fixed through interpreting the two warning types together.
