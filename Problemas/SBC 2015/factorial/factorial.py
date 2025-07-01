# https://judge.beecrowd.com/en/problems/view/1936

from functools import *
from operator import *

N = int(input())

def solve(n):
    facs = [0, 1] + [0] * 7 # max N is 10^5
    cur = 1
    i = 1
    while (cur * i) < n:
        i += 1
        cur = cur * i
        facs[i] = cur
    steps = 0
    while n > 0:
        facs = list(filter(partial(ge, n), facs))
        n -= max(facs)
        steps += 1
    return steps

print(solve(N))
