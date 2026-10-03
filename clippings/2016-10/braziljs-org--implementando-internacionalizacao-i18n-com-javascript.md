---
url: "http://braziljs.org/blog/implementando-internacionalizacao-i18n-com-javascript/"
captured_at: "2016-10-27T10:25:15-03:00"
title: "Implementando internacionalização (i18n) com JavaScript"
domain: "braziljs-org"
---

# Implementando internacionalização (i18n) com JavaScript

![1d27d8206b3823cb1ff693e58b1b9478.png](braziljs-org--implementando-internacionalizacao-i18n-com-javascript/1d27d8206b3823cb1ff693e58b1b9478.png)

Então, você está expandindo seu negócio/produto e deseja alcançar mais usuários, que falam diferentes idiomas ou ainda, está trabalhando no desenvolvimento de algo e deseja que essa solução atinja um público elevado de diferentes nacionalidades?   
Se você respondeu sim para algumas das perguntas, venha conhecer mais sobre o processo conhecido como i18n. Caso a resposta tenha sido não, essa é a hora de conhecer algo que pode lhe ser útil no futuro, vamos lá!

**Internacionalização** é popularmente conhecido no mundo de desenvolvimento como `i18n` e trata-se de um processo de criação ou transformação de produtos e/ou serviços, de modo que eles possam facilmente ser adaptados para idiomas e culturas locais específicas. Enquanto a **Localização**, comumente conhecido como `L10n`, é o processo de adaptação de um produto internacionalizado para uma região ou idioma específico.
Em linhas gerais, a internacionalização é o processo de adaptar o software para suportar múltiplas culturas (formato de moedas, datas, e assim por diante), enquanto que a localização é o processo de implementação de uma ou mais cultura.

### Por que internacionalizar meu software?

**Expandir e diversificar** seu software no âmbito internacional é, com certeza, algo que vai agregar muito valor ao seu produto/serviço e trará mais segurança para o seu negócio.

**Competitividade internacional**: Uma vez que a maioria dos recursos disponíveis na internet estão em inglês, nada melhor do que o seu produto/serviço competir com esses e não apenas com o mercado interno.

**Lucros maiores**: Expandir seus produtos/serviços para além das fronteiras poderá resultar em maiores lucros, visto que terá a capacidade de conquistar clientes de outras regiões.

**Diferenciação**: Diferenciar o produto/serviço pode ser uma opção que trará uma grande vantagem; uma vez que o mercado internacional pode exigir mudanças nos produtos/serviços de sua empresa/marca.

### Buscando por soluções

Há milhares de bibliotecas**¹** que se propõem a auxiliar no processo de internacionalização de seus produtos, mas me limitarei a falar sobre apenas três delas.

- **EcmaScript Intl API**

Pode ser uma surpresa para alguns de vocês, mas o JavaScript tem suporte [nativo para a internacionalização na forma da API](http://www.ecma-international.org/ecma-402/1.0/), que é conhecido como ECMA-402.   
O `Intl` é um objeto disponível no objeto `window` que funciona como um espaço de nomes para o API de Internacionalização. Esta API fornece atualmente métodos para formatar números e datas e para comparar *strings* em um idioma específico.   
Segue uma [lista de métodos que a API dispõem e seus suportes](http://kangax.github.io/compat-table/esintl/).

**Suporte**: A API está disponível para os navegadores mais modernos como Chrome 29+, Firefox 36+, Opera 16+, Safari 10+, IE11+ e no Node.js a partir da versão 0.12.

- **i18next.js**

i18next é uma biblioteca de internacionalização muito popular para navegador ou qualquer outro ambiente de JavaScript, por exemplo, Node.js.   
A biblioteca julga-se interessante por algumas características como suporte para *back-end* (traduções de carregamento via [XHR](https://developer.mozilla.org/pt-BR/docs/Web/API/XMLHttpRequest)), detecção de idioma do usuário e uma documentação completa e intuitiva.

**Suporte**: A biblioteca funciona tanto no Node.js quanto em navegadores modernos como Chrome, Firefox, Opera, Safari, IE10+ e IE9 com ES5 Shim.

- **JQuery Globalize**

Uma biblioteca para internacionalização e localização. A biblioteca funciona tanto para o navegador quanto como um módulo Node.js.   
Globalize é baseada no [Repositório do Consórcio Unicode Common Locale de Dados (CLDR)](http://cldr.unicode.org/), que é o maior e mais extenso repositório padrão de dados de localidade disponível. Assim, ao contrário de bibliotecas que incorporam dados de localidade, se você usar Globalize será realmente fácil estar sempre atualizado com os últimos dados *CLDR*.

**Suporte**: A biblioteca funciona tanto para o navegador, como um módulo Node.js.
Na sua versão atual, Globalize 1.1.1, suporta todos os principais navegadores, incluindo o IE9+, Chrome, Firefox, Safari 5.1+ e Opera 12.1+.

**¹** [Mais de 1.308 repositório no GitHub com o termo **i18n**](https://github.com/search?l=JavaScript&o=desc&q=i18n&s=&type=Repositories&utf8=%E2%9C%93)

Ainda que eu tenha declarado que citaria apenas três possíveis soluções, me sinto no direito de compartilhar com vocês o [i18n-2](http://ejohn.org/blog/i18n-module-for-node-and-express-js/), um módulo de tradução simples e leve para Node.js e Express.js com armazenamento JSON dinâmico, desenvolvido por ninguém menos que [John Resig](https://twitter.com/jeresig).

### Conclusão

Vale lembrar que não existe nenhuma biblioteca JavaScript capaz de suportar todas as necessidades de internacionalização. Todavia, você deve ser capaz de usar algumas das disponíveis para a formatação de dados básicos.

Essa foi uma breve introdução sobre alguns tópicos importantes relativos à internacionalização (i18n) com JavaScript. Se você ficou curioso e quer aprender mais, dê uma atenção para os seguintes tópicos:
