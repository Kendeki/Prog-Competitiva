# https://codeforces.com/problemset/problem/96/A

if len((time := input())) > 7:
    for i in range(len(time) - 6):
        if all(x == time[i] for x in time[i:i+7]):
            print("YES")
            exit()
    else: print("NO")
else: print("NO")
