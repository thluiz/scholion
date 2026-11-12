---
url: "https://dev.to/devengers/the-c-trilogy-how-dennis-ritchie-bjarne-stroustrup-and-anders-hejlsberg-built-the-modern-world-1onp"
captured_at: "2026-11-12T13:07:38+00:00"
title: "The C Trilogy: How Dennis Ritchie, Bjarne Stroustrup, and Anders Hejlsberg Built the Modern World 🏛️"
domain: "dev-to"
---

Almost every piece of software running on Earth today traces back to three people trying to solve the exact same headache: how to write large, complex programs without accidentally corrupting memory.

If you booted up a laptop today, opened a browser, played a 3D game, or swiped a credit card, you're running code shaped by **Dennis Ritchie**, **Bjarne Stroustrup**, and **Anders Hejlsberg**.

Together, they created the most famous trilogy in programming history: **C**, **C++**, and **C#**.

Let’s look at why these three languages exist, the corporate lawsuits that shaped them, and why all three are still running modern infrastructure today.

* * *

## [](#act-i-dennis-ritchies-machine-c-1972)Act I: Dennis Ritchie’s Machine (C, 1972)

```
      [ Dennis Ritchie @ Bell Labs ]
                    │
                    ▼
         "Trust the programmer."
                    │
            ┌───────┴───────┐
            ▼               ▼
      Raw Pointers     Linux & Windows
      Zero Safety      Runs on everything
```

Enter fullscreen mode Exit fullscreen mode

In the early 1970s at Bell Labs, writing an operating system meant writing raw Assembly.

If you wrote code for one machine and your lab brought in a new computer the following month, you had to rewrite nearly every line from scratch.

Dennis Ritchie wanted something practical: a language that read like structured code, but mapped directly to hardware registers.

So he built **C**.

[![Dennis Ritchie at Bell Labs](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2F5sp7n70ln7bl85pk79qn.jpg)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2F5sp7n70ln7bl85pk79qn.jpg)

### [](#the-rule-trust-the-programmer)The Rule: _"Trust the Programmer"_

C has one founding assumption: **you know what you are doing.**

If you tell C to take a block of memory and overwrite byte 4,000, it won't check if that buffer belongs to you. It won’t check if you're about to panic the kernel. It just executes the instruction.  

```
#include <stdio.h>
#include <stdlib.h>

// Act I: Raw Power. You ask for memory, you clean it up.
int main() {
    int count = 3;

    // Grabbing raw bytes from RAM
    int *scores = (int *)malloc(count * sizeof(int));
    if (scores == NULL) return 1;

    scores[0] = 95;
    scores[1] = 88;
    scores[2] = 100;

    for (int i = 0; i < count; i++) {
        printf("Score %d: %d\n", i + 1, scores[i]);
    }

    // Forget this line? That RAM is leaked until the process exits.
    free(scores);
    return 0;
}
```

Enter fullscreen mode Exit fullscreen mode

### [](#the-win-amp-the-pain)The Win & The Pain

Because C compiles almost 1-to-1 to CPU instructions, it became the foundation of modern computing. The Linux kernel, Windows, macOS, Git, PostgreSQL, and Python's C runtime all sit on top of C.

*   **The Win:** Pure execution speed. Zero runtime bloat. Runs on virtually any processor ever manufactured.
*   **The Pain:** Forget to free your memory? **Memory leak.** Read one byte past the array? **Segmentation fault.**

[![Segfault Meme](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fp464aoyx3ylqczco9g7n.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fp464aoyx3ylqczco9g7n.gif)

* * *

## [](#act-ii-bjarne-stroustrups-titan-c-1985)Act II: Bjarne Stroustrup’s Titan (C++, 1985)

```
        [ Bjarne Stroustrup @ Bell Labs ]
                       │
                       ▼
    "You don't pay for what you don't use."
                       │
            ┌──────────┴──────────┐
            ▼                     ▼
       Classes & RAII        Unreal Engine
     Zero-Cost Abstractions  AAA Games & Browsers
```

Enter fullscreen mode Exit fullscreen mode

By the mid-80s, software had outgrown C.

Writing a distributed simulation, a network switcher, or a graphical desktop application in procedural C meant managing thousands of disconnected structs and function pointers. Codebases were getting too large for loose pointers.

Bjarne Stroustrup (also at Bell Labs) liked the object-oriented structure of Simula, but needed the speed of C.

He didn't want to choose between abstraction and raw speed, so he built **C with Classes**, which became **C++**.

[![Bjarne Stroustrup](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fmwy6e8drgzo9mqyuwbwu.jpg)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fmwy6e8drgzo9mqyuwbwu.jpg)

### [](#the-rule-zerocost-abstractions)The Rule: _"Zero-Cost Abstractions"_

Stroustrup stuck to a strict design principle:

> _"What you don't use, you don't pay for. And further: What you do use, you couldn't hand code any better."_

C++ introduced classes, inheritance, operator overloading, and templates. Critically, it avoided adding a background runtime or garbage collector.

Instead, C++ introduced **RAII** (Resource Acquisition Is Initialization). The idea is straightforward: **objects own their resources, and when an object leaves its scope `{ }`, its destructor fires and cleans up the memory instantly.**  

```
#include <iostream>
#include <vector>

// Act II: Zero-Cost RAII.
// No malloc. No free. No manual pointer bookkeeping.
int main() {
    // std::vector allocates its internal buffer on the heap automatically
    std::vector<int> scores = {95, 88, 100};

    for (size_t i = 0; i < scores.size(); ++i) {
        std::cout << "Score " << (i + 1) << ": " << scores[i] << "\n";
    }

    // No free() needed. 
    // When 'scores' leaves this closing brace, its destructor cleans up the memory.
    return 0;
}
```

Enter fullscreen mode Exit fullscreen mode

### [](#the-win-amp-the-pain)The Win & The Pain

C++ became the industry standard wherever **every millisecond counts**: AAA game engines (Unreal Engine), browser rendering engines (Chromium, WebKit), high-frequency financial trading, and aerospace software.

*   **The Win:** High-level object-oriented patterns with bare-metal C performance.
*   **The Pain:** The language is enormous. Between templates, multiple inheritance, and move semantics, compiler error messages can look like an ancient spellbook.

[![Confused Reading Code](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2F6s87ev9ir6bjqcx9i4oq.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2F6s87ev9ir6bjqcx9i4oq.gif)

* * *

## [](#act-iii-anders-hejlsbergs-renaissance-c-2000)Act III: Anders Hejlsberg’s Renaissance (C#, 2000)

```
        [ Anders Hejlsberg @ Microsoft ]
                       │
                       ▼
      "Make the developer happy and safe."
                       │
            ┌──────────┴──────────┐
            ▼                     ▼
      Managed Runtime (CLR)  Modern .NET & Cloud
      Garbage Collection     Span<T> & High Perf
```

Enter fullscreen mode Exit fullscreen mode

By the late 90s, Microsoft had a Java problem.

Microsoft had been distributing their own modified implementation called **Visual J++**, adding Windows-specific hooks. Sun Microsystems sued them for breach of contract.

Following the lawsuit, Microsoft settled, walked away from Java, and decided to build their own language from scratch.

They tapped **Anders Hejlsberg**—the compiler engineer behind Turbo Pascal and Delphi—to lead "Project COOL" (_C-like Object Oriented Language_).

In 2000, that project launched as **C#**.

[![Anders Hejlsberg](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fhi0vmjlk4qobzez2djgz.jpg)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fhi0vmjlk4qobzez2djgz.jpg)

### [](#the-rule-developer-productivity-amp-safety)The Rule: _"Developer Productivity & Safety"_

Anders focused on cutting down developer friction: let the runtime handle memory bookkeeping so engineers can focus on shipping features.

C# paired a clean C-style syntax with the **CLR (Common Language Runtime)** and an automated **Garbage Collector (GC)**. Memory is allocated on demand, and unused objects are swept up in the background.

With modern C# top-level statements, the classic `class Program` and `static void Main` ceremony is gone:  

```
// Act III: Pure Productivity (Modern C# Top-Level Statements)
// No boilerplate class wrappers. Just write code.

var scores = new List<int> { 95, 88, 100 };

for (int i = 0; i < scores.Count; i++)
{
    Console.WriteLine($"Score {i + 1}: {scores[i]}");
}

// Zero memory bookkeeping. The Garbage Collector handles cleanup.
```

Enter fullscreen mode Exit fullscreen mode

### [](#dropping-the-guardrails-when-speed-matters)Dropping the Guardrails When Speed Matters

Plenty of devs still write off C# as a slow enterprise language, mostly because they haven't looked under the hood lately. When you actually need raw speed, modern C# lets you drop the guardrails:

1.  **The `unsafe` Keyword:** Need direct pointer arithmetic? You can drop into an `unsafe` block and manipulate memory addresses directly like you're writing C.
2.  **`Span<T>` and `Memory<T>`:** Modern C# lets you slice arrays, strings, and native memory buffers without allocating a single byte on the heap.

That combination is a big reason modern .NET regularly trades blows with Go and Rust on high-throughput TechEmpower web benchmarks.

### [](#the-win-amp-the-pain)The Win & The Pain

Between modern open-source **.NET** and the ubiquity of the **Unity Game Engine**, C# has evolved into one of the most practical general-purpose languages around.

*   **The Win:** Fast to write, memory-safe by default, and backed by a modern cross-platform runtime.
*   **The Pain:** Small runtime memory footprint, JIT compilation warm-up on cold starts, and occasional GC latency if you allocate millions of temporary objects carelessly.

## [](#)![Jeremiah Johnson Nod](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fwf57tryli5u538qt1t55.gif)

## [](#the-quick-comparison)The Quick Comparison

Here is how the three stack up side-by-side:

Feature

C (1972)

C++ (1985)

C# (2000)

**Creator**

Dennis Ritchie

Bjarne Stroustrup

Anders Hejlsberg

**Memory**

Manual (`malloc`/`free`)

Automatic via RAII (`std::vector`, smart pointers)

Managed by Garbage Collector (+ `Span<T>` & `unsafe` pointers)

**Safety**

Low (easy to crash)

High if using modern RAII (disastrous if not)

Very High (memory-safe by default)

**Speed**

🚀 Pure hardware speed

🚀 Pure hardware speed

⚡ Very fast (Modern .NET is heavily optimized)

**Best For**

Operating systems, drivers, tiny chips

Game engines (Unreal), browsers, trading

Web APIs, enterprise cloud, Unity games

* * *

## [](#why-theyre-all-still-running-the-world)Why They’re All Still Running the World

People have been forecasting the demise of the C family for decades:

*   _"Rust will replace C and C++."_
*   _"Go will replace C#."_
*   _"Python will replace everything."_

And yet, in 2026:

*   **C** still runs the kernels of 3 billion Android phones and the vast majority of cloud hypervisors.
*   **C++** powers Unreal Engine 5, NVIDIA's compute stacks, and local LLM runtimes (`llama.cpp`).
*   **C#** powers millions of commercial web backends and remains the default engine for indie game development via Unity.

Dennis Ritchie gave us the iron.

Bjarne Stroustrup gave us the abstractions.

Anders Hejlsberg gave us the developer ergonomics.

Fifty years on, they aren't even competing anymore—each one just claimed a different layer of the stack.

* * *

### [](#over-to-you)Over to You:

If you had to build a brand new project tomorrow and could only pick **one** of these three, which one are you grabbing: **C**, **C++**, or **C#**?

Drop your pick in the comments below! 👇
