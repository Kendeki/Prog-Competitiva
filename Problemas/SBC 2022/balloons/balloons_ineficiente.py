# https://judge.beecrowd.com/en/problems/view/3428

H = int(input())
B = list(map(int, input().split()))

T = 1
h = B.pop(0) - 1
x = 0

while B:
    if h in B[x:]:
        x = B.index(h)
        h = B.pop(x) - 1
    else:
        T += 1
        x = 0
        h = B.pop(0) - 1

print(T)
