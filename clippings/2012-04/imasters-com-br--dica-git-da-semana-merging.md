---
url: "http://imasters.com.br/artigo/24228/desenvolvimento/dica-git-da-semana-merging"
captured_at: "2012-04-25T16:57:47-03:00"
title: "Dica Git da semana: Merging"
domain: "imasters-com-br"
---

A dica Git desta semana aborda o trabalho com branches.

  

#### Merging

  

Até agora, temos apenas feito o commit do conteúdo para o repositório git. Em outras palavras, temos construído histórias lineares, um commit de cada vez. Embora não haja nada de errado com isso - afinal, a maioria dos outros sistemas de controle de versão que você tem usado pode trabalhar exatamente do mesmo modo - há uma grande quantidade de energia que o Git concede a você com branches.

  

Um monte de gente evita fazer branches, se eles só forem usados para sistemas de controle de versão menos como CVS ou SVN. Não pelo branching ser especialmente diferente (embora ainda uma ordem de magnitude mais lenta do que Git) - em vez disso, é a falta de bom merging que mata o branching. Como resultado, os branches estão reservados para versões do produto.

  

O Git, por outro lado, torna o branching e o merging livres - tanto que o branching torna-se um modo de vida em um fluxo de trabalho Git.

  

Um merge reúne mais de um commit para o branch atual. Normalmente, commits são nomes de branches, mas eles podem ser qualquer hash no repositório.

  

Um fluxo de trabalho comum é dividir um item de desenvolvimento para implementar um novo recurso. Em sistemas não distribuídos, isso é representado muitas vezes como a fase "dá uma olhada, mas não faça commit"; mas, no Git, criar um branch é gratuito e você é encorajado a fazer os commits enquanto produz - um pouco como a gravação automática de arquivos de origem. Quando estiver pronto, você pode fazer um merge de volta para o branch principal de desenvolvimento:

  

```
 $ git checkout -b feature  
   
 # implement feature  
   
 $ git commit -m "Feature part 1 implemented"  
   
 # implement feature  
   
 $ git commit -m "Feature part 2 implemented"  
   
 # test, check everything is OK  
   
 # Switch back to master:  
   
 $ git checkout master  
   
 $ get merge feature  
   
 # Optionally, delete the feature branch  
   
 $ git branch -d feature
```

  

O que fizemos aqui foi criar um novo recurso branch *feature*, trabalhamos nele por um tempo, então voltamos para os conteúdos *master* e *merge*. É bastante comum esse padrão ocorrer com frequência, às vezes, com recursos que se sobrepõem uns aos outros. Não se preocupe com isso; o Git sempre te mantém par de suas alterações.

  

Se não há problemas, então o *git merge* irá criar automaticamente um commit para você. Se não...

  

#### Conflitos

  

Nada na vida é de graça, e merging não é exceção. Se você mudou o mesmo arquivo em dois ou mais commits divergentes, então você pode acabar com um conflito de merge. Isso é como outros sistemas de controle de versão; você começa com marcadores no código *>>>>>>* , como veria em outros sistemas de controle de versão. No entanto, você vê isso muito menos frequentemente no Git, porque commits tendem a ser menores e, em muitos casos, o Git pode reproduzir reordenações em seu código.

  

Para corrigir o conflito de merge, edite o arquivo, removendo os marcadores e resolva um conflito de cada vez, e execute *git add* o arquivo. Você pode usar *git status* para mostrar-lhe a lista de arquivos, aqueles com conflitos de merge serão apresentados separadamente; você vai ver cada arquivo individualmente, e poderá corrigir e executar o *git add* conforme for desenvolvendo.

  

Quando você tiver terminado, executar *git commit* vai confirmar todas as alterações que você tenha feito. Diferentemente dos casos anteriores, nos quais você tem um único pai mencionado nos metadados de commit no topo, desta vez você vai ver dois pais. Eles representam os commits anteriores, e os commits que você está trazendo o outros branch.

  

Há coisas mais interessantes que podemos fazer com os merges e merged tress, mas vamos abordá-los com mais detalhes em outra ocasião.

  

*⁂*

  

*Texto original disponível em <http://alblue.bandlem.com/2011/04/git-tip-of-week-merging.html>*

  
[anexo ausente]  
  

[![9bcafcd24ef5e7a319a7e300c0d5b221.gif](imasters-com-br--dica-git-da-semana-merging/9bcafcd24ef5e7a319a7e300c0d5b221.gif)](http://share.feedsportal.com/viral/sendEmail.cfm?lang=pt&amp;title=Dica+Git+da+semana%3A+Merging&amp;link=http%3A%2F%2Fimasters.com.br%2Fartigo%2F24228%2Fdesenvolvimento%2Fdica-git-da-semana-merging)

  

[![75b9131ce15803402621ad7d693d4dd1.gif](imasters-com-br--dica-git-da-semana-merging/75b9131ce15803402621ad7d693d4dd1.gif)](http://res.feedsportal.com/viral/bookmark_pt.cfm?title=Dica+Git+da+semana%3A+Merging&amp;link=http%3A%2F%2Fimasters.com.br%2Fartigo%2F24228%2Fdesenvolvimento%2Fdica-git-da-semana-merging)

  
  
  
[[anexo ausente]](http://da.feedsportal.com/r/132918303488/u/49/f/546640/c/33212/s/1eba6e89/a2.htm) [anexo ausente]  
  
[anexo ausente]  
  
  
  
  
from iMasters - <http://feedproxy.google.com/~r/imasters/~3/0LMfApqkr8M/story01.htm>
