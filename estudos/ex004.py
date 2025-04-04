n1 = float(input('Insira um numero: '))
n2 = float(input('Insira um numero: '))
n3 = float(input('Insira um numero: '))
n4 = float(input('Insira um numero: '))
n5 = float(input('Insira um numero: '))
n6 = float(input('Insira um numero: '))
s = 0
c = 0
for i in (n1, n2, n3, n4, n5,n6):
    if i > 0:
        s += i
        c += 1
        m = s / c
print(f'{c} valores positivos')
print(m)



