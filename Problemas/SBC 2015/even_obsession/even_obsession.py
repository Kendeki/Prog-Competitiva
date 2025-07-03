import heapq

# UNFINISHED

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

INF = 0x7f7f7f7f7f

C, V = readint(2)

V += 1 # prevent out of bounds

adj = [[] for _ in range(V)]

for v1, v2, w in parse(3):
    adj[v1].append((v2, w))

pq = []
dist = [INF] * V
visitados = [False] * V

orig = 1

dist[orig] = 0

heapq.heappush(pq, (dist[orig], orig))

while pq:
    _, u = heapq.heappop(pq)
    if not visitados[u]:
        visitados[u] = True
        for v, c in adj[u]:
            if dist[v] > (dist[u] + c):
                dist[v] = dist[u] + c
                heapq.heappush(pq, (dist[v], v))

print(dist[C])
