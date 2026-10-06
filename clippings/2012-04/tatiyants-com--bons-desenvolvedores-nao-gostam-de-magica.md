---
url: "http://tatiyants.com/good-devs-dont-like-magic/"
captured_at: "2012-04-03T11:28:21-03:00"
title: "Bons desenvolvedores não gostam de mágica"
domain: "tatiyants-com"
---

### Sent to you by Thiago Silva via Google Reader:

## 

[Bons desenvolvedores não gostam de mágica](http://feedproxy.google.com/~r/imasters/~3/_vYjLxWtVKQ/story01.htm)

via [iMasters -](http://imasters.com.br/) by Alex Tatiyants () on 4/3/12

  

Recentemente, vi um tweet de alguém reclamando sobre os projetos de banco de dados do Visual Studio:

> Projetos de dados do Visual Studio - soa como uma ideia decente até você descobrir que foi concebido por pessoas que nunca construíram um app db para o mundo real.

Isso me fez lembrar a nossa própria [experiência](http://tatiyants.com/database-source-control-revisited/) com esta tecnologia. Tentamos usá-la, mas nos decidimos pelo db migration. E, apesar de haver muitas razões para não escolhê-la, provavelmente o mais convincente foi pelo fato da sua abordagem ter sido muito “mágica”.

#### O que, exatamente, quero dizer com “mágica”?

As soluções "mágicas" se identificam pela maneira que elas escondem (ocultam?) a implementação básica. Elas se apresentam ao desenvolvedor com uma proposta diabólica: facilitarei para que você tenha tudo feito, desde que não me pergunte como eu trabalho.

O projeto VS db é um estudo de caso clássico em soluções mágicas. Seu trabalho é ajudar você a gerenciar alterações de banco de dados e ele faz isso comparando o esquema atual (ou seja, desenvolvimento) com alguma versão base (ou seja, produção). Essa comparação resulta em um arquivo delta, no qual você pode, então, aplicar à linha de base

O problema é que é muito difícil prever o que vai estar no arquivo delta (especialmente em projetos com mudanças de bases de dados). Assim, para usar projeto db do Visual Studio você tem que confiar que ele sempre fará a coisa certa. Você precisa acreditar em magia.

#### Mas o que há de errado com Magia?

Bom, os bons desenvolvedores\* não gostam de mágica. Eles querem entender exatamente o que está acontecendo por dentro. Eles querem saber como a máquina começou a partir do ponto A ao ponto B. O mais importante, eles querem estar no controle do seu código (e não o contrário).

Bons desenvolvedores também sabem que a magia tem um custo. Esse custo é pago quando as coisas não funcionam exatamente como você esperava. De repente, você tem que cavar seu framework através de um labirinto de abstrações para entender o que deu errado.

É por isso que o migration é tão amigo dos desenvolvedores. Não há mistério aqui: arquivos sequencialmente numerados são aplicados, um a um para o banco de dados. Você pode ver exatamente quais mudanças estão sendo feitas a cada passo; e pode ver, também, exatamente onde a sua versão de banco de dados está atualmente, etc. Sem mágica!

#### Mas até um certo ponto não é tudo mágica?

Percebi que qualquer abstração pode ser considerada mágica. Por exemplo, um compilador é mágica: você confia cegamente nele para transformar a sua origem em um binário executável.

A questão é que para certas abstrações, o equilíbrio entre a transparência e a magia faz sentido. Claro, você pode descobrir exatamente o que o compilador está fazendo nos bastidores, mas por que você iria querer?

Além disso, nem sempre é óbvio quando essa troca faz sentido. Pegue o [CoffeeScript.](http://tatiyants.com/coffeescript/) Por um lado, um monte de bons desenvolvedores consideram que ele seja uma abstração muito útil de JavaScript. Por outro lado, alguns fazem uma [defesa convincente](http://ryanflorence.com/2011/2012/case-against-coffeescript/) de que o custo de obscurecimento é demasiado elevado.

\* Falando nisso, eu não acho que seja para todos os desenvolvedores. Na minha experiência, desenvolvedores medíocres / ruins são geralmente muito mais dispostos a aceitar soluções mágicas.

Você também pode gostar de:

- [Coisas que eu gostaria de saber como um estudante ciência da computação](http://tatiyants.com/leaving-solution-land/)
- [Criando um tema WordPress](http://tatiyants.com/creating-a-wordpress-theme/)
- [Um desenvolvedor social](http://tatiyants.com/a-social-developer/)
- [Tribos de desenvolvedor](http://tatiyants.com/developer-tribes/)
- [Deixando a Terra das Soluções](http://tatiyants.com/leaving-solution-land/)

*\*\*\**

*Artigo original disponível em: <http://tatiyants.com/good-devs-dont-like-magic/>*

[anexo ausente]

|  |  |
| --- | --- |
| [9bcafcd24ef5e7a319a7e300c0d5b221.gif](http://share.feedsportal.com/viral/sendEmail.cfm?lang=pt&amp;title=Bons+desenvolvedores+n%C3%A3o+gostam+de+m%C3%A1gica&amp;link=http%3A%2F%2Fimasters.com.br%2Fartigo%2F24024%2Fdesenvolvimento%2Fbons-desenvolvedores-nao-gostam-de-magica) | [75b9131ce15803402621ad7d693d4dd1.gif](http://res.feedsportal.com/viral/bookmark_pt.cfm?title=Bons+desenvolvedores+n%C3%A3o+gostam+de+m%C3%A1gica&amp;link=http%3A%2F%2Fimasters.com.br%2Fartigo%2F24024%2Fdesenvolvimento%2Fbons-desenvolvedores-nao-gostam-de-magica) |

  
  
[[anexo ausente]](http://da.feedsportal.com/r/130577494892/u/49/f/546640/c/33212/s/1e0daeab/kg/312/a2.htm)[anexo ausente][anexo ausente]

  

### Things you can do from here:

- [Subscribe to iMasters -](http://www.google.com/reader/view/feed%2Fhttp%3A%2F%2Fimasters.uol.com.br%2Ffeed%2F?source=email) using **Google Reader**
- [Get started using Google Reader](http://www.google.com/reader/?source=email) to easily keep up with **all your favorite sites**
