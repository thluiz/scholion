---
url: "https://mail.google.com/mail/u/0/?pli=1#label/Listas%2F05+-+Principais/14d6a51460661099"
captured_at: "2015-05-25T09:24:21-03:00"
title: "[elixir-talk:8515] Understanding Protocols - th.luiz@gmail.com - Gmail"
domain: "mail-google-com"
---

[elixir-talk:8515] Understanding Protocols

Participantes: shane@emmons.io, elixir-lang-talk@googlegroups.com, peterghamilton@gmail.com, jose.valim@plataformatec.com.br

[Abrir conversação no Gmail](https://mail.google.com/mail/u/0/?pli=1#label/Listas%2F05+-+Principais/14d6a51460661099)

Shane EmmonsTue, May 19, 2015 at 12:56 AM

I'm trying to work through Understanding Computation using Elixir instead of Ruby. Everything is going nicely so far, but I'm having trouble converting a generic reduce function into a protocol. Take a look at this gist: <https://gist.github.com/semmons99/e2a39a8a085d01df1f16>  
  
When I implement 'reduce' inside my VM module, everything works (ex1.exs), however, when I try to convert 'reduce' into a protocol and implement it with each struct, it no longer matches the way I'd expect (ex2.exs).  
  
  
> ```
> humanized: 1 * 2 + 3 * 4
> ```
>
> ```
> ** (KeyError) key :left not found in: %Num{val: 1}
>     /Users/shane/Desktop/ex2.exs:25: Reduce.Add.reduce/1
>     /Users/shane/Desktop/ex2.exs:25: Reduce.Add.reduce/1
>     /Users/shane/Desktop/ex2.exs:46: VM.eval/1
>     (elixir) lib/code.ex:307: Code.require_file/2
>     (elixir) lib/enum.ex:977: anonymous fn/3 in Enum.map/2
> ```

  
What I suspect is happening is 'reduce' is being run as implmented by the Add struct and not using the Mul struct's version and ultimately the Num structs version, but I don't understand why that is. Any pointers?  
  
Below are the raw files if you don't want to view a gist.  
  
----- ex1.exs -----  
  
defprotocol Reduce do  
  def reduce(element)  
end  
  
defmodule Num do  
  defstruct [:val]  
  
  defimpl String.Chars do  
    def to\_string(element), do: "#{element.val}"  
  end  
  
  defimpl Reduce do  
    def reduce(element), do: element  
  end  
end  
  
defmodule Add do  
  defstruct [:left, :right]  
  
  defimpl String.Chars do  
    def to\_string(element), do: "#{element.left} + #{element.right}"  
  end  
  
  defimpl Reduce do  
    def reduce(element), do: %Num{val: reduce(element.left).val + reduce(element.right).val}  
  end  
end  
  
defmodule Mul do  
  defstruct [:left, :right]  
  
  defimpl String.Chars do  
    def to\_string(element), do: "#{element.left} \* #{element.right}"  
  end  
  
  defimpl Reduce do  
    def reduce(element), do: %Num{val: reduce(element.left).val \* reduce(element.right).val}  
  end  
end  
  
defmodule VM do  
  import Reduce  
  
  def eval(formula) do  
    IO.puts "humanized: #{formula}"  
    IO.puts reduce(formula)  
  end  
end  
  
defmodule App do  
  def run do  
    num = &(%Num{val: &1})  
    add = &(%Add{left: &1, right: &2})  
    mul = &(%Mul{left: &1, right: &2})  
  
    formula = add.(  
      mul.(num.(1), num.(2)),  
      mul.(num.(3), num.(4))  
    )  
  
    VM.eval(formula)  
  end  
end  
  
App.run  
  
----- ex2.exs -----  
  
defprotocol Reduce do  
  def reduce(element)  
end  
  
defmodule Num do  
  defstruct [:val]  
  
  defimpl String.Chars do  
    def to\_string(element), do: "#{element.val}"  
  end  
  
  defimpl Reduce do  
    def reduce(element), do: element  
  end  
end  
  
defmodule Add do  
  defstruct [:left, :right]  
  
  defimpl String.Chars do  
    def to\_string(element), do: "#{element.left} + #{element.right}"  
  end  
  
  defimpl Reduce do  
    def reduce(element), do: %Num{val: reduce(element.left).val + reduce(element.right).val}  
  end  
end  
  
defmodule Mul do  
  defstruct [:left, :right]  
  
  defimpl String.Chars do  
    def to\_string(element), do: "#{element.left} \* #{element.right}"  
  end  
  
  defimpl Reduce do  
    def reduce(element), do: %Num{val: reduce(element.left).val \* reduce(element.right).val}  
  end  
end  
  
defmodule VM do  
  import Reduce  
  
  def eval(formula) do  
    IO.puts "humanized: #{formula}"  
    IO.puts reduce(formula)  
  end  
end  
  
defmodule App do  
  def run do  
    num = &(%Num{val: &1})  
    add = &(%Add{left: &1, right: &2})  
    mul = &(%Mul{left: &1, right: &2})  
  
    formula = add.(  
      mul.(num.(1), num.(2)),  
      mul.(num.(3), num.(4))  
    )  
  
    VM.eval(formula)  
  end  
end  
  
App.run

Peter HamiltonTue, May 19, 2015 at 1:01 AM

Try:

`def reduce(element), do: %Num{val: Reduce.reduce(element.left).val + Reduce.reduce(element.right).val}`

and

`def reduce(element), do: %Num{val: Reduce.reduce(element.left).val  \* Reduce.reduce(element.right).val}`

Without `Reduce.reduce` it just resolves to the function defined in the defimpl.

To view this discussion on the web visit [https://groups.google.com/d/msgid/elixir-lang-talk/CAOMhEnymB\_Oe34saSfPZu5%2BWLPRZMURx2YyL-Y%2BNa8B1tz4YAw%40mail.gmail.com](https://groups.google.com/d/msgid/elixir-lang-talk/CAOMhEnymB_Oe34saSfPZu5%2BWLPRZMURx2YyL-Y%2BNa8B1tz4YAw%40mail.gmail.com?utm_medium=email&utm_source=footer).

Shane EmmonsTue, May 19, 2015 at 3:31 AM

Interesting. I would have thought I could have done an ‘import Reduce’ in the module then to make it aware of the other implementations, but that doesn’t seem to work either.

  
  

> You received this message because you are subscribed to a topic in the Google Groups "elixir-lang-talk" group.  
> To unsubscribe from this topic, visit <https://groups.google.com/d/topic/elixir-lang-talk/Ke-Y36hnALE/unsubscribe>.  
> To unsubscribe from this group and all its topics, send an email to [elixir-lang-talk+unsubscribe@googlegroups.com](mailto:elixir-lang-talk+unsubscribe@googlegroups.com).  
> To view this discussion on the web visit [https://groups.google.com/d/msgid/elixir-lang-talk/CAOMhEnymB\_Oe34saSfPZu5%2BWLPRZMURx2YyL-Y%2BNa8B1tz4YAw%40mail.gmail.com](https://groups.google.com/d/msgid/elixir-lang-talk/CAOMhEnymB_Oe34saSfPZu5%2BWLPRZMURx2YyL-Y%2BNa8B1tz4YAw%40mail.gmail.com?utm_medium=email&utm_source=footer).  
> For more options, visit <https://groups.google.com/d/optout>.

  
--   
You received this message because you are subscribed to the Google Groups "elixir-lang-talk" group.  
To unsubscribe from this group and stop receiving emails from it, send an email to [elixir-lang-talk+unsubscribe@googlegroups.com](mailto:elixir-lang-talk+unsubscribe@googlegroups.com).  
To view this discussion on the web visit [https://groups.google.com/d/msgid/elixir-lang-talk/1432017070759.c210eba2%40Nodemailer](https://groups.google.com/d/msgid/elixir-lang-talk/1432017070759.c210eba2%40Nodemailer?utm_medium=email&utm_source=footer).

José ValimTue, May 19, 2015 at 4:13 AM

import is completely lexical, it makes a function available in the current file but it does not affect the current module at all.

In Ruby, because data and behaviour are coupled, it makes sense for including modules into a class or other modules because the common way to add functionality is by coupling more modules to the current object/data.

In Elixir, however, there are no objects and data and behaviour are decoupled. So we rarely include modules into other modules because it wouldn't have much purpose. Instead, we directly and explicitly invoke the other module. import is just a mechanism so you don't need to refer the imported module by full name every time.

**José Valim**

[www.plataformatec.com.br](http://www.plataformatec.com.br/)

Skype: jv.ptec

Founder and Lead Developer

To view this discussion on the web visit [https://groups.google.com/d/msgid/elixir-lang-talk/CAGnRm4JjAdcq13izo8Ek6nkkk95AwQBGjth%2BHHREQfpzoQUZZw%40mail.gmail.com](https://groups.google.com/d/msgid/elixir-lang-talk/CAGnRm4JjAdcq13izo8Ek6nkkk95AwQBGjth%2BHHREQfpzoQUZZw%40mail.gmail.com?utm_medium=email&utm_source=footer).
