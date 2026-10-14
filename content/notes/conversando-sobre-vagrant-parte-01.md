---
title: "Conversando sobre Vagrant – Parte 01"
date: '2013-01-21T14:21:10-03:00'
category: webclip
summary: 'O artigo apresenta o Vagrant como uma forma de criar uma VM de desenvolvimento com o VirtualBox, mostra a configuração inicial e explica um erro comum ao recarregar a máquina, com a correção indicada.'
tags: ["vagrant", "virtualbox", "virtualizacao", "vm"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Conversando sobre Vagrant – Parte 01"
    url: "http://imasters.com.br/desenvolvimento/conversando-sobre-vagrant-parte-01/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-01/imasters-com-br--conversando-sobre-vagrant-parte-01.md"
    kind: repo
---

O artigo mostra o Vagrant como uma solução para montar um ambiente de desenvolvimento com o VirtualBox, com configuração simples por `Vagrantfile` e um CLI mais amigável para quem desenvolve. Também indica os requisitos iniciais, como VirtualBox, Ruby e RVM.

Depois, o texto descreve o fluxo básico para criar e acessar a VM com `vagrant box add`, `vagrant init`, `vagrant up` e `vagrant ssh`. Em seguida, apresenta um problema que pode aparecer após atualizações do kernel ou do VirtualBox, quando o `vagrant reload` falha ao montar a pasta compartilhada, e lista os passos usados para instalar dependências e rodar as Guest Additions até a VM voltar a funcionar.

## Fichamento

- O Vagrant é apresentado como uma solução junto com o VirtualBox para criar um ambiente de desenvolvimento parecido com o de produção.
- O texto destaca como recursos do Vagrant o suporte básico a Puppet ou Chef, a configuração via `Vagrantfile` e um CLI amigável.
- Para começar, o artigo pede VirtualBox, Ruby e, de preferência, RVM para organizar o ambiente Ruby.
- O processo inicial inclui instalar o Vagrant com `gem install vagrant`, adicionar uma box e criar a VM com `vagrant init`.
- O `vagrant up` inicia a máquina e o `vagrant ssh` permite acessá-la.
- Após atualizar o kernel ou o VirtualBox, o `vagrant reload` pode falhar no comando de montagem da pasta compartilhada.
- A solução proposta instala `build-essential`, headers do kernel, `kernel-package` e `dkms`, depois monta a ISO das Guest Additions e executa `VBoxLinuxAdditions.run`.
