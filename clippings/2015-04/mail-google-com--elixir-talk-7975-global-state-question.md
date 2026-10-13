---
url: "https://mail.google.com/mail/u/0/?pli=1#inbox/14ca02f0d6fe1860"
captured_at: "2015-04-10T10:04:44-03:00"
title: "[elixir-talk:7975] A question about global state - th.luiz@gmail.com - Gmail"
domain: "mail-google-com"
---

[elixir-talk:7975] A question about global state

Participantes: louis@lpil.uk, elixir-lang-talk@googlegroups.com, ismaelga@gmail.com, adam@apathydrive.com, rvirding@gmail.com, jose.valim@plataformatec.com.br

[Abrir conversação no Gmail](https://mail.google.com/mail/u/0/?pli=1#inbox/14ca02f0d6fe1860)

Louis PilfoldThu, Apr 9, 2015 at 6:55 PM

Hello!  
  
I've found myself getting slightly confused by state in this immutable  
world again :P  
  
I'm writing a small library for colouring strings to be printed to the  
terminal. One thing that I wish to do is to check some environmental  
variables on program load (or the first time a function is called) in  
order to determine the capabilities of the terminal.  
  
I'd like to not perform this check each time, so I would like to set a  
flag somewhere that would be read in future. In Ruby-land I'd stick  
this on my top-level module. What do I do in Elixir?  
  
I think I could use an agent to hold this state, but when wouldn't  
that mean that users have to start some processes just to make use of  
a library that does some glorified string interpolation?  
It seems rather fiddly, and I'm not sure I'm understanding it correctly.  
  
Thanks,  
Louis

Ismael AbreuThu, Apr 9, 2015 at 7:04 PM

Hi.  
  
For what I know of, processes are very cheap so using them on this case shouldn’t be a problem at all.  
To view this discussion on the web visit <https://groups.google.com/d/msgid/elixir-lang-talk/94D830A6-BDE1-4E62-99A3-37BCA5FD257F%40gmail.com>.

Adam KittelsonThu, Apr 9, 2015 at 7:12 PM

You'd want your agent to be a supervised process, and your supervisor would be started by your application. So users of your library would not need to start your agent directly, they'd just add your application to their list of applications in their mix.exs, just as they'd do with things like :logger, or :phoenix, or :ecto etc.

That way when a user starts their application your application will be started, which will start any processes your library needs to do what it does.

More info at <http://elixir-lang.org/getting-started/mix-otp/supervisor-and-application.html>

Adam

To view this discussion on the web visit [https://groups.google.com/d/msgid/elixir-lang-talk/CABqbXnsu6XXC8vGkaiYquWBy8Hzi1DHesxAyDgfYX8FM1FRw3g%40mail.gmail.com](https://groups.google.com/d/msgid/elixir-lang-talk/CABqbXnsu6XXC8vGkaiYquWBy8Hzi1DHesxAyDgfYX8FM1FRw3g%40mail.gmail.com?utm_medium=email&utm_source=footer).

Robert VirdingThu, Apr 9, 2015 at 7:30 PM

If the data is quite static you could initialise it at startup time and put it in an ETS table and let all processes access it. If the data is more dynamic then you could still put it in an ETS table and have a process which manages it.  
  
Robert  
  
On Friday, April 10, 2015 at 12:12:10 AM UTC+2, Adam Kittelson wrote:
> You'd want your agent to be a supervised process, and your supervisor would be started by your application. So users of your library would not need to start your agent directly, they'd just add your application to their list of applications in their mix.exs, just as they'd do with things like :logger, or :phoenix, or :ecto etc.
>
> That way when a user starts their application your application will be started, which will start any processes your library needs to do what it does.
>
> More info at <http://elixir-lang.org/getting-started/mix-otp/supervisor-and-application.html>
>
> Adam
>
> On Thu, Apr 9, 2015 at 5:04 PM, Ismael Abreu <isma...@gmail.com> wrote:  
> > Hi.  
> >   
> > For what I know of, processes are very cheap so using them on this case shouldn’t be a problem at all.  
> >
> > > On 9 Apr 2015, at 22:55, Louis Pilfold <lo...@lpil.uk> wrote:  
> > >  
> > > Hello!  
> > >  
> > > I've found myself getting slightly confused by state in this immutable  
> > > world again :P  
> > >  
> > > I'm writing a small library for colouring strings to be printed to the  
> > > terminal. One thing that I wish to do is to check some environmental  
> > > variables on program load (or the first time a function is called) in  
> > > order to determine the capabilities of the terminal.  
> > >  
> > > I'd like to not perform this check each time, so I would like to set a  
> > > flag somewhere that would be read in future. In Ruby-land I'd stick  
> > > this on my top-level module. What do I do in Elixir?  
> > >  
> > > I think I could use an agent to hold this state, but when wouldn't  
> > > that mean that users have to start some processes just to make use of  
> > > a library that does some glorified string interpolation?  
> > > It seems rather fiddly, and I'm not sure I'm understanding it correctly.  
> > >  
> > > Thanks,  
> > > Louis  
> > >  
> > > --  
> > > You received this message because you are subscribed to the Google Groups "elixir-lang-talk" group.  
> > > To unsubscribe from this group and stop receiving emails from it, send an email to elixir-lang-ta...@googlegroups.com.  
> > > To view this discussion on the web visit <https://groups.google.com/d/msgid/elixir-lang-talk/CAM-pwt6VYvPPKZMk6POE3Z2aJg%2BYAkTQMNqBJTMXenXk-fSVDg%40mail.gmail.com>.  
> > > For more options, visit <https://groups.google.com/d/optout>.  
> >   
> > --  
> > You received this message because you are subscribed to the Google Groups "elixir-lang-talk" group.  
> > To unsubscribe from this group and stop receiving emails from it, send an email to elixir-lang-ta...@googlegroups.com.
> >
> > To view this discussion on the web visit <https://groups.google.com/d/msgid/elixir-lang-talk/94D830A6-BDE1-4E62-99A3-37BCA5FD257F%40gmail.com>.  
> >
> > For more options, visit <https://groups.google.com/d/optout>.

--   
You received this message because you are subscribed to the Google Groups "elixir-lang-talk" group.  
To unsubscribe from this group and stop receiving emails from it, send an email to [elixir-lang-talk+unsubscribe@googlegroups.com](mailto:elixir-lang-talk+unsubscribe@googlegroups.com).  
To view this discussion on the web visit [https://groups.google.com/d/msgid/elixir-lang-talk/d8287aa3-7d04-45ea-8c2d-e713cd7e98d4%40googlegroups.com](https://groups.google.com/d/msgid/elixir-lang-talk/d8287aa3-7d04-45ea-8c2d-e713cd7e98d4%40googlegroups.com?utm_medium=email&utm_source=footer).

José ValimFri, Apr 10, 2015 at 6:48 AM

> I think I could use an agent to hold this state, but when wouldn't  
> that mean that users have to start some processes just to make use of  
> a library that does some glorified string interpolation?  
> It seems rather fiddly, and I'm not sure I'm understanding it correctly.

If your concern is performance, some answers here have already tackled that. Feel free to create as many processes as you want. However, if you concern is usability (i.e. the user needs to start a process manually), you don't need to worry about that too.

If you create a new mix application using "mix new my\_app --sup", the generated application will contain an application callback that is invoked every time your application starts. This way, the user of your library never calls it automatically. In this callback, you need to start a supervisor, and the sample code we ship already does that. In that supervisor, you want to add your agent as child and store the state in there:

children = [

worker(MyApp.EnvState, [])

]

Then in MyApp.EnvState module:

defmodule MyApp.EnvState do

# Let's register the process with the same name as the module

@name \_\_MODULE\_\_

# Default callback invoked by the supervisor

def start\_link do

Agent.start\_link(fn ->

# Code that computes state based on env and returns a map

end, name: @name)

end

def get(key) do

Agent.get(@name, fn map -> Map.get(map, key) end)

end

end

You may say this is much more verbose than a class variable in Ruby and I completely agree! But that is exactly the point: if you have global state, you want to make it explicit and have explicit control over which operations you can perform, how to handle failures around the state and what not.

When you are writing complex applications in Ruby, the state is everywhere, so good luck introspecting or debugging it. In Elixir you know they are inside processes, often in the supervision trees, which are very easy to explore, debug and understand, even more with tools like :observer (try :observer.start on IEx if you haven't yet!).

--   
You received this message because you are subscribed to the Google Groups "elixir-lang-talk" group.  
To unsubscribe from this group and stop receiving emails from it, send an email to [elixir-lang-talk+unsubscribe@googlegroups.com](mailto:elixir-lang-talk+unsubscribe@googlegroups.com).  
To view this discussion on the web visit [https://groups.google.com/d/msgid/elixir-lang-talk/CAGnRm4%2BhhZPXXd9GnUavHtVTQviOfRC-xF4uN%3D0MJZ1oNcWE5w%40mail.gmail.com](https://groups.google.com/d/msgid/elixir-lang-talk/CAGnRm4%2BhhZPXXd9GnUavHtVTQviOfRC-xF4uN%3D0MJZ1oNcWE5w%40mail.gmail.com?utm_medium=email&utm_source=footer).
