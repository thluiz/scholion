---
url: "http://elemarjr.com/2016/12/26/melhorando-validacoes-no-dominio-com-melhores-assinaturas-de-metodo-e-logica-funcional-parte-2/"
captured_at: "2016-12-28T08:26:53-03:00"
title: "Melhorando validações no domínio com melhores assinaturas de método e lógica funcional (Parte 2)"
domain: "elemarjr-com"
---

# Melhorando validações no domínio com melhores assinaturas de método e lógica funcional (Parte 2)

*Tempo de leitura: 4 minutos*

O [post anterior](http://elemarjr.com/pt/2016/11/29/melhorando-validacoes-no-dominio-com-melhores-assinaturas-de-metodo-e-logica-funcional/) dividiu opiniões. Houve quem gostasse da abordagem que eu indiquei. Também houve quem achasse complexa demais.

Embora eu tenha deixado claro, logo no início, que havia selecionado um exemplo trivial apenas para poder apresentar conceitos, um bocado de gente ignorou tal aviso.

Pois bem, o post de hoje trata da aplicação dos conceitos apresentados no post anterior em cenários "do mundo real".

### Cenário

Imaginemos um exemplo simples, porém, relacionado com o código que escrevemos no dia-a-dia. Pensemos em 1) recuperar uma entidade do banco de dados, 2) aplicar uma modificação e 3) persistir a entidade modificada.

Como você implementaria isso?

### Uma abordagem frequente

Um caminho muito comum para resolver esse cenário seria algo semelhante ao indicado nesse esboço:

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13 | `public` `class` `EmployeeRepository`  `{`  `/* .. */`  `public` `Employee GetById(``string` `id) {` `/* .. */` `}`  `public` `void` `Save(Employee employee) {` `/* .. */` `}`  `/* .. */`  `}`  `public` `class` `Employee`  `{`  `/* .. */`  `public` `void` `RaiseSalary(``decimal` `amount) {` `/* .. */` `}`  `}` |

Há aqui um repositório (que é um serviço do domínio) que consegue recuperar e persistir a entidade que está sendo manipulada (no exemplo *Employee*). Também há uma entidade com um método que revela a motivação da mudança.

Parece estar tudo certo, não? Um exemplo de consumo poderia ser:

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22 | `class` `DummySalaryService`  `{`  `private` `readonly` `EmployeeRepository _repository;`  `public` `DummySalaryService(EmployeeRepository repository)`  `{`  `_repository = repository;`  `}`  `public` `void` `RaiseSalaryOfEmployee(``string` `employeeId,` `decimal` `amount)`  `{`  `var` `employee = _repository.GetById(employeeId);`  `if` `(employee ==` `null``)`  `{`  `// deveríamos lançar uma Exception?`  `}`  `employee.RaiseSalary(amount);`  `_repository.Save(employee);`  `}`  `}` |

Você percebe as fragilidades desse código?

### Crítica a forma como a entidade é recuperada

Vamos nos concentrar, por um breve instante, na forma como a entidade é recuperada.

|  |  |
| --- | --- |
| 1 | `public` `Employee GetById(``string` `id) {` `/* .. */` `}` |

O que essa assinatura nos diz?

Basicamente, sabemos que devemos passar o Id (que é um string) da entidade que desejamos recuperar e receberemos uma instância da entidade materializada.

Mas, por essa assinatura, me responda:

1. O que ocorre caso seja fornecido um Id inválido (*null*, por exemplo)?
2. O que ocorre caso não exista uma entidade correspondente ao Id fornecido? Será lançada uma *exception*? Será retornado *null*?
3. O que ocorre se houver um problema de conexão com o banco de dados?

Por convenção, você poderia afirmar que a passagem de um parâmetro inválido deveria disparar um *ArgumentException*, certo? Mas, se o cliente dessa API passar *null*, será disparada uma *ArgumentNullException*?

Caso o parâmetro fornecido seja válido, mas sem correspondência, o serviço retornará um *null*? Lançará uma *Exception*?

Muitas perguntas em aberto. Muitas respostas que serão conferidas apenas em tempo de execução ou inspecionando o código e facilmente ignoradas por programadores descuidados. Para mim, isso explica o porquê de tantos erros ridículos em tempo de execução.

### Tornando a assinatura mais clara

Pois bem, utilizando os tipos elevados que apresentei no post anterior (com [implementação no GitHub](https://github.com/ElemarJR/ElemarJR.FunctionalCSharp), caso tenha interesse), compartilho uma implementação mais coerente:

|  |  |
| --- | --- |
| 1 | `public` `Try<Exception, Employee> GetById(Untrusted<``string``> id) {` `/* .. */` `}` |

O que essa assinatura está nos dizendo:

1. Haverá uma tentativa de recuperar a entidade. Essa tentativa irá retornar a entidade, caso ela exista e tudo ocorrer bem, ou uma exception caso, por algum motivo, não seja possível recuperar a entidade.
2. O parâmetro que será recebido será tratado como pouco confiável. Afinal, não há garantias de que o Id esteja formatado adequadamente.

Ainda melhor seria enriquecer o modelo de domínio com uma nova primitiva representando um Id natural.

|  |  |
| --- | --- |
| 1 | `public` `Try<Exception, Employee> GetById(Cpf cpf) {` `/* .. */` `}` |

Estou afastando a possibilidade de retornar *null* para um id sem entidade correspondente.

### Crítica e proposta para a modificação do estado da entidade

A implementação da entidade proposta originalmente está, honestamente, melhor do que aquelas que tenho encontrado no "mundo real". Há um método que revela claramente a "motivação para a mudança" no lugar de uma propriedade estúpida com um *setter* anêmico. Entretanto, nem por isso, está livre de críticas.

Implementações mutáveis conduzem ao desenvolvimento de código difícil de manter, principalmente em cenários onde seja necessário suportar concorrência. Por isso, há tempos, venho usando entidades imutáveis.

Além disso, a assinatura original oculta o fato de que, caso uma regra de negócio seja violada, uma *exception* poderia ser disparada.

Minha proposta aqui seria:

|  |  |
| --- | --- |
| 1  2  3  4  5 | `public` `class` `Employee`  `{`  `/* .. */`  `public` `Try<Exception, Employee> RaiseSalary(``decimal` `amount) {` `/* .. */` `}`  `}` |

A modificação que estou propondo indica claramente que o método poderia resultar em uma *exception* ou em uma nova instância de *Employee* com o valor atualizado.

### Crítica e proposta para a persistência da entidade

Por fim, tempos a persistência da entidade.

Bertrand Meyer propôs que métodos deveriam operar como comandos, alterando o estado da entidade, ou como consultas, retornando alguma coisa. Logo, a proposta original para persistência da entidade parece correta.

|  |  |
| --- | --- |
| 1 | `public` `void` `Save(Employee employee) {` `/* .. */` `}` |

A verdade, porém, não é tão simples. Esse método pode (e deve) disparar uma *exception* caso algo inesperado ocorra. Mas, ele não deixa isso claro.

Minha proposta seria:

|  |  |
| --- | --- |
| 1 | `public` `Try<Exception, Unit> Save(Employee employee) {` `/* .. */` `}` |

O que estou propondo aqui é deixar claro que esse método pode falhar e forçar quem está implementando a oferecer tratamento adequado.

O tipo Unit, usado aqui, é uma implementação vazia, de marcação, usada em lugar de *void*.

### A versão revisada

A versão que eu recomendo para resolver o cenário proposto seria assim:

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13 | `public` `class` `EmployeeRepository`  `{`  `/* .. */`  `public` `Try<Exception, Employee> GetById(Untrusted<``string``> id) {` `/* .. */` `}`  `public` `Try<Exception, Unit> Save(Employee employee) {` `/* .. */` `}`  `/* .. */`  `}`  `public` `class` `Employee`  `{`  `/* .. */`  `public` `Try<Exception, Employee> RaiseSalary(``decimal` `amount) {` `/* .. */` `}`  `}` |

Aqui, o código todo indica claramante o que esperar de cada implementação.

Mas, o melhor está na implementação do código cliente.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16 | `class` `DummySalaryService`  `{`  `private` `readonly` `EmployeeRepository _repository;`  `public` `DummySalaryService(EmployeeRepository repository)`  `{`  `_repository = repository;`  `}`  `public` `Try<Exception, Unit> RaiseSalaryOfEmployee(``string` `employeeId,` `decimal` `amount)`  `{`  `return` `_repository.GetById(employeeId)`  `.Bind(employee => employee.RaiseSalary(amount))`  `.Bind(updatedEmployee => _repository.Save(updatedEmployee));`  `}`  `}` |

Dessa vez, o método está indicando claramente que pode falhar. Entretanto, o código segue um fluxo lógico de sucesso (Não há contaminações com tratamento de falhas).

Se o nome *Bind* (que é um operador funcional) te incomoda, pode recorrer a um simplificador

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7 | `public` `static` `class` `TryExtensions`  `{`  `public` `static` `Try<TFailure, TSuccessResult> Then<TFailure, TSuccess, TSuccessResult>(`  `this` `Try<TFailure, TSuccess> that,`  `Func<TSuccess, Try<TFailure, TSuccessResult>> func`  `) => that.Bind(func);`  `}` |

Quem sabe, pode até escrever algo assim:

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14 | `class` `DummySalaryService`  `{`  `private` `readonly` `EmployeeRepository _repository;`  `public` `DummySalaryService(EmployeeRepository repository)`  `{`  `_repository = repository;`  `}`  `public` `Try<Exception, Unit> RaiseSalaryOfEmployee(``string` `employeeId,` `decimal` `amount)`  `=> _repository.GetById(employeeId)`  `.Then(employee => employee.RaiseSalary(amount))`  `.Then(updatedEmployee => _repository.Save(updatedEmployee));`  `}` |

Masturbação funcional? Complexidade desnecessária? Sério? Eu vejo código mais expressivo e com muito menos chances de falha em tempo de execução.

Era isso.
