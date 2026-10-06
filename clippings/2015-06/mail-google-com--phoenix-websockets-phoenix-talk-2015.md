---
url: "https://mail.google.com/mail/u/0/?pli=1#inbox/14dab96b92a57e17"
captured_at: "2015-06-02T17:37:57-03:00"
title: "Phoenix & WebSockets - th.luiz@gmail.com - Gmail"
domain: "mail-google-com"
---

Phoenix & WebSockets

Participantes: darthdeus@gmail.com, phoenix-talk@googlegroups.com, steve@stevedomin.com, chris@chrismccord.com, josh@isotope11.com, ivan.inmm@gmail.com

[Abrir conversação no Gmail](https://mail.google.com/mail/u/0/?pli=1#inbox/14dab96b92a57e17)

Jakub ArnoldSun, May 31, 2015 at 5:08 PM

I'm posting here as a followup to my question on IRC.

The system that I'm currently building needs to work with raw websockets. I'm currently using Cowboy for that, which works wonderful. I'd also like to build a small API to handle some other requests, which lead me to Phoenix. The problem is that Phoenix doesn't mention WebSockets anywhere at all in its docs. Yes there are Channels, but given that I need to actually access the WebSocket, I can't really use those.

But since Phoenix supports Plug, I thought that I might use Plug directly to the WebSocket part, and mount that in the Phoenix app. But it seems that there is no API for WebSockets in Plug either (see <https://github.com/elixir-lang/plug/issues/65>).

The funny thing is that Phoenix currently runs on top of Cowboy, so basically I'm running one instance of Cowboy server on one port to handle the Websockets, and another one to run Phoenix.

So my question is, is there a way to solve this? It feels that there should be an abstraction layer in which I can just Plug in (no pun intended) and be handling WebSockets, but there doesn't seem to be one. I've also looked at other Elixir web frameworks other than Phoenix, but it seems the only other alternative is Sugar (<http://sugar-framework.github.io/>), which doesn't handle this either.

Steve DominSun, May 31, 2015 at 8:40 PM

Hi Jakub,

Have you tried to look at the websocket code in Phoenix? Specifically <https://github.com/phoenixframework/phoenix/blob/c12939a6bb2da6880ff93c41689edfbac726339f/lib/phoenix/endpoint/cowboy_websocket.ex>

I haven't looked exactly how to do it but I'm pretty sure it must be possible to use the Cowboy server used by Phoenix.

To view this discussion on the web visit [https://groups.google.com/d/msgid/phoenix-talk/a773060a-1458-4199-ab52-76ecd9cf1351%40googlegroups.com](https://groups.google.com/d/msgid/phoenix-talk/a773060a-1458-4199-ab52-76ecd9cf1351%40googlegroups.com?utm_medium=email&utm_source=footer).

Chris McCordMon, Jun 1, 2015 at 2:18 PM

To sum up the discussion from irc, until we have another plug adapter to try to abstract a websocket api for, we can’t support websockets directly in phoenix. Phoenix adds webscoket support for channels via its own private API that is coupled to cowboy, but we’d like to extend this in the future when Plug gets a WS api. So for now the best recommendation for someone who wants raw websockets (not using channels), is to use Plug dispatch options and a  raw cowboy websocket handler.

To view this discussion on the web visit [https://groups.google.com/d/msgid/phoenix-talk/6AA9CAC2-3836-4F2D-A0C4-4B386B8F805B%40chrismccord.com](https://groups.google.com/d/msgid/phoenix-talk/6AA9CAC2-3836-4F2D-A0C4-4B386B8F805B%40chrismccord.com?utm_medium=email&utm_source=footer).

Josh AdamsMon, Jun 1, 2015 at 2:25 PM

I'm presently working on something that's just a websockets proxy (with some business logic layered on at the proxy layer) and will be using meh's Socket.  I wanted to use Phoenix but obv. Channels != WebSockets.  Would love to see where common abstractions overlap though.

--   

**Josh Adams**  
CTO | [isotope|eleven](http://www.isotope11.com/)  
[cell] [(205) 215-3957](tel:%28205%29%20215-3957)  
[work] [(877) 476-8671 x201](tel:%28877%29%20476-8671%20x201)

[mail]

3800 Colonnade Pkwy  
Suite 140  
Birmingham, AL 35242

--   
You received this message because you are subscribed to the Google Groups "phoenix-talk" group.  
To unsubscribe from this group and stop receiving emails from it, send an email to [phoenix-talk+unsubscribe@googlegroups.com](mailto:phoenix-talk+unsubscribe@googlegroups.com).  
To post to this group, send email to [phoenix-talk@googlegroups.com](mailto:phoenix-talk@googlegroups.com).  
Visit this group at <http://groups.google.com/group/phoenix-talk>.  
To view this discussion on the web visit [https://groups.google.com/d/msgid/phoenix-talk/CAApdLgz\_sA8QnApg6X%2BuS2hsVS%2BmtE-UM4QJCwb5ms%3DVt0T4oQ%40mail.gmail.com](https://groups.google.com/d/msgid/phoenix-talk/CAApdLgz_sA8QnApg6X%2BuS2hsVS%2BmtE-UM4QJCwb5ms%3DVt0T4oQ%40mail.gmail.com?utm_medium=email&utm_source=footer).

Ivan MirandaTue, Jun 2, 2015 at 5:08 PM

I'm sorry for taking the conversation in half, but could explain (or pass a link explaining) the difference between the phoenix's channels and websockets plz?

Em segunda-feira, 1 de junho de 2015 14:18:06 UTC-3, Chris McCord escreveu:
> To sum up the discussion from irc, until we have another plug adapter to try to abstract a websocket api for, we can’t support websockets directly in phoenix. Phoenix adds webscoket support for channels via its own private API that is coupled to cowboy, but we’d like to extend this in the future when Plug gets a WS api. So for now the best recommendation for someone who wants raw websockets (not using channels), is to use Plug dispatch options and a  raw cowboy websocket handler.
>
> > On May 31, 2015, at 7:40 PM, Steve Domin <st...@stevedomin.com> wrote:
> >
> >   
> >
> > Hi Jakub,
> >
> > Have you tried to look at the websocket code in Phoenix? Specifically <https://github.com/phoenixframework/phoenix/blob/c12939a6bb2da6880ff93c41689edfbac726339f/lib/phoenix/endpoint/cowboy_websocket.ex>
> >
> > I haven't looked exactly how to do it but I'm pretty sure it must be possible to use the Cowboy server used by Phoenix.
> >
> > On Sunday, 31 May 2015 21:08:09 UTC+1, Jakub Arnold wrote:
> > > I'm posting here as a followup to my question on IRC.
> > >
> > > The system that I'm currently building needs to work with raw websockets. I'm currently using Cowboy for that, which works wonderful. I'd also like to build a small API to handle some other requests, which lead me to Phoenix. The problem is that Phoenix doesn't mention WebSockets anywhere at all in its docs. Yes there are Channels, but given that I need to actually access the WebSocket, I can't really use those.
> > >
> > > But since Phoenix supports Plug, I thought that I might use Plug directly to the WebSocket part, and mount that in the Phoenix app. But it seems that there is no API for WebSockets in Plug either (see <https://github.com/elixir-lang/plug/issues/65>).
> > >
> > > The funny thing is that Phoenix currently runs on top of Cowboy, so basically I'm running one instance of Cowboy server on one port to handle the Websockets, and another one to run Phoenix.
> > >
> > > So my question is, is there a way to solve this? It feels that there should be an abstraction layer in which I can just Plug in (no pun intended) and be handling WebSockets, but there doesn't seem to be one. I've also looked at other Elixir web frameworks other than Phoenix, but it seems the only other alternative is Sugar (<http://sugar-framework.github.io/>), which doesn't handle this either.
> >
> > --   
> > You received this message because you are subscribed to the Google Groups "phoenix-talk" group.  
> > To unsubscribe from this group and stop receiving emails from it, send an email to phoenix-talk...@googlegroups.com.  
> > To post to this group, send email to phoeni...@googlegroups.com.  
> > Visit this group at <http://groups.google.com/group/phoenix-talk>.  
> > To view this discussion on the web visit [https://groups.google.com/d/msgid/phoenix-talk/a773060a-1458-4199-ab52-76ecd9cf1351%40googlegroups.com](https://groups.google.com/d/msgid/phoenix-talk/a773060a-1458-4199-ab52-76ecd9cf1351%40googlegroups.com?utm_medium=email&utm_source=footer).  
> > For more options, visit <https://groups.google.com/d/optout>.

--   
You received this message because you are subscribed to the Google Groups "phoenix-talk" group.  
To unsubscribe from this group and stop receiving emails from it, send an email to [phoenix-talk+unsubscribe@googlegroups.com](mailto:phoenix-talk+unsubscribe@googlegroups.com).  
To post to this group, send email to [phoenix-talk@googlegroups.com](mailto:phoenix-talk@googlegroups.com).  
Visit this group at <http://groups.google.com/group/phoenix-talk>.  
To view this discussion on the web visit [https://groups.google.com/d/msgid/phoenix-talk/cd7d4e93-45fd-42d4-bf2f-422e94922c92%40googlegroups.com](https://groups.google.com/d/msgid/phoenix-talk/cd7d4e93-45fd-42d4-bf2f-422e94922c92%40googlegroups.com?utm_medium=email&utm_source=footer).

Chris McCordTue, Jun 2, 2015 at 5:15 PM

Phoenix Channels abstracts the transport layer and provides conveniences for trivial realtime communication across clients.

Phoenix Channels has three main layers:

Transport layer:

We support websockets and longpolling by default so for older browsers the phoenix.js client will fallback to longpolling. We also provide other features like automatic reconnects, exponotential backoff connection recovery, error handling, etc. With our transport setup, someone could write a message queue based transport, a MQTT transport, CoAP, etc, and the channel code on the server remains the same.

PubSub layer:

The pubsub layer sits underneath channels and brokers messages across nodes and broadcasts across clients. When you `broadcast! socket, “new:msg”, %{body: “hello!”})`, the pubsub layer underneath will deliver it to all subscribers, across nodes. The PubSub layer is adapter based, so we use :pg2 (std lib) by default for distrubited elixir, but we have a redis adapter for those on non-distributed deployments.

Channel Module callbacks:

The channel modes allow you do define callbacks to match on incoming and outgoing \*events\*. So channels have a tiny protocol that allows sending events b/w client and server with payloads.

Addiontally, we multiplex the single WS/Longpolling connection on the client. My ElixirConfEU keynote gives a really nice channel overview that should help:

<http://www.chrismccord.com/blog/2015/05/09/elixirconfeu-keynote-phoenix-takes-flight/>

To view this discussion on the web visit [https://groups.google.com/d/msgid/phoenix-talk/A8F8404D-23A2-4428-BE0E-49DE898C4E72%40chrismccord.com](https://groups.google.com/d/msgid/phoenix-talk/A8F8404D-23A2-4428-BE0E-49DE898C4E72%40chrismccord.com?utm_medium=email&utm_source=footer).

Chris McCordTue, Jun 2, 2015 at 5:22 PM

So to add to my last post, channels provide a messaging protocol for pubsub on top of the underlying transport via “topics", whether that’s websocket, long polling, or whatever else you’d like to implement and take care a lot of the features you’d require from messaging over the wire, reconnects, error handling, authorization, different devices/platforms, etc.

To view this discussion on the web visit [https://groups.google.com/d/msgid/phoenix-talk/89753D41-3DA3-4ECD-9A64-06549C1DD54B%40chrismccord.com](https://groups.google.com/d/msgid/phoenix-talk/89753D41-3DA3-4ECD-9A64-06549C1DD54B%40chrismccord.com?utm_medium=email&utm_source=footer).

Ivan MirandaTue, Jun 2, 2015 at 5:33 PM

thanks for the clarification :D  
  
Em terça-feira, 2 de junho de 2015 17:22:20 UTC-3, Chris McCord escreveu:
> So to add to my last post, channels provide a messaging protocol for pubsub on top of the underlying transport via “topics", whether that’s websocket, long polling, or whatever else you’d like to implement and take care a lot of the features you’d require from messaging over the wire, reconnects, error handling, authorization, different devices/platforms, etc. 
>
> > On Jun 2, 2015, at 4:15 PM, Chris McCord <ch...@chrismccord.com> wrote:
> >
> >   
> >
> > Phoenix Channels abstracts the transport layer and provides conveniences for trivial realtime communication across clients.
> >
> > Phoenix Channels has three main layers:
> >
> > Transport layer:
> >
> > We support websockets and longpolling by default so for older browsers the phoenix.js client will fallback to longpolling. We also provide other features like automatic reconnects, exponotential backoff connection recovery, error handling, etc. With our transport setup, someone could write a message queue based transport, a MQTT transport, CoAP, etc, and the channel code on the server remains the same.
> >
> > PubSub layer:
> >
> > The pubsub layer sits underneath channels and brokers messages across nodes and broadcasts across clients. When you `broadcast! socket, “new:msg”, %{body: “hello!”})`, the pubsub layer underneath will deliver it to all subscribers, across nodes. The PubSub layer is adapter based, so we use :pg2 (std lib) by default for distrubited elixir, but we have a redis adapter for those on non-distributed deployments.
> >
> > Channel Module callbacks:
> >
> > The channel modes allow you do define callbacks to match on incoming and outgoing \*events\*. So channels have a tiny protocol that allows sending events b/w client and server with payloads.
> >
> > Addiontally, we multiplex the single WS/Longpolling connection on the client. My ElixirConfEU keynote gives a really nice channel overview that should help:
> >
> > <http://www.chrismccord.com/blog/2015/05/09/elixirconfeu-keynote-phoenix-takes-flight/>
> >
> > > On Jun 2, 2015, at 4:08 PM, Ivan Miranda <ivan...@gmail.com> wrote:
> > >
> > >   
> > >
> > > I'm sorry for taking the conversation in half, but could explain (or pass a link explaining) the difference between the phoenix's channels and websockets plz?
> > >
> > > Em segunda-feira, 1 de junho de 2015 14:18:06 UTC-3, Chris McCord escreveu:
> > > > To sum up the discussion from irc, until we have another plug adapter to try to abstract a websocket api for, we can’t support websockets directly in phoenix. Phoenix adds webscoket support for channels via its own private API that is coupled to cowboy, but we’d like to extend this in the future when Plug gets a WS api. So for now the best recommendation for someone who wants raw websockets (not using channels), is to use Plug dispatch options and a  raw cowboy websocket handler.
> > > >
> > > > > On May 31, 2015, at 7:40 PM, Steve Domin <st...@stevedomin.com> wrote:
> > > > >
> > > > >   
> > > > >
> > > > > Hi Jakub,
> > > > >
> > > > > Have you tried to look at the websocket code in Phoenix? Specifically <https://github.com/phoenixframework/phoenix/blob/c12939a6bb2da6880ff93c41689edfbac726339f/lib/phoenix/endpoint/cowboy_websocket.ex>
> > > > >
> > > > > I haven't looked exactly how to do it but I'm pretty sure it must be possible to use the Cowboy server used by Phoenix.
> > > > >
> > > > > On Sunday, 31 May 2015 21:08:09 UTC+1, Jakub Arnold wrote:
> > > > > > I'm posting here as a followup to my question on IRC.
> > > > > >
> > > > > > The system that I'm currently building needs to work with raw websockets. I'm currently using Cowboy for that, which works wonderful. I'd also like to build a small API to handle some other requests, which lead me to Phoenix. The problem is that Phoenix doesn't mention WebSockets anywhere at all in its docs. Yes there are Channels, but given that I need to actually access the WebSocket, I can't really use those.
> > > > > >
> > > > > > But since Phoenix supports Plug, I thought that I might use Plug directly to the WebSocket part, and mount that in the Phoenix app. But it seems that there is no API for WebSockets in Plug either (see <https://github.com/elixir-lang/plug/issues/65>).
> > > > > >
> > > > > > The funny thing is that Phoenix currently runs on top of Cowboy, so basically I'm running one instance of Cowboy server on one port to handle the Websockets, and another one to run Phoenix.
> > > > > >
> > > > > > So my question is, is there a way to solve this? It feels that there should be an abstraction layer in which I can just Plug in (no pun intended) and be handling WebSockets, but there doesn't seem to be one. I've also looked at other Elixir web frameworks other than Phoenix, but it seems the only other alternative is Sugar (<http://sugar-framework.github.io/>), which doesn't handle this either.
> > > > >
> > > > > --   
> > > > > You received this message because you are subscribed to the Google Groups "phoenix-talk" group.  
> > > > > To unsubscribe from this group and stop receiving emails from it, send an email to phoenix-talk...@googlegroups.com.  
> > > > > To post to this group, send email to phoeni...@googlegroups.com.  
> > > > > Visit this group at <http://groups.google.com/group/phoenix-talk>.  
> > > > > To view this discussion on the web visit [https://groups.google.com/d/msgid/phoenix-talk/a773060a-1458-4199-ab52-76ecd9cf1351%40googlegroups.com](https://groups.google.com/d/msgid/phoenix-talk/a773060a-1458-4199-ab52-76ecd9cf1351%40googlegroups.com?utm_medium=email&utm_source=footer).  
> > > > > For more options, visit <https://groups.google.com/d/optout>.
> > >
> > > --   
> > > You received this message because you are subscribed to the Google Groups "phoenix-talk" group.  
> > > To unsubscribe from this group and stop receiving emails from it, send an email to phoenix-talk...@googlegroups.com.  
> > > To post to this group, send email to phoeni...@googlegroups.com.  
> > > Visit this group at <http://groups.google.com/group/phoenix-talk>.  
> > > To view this discussion on the web visit [https://groups.google.com/d/msgid/phoenix-talk/cd7d4e93-45fd-42d4-bf2f-422e94922c92%40googlegroups.com](https://groups.google.com/d/msgid/phoenix-talk/cd7d4e93-45fd-42d4-bf2f-422e94922c92%40googlegroups.com?utm_medium=email&utm_source=footer).  
> > > For more options, visit <https://groups.google.com/d/optout>.

--   
You received this message because you are subscribed to the Google Groups "phoenix-talk" group.  
To unsubscribe from this group and stop receiving emails from it, send an email to [phoenix-talk+unsubscribe@googlegroups.com](mailto:phoenix-talk+unsubscribe@googlegroups.com).  
To post to this group, send email to [phoenix-talk@googlegroups.com](mailto:phoenix-talk@googlegroups.com).  
Visit this group at <http://groups.google.com/group/phoenix-talk>.  
To view this discussion on the web visit [https://groups.google.com/d/msgid/phoenix-talk/ac9b796b-e1a2-428b-ae6a-098db8ab4a70%40googlegroups.com](https://groups.google.com/d/msgid/phoenix-talk/ac9b796b-e1a2-428b-ae6a-098db8ab4a70%40googlegroups.com?utm_medium=email&utm_source=footer).
