# https://codeforces.com/problemset/problem/2123/C

def presufix():
    nTestes = int(input())
    for _ in range(nTestes):
        tamanho = int(input())
        lista = [int(x) for x in input().split()]

        pre = [lista[0]]
        suf = [0] * tamanho
        suf[-1] = lista[-1]

        for i in range(1, tamanho):
            pre.append(min(pre[-1], lista[i]))
        for i in range(tamanho - 2, -1, -1):
            suf[i] = max(suf[i + 1], lista[i])

        print("".join("1" if lista[i] in (pre[i], suf[i]) else "0" for i in range(tamanho)))

presufix()
