---
url: "https://web.archive.org/web/20150319144624/http://www.akitaonrails.com/2013/10/25/iniciante-criando-um-ambiente-de-desenvolvimento-com-vagrant-e-chef-solo"
captured_at: "2013-10-26T10:04:26-03:00"
title: "[Iniciante] Criando um ambiente de desenvolvimento com Vagrant e Chef-Solo"
domain: "web-archive-org"
---

[Iniciante] Criando um ambiente de desenvolvimento com Vagrant e Chef-Solo  
  
<http://www.akitaonrails.com/2013/10/25/iniciante-criando-um-ambiente-de-desenvolvimento-com-vagrant-e-chef-solo>  
  

Este artigo é mais uma anotação para mim mesmo mas deve servir para mais pessoas também. Se você ainda não sabe o que é Vagrant, leia o artigo do Nando Vieira ["Usando o Vagrant como ambiente de desenvolvimento no Windows"](http://simplesideias.com.br/usando-o-vagrant-como-ambiente-de-desenvolvimento-no-windows) ou assista [a palestra que ele deu na Rubyconf Brasil 2013](https://www.eventials.com/pt-br/locaweb/usando-vagrant-como-ambiente-de-desenvolvimento-ruby/).

  

Assumindo que você já sabe o que é Vagrant, resolvi explorar mais algumas de suas opções. Em particular, como subir uma nova máquina e automatizar sua configuração. Existem algumas formas, a mais simples é [provisionamento via shell-scripts](http://docs.vagrantup.com/v2/provisioning/shell.html) a mais interessante é o [provisionamento usando Chef-Solo](http://docs.vagrantup.com/v2/provisioning/chef_solo.html). Existem também as opções com [Ansible](http://docs.vagrantup.com/v2/provisioning/ansible.html) e [Puppet](http://docs.vagrantup.com/v2/provisioning/puppet_apply.html).

  

Para começar a usar Chef-Solo adicione o seguinte bloco ao seu Vagrantfile:

  

```
 1  
 2  
 3  
 4
```

  

```
 config.vm.provision :chef_solo do |chef|  
   chef.cookbooks_path = 'cookbooks'  
   chef.add_recipe 'main'  
 end
```

Então crie um diretório para seus cookbooks e comece a adicionar receitas, ou use [Berks](http://berkshelf.com/) (que funciona como um Bundler para cookbooks de Chef), e pronto, quando subir sua máquina com 'vagrant up' ele vai usar esses cookbooks para automaticamente instalar e configurar tudo que você precisa. E quando quiser adicionar mais cookbooks basta executar 'vagrant provision'.

  

Em particular, criei meu próprio cookbook fazendo um fork do [@brennovich](http://github.com/brennovich/brotodevbox). Como ambiente para desenvolvimento eu instalo um [Ubuntu 12.04 LTS Precise Pangolin](http://www.akitaonrails.com/2012/08/13/ruby-e-rails-no-ubuntu-12-04-lts-precise-pangolin). Eu gosto de instalar Postgresql, Mysql, Redis, MongoDB, Memcached, Ruby com RVM, Python com PIP e virtualenv, Oracle Java 1.7 e Elasticsearch.

  

Além disso também prefiro usar o conjunto de dotfiles [YADR](https://github.com/akitaonrails/dotfiles). Neste processo eu só faço o clone mas não instalo porque não há uma receita e a rake task que faz isso exige prompts do usuário que ainda não dá para automatizar, então se quiser ativar o YADR, depois de logar com 'vagrant ssh', faça:

  

```
 1  
 2
```

  

```
 cd ~/.yadr  
 rake install
```

Outra coisa que ainda não entendi é que a receita de RVM não está instalando os rubies. Se alguém descobrir porque não deixe de comentar.

  

Para colocar tudo isso para funcionar, instale o Virtualbox ou VMWare, instale o Vagrant e comece assim:

  

```
 1  
 2  
 3  
 4  
 5
```

  

```
 git clone https://github.com/akitaonrails/brotodevbox.git  
 cd brotodevbox  
 git submodule update --init  
   
 vagrant up
```

Meu Vagrantfile está hardcoded para meu diretório de projetos, então altere esta linha para mapear seu diretório:

  

```
 1
```

  

```
 config.vm.synced_folder "~/Sites", "/vagrant"
```

E se estiver usando Vmware como provider, suba assim:

  

```
 1
```

  

```
 vagrant up --provider=vmware_fusion
```

## Conclusão

  

A grande vantagem de usar Vagrant, para mim, é ter um ambiente completo de desenvolvimento isolado nele mesmo. Recentemente fiz upgrade do OS X Mountain Lion para Mavericks, se não tivesse o Vagrant gastaria horas reinstalando tudo, tendo problemas com binários incompatíveis e assim por diante.

  

Alguns vão preferir usar o Vim diretamente do Terminal, com tmux para garantir a sessão. Eu pessoalmente gosto de editar por fora usando MacVim e outros desenvolvedores podem executar seu editor favorito como Sublime Text 2.

  

Se seu ambiente já é um Linux, não deixe de usar o [Vagrant-LXC como provider](http://fabiorehm.com/blog/2013/04/28/lxc-provider-for-vagrant/) que o [@frehm](http://fabiorehm.com/blog/2013/08/07/vagrant-lxc-0-5-0-and-beyond/) está evoluindo, é um dos desenvolvedores mais empolgados em ajudar a tornar o Vagrant uma ferramenta essencial.

  

E mesmo se estiver no OS X como eu, uma experiência que ainda vou fazer é rodar um Linux dentro do VMWare e, com a ajuda do Vagrant-LXC conseguir criar simulações de ambientes mais complexos que exigiriam múltiplas máquinas VMWare (como um cluster MongoDB, por exemplo), e com o Vagrant-LXC vou precisar só de uma máquina virtual.

  

Por enquanto já fico contente de ter um ambiente de desenvolvimento estável.

  

[[anexo ausente]](http://feeds.feedburner.com/~ff/AkitaOnRails?a=SYxFVK7KxNk:VTZJLlKdhSk:yIl2AUoC8zA) [![19573bccbf573b8326733b1261924f22.gif](web-archive-org--iniciante-criando-um-ambiente-de-desenvolvimento-com-vagrant/19573bccbf573b8326733b1261924f22.gif)](http://feeds.feedburner.com/~ff/AkitaOnRails?a=SYxFVK7KxNk:VTZJLlKdhSk:63t7Ie-LG7Y) [[anexo ausente]](http://feeds.feedburner.com/~ff/AkitaOnRails?a=SYxFVK7KxNk:VTZJLlKdhSk:F7zBnMyn0Lo) [[anexo ausente]](http://feeds.feedburner.com/~ff/AkitaOnRails?a=SYxFVK7KxNk:VTZJLlKdhSk:V_sGLiPBpWU) [[anexo ausente]](http://feeds.feedburner.com/~ff/AkitaOnRails?a=SYxFVK7KxNk:VTZJLlKdhSk:7Q72WNTAKBA)

  
[anexo ausente]  
  
  
  
  
  
via AkitaOnRails.com [http://www.akitaonrails.com](http://www.akitaonrails.com/)  
  
October 25, 2013 at 09:12PM
