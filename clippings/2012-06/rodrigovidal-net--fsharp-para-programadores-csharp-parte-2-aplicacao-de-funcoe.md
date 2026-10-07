---
url: "http://rodrigovidal.net/?p=737"
captured_at: "2012-06-15T09:42:55-03:00"
title: "F# para programadores C# – Parte 2 – Aplicação de Funções"
domain: "rodrigovidal-net"
---

Olá pessoal, vamos dar continuidade à série!

  

A parte 1 você encontra [aqui!](http://rodrigovidal.net/?p=727) É indicado que você leia o post anterior antes de continuar.

  

Neste ponto eu gostaria de recomendar um excelente livro de F# para quem está começando –> [Programming F# do Chris Smith](http://www.amazon.com/Programming-comprehensive-writing-complex-problems/dp/0596153643/ref=sr_1_1?ie=UTF8&amp;qid=1339727347&amp;sr=8-1).

  

Aplicações de Funções vs. Invocação de Métodos

  

Em linguagens funcionais como F#, é comum usar o termo aplicação, para dizer que uma função será executada com um conjunto de argumentos. Enquanto no C# invocamos um método a partir de um objeto.

  

Para invocar um método de um objeto no C# devemos fazer:

  

```

```

  

```
 obj.Foo(x);
```

  

```

```

  

onde obj representa uma objeto qualquer. Enquanto em F# as funções podem ser aplicadas diretamente.

  

```

```

  

```
 foo x
```

  

```

```

  

Funções de Dois Argumentos

  

C#

  

```

```

  

```
 obj.Foo(a,b);
```

  

```

```

  

F#

  

```

```

  

```
 foo a b
```

  

```

```

  

Repare que F# dispensa o uso de parênteses, de virgulas e do ponto e virgula no final, mantendo uma sintaxe mais sucinta.

  

O Resultado de uma função como argumento

  

C#

  

```

```

  

```
 Foo(Fee(x));  
 Foo(a, Fee(b));
```

  

```

```

  

F#

  

```

```

  

```
 foo (fee x)  
 foo a (fee b)
```

  

```

```

  

Assim como em Haskell em F# os parênteses servem para alterar a prioridade de execução.

  

Escrevendo suas próprias funções

  

Você pode agora criar uma arquivo hello.fsx, sendo FSX de FSharp Script. E adicione o seguinte código:

  

```

```

  

```
 let add a b = a + b  
 let inc a = add a 1  
 let double x = x + x  
 let quadruple x = double (double x)
```

  

```

```

  

Caso você esteja usando o VS basta usando ALT + Enter para que o script rode no console interativo. Caso esteja usando o REPL na linha de comando basta colocar C:\Program Files (x86)\Microsoft SDKs\F#\3.0\Framework\v4.0 no path das suas variáveis de ambiente do Windows e digitar fsi .

  

Em C#

  

```

```

  

```
 Func<int, int, int> add = (a, b) => a + b;  
 Func<int, int> inc = a => add(a, 1);  
 Func<int, int> @double = x => x + x;  
 Func<int, int> quadruple = x => @double(@double(x));
```

  

```

```

  

Bem parecido, no entanto podemos perceber que o F# trata funções como membros de primeira classe. Pois ele consegue inferir com facilidade o tipo da função sempre precisamos definir o tipo. Enquanto isso o C# trata a função como um objeto, Func, e o mecanismo de inferência não funciona tão bem para resolver isso no C#.

  

Por hoje era isso!

  

Abraço,  
  
Rodrigo Vidal

  

[[anexo ausente]](http://digg.com/submit?url=http%3A%2F%2Frodrigovidal.net%2F%3Fp%3D737&amp;title=F%23+para+programadores+C%23+&amp;ndash%3B+Parte+2+&amp;ndash%3B+Aplica&amp;ccedil%3B&amp;atilde%3Bo+de+Fun&amp;ccedil%3B&amp;otilde%3Bes)   [[anexo ausente]](http://www.reddit.com/submit?url=http%3A%2F%2Frodrigovidal.net%2F%3Fp%3D737&amp;title=F%23+para+programadores+C%23+&amp;ndash%3B+Parte+2+&amp;ndash%3B+Aplica&amp;ccedil%3B&amp;atilde%3Bo+de+Fun&amp;ccedil%3B&amp;otilde%3Bes)   [[anexo ausente]](http://www.stumbleupon.com/submit?url=http%3A%2F%2Frodrigovidal.net%2F%3Fp%3D737&amp;title=F%23+para+programadores+C%23+&amp;ndash%3B+Parte+2+&amp;ndash%3B+Aplica&amp;ccedil%3B&amp;atilde%3Bo+de+Fun&amp;ccedil%3B&amp;otilde%3Bes)   [[anexo ausente]](http://buzz.yahoo.com/buzz?targetUrl=http%3A%2F%2Frodrigovidal.net%2F%3Fp%3D737&amp;headline=F%23+para+programadores+C%23+&amp;ndash%3B+Parte+2+&amp;ndash%3B+Aplica&amp;ccedil%3B&amp;atilde%3Bo+de+Fun&amp;ccedil%3B&amp;otilde%3Bes)   [[anexo ausente]](http://www.dzone.com/links/add.html?title=F%23+para+programadores+C%23+&amp;ndash%3B+Parte+2+&amp;ndash%3B+Aplica&amp;ccedil%3B&amp;atilde%3Bo+de+Fun&amp;ccedil%3B&amp;otilde%3Bes&amp;url=http%3A%2F%2Frodrigovidal.net%2F%3Fp%3D737)   [[anexo ausente]](http://www.facebook.com/sharer.php?t=F%23+para+programadores+C%23+&amp;ndash%3B+Parte+2+&amp;ndash%3B+Aplica&amp;ccedil%3B&amp;atilde%3Bo+de+Fun&amp;ccedil%3B&amp;otilde%3Bes&amp;u=http%3A%2F%2Frodrigovidal.net%2F%3Fp%3D737)   [[anexo ausente]](http://delicious.com/save?title=F%23+para+programadores+C%23+&amp;ndash%3B+Parte+2+&amp;ndash%3B+Aplica&amp;ccedil%3B&amp;atilde%3Bo+de+Fun&amp;ccedil%3B&amp;otilde%3Bes&amp;url=http%3A%2F%2Frodrigovidal.net%2F%3Fp%3D737)   [[anexo ausente]](http://www.dotnetkicks.com/kick/?title=F%23+para+programadores+C%23+&amp;ndash%3B+Parte+2+&amp;ndash%3B+Aplica&amp;ccedil%3B&amp;atilde%3Bo+de+Fun&amp;ccedil%3B&amp;otilde%3Bes&amp;url=http%3A%2F%2Frodrigovidal.net%2F%3Fp%3D737)   [[anexo ausente]](http://dotnetshoutout.com/Submit?title=F%23+para+programadores+C%23+&amp;ndash%3B+Parte+2+&amp;ndash%3B+Aplica&amp;ccedil%3B&amp;atilde%3Bo+de+Fun&amp;ccedil%3B&amp;otilde%3Bes&amp;url=http%3A%2F%2Frodrigovidal.net%2F%3Fp%3D737)   [[anexo ausente]](http://www.linkedin.com/shareArticle?mini=true&amp;url=http%3A%2F%2Frodrigovidal.net%2F%3Fp%3D737&amp;title=F%23+para+programadores+C%23+&amp;ndash%3B+Parte+2+&amp;ndash%3B+Aplica&amp;ccedil%3B&amp;atilde%3Bo+de+Fun&amp;ccedil%3B&amp;otilde%3Bes&amp;summary=&amp;source=)   [[anexo ausente]](http://www.technorati.com/faves?add=http%3A%2F%2Frodrigovidal.net%2F%3Fp%3D737)   [[anexo ausente]](http://twitter.com/home?status=Reading+http%3A%2F%2Frodrigovidal.net%2F%3Fp%3D737)   [[anexo ausente]](http://www.google.com/buzz/post?url=http%3A%2F%2Frodrigovidal.net%2F%3Fp%3D737)

  
  
  
from Rodrigo Vidal <http://rodrigovidal.net/?p=737>
