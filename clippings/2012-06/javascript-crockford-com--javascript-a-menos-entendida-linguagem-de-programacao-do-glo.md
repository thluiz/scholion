---
url: "http://javascript.crockford.com/pt/javascript.html"
captured_at: "2012-06-08T05:46:57-03:00"
title: "JavaScript: A Menos Entendida Linguagem de Programação do Globo!"
domain: "javascript-crockford-com"
---

# JavaScript: A Menos Entendida Linguagem de Programação do Globo!

[JavaScript: The World's Most Misunderstood Programming Language](http://javascript.crockford.com/javascript.html)

Douglas Crockford

JavaScript também conhecido por “Mocha”, “LiveScript”, “JScript” e “ECMAScript”, é uma das linguagens de programação mais populares do mundo. Praticamente todos os computadores pessoais do ao redor do globo, têm pelo menos um interpretador JavaScript instalado e em uso. Essa popularidade é devida inteiramente ao seu papel como “linguagem de script para o ambiente Web”.

Fora todo esse sucesso, poucas pessoas sabem que o JavaScript é uma linguagem excelente de programação, dinâmica, orientada a objetos e também para usos gerais (fora do ambiente Web). Mas umas dúvidas surgem na mente: Como isso pode ser um segredo? Porque essa linguagem é tão mal compreendida?

**O Nome**

O prefixo “Java” sugere que o JavaScript possui de alguma forma uma relação com o Java da Sun, isto é, uma sub-linguagem ou uma versão menos capaz do Java. Java é simplesmente Java interpretado. JavaScript é uma linguagem totalmente diferente.

JavaScript tem uma similaridade sintática com o Java, mas do que com o Java tem com o C. Mas não é uma sub-linguagem do Java, assim como o Java não é uma sub-linguagem do C. É muito melhor do que o Java em aplicações em que o próprio Java (chamado Oak antigamente) fora originalmente projetado para poder implementá-las.

Além do mais, o JavaScript não foi desenvolvido na Sun Microsystems, a casa do Java. Mas sim pela Netscape. Esta linguagem foi originalmente chamada de “LiveScript”, mas este nome não era confuso o bastante.

O sufixo “Script” sugere que não é uma linguagem de programação real, que uma linguagem de script é menos capaz do que uma linguagem de programação. Mas isso é realmente um assunto de profissionalismo. Comparado com o C, o JavaScript consegue um expressivo poder de performance e dinamismo.

**Lisp vestido de C**

A sintaxe do JavaScript é parecida com a do C, incluindo as chaves “{}”, e o suporte para a declaração “for”, com essas semelhanças o JavaScript parece ser mais uma linguagem de programação procedural comum. É óbvio que isso é um equívoco porque o JavaScript tem muito mais a ver com uma linguagem funcional como o [Lisp ou Scheme](http://javascript.crockford.com/little.html "Crockford Page")  do que com o C ou o próprio Java. O JavaScript tem arrays ao invés de listas e objetos ao invés de listas de propriedades. Funções são primeiramente classes. Ele tem closures. Você pode utilizar os lambdas sem ter a necessidade de utilizar todos aqueles parênteses.

**Typecasting (Conversão de Tipos)**

O JavaScript foi projetado pra rodar no navegador Netscape. O seu sucesso o conduziu para se tornar uma característica padrão em praticamente todos os navegadores. O resultado disso foi a necessidade de typecasting. JavaScript é o [George Reeves](http://www.amazon.com/exec/obidos/ASIN/B000KWZ7JC/wrrrldwideweb "George Reeves")  das linguagens de programação. Pois se adequa bem para classes de grande porte em aplicações não relacionadas com o mundo Web.

**Mudando o Objetivo**

As primeiras versões do JavaScript eram muito fracas e careciam de muitas funcionalidades. Faltavam nelas manipuladores de exceção, funções privadas, e herança. Mas o JavaScript no seu formato atual remete sim, a uma linguagem orientada a objetos. Embora muitas das opções da linguagem são baseados em formatos não muito bem desenvolvidos.

**Alguns Probleminhas**

Nenhuma linguagem de programação é perfeita. O JavaScript tem as suas próprias falhas, como sobrecargas (overloading) de “+” pra representar operações matemáticas de adição e também para concatenação como um tipo de coerção (é decidido na hora se o código está somando ou concatenando), e o erro consciente do uso da expressão “with” deve ser evitado. Aliado a isto tem as políticas de palavras reservadas que são muito rígidas. E o acréscimo de ponto-e-vírgula é uma grande falha, assim como era o uso da notação de expressões regulares. Esses erros deviam conduzir a erros de programação, e a colocar em cheque a estrutura da linguagem. Ainda bem que muitos desses problemas podem ser minimizados com um bom programa [lint (curativo)](http://www.crockford.com/javascript/lint.html "lint") .

A estrutura da linguagem como um todo é bastante sólido e completo. De um modo surpreendente o comitê ECMAScript não parece muito interessado em corrigir esses problemas (talvez eles estão interessados em crias novos).

**Aplicações Não Bem Projetadas**

Algumas das aplicações mais antigas do JavaScript eram um tanto bugadas. Isso repercutiu negativamente na linguagem. Misturado com tudo isso essas aplicações eram adicionadas em navegadores horríveis e propensos a falhas.

**Livros de Má Qualidade**

Quase todos os livros de JavaScript são horríveis. Eles possuem erros, exemplos pobres e promovem más práticas de programação. As características importantes da linguagem são explicadas de uma maneira pobre e vazia, ou então são simplesmente deixadas de lado. Eu tenho examinado vários livros de JavaScript, e um eu posso recomendar é: [JavaScript: The Definitive Guide (5th Edition) de David Flanagan](http://www.amazon.com/exec/obidos/ASIN/0596101996/wrrrldwideweb "The Definitive Guide") . (Atenção autores: Se vocês escreveram algum livro bom sobre o assunto, por favor, me envie uma cópia de avaliação).

**Sub-Norma da Norma**

A [ECMA](http://www.ecma-international.org/ "ECMA")  é o órgão que [publica a especificação oficial da linguagem](http://www.ecma-international.org/publications/standards/Ecma-262.htm "ECMA JavaScript publication") . Mas como era de se esperar esta especificação não possui muita qualidade e é extremamente pobre. Ela é difícil de ler e de ser entendida. Isso tem sido uma contribuição para o problema dos livros ruins, porque os autores tem sido incapazes de utilizar os documentos com as normas e melhorar com a sua própria compreensão da linguagem. ECMA e o [TC39](http://www.ecma-international.org/memento/TC39.htm "TC39 Programming and Scripting languages")  devem estar muito envergonhados.

**Amadores**

A maioria das pessoas que programam em JavaScript não são programadores. Faltam nessas pessoas treinamento, e disciplina para escrever um bom programa. Com o poder expressivo que o JavaScript possui essas pessoas podem ser capazes de fazer coisas surpreendentes com essa linguagem, de qualquer forma… Isso tem dado ao JavaScript a reputação de estar limitado a amadores, que não é adequada a programadores profissionais. É claro que isso não é simplesmente o caso.

**Orientação a Objetos**

O JavaScript é orientado à objetos? Bem, ele contém objetos que podem conter dados e métodos que agem sobre esses dados. Objetos podem conter outros objetos. O JavaScript não possui classes, mas possui construtores que são capazes de fazer o que as classes fazem, incluindo agir como contêineres para classes de variáveis e métodos. Ele não possui herança orientada a classe, mas tem herança orientada a protótipo.

Os dois modos de se fazer sistema de objetos são por herança (é-a) e por agregação (tem-a). O JavaScript tem a capacidade de fazer os dois modos mas por sua natureza dinâmica, ele permite o uso de agregação. Alguns debatem que o JavaScript não é verdadeiramente orientado à objetos porque ele não provê um modo para esconder informações. Isto é, objetos não podem possuir variáveis e métodos privados: Todos os membros são públicos. Mas isso não é de todo verdade, pois os objetos do JavaScript podem possuir variáveis e métodos privados (Clique [aqui](http://www.crockford.com/javascript/private.html "JavaScript variables and private methods") , e veja como é possível). Mas é claro, poucos sabem disso, pois o JavaScript é a linguagem de programação pior entendida no mundo.

Alguns argumentam que o JavaScript não é verdadeiramente orientado à objetos porque não possui herança. [Mas na verdade essa linguagem não somente aceita herança como também outros modelos de reuso de código](http://javascript.crockford.com/inheritance.html "Inheritance and other reuse patterns") .

Copyright 2001 Douglas Crockford. [All Rights Reserved Wrrrldwide.](http://www.crockford.com/)
