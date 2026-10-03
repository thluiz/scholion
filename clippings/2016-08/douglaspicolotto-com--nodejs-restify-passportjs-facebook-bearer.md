---
url: "http://douglaspicolotto.com/2016/05/01/passportjs-facebook-oauth-bearer/"
captured_at: "2016-08-29T18:55:35-03:00"
title: "NodeJS + Restify + PassportJS + Facebook + Bearer"
domain: "douglaspicolotto-com"
---

# NodeJS + Restify + PassportJS + Facebook + Bearer

[NodeJS](http://douglaspicolotto.com/category/nodejs/)

Olá pessoal, tudo bem?

Em meu primeiro post, vou falar um pouco sobre uma das experiências que tive recentemente ao implementar autenticação (Facebook Oauth + Bearer Token) para uma api RESTful usando [Restify](http://restify.com/) e [PassportJS](http://passportjs.org/), sem usar sessões.

Não encontrei nenhuma publicação na internet que me detalhasse o fluxo de autenticação completo para utilizar a strategy OAuth do facebook e a strategy para token ao portador (bearer), simultaneamente no Passportjs. Praticamente todos os exemplos eram aplicados sobre o [Express](http://expressjs.com/pt-br/), e usavam sessões (o que não acho interessante para uma api). Então, abaixo descrevo a minha solução para o cenário proposto.

**Dependências**

As módulos do Node necessários são:

**Inicialização do Mongoose**

Neste exemplo, crio apenas um model no Mongoose para persistir as informações do usuário.

|  |  |
| --- | --- |
|  | //User Schema  UserSchemamongooseSchema  String  facebook  String  mongoosemodel'User'UserSchema |

**Inicialização do Passport**

A primeira coisa a fazer, após criar o servidor do Restify, é inicializar o PassportJS chamando o método **initialize,** e incluí-lo no pipeline de requisições.

|  |  |
| --- | --- |
|  | //Criação do servidor  serverrestifycreateServer  'RestifyFacebookBearer'  //Inclusão dos parsers para query e body  serverrestifybodyParser  restifyqueryParser  //Inicialização do passport  serverpassportinitialize |

Em um segundo momento, é necessário incluir as strategies do Passport que serão utilizadas.

**Strategy do Facebook**

A strategy de autenticação do Facebook utiliza a api OAuth 2.0 do mesmo. O retorno da strategy ocorre após o usuário ter sido validado, e fornece informações do mesmo através do objeto **p****rofile*****.***Com ele,  é possível obter o id do usuário do Facebook, verificar se o  usuário já está cadastrado e caso contrário criar um novo. Na função **done,** é retornado assincronamente um objeto com o id local do usuário.

|  |  |
| --- | --- |
|  | //Estratégia para o Facebook  passportFacebookStrategy  clientID'<CLIENTID>'  clientSecret'<CLIENTSECRET>'  callbackURL//localhost:8080/api/accounts/facebook/cb`,  profileFields'displayName'  functionaccessTokenrefreshTokenprofile  findOne'facebook.id'profilefunction  scope'all'  profiledisplayName  facebook  profile  functionnewUsr  newUsrscope'all' |

**Strategy para token ao portador**

A strategy para token ao portador irá receber o jsonwebtoken (jwt), obter as informações salvas no mesmo (no caso o id local), e verificar se o usuário existe.

|  |  |
| --- | --- |
|  | //Estratégia para token ao portador  passportBearerStrategyfunctiontoken  tokenDataverifytoken'<TOKEN\_SECRET>'  findByIdtokenDatafunction  false  scope'all' |

**Resources da WebApi**

O último passo é definir os resources da api. Neste caso teremos duas operações para permitir a autenticação usando a strategy do Facebook e uma que irá retornar o nome do usuário autenticado. A função **facebookCallback** será executada após o usuário ter sido autenticado pela strategy do Facebook, o que garante que ele esteja disponível no objeto **req (**o mesmo que foi passado como argumento na função**done).** A partir dai é gerado um jwt que é retornado na resposta da requisição. Este objeto será utilizado para autenticar as requisições subsequentes (como  “api/users/me” no exemplo abaixo).

|  |  |
| --- | --- |
|  | //Operações  functionfacebookCallback  token'<TOKEN\_SECRET>'expiresIn'30 days'  tokentoken  function  //Login Facebook  server'api/accounts/facebook'passportauthenticate'facebook'sessionfalse  server'api/accounts/facebook/cb'passportauthenticate'facebook'sessionfalsefacebookCallback  //Dados do usuário  server'api/users/me'passportauthenticate'bearer'sessionfalse  //Autenticação local, criação de conta local  //Inicialização do servidor  serverlistenfunction  consoleServerlisteningserveraddress |

**Resumo**

Em suma, a autenticação do Facebook é utilizada apenas para garantir que o usuário (válido é claro) exista localmente, e irá retornar um jwt como resposta. Todas as outras requisições irão utilizar este jwt para autenticar o usuário na api.

**Conclusão**

Como disse anteriormente, esta foi a melhor solução que encontrei para utilizar as duas strategies simultaneamente sem usar sessões no passport. Possibilitando, inclusive, a utilização de outros métodos de autenticação (twitter, google, etc) sem muito refactoring.
