from sys import stdin
from operator import itemgetter

_, em_casa, no_trabalho = list(map(int, input().split()))
days = [(home == "Y", work == "Y") for home, work in map(str.split, stdin.readlines())]

chovendo_na_saida = itemgetter(0)
chovendo_na_volta = itemgetter(1)

for day in days:
    if chovendo_na_saida(day) or no_trabalho < 1:
        print("Y", end=" ")
        em_casa -= 1
        no_trabalho += 1
    else:
        print("N", end=" ")
    if chovendo_na_volta(day) or em_casa < 1:
        print("Y")
        no_trabalho -= 1
        em_casa += 1
    else:
        print("N")