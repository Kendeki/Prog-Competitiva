# https://codeforces.com/problemset/problem/71/A

print("\n".join([palavra if len(palavra := input()) < 11 else palavra[0] + str(len(palavra) - 2) + palavra[-1] for _ in range(int(input()))]))
