---
title: "Stack in C# - Code Maze"
date: '2022-06-02T09:53:06-03:00'
category: webclip
summary: 'The article explains Stack in C# as a LIFO collection, shows the non-generic and generic constructors, and covers Count, Push, Peek, Pop, Clear, plus thread-safe options.'
tags: ["stack", "lifo", "generics", "thread-safety"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Stack in C# - Code Maze"
    url: "https://code-maze.com/stack-csharp/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-06/code-maze-com--stack-in-csharp-code-maze.md"
    kind: repo
---

The article presents Stack in C# as a collection that follows the last-in-first-out rule. It contrasts Stack with FIFO behavior, explains push and pop as the basic operations, and notes that Stack is useful for cases like undo-redo histories.

## Reading notes

- Stack in C# keeps the last added element at the top, so it is used when data must follow LIFO.
- The non-generic Stack can store different types, but it needs casting between object and the real type.
- Stack<T> is the generic version and stores items of one type from System.Collections.Generic.
- The non-generic Stack has three constructors: empty, from ICollection, and with an initial capacity.
- The generic Stack<T> also has three constructors: empty, from IEnumerable<T>, and with an initial capacity.
- Count returns how many elements are stored in the stack.
- Push adds an item, and when the stack reaches capacity, its capacity doubles by default.
- Peek returns the top element without removing it.
- Peek on an empty stack throws InvalidOperationException, while TryPeek can return false safely in the generic case.
- Pop removes and returns the top element.
- Pop on an empty stack throws InvalidOperationException, while TryPop can return false safely in the generic case.
- Clear removes all elements and leaves the stack empty.
- Non-generic Stack can be wrapped with Stack.Synchronized to make access thread-safe.
- For generic stacks, the thread-safe option is ConcurrentStack<T>.
