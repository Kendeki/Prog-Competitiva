from functools import *
from operator import *

print("S" if all(map(partial(contains, ["1","0"]), input().split())) else "F")
