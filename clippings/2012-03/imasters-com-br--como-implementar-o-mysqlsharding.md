---
url: "http://imasters.com.br/artigo/22687/banco-de-dados/como-implementar-o-mysqlsharding"
captured_at: "2012-03-26T15:12:21-03:00"
title: "Como implementar o MySQLSharding – iMasters"
domain: "imasters-com-br"
---

## [Banco de Dados](http://imasters.com.br/canal/banco-de-dados) + [MySQL](http://imasters.com.br/secao/mysql)

# Como implementar o MySQLSharding

Segunda-feira, 26/03/2012 às 11h15, por [Liran Zelkha](http://imasters.com.br/perfil/liran_zelkha)

Neste artigo, tentarei explicar como implementar o sharding em um pegar uma aplicação existente.

O Database Sharding tem se mostrado uma estratégia muito bem sucedida para escalar bancos de dados relacionais. Quase toda grande solução de website/SaaS usa o sharding quando escreve para seu banco de dados relacional.

O motivo é muito simples - a tecnologia de banco de dados relacional está mostrando sua imagem e simplesmente não consegue atingir as necessidades de hoje: um número massivo de operações/segundo, muitas conexões abertas (uma vez que existem muitos servidores de aplicações conversando com o servidor), grandes quantidades de dados, e uma muita quantidade de taxa de escrita (qualquer coisa acima de 10% é alta quando se fala em bancos de dados relacionais).

Muitos artigos de sites e blogs explicam o que é sharding, por exemplo [aqui](http://en.wikipedia.org/wiki/Shard_%28database_architecture%29)  e [aqui](http://www.datacenterknowledge.com/archives/2007/04/27/database-sharding-helps-high-traffic-sites/) . Mas como você faz sharding na sua aplicação? Na verdade, o fluxo é bastante simples, e consiste de apenas 4 passos:

1. Analise seu schema para encontrar a melhor configuração de sharding.
2. Inicie instâncias múltiplas de banco de dados.
3. Divida os dados entre os bancos de dados de acordo com a configuração de sharding.
4. Atualize o código da sua aplicação para suportar sua configuração de sharding.

(Infelizmente, é bem difícil implementar o sharding. É por isso que iniciamos o  ScaleBase).

Neste artigo, irei explorar a primeira tarefa – analisar seu schema para encontrar a melhor configuração de sharding.

#### Dados necessários

Para construir uma configuração de sharding, você vai precisar dos seguintes dados:

1. Lista de tabelas e tamanhos: tabelas grandes são ótimas candidatas para o sharding, uma vez que vários comandos SQL são executados nelas (caso contrario, elas não seriam tão grandes).
2. Lista de chaves estrangeiras: chaves estrangeiras podem te ajudar a compreender dependências entre tabelas. Tabelas que dependem umas das outras devem ser divididas de uma maneira inteligente o suficiente, caso contrario, a integridade dos seus dados será perdida.
3. SQL Query log (preferivelmente um que foi recolhido depois da execução testes completos da aplicação). Algumas operações SQL são incrivelmente difíceis de implementar em um ambiente de sharding. Você precisa do SQL log para compreender se você pode implementar o sharding em algumas tabelas. O SQL log também pode fornecer uma boa indicação de quais tabelas são bastante acessadas e quais não são.

Claro, esta sessão contem uma suposição: a de que o banco de dados está bem definido e já contém os dados. Esse é o melhor curso de ação. Se você tiver um novo banco de dados, e você não tiver certeza de quantas linhas cada tabela irá conter, ou o que o SQL query log irá mostrar, você terá simplesmente que fazer um chute aproximado.

#### Políticas das Tabelas

Antes que você comece a implementar o sharding, é importante entender que nem toda tabela no schema entrará no sharding. Como o sharding limita suas capacidades de SQL (sem ligação entre tabelas com sharding, singularidade, colunas com autoincremento etc), você irá forçar os limites na sua aplicação que serão difíceis de superar com código.

Normalmente, algumas tabelas simplesmente serão replicadas através de todos os shards. Na verdade, a maioria das tabelas será replicada (no ScaleBase, pelo bem da discussão, podemos chamar essas tabelas de Tabelas Globais), e somente algumas tabelas terão o sharding.

#### Decidindo em qual tabela fazer o sharding

O algoritimo para escolher em quais tabelas fazer o sharding não é muito complexo:

1. Procure pelas maiores tabelas no seu schema: não existe um numero exato de tabelas. A maioria dos schemas tem várias tabelas grandes, e o resto são muito pequenas. O tamanho das tabelas não é dividido igualmente.
2. Olhe o SQL log: existem ligações entre essas tabelas? Se sim, pegue a tabela menor, e a transforme em uma tabela global. Se não, aquelas tabelas servirão como seu ambiente de sharding. Olhe o SQL log: se as tabelas não forem acessadas frequentemente, transforme-as em tabelas globais; procure pelas tabelas mais acessadas (especialmente aquelas com muitos comandos de escrita) e marque as como sharded. Volte ao início deste passo para garantir que possa ser feito o sharding nelas.

A lista de tabelas que você obtém contém os melhores candidatos para o sharding. Futuramente, iremos aprender como migrar seus dados existentes para um ambiente de sharding.

*⁂*

*Texto original em inglês de Liran, disponível em <http://www.scalebase.com/how-to-implement-mysql-sharding/>*
