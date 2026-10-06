---
url: "http://elcio.com.br/qual-e-exatamente-o-problema-com-eval/"
captured_at: "2012-06-12T13:31:38-03:00"
title: "Qual é exatamente o problema com eval()?"
domain: "elcio-com-br"
---

Para iniciar este post, é preciso deixar algo claro: diferente da minha postura com os polêmicos ponto-e-vírgula, em que sei que sou “promíscuo e relaxado”, eu sou muito reticente quanto ao uso de eval() em javascript. O principal motivo é que eval() me cheira a gambiarra. Mas tenho muita dificuldade em dizer porquê. Na verdade, acho mesmo que é só uma questão de elegância.

  

Já li muita coisa sobre o assunto, mas nenhum argumento me convenceu. Os dois principais argumentos são performance e segurança. Em minha opinião nem um dos dois argumentos procede.

  

### Performance

  

Em primeiro lugar, é preciso dizer que o argumento de que JSON tem pior performance raramente é verdade. Há alguns anos, código executado via eval não poderia ser cacheado ou pré-otimizado. Isso não é mais verdade hoje em dia. A V8 (Chrome), a Nitro (Safari) e a SpiderMonkey (Firefox) já trabalham com caching do código passado a eval em diversas circunstâncias. Além disso, pense nas situações em que eval seria útil. Não consigo imaginar uma em que performance seja um problema. Por exemplo, uso eval como um fallback para navegadores que não tem suporte nativo a JSON. Sinceramente, depois de um delay de dois segundos esperando por uma requisição Ajax, não faz absolutamente nenhuma diferença se interpretar esse retorno vai levar dez milissegundos a mais.

  

Alguém pode dizer que seria melhor nessa situação usar uma biblioteca JSON com validações, como [a do Douglas Crockford](https://github.com/douglascrockford/JSON-js). Mas isso acrescentaria 17Kb de código em troca de absolutamente nada. Alguém pode então argumentar que o que se ganha usando uma biblioteca dessas não é exatamente nada, mas pelo menos um validador do código antes da execução. Respondo a isso no final.

  

### Segurança

  

O segundo argumento mais usado contra o uso de eval() é segurança. O fato de executar uma string, gerada dinamicamente, e não código escrito diretamente por você, pode dar calafrios. Puxa, mas não dá para ter a menor ideia do que será executado! Um agressor não poderia usar isso para executar código arbitrário? Isso não abre as portas para ataques XSS ou man-in-the-middle?

  

Aqui também, ninguém nunca conseguiu me demonstrar um único caso em que isso fosse uma preocupação real. Imagine o caso de uso que citei acima, por exemplo, de fazer parsing de dados JSON vindos via Ajax. Embora o código que vá passar por eval() não esteja no seu javascript, ele efetivamente foi escrito por você, no servidor. Se alguém consegue acesso a sua aplicação server afim de enviar dados maliciosos para suas requisições Ajax, por que ele se daria ao trabalho de fazer isso se ele poderia simplesmente gerar Javascript malicioso ou HTML malicioso? Se alguém teve esse nível de acesso a seu servidor, XSS é a menor de suas preocupações.

  

Outra variação do argumento da segurança diz que se você usa eval() a partir de uma entrada de dados do usuário, isso sim poderia abrir as portas para a execução de código malicioso. É preciso lembrar aqui que código javascript roda no client. Assim, o fato de eu poder digitar um script malicioso num campo de formulário, por exemplo, não significa nada exceto o fato de que posso “invadir minha própria máquina”.

  

Claro, se você recebe os dados gerados por esse eval() no servidor sem validá-los, isso pode causar problemas. Mas, nesse caso, o problema não está no eval() mas em sua validação porca no servidor. Se não houvesse eval() no código, a mesma coisa poderia ser feita na Firebug ou no console do Chrome.

  

Há ainda a preocupação com buscar dados de um servidor externo e executá-los, o que faria com que seu site possa executar código malicioso. Bom, se você inclui javascript em sua página gerado pelo Google Analytics, e pelo Twitter, Facebook, AddThis e outros geradores de widgets, porque não confiaria em executar código dessas mesmas fontes via eval()? Qual é exatamente a diferença?

  

Em suma, se as fontes de dados para o eval() não são confiáveis, não use-as de jeito nenhum. O problema não está no eval().

  

### Qualidade de código

  

Um último argumento, menos usado mas em minha opinião mais relevante, tem a ver com a qualidade de código. O principal motivo que me faz evitar o uso de eval() é o fato de, se houver algum erro no código avaliado, será bem mais difícil debugar. O navegador vai acusar o número da linha do eval(). Esse é um forte argumento, mas não para todas as situações. Geralmente eu gero JSON no servidor com uma biblioteca ou módulo bastante confiáveis, tanto em PHP quanto em Python. Quais são sinceramente as chances de meu software falhar porque há um problema na biblioteca padrão de JSON do PHP?

  

Por isso, eu não costumo trocar um simples eval() pelo uso de uma biblioteca de JSON, por exemplo.

  

### Fazendo errado

  

Não importa quão útil e boa seja uma ferramenta, sempre há uma infinidade de maneiras erradas de usá-la. Vi esses dias código assim:

  

```
 eval('document.'+obj).className='selected'
```

  

Esse código é muito ruim, demonstrando um desconhecimento básico dos recursos da linguagem. Pode facilmente ser substituído por isso:

  

```
 document[obj].className='selected'
```

  

Entenda que este artigo questionando os argumentos comuns contra o uso de eval() não é uma defesa de seu uso, principalmente de seu uso indiscrimado.

  

### Seu argumento

  

Perdi alguma coisa? Há algo mais que precise ser dito? Por favor, fique à vontade para deixar seus comentários.

  
  
  
  

[[anexo ausente]](http://feedads.g.doubleclick.net/~a/0t736TgHcpwuRUmTjSQcnjV5SV4/0/da)  
[[anexo ausente]](http://feedads.g.doubleclick.net/~a/0t736TgHcpwuRUmTjSQcnjV5SV4/1/da)

  

[[anexo ausente]](http://feeds.feedburner.com/~ff/Fechatag?a=RsaT8N2WvFk:tTqXstYXwf4:yIl2AUoC8zA) [![3d367448f9b233e8897a67010597729b.gif](elcio-com-br--qual-e-exatamente-o-problema-com-eval/3d367448f9b233e8897a67010597729b.gif)](http://feeds.feedburner.com/~ff/Fechatag?a=RsaT8N2WvFk:tTqXstYXwf4:D7DqB2pKExk)

  
  
  
from fechaTag [http://elcio.com.br/qual-e-exatamente-o-problema-com-eval/?utm\_source=feedburner&utm\_medium=feed&utm\_campaign=Feed%3A+Fechatag+%28fechaTAG%29](http://elcio.com.br/qual-e-exatamente-o-problema-com-eval/?utm_source=feedburner&amp;utm_medium=feed&amp;utm_campaign=Feed%3A+Fechatag+%28fechaTAG%29)
