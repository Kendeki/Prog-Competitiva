# i made this so i could copy paste
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
