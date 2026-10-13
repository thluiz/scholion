---
url: "http://simplesideias.com.br/formatando-datas-no-ruby-on-rails"
captured_at: "2014-02-23T10:46:56-03:00"
title: "Formatando datas no Ruby on Rails - Simples Ideias"
domain: "simplesideias-com-br"
---

# [Formatando datas no Ruby on Rails](http://simplesideias.com.br/formatando-datas-no-ruby-on-rails "Formatando datas no Ruby on Rails")

31 de Agosto de 2007   
Leia em menos de um minuto

Imagine que você tenha um campo `datetime` e que você queira exibir logo abaixo de um post de blog. Você poderia criar um helper para fazer isso:

```
class PostsHelper
  def post_date(date)
    # formatting date: Aug, 31 2007 - 9:55PM
    date.strftime("posted on %b, %m %Y - %H:%M")
  end
end
```

E em seu template poderia chamar algo como:

```
<%= post_date @post.created_at %>
```

Você também poderia fazer esta formatação no modelo, utilizando o método `after_find`:

```
class Post < ActiveRecord::Base
  private
    def after_find
      self.created_at = created_at.strftime("posted on %b, %m %Y - %H:%M")
    end
end
```

Porém, a maneira mais interessante de se formatar datas no Rails, é utilizando o método `to_s`; tudo o que você precisa fazer é definir um novo formato. Para fazer isso, adicione a seguinte linha ao seu arquivo "environment.rb":

```
Time::DATE_FORMATS[:post] = "posted on %b, %m %Y - %I:%M%p"
```

Para exibir a data devidamente formatada, basta chamar o método `to_s` passando o formato que você quer utilizar.

```
<%= @post.created_at.to_s(:post) %>
```

Lembre-se que você pode definir quantos formatos quiser:

```
Time::DATE_FORMATS[:archive] = "%B/%Y"
Time::DATE_FORMATS[:updated] = "updated on %b, %m %Y - %I:%M%p"
```
