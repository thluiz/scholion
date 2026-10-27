---
title: "Configuração de teclado utilizando as distribuições CentOS, Debian e Ubuntu"
date: '2014-03-22T20:45:41-03:00'
category: webclip
summary: 'A dica mostra como configurar o layout ABNT2 em Debian 6, CentOS 6 e Ubuntu 12.04 editando arquivos do sistema, em vez de usar comandos.'
tags: ["linux", "teclado", "abnt2", "debian-ubuntu-centos"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Linux: Configuração de teclado utilizando as distribuições CentOS, Debian e Ubuntu [Dica]"
    url: "http://www.vivaolinux.com.br/dica/Configuracao-de-teclado-utilizando-as-distribuicoes-CentOS-Debian-e-Ubuntu/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-03/vivaolinux-com-br--configuracao-de-teclado-em-centos-debian-e-ubuntu.md"
    kind: repo
---

A página explica como deixar o teclado no layout ABNT2 no Brasil, nas distribuições Debian 6, CentOS 6 e Ubuntu 12.04. A proposta é fazer isso editando arquivos do sistema, sem recorrer a comandos.

## Fichamento

- No Brasil, o layout adotado pela ABNT é o QWERTY ABNT2, e a dica trata de configurá-lo em Debian 6, CentOS 6 e Ubuntu 12.04.
- Para Debian e Ubuntu, a orientação é editar `/etc/default/keyboard` e definir `XKBMODEL="pc105"`, `XKBLAYOUT="br"`, `XKBVARIANT="abnt2"` e `XKBOPTIONS=""`.
- Depois de salvar essas alterações, o teclado fica configurado com o layout ABNT2.
- Para CentOS, a orientação é editar `/etc/sysconfig/keyboard` e definir `KEYTABLE="br-abnt2"`, `MODEL="abnt2"`, `LAYOUT="br"` e `KEYBOARDTYPE="pc"`.
- Depois de salvar essas alterações, o teclado fica configurado com o layout ABNT2.
- A própria página descreve a dica como simples e útil para necessidades básicas.
