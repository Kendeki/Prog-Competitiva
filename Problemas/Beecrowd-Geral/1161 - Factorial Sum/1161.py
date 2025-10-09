from sys import stdin

def factorial(x: int) -> int:
    product = 1
    for i in range(2, x+1):
        product *= i
    return product

values = list(map(lambda x: (int(i) for i in x), map(lambda x: x.split(), stdin.readlines())))

for x,y in values:
    print(factorial(x) + factorial(y))
