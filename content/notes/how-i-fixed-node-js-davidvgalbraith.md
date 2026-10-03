---
title: "How I fixed Node.js"
date: '2016-02-07T23:05:58-03:00'
category: webclip
summary: 'The author tracks a ChildProcess memory leak to stdout not closing after read() sets _consuming, then fixes flushStdio so resume() runs and the process can close.'
tags: ["node-js", "memory-leak", "childprocess", "bug-fix"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How I fixed Node.js - davidvgalbraith"
    url: "http://davidvgalbraith.com/how-i-fixed-node-js/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-02/davidvgalbraith-com--how-i-fixed-node-js-davidvgalbraith.md"
    kind: repo
---

The post follows a first open-source contribution in node.js. The author starts from a ChildProcess memory leak, traces how spawn, read, kill, maybeClose, and flushStdio interact, and finds that calling read() on stdout sets _consuming in a way that prevents stdout from closing.

## Reading notes

- The bug appears when a child process is spawned, its stdout is read, and the process is killed, because ChildProcess objects are not being freed by the garbage collector.
- The reproducing script uses weak.js to track garbage collection and shows child_processes_in_memory steadily increasing.
- The author investigates ChildProcess.kill(), the constructor, and the onexit handler, then focuses on maybeClose and the _closesGot and _closesNeeded counters.
- ChildProcess closes only after the shell command finishes and stdout and stderr emit close events.
- Tracing emitted events shows that some leaking ChildProcess objects never emit close events.
- Removing the call to p.stdout.read() makes the close events fire consistently.
- In net.js, Socket.prototype.read sets this._consuming to true the first time it is called with a nonzero argument, and p.stdout.read() does that.
- In flushStdio, stream.resume() is skipped when stream._consuming is set, so stdout is not resumed after exit.
- The fix is to remove stream._consuming from the condition in flushStdio so resume() runs and the stream can close.
- The author adds a test, changes it from yes to echo for Windows compatibility, and gets the pull request approved.
