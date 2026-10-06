---
title: "Assegurando a qualidade do seu código JavaScript"
date: '2012-07-09T10:31:25-03:00'
category: webclip
summary: 'O texto reúne ferramentas de lint para verificar sintaxe e padrões em JavaScript, explica que elas não validam a lógica do programa e compara JSLint, JSHint, Closure Linter e jQuery Lint.'
tags: ["javascript", "lint", "quality", "syntax"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Assegurando a qualidade do seu código JavaScript"
    url: "https://tableless.com.br/assegurando-a-qualidade-do-seu-codigo-javascript/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-07/tableless-com-br--assegurando-a-qualidade-do-seu-codigo-javascript.md"
    kind: repo
---

Ferramentas de lint ajudam a encontrar problemas de sintaxe e padrão no JavaScript, como variáveis não usadas, espaços em branco no fim de linha e ausência de ponto e vírgula. O texto também distingue esse tipo de verificação dos testes automatizados, que asseguram o funcionamento das aplicações.

## Fichamento

- Ferramentas de lint interpretam arquivos JavaScript e buscam erros de sintaxe e de estilo.
- Elas podem apontar variáveis não utilizadas, espaços em branco no fim de linha e ausência de ponto e vírgula.
- Esse tipo de ferramenta não garante que o código funcione nem que a lógica esteja correta.
- JSLint foi desenvolvida por Douglas Crockford e busca erros de sintaxe e erros estruturais.
- JSHint começou como um fork da JSLint e oferece mais flexibilidade e opções de configuração.
- Closure Linter obriga o estilo JavaScript defendido pela Google e vem com um script para corrigir erros encontrados.
- Na Closure Linter, gjslint faz a análise e fixjsstyle corrige os erros.
- jQuery Lint analisa sintaxe e estrutura no contexto da página e envia a resposta para o console do navegador.
- jQuery Lint é configurável e pode ser adaptada aos padrões do projeto.
