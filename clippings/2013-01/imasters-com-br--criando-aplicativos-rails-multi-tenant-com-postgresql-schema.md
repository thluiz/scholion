---
url: "http://imasters.com.br/banco-de-dados/postgresql/criando-aplicativos-rails-multi-tenantrails-com-postgresql-schemas/"
captured_at: "2013-01-15T17:25:28-03:00"
title: "Criando aplicativos Rails multi-tenant com PostgreSQL schemas"
domain: "imasters-com-br"
---

Muitos aplicativos Rails precisam acomodar vários tenants. Existem algumas maneiras diferentes de fazer isso, cada uma com o seu conjunto de prós e contras. Guy Naor fez um ótimo trabalho de mergulhar nos prós e contras de cada estratégia em sua palestra 2009 Acts As Conference.

  

Uma das estratégias multi-tenant que ele apresentou tira proveito de um recurso específico para o [PostgreSQL](http://www.postgresql.org/) chamado de “schemas”. Seu discurso foi técnico, mas não entrou em detalhes de implementação. Há alguns artigos, threads [no Stack Overflow](http://stackoverflow.com/questions/2782758/creating-a-multi-tenant-application-using-postgresqls-schemas-and-rails), e posts soltos por aí sobre como realmente fazer um aplicativo multi-tenant usando essa estratégia, mas eu ainda tive que descobrir muitas coisas sozinho, então eu percebi que iria documentar a configuração.

  

## Por que PostgreSQL schemas

  

Guy definiu três estratégias básicas para aplicativos Rails multi-tenant.

  

1. Bancos de dados separadas para cada tenant

     

   Um banco de dados com registros limitados através de uma relação “tenant”

     

   Um banco de dados com esquemas separados para cada tenant (PostgreSQL apenas)

Eu não vou mostrar todos os fatores na escolha de uma estratégia multi-tenant, mas vou dizer quando convém escolher a estratégia #3. Se seu aplicativo tem as seguintes características:

  

1. Cada dado de tenant é privado e não deve ser vazado entre eles

     

   Você tem pouca ou nenhuma necessidade de executar consultas que agregam todos os tenants

     

   Você pode ter muitos tenants e não pode lidar com a sobrecarga de administração elevada

Existem, é claro, as nuances para cada aplicativo, e cada um deve tomar a decisão por conta própria. Se você decidir que gostaria de seguir o caminho do esquema PostgreSQL, termine de ler este artigo.

  

## Como os PostgreSQL schemas funcionam

  

“Schema” é um nome horrível para esse recurso. Quando as pessoas ouvem o termo “schema”, elas pensam em uma definição de dados de algum tipo. Isso é não o que os [PostgreSQL schemas](http://www.postgresql.org/docs/9.0/static/ddl-schemas.html) são. Tenho certeza de que os desenvolvedores do PostgreSQL tiveram suas razões, mas eu realmente gostaria que eles tivessem nomeado-o mais adequadamente. “Namespaces” teria sido apropriado.

  

A maneira mais fácil para eu descrever os PostgreSQL schemas (além de dizer que eles são, de fato, namespaces para tabelas) é relacioná-los ao caminho de execução UNIX. Quando você executar um comando UNIX sem especificar seu caminho absoluto, o seu shell vai trabalhar seu caminho no *$PATH* até encontrar um executável com o mesmo nome.

  

Levando em consideração que o seu *$PATH* se pareça com isto:

  

`/usr/local/bin:/usr/bin`

  

Quando você digita *vim,* o seu shell irá procurar *vim* em */usr/local/bin* e depois em */usr/bin* antes de desistir.

  

Os PostgreSQL schemas funcionam praticamente da mesma forma. Cada tabela em um banco de dados PostgreSQL pertence a um schema. Por padrão, as tabelas vão no schema *public*. Você pode ver o schema atual procurando pelo caminho:

  

```
 SHOW search_path;
```

  

Se você não tiver feito qualquer coisa relacionada ao schema ainda, você vai ver *“$user”,public* como o caminho. Isso significa que quando você consultar uma tabela sem especificar explicitamente o ~~namespace~~ schema da tabela vai procurar primeiro no schema do seu usuário (cada usuário recebe um) e depois no schema público antes de desistir. Isso significa que:

  

```
 SELECT count(*) FROM users;
```

  

É funcionalmente equivalente a:

  

```
 SELECT count(*) FROM public.users;
```

  

O que tudo isso significa? Significa que você pode ter a mesma tabela muitas vezes em um banco de dados, desde que cada um viva no seu próprio schema e você possa consultar as tabelas sem ter que declarar explicitamente em qual schema elas estão. Você só tem que definir o caminho de procura de schema apropriadamente e o PostgreSQL irá lidar com o resto.

  

Em outras palavras, você começa a separação de dados através de tenants, modificando muito pouco de sua lógica de aplicação!

  

## Definindo o caminho

  

Então, como é que você faz tudo isso em Rails?

  

NOTA: Esta implementação é voltada para Rails 3.0.9 e PostgreSQL 9.0.4. YMMV.

  

Primeiro, vamos supor que você tenha um modelo *Tenant* que detém uma string de subdomínio exclusivo. Quando uma solicitação HTTP vem com um subdomínio nela, você encontra o tenant adequado e usa sua chave primária (*id*) para definir o caminho (você pode usar o próprio subdomínio, mas você pode querer permitir que os usuários alterem seu subdomínio).

  

Essa lógica deve acontecer em cada pedido, então coloque-a em um *before\_filter* no seu *ApplicationController*.

  

```
 class ApplicationController < ActionController::Base before_filter :handle_subdomain def handle_subdomain if @tenant = Tenant.find_by_subdomain(request.subdomain) PgTools.set_search_path @tenant.id else PgTools.restore_default_search_path end end end
```

  

A lógica não é difícil de acompanhar. Você define o caminho de pesquisa para o tenant combinado se um for encontrado. Caso contrário, você restaura o caminho padrão. Os bits do banco de dados estão escondidos dentro de *PgTools*, que é um módulo muito pequeno que você pode colocar em *lib/*. Aqui estão os métodos relevantes:

  

```
 module PgTools extend self def default_search_path @default_search_path ||= %{"$user", public} end def set_search_path(name, include_public = true) path_parts = [name.to_s, ("public" if include_public)].compact ActiveRecord::Base.connection.schema_search_path = path_parts.join(",") end def restore_default_search_path ActiveRecord::Base.connection.schema_search_path = default_search_path end end
```

  

Estes métodos são bastante autoexplicativos, mas eu gostaria de salientar que o método *set\_search\_path* incluirá o caminho de pesquisa público por padrão, mas pode ser desativado passando *false* como um segundo parâmetro para o método. Isso virá à tona um pouco mais abaixo.

  

No caso de um tenant com id de “4″, no final do seu método *handle\_subdomain* o caminho de procura de PostgreSQL schema será parecido com: *4, public*.

  

Para o restante do pedido, todas as suas consultas serão enviadas através dos “4″ primeiros esquema, desde que você tenha tabelas em que ele seja usado. Então, como você obtém todas as tabelas no schema de cada tenant?

  

## Adicionando novos tenants

  

As definições atuais da tabela do banco de dados precisam ser carregadas para o schema particular de cada novo tenant do sistema. Você pode executar essa tarefa em uma chamada de retorno depois que o registro inquilino foi criado. Algo parecido com isto:

  

```
 class Tenant < ActiveRecord::Base after_create :prepare_tenant private def prepare_tenant create_schema load_tables end def create_schema PgTools.create_schema id unless PgTools.schemas.include? id.to_s end def load_tables return if Rails.env.test? PgTools.set_search_path id, false load "#{Rails.root}/db/schema.rb" PgTools.restore_default_search_path end end
```

  

Depois que o método *create\_schema* garantir que o novo tenant tenha seu próprio schema, o método *load\_tables* define o caminho para seu schema e carrega o arquivo “schema.rb”. Você pode notar que, desta vez *false* está sendo enviado para o método *set\_search\_path*. Isso é porque você só quer que o arquivo carregado “schema.rb” afete o esquema do tenant, não o schema público.

  

NOTA: Este código pode levar algum tempo para executar e deve ser executado em um processo background.

  

Aqui você está usando mais dois métodos do módulo *PgTools*. Aqui estão as suas implementações:

  

```
 def create_schema(name) sql = %{CREATE SCHEMA "#{name}"} ActiveRecord::Base.connection.execute sql end def schemas sql = "SELECT nspname FROM pg_namespace WHERE nspname !~ '^pg_.*'" ActiveRecord::Base.connection.query(sql).flatten end
```

  

Nesse ponto você realizou a maior parte da lógica que entra em um aplicativo Rails multi-tenant com schemas PostgreSQL, mas há algumas outras coisas de que você precisa estar ciente.

  

## Tenants que migram

  

Uma vez que cada tenant tem seu próprio conjunto de tabelas, isso já não é bom o suficiente para apenas rodar *rake db:migrate* para fazer alterações no banco de dados. Em vez disso, cada tenant deve ter seu schema de tabelas migrado.

  

Isso não é muito ruim, você só precisa de uma task customizada do rake que faz um loop da tabela *tenants*, definindo o caminho de procura de schema e migrando o banco de dados. Adicione isso a *lib/tasks/tenants.rake*.

  

```
 namespace :tenants do namespace :db do desc "runs db:migrate on each tenant's private schema" task migrate: :environment do verbose = ENV["VERBOSE"] ? ENV["VERBOSE"] == "true" : true ActiveRecord::Migration.verbose = verbose Tenant.all.each do |tenant| puts "migrating tenant #{tenant.id} (#{tenant.subdomain})" PgTools.set_search_path tenant.id, false version = ENV["VERSION"] ? ENV["VERSION"].to_i : nil ActiveRecord::Migrator.migrate("db/migrate/", version) end end end end
```

  

Certifique-se de executar isso além de *rake db:migrate*. Você pode querer ligá-lo à tarefa *db:migrate* de alguma forma.

  

Isso também deve estar ligado ao seu processo de deploy. Se você estiver usando capistrano para deploy, você pode adicioná-lo assim:

  

```
 namespace :db do desc "Runs rake task which migrates database tables for all tenants" task :migrate_tenants do env = "RAILS_ENV=production" run "cd #{release_path} && bundle exec rake #{env} tenants:db:migrate" end end after "deploy:migrate", "db:migrate_tenants"
```

  

Isso deve bastar!

  

## Tabelas compartilhadas

  

Até agora, este artigo apenas compilou e destilou informações disponíveis a partir de várias fontes, mas uma coisa sobre a qual ninguém mais parece estar falando é que nem todas as tabelas do seu aplicativo serão privadas para cada tenant.

  

A tabela *tenants* em si, por exemplo, precisa estar acessível a todos os tenants (de que outra forma eles vão editar suas configurações de conta?). Além disso, e se você quiser que os usuários possam fazer login para múltiplos tenants em todo o sistema (single sign-on)?

  

Uma maneira de conseguir isso é ter tabelas compartilhadas ao vivo nos schemas específicos de tenant público e tabelas privadas ao vivo nos schemas tenant-específicos. Tecnicamente, todas as tabelas devem existir no schema público para o Rails para inicializar corretamente. Isso não é um problema. Uma vez que o caminho esteja sendo configurado para procurar nos schemas privados primeiro, ele vai encontrar as tabelas lá e usar a tabela certa. No entanto, se um schema  privado tem uma tabela *tenants* e o schema público tem a tabela *tenants* nos com dados nele, a errada vai ser usada.

  

Uma solução é excluir as tabelas compartilhadas de schemas privados. Isso irá garantir que o caminho não vai encontrá-los nos schemas privados e vai encontrá-los no schema público.

  

Para conseguir isso, eu mantenho uma lista de tabelas compartilhadas e modifico o método *Tenant#load\_tables* para ficar assim:

  

```
 def load_tables return if Rails.env.test? PgTools.set_search_path id, false load "#{Rails.root}/db/schema.rb" MyApp::SHARED_TABLES.each { |name| connection.execute %{drop table "#{name}"} } PgTools.restore_default_search_path end
```

  

Imagine um aplicativo que tem uma tabela *users* compartilhada e *posts* privados e tabelas *comments*. Com essa configuração, a lista de tabela será parecida com isto:

  

```
 public.posts public.comments public.users 1.posts 1.comments
```

  

Quando o caminho é definido como *1, public*, comentários e artigos serão obtidos a partir do schema “1″ e os usuários serão obtidos a partir do esquema público. Isso é muito legal, se você me perguntar!

  

Isso dá uma mexida em mais uma área de desenvolvimento: a migração de tabelas compartilhadas. Os schemas privados não têm as tabelas compartilhadas neles, assim você vai encontrar erros ao fazer looping através deles e executar migrações. A correção para isso é bastante simples, mas precisa ser comunicada a todos os desenvolvedores do projeto.

  

Qualquer migração que opera em tabelas compartilhadas deve sofrer curto-circuito se o caminho atual do schema for privado. Adicione este método a *PgTools*:

  

```
 def private_search_path? !search_path.match /public/ end
```

  

Considere a adição de um administrador booleano para a tabela *users* compartilhada acima mencionada. A migração deve ser parecida com isto:

  

```
 class AddAdminToUsers < ActiveRecord::Migration def self.up return if PgTools.private_search_path? add_column :users, :admin, :boolean, default: false end def self.down return if PgTools.private_search_path? remove_column :users, :admin end end
```

  

Essa migração será executada normalmente durante rake db:migrate e será ignorada com segurança durante *rake tenants:db:migrate*.

  

## Boa sorte!

  

Espero que este artigo sirva como um guia para a sua própria aventura em aplicativos Rails multi-tenant no PostgreSQL. Eu tenho usado isso há algum tempo e, apesar de ter muita coisa confundindo sua cabeça para configurar o início, ele acerta em cheio quando você pode ignorar todo o problema para grande parte da sua lógica de aplicativo e ter a paz de espírito de que um erro de codificação não expõe os dados sensíveis de seus usuários acidentalmente.

  

\*\*\*

  

*Texto original disponível em <http://blog.jerodsanto.net/2011/07/building-multi-tenant-rails-apps-with-postgresql-schemas/>*

  
[anexo ausente]  
  

[![9bcafcd24ef5e7a319a7e300c0d5b221.gif](imasters-com-br--criando-aplicativos-rails-multi-tenant-com-postgresql-schema/9bcafcd24ef5e7a319a7e300c0d5b221.gif)](http://share.feedsportal.com/viral/sendEmail.cfm?lang=pt&amp;title=Criando+aplicativos+Rails+multi-tenant+com+PostgreSQL+schemas&amp;link=http%3A%2F%2Fimasters.com.br%2Fbanco-de-dados%2Fpostgresql%2Fcriando-aplicativos-rails-multi-tenantrails-com-postgresql-schemas%2F)

  

[![75b9131ce15803402621ad7d693d4dd1.gif](imasters-com-br--criando-aplicativos-rails-multi-tenant-com-postgresql-schema/75b9131ce15803402621ad7d693d4dd1.gif)](http://res.feedsportal.com/viral/bookmark_pt.cfm?title=Criando+aplicativos+Rails+multi-tenant+com+PostgreSQL+schemas&amp;link=http%3A%2F%2Fimasters.com.br%2Fbanco-de-dados%2Fpostgresql%2Fcriando-aplicativos-rails-multi-tenantrails-com-postgresql-schemas%2F)

  
  
  
[[anexo ausente]](http://da.feedsportal.com/r/151884683114/u/49/f/546640/c/33212/s/278c849c/a2.htm) [anexo ausente]  
  
[anexo ausente]  
  
  
  
from iMasters <http://imasters.com.br/banco-de-dados/postgresql/criando-aplicativos-rails-multi-tenantrails-com-postgresql-schemas/>
