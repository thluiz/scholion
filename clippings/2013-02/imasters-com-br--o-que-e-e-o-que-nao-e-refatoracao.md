---
url: "http://imasters.com.br/desenvolvimento/o-que-e-e-o-que-nao-e-refatoracao-de-acordo-com-kent-beck-e-martin-fowler/"
captured_at: "2013-02-19T18:57:01-03:00"
title: "O que é e o que não é refatoração – de acordo com Kent Beck e Martin Fowler"
domain: "imasters-com-br"
---

Às vezes, um programador virá a mim e explicará que ele  não gosta do design de alguma coisa e que “vamos precisar fazer um monte de refatoração” para fazer a coisa direito. Isso não parece bom. E não parece refatoração ou…

  

[Confira o novo refcard de refatoração! – Interrupção do curador DZone.](http://refcardz.dzone.com/refcardz/refactoring-patterns)

  

Refatoração, como originalmente definido por Martin Fowler e Kent Beck, é:

  
> Uma alteração feita na estrutura interna do software para torná-lo mais fácil de entender e mais barato para modificar sem alterar seu comportamento observável… É uma forma disciplinada de limpar código que minimiza as chances de introduzir bugs.

  

A refatoração é feita para preencher atalhos, eliminar a duplicação e código legado e para tornar o design e a lógica claros. Para tornar melhor e mais claro o uso da linguagem de programação. Para tirar proveito das informações que você tem agora, mas que o programador não tem – ou das quais eles ainda não tiraram proveito. Simplifique sempre o código e torne-o mais fácil de compreender. Sempre o torne mais fácil e seguro para alterar no futuro.

  

Corrigir quaisquer bugs que você encontrar pelo caminho não é refatoração. Otimização não é refatoração. Intensificar o tratamento de erros e adicionar um defensive code não é refatoração. Tornar o código mais testável não é refatoração - embora isso possa acontecer como resultado de refatoração. Todas essas são coisas boas para fazer. Mas não são refatoração.

  

Os programadores, especialmente os de manutenção de código, sempre limpam o código como parte de seu trabalho. É natural e muitas vezes necessário para realizar o trabalho. O que Martin Fowler e outros fizeram foi [formalizar as práticas de reestruturação](http://www.amazon.com/Refactoring-Improving-Design-Existing-Code/dp/0201485672) de código, e [documentar um catálogo](http://martinfowler.com/refactoring/catalog/) de padrões comuns e comprovados de refatoração – as metas e as etapas.

  

Refatoração é simples. Proteja-se de cometer erros ao fazer testes primeiramente onde você puder. Faça mudanças estruturais para o código em pequenos passos, etapas independentes e seguras, e teste o código depois de cada uma dessas etapas para garantir que você não tenha mudado o comportamento – ainda funciona da mesma maneira, apenas parece diferente. Os padrões e as ferramentas de refatoração em IDEs modernas tornam a refatoração fácil, segura e barata.

  

## A refatoração não é um fim em si mesmo

  

A refatoração deveria ser uma prática que suporta fazer alterações ao código. Você refatora o código antes de fazer alterações, para que você possa confirmar a sua compreensão do código e torná-lo mais fácil e mais seguro de aplicar a sua mudança. Faça testes de regressão no seu trabalho de refatoração. Então, faça suas correções ou alterações. Teste novamente. E depois, talvez, refatore um pouco mais o código para tornar a intenção das mudanças mais claras. E teste tudo novamente. Refatorar, em seguida, mudar. Ou mudar, então refatorar.

  
> Você não decide refatorar. Você refatora porque você quer fazer outra coisa, e a refatoração ajuda a fazer essa outra coisa.

  

O escopo do seu trabalho de refatoração deve ser conduzido pela mudança ou pela correção que você precisa fazer – o que você precisa fazer para tornar a mudança mais segura e mais limpa? Em outras palavras: não refatore pelo bem da refatoração. Não refatore o código que você não está mudando ou se preparando para mudar.

  

## Refatorando do zero para compreender

  

Existe também a refatoração do zero da obra [Working Effectively with Legacy Code](http://www.amazon.com/gp/product/0131177052?ie=UTF8&amp;tag=solisyntprog-20&amp;linkCode=as2&amp;camp=1789&amp;creative=9325&amp;creativeASIN=0131177052), de Michael Feather, o que Martin Fowler chama de “Refatorar para compreender”. É aqui que você pega o código que você não entende (ou não suporta) e o limpa de modo que você possa ter uma ideia melhor do que está acontecendo antes de começar a realmente trabalhar para mudá-lo de verdade, ou para ajudar a depurá-lo. Renomeie variáveis ​​e métodos, uma vez que você descobrir o que eles realmente querem dizer. Apague o código que você não quer ver (ou acha que não funciona), quebre instruções condicionais complexas, quebre rotinas longas em outras menores que você possa compreender.

  

Não se preocupe em analisar e testar todas essas mudanças. A meta é se mover rapidamente – este é um protótipo rápido e sujo para te dar uma visão do código e como ele funciona. Aprenda com ele e jogue fora. A refatoração do zero também permite testar abordagens de refatoração diferentes e aprender mais sobre as técnicas de refatoração. Michael Feathers recomenda que você mantenha notas sobre isso em qualquer coisa que não seja óbvia ou que foi especialmente útil, para que você possa voltar e fazer um bom trabalho mais tarde – em passos pequenos, disciplinados, com testes.

  

## E a refatoração em larga escala?

  

Você pode obter um grande retorno em entendimento e manutenção fazendo alterações de refatoração simples e óbvias: elimine a duplicação, mude nomes de variáveis e de método para ser mais significativo, extraia métodos para tornar o código mais fácil de entender e mais reutilizável, simplifique a lógica condicional, substitua um número mágico com uma constante, mova o código comum em conjunto.

  

Existe uma grande diferença entre refatoração menor em linha como esta e reestruturação de design mais fundamental – o que Martin Fowler se refere como “Refatoração grande”. Mudanças grandes e dispendiosas que carregam uma série de riscos técnicos. Isso não é limpeza de código e melhorar o design enquanto você está trabalhando: isso é redesign fundamental.

  

Algumas pessoas gostam de chamar de redesign ou reescrever ou replatforming ou reengenharia de um sistema de “[Refatoração em larga escala](http://www.infoq.com/news/2010/08/large-scale-refactoring)” porque tecnicamente você não está mudando o comportamento – a lógica do negócio e as entradas e saídas permanecem as mesmas; “apenas” o design e a implementação estão mudando. A diferença parece ser que você pode reescrever o código ou até mesmo todo um sistema e, desde que faça isso em etapas, você ainda pode chamá-lo de “refatoração”, mesmo que você esteja lentamente encapsulando um sistema legado com o novo código, ou [fazendo alterações de grande escala na arquitetura de um sistema](http://www.amazon.com/Refactoring-Large-Software-Projects-Restructurings/dp/0470858923).

  

As mudanças de refatoração em larga escala podem ser feias. Elas podem levar semanas ou meses (ou anos) para completar, exigindo mudanças em várias partes diferentes do código. Eles precisam ser discriminados e lançados em várias etapas, exigindo andaimes temporários e desvios, especialmente se você estiver trabalhando em pequenos sprints Agile. É aqui que as práticas como [Branch por abstração](http://continuousdelivery.com/2011/05/make-large-scale-changes-incrementally-with-branch-by-abstraction/) entram em ação, para ajudar você a gerenciar alterações dentro do código por um longo período de tempo.

  

Nesse meio tempo, você tem que continuar trabalhando com o código antigo e com o novo juntos, tornando o código mais difícil de seguir e mais difícil de mudar, mais frágil e cheio de bugs – o oposto do que refatoração deve alcançar. Às vezes, isso pode continuar para sempre – o trabalho de transição nunca é concluído porque a maioria dos benefícios é realizada mais cedo, ou porque o consultor que deu a ideia saiu para fazer outra coisa, ou o orçamento foi cortado, e você está preso na manutenção de um Frankensystem (um sistema Frankenstein).

  

## Isto é refatoração – aquilo não é

  

Misturar esse tipo de projeto pesado desenvolvido com a disciplina de refatoração-as-you-go é errado. Eles são fundamentalmente tipos diferentes de trabalho, com custos e riscos muito diferentes. Ele se confunde com o que as pessoas pensam que refatoração é, e como a refatoração deve ser feita.

  

Refatorar pode e deve ser apresentada na forma como você escreve e mantém o código – uma parte da disciplina diária de desenvolvimento, como a escrita de testes e a revisão de código. Isso deve ser feito em silêncio, de forma contínua e implicitamente. Torna-se parte do custo de fazer o trabalho, mostrando as estimativas e as avaliações de risco. Feito corretamente, ele não precisa ser explicado ou justificado.

  

Refatoração que leva alguns minutos ou uma hora ou duas, como parte de uma mudança, é apenas parte do trabalho. Refatoração que pode levar vários dias ou mais não é refatoração, e sim reescrita ou redesign. Se você tiver que reservar blocos explícitos de tempo (ou um sprint inteiro!) para refatorar código, se você tiver que obter permissão ou fazer um caso de negócio para limpeza de código, então você não está refatorando – mesmo se você estiver usando técnicas de ferramentas de refatoração, você está fazendo outra coisa.

  

Alguns programadores acreditam que é direito e responsabilidade deles fazer alterações fundamentais e importantes para o código, reinventar e reescrevê-lo em nome da refatoração e para o bem do futuro e para a sua arte. Às vezes, o correto é fazer o redesign e a reescrita do código. Mas seja honesto e claro. Não esconda isso com o nome de refatoração.

  

\*\*\*

  

*Texto original disponível em <http://agile.dzone.com/articles/what-refactoring-and-what-it-0>*

  

O post [O que é e o que não é refatoração – de acordo com Kent Beck e Martin Fowler](http://imasters.com.br/desenvolvimento/o-que-e-e-o-que-nao-e-refatoracao-de-acordo-com-kent-beck-e-martin-fowler/) apareceu primeiro em [iMasters](http://imasters.com.br/).

  
[anexo ausente]  
  

[![9bcafcd24ef5e7a319a7e300c0d5b221.gif](imasters-com-br--o-que-e-e-o-que-nao-e-refatoracao/9bcafcd24ef5e7a319a7e300c0d5b221.gif)](http://share.feedsportal.com/viral/sendEmail.cfm?lang=pt&amp;title=O+que+%C3%A9+e+o+que+n%C3%A3o+%C3%A9+refatora%C3%A7%C3%A3o+%E2%80%93+de+acordo+com+Kent+Beck+e+Martin+Fowler&amp;link=http%3A%2F%2Fimasters.com.br%2Fdesenvolvimento%2Fo-que-e-e-o-que-nao-e-refatoracao-de-acordo-com-kent-beck-e-martin-fowler%2F)

  

[![75b9131ce15803402621ad7d693d4dd1.gif](imasters-com-br--o-que-e-e-o-que-nao-e-refatoracao/75b9131ce15803402621ad7d693d4dd1.gif)](http://res.feedsportal.com/viral/bookmark_pt.cfm?title=O+que+%C3%A9+e+o+que+n%C3%A3o+%C3%A9+refatora%C3%A7%C3%A3o+%E2%80%93+de+acordo+com+Kent+Beck+e+Martin+Fowler&amp;link=http%3A%2F%2Fimasters.com.br%2Fdesenvolvimento%2Fo-que-e-e-o-que-nao-e-refatoracao-de-acordo-com-kent-beck-e-martin-fowler%2F)

  
  
  
[[anexo ausente]](http://da.feedsportal.com/r/158873097909/u/49/f/546640/c/33212/s/28bc36ca/a2.htm) [anexo ausente]  
  
[anexo ausente]  
  
  
  
from iMasters <http://imasters.com.br/desenvolvimento/o-que-e-e-o-que-nao-e-refatoracao-de-acordo-com-kent-beck-e-martin-fowler/>
