# https://judge.beecrowd.com/en/problems/view/3428

int(input())
B = map(int, input().split())

A = [0] * (10**6 + 1)
T = 0

for h in B:
    if A[h] < 1:
        if h > 1:
            A[h - 1] += 1
        T += 1
    else:
        A[h] -= 1
        if h > 1:
            A[h - 1] += 1

print(T)
