---
url: "https://thoughtworks.com/pt/insights/blog/functional-tests-how-decide-what-automate"
captured_at: "2026-11-16T03:25:40+00:00"
title: "Testes Funcionais - Como decidir o que automatizar?"
domain: "thoughtworks-com"
---

Quando estamos trabalhando em projetos de entrega de software, nós eventualmente teremos que encarar a decisão de automatizar ou não um teste para um cenário específico. O questionamento sobre se devemos automatizar ou não é o que vamos discutir neste artigo.

### Porque nós automatizamos

Geralmente, nós automatizamos para evitar trabalho manual repetido, obter um feedback mais rápido, economizar tempo executando testes repetidamente, e assegurar que estamos sempre executando testes de forma consistente com as mesmas precondições e expectativas.

Executar testes manuais repetidas vezes é algo chato, e além disso, seres humanos executando um monte de testes manualmente não alcançam o mesmo resultado todas as vezes. Fatores como o viés de confirmação e o erro humano entram em jogo. Em algum momento, uma pessoa poderia executar um teste manualmente e perder um passo importante, deixando de identificar um bug na aplicação que está sendo testada.

![How to decide what to automate or not](https://thoughtworks.com/content/dam/thoughtworks/images/photography/inline-image/insights/blog/testing/blg_inline_functional_tests_how_decide_what_automate.jpg)

O feedback rápido é importante para qualquer estratégia de integração contínua de sucesso, e fundamental na medida em que você se direciona à Entrega Contínua. Ele permite que você identifique se há alguma regressão na qualidade no momento em que o código é consolidado, permitindo que a equipe corrija problemas assim que eles são apresentados. O feedback rápido também nos permite ter nossos cenários de teste reproduzíveis a qualquer momento que precisarmos executá-los novamente. A equipe também poderá contar com ele para implementar mudanças, ou para refatorar o código.

Entretanto, mesmo com todos esses benefícios, ele não anula a necessidade de fazer testes exploratórios na aplicação em algum momento na pipeline.

### O que nós automatizamos

Ao decidir que testes automatizar, primeiramente precisamos observar a Pirâmide de Testes de Mike Cohn. Em sua essência, a pirâmide demonstra que há muito mais testes unitários do que testes automatizados de UI, de serviço ou de integração de alto nível.

O instinto natural de alguém que é novato em automação de teste é tentar cobrir todos os cenários que seriam testados manualmente. A integração contínua requer testes automatizados, porque para cada pequena mudança, somos capazes de reexecutar todas as regressões e nos certificarmos de que não estamos estragando nada.

No entanto, testes funcionais podem, mesmo sem a intenção, criar um enorme conjunto de casos de teste, gerando consequências inconvenientes. Mesmo que para cada nova história nós adicionemos um pequeno conjunto de testes funcionais, depois de algumas iterações nossa suíte de regressão vai levar um tempo considerável para ser executada. Uma suíte de testes de regressão de longa duração se torna rapidamente um gargalo ao consolidar alterações. Consequentemente, os desenvolvedores vão consolidar com menos frequência e com consolidações maiores.

Na medida que uma aplicação evolui, nós não queremos simplesmente manter um conjunto de casos de teste cada vez maiores e que estão sendo executados eternamente. Nós queremos um conjunto de testes que garanta que as funcionalidades novas e as existentes estejam funcionando conforme o esperado. Uma abordagem mais eficiente seria cobrir as áreas que são mais importantes em uma perspectiva empresarial, ou que são conhecidas por serem instáveis ​​e terem uma maior probabilidade de apresentarem erros.

Nosso foco deve ser criar uma suíte de testes de alto valor, que foca nas áreas críticas de negócios do nosso produto. Para alcançar nosso objetivo, precisamos levar os dois pontos de vista em consideração, associando dois conceitos a cada história: relevância de negócios e taxa de erro de cada funcionalidade. Desta forma, podemos construir uma matriz para determinar quais funcionalidades têm mais impacto e deveriam ter mais testes.

Por exemplo:

Features

Business Relevance

Error Rate

Total

Inbox

2

3

5

New mail

1

2

3

Login

3

1

4

Settings

1

1

2

Como sabemos, a relevância de negócios muda ao longo do tempo e a probabilidade de falha em um teste que está sendo executado por um longo tempo é baixa. Os resultados dos testes devem ser revisados constantemente para determinar qual deve permanecer em nosso conjunto de testes funcional. Portanto, nós sugerimos que você avalie seus testes a cada iteração.

### Conclusion

Ao implementar integração contínua, é importante ter uma suíte de testes automatizados que executa de forma rápida e fornece confiança em seu produto. Ter a capacidade de entregar valor de negócios mais rápido que seus concorrentes está se tornando muito importante no mercado digital. Uma boa estratégia de automação de testes que pode garantir qualidade de software mais rápido, o coloca um passo à frente de seus concorrentes. Entretanto, sabemos que não há garantias quando falamos de estratégia de teste. A situação sempre dependerá do projeto e do tipo de testes que precisamos ter em foco para atingir os objetivos do projeto.
