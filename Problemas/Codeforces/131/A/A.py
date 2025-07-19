# https://codeforces.com/problemset/problem/131/A

# bruh

a = input()
if a.isupper():
  print(a.lower())
else:
  if len(a) == 1:
    print(a.upper())
  elif a[1:].isupper():
    print(a[0].upper()+a[1:].lower())
  else:
    print(a)
