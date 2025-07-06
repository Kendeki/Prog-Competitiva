# https://judge.beecrowd.com/en/problems/view/1076
# Repo: https://github.com/xTecna/solucoes-da-beecrowd
# Permalink: https://github.com/xTecna/solucoes-da-beecrowd/blob/8c445fbd21659308ab039376b302e57afb009838/problemas/grafos/1076/1076.py

# O SEGUINTE CÓDIGO FOI DESENVOLVIDO POR https://github.com/xTecna

# O objetivo dele aqui é servir como referência futura, e demonstra
# os benefícios de entender o problema e suas restrições.

N = int(input())

for _ in range(N):
    N = int(input())

    n, m = [int(x) for x in input().strip().split(' ')] # readint(2)

    arestas = set() # a estrutura 'set' garante que não existam registros duplicados
    for _ in range(m):
        u, v = [int(x) for x in input().strip().split(' ')] # readint(2)

        arestas.add((u, v))
        arestas.add((v, u))

    print(len(arestas)) # sim, a resposta é LITERALMENTE 2m, subtraido da quantidade de caminhos duplicados, exemplo: (1,4) e (4,1)

# Considerações finais? fui moggado pelo beecrowd
