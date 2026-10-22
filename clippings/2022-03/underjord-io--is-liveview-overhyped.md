---
url: "https://underjord.io/is-liveview-overhyped.html"
captured_at: "2022-03-18T07:39:34-03:00"
title: "Underjord | Is LiveView Overhyped?"
domain: "underjord-io"
---

# Is LiveView Overhyped?

2022-03-17

To alleviate any sense of clickbait. No, it is not overhyped as a technology, in my opinion. Let’s get into the nuances.

In a recent tweet a while back a member of the Elixir community expressed some frustration with how everything is all about LiveView. It led to some interesting and useful discussion and as someone who writes a fair bit about Elixir, Phoenix and such I have thoughts. Following on that discussions other people expressed further concern about the unreserved enthusiasm with which some of us have pushed LiveView and maybe even more, the PETAL stack. I doubt they were just thinking of me there but I’d be surprised if I wasn’t considered a bit of a cheerleader for it. So taking some of that very reasonable criticism and skepticism, let’s try to address that and also dig into some of the concerns about the LiveView hype.

The discussion can be somewhat uncomfortable if you are enthusiastic about LiveView. It is easy to get defensive and that’s not all that useful. If we look past that the discussion itself can be useful and should be very welcome. There was no drama in that thread I saw and it was all very civil. So lets continue along those lines.

## My understanding

How qualified am I to write about Phoenix LiveView? Somewhat. I’ve seen all the keynotes, followed it since the inception and I’ve used it a fair bit. Many hobby projects, some production work. I’ve used it in anger and joy, run into problems and delights. So I think I can speak with some nuance on it. As I go into writing this my stance is that I find it useful, powerful and a very interesting approach for building web UI. I am enthusiastic about it. It makes some trade-offs that even I find frustrating. It is not best for everything.

Let’s line up some of the criticisms brought up around LiveView:

- It cannot work offline.
- Latency is a concern.
- Bandwidth and poor connections, are they screwed?
- It deviates from standard server-side rendering and will not by default fall back gracefully.
- It has been overhyped.

## Offline

This is the major trade-off. If you need to make an offline-first Progressive Web App or similar you should either not use LiveView or only use LiveView for the parts that don’t make sense offline. There are potential ways of building on top of LiveView and the JS integration to deliver something that mixes this together but you’d be off in the wilds with a machete at that point. That’s not what is meant to do. There’s nothing good about this and there is no big point in dancing around it. The gains you get from shifting state and much of the interactivity to the server in terms of deduplication, security aspects and simplicity comes with the trade-off that it isn’t on the client.

I don’t expect this to change but I could see efforts like Lumen (Elixir to WASM compiler) or Gleam (targets the BEAM and JS) make it potentially possible to build some shared state management code for both client and server but that’s a far ways off if it ever happens. I think for now we should accept that this is the major trade-off we make when using LiveView.

## Latency

LiveView communicates near-realtime events and state changes over WebSockets and that means I can do things like validate as the user types. Compared to a client-side frontend this means we have more latency concerns for similar validations. Round-trip latency affects every update and if we’re in Australia talking to the US we’ll see ping times of around 250ms which is noticeable. Bad internet weather can cause the same symptom. This is a good case why LiveView really isn’t meant for games or other latency-sensitive applications. It may be annoying that your validation takes a quarter of a second but if you are playing an action-oriented game, that’s often considered unplayable.

Now LiveView doesn’t prevent doing client-side validations and interactivity so for smaller operations you can cut that latency by doing things on the client. However, part of the idea of LiveView is that it reduces the amount of JS you need to write. So saying you need to do client-side JS is a bit of a cop out. Now for actual validation against server state and more serious interactivity LiveView is the same or better as talking to an API using a client-side JS framework. Going over WebSockets should reduce latency compared to most HTTP API calls. The BEAM is good at consistently keeping reasonably latencies so you shouldn’t run into many random latency spikes from the runtime.

The latency concerns are warranted if you have a lot of work you could do client-side. Whether you should be doing a separate JS frontend or use LiveView JS interop is really up to you at that point. The latency of LiveView should typically be lower than doing things over a full HTTP requests and responses though since LiveView runs over an open WebSocket. This also lets the server trivially push events and state. So I’d expect typically lower latencies than your REST-driven SPA for anything that requires a server roundtrip.

## Inclusivity and Poor Connectivity

There were also concerns expressed about how it impacts poor connections, bandwidth usage and such. José Valim adressed some of this in the Twitter thread. LiveView sends as little data as it can figure out how to by initially calculating what parts of a template can change and then only sending diffs when state does change. So it would typically send less data than a normal JSON payload to achieve a change. It does of course send more data than performing the operation on the client. Assuming that the javascript code required for the client-side operations is not huge and a cause of bandwidth issues itself.

I will say, I don’t know the experience of using WebSocket webapps heavily on poor connections. Being stateful connections I imagine you might drop them due to your network being dodgy. LiveView should recover that pretty well but in that sense it cuts down on overhead by setting up a persistent connection but you might be paying a bit in fragility. WebSockets are more fragile in comparison to HTTP requests that are typically just request, response, done. This could hit any system that leans on WebSockets though, not just LiveView and I’ve not seen any real issues using LiveView apps while out and about on cellular data.

I think it is a sensible trade-offs for many modern web apps but it is always worthwhile to consider your audience and whether they might be negatively impacted by your technical choices. My feeling is that LiveView does more by default to keep things lean and efficient than most web apps do when actively trying, just by virtue of having the diffing in place to minimize payloads.

## Graceful degradation

I don’t know if this is more a criticism someone has brought up or something I have on my mind. How do we handle falling back to the lowest common denominator? How good a citizen of HTML and HTTP can LiveView be? How good is it by default?

LiveView will by default render a normal web page if it cannot establish the WebSocket. If it is a form it will not work unless you put extra effort in. So most likely readable, not interactable.

I’d be interested to see a library that does some nice work to essentially create a normal form endpoint based on the submit event handler. It *seems* like it could be pretty straight-forward. I’m not sure if that’s just optimism on my part. Making more nuanced forms work well would have all the normal challenges of making something work great both ways.

I think LiveView does a fair job and a reasonable trade-offs here. What I’d wish is that it had a perfect fallback strategy if JS isn’t available. My wish to see perfect solutions isn’t really LiveView’s problem though and I’ll own that one myself.

It seems entirely possible to do great graceful degradation but as always it isn’t necessarily easy or typically a very compelling return on investment. Unfortunately.

## OVERHYPE!

The Elixir community often self-identifies as a pragmatic bunch. I think that’s mostly true. I saw some concern raised that LiveView was being swung around with rose-tinted glasses. I think that certainly happens. We have plenty of people who like the shiny thing. I’m a sucker for it personally. However, in fairness to the pragmatic streak, I think the discussion of trade-offs has been with LiveView since the very start. I think José and Chris have addressed it continuously as well. I see the community being enthusiastic but not unreservedly so. I do have my own sense of this hype being a bit much sometimes and I imagine I know where the feeling comes from.

The many conference talks, the numerous articles and the general air of active excitement you might see when following the community. So much of it is about LiveView. As someone actively engaged you’ve heard more about LiveView than you can stand by now, probably. Yet every day someone’s exposure to that new talk is their first glimpse of LiveView. I think we should keep talking about it, writing about it and sharing how we use it. I’m painfully aware that I’m mostly not the audience though. It’s not new to me, building an app in LiveView is not a thing of excitement to me, it’s just a thing I do, a tool I enjoy. Much like Phoenix itself, Phoenix Channels, Ecto and all these tools that I was so excited about are now just things I apply to do what I do.

I’m still very interested in Elixir, Phoenix, Ecto, LiveView and everything else. I’m excited about what they let me do. Depending on where you are along your path you’ll have exhausted your hype about a thing. There’s also the possibility that a particular tool just never speaks to you the way it does to others. That’s fine as well. In that case the enthusiasm is probably overbearing.

## In summary

I don’t find LiveView to be overhyped as in being claimed to be better than it technically is. It is cool tech that achieves some interesting capabilities by making some well-chosen trade-offs. I think it’s great, a good design, well iterated, a compelling tool. Most importantly for me, it lets me do more building, faster and with fewer frustrations.

It has also been promoted a lot and it continues to be. Some will be breathless in their praise, some will be nuanced. I’ve definitely spent my time getting out of breath shouting about it. Hopefully this weighs in on the nuanced side.

Seems good to me but isn’t a panacea. **Very hot take.**

Thanks for reading. If I’m very wrong, very right or somewhere in the middle and you want to have words about it, good or bad, I’m available at [lars@underjord.io](https://underjord.io/is-liveview-overhyped.htmlmailto:lars@underjord.io) and [@lawik](https://twitter.com/lawik).

There are some companies that support my publishing and they **want to hire Elixir developers**, even *aspiring ones*. I personally talk to these companies to figure out what they want and what they can offer, so please do [check the jobs page](https://underjord.io/jobs.html). It really does help.
