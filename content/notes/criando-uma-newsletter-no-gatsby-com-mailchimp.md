---
title: "Criando uma Newsletter no Gatsby com Mailchimp"
date: '2020-07-05T14:11:17+00:00'
category: webclip
summary: 'O post mostra como automatizar uma newsletter no Gatsby com Mailchimp usando RSS, campanha automática, double opt-in e um formulário com gatsby-plugin-mailchimp.'
tags: ["gatsby", "mailchimp", "newsletter", "rss"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Criando uma Newsletter no Gatsby com Mailchimp"
    url: "https://gabrieluizramos.com.br/criando-uma-newsletter-no-gatsby-com-mailchimp"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/gabrieluizramos-com-br--criando-uma-newsletter-no-gatsby-com-mailchimp.md"
    kind: repo
---

O texto descreve uma forma de automatizar uma newsletter em um blog com Gatsby e Mailchimp. A integração se apoia em um feed RSS para expor os posts, em uma campanha automatizada do tipo Share blog updates no Mailchimp e em um formulário de inscrição ligado ao plugin gatsby-plugin-mailchimp.

## Fichamento

- A newsletter é apresentada como uma inscrição por e-mail para receber novidades e publicações de um site ou blog.
- A automação parte de um feed RSS, que o Mailchimp consulta para disparar e-mails quando houver conteúdo novo.
- O autor divide a implementação em três partes: feed RSS, campanha no Mailchimp e formulário de assinatura.
- O feed é gerado no Gatsby com o plugin gatsby-plugin-feed e pode ser ajustado para incluir apenas os posts desejados.
- A campanha no Mailchimp é criada em Create -> Email, escolhendo Automated e a categoria Share blog updates.
- A configuração da campanha passa por RSS Feed, Recipients, Setup, Template, Design e Confirm.
- O texto recomenda ativar double opt-in para confirmar a inscrição por e-mail e reduzir cadastros falsos.
- Também é possível ativar reCAPTCHA para aumentar a confiabilidade do formulário.
- O formulário de assinatura usa o plugin gatsby-plugin-mailchimp para cadastrar e-mail e nome na audiência.
- O endpoint de cadastro pode ser obtido a partir de um formulário embutido gerado pelo próprio Mailchimp.
- O plugin aceita a opção timeout, útil quando a resposta do Mailchimp demora mais do que o esperado.
- No componente de newsletter, o autor controla os estados de envio e resposta para mostrar mensagens de sucesso, erro ou aviso.
- O formulário desabilita o botão durante o envio para evitar múltiplas requisições.
- Ao final, novos posts do feed RSS passam a ser enviados automaticamente para a audiência cadastrada.
