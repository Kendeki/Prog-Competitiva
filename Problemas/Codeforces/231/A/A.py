# https://codeforces.com/problemset/problem/231/A

print(sum([int(input().count("1") > 1) for _ in range(int(input()))]))
