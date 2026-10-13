---
title: "Formatando datas no Ruby on Rails"
date: '2014-02-23T10:46:56-03:00'
category: webclip
summary: 'Mostra três jeitos de exibir um campo datetime no Rails: helper, after_find no modelo e, de forma mais flexível, um formato customizado em Time::DATE_FORMATS usado com to_s.'
tags: ["ruby-on-rails", "datetime", "formatting"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Formatando datas no Ruby on Rails - Simples Ideias"
    url: "http://simplesideias.com.br/formatando-datas-no-ruby-on-rails"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-02/simplesideias-com-br--formatando-datas-no-ruby-on-rails.md"
    kind: repo
---

O texto mostra três maneiras de exibir datas em um post no Rails. Primeiro, sugere um helper para formatar o valor antes de mostrá-lo no template. Depois, mostra a alternativa de fazer isso no modelo com after_find. A opção destacada é definir formatos próprios em Time::DATE_FORMATS e chamá-los com to_s.

## Fichamento

- Um campo datetime pode ser exibido abaixo de um post com um helper que aplica strftime.
- A mesma formatação também pode ser feita no modelo usando after_find.
- A forma apresentada como mais interessante no Rails é criar um formato novo em Time::DATE_FORMATS no environment.rb.
- Depois de definir o formato, a data é exibida com to_s e o nome do formato, como :post.
- O texto diz que é possível definir quantos formatos quiser, como :archive e :updated.
