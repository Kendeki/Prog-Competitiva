# recebe TODO o input do arquivo de uma vez, e já acessa tratado
# ultimamente venho preferindo esse pela simplicidade

"""
Exemplo de uso:

while not EOF():
  A, B = readint(2)
  print(A, B)
"""

import sys; from collections import deque
lns = deque(map(lambda l:l.strip().split(), sys.stdin.readlines()))
def readint(n):
  ln = lns.popleft(); assert len(ln) == n
  return [int(x) for x in ln]
def EOF(): return not lns
