---
title: "[Iniciante] Criando um ambiente de desenvolvimento com Vagrant e Chef-Solo"
date: '2013-10-26T10:04:26-03:00'
category: webclip
summary: 'O artigo mostra como subir uma máquina Vagrant e automatizar sua configuração com Chef-Solo, usando cookbooks para instalar serviços, ajustar dotfiles e manter um ambiente de desenvolvimento reproduzível.'
tags: ["vagrant", "chef-solo", "provisionamento", "ambiente-de-desenvolvimento"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "[Iniciante] Criando um ambiente de desenvolvimento com Vagrant e Chef-Solo"
    url: "https://web.archive.org/web/20150319144624/http://www.akitaonrails.com/2013/10/25/iniciante-criando-um-ambiente-de-desenvolvimento-com-vagrant-e-chef-solo"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-10/web-archive-org--iniciante-criando-um-ambiente-de-desenvolvimento-com-vagrant.md"
    kind: repo
---

O texto apresenta um jeito de usar Vagrant para criar uma máquina de desenvolvimento e automatizar sua configuração com Chef-Solo. Ele menciona outras opções de provisionamento, como shell scripts, Ansible e Puppet, mas foca em Chef-Solo por meio de cookbooks apontados no Vagrantfile.

O autor descreve um ambiente baseado em Ubuntu 12.04 LTS, com instalação de PostgreSQL, MySQL, Redis, MongoDB, Memcached, Ruby com RVM, Python com PIP e virtualenv, Oracle Java 1.7 e Elasticsearch. Também cita o uso de YADR como dotfiles, explica como iniciar o ambiente com o repositório brotodevbox, como ajustar o synced_folder, como subir com Vagrant e como usar o provider VMware quando necessário.

## Fichamento

- Usa Vagrant para subir uma máquina nova e automatizar sua configuração com Chef-Solo.
- Aponta shell scripts, Ansible e Puppet como alternativas de provisionamento, mas destaca Chef-Solo como a opção mais interessante.
- Mostra o bloco de configuração no Vagrantfile para apontar a pasta de cookbooks e chamar a recipe main.
- Recomenda criar um diretório de cookbooks ou usar Berks para gerenciar cookbooks de Chef.
- Relata um ambiente de desenvolvimento baseado em Ubuntu 12.04 LTS.
- Lista os componentes instalados no ambiente: PostgreSQL, MySQL, Redis, MongoDB, Memcached, Ruby com RVM, Python com PIP e virtualenv, Oracle Java 1.7 e Elasticsearch.
- Diz que faz apenas o clone do YADR, sem instalar automaticamente, porque a tarefa exige interação do usuário.
- Explica que, depois de entrar por SSH na máquina, é possível rodar `cd ~/.yadr` e `rake install` para ativar o YADR.
- Informa que a receita de RVM ainda não está instalando os rubies e deixa essa dúvida em aberto.
- Mostra os passos para clonar o repositório, atualizar submodules e executar `vagrant up`.
- Diz que o caminho sincronizado do projeto precisa ser ajustado no Vagrantfile.
- Indica o comando `vagrant up --provider=vmware_fusion` para quem usar VMware.
- Defende Vagrant como forma de manter um ambiente de desenvolvimento completo e isolado.
- Menciona que, em Linux, o Vagrant-LXC pode ser usado como provider para simular ambientes mais complexos com uma única máquina virtual.
