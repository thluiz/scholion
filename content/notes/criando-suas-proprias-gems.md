---
title: "Criando suas próprias gems"
date: '2012-02-01T12:23:49-03:00'
category: webclip
summary: 'O texto mostra como criar uma gem simples em Ruby com Bundler, desde a estrutura inicial e o gemspec até versionamento, dependências, build e release.'
tags: ["ruby", "rubygems", "bundler", "gemas"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Criando suas próprias gems"
    url: "http://imasters.com.br/artigo/23464/ruby-on-rails/criando-suas-proprias-gems"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-02/imasters-com-br--criando-suas-proprias-gems.md"
    kind: repo
---

O texto apresenta o caminho para criar uma gem simples em Ruby. Primeiro distingue RubyGems, como gerenciador de pacotes, das gems, que podem ser bibliotecas, pacotes ou aplicações. Depois mostra a criação do ambiente com RVM, a geração da estrutura com Bundler, a edição do gemspec, o versionamento e a definição de um método básico.

## Fichamento

- RubyGems é o gerenciador que facilita instalar, versionar, desinstalar, listar, procurar e construir gems.
- Gems podem ser bibliotecas, pacotes ou aplicações em Ruby, e seu uso depende da decisão de cada projeto.
- O artigo propõe aprender a construção de uma gem simples usando o exemplo HelloWorld.
- O RVM ajuda a organizar os rubies dos projetos e a criar um gemset para a gem.
- A estrutura da gem pode ser criada com mkdir ou com Bundler, que gera arquivos como Gemfile, Rakefile e o arquivo .gemspec.
- O .gemspec reúne dados da gem, como nome, versão, autores, email, homepage, summary e description.
- O Bundler cria um arquivo de versionamento em lib/hello_world/version.rb com a constante HelloWorld::VERSION.
- A gem pode expor um método em lib/hello_world.rb, no exemplo um método hello que retorna "Olá mundo!".
- O gemspec pode ser ajustado antes da publicação com informações reais do autor e com a descrição da gem.
- O comando gem build gera o arquivo .gem a partir do gemspec.
- Dependências de desenvolvimento, como rspec, podem ser colocadas no gemspec para serem carregadas pelo Bundler.
- O bundle instala as dependências e ajuda a configurar o ambiente de quem vai contribuir com a gem.
- O Rakefile gerado pelo Bundler traz tarefas como build, install e release.
- A tarefa release cria uma tag, constrói a gem e publica no RubyGems.
