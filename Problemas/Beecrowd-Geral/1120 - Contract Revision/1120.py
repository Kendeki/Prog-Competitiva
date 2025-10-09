from sys import stdin

values = list(map(lambda x: x.split(), stdin.readlines()))
del values[-1]

for failure, digit in values:
    try:
        print(int(''.join([i for i in digit if i != failure])))
    except ValueError:
        print(0)