---
url: "https://dev.to/mviegas/pt-br-introducao-ao-rabbitmq-com-net-core-15oc"
captured_at: "2026-11-16T00:53:59+00:00"
title: "(pt-BR) Introdução ao RabbitMQ com .NET Core"
domain: "dev-to"
---

> _tl/dr:_ preparei aqui um guia introdutório a partir de várias leituras e vídeos que escutei ao longo desse ano (fontes serão devidamente dadas) explicando o básico sobre o RabbitMQ e como ele pode ser um recurso interessante na infra-estrutura pra desacoplamento e comunicação entre aplicações. Meu objetivo aqui é ser mais coeso e objetivo e apresentar uma visão básica, porém suficiente pra um entendimento incial, e em português. Caso você saiba inglês, colocarei também alguns links ao longo do artigo.

## [](#rabbitmq-conceitos-b%C3%A1sicos-e-motiva%C3%A7%C3%A3o)RabbitMQ: conceitos básicos e motivação

Atualmente, muito se fala do RabbitMQ e message brokers como ferramentas para quebrar os "monolitos" - e aqui eu falo sem o pejorativismo que essa palavra carrega ultimamente. A distribuição de um monolito e o surgimento de arquiteturas distribuídas podem trazer vantagens como desacoplamento, maior coesão e autonomia das partes desacopladas. Essa nova arquitetura distribuída passa a se basear na comunicação entre os participantes para realizar certas ações, o que traz algumas outras complexidades. É introduzida uma camada extra, a rede, e por isso garantias de resiliência, confiabilidade e escalabilidade passam a ser ainda mais necessárias pra esse novo modo de comunicação.

Dito isso, o que é o RabbitMQ? É um **message broker**, um recurso que se baseia no conceito de mensageria e que funciona da seguinte forma: uma determinada aplicação _publica_ uma determinada mensagem para o _broker_ que recebe essa mensagem e a encaminha para uma _fila_. Na outra ponta, uma outra aplicação se _inscreve_ para receber as mensagens daquela fila. Temos então alguém que publica (_publisher_), alguém que se inscreve pra ouvir as mensagens publicadas (_subscriber_) e um agente no meio que distribui e entrega essas mensagens (_message broker_). É o padrão _pub/sub_.

O RabbitMQ traz suporte à alguns protocolos diferentes, como AMQP, MQTT e STOMP. Meu objetivo aqui é ser mais introdutório, mas o Luiz Carlos Faria fala um pouco mais à fundo sobre isso [nesse vídeo](https://www.youtube.com/watch?v=iEeJDAU-Sg0) e numa série de posts que começa [com esse aqui](https://gago.io/blog/rabbitmq-amqp-1-prefacio/).

## [](#vantag-ou-melhor-algumas-considera%C3%A7%C3%B5es)Vantag ... ou melhor, algumas considerações

*   **Escalabilidade**: esse tipo de infra-estrutura suporta centenas de milhares produtos/consumidores de forma simultânea e possui a **entrega única** como característica, ou seja, cada mensagem só entregue à um consumidor.
*   **Mediação**: uma mesma mensagem talvez precise ser entrege para _n_ consumidores que irão processá-la de maneira diferente. O Rabbit possui mecanismos para roteamento e distribuição dessa mensagem, atuando como um _mediador_ dentro da camada de transporte dessa arquitetura distribuída.
*   **Assincronicidade**: o envio de mensagens assíncronas retira um ponto de falha de quem envia essas mensagens, o que deixa a aplicação que publica uma mensagem mais leve, pois desacoplou uma responsabilidade dela. Isso contudo, introduz outros possíveis pontos de falha que devem ser tratados para garantir uma aplicação _resiliente_. Por exemplo, ao retirar o salvamento de log de uma transação SQL dentro da sua aplicação e passando a publicar esse log num message broker pra ser consumido por outra ponta, você retira a dependência dessa transação mas inclui novos possíveis pontos de falha como, por exemplo, a rede que passa a ser uma camada de comunicação e o cliente que vai consumir as mensagens. Em um desses pontos conseguimos ter razoável controle quando publicamos, no outro não. Existem técnicas pra lidar com isso, mas não é o objetivo desse post.

## [](#como-funciona)Como funciona

Uma aplicação _publica_ uma mensagem para o Rabbit. Essa mensagem então é enviada para uma **exchange**, que é um artefato de roteamento, fazendo uma analogia, como um _carteiro responsável por fazer a entrega_). As exchanges, cada qual de acordo com sua configuração, direcionam a mensagem para uma ou mais **filas**. Na outra ponta, existe um (ou mais) **consumidor(es)** responsável por escutar a fila e consumir a mensagem (mais sobre isso abaixo).

É importante dizer que se uma mensagem chegar numa fila com 3 consumidores conectados, **apenas um deles receberá a mensagem para processamento** (entrega única). Caso seja necessário que mais de um consumidor receba a mesma mensagem, , a exchange para qual a mensagem é enviada deve ser configurada para rotear essa mensagem para várias filas. Assim, a mensagem é replicada e entregue para n filas, permitindo consumidores independentes de uma mesma mensagem - _spoiler do que vamos falar mais à frente_. Aqui embaixo uma imagem do CloudAMQP para ilustrar:

[![Imagem do CloudAQMP](https://res.cloudinary.com/practicaldev/image/fetch/s--qlpwbHbv--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://www.cloudamqp.com/img/docs/camqp.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--qlpwbHbv--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://www.cloudamqp.com/img/docs/camqp.png)

> O CloudAMQP (um provider de Rabbit na nuvem) tem uma série muito boa (em inglês) de RabbitMQ para iniciantes. Disponível [nesse link aqui](https://www.cloudamqp.com/blog/2015-05-18-part1-rabbitmq-for-beginners-what-is-rabbitmq.html).

## [](#quem-faz-o-que-dentro-do-rabbitmq)Quem faz o que dentro do RabbitMQ

### [](#exchange)Exchange

Sendo um pouco repetitivo, a Exchange é um artefato de roteamento que funciona como um carteiro responsável por entregar as mensagens. Quando uma mensagem é publicada numa exchange, é enviada uma propriedade (setada por quem envia) chamada _routing key_. Essa key funciona como o endereço do destinatário. A exchange olha a key e sabe para onde entregar.

Dito isso, Existem quatro tipos exchange no RabbitMQ:

*   _Direct_: a mensagem é enviada para uma fila com o mesmo nome da routing key. Se a routing key não for informada, ela é enviada para uma fila padrão.
    
*   _Fanout_: a mensagem é distribuída para todas as filas associadas (falaremos sobre isso mais abaixo). Esse tipo de exchange ignora a routing key.
    
*   _Topic_: a mensagem é distribuída de acordo com um padrão enviado pela routing key.
    
*   _Header_: a mensagem é distribuída de acordo com seus cabeçalhos. Dessa forma, é feito um match com qual consumidor deve receber aquela mensagem.
    

### [](#queues-filas)Queues (filas)

Recebem as mensagens da exchange e armazenam até que um consumidor se conecte para retirar as mensagens de lá. O nome sugere, isso é feito seguindo uma lógica FIFO (first-in, first-out). Podem ter os seguintes atributos:

*   _Durable_: a fila sobrevive ao restart do message broker. O RabbitMQ possui um banco de dados chamado _Mnesia_ aonde armazena essas informações.
*   _Exclusive_: possui somente 1 consumidor e morre quando não há mais consumidores.
*   _Autodelete_: morre quando não há mais mensagens.

### [](#binds-associa%C3%A7%C3%B5es)Binds (associações)

Para que uma exchange entregue uma mensagem para uma fila, deve haver uma associação, um **bind** entre elas. Isso pode ser feito de maneira programática por quem envia ou através de uma interface web que o RabbitMQ disponibiliza para gerenciamento do broker.

### [](#virtual-hosts-vhosts)Virtual hosts (vhosts)

Tudo isso que falamos acima, são entidades do RabbitMQ. Um grupo lógico dessas entidades é chamado de **virtual host**. Um vhost funciona como um _tenant_ dentro do RabbitMQ, que, inclusive, é descrito (na doc sobre vhosts)\[[https://www.rabbitmq.com/vhosts.html](https://www.rabbitmq.com/vhosts.html)\] por essa razão um sistema multi-tenant.

É importante frisar que um vhost é um separação _lógica_ e não física dessas entidades. Separar esses recursos fisicamente é detalhe de implementação de infra-estrutura.

## [](#fire-and-forget)Fire and forget 🤘🏼

Uma das premissas básicas desse tipo de recurso é que quem publica não conhecem quem consome. Quando uma mensagem é disparada, ela é entregue ao mediador e quem disparou não sabe mais sobre o seu paradeiro. Conseguimos saber apenas se ela chegou ao mediador. Por isso, sempre que algum tipo de retorno for necessário, é seguro dizer que o RabbitMQ não é o recurso adequado para ser utilizado.

Por outro lado, existem alguns lugares aonde podemos ter ganhos consideráveis com esse padrão:

*   Quando não me importa o retorno da mensagem.
*   Quando n workers precisam processar uma única mensagem, por exemplo, uma api REST que recebe uma requisição e distribui ela para processamento paralelo.

Quando um consumidor recebe uma mensagem, ele é responsável por dizer ao broker que essa mensagem foi consumida e que já pode ser retirada da fila. É o conceito de **acknowledgement**. O consumidor é responsável por emitir um _ack_ (mais simpático, mais curto). Ao receber o ack, o Rabbit entende que o consumidor disse: _ok Rabbit, já peguei e processei a mensagem, pode retirar ela da fila_.

## [](#padr%C3%B5es-de-consumo)Padrões de consumo

Existem diversos padrões de consumo disponíveis, mas não é meu objetivo falar mais sobre eles nesse post. O **RPC** é um deles e o próprio site de docs do RabbitMQ tem um tutorial disponível [aqui](https://www.rabbitmq.com/tutorials/tutorial-six-dotnet.html). Eu, contudo, recomendo que os outros tutoriais sejam feitos antes pra exercitar.

## [](#e-agora-como-eu-testo-isso-tudo)E agora, como eu testo isso tudo?!

### [](#provisionando)Provisionando

De maneira rápida, existem duas maneiras que eu recomendo pra se começar a utilizar o RabbitMQ para aprender desenvolvendo.

*   [Conta free no CloudAQMP](https://www.cloudamqp.com/plans.html). Importante dizer que esse post não é um ads pra eles, embora eu já os tenha citado algumas vezes. É só porque eles tem um vasto conteúdo pra iniciante e permitem uma conta free. A desvantagem da conta free é que ela funciona dentro de uma infra-estrutura compartilhada do RabbitMQ, como um **virtual host** (um assunto-futuro, quem sabe).
    
*   **Subindo um container no Docker**. Eu costumo ter isso nos meus _docker-compose.override.yml_, mas um comando para subir de primeira é esse aqui:
    

`docker run -d --hostname my-rabbit --name some-rabbit -p 5672:5672 15672:15672 rabbitmq:3-management`

> O usuário e senha padrão para conexão e acesso da GUI são guest/guest.

#### [](#utilizando-o-rabbitmq-com-net-core)Utilizando o RabbitMQ com .NET Core

Existem uma série de bibliotecas que implementam com boas práticas um _service bus_ e trabalham algumas garantias como resiliência para falhas na conexão com o broker, mas não é o objetivo mostrá-las. Pra esse exemplo, basta criar duas aplicações console em .NET Core a adicionar a cada uma o package RabbitMQ.Client pelo seguinte comando:

`dotnet add package RabbitMQ.Client`

#### [](#publisher-console-app-em-net-core)_Publisher_: console app em .NET Core

> **Importante**: nos dois códigos abaixo vocês vão ver que eu não especifiquei o _vhost_ na conexão. Quando isso acontece, é criada uma conexão ao vhost padrão _/_.  

```
using System;
using System.Text;
using RabbitMQ.Client;

namespace RabbitMQDemo.Publisher
{
    class Program
    {
        static void Main(string[] args)
        {
            var connectionFactory = new ConnectionFactory()
            {
                HostName = "localhost",
                Port = 5672,
                UserName = "guest",
                Password = "guest",
            };

            using (var connection = connectionFactory.CreateConnection())
            using (var channel = connection.CreateModel())
            {
                while (true)
                {
                    Console.WriteLine("Type your message");

                    var teste = Console.ReadLine();

                    channel.QueueDeclare(
                        queue: "tests",
                        durable: false,
                        exclusive: false,
                        autoDelete: false,
                        arguments: null);

                    string message =
                        $"{DateTime.Now.ToString("dd/MM/yyyy HH:mm:ss")} - " +
                        $"Message content: {teste}";
                    var body = Encoding.UTF8.GetBytes(message);

                    channel.BasicPublish(exchange: "",
                                         routingKey: "tests",
                                         basicProperties: null,
                                         body: body);
                }
            }
        }
    }
}
```

#### [](#consumer-console-app-net-core)_Consumer_: console app .NET Core

```
using System;
using System.Text;
using RabbitMQ.Client;
using RabbitMQ.Client.Events;

namespace RabbitMQDemo.Consumer
{
    public class Program
    {
        static void Main(string[] args)
        {
            var connectionFactory = new ConnectionFactory()
            {
                HostName = "localhost",
                Port = 5672,
                UserName = "guest",
                Password = "guest"
            };

            using (var connection = connectionFactory.CreateConnection())
            using (var channel = connection.CreateModel())
            {
                channel.QueueDeclare(
                    queue: "tests",
                    durable: false,
                    exclusive: false,
                    autoDelete: false,
                    arguments: null);

                var consumer = new EventingBasicConsumer(channel);

                consumer.Received += (sender, eventArgs) =>
                {
                    var message = Encoding.UTF8.GetString(eventArgs.Body);

                    Console.WriteLine(Environment.NewLine + "[New message received] " + message);
                };

                channel.BasicConsume(queue: "tests",
                     autoAck: true,
                     consumer: consumer);

                Console.WriteLine("Waiting messages to proccess");
                Console.WriteLine("Press some key to exit...");
                Console.ReadKey();
            }

        }
    }
}
```

#### [](#output-das-aplica%C3%A7%C3%B5es-de-exemplo)Output das aplicações de exemplo

[![Alt Text](https://res.cloudinary.com/practicaldev/image/fetch/s--qdoyklu_--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/vfzm9liv2eaphgk04656.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--qdoyklu_--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/vfzm9liv2eaphgk04656.png)  
[![Alt Text](https://res.cloudinary.com/practicaldev/image/fetch/s--9IMpN7CB--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/24khmzhn9dtceboblka0.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--9IMpN7CB--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/24khmzhn9dtceboblka0.png)

## [](#resumo)Resumo

O objetivo desse post foi dar um overview básico e o caminho das pedras pra quem quiser se aventurar nesse mundo de sistemas distribuídos com brokers de mensageria. Existem uma série de outras preocupações que esse tipo de arquitetura trazem como: o message broker passa a ser uma parte vital de sua infraestrutura, então ele precisa ter _disponibilidade_ na última casa decimal dos 99,99999....%.

Por fim, gostaria de lembrar que **não existem balas de prata**. Por isso, pense com cuidado e avalie se cabe na sua aplicação. O RabbitMQ é um recurso incrível, assim como são arquiteturas distribuídas, mas que pode(m) trazer sérias dores de cabeça e prejuízos para o negócio se aplicados sem necessidade e/ou de forma errada.

### [](#links-%C3%BAteis)Links úteis:

*   [Documentação oficial](https://www.rabbitmq.com/#getstarted)
*   [Série do Luiz Carlos Faria sobre RabbitMQ e AMQP](https://gago.io/blog/rabbitmq-amqp-1-prefacio/)
*   [(en) Série do CloudAMQP RabbitMQ para iniciantes](https://www.cloudamqp.com/blog/2015-05-18-part1-rabbitmq-for-beginners-what-is-rabbitmq.html)
