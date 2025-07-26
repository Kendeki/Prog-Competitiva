def recurDiv(x: int, y: int = 0):
    notas = [100,50,20,10,5,2,1]
    print(f"{int(x/notas[y])} nota(s) de R$ {notas[y]},00")
    if y != 6:
        recurDiv(x % notas[y], y + 1)
n = int(input())
print(n)
recurDiv(n)
