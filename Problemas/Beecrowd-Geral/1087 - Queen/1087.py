from sys import stdin

def sameLine(x: list) -> bool:
    return (abs(x[2] - x[0]) == abs(x[3] - x[1]) 
            or (x[2] == x[0])
            or (x[3] == x[1]))

def equal(x: list) -> bool:
    return x[2] == x[0] and x[3] == x[1]

cases = list(map(lambda x: [int(i) for i in x], map(lambda y: y.split(), stdin.readlines())))

for i in cases[:-1]:
    if equal(i):
        print(0)
    elif sameLine(i):
        print(1)
    else: 
        print(2)