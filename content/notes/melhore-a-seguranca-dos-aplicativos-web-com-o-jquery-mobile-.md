---
title: "Melhore a segurança dos aplicativos web com o jQuery Mobile - Parte 02"
date: '2012-07-24T13:43:13-03:00'
category: webclip
summary: 'A página mostra vulnerabilidades comuns no lado do servidor em um app com jQuery Mobile, PHP e MySQL, e apresenta contramedidas para controle de acesso, SQL injection, file inclusion e outras falhas.'
tags: ["seguranca-web", "php", "mysql", "jquery-mobile"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Melhore a segurança dos aplicativos web com o jQuery Mobile - Parte 02"
    url: "https://web.archive.org/web/20150613190747/http://imasters.com.br/artigo/21883/jquery/melhore-a-seguranca-dos-aplicativos-web-com-o-jquery-mobile-parte-02"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-07/web-archive-org--melhore-a-seguranca-dos-aplicativos-web-com-o-jquery-mobile-.md"
    kind: repo
---

O texto retoma um aplicativo web feito com jQuery Mobile, PHP e MySQL para mostrar falhas do lado do servidor e suas contramedidas. Ele descreve controle de acesso quebrado, injeção de SQL, inclusão de arquivos, injeção de comandos de OS, injeção de linguagem de script e criação de arquivos arbitrários, sempre ligando cada falha a um uso prático e a uma correção possível.

## Fichamento

- O artigo destaca que muitos desenvolvedores tratam segurança como prioridade baixa e que erros desse tipo podem ficar ocultos até um ataque.
- No controle de acesso quebrado, usuários não autenticados ou sem permissão conseguem acessar recursos porque a proteção se limita a esconder URLs ou porque o script não interrompe a execução após redirecionar.
- O texto mostra aumento de privilégios quando o ID do usuário fica no lado do cliente e pode ser alterado antes do envio do formulário.
- A correção do controle de acesso exige interromper a execução após a falha de autenticação e manter no servidor dados que definem privilégios, como o ID da sessão.
- A injeção de SQL continua relevante e pode permitir divulgação, modificação e inserção de dados, acesso ao sistema de arquivos e comprometimento do sistema.
- O artigo mostra desvio de autenticação e extração de dados usando consultas montadas com entrada não validada, inclusive com UNION.
- A defesa contra SQL injection passa por escapar e validar entradas, usar consultas parametrizadas e converter valores para o tipo esperado.
- A inclusão de arquivos pode ser local ou remota e permitir leitura de arquivos arbitrários ou execução de código, dependendo de como a entrada é usada.
- O texto recomenda evitar passar entrada do usuário para funções que leem ou incluem arquivos e, quando isso for inevitável, usar lista branca e rejeitar travessias de diretório e bytes nulos.
- Na injeção de comandos de OS, a entrada chega a uma função que executa comandos do sistema, permitindo a inserção de caracteres e comandos maliciosos.
- A proteção sugerida é evitar chamadas ao sistema sempre que possível e usar escapeshellcmd quando a entrada precisar compor argumentos de linha de comando.
- Na injeção de linguagem de script, a entrada é interpretada como código, o que pode levar à execução de comandos no contexto do processo do intérprete.
- A correção indicada é evitar eval e reescrever a lógica com funções de API mais seguras, além de validação rígida quando isso não for possível.
- Na criação de arquivos arbitrários, um upload ou uma consulta manipulada pode gerar um arquivo executável e abrir caminho para execução remota de código.
- O texto recomenda validar extensões com lista branca, rejeitar entradas suspeitas, verificar envenenamento por byte nulo e manter arquivos carregados fora da raiz do documento.
- O artigo termina dizendo que não existe fonte completa nem sistema totalmente seguro, e que a proteção depende de acompanhar novas ameaças e correções.
