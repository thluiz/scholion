---
url: "https://mail.google.com/mail/u/0/?pli=1#label/Listas%2F05+-+Principais/14d5d816ae28e97f"
captured_at: "2015-05-25T09:20:58-03:00"
title: "[elixir-talk:8485] Problems dealing with Enumerable protocol - th.luiz@gmail.com - Gmail"
domain: "mail-google-com"
---

[elixir-talk:8485] Problems dealing with Enumerable protocol

Participantes: vitumail@gmail.com, elixir-lang-talk@googlegroups.com, jose.valim@plataformatec.com.br, bbense@gmail.com, peterghamilton@gmail.com

[Abrir conversação no Gmail](https://mail.google.com/mail/u/0/?pli=1#label/Listas%2F05+-+Principais/14d5d816ae28e97f)

Victor RodriguesSat, May 16, 2015 at 1:14 PM

Hi,

Playing with Elixir these days, it's being a great experience! Just struggling a little bit with Enumerable at this moment.

This is a library I'm building to exercise: <https://github.com/rodrigues/red> . It builds Redis queries that can be chained, and fetching only happens when the query is treated as an Enumerable, like in:

`"user#42" |> Red.rel(:follow) |> Enum.take(5)`

Enum.take(query, 5) ends up calling reduce, but this 5 is valuable information that I could pass to Redis to get only the 5 top items in the sorted set, not all its members beforehand.

Enum.at(query, 3) goes through the reduce the same way, but I could make a very performant call to Redis to get only the element at that position.

Enumerable.count and .member? already allows me to be very performant for these two situations.

In Ruby I could just reimplement the behaviour for some of these functions for my abstract collection. I know Protocols are different, but maybe I'm missing something that would allow me to do something like that with Elixir.

Any ideas on how to approach that better? Right now I'm creating limit and offset functions that put pagination information in my query and then I do some Enum call, I'd prefer to resolve this in a way Enum functions would work good with it.

Thanks!

José ValimSat, May 16, 2015 at 1:47 PM

I would say your solution, with a explicit limit and offset is the correct one. It is important to make a distinction between database and in-memory/stream operations because they are very different when it comes to performance, latency (or lack of), error reasons, etc.

The closest you could get to seamless integration is via streaming, which often brings a asynchronicity anyway, but I am not sure if Redis supports it (and it has higher overhead if all you care is the first five items).

So go with explicit limit/offset. I would make count and member? explicit too.

--   

**José Valim**

[www.plataformatec.com.br](http://www.plataformatec.com.br/)

Skype: jv.ptec

Founder and Lead Developer

  
--   
You received this message because you are subscribed to the Google Groups "elixir-lang-talk" group.  
To unsubscribe from this group and stop receiving emails from it, send an email to [elixir-lang-talk+unsubscribe@googlegroups.com](mailto:elixir-lang-talk+unsubscribe@googlegroups.com).  
To view this discussion on the web visit [https://groups.google.com/d/msgid/elixir-lang-talk/CAGnRm4%2BcSyfGheBYi2xr7a0\_tiJ0OFY%3DQyyqoM-2H53OXcYrVQ%40mail.gmail.com](https://groups.google.com/d/msgid/elixir-lang-talk/CAGnRm4%2BcSyfGheBYi2xr7a0_tiJ0OFY%3DQyyqoM-2H53OXcYrVQ%40mail.gmail.com?utm_medium=email&utm_source=footer).

Booker BenseSat, May 16, 2015 at 1:53 PM

If you want Enum.take to "short circuit" the enumeration, you have to implement your

function as a Stream, rather than an Enumerable.

If you implement something as an Enumerable, it's going to run through the full reduction every

time you call it regardless of how the "downstream" ( downpipe?) function works.

You can use Stream.resource to wrap the Redis lookup and provide a Streamable version

of your api.

- Booker C. Bense

To view this discussion on the web visit [https://groups.google.com/d/msgid/elixir-lang-talk/6e96c52f-cf63-445c-9616-04c3a763717c%40googlegroups.com](https://groups.google.com/d/msgid/elixir-lang-talk/6e96c52f-cf63-445c-9616-04c3a763717c%40googlegroups.com?utm_medium=email&utm_source=footer).

Peter HamiltonSat, May 16, 2015 at 2:17 PM

I'd recommend providing semantically similar functions in Red for take, at, etc.

Just as Stream.take and Enum.take have similar result but a very different implementation (and thus execution has different properties), Red.take could fit the same pattern. The result of all three should be the same, but one will be lazy, one will ve eager, and the third will be in the database.

To view this discussion on the web visit [https://groups.google.com/d/msgid/elixir-lang-talk/CAOMhEny\_c3OGQWQW\_D2jiRNMrMd5-VawTixQwQRsXoHo-NRYXw%40mail.gmail.com](https://groups.google.com/d/msgid/elixir-lang-talk/CAOMhEny_c3OGQWQW_D2jiRNMrMd5-VawTixQwQRsXoHo-NRYXw%40mail.gmail.com?utm_medium=email&utm_source=footer).

José ValimSat, May 16, 2015 at 4:47 PM

Booker, all enumerables work with Enum and Stream. The laziness in this case is not a property of the collection but a property of the module he chooses. So his implementation is likely fine, he can't know in anyway how to tell Redis to collect only 5, be it in Stream or Enum. The Enumerable just know when to stop.  
  
--   

**José Valim**

[www.plataformatec.com.br](http://www.plataformatec.com.br/)

Skype: jv.ptec

Founder and Lead Developer

  
--   
You received this message because you are subscribed to the Google Groups "elixir-lang-talk" group.  
To unsubscribe from this group and stop receiving emails from it, send an email to [elixir-lang-talk+unsubscribe@googlegroups.com](mailto:elixir-lang-talk+unsubscribe@googlegroups.com).  
To view this discussion on the web visit [https://groups.google.com/d/msgid/elixir-lang-talk/CAGnRm4J%3DbHkuYof86J5MygjKZ%2BaAXK8-P5%3Dkc37nduic-5Dg5Q%40mail.gmail.com](https://groups.google.com/d/msgid/elixir-lang-talk/CAGnRm4J%3DbHkuYof86J5MygjKZ%2BaAXK8-P5%3Dkc37nduic-5Dg5Q%40mail.gmail.com?utm_medium=email&utm_source=footer).

Booker BenseSun, May 17, 2015 at 1:48 PM

Still lot's of ruby intuition to unlearn... I keep slipping into the thought mode of data having methods.   
  
On Saturday, May 16, 2015 at 12:47:17 PM UTC-7, José Valim wrote:
> Booker, all enumerables work with Enum and Stream. The laziness in this case is not a property of the collection but a property of the module he chooses. So his implementation is likely fine, he can't know in anyway how to tell Redis to collect only 5, be it in Stream or Enum. The Enumerable just know when to stop.  
>   
> --   
>
> **José Valim**
>
> [www.plataformatec.com.br](http://www.plataformatec.com.br/)
>
> Skype: jv.ptec
>
> Founder and Lead Developer

--   
You received this message because you are subscribed to the Google Groups "elixir-lang-talk" group.  
To unsubscribe from this group and stop receiving emails from it, send an email to [elixir-lang-talk+unsubscribe@googlegroups.com](mailto:elixir-lang-talk+unsubscribe@googlegroups.com).  
To view this discussion on the web visit [https://groups.google.com/d/msgid/elixir-lang-talk/d6eef295-5c32-4324-a852-3dc89cfd7367%40googlegroups.com](https://groups.google.com/d/msgid/elixir-lang-talk/d6eef295-5c32-4324-a852-3dc89cfd7367%40googlegroups.com?utm_medium=email&utm_source=footer).
