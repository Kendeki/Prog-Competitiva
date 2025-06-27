input()
print(sum(map(lambda e: len(e) if len(e) > 1 else 0, input().split("b"))))