---
url: "http://tableless.com.br/i18next-para-internacionalizacao/"
captured_at: "2014-10-18T07:16:09-03:00"
title: "i18next para Internacionalização"
domain: "tableless-com-br"
---

![b4f6fbd1ecbd8080f31374f22011872b.jpg](tableless-com-br--i18next-para-internacionalizacao/b4f6fbd1ecbd8080f31374f22011872b.jpg)

Eu nunca me importei até que em um belo dia, um cliente teve essa necessidade e foi aí que precisei pensar, pesquisar e aprender sobre internacionalização. Participei de um projeto para a copa do mundo e o conteúdo deveria ser suportado por no mínimo 3 linguas diferentes: o inglês, espanhol e o português. Mas eu nunca tinha feito nada multilinguagem e nesse momento quase bateu o desespero. Acho que a pior dificuldade foi de me expressar, porque até então eu não tinha noção de que o termo **internacionalização** seria a palavra chave pra isso tudo.

Os primeiros questionamentos que eu me fiz foram:

- “Vou ter que fazer 3 sites diferentes?”
- “Vou ter mais trabalho que o normal?”
- “Como eu vou pesquisar sobre alguma lib que me ajude com isso? Será que existe?”

Antes de ir adiante, vamos ver o significado da coisa segundo o dicionário: **Tornar-se internacional; Espalhar ou difundir por vários países.**

Depois de toda essa introdução, finalmente apresento a vocês o maestro da orquestraque pode ser a solução para os seus problemas: O [i18next](http://i18next.com/ "site da lib i18next")!

Algumas considerações sobre esta lib:

- Seu suporte não é só para JavaScript.
- Possui integração com o jQuery.
- Todo seu conteúdo textual é inserido em um JSON.
- Documentação completa, fácil e direta.
- Você pode traduzir todo e qualquer texto do seu projeto, seja ele um *title*, *alt*, ou de qualquer outro atributo.
- Você pode detectar a linguagem do usuário e inserir o conteúdo de acordo com seu idioma.
- Ativar a internacionalização no clique.

Vou descrever os passos para você conseguir chegar [neste resultado](http://thulioph.github.io/i18next-internacionalizacao/ "Resultado final") que será acessível para espanhol, inglês e português.

*ps: não levem em conta as más práticas nem a nomenclatura, apenas criei a página para ajudar no entendimento.*

## Como iniciar?

**Estrutura básica**

As traduções do conteúdo deverão ser subpastas da pasta `locales` e precisam conter um arquivo `translation.json` com o json das traduções.

Então para o nosso exemplo a estrutura fica desta forma:

`/locales -> /en-US -> translation.json  
 /locales -> /es -> translation.json  
 /locales -> /pt-BR -> translation.json`

### Configurações básicas

Para o texto da tradução ser inserido no local desejado você deve utilizar o atributo `data-i18n` que permite vários valores, passando o objeto com chave e valor. Caso o conteúdo traduzido seja um atributo, seu nome deverá ser inserido dentro de colchetes `[]` seguido de sua posição no JSON. Algo assim:

```

```

O HTML fica sem nenhum conteúdo textual, pois todo conteúdo será inserido de acordo com a linguagem de forma dinâmica.

Seguindo os passos para o HTML, você agora está pronto para o JavaScript, onde é preciso setar algumas configurações de inicialização. Algo como:

```
i18n.init({
  fallbackLng: 'en-US'
  ,debug: true
  ,fixLng: true
  ,load: 'current'
},

function(translation) {
  $('[data-i18n]').i18n();
  var appName = translation('app.name');
});
```

### Configuração detalhada

**fallbackLng** fallback para quando não for definida ou não for localizada a linguagem do usuário.

**debug** debug da lib, habilitando no console algumas informações que podem ser úteis para desenvolvimento.

**fixLng** preserva o cookie da linguagem setada pelo usuário para quando o mesmo for acessar novamente.

**load** faz o request apenas para a linguagem definida.

**$(‘[data-i18n]‘).i18n();** todos os atributos data-i18n recebem a tradução.

### Explicando

Por padrão a lib detecta a linguagem do navegador e insere o conteúdo de acordo, caso o idioma detectado não possua tradução, o que for definido em `fallbackLng` será o conteúdo inserido.

Se o idioma for definido a partir de um clique ou qualquer outra interação você seta uma nova linguagem, preserva o cookie e inicia a tradução:

```
$('elemento').on('click', function() {
  i18n.setLng('es', {fixLng: true}, function(translation){
    $('[data-i18n]').i18n();
  });
});
```

A lib é realmente bastante simples, não tem muito o que se fazer, seguindo os passos descritos, você consegue deixar seu conteúdo mais acessível e em vários idiomas. [Aqui](https://github.com/thulioph/i18next-internacionalizacao/) você encontra o repositório com o exemplo que foi mostrado e todo o código comentado.

Qualquer dúvida, crítica ou sugestão você pode deixar nos comentários ou entrar em contato comigo [anexo ausente]

---  
Este artigo foi escrito por [Thulio Philipe](http://tableless.com.br/author/thulioph/).

Visite o nosso site para mais posts sobre desenvolvimento web! [Tableless](http://tableless.com.br).

[[anexo ausente]](http://feeds.feedburner.com/~ff/tableless?a=V6VWBxwtKtM:OIyNvTLiglo:yIl2AUoC8zA)
[[anexo ausente]](http://feeds.feedburner.com/~ff/tableless?a=V6VWBxwtKtM:OIyNvTLiglo:D7DqB2pKExk)
[[anexo ausente]](http://feeds.feedburner.com/~ff/tableless?a=V6VWBxwtKtM:OIyNvTLiglo:7Q72WNTAKBA)
[[anexo ausente]](http://feeds.feedburner.com/~ff/tableless?a=V6VWBxwtKtM:OIyNvTLiglo:aKCwKftKxY0)
[[anexo ausente]](http://feeds.feedburner.com/~ff/tableless?a=V6VWBxwtKtM:OIyNvTLiglo:dnMXMwOfBR0)
[![461e440a1d3becc7e11e0f65f4ce18e3.gif](tableless-com-br--i18next-para-internacionalizacao/461e440a1d3becc7e11e0f65f4ce18e3.gif)](http://feeds.feedburner.com/~ff/tableless?a=V6VWBxwtKtM:OIyNvTLiglo:YwkR-u9nhCs)
[[anexo ausente]](http://feeds.feedburner.com/~ff/tableless?a=V6VWBxwtKtM:OIyNvTLiglo:JEwB19i1-c4)
[[anexo ausente]](http://feeds.feedburner.com/~ff/tableless?a=V6VWBxwtKtM:OIyNvTLiglo:wF9xT3WuBAs)
[[anexo ausente]](http://feeds.feedburner.com/~ff/tableless?a=V6VWBxwtKtM:OIyNvTLiglo:V_sGLiPBpWU)
[![980a0ed8254c7a6a3722903cbad9d965.gif](tableless-com-br--i18next-para-internacionalizacao/980a0ed8254c7a6a3722903cbad9d965.gif)](http://feeds.feedburner.com/~ff/tableless?a=V6VWBxwtKtM:OIyNvTLiglo:tYZ39nBRSfM)

[anexo ausente]
