# https://olimpiada.ic.unicamp.br/pratique/ps/2021/f2/sanduiche/

from itertools import *

N, M = map(int, input().split())
R = [set(map(int, input().split())) for _ in range(M)]
C = (combinations(range(1, N+1), x) for x in range(2, N+1)) # skip the 1

def comblen(it): return sum((1 for seq in it
                             if all((not r.issubset(seq) for r in R))))

X = sum((comblen(it) for it in C))

print(N + X)