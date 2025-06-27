# https://judge.beecrowd.com/en/problems/view/3428

# ignora a primeira linha do input (o numero de baloes)
int(input())

# pega os balao
baloes = list(map(int, input().split()))

# parte mais importante
# isso aqui inicializa a lista que contem o
# número de flechas em uma determinada altura,
# por exemplo, se flechas_na_altura[5] = 10,
# significa que existem 10 flechas na altura 5
flechas_na_altura = [0] * (10**6 + 1)

# numero de flechas atiradas, elas saem sob demanda
flechas_totais = 0

for y in baloes:
    # se não houverem flechas na altura do balao atual,
    # atiramos uma flecha exclusiva para ele, aumentando o total
    # e colocando a flecha (que acabou de acertá-lo) na sua
    # próxima posição
    if flechas_na_altura[y] < 1:
        flechas_totais += 1
        # proteção para caso a flecha já esteja no fim do mapa
        if y > 1:
            flechas_na_altura[y - 1] += 1
    # caso hajam flechas na altura do balao atual, aproveitamos
    # essa flecha para remover esse balao, sem precisar gastar
    # uma flecha extra para ele, assim como antes, a flecha
    # também é colocada na sua próxima posição
    else:
        flechas_na_altura[y] -= 1
        if y > 1:
            flechas_na_altura[y - 1] += 1

print(flechas_totais)
