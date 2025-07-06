# https://judge.beecrowd.com/pt/problems/view/1340

# QUE SOLUÇÃO PORCA

#automatic
import sys;from collections import deque
lns = deque(map(lambda l:l.strip().split(), sys.stdin.readlines()))
def readint(n):
  return [int(x) for x in lns.popleft()]
def EOF(): return not lns
#automatic
import heapq
QUEUE = 0
STACK = 1
PQ = 2
while not EOF():
  N, = readint(1)
  values = [0] * 1000
  possible = [True, True, True]
  np = 3
  pq = []
  s = deque([])
  q = deque([])
  
  for _ in range(N):
    O, x = readint(2)
    if np == 0:
      continue
    if O == 1:
      values[x] += 1
      s.appendleft(x)
      q.appendleft(x)
      heapq.heappush(pq, -x)
    if O == 2:
      if values[x] > 0:
        values[x] -= 1
      else:
        np = 0
        continue
      if possible[PQ]:
        if pq:
          pq_x = -heapq.heappop(pq)
          if pq_x != x:
            possible[PQ] = False
            np -= 1
        else:
          possible[PQ] = False
          np -= 1
      if possible[STACK]:
        if s:
          s_x = s.popleft()
          if s_x != x:
            possible[STACK] = False
            np -= 1
        else:
          possible[STACK] = False
          np -= 1
      if possible[QUEUE]:
        if q:
          q_x = q.pop()
          if q_x != x:
            possible[QUEUE] = False
            np -= 1
        else:
          possible[QUEUE] = False
          np -= 1
  if np > 1:
    print("not sure")
  elif np == 0:
    print("impossible")
  else:
    match possible:
      case [True, _, _]:
        print("queue")
      case [_, True, _]:
        print("stack")
      case [_, _, True]:
        print("priority queue")
    
