# https://judge.beecrowd.com/en/problems/view/1931

# PERDI NOITES DE SONO E TIVE QUE PEDIR AJUDA NO GEEKSFORGEEKS WOMP WOMP
# Relevante: "Yapping/1931.md"

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

C, V = readint(2)

SIZE = V * 10 + 3

adj = [[] for _ in range(SIZE)]

def par(x): return x * 10 + 2
def impar(x): return x * 10 + 1

for v1, v2, w in parse(3):
    adj[par(v1)].append((impar(v2), w))
    adj[impar(v1)].append((par(v2), w))
    adj[par(v2)].append((impar(v1), w))
    adj[impar(v2)].append((par(v1), w))

def dijkstra(src, dest):
    pq = []
    dist = [INF] * SIZE
    visi = [False] * SIZE
    
    dist[par(src)] = 0
    
    heapq.heappush(pq, (0, par(src)))
    
    while pq:
        _, u = heapq.heappop(pq)
        if not visi[u]:
            visi[u] = True
            for v, w in adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))
                    
    d = dist[par(dest)]
    return -1 if d == INF else d

print(dijkstra(1, C))
