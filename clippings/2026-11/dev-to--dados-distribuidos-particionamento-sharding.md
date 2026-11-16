---
url: "https://dev.to/brenoferreira/dados-distribuidos-particionamento-sharding-pip"
captured_at: "2026-11-16T02:01:52+00:00"
title: "Dados distribuídos — Particionamento/Sharding"
domain: "dev-to"
---

Parte da [série](https://dev.to/brenoferreira/designing-data-intensive-apps-um-resumo-2df9) sobre o resumo do livro [Designing Data Intensive Apps](https://amzn.to/2YaKEhB).

Até aqui, falamos sobre alguns temas gerais sobre bancos de dados: [Sistemas de dados](https://dev.to/brenoferreira/designing-data-intensive-apps-um-resumo-390c), [Modelos de Dados](https://dev.to/brenoferreira/designing-data-intensive-apps-resumo-cap-2-4b75), [Armazenamento de Dados](https://dev.to/brenoferreira/designing-data-intensive-apps-capitulo-3-1693), [Serialização de Dados](https://dev.to/brenoferreira/encoding-e-dataflow-4p60) e [Replicação de Dados](https://dev.to/brenoferreira/dados-distribuidos-replicacao-de-dado-1n96).

Uma outra técnica que pode ser utilizado para aumentar a escalabilidade do banco de dados é particionamento (ou também conhecido como sharding) de dados que pode ser aplicado em conjuntos de dados muito grandes com com um volume de queries muito alto.

[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fcdn-images-1.medium.com%2Fmax%2F1600%2F1%2AeFvhv5GyO_1rgMKFo1XDUQ.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fcdn-images-1.medium.com%2Fmax%2F1600%2F1%2AeFvhv5GyO_1rgMKFo1XDUQ.png)

### [](#como-particionar-os-dados)Como particionar os dados?

Uma parte mais dificil de particionar dados é: como particionar? Existem técnicas diferentes, algumas funcionam melhores que outras.

Técnicas mais ingênuas de particionamento costumam causar hot-spots em algumas partições, ou seja, um número muito alto de acessos à uma única partição enquanto as outras estão paradas. Por exemplo:

Numa rede social, particionar por username. Entao, cada partição armazenaria dados de usuarios com username começando de A à C, de D à F, etc..

[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fcdn-images-1.medium.com%2Fmax%2F1600%2F1%2AERByZVRYhLILPKVnMHm22w.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fcdn-images-1.medium.com%2Fmax%2F1600%2F1%2AERByZVRYhLILPKVnMHm22w.png)

No Instagram por exemplo, os [usuários com mais seguidores](https://en.wikipedia.org/wiki/List_of_most-followed_Instagram_accounts) estão distribuídos da seguinte forma:

[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fcdn-images-1.medium.com%2Fmax%2F1600%2F1%2ATPovGfwzmjPgHyPgBqNxpw.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fcdn-images-1.medium.com%2Fmax%2F1600%2F1%2ATPovGfwzmjPgHyPgBqNxpw.png)

Dá pra perceber que nesse caso a primeira partição seria um hot spot, pois 2 dos 3 usuarios com mais seguidores tem seu username começando com A, B ou C (Ariana Grande e Cristiano Ronaldo), além de Beyonce em 9 lugar. Todos com centenas de milhões de seguidores. Olhando o ranking dá pra perceber que usuários com +100 milhões de usuários tem as iniciais mais comuns T, K, J, N.

Outro exemplo: particionar por data. Digamos que dados escritos num dia são escritos em partições diferentes. Caso haja um volume muito alto de escrita, em cada dia uma partição será o hotspot, enquanto as outras só irão atender à requisições de leitura.

#### [](#consistent-hashing-partitioning)Consistent Hashing Partitioning

Uma técnica que ajuda a diminuir (mas não eliminar) esses hotspots é particionar por um hash. No exemplo da rede social, voce pode calcular um hash do username e armazenar em alguma partição. Esses hashes devem ser distribuídos uniformemente entre as partições.

[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fcdn-images-1.medium.com%2Fmax%2F1600%2F1%2ATsj5HOfQTHELQExjClZqPg.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fcdn-images-1.medium.com%2Fmax%2F1600%2F1%2ATsj5HOfQTHELQExjClZqPg.png)

Particionar por hash ainda não elimina hotspots. Por exemplo a partição onde os dados do Cristiano Ronaldo estão armazenados vai continuar sendo muito acessada. Mas assim voce consegue distribuir melhor os dados e a carga.

### [](#problemas-com-particionamento)Problemas com particionamento

Claro que os problemas não iriam acabar aí.

No caso de bancos de dados relacionais, joins agora podem potencialmente ser distribuídos em varios nós, consequentemente, bem menos eficientes. Por isso saber escolher bem sua estratégia de particionamento é importante.

Outro problema ocorre com índices secundários. No caso do índice primário no hash da chave, os dados estão na mesma partição, então não costuma ser muito problemático. Mas em um índice secundário os dados provavelmente vão estar em partições diferentes. Por exemplo: armazenando dados de livros, voce particiona pelo hash do código ISBN, mas com certeza vai precisar também de um índice secundário no título dos livros para buscas eficientes. Então, os livros sobre "Computação Distribuída" não vão estar necessariamente na mesma partição.

[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fcdn-images-1.medium.com%2Fmax%2F1600%2F1%2AidIsm7Q4aRMYh24jSkpm_Q.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fcdn-images-1.medium.com%2Fmax%2F1600%2F1%2AidIsm7Q4aRMYh24jSkpm_Q.png)  
Índice secundário local

Uma estratégia é cada partição manter seus índices secundários para os seus próprios dados. Então, quando um cliente executa uma consulta, é necessario consultar os índices de cada partição, numa operação conhecida como scatter/gather. Essas consultas geralmente costumam ser bem lentas.

[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fcdn-images-1.medium.com%2Fmax%2F1600%2F1%2AYfguGRoWVv-UxOOlO96F-w.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fcdn-images-1.medium.com%2Fmax%2F1600%2F1%2AYfguGRoWVv-UxOOlO96F-w.png)  
Índice secundário global

Outra estratégia é criar um índice global particionado. No exemplo de livros, o termo "Computação" estaria no índice na partição 1, enquanto o termo "Medicina" estaria no índice na partição 3. Os dados em si podem estar em outras partições, mas ao contrário do índice local por partição, não é necessário fazer uma busca em **todas** as partições, pois o índice por termo garante que voce encontra todos os documentos associados àquele termo e buscar diretamente nas partições que contêm os dados, melhorando a performance de consulta. O problema com essa estratégia é que a performance de escrita é ruim, pois esse índice distribuído precisa ser atualizado à cada escrita. Essa atualização geralmente é feita de maneira assíncrona, então ela sofre com o Lag de Replicação que foi abordado no post anterior. Manter um índice distribuído fortemente consistente requer uma transação distribuída, que é bem custosa.
