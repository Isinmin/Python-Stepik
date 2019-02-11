def nok(a,b):
    d= a*b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return d // (a+b)

a = int(input())
b = int(input())
print(nok(a,b))