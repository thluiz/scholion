---
url: "https://nandovieira.com.br/usando-responders-no-rails"
captured_at: "2012-09-03T10:51:25-03:00"
title: "Usando responders no Rails"
domain: "nandovieira-com-br"
---

O Responder é uma funcionalidade que foi introduzida no Rails 3.0. Com ele é possível abstrair o modo como nossos controllers devem responder às requisições feitas na aplicação. Veja o controller abaixo:

  

```
 class TasksController < ApplicationController  
   def index  
     @tasks = Task.all  
    
     respond_to do |format|  
       format.html # index.html.erb  
       format.json { render json: @tasks }  
     end  
   end  
    
   def show  
     @task = Task.find(params[:id])  
    
     respond_to do |format|  
       format.html # show.html.erb  
       format.json { render json: @task }  
     end  
   end  
    
   def new  
     @task = Task.new  
    
     respond_to do |format|  
       format.html # new.html.erb  
       format.json { render json: @task }  
     end  
   end  
    
   def edit  
     @task = Task.find(params[:id])  
   end  
    
   def create  
     @task = Task.new(params[:task])  
    
     respond_to do |format|  
       if @task.save  
         format.html { redirect_to @task, notice: 'Task was successfully created.' }  
         format.json { render json: @task, status: :created, location: @task }  
       else  
         format.html { render action: "new" }  
         format.json { render json: @task.errors, status: :unprocessable_entity }  
       end  
     end  
   end  
    
   def update  
     @task = Task.find(params[:id])  
    
     respond_to do |format|  
       if @task.update_attributes(params[:task])  
         format.html { redirect_to @task, notice: 'Task was successfully updated.' }  
         format.json { head :no_content }  
       else  
         format.html { render action: "edit" }  
         format.json { render json: @task.errors, status: :unprocessable_entity }  
       end  
     end  
   end  
    
   def destroy  
     @task = Task.find(params[:id])  
     @task.destroy  
    
     respond_to do |format|  
       format.html { redirect_to tasks_url }  
       format.json { head :no_content }  
     end  
   end  
 end
```

  

Este controller foi gerado à partir de um scaffold, mas é muito comum vermos aplicações reais usarem algo muito próximo disso. O grande problema é que existe grandes chances de ter códigos semelhantes a este espalhado por diferentes controllers. Perceba como a chamada ao método `respond_to` é bastante semelhante em todas as actions.

  

Para resolver este problema, podemos usar o método `respond_with`, que abstrai a classe `ActionController::Responder`, fazendo com que nosso controller seja muito mais conciso e simples.

  

```
 class TasksController < ApplicationController  
   respond_to :html, :json  
    
   def index  
     @tasks = Task.all  
     respond_with(@tasks)  
   end  
    
   def show  
     @task = Task.find(params[:id])  
     respond_with(@task)  
   end  
    
   def new  
     @task = Task.new  
     respond_with(@task)  
   end  
    
   def edit  
     @task = Task.find(params[:id])  
     respond_with(@task)  
   end  
    
   def create  
     @task = Task.new(params[:task])  
     flash[:notice] = 'Task was successfully created.' if @task.save  
     respond_with(@task, :location => @task)  
   end  
    
   def update  
     @task = Task.find(params[:id])  
     flash[:notice] = 'Task was successfully updated.' if @task.update_attributes(params[:task])  
     respond_with(@task, :location => @task)  
   end  
    
   def destroy  
     @task = Task.find(params[:id])  
     @task.destroy  
     respond_with(nil, :location => tasks_path)  
   end  
 end
```

  

Para poder usar o Responder, você deve especificar quais formatos um controller pode responder. Neste nosso caso, o controller irá responder aos formatos HTML e JSON. Isso foi feito com o método `respond_to`, com uma chamada realizada na classe `ActionController::Base` (lembre-se que `ApplicationController` herda da classe `ActionController::Base`).

  

O Responder irá verificar o estado do recurso (se foi salvo ou se possui erros) para saber como ele deve responder. Além disso, ele leva em consideração qual o tipo de formato que está sendo solicitado para saber se deve responder como um comportamento de navegação ou de API.

  

Mesmo a nossa nova e simplificada implementação de controller, ainda podemos reduzir um pouco mais a duplicação. Perceba como definimos a flash message baseado na resposta dos métodos `ActiveRecord::Base#save` e `ActiveRecord::Base#update_attributes`. Você poderia criar um novo Responder que lidasse com as flash messages dependendo do estado do recurso. Mas em vez de fazermos isso manualmente, nós iremos utilizar a gem [responders](http://rubygems.org/gems/responders), criada pelo [José Valim](http://github.com/josevalim).

  

### Usando a gem responders

  

Para instalá-la, adicione a linha abaixo ao seu arquivo `Gemfile`.

  

```
 gem "responders"
```

  

Execute o comando `bundle install`.

  

Agora, abra o arquivo `app/controllers/application_controller.rb` e defina os formatos que os controllers deverão responder por padrão. Nós também iremos definir quais responders nosso controller irá usar, através do método `responders`, adicionado pela gem.

  

```
 class ApplicationController < ActionController::Base  
   protect_from_forgery  
    
   respond_to :html, :json  
   responders :flash  
 end
```

  

Agora, remova todas as definições de flash messages que existir no controller. Aproveite também para alterar o modo como os objetos são salvos/criados.

  

```
 class TasksController < ApplicationController  
   def index  
     @tasks = Task.all  
     respond_with(@tasks)  
   end  
    
   def show  
     @task = Task.find(params[:id])  
     respond_with(@task)  
   end  
    
   def new  
     @task = Task.new  
     respond_with(@task)  
   end  
    
   def edit  
     @task = Task.find(params[:id])  
     respond_with(@task)  
   end  
    
   def create  
     @task = Task.create(params[:task])  
     respond_with(@task, :location => @task)  
   end  
    
   def update  
     @task = Task.find(params[:id])  
     @task.update_attributes(params[:task])  
     respond_with(@task, :location => @task)  
   end  
    
   def destroy  
     @task = Task.find(params[:id])  
     @task.destroy  
     respond_with(nil, :location => tasks_path)  
   end  
 end
```

  

Com a gem responders você tem suporte transparente a flash messages internacionalizadas.

  

```
 en:  
   flash:  
     actions:  
       create:  
         notice: "%{resource_name} has been created."  
         alert: "Double check your form before continuing."  
       update:  
         notice: "%{resource_name} has been updated."  
         alert: "Double check your form before continuing."  
       destroy:  
         notice: "%{resource_name} has been removed."  
         alert: "%{resource_name} couldn't be removed."
```

  

Se você precisar personalizar a mensagem, utilize o escopo `flash.<controller>.action.<tipo>`.

  

```
 en:  
   flash:  
     tasks:  
       create:  
         notice: "This task has been created!"  
       update:  
         notice: "This task has been updated!"  
       destroy:  
         notice: "This task has been removed!"
```

  

Essa gem possui outros Responders bastante interessantes, então não deixe de dar uma olhada na [documentação](https://github.com/plataformatec/responders).

  

### Usando um Responder personalizado

  

Quando você precisa sair um pouco do padrão utilizado pelo Responder, é muito comum voltarmos a usar o método `respond_to`. A ação abaixo sempre redirecionar para um endereço, independente de o objeto ter sido salvo com sucesso ou não. Isso provavelmente aconteceria no caso de comentários, onde o formulário de criação será sempre exibido no relacionamento-pai, ou seja, no `Post`.

  

```
 class CommentsController < ApplicationController  
   def create  
     @post = Post.find(params[:post_id])  
     @comment = post.comments.create(params[:comment])  
    
     respond_to do |format|  
       format.html do  
         if @comment.new_record?  
           flash[:notice] = t("flash.comments.create.notice")  
         else  
           flash[:alert] = @comment.errors.full_messages.to_sentence  
         end  
    
         redirect_to @post  
       end  
    
       format.json  
     end  
   end  
 end
```

  

Funciona, mas é feio! Para resolver este problema podemos criar nosso próprio Responder, que irá abstrair apenas a lógica do formato HTML. Primeiro, crie um diretório `app/responders`. Se você estiver executando o servidor, lembre-se de reiniciá-lo. Depois, crie o arquivo `app/responders/application_responder`, que irá definir o comportamento padrão para todos os responders que criarmos.

  

```
 class ApplicationResponder < ActionController::Responder  
   include Responders::FlashResponder  
    
   delegate :t, :flash, :to => :controller  
 end
```

  

A classe `ActionController::Responder` não implementa os métodos `flash` e `t` e, por isso, estamos fazendo a delegação para o objeto `controller`.

  

Agora, podemos criar nosso Responder personalizado, que será usado apenas na action `create`. Crie o arquivo `app/responders/comments/create_responder.rb` com o código abaixo:

  

```
 module Comments  
   class CreateResponder < ApplicationResponder  
     def to_html  
       if resource.new_record?  
         flash[:notice] = t("flash.comments.create.notice")  
       else  
         flash[:alert] = @comment.errors.full_messages.to_sentence  
       end  
    
       redirect_to navigation_location  
     end  
   end  
 end
```

  

Só falta refatorar nosso controller, de modo que ele use este responder. Como seu comportamento é específico da action `create`, podemos especificá-lo com a opção `:responder`.

  

```
 class CommentsController < ApplicationController  
   def create  
     @post = Post.find(params[:post_id])  
     @comment = post.comments.create(params[:comment])  
    
     respond_with(@comment, {  
       :location => post_path(@post),   
       :responder => Comments::CreateResponder  
     })  
   end  
 end
```

  

E para garantir que este responder esteja funcionando como esperado, escrevo testes de integração (que eu já faria mesmo sem usar o Responder), fazendo expectativas quanto a presença da mensagem baseado no estado do objeto.

  
 ![](http://feeds.feedburner.com/~r/simplesideias/~4/EIttlut6a6s)  
   
   
   
 from Simples Ideias. Por Nando Vieira. <http://simplesideias.com.br/usando-responders-no-rails/?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+simplesideias+%28Simples+Id%C3%A9ias.+Por+Nando+Vieira.%29>
