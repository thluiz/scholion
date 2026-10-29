---
url: "http://elemarjr.net/2015/09/08/usando-o-project-euler-para-aprender-f-problemas-6-7-8-9-e-10/"
captured_at: "2015-09-09T10:34:21-03:00"
title: "Usando o “Project Euler” para aprender F# – Problemas 6, 7, 8, 9 e 10"
domain: "elemarjr-net"
---

# Usando o “Project Euler” para aprender F# – Problemas 6, 7, 8, 9 e 10

Continuo minha cruzada para aprender F#. Como ando sem tempo para um projeto “grande”, como o de [Xadrez](https://github.com/ElemarJR/SolvingChess), estou resolvendo os problemas propostos pelo “[Projeto Euler](https://projecteuler.net/)“. Se ainda não conhece, vai lá conhecer.

Neste post, apresento as soluções para os problemas 6, 7, 8, 9 e 10.

### Problema 6

Enunciado:

> The sum of the squares of the first ten natural numbers is,
>
> 12 + 22 + … + 102 = 385
>
> The square of the sum of the first ten natural numbers is,
>
> (1 + 2 + … + 10)2 = 552 = 3025
>
> Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
>
> Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

Solução:

|  |  |
| --- | --- |
|  | `let` `SumSquareDifference max =`  `let` `inline` `sq x = x * x`  `let` `sumOfSquare =`  `[1..max]`  `|> List.map sq`  `|> List.sum`  `let` `squareOfSum =`  `[1..max]`  `|> List.sum`  `|> sq`  `squareOfSum - sumOfSquare`  `SumSquareDifference 10`  `SumSquareDifference 100` |

### Problema 7

Enunciado:

> By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
>
> What is the 10001st prime number?

Solução:

|  |  |
| --- | --- |
|  | `let` `nth_prime n =`  `let` `inline` `ub n =  int64 (sqrt(double(n)))`  `let` `isPrime n =`  `let` `rec` `iterate i =`  `i > ub(n) || (n % i <> 0L && iterate (i + 1L))`  `iterate 2L`  `let` `rec` `primes x = seq {`  `if` `(isPrime x)` `then` `yield` `x`  `yield``! primes (x + 1L)`  `}`  `primes 2L`  `|> Seq.item (n - 1)`  `nth_prime 6`  `nth_prime 10001` |

### Problema 8

Enunciado:

> The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
>
> 73167176531330624919225119674426574742355349194934  
> 96983520312774506326239578318016984801869478851843  
> 85861560789112949495459501737958331952853208805511  
> 12540698747158523863050715693290963295227443043557  
> 66896648950445244523161731856403098711121722383113  
> 62229893423380308135336276614282806444486645238749  
> 30358907296290491560440772390713810515859307960866  
> 70172427121883998797908792274921901699720888093776  
> 65727333001053367881220235421809751254540594752243  
> 52584907711670556013604839586446706324415722155397  
> 53697817977846174064955149290862569321978468622482  
> 83972241375657056057490261407972968652414535100474  
> 82166370484403199890008895243450658541227588666881  
> 16427171479924442928230863465674813919123162824586  
> 17866458359124566529476545682848912883142607690042  
> 24219022671055626321111109370544217506941658960408  
> 07198403850962455444362981230987879927244284909188  
> 84580156166097919133875499200524063689912560717606  
> 05886116467109405077541002256983155200055935729725  
> 71636269561882670428252483600823257530420752963450
>
> Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

Solução:

|  |  |
| --- | --- |
|  | `open` `System`  `let` ``` ``1000 digits number`` = ```  `"73167176531330624919225119674426574742355349194934"` `+`  `"96983520312774506326239578318016984801869478851843"` `+`  `"85861560789112949495459501737958331952853208805511"` `+`  `"12540698747158523863050715693290963295227443043557"` `+`  `"66896648950445244523161731856403098711121722383113"` `+`  `"62229893423380308135336276614282806444486645238749"` `+`  `"30358907296290491560440772390713810515859307960866"` `+`  `"70172427121883998797908792274921901699720888093776"` `+`  `"65727333001053367881220235421809751254540594752243"` `+`  `"52584907711670556013604839586446706324415722155397"` `+`  `"53697817977846174064955149290862569321978468622482"` `+`  `"83972241375657056057490261407972968652414535100474"` `+`  `"82166370484403199890008895243450658541227588666881"` `+`  `"16427171479924442928230863465674813919123162824586"` `+`  `"17866458359124566529476545682848912883142607690042"` `+`  `"24219022671055626321111109370544217506941658960408"` `+`  `"07198403850962455444362981230987879927244284909188"` `+`  `"84580156166097919133875499200524063689912560717606"` `+`  `"05886116467109405077541002256983155200055935729725"` `+`  `"71636269561882670428252483600823257530420752963450"`  `let` `digits =`  ``` ``1000 digits number``.ToCharArray() ```  `|> Seq.map (``fun` `x -> Int64.Parse(x.ToString()))`  `|> List.ofSeq`  `let` `mul numbers = numbers |> Seq.fold (*) 1L`  `let` `largestProduct l =`  `[0 .. (digits.Length - (l + 1))]`  `|> List.map (``fun` `start -> [0..(l - 1)] |> Seq.map(``fun` `a -> digits.[start + a]) |> mul)`  `|> List.max`  `largestProduct 4`  `largestProduct 13` |

### Problema 9

Enunciado:

> A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
>
> a2 + b2 = c2
>
> For example, 32 + 42 = 9 + 16 = 25 = 52.
>
> There exists exactly one Pythagorean triplet for which a + b + c = 1000.  
> Find the product abc.

Solução:

|  |  |
| --- | --- |
|  | `let` `problem9 =`  `let` `euclid_pythagorean_triplets limit =`  `[`  `for` `m` `in` `1 .. limit` `do`  `for` `n` `in` `1 .. m-1` `do`  `let` `a = m*m-n*n`  `let` `b = 2*m*n`  `let` `c = m*m+n*n`  `yield` `[a;b;c]`  `]`  `euclid_pythagorean_triplets 1000`  `|> List.find (``fun` `[a; b; c] -> a + b + c = 1000)`  `|> List.fold (*) 1` |

### Problema 10

Enunciado:

> The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
>
> Find the sum of all the primes below two million.

Solução:

|  |  |
| --- | --- |
|  | `let` `sumOfProblemsBellow n =`  `let` `inline` `ub n =  int64 (sqrt(double(n)))`  `let` `isPrime n =`  `let` `rec` `iterate i =`  `i > ub(n) || (n % i <> 0L && iterate (i + 1L))`  `iterate 2L`  `let` `rec` `primes x = seq {`  `if` `(isPrime x)` `then` `yield` `x`  `yield``! primes (x + 1L)`  `}`  `primes 2L`  `|> Seq.takeWhile (``fun` `x -> x < n)`  `|> Seq.sum`  `sumOfProblemsBellow 10L`  `sumOfProblemsBellow 2000000L` |

Era isso.

### Deixe um comentário [Cancelar resposta](http://elemarjr.net/2015/09/08/usando-o-project-euler-para-aprender-f-problemas-6-7-8-9-e-10/#respond)
