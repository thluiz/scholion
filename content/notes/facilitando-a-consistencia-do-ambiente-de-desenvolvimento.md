---
title: "Facilitando a consistência do ambiente de desenvolvimento"
date: '2013-01-31T20:58:29-03:00'
category: webclip
summary: 'O artigo defende ambientes locais virtualizados para dar consistência ao time, acelerar o trabalho e reduzir a dependência da Internet, usando VirtualBox, Vagrant e Puppet.'
tags: ["virtualbox", "vagrant", "puppet", "desenvolvimento-web"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Facilitando a consistência do ambiente de desenvolvimento"
    url: "https://web.archive.org/web/20140705174939/http://imasters.com.br/linguagens/php/facilitando-a-consistencia-do-ambiente-de-desenvolvimento/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-01/web-archive-org--facilitando-a-consistencia-do-ambiente-de-desenvolvimento.md"
    kind: repo
---

A página defende que a equipe precisa de um ambiente consistente e que o trabalho remoto pode reduzir velocidade e depender de uma conexão confiável. A proposta é trabalhar localmente com máquinas virtuais para manter homogeneidade entre os ambientes de desenvolvimento.

## Fichamento

- Aplicações web modernas dependem de vários componentes, como PHP, servidor web, banco de dados, frameworks de teste e outros serviços.
- A abordagem clássica é instalar todos os pacotes necessários em um servidor para dar ao time a mesma experiência ao longo do desenvolvimento.
- O desenvolvimento remoto traz perda de velocidade e dependência de uma conexão confiável com a Internet.
- Trabalhar localmente é mais rápido, mas exige instalar os mesmos pacotes em cada máquina, o que gera inconsistência.
- A solução proposta é criar uma máquina dentro de outra máquina, funcionando em todas as plataformas e garantindo homogeneidade entre os ambientes.
- O VirtualBox executa outro sistema operacional na máquina local.
- O Vagrant permite manipular máquinas virtuais pela linha de comando.
- O Puppet define as mudanças de configuração necessárias para a máquina funcionar como desejado.
- O exemplo usa Vagrantfile e Puppet para provisionar Apache, MySQL, PHP, Xdebug, PEAR, PHP CodeSniffer e PHPUnit.
- A configuração encaminha a porta 80 para localhost:8080 e compartilha a pasta www local com o DocumentRoot do Apache na VM.
- A máquina é iniciada com vagrant up, acessada com vagrant ssh e também pode ser acessada com ssh vagrant@localhost -p 2222.
- O Puppet mantém a configuração sincronizada, e mudanças personalizadas devem ser registradas no arquivo de configuração antes de serem distribuídas.
- A máquina virtual pode ser recarregada, destruída e recriada, suspensa, retomada ou empacotada para distribuição.
- Com essa configuração, o desenvolvedor edita arquivos locais, recarrega o navegador e vê os resultados.
- O texto diz que essa abordagem também pode servir para integração contínua, com provisionamento da máquina, instalação do aplicativo, execução de testes e retorno dos resultados.
