T = [list(map(lambda x: int(x), input().split(" "))) for i in range(int(input()))]
T = {key: value for key, value in zip(list(map(lambda x: str(x), range(1, len(T) + 1))), T)}
P = [list(map(lambda x: int(x), input().split(" "))) for i in range(int(input()))]

for line in P:
    tokens = []
    for i in T:
        if T[i][0]*line[0] + line[1] > T[i][1]:
            tokens.append(i)
    print(len(tokens), ' '.join(tokens))
    [T.pop(t) for t in tokens]
