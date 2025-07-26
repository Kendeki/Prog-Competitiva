Qtd = [4] * 14
win = -1


def cartify(c: str) -> int:
    global Qtd
    vi = int(c)
    Qtd[vi] -= 1
    return vi if vi < 10 else 10


int(input())
Joma = sum(map(cartify, input().split()))
Nya = sum(map(cartify, input().split()))
Pool = sum(map(cartify, input().split()))

Joma += Pool
Nya += Pool


for carta, qtd in enumerate(Qtd):
    if qtd < 1:
        continue
    carta = min(carta, 10)
    if Nya + carta == 23:
        win = carta
        break
    if Joma + carta > 23 and Nya + carta < 23:
        win = carta
        break

print(win)