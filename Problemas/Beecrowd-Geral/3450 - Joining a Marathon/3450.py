from sys import stdin
from typing import Callable


def corredor(t0: int, v: int) -> Callable[[int], int]:
    return lambda t: v * (t - t0)


def foto(t: int, A: int, B: int) -> Callable[[Callable[[int], int]], bool]:
    return lambda f: f(t) >= A and f(t) <= B


corredores_n = int(input())
corredores = [corredor(*map(int, input().split())) for _ in range(corredores_n)]

# 10^6
fotos_n = int(input())
fotos = [foto(*map(int, input().split())) for _ in range(fotos_n)]

lixos = list(
    filter(lambda foto: not any((foto(corredor)) for corredor in corredores), fotos)
)

int(input())
for q_t0, q_v in (map(int, line.split()) for line in stdin.readlines()):
    contagem = len(lixos)
    for lixo in lixos:
        if lixo(corredor(q_t0, q_v)):
            contagem -= 1
    print(contagem)
