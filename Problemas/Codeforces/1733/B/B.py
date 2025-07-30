# https://codeforces.com/problemset/problem/1733/B

def solve():
  n, x, y = map(int, input().split())
  
  if x < y: x, y = y, x

  if (y != 0) or (x == 0) or (n - 1) % x != 0:
    print(-1)
    return

  k = 2
  while k <= n:
    i = 1
    while i <= x:
      i += 1
      print(k, end=" ")
    k += x

t = int(input())
for _ in range(t):
  solve()
