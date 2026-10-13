---
title: "Variáveis de classe e de instância de classe em Ruby"
date: '2014-03-05T09:19:17-03:00'
category: webclip
summary: 'O texto explica a diferença entre variáveis de classe e variáveis de instância de classe em Ruby. Em herança, a primeira é compartilhada na hierarquia; a segunda fica associada a cada classe.'
tags: ["ruby", "variaveis-de-classe", "heranca"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Variáveis de classe e de instância de classe em Ruby - Guilherme Garnier"
    url: "http://blog.guilhermegarnier.com/2014/02/variaveis-de-classe-e-de-instancia-de-classe-em-ruby/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-03/blog-guilhermegarnier-com--variaveis-de-classe-e-de-instancia-de-classe-em-ruby.md"
    kind: repo
---

Ruby trata classes como objetos, então além de variáveis de instância de objetos também existem variáveis de classe e variáveis de instância de classe. O texto mostra que @@dias_de_ferias pertence à classe e @salario pertence a cada instância de Funcionario.

## Fichamento

- Variáveis de classe se referem à própria classe; variáveis de instância se referem a cada instância de uma classe.
- No exemplo, @@dias_de_ferias tem um único valor compartilhado, enquanto cada objeto Funcionario mantém seu próprio @salario.
- Como classes também são objetos em Ruby, elas podem ter variáveis de instância acessadas com @ dentro do escopo da classe ou de um método de classe.
- Em herança, variáveis de classe são compartilhadas entre Funcionario e Gerente.
- Ao alterar @@dias_de_ferias na subclasse, o valor também muda na superclasse, porque é a mesma instância.
- Já @bonus fica separado por classe, com um valor em Funcionario e outro em Gerente.
