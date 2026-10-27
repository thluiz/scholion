---
url: "https://web.archive.org/web/20130117195748/http://imasters.com.br/tecnologia/seguranca/oauth-sem-dor-com-php-php-oauth-api-parte-02/"
captured_at: "2012-12-03T15:47:24-03:00"
title: "OAuth sem dor com PHP – PHP OAuth API – Parte 02"
domain: "web-archive-org"
---

**Package:** [PHP OAuth API](http://www.phpclasses.org/package/7700-PHP-Authorize-and-access-APIs-using-OAuth.html)

  

Na [primeira parte deste artigo](http://imasters.com.br/tecnologia/seguranca/oauth-sem-dor-com-php-php-oauth-api-parte-01), vimos que o OAuth é um protocolo muito usado para acessar APIs de determinados sites em nome dos usuários desses sites. Apesar de ele ser relativamente fácil de explicar, não é fácil implementá-lo sem lidar com as dores de cabeça das múltiplas configurações do protocolo, as versões de protocolos diferentes, os detalhes de implementações específicas do local e o pior de tudo: ter de saber mais do que gostaria dos detalhes do protocolo.

  

Depois de começar com os fundamentos (porque ele é necessário, como funciona e as implementações de consumo PHP OAuth), hoje continuaremos com a parte prática – como utilizar a classe PHP OAuth.

  

## **Utilizando a classe PHP OAuth API na prática**

  

### **1. Não me faça aprender o protocolo OAuth**

  

Esta classe de cliente PHP OAuth foi construída especificamente com a finalidade de que você obtenha velocidade sem conhecer muito sobre o funcionamento do protocolo.

  

É sempre bom saber como o protocolo funciona internamente, mas se você não tem tempo nem paciência, você não precisa conhecê-lo de modo extensivo.

  

Existem duas versões principais do protocolo OAuth em uso: a 1.0a e a 2.0. Mas não se preocupe, a classe abstrai todas as diferenças entre elas, para que você não tem que escrever múltiplas seções de código dependendo da versão do protocolo suportado pelo site provedor.

  

Também há diferenças de implementação e configuração ao acessar sites específicos de provedor OAuth. Na maioria dos casos, essas diferenças serão transparentes para você. A classe é inteligente o suficiente para lidar com pelo menos algumas dessas diferenças, de modo que você não tenha que lidar com elas em seu aplicativo.

  

Tudo o que você precisa saber é que a classe faz principalmente duas coisas: a) interage com um site de provedor de OAuth para obter um token de acesso, b) chama a API do site de provedor para executar uma função da API utilizando um token de acesso obtido anteriormente.

  

### **2. Introdução ao caso de uso de mapping approach**

  

Antes de explicar como usar a classe para fins relacionados ao OAuth, para aqueles que gostam de estudar como as coisas funcionam internamente, pode ser legal dar uma olhada na abordagem que usei nessa classe e em outras que encapsulam funcionalidades do que chamo de [componentes de nível de aplicação](http://www.phpclasses.org/blog/post/49-Developing-useful-application-level-PHP-components.html).

  

Caso prefira aprender com exemplo de código, você pode pular essa parte para a etapa chamada “Obtendo o Token de Acesso”.

  

A abordagem é chamada de mapping de caso de uso. Quando você precisa implementar um sistema de software e quando esse sistema é grande o suficiente, normalmente você vai dividi-lo em sub-sistemas. Cada sistema ou sub-sistema implementa um conjunto de casos de uso.

  

Os casos de uso são situações individuais com que seus sistemas precisam lidar para atingir seus objetivos. Algumas pessoas dão outros nomes para os casos de uso, como telas ou páginas. Por exemplo, em um sistema, podemos ter casos de uso como: página de registro, página de login, opções do usuário, entrega de newsletter etc.

  

Para aqueles familiarizados com modelagem de desenvolvimento agile, os casos de uso são semelhantes às [histórias de usuários](http://en.wikipedia.org/wiki/User_story#User_stories_and_use_cases). Eu prefiro pensar em termos de casos de uso, porque às vezes você precisa lidar com as interações entre o seu sistema e um agente que não é um usuário real, como um sistema externo que o seu sistema precisa para se comunicar com o uso de algumas APIs.

  

Enfim, para a implementação real de casos de uso, eu projetei um padrão para implementá-las como classes. Cada caso de uso mapeia para uma classe, por isso o nome mapping de caso de uso para essa abordagem.

  

A classe cliente de OAuth foi implementada como uma classe de caso de uso. Neste artigo, só vou descrever as funções públicas e as variáveis de classes de casos de uso, pois é tudo que você precisa saber para usar a classe cliente de OAuth.

  

Basicamente, uma classe de caso de uso possui quatro funções públicas e duas variáveis públicas. Podem existir outras funções públicas e variáveis específicas para o propósito do caso de uso. Por agora, vou explicar o papel das funções públicas e variáveis básicas.

  

**Funções**

  

Initialize() - É a primeira função você precisa chamar após a criação de um objeto de classe. Não é uma função do construtor. É uma função que inicializa o objeto e avalia se certas condições obrigatórias são válidas, como estabelecer uma conexão com o banco de dados.

  

Essas condições obrigatórias são chamadas de pré-condições. Se uma ou mais pré-condição não for cumprida, a função retorna falso, e uma variável de erro é definida para explicar o motivo da falha ao desenvolvedor.

  

Process() - É a função onde toda a ação acontece. A sua função é a de processar qualquer entrada e preparar a geração de qualquer saída. Em geral, a saída final não deve ser gerada aqui.

  

Ela deve ser chamada apenas depois de chamar a função Initialize(). Se por algum motivo o processamento falhar, esta função retorna falso, e uma variável de erro é definida.

  

Finalize() - Esta função foi feita para limpar quaisquer recursos alocados durante as chamadas Initialize e Process. Normalmente, é utilizada para assegurar que certas condições sejam satisfeitas no final do caso de uso. Essas condições são chamadas de pós-condições. Gerar entradas de log de todos os eventos que aconteceram durante o processamento é um exemplo de uma pós-condição.

  

Esta função não deve ser chamada se a função Initialize falhou. É preciso um parâmetro que é geralmente o valor de retorno da chamada para a função de Process. Mais uma vez, se por algum motivo a finalização falhar, esta função retorna falso, e uma variável de erro é definida.

  

Output() - Este é o lugar onde qualquer saída se o caso de uso deve ser emitido. A saída pode ser gerada a partir de informação produzida durante a chamada para a função Process. Quando necessário, as variáveis de classe privada podem ser usadas para compartilhar informações entre as chamadas Process e Output.

  

Dessa forma, você pode implementar a separação de preocupações. Nenhuma saída acontece durante o processamento, ou qualquer processamento ocorre durante a produção.

  

Normalmente, a função Output não retorna nada, porque a saída é exibida para o usuário, mas em alguns casos ela pode retornar uma string com os dados de saída reais, caso seja conveniente.

  

**Variáveis**

  

$error – Esta é a variável que armazena uma mensagem de erro se qualquer uma das funções Initialize, Process e Finalize falhar. A mensagem de erro não é para ser exibida para os usuário, se sim para permitir que o desenvolvedor saiba por que ele falhou.

  

$exit – Esta variável booleana pode ser definida pela classe de caso de uso para dizer se o script deve sair imediatamente, sem retornar nada. Quando esta variável for verdadeira, o script deve sair sem chamar a função Output. Normalmente, isso significa que a classe emitiu cabeçalhos especiais, como aqueles que redirecionam o navegador para outra página.

  

### **3. Obtendo o token de acesso**

  

OAuth é um protocolo complexo que exige acesso à API do site de provedor e redireciona o navegador do usuário para frente e para trás entre sites consumidores e provedores. Essa interação requer a definição de vários parâmetros, como as URLs do site de provedor para acessar cada coisa.

  

Felizmente, essa classe fornece suporte built-in de alguns dos sites provedores mais populares. Você só precisa definir uma única variável chamada $server com o tipo de servidor que você deseja acessar. Dessa forma, a classe configura automaticamente diversas de suas variáveis, de modo que você não tem que fazê-lo manualmente.

  

A classe fornece suporte built-in para muitos sites provedores. Outros serão acrescentados no futuro. No entanto, se você precisar acessar um servidor OAuth que é suportado diretamente pela classe, você ainda pode usar a classe para acessá-lo. Você só precisa configurar algumas variáveis manualmente.

  

Configurar a classe de acesso a esses outros servidores está fora do escopo deste artigo. Leia a documentação da classe para saber o que você precisa fazer. Fique à vontade para fazer perguntas no [fórum de suporte da classe](http://www.phpclasses.org/discuss/package/7700/), se você tiver qualquer dificuldade.

  

Então, o seu do script básico de autorização OAuth começa assim:

  

```
 $client = new OAuth_client_class; $client->server = 'Twitter';
```

  

A próxima coisa que você precisa fazer é configurar a identidade de seus aplicativos. Primeiro, você precisa ir ao site provedor e registrar um aplicativo. O registro fornecerá os valores para o identificador e de um segredo do mesmo. Por razões de segurança, você não deve compartilhar esse segredo com ninguém.

  

```
 $client->client_id = 'Application identifier goes here'; $client->client_secret = 'Application secret goes here';
```

  

Os servidores OAuth 2.0 podem deixar que você solicite a permissão para acessar seções específicas da API do site provedor. Essas permissões devem ser configuradas usando a variável $scope. Para sites provedores OAuth de 1.0, elas são normalmente configuradas na página de opções do aplicativo.

  

Os valores das permissões para solicitar dependem do site provedor. Você precisa verificar a documentação da API do do site provedor para determinar os valores de permissão que o seu aplicativo precisa.

  

```
 $client->scope = 'API permissions list goes here';
```

  

Durante o processo de autorização OAuth, o navegador do usuário é redirecionado para o site provedor. Em seguida, o browser é redirecionado para o site consumidor, após o usuário conceder acesso ao seu aplicativo. O site provedor precisa saber para qual página o usuário deve ser redirecionado.

  

Normalmente, você pode configurar a URL da página para redirecionar o navegador do usuário para seu site consumidor usando a variável $redirect\_uri. Alguns servidores exigem que essa URL esteja sob um domínio público válido. Assim, domínios privados podem não ser aceitos.

  

```
 $client->redirect_uri = 'http://'.$_SERVER['HTTP_HOST']. dirname(strtok($_SERVER['REQUEST_URI'],'?')). '/change_this_to_the_name_of_this_script.php';
```

  

Agora você está pronto para iniciar o processo OAuth.

  

```
 if(($success = $client->Initialize())) { if(($success = $client->Process())) {
```

  

Depois de chamar a função Process, o processo de autorização OAuth pode ou não ter sido concluído. Caso tenha sido, a variável $access\_token é definida como uma string não vazia.

  

Talvez você queira armazenar o valor do token de acesso em algum lugar para utilização posterior. Normalmente, aplicativos armazenam o token em um banco de dados para que eles possam usá-lo para chamar a API do site provedor depois, eventualmente quando o usuário não estiver presente.

  

Para sites provedores de OAuth 1.0a, existe um token com valor secreto adicional que você também precisa manter. Ele é armazenado na variável $access\_token\_secret.

  

```
 if(strlen($client->access_token)) { // Do something useful with the access token }
```

  

Se houvesse um erro ao recuperar o token de acesso, a variável $authorization\_error seria definida como a mensagem de erro.

  

```
  elseif(strlen($client->authorization_error)) { $client->error = $client->authorization_error; $success = false; } }
```

  

No final, sempre chame a função Finalize, independentemente de o processo de autorização ter sido concluído com sucesso ou não.

  

```
  $success = $client->Finalize($success); }
```

  

Então, você precisa verificar a variável $exit para determinar se o seu script precisa sair imediatamente para que o processo OAuth possa funcionar corretamente.

  

```
 if($client->exit) exit;
```

  

Se o processo foi concluído com sucesso, é legal que você mostre uma mensagem útil para o usuário.

  

```
 if($client->access_token) { echo '<h1>API access was authorized successfully!</h1>'; }
```

  

Seria legal também se você apresentasse mensagens úteis para o usuário, caso o processo tiver falhado por algum motivo.

  

```
 if($client->authorization_error) { echo '<h1>It was not possible to obtain API access', ' authorization!</h1>, '<p>Please <a href="?">try again</a>.</p>'; }
```

  

### **4. Chamando o fornecedor do site API**

  

Depois de ter obtido o token de acesso, você pode chamar a API do site de provedor imediatamente, usando a função CallAPI logo após retornar da função Process e antes de chamar a função Finalize.

  

Alguns sites provedores também permitem o acesso a suas APIs em nome do usuário, mesmo quando o usuário não está presente. Você só precisa utilizar a função CallAPI passando os valores de $access\_token e $access\_token\_secret obtidos anteriormente.

  

```
 $client->access_token = 'Access token here'; $client->access_token_secret = 'Access token secret here'; $url = 'https://api.twitter.com/1.1/account/verify_credentials.json'; $method = 'GET'; $parameters = array(); $options = array(); $success = $client->CallAPI($url, $method, $parameters, $options, $response)))
```

  

Os parâmetros $url e $method da chamada da API são definidos na documentação da API do site provedor. O parâmetro $options é um array com opções eventuais que você pode precisar definir para configurar a forma como a chamada da API é processada. Verifique essa documentação de classe para obter mais detalhes sobre essas opções.

  

O parâmetro $response retorna os resultados da chamada da API. Se os resultados forem formulário de URL codificada ou JSON codificado, o valor CallAPI decodifica a resposta para você.

  

Se a chamada API falhou devido a algum problema relacionado com os parâmetros ou com o token de acesso, a variável $access\_token\_error é definida como a mensagem de erro que você precisa verificar.

  

## Conclusão

  

Apesar da complexidade do protocolo OAuth e suas diferentes implementações, essa classe tenta abstrair, tanto quanto possível, todos os detalhes para que os aplicativos exijam apenas uma quantidade mínima de código para obter autorização para chamar as APIs do site de provedor.

  

Em parte, essa simplificação do processo foi conseguida pela adição de suporte built-in para alguns OAuth mais populares baseados em servidores de APIs. Não é possível adicionar suporte built-in para todas as APIs existentes. No entanto, a classe continuará evoluindo para cobrir o máximo possível de APIs.

  

Outra parte da presente simplificação está relacionada ao fato de que a classe é auto-contida. Isso significa que você só precisa carregar essa classe para usar todas as funcionalidades fornecidas. A dependência externa está apenas em uma [classe HTTP](http://www.phpclasses.org/package/3-PHP-HTTP-client-to-access-Web-site-pages.html) para enviar solicitações HTTP para o servidor web do provedor. Não existem outras classes que você precisa para usar toda a funcionalidade de cliente OAuth.

  

\*\*\*

  

*Texto original disponível em <http://www.phpclasses.org/blog/package/7700/post/1-Painless-OAuth-with-PHP.html>*

  
[anexo ausente]  
  

[![9bcafcd24ef5e7a319a7e300c0d5b221.gif](web-archive-org--oauth-sem-dor-com-php-php-oauth-api-parte-02/9bcafcd24ef5e7a319a7e300c0d5b221.gif)](http://share.feedsportal.com/viral/sendEmail.cfm?lang=pt&amp;title=OAuth+sem+dor+com+PHP+%E2%80%93+PHP+OAuth+API+%E2%80%93+Parte+02&amp;link=http%3A%2F%2Fimasters.com.br%2Ftecnologia%2Fseguranca%2Foauth-sem-dor-com-php-php-oauth-api-parte-02)

  

[![75b9131ce15803402621ad7d693d4dd1.gif](web-archive-org--oauth-sem-dor-com-php-php-oauth-api-parte-02/75b9131ce15803402621ad7d693d4dd1.gif)](http://res.feedsportal.com/viral/bookmark_pt.cfm?title=OAuth+sem+dor+com+PHP+%E2%80%93+PHP+OAuth+API+%E2%80%93+Parte+02&amp;link=http%3A%2F%2Fimasters.com.br%2Ftecnologia%2Fseguranca%2Foauth-sem-dor-com-php-php-oauth-api-parte-02)

  
  
  
[![](http://da.feedsportal.com/r/151883076723/u/49/f/546640/c/33212/s/26395861/a2.img)](http://da.feedsportal.com/r/151883076723/u/49/f/546640/c/33212/s/26395861/a2.htm) [anexo ausente]  
  
[anexo ausente]  
  
  
  
from iMasters <http://da.feedsportal.com/c/33212/f/546640/s/26395861/l/0Limasters0N0Bbr0Ctecnologia0Cseguranca0Coauth0Esem0Edor0Ecom0Ephp0Ephp0Eoauth0Eapi0Eparte0E0A2/ia1.htm>
