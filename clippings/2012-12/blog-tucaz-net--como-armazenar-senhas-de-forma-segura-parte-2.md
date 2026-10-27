---
url: "https://blog.tucaz.net/2012/11/30/como-armazenar-senhas-de-forma-segura-em-sua-aplicacao-parte-2/"
captured_at: "2012-12-03T10:12:54-03:00"
title: "Como armazenar senhas de forma segura em sua aplicação - Parte 2"
domain: "blog-tucaz-net"
---

Na [primeira parte](http://blog.tucaz.net/2012/11/02/como-armazenar-senhas-de-forma-segura-em-sua-aplicacao-parte-1/) desta série abordei alguns conceitos básicos e terminei falando de hashing e como ele serve pra gerarmos um valor único e irreversível a partir de um input de dados.

  

#### Como utilizar hashing pra proteger nossa aplicaçao

  

Já que nao conseguimos reverter o valor gerado a partir de uma funçao de hashing como podemos utiliza-lo como forma de proteçao de senha?

  

```
 public void CadastroUsuario(string login, string senha /* outros dados do usuário */)  
 {  
     var hashSenha = GerarHash(senha);  
     Usuarios.Armazenar(login, hashSenha /* outros dados do usuário */ )  
 }  
   
 public bool LoginEhValido(string login, string senha)  
 {  
     var hashUsuarioArmazenado = Usuarios.RecuperarHash(login);  
     var hashSenha = GerarHash(senha);  
   
     return hashSenha == hashUsuarioArmazenado;  
 }
```

  

1. No momento do cadastro do usuário, ao invés da senha, armazenamos o hash resultante da senha do usuário como exemplificado no método *CadastroUsuario*

     

   Na hora de verificar o login, como bons algoritmos de hashing garantem unicidade, basta comparar o hash armazenado com o hash resultando da senha informada pelo usuário pra verificar se ele é quem diz ser já que apenas a senha original terá o hash compatível com o armazenado

Além de garantirmos que mesmo que nossa base de dados caia em maos erradas ninguém terá acesso a senha original do usuário também garantimos que nós (mantenedores da aplicaçao) também nao teremos acesso o que também é muito bom já que a maioria dos usuários utiliza a mesma senha em mais de uma aplicaçao.

  

#### Criando um algorítmo simples de hashing

  

Pra entender melhor a idéia de um algorítmo desse tipo vamos implementar uma versao bem simplificada:

  

```
 public static string GerarHash(string entrada)  
 {  
     var hash = entrada.Sum(caracter => (int) caracter);  
     return hash.ToString();  
 }  
   
 GerarHash("senha");  //resultado 527  
 GerarHash("SENHA");  //resultado 367  
 GerarHash("ddddM2"); //resultado 527
```

  

Podemos perceber algumas coisas neste método:

  

Mesmo inserindo uma entrada com o mesmo significado em portugûes ("senha" e "SENHA") obtemos dois hashes diferentes, o que é desejável, pois tratando-se de senhas, diferenciar maíusculas e mínusculas é uma maneira de gerar senhas mais complexas e difíceis de se adivinhar

  

Este algoritmo garante unicidade apenas em um pequeno grupo de entradas já que tanto "senha" quanto "ddddM2" geraram o mesmo resultado. Isto acontece, pois o algorítmo é muito simples e apenas soma o valor [ASCIÎ](http://www.asciitable.com/) de cada um dos caracteres da sequência de entrada

  

Ainda assim, podemos perceber também que é virtualmente impossível, a partir do hash, descobrir com certeza qual entrada originou o hash já que executamos uma sequência matemática que nos permite obter o mesmo resultado com mais de um input diferente.

Como vocês já devem ter concluído este nao é um algoritmo de hashing que devemos usar caso nosso objetivo seja garantir a segurança de nossa aplicaçao já que colisoes sao muito frequentes.

  

Partindo dai é que surgiu o MD5, um dos algorítmos mais utilizados hoje em dia pra geraçao de hashes. Em .NET ele está disponível nativamente por meio da classe MD5 existente no namespace System.Security.Criptography. Um exemplo de uso pode ser encontrado na [página oficial de documentaçao no MSDN](http://msdn.microsoft.com/pt-br/library/system.security.cryptography.md5.aspx) e o [pseudo código e algumas implementaçoes simples na Wikipedia](http://en.wikipedia.org/wiki/MD5).

  

Apesar de MD5 ser um bom algorítmo ele já nao é mais considerado seguro e pode ser quebrado facilmente. Contudo existem outras maneiras de mesmo com MD5 garantir que as senhas de seus usuários estejam seguras e é sobre isso que vou falar no próximo post.

  

Até lá!

  

[[anexo ausente]](http://feeds.feedburner.com/~ff/tucaz?a=0-TcVjZbHyQ:LfgLefaTo7g:yIl2AUoC8zA) [![19573bccbf573b8326733b1261924f22.gif](blog-tucaz-net--como-armazenar-senhas-de-forma-segura-parte-2/19573bccbf573b8326733b1261924f22.gif)](http://feeds.feedburner.com/~ff/tucaz?a=0-TcVjZbHyQ:LfgLefaTo7g:63t7Ie-LG7Y) [[anexo ausente]](http://feeds.feedburner.com/~ff/tucaz?a=0-TcVjZbHyQ:LfgLefaTo7g:qj6IDK7rITs) [[anexo ausente]](http://feeds.feedburner.com/~ff/tucaz?a=0-TcVjZbHyQ:LfgLefaTo7g:V_sGLiPBpWU) [[anexo ausente]](http://feeds.feedburner.com/~ff/tucaz?a=0-TcVjZbHyQ:LfgLefaTo7g:7Q72WNTAKBA)

  
[anexo ausente]  
  
  
  
from tucaz [http://blog.tucaz.net/2012/11/30/como-armazenar-senhas-de-forma-segura-em-sua-aplicacao-parte-2/?utm\_source=feedburner&utm\_medium=feed&utm\_campaign=Feed%3A+tucaz+%28tucaz.blog.now%28%29%29](http://blog.tucaz.net/2012/11/30/como-armazenar-senhas-de-forma-segura-em-sua-aplicacao-parte-2/?utm_source=feedburner&amp;utm_medium=feed&amp;utm_campaign=Feed%3A+tucaz+%28tucaz.blog.now%28%29%29)
