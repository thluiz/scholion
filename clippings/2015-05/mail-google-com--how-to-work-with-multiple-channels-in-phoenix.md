---
url: "https://mail.google.com/mail/u/0/?pli=1#label/Listas%2F05+-+Principais/14d7eb385171ca3a"
captured_at: "2015-05-25T08:56:39-03:00"
title: "[elixir-talk:8579] How to work with multiple Channels in Phoenix? - th.luiz@gmail.com - Gmail"
domain: "mail-google-com"
---

[elixir-talk:8579] How to work with multiple Channels in Phoenix?

Participantes: ivan.inmm@gmail.com, elixir-lang-talk@googlegroups.com, jose.valim@plataformatec.com.br, phoenix-talk@googlegroups.com, chris@chrismccord.com, spyromus@gmail.com

[Abrir conversação no Gmail](https://mail.google.com/mail/u/0/?pli=1#label/Listas%2F05+-+Principais/14d7eb385171ca3a)

Ivan MirandaFri, May 22, 2015 at 11:56 PM

I have the following situation:

The user need receive and send messages to the chat topic, the news topic and the stock exchange topic

Can i share the user info between the topics using the socket struct or realy i need to join in the 3 topics?

Thanks

José ValimSat, May 23, 2015 at 6:12 AM

Hello Ivan, you should try the Phoenix mailing list: <http://groups.google.com/group/phoenix-talk> :)

**José Valim**

[www.plataformatec.com.br](http://www.plataformatec.com.br/)

Skype: jv.ptec

Founder and Lead Developer

To view this discussion on the web visit [https://groups.google.com/d/msgid/elixir-lang-talk/CAGnRm4Kzs%3Dn\_FkrGYDLRTQhKypix2ebL%2B0Y3wX5KFP2bLb%3D-Qw%40mail.gmail.com](https://groups.google.com/d/msgid/elixir-lang-talk/CAGnRm4Kzs%3Dn_FkrGYDLRTQhKypix2ebL%2B0Y3wX5KFP2bLb%3D-Qw%40mail.gmail.com?utm_medium=email&utm_source=footer).

Ivan MirandaSat, May 23, 2015 at 2:10 PM

Ok!

Sorry and thank you :)

Em sábado, 23 de maio de 2015 06:13:17 UTC-3, José Valim escreveu:
> Hello Ivan, you should try the Phoenix mailing list: <http://groups.google.com/group/phoenix-talk> :)
>
> **José Valim**
>
> [www.plataformatec.com.br](http://www.plataformatec.com.br/)
>
> Skype: jv.ptec
>
> Founder and Lead Developer
>
>   
>
> On Sat, May 23, 2015 at 4:56 AM, Ivan Miranda <ivan...@gmail.com> wrote:  
> > I have the following situation:
> >
> > The user need receive and send messages to the chat topic, the news topic and the stock exchange topic
> >
> > Can i share the user info between the topics using the socket struct or realy i need to join in the 3 topics?
> >
> > Thanks
> >
> > --   
> > You received this message because you are subscribed to the Google Groups "elixir-lang-talk" group.  
> > To unsubscribe from this group and stop receiving emails from it, send an email to elixir-lang-ta...@googlegroups.com.  
> > To view this discussion on the web visit [https://groups.google.com/d/msgid/elixir-lang-talk/defc1805-102e-4b2c-ba1d-d1297ab3c6b3%40googlegroups.com](https://groups.google.com/d/msgid/elixir-lang-talk/defc1805-102e-4b2c-ba1d-d1297ab3c6b3%40googlegroups.com?utm_medium=email&utm_source=footer).  
> > For more options, visit <https://groups.google.com/d/optout>.

--   
You received this message because you are subscribed to the Google Groups "elixir-lang-talk" group.  
To unsubscribe from this group and stop receiving emails from it, send an email to [elixir-lang-talk+unsubscribe@googlegroups.com](mailto:elixir-lang-talk+unsubscribe@googlegroups.com).  
To view this discussion on the web visit [https://groups.google.com/d/msgid/elixir-lang-talk/72642da2-6713-4e8f-bbc4-0d22993e0b42%40googlegroups.com](https://groups.google.com/d/msgid/elixir-lang-talk/72642da2-6713-4e8f-bbc4-0d22993e0b42%40googlegroups.com?utm_medium=email&utm_source=footer).

Ivan MirandaSat, May 23, 2015 at 2:15 PM

I have the following situation:

The user need receive and send messages to the chat topic, the news topic and the stock exchange topic.

Both has a lot of events and functions that i would like to leave in separate modules

Can i share the user info between the topics using the socket struct or i need to join in the 3 topics?

Thanks

Chris McCordSat, May 23, 2015 at 2:30 PM

You need to join the three topics. You can broadcast on any topic with `broadcast topic, event, payload`, but the client needs to join every topic it wants to receive events from. We added “socket params” and “channel params” to make this easier, so if you update to 0.13.1 ,you can do:

let socket = new Phoenix.Socket("/ws", params: {user\_token: userToken}) // socket params

socket.connect()

let exchangeChan = socket.chan(“exchanges:123”, {key: “val"})  // channel params

….

Then join/3 for \*all\* channels will include the socket params which are merged into the channel params. So for the above example, the ExhangeChannel join/3 could match like this:

def join(“exchanges:” <> id, %{“user\_token” => user\_token, “key” => “val”}, socket) do …

In Phoenix 0.14 we are adding helper functions to easily generate and verify channel tokens/data, but this setup will let you treat the socket params like a session, so long as you verify on join/3’s. Does that answer your questions?

Chris

To view this discussion on the web visit [https://groups.google.com/d/msgid/phoenix-talk/92302E0C-AA42-4142-B211-FDC52FCFF033%40chrismccord.com](https://groups.google.com/d/msgid/phoenix-talk/92302E0C-AA42-4142-B211-FDC52FCFF033%40chrismccord.com?utm_medium=email&utm_source=footer).

Ivan MirandaSat, May 23, 2015 at 2:45 PM

Nice,

In this way, I'll need to use the token to retrieve user data from some agent or database eg...

is there any problem if I use the macro "\_\_using\_\_" to import the functions of other modules?

I not tested and do not know if it would work.It seems to me an ugly hack but I would like to know because we can not do something like.

tnx

Em sábado, 23 de maio de 2015 14:30:19 UTC-3, Chris McCord escreveu:
> You need to join the three topics. You can broadcast on any topic with `broadcast topic, event, payload`, but the client needs to join every topic it wants to receive events from. We added “socket params” and “channel params” to make this easier, so if you update to 0.13.1 ,you can do:
>
> let socket = new Phoenix.Socket("/ws", params: {user\_token: userToken}) // socket params
>
> socket.connect()
>
> let exchangeChan = socket.chan(“exchanges:123”, {key: “val"})  // channel params
>
> ….
>
> Then join/3 for \*all\* channels will include the socket params which are merged into the channel params. So for the above example, the ExhangeChannel join/3 could match like this:
>
> def join(“exchanges:” <> id, %{“user\_token” => user\_token, “key” => “val”}, socket) do …
>
> In Phoenix 0.14 we are adding helper functions to easily generate and verify channel tokens/data, but this setup will let you treat the socket params like a session, so long as you verify on join/3’s. Does that answer your questions?
>
> Chris
>
> > On May 23, 2015, at 1:15 PM, Ivan Miranda <ivan...@gmail.com> wrote:
> >
> >   
> >
> > I have the following situation:
> >
> > The user need receive and send messages to the chat topic, the news topic and the stock exchange topic.
> >
> > Both has a lot of events and functions that i would like to leave in separate modules
> >
> > Can i share the user info between the topics using the socket struct or i need to join in the 3 topics?
> >
> > Thanks
> >
> > --   
> > You received this message because you are subscribed to the Google Groups "phoenix-talk" group.  
> > To unsubscribe from this group and stop receiving emails from it, send an email to phoenix-talk...@googlegroups.com.  
> > To post to this group, send email to phoeni...@googlegroups.com.  
> > Visit this group at <http://groups.google.com/group/phoenix-talk>.  
> > To view this discussion on the web visit [https://groups.google.com/d/msgid/phoenix-talk/a52b0a61-74eb-4d78-8ef4-c5e6b0dc1015%40googlegroups.com](https://groups.google.com/d/msgid/phoenix-talk/a52b0a61-74eb-4d78-8ef4-c5e6b0dc1015%40googlegroups.com?utm_medium=email&utm_source=footer).  
> > For more options, visit <https://groups.google.com/d/optout>.

--   
You received this message because you are subscribed to the Google Groups "phoenix-talk" group.  
To unsubscribe from this group and stop receiving emails from it, send an email to [phoenix-talk+unsubscribe@googlegroups.com](mailto:phoenix-talk+unsubscribe@googlegroups.com).  
To post to this group, send email to [phoenix-talk@googlegroups.com](mailto:phoenix-talk@googlegroups.com).  
Visit this group at <http://groups.google.com/group/phoenix-talk>.  
To view this discussion on the web visit [https://groups.google.com/d/msgid/phoenix-talk/8bd6e56a-e4ec-4753-b096-6164ffde9fc4%40googlegroups.com](https://groups.google.com/d/msgid/phoenix-talk/8bd6e56a-e4ec-4753-b096-6164ffde9fc4%40googlegroups.com?utm_medium=email&utm_source=footer).

Ivan MirandaSat, May 23, 2015 at 2:49 PM

Nice,

In this way, I'll need to use the token to retrieve user data from some agent or database eg...

but it was good to know that the next version will have a more practical way to solve it

is there any problem if I use the macro "\_\_using\_\_" to import the functions of other modules? It seems to me an ugly hack but it would be interesting to know if it would work...

tnx

  
Em sábado, 23 de maio de 2015 14:15:58 UTC-3, Ivan Miranda escreveu:
> I have the following situation:
>
> The user need receive and send messages to the chat topic, the news topic and the stock exchange topic.
>
> Both has a lot of events and functions that i would like to leave in separate modules
>
> Can i share the user info between the topics using the socket struct or i need to join in the 3 topics?
>
> Thanks

--   
You received this message because you are subscribed to the Google Groups "phoenix-talk" group.  
To unsubscribe from this group and stop receiving emails from it, send an email to [phoenix-talk+unsubscribe@googlegroups.com](mailto:phoenix-talk+unsubscribe@googlegroups.com).  
To post to this group, send email to [phoenix-talk@googlegroups.com](mailto:phoenix-talk@googlegroups.com).  
Visit this group at <http://groups.google.com/group/phoenix-talk>.  
To view this discussion on the web visit [https://groups.google.com/d/msgid/phoenix-talk/77238eb9-e2e5-41b2-828b-1fe380858585%40googlegroups.com](https://groups.google.com/d/msgid/phoenix-talk/77238eb9-e2e5-41b2-828b-1fe380858585%40googlegroups.com?utm_medium=email&utm_source=footer).

Aleksey GureevSun, May 24, 2015 at 12:46 PM

Well, you can broadcast to any topic. Check out PubSub section of the doc. And as Jose mentioned, it's better be asked there.  
  
On Saturday, May 23, 2015 at 5:56:39 AM UTC+3, Ivan Miranda wrote:
> I have the following situation:
>
> The user need receive and send messages to the chat topic, the news topic and the stock exchange topic
>
> Can i share the user info between the topics using the socket struct or realy i need to join in the 3 topics?
>
> Thanks

--   
You received this message because you are subscribed to the Google Groups "elixir-lang-talk" group.  
To unsubscribe from this group and stop receiving emails from it, send an email to [elixir-lang-talk+unsubscribe@googlegroups.com](mailto:elixir-lang-talk+unsubscribe@googlegroups.com).  
To view this discussion on the web visit [https://groups.google.com/d/msgid/elixir-lang-talk/b4d4dfb6-6ffe-45c8-a2e6-fea10aa6bdcd%40googlegroups.com](https://groups.google.com/d/msgid/elixir-lang-talk/b4d4dfb6-6ffe-45c8-a2e6-fea10aa6bdcd%40googlegroups.com?utm_medium=email&utm_source=footer).
