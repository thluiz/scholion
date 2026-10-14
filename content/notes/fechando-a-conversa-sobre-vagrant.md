---
title: "Fechando a conversa sobre Vagrant"
date: '2013-02-04T14:21:38-03:00'
category: webclip
summary: 'O texto atualiza novidades do Vagrant e mostra como definir nome, memória e múltiplas máquinas no Vagrantfile, incluindo uma app e um banco com redes e portas próprias.'
tags: ["vagrant", "virtualbox", "vagrantfile", "virtual-machines"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Fechando a conversa sobre Vagrant"
    url: "http://imasters.com.br/desenvolvimento/fechando-a-conversa-sobre-vagrant/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-02/imasters-com-br--fechando-a-conversa-sobre-vagrant.md"
    kind: repo
---

O texto encerra a sequência sobre Vagrant com duas novidades: a existência de uma empresa por trás do projeto, a Hashicorp, e a chegada de um novo site e logotipo. Depois disso, mostra como ajustar a configuração básica da VM para definir nome e memória, e como declarar mais de uma máquina no mesmo Vagrantfile para separar aplicação e banco.

## Fichamento

- O artigo faz a despedida da sequência sobre Vagrant e registra que o projeto passou a ter a Hashicorp como empresa responsável.
- Também informa que o Vagrant ganhou site e logo novos.
- A configuração básica da VM é estendida com `customize` para definir nome e memória.
- O exemplo mostra uma VM chamada `app` com 512 MB de memória.
- O texto apresenta um Vagrantfile com `box`, redirecionamento de porta e pasta compartilhada.
- Em seguida, mostra um cenário com duas VMs definidas no mesmo arquivo, uma para a aplicação e outra para o banco.
- A VM `app` recebe 1024 MB, porta 22 encaminhada para 2222, porta 80 para 8080, rede host-only `10.0.0.100` e pasta compartilhada.
- A VM `db` recebe 512 MB, porta 3306 encaminhada para 4306 e rede host-only `10.0.0.200`.
- O texto pede cuidado com máquinas virtuais já rodando para evitar conflito de rede.
- Para subir as VMs, o comando indicado é `vagrant up`.
- O resultado esperado mostra a importação das boxes, a criação das regras de rede, o boot das VMs e a montagem das pastas compartilhadas.
- Para acessar cada máquina, o texto usa `vagrant ssh app` e `vagrant ssh db`.
- No final, o autor diz que fecha o ciclo sobre Vagrant e que pode voltar ao tema ou a tecnologias parecidas.
