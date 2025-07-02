# https://judge.beecrowd.com/en/problems/view/1940

j, r = list(map(int, input().split()))
v = list(map(int, input().split()))

p = [0] * j

for i, n in enumerate(v):
    p[i % j] += n

m = 0
mj = 0
for jogador in range(j):
    if p[jogador] >= m:
        m = p[jogador]
        mj = jogador

print(mj + 1)
