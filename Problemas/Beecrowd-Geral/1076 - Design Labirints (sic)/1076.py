# https://judge.beecrowd.com/en/problems/view/1076
# FIRST TRY, EU SOU O GOAT

import heapq

#automatic
import sys; iC = callable
rl = sys.stdin.readlines
def readint(n,I=input):
  if iC(I):I=I()
  s=I.split(); assert len(s) == n
  return [int(x) for x in s]
def readwith(f):
  return [f(l) for l in rl()]
def parse(n):
  return readwith(f=lambda l:readint(n,l))
#automatic

INF = 1e9

T,    = readint(1)
Tests = [None] * T

for i in range(T):
    N,   = readint(1)
    V, E = readint(2)
    Adj  = [[] for _ in range(V)]
    for _ in range(E):
        A, B = readint(2)
        Adj[A].append(B)
        Adj[B].append(A)
    Tests[i] = (V, E, Adj, N)

def solve(V, E, adj, i):
    pq = []
    
    visited = [False] * V
    dist = [INF] * V
    prev = [0  ] * V

    fScore = [INF] * V
    
    dist[i] = 0
    fScore[i] = 0

    traversed = 0

    heapq.heappush(pq, (0, i))

    def h(u):
        v = 1 if visited[u] else 0
        a = len(adj[u])
        return v + a

    while pq:
        _, u = heapq.heappop(pq)
        if not visited[u]:
            traversed += 1
            for v in adj[u]:
                visited[u] = True
                if dist[u] + 1 < dist[v]:
                    dist[v] = dist[u] + 1
                    fScore[v] = dist[v] + h(v)
                    heapq.heappush(pq, (fScore[v], v))
    return (traversed-1) * 2
    
for test in Tests:
  print(solve(*test))
