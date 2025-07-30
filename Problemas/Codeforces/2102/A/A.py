#https://codeforces.com/problemset/problem/2102/A

t = int(input())
for _ in range(t):
    n, m, p, q = map(int, input().split())

    if n % p == 0 and (n // p) * q != m:
        print("NO")
    else:
        print("YES")
