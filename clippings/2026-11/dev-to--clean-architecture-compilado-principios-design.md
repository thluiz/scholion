---
url: "https://dev.to/psanrosa13/clean-architecture-um-compilado-dos-principios-de-design-2mla"
captured_at: "2026-11-16T02:01:27+00:00"
title: "Clean Architecture : um compilado dos Princípios de Design"
domain: "dev-to"
---

Confesso que demorei um pouco para entender o conteúdo que o Livro queria me trazer sobre **SOLID**, talvez seja o tempo que meu cérebro leve para assimilar as coisas.  
Por isso que eu levei um tempinho para compilar este tópico.  
Devemos entender que alguns conceitos variam de implementação para arquitetura e que quando usamos o termo dentro da área de desenvolvimento de software podemos nos referir a conceito macro, funcional, componentes, bibliotecas ou classes do seus sistema.  
Os princípios que podem variar sua aplicação de acordo com o nível em que são aplicados.  
Se você não conhece, **SOLID** é um conjunto de princípios que nos orientam para design, o que muda muito na abordagem do livro e no que citarei aqui é que muitas vezes aprendemos no nível de implementação do código e hoje vamos focar em entender no que muda para o contexto de arquitetura.  
Estes princípios nos permitem ter flexibilidade em mudanças, entendimento e melhor divisão dos domínios e reuso de componentes.

### [](#srp-princ%C3%ADpio-da-responsabilidade-%C3%BAnica)SRP - Princípio da Responsabilidade única.

Bom este princípio tem um nome que logo dar a entender que um pedaço do seu código , como classe, módulo, deve fazer apenas uma coisa.  
E este significado realmente está vinculado a um princípio, mas não a este do sólid. Essa abordagem é usada ao refatorar uma função ou método, mas não quando estamos falando do S do Solid.  
Este princípio quer dizer que um Módulo deve ter apenas uma razão para mudar. Todo sistema tem seus usuários e stakeholders, uma funcionalidade, sistema, componente está ligada a um único ator deste grupo de stakeholders/usuários e deve ser mudado somente por ele.  
Este item no nível arquitetural deve ser utilizado para encontrarmos os limites entre os sistemas e suas comunicações. Esta ação é conhecida como Eixo da Mudança e segundo o próprio autor ele vai esboçar mais isso em outros capítulos, então não vou dar spoiler, apenas acompanhe a série de artigos que você irá compreender.

### [](#ocp-princ%C3%ADpio-abertofechado)OCP - Princípio Aberto/Fechado

De certa forma, lendo este item eu me deparei muito com o uso de apis, isso porque este princípio aborda que um artefato deve ser extensível , mas sem que ele sofra modificações, fala se não te lembrou também sobre o uso de apis?  
Este item é bem conhecido na área de design de classes e módulos como sendo um dos princípios mais importantes. Porém quando falamos de componentes de arquitetura este princípio ganha mais importância, isto porque ele permite que sistemas sejam fáceis de serem utilizados em outros contextos sem que isso gere muito impacto nele mesmo. Isso permite que os sistemas de níveis alto fiquem protegidos do comportamento de quem os utiliza.

### [](#lsp-princ%C3%ADpio-de-substitui%C3%A7%C3%A3o-de-liskov)LSP : Princípio de Substituição de Liskov

Quando esse princípio surgiu, logo foi associado com o uso de herança em aplicações, porém no decorrer dos anos esse princípio foi ganhando um contexto mais amplo para o uso de interfaces e implementações.  
No contexto de arquitetura isso se aplica para garantir que o comportamento seja o mesmo independente da comunicação ou sistema, pois isso adicionaria muitos tratamentos diferentes nos fluxos de comunicação mesmo que o domínio de negócio seja o mesmo.

### [](#isp-princ%C3%ADpio-da-segrega%C3%A7%C3%A3o-de-interface)ISP : Princípio da Segregação de Interface

Esse princípio nos orienta sobre como não é eficaz depender de módulos que tem mais elementos do que vocês precisa, isso vale para dependências, mas também para níveis altos dentro da arquitetura.  
O que o seus sistema depende de A, A depende de B e quando você menos espera o B está causando impactos na sua arquitetura.  
Ou seja, nos preocuparmos com dependências que impactam na nossa arquitetura é fundamental e segundo o livro o Princípio do Reuso Comum permite coesão nos componentes da arquitetura.

### [](#dip-princ%C3%ADpio-da-invers%C3%A3o-de-depend%C3%AAncia)DIP : Princípio da Inversão de Dependência

Este princípio que fala para implementações dependerem de referências e não a itens concretos. Se olharmos para o caso do Java, teremos o uso de classes abstratas e de interfaces ao invés do uso direto da classe que implementa o código.  
No contexto arquitetural esse princípio é utilizado por exemplo para evitar vendor-lock in, que é quando existe uma dependência na sua arquitetura de um componente externo de um fornecedor e que pode gerar problemas de dependência direta dele.  
Esse princípio evita o acoplamento entre componentes arquiteturais.

#### [](#at%C3%A9-a-pr%C3%B3xima)Até a próxima...

Lembrem-se que meu intuito aqui é compilar resumidamente o que venho entendendo e lendo no livro **Clean Architecture**, do Tio Bob, assim despertando em você entusiasmo para ler o livro, bom pelo menos é essa a minha intenção :)  
**Aguardem os próximos capítulos.**
