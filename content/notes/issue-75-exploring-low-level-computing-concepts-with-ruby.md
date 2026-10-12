---
title: "Issue 7.5: Exploring low-level computing concepts with Ruby"
date: '2014-06-19T11:14:56-03:00'
category: webclip
summary: 'The article builds a stripped-down 6502 simulator in JRuby to run Snake6502, explaining machine code, memory, stack behavior, memory-mapped I/O, registers, flags, addressing modes, and the instruction loop.'
tags: ["ruby", "6502", "computer-architecture", "emulation"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Issue 7.5: Exploring low-level computing concepts with Ruby - Practicing Ruby"
    url: "https://practicingruby.com/articles/low-level-computing?u=c84864ec01"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-06/practicingruby-com--issue-75-exploring-low-level-computing-concepts-with-ruby.md"
    kind: repo
---

The article shows how to build a small 6502 simulator in JRuby that is just complete enough to run Snake6502. It uses the game as a guide to explain machine code, disassembly, memory as a shared store for code and data, and the role of the program counter and stack in control flow.

It then adds memory-mapped I/O for random numbers, keyboard input, and pixel output, and introduces a CPU model with registers and flags. From there, it explains addressing modes, config-driven opcode lookup, and a simulator loop that reads bytes from a ROM and executes the matching instruction definitions.

## Reading notes

- The issue is directly inspired by Nick Morgan’s Easy 6502 tutorial, and the Snake6502 bytecode is used as the concrete example throughout.
- Machine code is presented as a stream of bytes that can be disassembled into assembly instructions such as JSR, LDA, STA, BEQ, and RTS.
- Addressing modes are treated as different ways of turning an operand into an effective address, so instruction behavior can be defined after the address is computed.
- The storage model uses a 16-bit address space with 8-bit values, a program counter starting at $0600, and stack storage between $0100 and $01ff.
- Jump, branch, jsr, and rts behavior are built on top of the program counter and stack.
- Memory-mapped I/O handles reads from $fe as random bytes, reads from $ff as the last key pressed, and writes to $0200-$05ff as screen pixels.
- The CPU model tracks A, X, Y, and P, with carry, negative, and zero flags implemented for the Snake6502 game.
- CMP and BEQ are explained as a combination of flag setting and conditional branching.
- The article lists the addressing modes used by Snake6502, including implicit, relative, immediate, zero page, zero page indexed by X, absolute, indexed indirect, and indirect indexed.
- A configuration object loads opcode mappings from CSV and instruction definitions from a DSL file, and the simulator executes operations by looking up the opcode, computing the effective address, and evaluating the matching definition.
