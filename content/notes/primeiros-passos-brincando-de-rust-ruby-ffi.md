---
title: "[Primeiros Passos] Brincando de Rust + Ruby/FFI"
date: '2015-06-06T18:08:09-03:00'
category: webclip
summary: 'O texto mostra um experimento com Rust e Ruby usando FFI para processar um arquivo do IMDb, explica noções básicas de Cargo, ownership, Result e Option, e compara desempenho entre as duas abordagens.'
tags: ["rust", "ruby-ffi", "ownership", "cargo"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "[Primeiros Passos] Brincando de Rust + Ruby/FFI | AkitaOnRails.com"
    url: "http://www.akitaonrails.com/2015/06/05/primeiros-passos-brincando-de-rust-ruby-ffi#.VXNersu5fqA"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-06/akitaonrails-com--primeiros-passos-brincando-de-rust-ruby-ffi.md"
    kind: repo
---

O artigo usa um arquivo de atores do IMDb como teste para comparar uma versão em Ruby com uma versão em Rust. Primeiro apresenta o script Ruby, depois o código Rust equivalente, explica Cargo, o arquivo Cargo.toml e a diferença entre bibliotecas, binários e dependências no ecossistema do Rust. Também mostra como expor uma função Rust para consumo via FFI no Ruby.

O texto passa por tipos, generics, String e str, mutabilidade, ownership, borrowing, lifetime, Result, Option, unwrap e match. Na comparação de desempenho, a versão Ruby aparece mais rápida no teste inicial, mas a troca da crate regex por pcre faz a implementação em Rust ficar bem mais veloz. No fechamento, o autor destaca que Rust exige adaptação, é voltado a tarefas de sistema e tem um modelo de memória mais seguro, com Cargo ajudando bastante no fluxo de compilação.

## Fichamento

- Usa um arquivo de atores do IMDb como base para comparar um processamento em Ruby com outro em Rust.
- O exemplo Ruby percorre o arquivo, separa ator e filme, acumula os nomes e devolve a lista final.
- O projeto em Rust usa Cargo, com Cargo.toml para tarefas e dependências, e o autor compara isso ao par Rake/Bundler.
- O código Rust apresentado trabalha com File, BufReader, Regex e um vetor de Strings para chegar ao mesmo resultado.
- O texto explica que Rust tem tipos declarados, inferência de tipos, structs, Traits e Generics.
- Também descreve String e str, além de mutabilidade explícita com let mut.
- O modelo de ownership, borrowing e lifetime aparece como um dos pontos mais difíceis para quem vem de Ruby ou JavaScript.
- O artigo explica que Rust não usa garbage collector e busca desalocação determinística com base em stack e propriedade dos valores.
- unwrap é apresentado como atalho para lidar com Result quando o erro não será tratado.
- match, Result e Option são mostrados como a forma do Rust de lidar com falhas e ausência de valor sem exceptions nem null.
- A seção de FFI mostra uma função extern C com #[no_mangle] que recebe ponteiros, converte strings de C para String e devolve um ponteiro para uso no Ruby.
- Do lado do Ruby, o código usa a gem ffi para ligar na biblioteca compilada em target/release.
- No teste inicial, a versão Ruby aparece um pouco mais rápida que a versão Rust.
- Depois, com um arquivo maior, o Ruby ainda vence no tempo medido pelo autor.
- O texto atribui isso ao custo de I/O, à engine de regex e ao fato de a crate regex ainda ser imatura naquele momento.
- Quando a crate regex é trocada por pcre, a versão Rust passa a ser bem mais rápida que a Ruby.
- A conclusão defende que Rust já era uma linguagem de sistema promissora, mais segura para memória e adequada para bibliotecas nativas e ferramentas de linha de comando.
