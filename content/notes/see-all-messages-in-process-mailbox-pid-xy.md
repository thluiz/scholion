---
title: "See all messages in process's mailbox with pid XY"
date: '2015-05-25T09:22:50-03:00'
category: webclip
summary: 'The thread shows how to inspect a process mailbox with :erlang.process_info(:messages), notes that Observer can display a queue snapshot, and warns that copying messages can be expensive.'
tags: ["erlang", "elixir", "mailbox", "observer"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "[elixir-talk:8497] See all messages in process's mailbox with pid XY - th.luiz@gmail.com - Gmail"
    url: "https://mail.google.com/mail/u/0/?pli=1#label/Listas%2F05+-+Principais/14d63158a40733c0"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-05/mail-google-com--see-all-messages-in-process-mailbox-pid-xy.md"
    kind: repo
---

The thread answers that a process mailbox can be inspected with :erlang.process_info(pid, :messages). It also mentions the Observer application for viewing a message queue snapshot in a GUI, and Erlang tracing tools for watching messages sent to or from processes.

## Reading notes

- :erlang.process_info(pid, :messages) returns the current messages in a process mailbox.
- The example sends :foobar to a process and inspects the mailbox from another process.
- :observer.start can open Observer, where the Processes tab shows a snapshot of the queue.
- :sys, :dbg, and :erlang.trace/3 can be used to trace message flow dynamically.
- Robert Virding warns that reading another process's mailbox can be costly because the messages are copied.
- He suggests checking Process.info(pid, :message_queue_len) first.
