---
title: "Se o servidor é seu, porque o problema é meu?"
date: '2012-06-29T12:06:59-03:00'
category: webclip
summary: 'O texto defende que o desenvolvedor Java precisa conhecer o servidor de produção, ler logs e assumir os problemas do aplicativo, em vez de transferi-los para o suporte.'
tags: ["java", "servidor-java", "producao", "logs"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Se o servidor é seu, porque o problema é meu?"
    url: "http://imasters.com.br/artigo/24862/java/se-o-servidor-e-seu-porque-o-problema-e-meu"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-06/imasters-com-br--se-o-servidor-e-seu-porque-o-problema-e-meu.md"
    kind: repo
---

O texto sustenta que o trabalho do desenvolvedor não termina na máquina de desenvolvimento. Ele precisa conhecer o servidor Java, entender limitações de memória, configuração, permissões, banco de dados e envio de e-mail, além de acompanhar o que acontece em produção.

## Fichamento

- Critica desenvolvedores que encaminham ao suporte problemas que nasceram no próprio aplicativo.
- Defende que o profissional de Java precisa conhecer como o servidor escolhido opera, não só instalar, configurar, iniciar e parar.
- Afirma que o aplicativo deve funcionar fora da máquina de desenvolvimento e que a produção revela falhas escondidas.
- Aponta erros comuns como nome de banco e usuário diferentes, permissões de arquivos, host e porta errados, limites de memória, SMTP, erro 404, bibliotecas ausentes ou duplicadas, locale e falha na descompactação do WAR.
- Diz que assumir o problema é parte do trabalho do desenvolvedor.
- Destaca que logs são a chave para entender as exceções e encontrar a causa dos erros.
- Observa que bibliotecas, frameworks e servidores Java mudam com o tempo e podem exigir ajustes.
- Recomenda otimizar consultas e estrutura do banco, rever o comportamento do aplicativo, testar outros servidores Java e buscar alternativas quando o sistema não aguenta a demanda.
