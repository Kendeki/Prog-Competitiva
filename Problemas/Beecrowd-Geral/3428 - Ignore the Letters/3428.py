from sys import stdin

input()
numbers = list(map(lambda x: int(''.join([i for i in x if i.isdigit()])), stdin.readlines()))
print(sum(numbers))