# C. Equal Values

[Link do Problema](https://codeforces.com/contest/2111/problem/C)
[Link do guia de solução](https://codeforces.com/blog/entry/143528)

### Solução/Comentários

Pra meu primeiro problema do codeforces, já percebi uma diferença enorme no layout do problema.
O codeforces tem uma linguagem muito mais formal e direta do que o beecrowd, sem historinha, sem
explicação do caso, só uma tarefa, entrada e saída.

Resolver esse problema foi bem complicado, por mais que seja só um exemplo simples do método de two pointers.
O verdadeiro desafio está no raciocínio da solução, tanto que eu precisei checar o editorial para resolver.

A solução é dividida em algumas observações simples, que vou demonstrar com um exemplo:

### Exemplo utilizado nas observações

    10
    7 5 5 5 10 9 9 4 6 10

Nesse caso, temos que N = 10.

### Observação 1:

A primeira observação é a seguinte, o custo de cada uma das operações é igual ao número de elementos afetados * o valor do indice.
Exemplo, se escolhessemos realizar a operação para os valores à esquerda do `4`, o custo seria (i - 1) * 4, ou, 7 * 4, que é o
número de elementos à esquerda do `4`.

As próximas observações eu demorei um pouco mais para entender, que são as seguintes:

### Observação 2:

Pense numa operação à esquerda realizada em um índice A, e uma à direita no índice B, onde o índice A vem depois do B, por exemplo, `A = 6` e `B = 5`.
Nesse caso, é possível reduzir o custo geral aplicando as duas operações partindo de apenas um deles. No nosso exemplo:

Forma 1 (original):

             B A
    1 2 3 4  5 6 7 8 9 10
    7 5 5 5 10 9 9 4 6 10
             ----------->
    Operação: B>, custo: (n - 5) * 10 = (10 - 5) * 10 = 50
             
             B A
    1 2 3 4  5 6 7 8 9 10
    7 5 5 5 10 9 9 4 6 10
    <-----------
    Operação: <A, custo: (i - 1) * 9 = (6 - 1) * 9 = 45

    Custo geral: 95

Forma 2 (escolhendo um):

    Teste 1: escolhendo B
             B A
    1 2 3 4  5 6 7 8 9 10
    7 5 5 5 10 9 9 4 6 10
             ----------->
    Operação: B>, custo: (n - 5) * 10 = (10 - 5) * 10 = 50

             B A
    1 2 3 4  5 6 7 8 9 10
    7 5 5 5 10 9 9 4 6 10
    <---------
    Operação: <B, custo: (i - 1) * 10 = (5 - 1) * 10 = 40

    Custo geral: 90

    Teste 2: escolhendo A
             B A
    1 2 3 4  5 6 7 8 9 10
    7 5 5 5 10 9 9 4 6 10
               --------->
    Operação: A>, custo: (n - 6) * 9 = (10 - 6) * 9 = 36

             B A
    1 2 3 4  5 6 7 8 9 10
    7 5 5 5 10 9 9 4 6 10
    <---------
    Operação: <A, custo: (i - 1) * 9 = (6 - 1) * 9 = 45

    Custo geral: 81

Dessa forma, podemos provar que existe uma solução onde as operações realizadas em A não afetam elementos alterados por B e vice versa.

# Observação 3:

Essa observação é um pouco mais intuitiva, comecemos analisando apenas as operações que afetam os elementos à esquerda.
Por exemplo, uma operação no índice `A = 5` e outra operação no índice `B = 6`. Podemos confirmar que se realizarmos apenas a operação `B`,
o efeito será o mesmo, pois o conjunto de valores afetados pela operação de `A` foi consumido pela operação em `B`:

             A B
    1 2 3 4  5 6 7 8 9 10
    7 5 5 5 10 9 9 4 6 10

    Teste 1: primeiro aplicando A, e em seguida B
      Passo 1: aplicar uma operação à esquerda em A

             A B
    1 2 3 4  5 6 7 8 9 10
    7 5 5 5 10 9 9 4 6 10
    <---------

                 A B
     1  2  3  4  5 6 7 8 9 10
    10 10 10 10 10 9 9 4 6 10

      Passo 2: aplicar uma operação à esquerda em B

            A B
    1 2 3 4 5 6 7 8 9 10
    9 9 9 9 9 9 9 4 6 10

    # Fim do primeiro teste #

    Teste 2: aplicando somente B
      Passo 1: aplicando B

            A B
    1 2 3 4 5 6 7 8 9 10
    9 9 9 9 9 9 9 4 6 10

    # Fim do segundo teste #

Com isso, temos que o estado da lista após duas operações de mesmo tipo em índices `A` e `B` é exatamente igual ao
estado da lista após uma única operação desse tipo no maior índice entre os dois, ou, `max(A,B)`.
O mesmo vale para operações à direita.

E com isso, provamos que é necessário apenas uma operação de cada tipo.

### Observação 4:

A última observação foi a raiz de toda a minha confusão em relação à esse problema, e é basicamente a solução em si.

A observação consiste no critério de escolha da solução, com as provas acima, nos certificamos de que no máximo precisaremos
de uma operação de cada, e então precisamos encontrar índices `A` e `B` que satisfaçam alguma condição específica. Vamos recaptular:

sejam `A` e `B`, os índices onde serão aplicadas, respectivamente, uma operação à esquerda, e uma operação a direita.
Provamos que existe uma solução ideal onde `A <= B`, (Observação 2).

Como escolhemos os índices?

Vamos considerar que o valor final dos elementos da lista seja um valor `x`. Apenas faria sentido, lógicamente, realizar operações
em índices que possuem o valor `x`, considerando que apenas faremos uma de cada tipo, e que todos os valores precisam ser iguais a `x`.

Com isso, no ponto de vista lógico, se o computador escolhesse dois valores ideais para `A` e `B`, podemos assumir o seguinte:

- SE `A = B`, nada a assumir, era apenas a opção de menor custo
- SE `A < B`, esse é o caso interessante, se o computador escolheu uma solução ideal onde as operações
  são realizadas em índices diferentes, isso significa que todos os índices **entre** eles já eram uma sequência
  contínua de valor `x`, portanto, o computador economizou elementos apenas excluindo essa sequência de suas operações!

### Cálculo do custo:

Por último, temos o cálculo do custo. O problema utiliza índices iniciando em 1, então considere cada `i` como i - 1 na programação do algoritmo.
Com isso, temos as seguintes expressões para o custo:

- Esquerda: `(i - 1) * v[i]`
- Direita: `(n - i) * v[i]`

Onde `v[i]` é o valor naquele índice.

Sendo, assim, com dois índices `A` e `B`, nossa expressão de custo total fica:

    T = (A - 1) * v[A] + (n - B) * v[B]

Lembrando que para a escolha dos índices ser ideal, eles precisam ter um mesmo valor `x`, portanto:

    T = (A - 1) * x + (n - B) * x

Simplificando:

    T = x * (n - 1 - (B - A))

Vamos simular uma busca no nosso exemplo:

    Índices: 1 2 3 4  5 6 7 8 9 10
    Valores: 7 5 5 5 10 9 9 4 6 10

    A = 1, B = 1
    T = x * (n - 1 - (B - A)) = 7 * (10 - 1 - (1 - 1)) = 63

    Índices: 1 2 3 4  5 6 7 8 9 10
    Valores: 7 5 5 5 10 9 9 4 6 10

    A = 2, B = 2
    
Nesse caso, ainda não calcularemos o custo total, pois, percebe-se que é possível economizar
índices com essa sequência de valores iguais pré-existente, no trecho `5 5 5`.
Ao invés de calcular, movemos o índice `B` para o final da sequência, mantendo o `A` em
posição.

    A = 2, B = 4
    T = 5 * (10 - 1 - (4 - 2)) = 35

E aplicando esse mesmo truque ao resto dos elementos da lista, utilizando o método *two-pointers*
e mantendo o menor valor encontrado de `T` em uma variável, o problema é resolvido.
