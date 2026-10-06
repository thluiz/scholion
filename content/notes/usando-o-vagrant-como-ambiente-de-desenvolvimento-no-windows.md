---
title: "Usando o Vagrant como ambiente de desenvolvimento no Windows"
date: '2012-10-05T10:26:17-03:00'
category: webclip
summary: 'O artigo mostra como usar o Vagrant para substituir um ambiente de desenvolvimento lento no Windows, rodando uma máquina Linux com VirtualBox, pasta compartilhada e acesso por SSH.'
tags: ["vagrant", "windows", "ruby-on-rails", "virtualbox"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Usando o Vagrant como ambiente de desenvolvimento no Windows"
    url: "https://nandovieira.com.br/usando-o-vagrant-como-ambiente-de-desenvolvimento-no-windows"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-10/nandovieira-com-br--usando-o-vagrant-como-ambiente-de-desenvolvimento-no-windows.md"
    kind: repo
---

O artigo explica que o Vagrant permite virtualizar o ambiente de desenvolvimento de forma simples. No Windows, isso evita depender de ferramentas como Cygwin e contorna a lentidão de Ruby on Rails e as limitações da linha de comando.

## Fichamento

- O Vagrant permite rodar máquinas virtuais com VirtualBox.
- O uso de boxes personalizados simplifica a preparação do ambiente para novos integrantes.
- No Windows, desenvolver com Ruby on Rails é descrito como muito lento.
- O PowerShell melhora a experiência, mas ainda fica abaixo de Bash.
- O Vagrant resolve isso ao usar uma distribuição Linux como ambiente de execução.
- O trabalho continua no editor local do Windows, com conexão ao guest por SSH.
- Um diretório compartilhado entre host e guest mantém as alterações sincronizadas.
- O artigo orienta instalar VirtualBox antes do Vagrant.
- O box usado no exemplo é `hellobits`, com Vim, MySQL, Ruby 1.9.3, Bundler, Sphinx, Git e Curl.
- No Windows, o acesso por SSH exige PuTTY e PuTTYgen.
- O `Vagrantfile` define o box e faz o encaminhamento da porta 3000.
- Para iniciar a máquina, o comando usado é `vagrant up`.
- No ambiente virtual, o Rails é instalado com `gem install rails`.
- O app é criado em `/vagrant` com `rails new myapp -d mysql`.
- O `therubyracer` precisa ser ativado no `Gemfile` antes de rodar `bundle install`.
- O servidor Rails é iniciado com `rails s`.
- Entre os comandos úteis, o texto cita `vagrant suspend`, `vagrant resume` e `vagrant destroy`.
- A máquina virtual descrita é um Ubuntu Linux Server 10.04 LTS 32-bits.
- Para atualizar pacotes, o artigo lista comandos como `apt-get update` e `apt-get upgrade`.
- Para atualizar o Ruby, o texto usa `~/scripts/ruby`.
- Para manter o Guest Additions atualizado, o artigo recomenda `vagrant-vbguest`.
