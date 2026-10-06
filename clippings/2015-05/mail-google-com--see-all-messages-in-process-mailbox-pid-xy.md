---
url: "https://mail.google.com/mail/u/0/?pli=1#label/Listas%2F05+-+Principais/14d63158a40733c0"
captured_at: "2015-05-25T09:22:50-03:00"
title: "[elixir-talk:8497] See all messages in process's mailbox with pid XY - th.luiz@gmail.com - Gmail"
domain: "mail-google-com"
---

[elixir-talk:8497] See all messages in process's mailbox with pid XY

Participantes: tomaz.zlender@gmail.com, elixir-lang-talk@googlegroups.com, sasa.juric@gmail.com, rvirding@gmail.com

[Abrir conversação no Gmail](https://mail.google.com/mail/u/0/?pli=1#label/Listas%2F05+-+Principais/14d63158a40733c0)

tomaz.zlender@gmail.comSun, May 17, 2015 at 3:14 PM

Is it possible to see all messages that are in mailbox of a process with a given pid? I know it is possible to use flush in console process. But flush removes all messages and I just want to see them and not just for console mailbox, but for any mailbox I know.

Saša JurićSun, May 17, 2015 at 3:24 PM

You can use :erlang.process\_info

E.g.:

iex(1)> shell\_process = self

iex(2)> spawn(fn ->

...(2)>   send(shell\_process, :foobar)

...(2)>   :erlang.process\_info(shell\_process, :messages) |> IO.inspect

...(2)> end)

{:messages, [:foobar]}

You can have a GUI interface via observer application. Just start it from the shell with :observer.start, head to Processes tab, find the target process, double click it, and in messages you should see a snapshot of the message queue.

It is also possible to use Erlang's tracing via :sys, :dbg module, and :erlang.trace/3 function to dynamically start traces for various events. Among other things, you can trace messages sent to or from particular process(es).  
  
On Sunday, May 17, 2015 at 8:14:22 PM UTC+2, [tomaz....@gmail.com](mailto:tomaz....@gmail.com) wrote:
> Is it possible to see all messages that are in mailbox of a process with a given pid? I know it is possible to use flush in console process. But flush removes all messages and I just want to see them and not just for console mailbox, but for any mailbox I know.

--   
You received this message because you are subscribed to the Google Groups "elixir-lang-talk" group.  
To unsubscribe from this group and stop receiving emails from it, send an email to [elixir-lang-talk+unsubscribe@googlegroups.com](mailto:elixir-lang-talk+unsubscribe@googlegroups.com).  
To view this discussion on the web visit [https://groups.google.com/d/msgid/elixir-lang-talk/bcfe033f-e532-4c33-ac5e-87f72d977c0b%40googlegroups.com](https://groups.google.com/d/msgid/elixir-lang-talk/bcfe033f-e532-4c33-ac5e-87f72d977c0b%40googlegroups.com?utm_medium=email&utm_source=footer).

Tomaž ŽlenderSun, May 17, 2015 at 4:05 PM

Awesome! Thank you :)

On Sun, May 17, 2015 at 8:24 PM, Saša Jurić <[sasa.juric@gmail.com](mailto:sasa.juric@gmail.com)> wrote:  
> You can use :erlang.process\_info
>
> E.g.:
>
> iex(1)> shell\_process = self
>
> iex(2)> spawn(fn ->
>
> ...(2)>   send(shell\_process, :foobar)
>
> ...(2)>   :erlang.process\_info(shell\_process, :messages) |> IO.inspect
>
> ...(2)> end)
>
> {:messages, [:foobar]}
>
> You can have a GUI interface via observer application. Just start it from the shell with :observer.start, head to Processes tab, find the target process, double click it, and in messages you should see a snapshot of the message queue.
>
> It is also possible to use Erlang's tracing via :sys, :dbg module, and :erlang.trace/3 function to dynamically start traces for various events. Among other things, you can trace messages sent to or from particular process(es).  
>   
> On Sunday, May 17, 2015 at 8:14:22 PM UTC+2, [tomaz....@gmail.com](mailto:tomaz....@gmail.com) wrote:
> > Is it possible to see all messages that are in mailbox of a process with a given pid? I know it is possible to use flush in console process. But flush removes all messages and I just want to see them and not just for console mailbox, but for any mailbox I know.
>
> --   
> You received this message because you are subscribed to a topic in the Google Groups "elixir-lang-talk" group.  
> To unsubscribe from this topic, visit <https://groups.google.com/d/topic/elixir-lang-talk/sF84esrPSoc/unsubscribe>.  
> To unsubscribe from this group and all its topics, send an email to [elixir-lang-talk+unsubscribe@googlegroups.com](mailto:elixir-lang-talk+unsubscribe@googlegroups.com).  
> To view this discussion on the web visit [https://groups.google.com/d/msgid/elixir-lang-talk/bcfe033f-e532-4c33-ac5e-87f72d977c0b%40googlegroups.com](https://groups.google.com/d/msgid/elixir-lang-talk/bcfe033f-e532-4c33-ac5e-87f72d977c0b%40googlegroups.com?utm_medium=email&utm_source=footer).
>
> For more options, visit <https://groups.google.com/d/optout>.

--   
You received this message because you are subscribed to the Google Groups "elixir-lang-talk" group.  
To unsubscribe from this group and stop receiving emails from it, send an email to [elixir-lang-talk+unsubscribe@googlegroups.com](mailto:elixir-lang-talk+unsubscribe@googlegroups.com).  
To view this discussion on the web visit [https://groups.google.com/d/msgid/elixir-lang-talk/CAFDi8Ga-c%3DtxFJ%3DWOArUmk8YOdCGgNHKciH1pfQ5YVS8GHg2ZQ%40mail.gmail.com](https://groups.google.com/d/msgid/elixir-lang-talk/CAFDi8Ga-c%3DtxFJ%3DWOArUmk8YOdCGgNHKciH1pfQ5YVS8GHg2ZQ%40mail.gmail.com?utm_medium=email&utm_source=footer).

Robert VirdingSun, May 17, 2015 at 6:51 PM

You should be aware that getting all the messages in another process's mailbox can be a very costly operation. All the messages are copied from the other process to your process. Processes don't share data. To be safe it might be better to first check the length of the message queue using Process.info(pid, :message\_queue\_len).  
  
Robert  
  
On Sunday, May 17, 2015 at 9:05:56 PM UTC+2, Tomaž Žlender wrote:
> Awesome! Thank you :)
>
> On Sun, May 17, 2015 at 8:24 PM, Saša Jurić <sasa....@gmail.com> wrote:  
> > You can use :erlang.process\_info
> >
> > E.g.:
> >
> > iex(1)> shell\_process = self
> >
> > iex(2)> spawn(fn ->
> >
> > ...(2)>   send(shell\_process, :foobar)
> >
> > ...(2)>   :erlang.process\_info(shell\_process, :messages) |> IO.inspect
> >
> > ...(2)> end)
> >
> > {:messages, [:foobar]}
> >
> > You can have a GUI interface via observer application. Just start it from the shell with :observer.start, head to Processes tab, find the target process, double click it, and in messages you should see a snapshot of the message queue.
> >
> > It is also possible to use Erlang's tracing via :sys, :dbg module, and :erlang.trace/3 function to dynamically start traces for various events. Among other things, you can trace messages sent to or from particular process(es).  
> >   
> > On Sunday, May 17, 2015 at 8:14:22 PM UTC+2, tomaz....@gmail.com wrote:
> > > Is it possible to see all messages that are in mailbox of a process with a given pid? I know it is possible to use flush in console process. But flush removes all messages and I just want to see them and not just for console mailbox, but for any mailbox I know.
> >
> > --   
> > You received this message because you are subscribed to a topic in the Google Groups "elixir-lang-talk" group.  
> > To unsubscribe from this topic, visit <https://groups.google.com/d/topic/elixir-lang-talk/sF84esrPSoc/unsubscribe>.  
> > To unsubscribe from this group and all its topics, send an email to elixir-lang-ta...@googlegroups.com.  
> > To view this discussion on the web visit [https://groups.google.com/d/msgid/elixir-lang-talk/bcfe033f-e532-4c33-ac5e-87f72d977c0b%40googlegroups.com](https://groups.google.com/d/msgid/elixir-lang-talk/bcfe033f-e532-4c33-ac5e-87f72d977c0b%40googlegroups.com?utm_medium=email&utm_source=footer).
> >
> > For more options, visit <https://groups.google.com/d/optout>.

--   
You received this message because you are subscribed to the Google Groups "elixir-lang-talk" group.  
To unsubscribe from this group and stop receiving emails from it, send an email to [elixir-lang-talk+unsubscribe@googlegroups.com](mailto:elixir-lang-talk+unsubscribe@googlegroups.com).  
To view this discussion on the web visit [https://groups.google.com/d/msgid/elixir-lang-talk/38e08b19-53ee-4b3e-bc9e-791a3ed2d5db%40googlegroups.com](https://groups.google.com/d/msgid/elixir-lang-talk/38e08b19-53ee-4b3e-bc9e-791a3ed2d5db%40googlegroups.com?utm_medium=email&utm_source=footer).
