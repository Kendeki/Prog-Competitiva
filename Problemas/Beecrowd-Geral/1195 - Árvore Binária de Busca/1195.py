# automatic
import sys; from collections import deque
lns = deque(map(lambda l:l.strip().split(), sys.stdin.readlines()))
def readint(n):
  ln = lns.popleft(); assert len(ln) == n
  return [int(x) for x in ln]
def EOF(): return not lns
def skip(): lns.popleft()
# automatic

class bt:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
  def hasLeft(self):
    return self.left is not None
  def hasRight(self):
    return self.right is not None

def recurse_pre(tree):
  print(f" {tree.val}",end="")
  if tree.hasLeft():
    recurse_pre(tree.left)
  if tree.hasRight():
    recurse_pre(tree.right)
    
def recurse_in(tree):
  if tree.hasLeft():
    recurse_in(tree.left)
  print(f" {tree.val}",end="")
  if tree.hasRight():
    recurse_in(tree.right)
    
def recurse_post(tree):
  if tree.hasLeft():
    recurse_post(tree.left)
  if tree.hasRight():
    recurse_post(tree.right)
  print(f" {tree.val}",end="")

def print_tree(tree):
  print("Pre.:",end="")
  recurse_pre(tree)
  print()
  print("In..:",end="")
  recurse_in(tree)
  print()
  print("Post:",end="")
  recurse_post(tree)
  print("\n")

skip()

c = 0
while not EOF():
  N, = readint(1)
  x, *xs = readint(N)
  tree = bt(x)
  for x in xs:
    t = tree
    while True:
      if x > t.val:
        if t.hasRight():
          t = t.right
        else:
          t.right = bt(x)
          break
      else:
        if t.hasLeft():
          t = t.left
        else:
          t.left = bt(x)
          break
  c += 1
  print(f"Case {c}:")
  print_tree(tree)
  
