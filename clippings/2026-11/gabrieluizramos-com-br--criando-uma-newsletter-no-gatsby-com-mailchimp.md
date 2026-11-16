---
url: "https://gabrieluizramos.com.br/criando-uma-newsletter-no-gatsby-com-mailchimp"
captured_at: "2026-11-16T04:11:03+00:00"
title: "Criando uma Newsletter no Gatsby com Mailchimp"
domain: "gabrieluizramos-com-br"
---

Recentemente implementei uma Newsletter aqui no blog (inclusive você participar se quiser, é só se cadastrar no fim do post!) utilizando [Mailchimp](https://mailchimp.com/) e foi uma integração bem legal de se fazer.

Como é algo bem comum nos nesse cenário de blogs (e qualquer outro tipo de site) talvez possa ser útil para você também.

* * *

### [#](#mas-antes-de-tudo-o-que-e-uma-newsletter)Mas, antes de tudo, o que é uma Newsletter?

`Newsletter` (ou "Boletim Informativo") é o nome dado pra modalidade de inscrição onde você cadastra seu e-mail e recebe novidades e uma série de publicações de algum produto, serviço ou site. Talvez você receba em seu e-mail diariamente algumas notícias e posts de algum outro blog que você se cadastrou ou site que costuma acessar (talvez sua inscrição no Medium).

Isso que é uma Newsletter.

* * *

### [#](#bora-la)Bora lá!

A ideia da Newsletter é deixá-la automatizada a partir de qualquer novo post ou conteúdo do seu site/blog.

Você consegue (utilizando o próprio Mailchimp) enviar emails para uma lista de usuários quando quiser de forma bem simples, sem necessariamente automatizar ou criar um feed (como vermos mais abaixo). Entretanto, para um blog ou algum serviço de notícias é interessante deixar tudo pronto para avisar as pessoas inscritas sobre qualquer conteúdo novo que esteja no ar.

Pra implementar uma Newsletter usando Mailchimp com esse modelo, vale a pena dividir o conteúdo em 3 partes:

*   Criação de um Feed RSS;
*   Criação da Campanha no Mailchimp (com ou sem opt-in duplo);
*   Desenvolvimento do formulário de assinatura.

Então, vamos por partes...

Para iniciar a integração, primeiro você precisa configurar e ter um feed RSS no seu site. Esse arquivo é um XML que contém informações úteis sobre os seus posts para que sistemas (e até leitores) possam consumir. Ele vai ser necessário para que o Mailchimp possa consumir e consultar as informações de posts novos e disparar os e-mails automaticamente.

Para fazer isso é bem fácil e já existe um plugin pronto no Gatsby: o [gatsby-plugin-feed](https://www.gatsbyjs.org/packages/gatsby-plugin-feed/).

A documentação dele tá bem bacana e é bem fácil de seguir, você consegue customizar os itens que vão aparecer no seu feed praticamente como qualquer outro plugin do Gatsby (no meu caso, eu [excluo todos os posts que estão como rascunho](https://github.com/gabrieluizramos/gabrieluizramos.com.br/blob/master/gatsby-config.js#L148) e não estão prontos para serem publicados).

Então o primeiro passo é configurar pra que seu feed exporte os posts da forma como mais se adequar à maneira que você gostaria de enviar os emails e quais informações serão úteis pra você. Disponibilize esse feed em alguma URL de sua preferência, no meu caso, [meu feed ficou assim](https://gabrieluizramos.com.br/feed.xml).

Provavelmente essa parte é a mais manual e a mais chatinha de todo o processo, já que aqui é que você precisa definir como seu disparo de e-mail vai funcionar.

Você vai precisar criar uma conta no site do [Mailchimp](https://mailchimp.com/). Durante o tutorial e processo de configuração da sua conta você consegue iniciar a criação de um template de e-mail ou adiar essa criação para o momento que for criar a sua Campanha (que é a nomenclatura que o Mailchimp usa para definir esses disparos de email).

Com a configuração da sua conta finalizada, para criar sua Campanha automatizada, no seu painel do Mailchimp, selecione `Create -> Email`. Isso fará com que uma modal abra para você selecionar o tipo de email que deseja configurar, com isso, clique em `Automated` e selecione a categoria `Share blog updates`. Com isso, essa modal mostrará uma opção para você selecionar uma audiênca (que é uma lista de emails que você pode configurar par disparo), essa audiência já virá com uma opção para você escolher após a configuração inicial da sua conta. Finalizada essa etapa, basta clicar em `begin` para iniciar a criação da sua Campanha.

Agora você irá configurar os detalhes de disparo, feed e template que utilizará, e é dividido em 6 etapas:

1.  RSS Feed: aqui você deve informar a URL do seu arquivo de Feed, que foi configurado e gerado. Após informar a URL, você deve informar quando os emails devem ser enviados. Marque os dias que você achar mais adequado e vale se atentar ao timezone que o Mailchimp utiliza (Eastern) e fazer um "de -> para" da timezone que você deseja disparar;
2.  Recipients: aqui você seleciona a audiência (aquele público alvo da sua lista) que receberá os emails dessa campanha. Se quiser segmentar ou criar algumas tags para dividir quem receberá as novidades, você também consegue nessa etapa;
3.  Setup: é a etapa que você vai configurar alguns detalhes dos emails que serão enviados (assunto, descrição, nome do remetente e outras informações);
4.  Template: é onde você escolhe a base do seu template, com quantas colunas quer e e qual modelo já existente prefere utilizar;
5.  Design: a parte mais trabalhosa de todo o processo, onde você vai definir os blocos e as informações do seu template de email. Vale prestar bastante atenção aqui pros blocos existentes que contém informação **RSS** (o RSS Header e RSS Items), eles já vem com alguns dados prontos pra facilitar a criação do seu template. Pra facilitar a sua criação, tem [um guia](https://mailchimp.com/pt/help/rss-merge-tags/) que detalha todas as tags que o Mailchimp usa para mesclar os dados do feed RSS com o seu template que é bastante útil nessa etapa. Vale deixar uma dica aqui também: tive alguns problemas pra abrir o email no celular corretamente (mesmo enviando os emails de teste). Se tiver com esse problema também, sugiro que baixe o app do Mailchimp que você consegue ver o resultado do template da sua campanha em tempo real e da forma que vai aparecer no celular ao final de todo o processo;
6.  Confirm: é a etapa final, onde basicamente você revisa os dados e inicia a sua campanha com tudo o que configurou até o momento.

Passando essas etapas você pode confirmar o início da Campanha ou, caso te deixe mais confortável, esperar o desenvolvimento e inserção do formulário de inscrição que vamos ver a seguir (se quiser deixar tudo preparado antes de iniciar os disparos de sua Newsletter).

#### [#](#opt-in-duplo-ou-dupla-aceitacao)Opt-in duplo (ou dupla aceitação)

Outro ajuste que vale a pena ser feito agora é a configuração de opt-in (ou aceitação) duplo. Sabe quando você se inscreve em algum site e recebe, no endereço de email cadastrado, um email de confirmação?

Essa etapa de opt-in duplo serve justamente pra isso, configurar essa confirmação dupla de inscrição. Dessa forma, você evita que pessoas cadastrem emails falsos na sua lista de audiência, já que a pessoa interessada em receber suas novidades, receberá automaticamente um email para confirmar sua inscrição e, possivelmente, um recaptcha para confirmar que não é um robô.

Ativar essa opção é bem simples e você faz ela com alguns poucos cliques. Através do painel do Mailchimp ([admin.mailchimp.com](https://admin.mailchimp.com/)) é só acessar a aba `Audience`, depois clicar no select `Manage Audience -> Settings`, depois selecionar a opção `Audience name and defaults`. Ao acessar essa tela, existe uma parte chamada `Form settings` e é só selecionar o checkbox com a opção `Enable double opt-in`. Se quiser selecionar a opção `Enable reCAPTCHA` também você adiciona uma camada a mais de confiabilidade nos formulários de inscrição.

Caso não queira ativar essa opção, todos os usuários que preencherem seu formulário estarão automaticamente inscritos na sua audiência sem passar por qualquer "filtro".

Caso precise de mais um suporte, esses links de documentação do Mailchimp podem ser úteis:

*   [Compartilhe suas publicações de blog com o Mailchimp](https://mailchimp.com/pt/help/share-your-blog-posts-with-mailchimp/)
*   [Etiquetas de Mesclagem RSS (as merge tags)](https://mailchimp.com/pt/help/rss-merge-tags/)
*   [Sobre aceitação dupla (double opt-in)](https://mailchimp.com/pt/help/about-double-opt-in/)
*   [Encontra o ID do seu público](https://mailchimp.com/pt/help/find-audience-id/)

### [#](#desenvolvimento-do-formulario-de-assinatura)Desenvolvimento do formulário de assinatura

Chegou a hora de colocar a mão no código. Pra desenvolver esse formulário vamos utilizar o plugin [`gatsby-plugin-mailchimp`](https://www.gatsbyjs.org/packages/gatsby-plugin-mailchimp/).

Esse plugin basicamente disponibiliza uma função que é responsável por cadastrar os dados dos usuários (como email e nome) na lista da sua audiência no Mailchimp.

Para fazer isso, após instalar o plugin, é necessário consultar o endpoint disponibilizado pelo Mailchimp que é utilizado para realizar o cadastro desses usuários e pra fazer isso é bem simples e a forma mais fácil que encontrei foi a seguinte: na página da sua audiência (igual acessamos anteriormente), basta selecionar a opção `Signup forms` e depois a opção `Embedded forms`. Depois disso, você pode selecionar qualquer formulário que o próprio Mailchimp vai gerar um HTML para você utilizar no seu site e, nesse HTML, existirá uma tag `<form>` onde a `action` será justamente esse endpoint de cadastro que utilizaremos no plugin.

Caso queira simplesmente utilizar o formulário deles, sem configurar ou customizar mais nenhuma opção, você pode copiar e colar o código sem problemas. Mas ao longo desse passo vamos customizar um componente para tratar os estados e os disparos pra gente.

Feito isso, agora é só configurar o plugin no seu projeto (no arquivo `gatsby-config.js`):

```
module.exports = {
  plugins: [
    {
      resolve: 'gatsby-plugin-mailchimp',
      options: {
          endpoint: '', // url do seu endpoint
      },
    },
  ];
};
```

**Atualização**: enquanto desenvolvia o meu formulário, percebi que em alguns casos a resposta do Mailchimp demorava um pouco mais que o esperado e havia um timeout fixo de 3.5 segundos no plugin. Submeti uma Issue/PR para o mantedor e, a partir do [PR 68](https://github.com/benjaminhoffman/gatsby-plugin-mailchimp/pull/68/) o plugin aceita uma opção de `timeout`. Caso esteja com algum problema parecido e queira modificar o tempo utilizado para aguardar a resposta do Mailchimp é só inserir a opção `timeout` diretamente nas configurações do plugin no arquivo `gatsby-config`, contendo (em milissegundos) o valor desejado.

E vamos ao desenvolvimento!

Esse plugin exporta uma função `default` e, nas docs, o pessoal utiliza ela com o nome `addToMailChimp`. Então, no seu formulário, basta importá-la como:

```
import addToMailChimp from 'gatsby-plugin-mailchimp';
```

Essa deve receber como parâmetro o email do usuário e pode receber também um objeto com algumas informações adicionais (como nome da pessoa que se cadastrou) e retorna uma Promise.

Então, sua execução, no fim do processo será algo como:

```
import addToMailChimp from 'gatsby-plugin-mailchimp';

addToMailChimp('usuario@email.com', { FNAME: 'Nome' })
// .then()
// .catch()
```

Na [documentação](https://www.gatsbyjs.org/packages/gatsby-plugin-mailchimp/#returns) eles deixam bem claro que a Promise sempre será resolvida com `200` (mesmo que resolva com erro) e o que difere no caso de sucess/erro é o campo "result". Eu me deparei com um caso em específico que essa Promise falhava: nos casos onde o usuário, possivelmente, havia se cadastrado mas não tinha confirmado o email de opt-in duplo, então, seguindo boas práticas em geral, vale a pena tratarmos possíveis casos de erro, mesmo que isso não seja uma resposta 100% correta da API.

No meu caso, preferi tratar essa mensagem como um possível aviso e, fora isso, tratar os casos de sucesso/falha independentendemente com algumas mensagens separadas:

```
const messages = {
  success: 'Prontinho! Agora é só confirmar sua inscrição no email que você vai receber em instantes.',
  error: 'Ops! Parece que que tivemos algum erro... Por favor, tente novamente.',
  warning: 'Você deve ter recebido um email para confirmar sua inscrição. Caso não receba, tente novamente em alguns instantes por favor.'
};
```

Mantendo duas variáveis de estado (`result` e `sending`) para os estados de resposta do envio e carregamento. E trato os disparos e mensagens da seguinte forma:

```
import React, { useState } from 'react';

// import Form from 'components/form';

import addToMailChimp from 'gatsby-plugin-mailchimp';

const messages = {
  success: 'Prontinho! Agora é só confirmar sua inscrição no email que você vai receber em instantes.',
  error: 'Ops! Parece que que tivemos algum erro... Por favor, tente novamente.',
  warning: 'Você deve ter recebido um email para confirmar sua inscrição. Caso não receba, tente novamente em alguns instantes por favor.'
}

const Newsletter = () => {
  const [result, setResult] = useState('');
  const [sending, setSending] = useState(false);

  const getPathName = () => window.location.pathname;

  const subscribe = ({
    FNAME,
    email,
    pathname = getPathName()
  }) => addToMailChimp(email, { FNAME, pathname })

  const onSubmit = async (values) => {
    setSending(true);
    try {
      const { result } = await subscribe(values);
      setResult(result);
    } catch (err) {
      setResult('warning');
    }
    setSending(false);
  };

  const renderMessage = () => result && !sending && (
    <div>
      {messages[result]}
    </div>
  );

  return (
    // <Form onSubmit={onSubmit} disabled={sending} />
    {renderMessage()}
  );
};

export default Newsletter;
```

Dessa forma consigo tratar o estado de envio (disparando ou não a requisição) e desabilitar o botão de cadastro para que o usuário não consiga disparar várias vezes a requisição.

Deixei o componente comentado e o `import` apenas pois isso pode variar da forma como você lida com formulários. Acredito que com o que temos até aqui você já consegue implementar todo o fluxo de cadastro e disparo da Newsletter por si só, já que agora é apenas configurar as suas preferências de formulário como for mais adequada ao seu projeto.

Se quiser ver com mais detalhes como eu implementei esse formulário, você pode conferir diretamente no componente que criei de `Newsletter` que está no [github](https://github.com/gabrieluizramos/gabrieluizramos.com.br/blob/master/src/templates/post/article/newsletter/index.js).

* * *

### [#](#finalizamos-o-desenvolvimento-da-newsletter-%EF%B8%8F)Finalizamos o desenvolvimento da Newsletter! ✉️

Agora basta confirmar (caso ainda não tenha confirmado) a criação da sua campanha no painel do Mailchimp e pronto! Os próximos posts que forem adicionados ao seu arquivo do Feed RSS já serão automaticamente enviados para sua audiência usando o template e tudo que criamos ao longo desse processo.

Sei que o post ficou grande, mas espero que tenha gostado e que possa te ajudar caso precise implementar alguma coisa parecida utilizando Mailchimp e Feed RSS no seu site/blog com Gatsby!

Aproveitando que chegamos até aqui, o que acha de se inscrever na Newsletter que criei aqui pro blog seguindo exatamente esse processo?

É só preencher o formulário que tá aí embaixo e confirmar sua inscrição no email (opt-in duplo 😉) que você vai receber!
