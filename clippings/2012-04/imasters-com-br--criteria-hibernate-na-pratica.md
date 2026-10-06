---
url: "https://imasters.com.br/back-end/criteria-hibernate-na-pratica"
captured_at: "2012-04-03T10:15:28-03:00"
title: "Criteria Hibernate na prática"
domain: "imasters-com-br"
---

### Sent to you by Thiago Silva via Google Reader:

## 

[Criteria Hibernate na prática](http://feedproxy.google.com/~r/imasters/~3/_TaHj4gdfoA/story01.htm)

via [iMasters -](http://imasters.com.br/) by Camilo Lopes () on 4/3/12

  

Olá, pessoal! Se você está iniciando com o Hibernate, um dia vai ser apresentado ao Criteria. Realmente, quem usa o Criteria não quer voltar ao SQL para as funções mais básicas e só o faz nos casos extremos, nos quais o Criteria não atende. Então, neste artigo vou mostrar um pouco o que se pode fazer com o Criteria nas suas aplicações Java. Farei uma breve introdução neste primeiro artigo e no próximo vamos colocar mão na massa. Mas, por enquanto, quero que conheçam um pouco a sintaxe.

#### Criteria

O [Criteria Query API](http://docs.jboss.org/hibernate/core/3.3/reference/en/html/querycriteria.html) permite construir query expression em Java, possibilitando, assim, a checagem em tempo de compilação - ao contrário do HQL ou SQL. O Criteria API permite, de forma programática, construir objetos query a partir da interface org.hibernate.Criteria, que define os métodos disponíveis que precisamos para trabalhar com o Criteria.

Para persistir um objeto da classe, usamos o método createCriteria(), que retorna um objeto Criteria, que permite ter acesso a instância de persistência da classe. O createCriteria() pertence à interface Session. Então, se for preciso retornar todas propriedades de uma classe com Criteria, seria assim:

```
 Criteria critera = session.createCriteria(Produto.class)  
 List lista = criteria.list();
```

Bem mais simples do que o HQL. Este é o mesmo resultado com o from Produtos, que executamos no HQL e que fazemos no SQL: SELECT \* from mytable.

Vamos dizer que precisamos obter os produtos que tenham no nome “smartphone”, então, precisamos conhecer o método add() da classe Criteria, que tem como objetivo adicionar uma restrição em seu argumento. Uma outra classe importante é Restrictions class, do pacote org.hibernate.Criterion, que possui métodos static para as condições de restrições que precisamos. Veja o trecho do código:

```
 Criteria crit = sesion.createCriteria(Produto.class)  
 crti.add(Resctrictions.eq(“nome”, “smart phone”);  
 List list = crit.list();
```

#### Explicando o código:

Na primeira linha, nós criamos o objeto Criteria que fez a persistência em nossa entidade. Na linha 02, costumo ler da seguinte forma para facilitar a compreensão: “adicionando uma restrição a class persistida”. Na linha 03 é o resultado da restrição.

Um ponto importante é que não podemos fazer uma restrição de resultado usando o método eq/ne para propriedades com o valor null. Para isso, há métodos static especificos: o isNull() e o isNotNull().

Para realizar busca, temos os métodos like() e ilike(). Eles servem para quando precisamos buscar algo fornecendo apenas algumas informações para o buscador. Exemplo: traga todos os produtos que tem a palavra “smart”. A diferença é que o ilike é case-insensitive.

Outro detalhe importante que podemos informar é onde buscaremos a palavra: no inicio, no final - para ser exato -, ou em qualquer lugar. Exemplo:

```
 Criteria crit = session.createCriteria(Produto.class)  
 crit.add(Restrictions.like(“nome”, “smart%”));  
 List list = crit.list();
```

O símbolo % informa que a busca é por partes da string. No exemplo a seguir, eu seleciono para buscar no final dela.

```
Crit.add(Restrictions.like(“nome”, “smart”, MatchMode.end));
```

O MatchMode é um tipo de enumeration que possui quatro tipos diferentes de match: anywhere, end, exact, start.

E assim finalizo o primeiro artigo sobre Criteria. No próximo veremos mais algumas restrições interessantes.

 Espero que tenham gostado do artigo!

[anexo ausente]

|  |  |
| --- | --- |
| [9bcafcd24ef5e7a319a7e300c0d5b221.gif](http://share.feedsportal.com/viral/sendEmail.cfm?lang=pt&title=Criteria+Hibernate+na+pr%C3%A1tica&link=http%3A%2F%2Fimasters.com.br%2Fartigo%2F24039%2Fbanco-de-dados%2Fcriteria-hibernate-na-pratica) | [75b9131ce15803402621ad7d693d4dd1.gif](http://res.feedsportal.com/viral/bookmark_pt.cfm?title=Criteria+Hibernate+na+pr%C3%A1tica&link=http%3A%2F%2Fimasters.com.br%2Fartigo%2F24039%2Fbanco-de-dados%2Fcriteria-hibernate-na-pratica) |

  
  
[[anexo ausente]](http://da.feedsportal.com/r/130996439109/u/49/f/546640/c/33212/s/1e0d0b7b/a2.htm)[anexo ausente][anexo ausente]

  

### Things you can do from here:

- [Subscribe to iMasters -](http://www.google.com/reader/view/feed%2Fhttp%3A%2F%2Fimasters.uol.com.br%2Ffeed%2F?source=email) using **Google Reader**
- [Get started using Google Reader](http://www.google.com/reader/?source=email) to easily keep up with **all your favorite sites**
