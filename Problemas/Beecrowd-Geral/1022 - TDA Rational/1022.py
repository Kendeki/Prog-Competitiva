from sys import stdin

def mdc(a: int, b: int) -> int:
    while True:
        r = a % b
        if not r:
            return b
        a, b = b, r

def op(exp: list) -> str:
    for i in range(len(exp)):
        try:
            exp[i] = int(exp[i])
        except ValueError:
            pass
        
    if exp[3] == "+":
        return str((exp[0] * exp[6]) + (exp[4] * exp[2])) + '/' + str(exp[2] * exp[6])
    if exp[3] == "-":
        return str((exp[0] * exp[6]) - (exp[4] * exp[2])) + '/' + str(exp[2] * exp[6])
    if exp[3] == "*": 
        return str((exp[0] * exp[4])) + '/' + str(exp[2] * exp[6])
    if exp[3] == "/": 
        return str((exp[0] * exp[6])) + '/' + str(exp[4] * exp[2])

input()

exp = list(map(lambda x: op(x.split()), stdin.readlines()))
for i in exp:
    index = i.find("/")
    divisor = mdc(int(i[:index]), int(i[index + 1:]))
    print(f"{i} = {str(int(int(i[:index]) / divisor)) + '/' + str(int(int(i[index + 1:]) / divisor))}")