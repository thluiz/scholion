---
title: "Implementando internacionalização (i18n) com JavaScript"
date: '2016-10-27T10:25:15-03:00'
category: webclip
summary: 'O texto explica i18n e L10n, mostra por que internacionalizar software e apresenta opções em JavaScript para formatar números e datas, detectar idioma e lidar com dados de localidade.'
tags: ["i18n", "javascript", "localizacao"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Implementando internacionalização (i18n) com JavaScript"
    url: "http://braziljs.org/blog/implementando-internacionalizacao-i18n-com-javascript/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-10/braziljs-org--implementando-internacionalizacao-i18n-com-javascript.md"
    kind: repo
---

O texto define internacionalização como a criação ou transformação de produtos para que possam ser adaptados a idiomas e culturas locais, e localização como a adaptação de um produto internacionalizado para uma região ou idioma específico. Também aponta motivos para internacionalizar software, como alcance internacional, competitividade, lucros maiores e diferenciação.

## Fichamento

- Internacionalização é o processo de criar ou transformar produtos para que possam ser adaptados a idiomas e culturas locais.
- Localização é a adaptação de um produto internacionalizado para uma região ou idioma específico.
- Internacionalizar software permite suportar múltiplas culturas, como formatos de moedas e datas.
- Expandir o software para outros mercados pode agregar valor ao produto e ao negócio.
- Entre os motivos citados estão competir com recursos disponíveis na internet, obter mais lucros e diferenciar o produto para exigências de outros mercados.
- O texto cita três soluções principais para i18n em JavaScript: EcmaScript Intl API, i18next.js e JQuery Globalize.
- A API Intl é nativa do JavaScript e serve para formatar números e datas e comparar strings em um idioma específico.
- A API está disponível em navegadores modernos e no Node.js a partir da versão 0.12.
- i18next.js é descrita como uma biblioteca popular para navegador e Node.js, com suporte a carregamento de traduções via XHR, detecção de idioma e documentação completa.
- JQuery Globalize funciona no navegador e como módulo Node.js e usa o repositório CLDR como base de dados de localidade.
- O texto menciona também o i18n-2, um módulo simples e leve para Node.js e Express.js com armazenamento JSON dinâmico.
- A conclusão afirma que nenhuma biblioteca JavaScript cobre todas as necessidades de internacionalização, mas algumas atendem à formatação de dados básicos.
