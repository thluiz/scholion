---
title: "E-mail Newsletter Responsivo"
date: '2013-01-03T12:37:42-03:00'
category: webclip
summary: 'O texto mostra como adaptar newsletters por HTML e media queries, com foco em e-mail clients móveis, uso de tabelas, estilos inline, imagens e limites de compatibilidade.'
tags: ["design-responsivo", "newsletters", "media-queries", "email-html"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "E-mail Newsletter Responsivo"
    url: "http://tableless.com.br/e-mail-newsletter-responsivo/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-01/tableless-com-br--e-mail-newsletter-responsivo.md"
    kind: repo
---

O texto defende que técnicas de design responsivo também podem ser usadas em newsletters por e-mail. A proposta é combinar HTML antigo, estilos inline e media queries para adaptar o layout a telas menores, com atenção a compatibilidade, imagens e densidade de pixels.

## Fichamento

- O artigo parte do design responsivo e o trata como um conjunto de técnicas de CSS e estrutura que melhora usabilidade e acessibilidade em diferentes dispositivos.
- A aplicação do responsivo não fica restrita a sites; newsletters também podem receber adaptações para dispositivos móveis.
- Em e-mails, muitos clientes não leem CSS de forma confiável, então o código depende de estilos no HTML e do uso de tabelas.
- Media queries permitem sobrescrever estilos em clientes que as suportam, enquanto leitores mais antigos mantêm o layout de desktop.
- O texto lista clientes nativos e não nativos de leitura de e-mail que suportam ou não media queries.
- O layout deve considerar diferentes dispositivos, com fonte mínima de 13px em alguns apps, área clicável mínima de 44 por 44 pixels e larguras em porcentagem.
- Em e-mail templates, colunas funcionam melhor em desktop do que em smartphone, onde layouts mais simples evitam aperto visual.
- O artigo recomenda focar primeiro nos dispositivos móveis usando uma media query com max-device-width e reforçar estilos com !important.
- A estrutura-base mostrada usa uma tabela principal de 640px e duas colunas internas de 320px, com cellpadding para espaçamento interno.
- Para imagens, o texto propõe definir largura e altura na própria tag, esconder versões grandes em telas menores e, em alguns casos, usar background-size: cover.
- Outra solução apresentada é redimensionar imagens com width:100% e height:auto dentro de media queries.
- Para telas de alta densidade, como Retina Display, o texto sugere media queries específicas para device-pixel-ratio.
- Nas considerações finais, o artigo afirma que a web já não cabe em um único formato de tela e que adaptar layouts para cada mídia virou uma obrigação.
