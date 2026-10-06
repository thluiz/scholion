---
url: "http://tatiyants.com/risk-and-waste-on-agile-projects/"
captured_at: "2012-07-10T22:24:57-03:00"
title: "Risco e desperdício em projetos Agile"
domain: "tatiyants-com"
---

Quando você começa a "fazer Agile", o foco está em obter a mecânica certa:

  

mantenha seus updates curtos

  

não sobrecarregue no design

  

lembre-se de adicionar testes para tudo

  

lembre-se de verificar o status da CI

  

mostre apenas código de trabalho durante showcases

  

...

Isso é perfeitamente natural já que os membros da equipe se esforçam para [Competência](http://en.wikipedia.org/wiki/Dreyfus_model_of_skill_acquisition). Infelizmente, também é natural a tendência de se envolver em táticas e esquecer-se de prestar atenção ao quadro maior.

  

Afinal, Agile é simplesmente uma maneira de gerenciar projetos de software. Assim como qualquer outra metodologia de gerenciamento de projetos, ele tenta garantir a entrega bem sucedida, lidando com as coisas que fazem com que projetos fracassem. Coisas como falta de coordenação, falta de compreensão, ineficiências etc. E, embora essas armadilhas possam derrubar qualquer equipe, parece que as novas equipes Agile são particularmente propensas a duas: risco e desperdício.

  

#### Risco

  

As equipes Agile muitas vezes acreditam (fortemente) em [Emergent Design](http://xprogramming.com/classics/expemergentdesign/), enquanto omitem [Design Big Up Front](http://en.wikipedia.org/wiki/Big_Design_Up_Front). Ou seja, querem deixar o design do sistema "aparecer" ao longo do tempo, em vez de planejarem tudo à frente do tempo \*. A razão por trás disso é simples: BDUF te força a fazer escolhas de design com informações incompletas, o que leva a um trabalho desnecessário (“nós realmente precisamos de cinco camadas para carregar um conjunto de dados") ou retrabalho ("eu realmente gostaria de saber que a biblioteca X não suporta recurso Y antes de usar em todo o lugar!”).

  

Há todo um conjunto de técnicas à nossa disposição para a prática de Emergent Design: atrasar decisões até o último momento em que for possível, tentar fazer a coisa mais simples primeiro, tentar evitar construir coisas a não ser que realmente precise delas etc. Tudo isso são técnicas ótimas e úteis que devem ser utilizadas sempre que possível. Exceto quando não é possível.

  

A coisa é que, na verdade, fazer Emergent Design (especialmente em grande escala) não é trivial. Cada sistema possui requisitos imprescindíveis no projeto que podem forçar a implementação a ocorrer de uma maneira ou de outra. Por exemplo, a necessidade de expor a funcionalidade de vários tipos diferentes de consumidores muitas vezes resulta em colocar a lógica de negócios por trás de uma camada de serviços. Se esses requisitos não estiverem lá, é desnecessária e provavelmente nociva uma camada de serviços (na medida em que complica as coisas e torna o sistema menos sustentável).

  

Quando se trata de requisitos imprescindíveis no projeto, a ignorância não é uma bênção. Surpresas que resultam da descoberta de requisitos imprescindíveis no projeto tarde demais raramente são agradáveis. Na melhor das hipóteses, você pode ter mais trabalho do que você planejava. No pior caso, pode ser necessário reescrever grandes partes do sistema que você já construiu.

  

Então, seguir os princípios de Emergent Design cegamente é arriscado, pois pode fazer com que as equipes Agile adiem a descoberta de requisitos do seu sistema de design. Em outras palavras, assim como fazer BDUF pode gerar desperdício, não fazer algum projeto Up Front (SDUF?) pode fazer a mesma coisa (Sim, pode ser um tipo diferente de desperdício, mas é não deixa de ser desperdício). O que me leva ao meu próximo ponto...

  

#### Desperdícios

  

Quase por definição, processos Agile assumem que haverá algum desperdício. Quero dizer, se você está construindo algo ao longo do tempo, aprendendo e mudando à medida que avança, você terá, muito provavelmente, que voltar atrás e mudar pelo menos algumas partes criadas anteriormente. O que torna os resíduos do Agile especialmente dispendiosos é o investimento em qualidade que as equipes Agile frequentemente fazem.

  

Muito frequentemente, as equipes Agile enfatizam fortemente a construção de software de qualidade (e, se não o fazem, deveriam). Mas a qualidade não é livre. Fazer TDD, escrever testes automatizados, emparelhamento, e outras maneiras de garantir qualidade têm um custo associado a eles. Quanto mais testes você tiver dando suporte para o código que escreveu, mais testes você poderá ter que mudar se decidir refatorá-lo de forma significativa.

  

Um problema relacionado aparece quando o investimento em qualidade é feito às cegas. Se o código que você está testando realmente vai chegar à produção, então o investimento em qualidade é justificado. Por outro lado, se você faz TDD em uma solução que acaba sendo descartada ou escreve testes funcionais contra algo que irá mudar definitivamente (como uma interface de usuário em fluxo), aquele nível de investimento em qualidade não é, provavelmente, justificado. Poderá fazer mais sentido fazer um spike (ou talvez até um [tracer bullet](http://www.artima.com/intv/tracer.html)) primeiro para compreender melhor o que precisa ser feito.

  

#### Ok, vamos encerrar...

  

Assim, para resumir: descubra o risco antecipadamente para minimizar desperdícios. Fazer isso não o torna menos Ágil. É apenas bom gerenciamento de projetos.

  

\* Em seu [ótimo livro sobre os princípios Agile](http://search.safaribooksonline.com/book/programming/csharp/0131857258), Bob Martin dá um exemplo bastante ilustrativo de Emergent Design ao implementar um placar de jogo de boliche.

  

⁂

  

*Texto original disponível em <http://tatiyants.com/risk-and-waste-on-agile-projects/>*

  
[anexo ausente]  
  

[![9bcafcd24ef5e7a319a7e300c0d5b221.gif](tatiyants-com--risco-e-desperdicio-em-projetos-agile/9bcafcd24ef5e7a319a7e300c0d5b221.gif)](http://share.feedsportal.com/viral/sendEmail.cfm?lang=pt&amp;title=Risco+e+desperd%C3%ADcio+em+projetos+Agile&amp;link=http%3A%2F%2Fimasters.com.br%2Fartigo%2F24915%2Fagile%2Frisco-e-desperdicio-em-projetos-agile)

  

[![75b9131ce15803402621ad7d693d4dd1.gif](tatiyants-com--risco-e-desperdicio-em-projetos-agile/75b9131ce15803402621ad7d693d4dd1.gif)](http://res.feedsportal.com/viral/bookmark_pt.cfm?title=Risco+e+desperd%C3%ADcio+em+projetos+Agile&amp;link=http%3A%2F%2Fimasters.com.br%2Fartigo%2F24915%2Fagile%2Frisco-e-desperdicio-em-projetos-agile)

  
  
  
[[anexo ausente]](http://da.feedsportal.com/r/139262046540/u/49/f/546640/c/33212/s/2132ef42/a2.htm) [anexo ausente]  
  
[anexo ausente]  
  
  
  
from iMasters - <http://feedproxy.google.com/~r/imasters/~3/bvLbUm9agYk/story01.htm>
