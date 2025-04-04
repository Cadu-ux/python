n1 = int(input('Insira um numero: '))
n2 = int(input('Insira um numero: '))
n3 = int(input('Insira um numero: '))
n4 = int(input('Insira um numero: '))
n5 = int(input('Insira um numero: '))
p = 0
im = 0
po = 0
ne = 0
for i in (n1, n2, n3, n4, n5):
    if i % 2 == 0:
        p += 1
    else:
        im += 1
        
    if i > 0:
        po += 1
    elif i < 0:
        ne += 1       
print(f'{p} valores pares')
print(f'{im} valores impares')
print(f'{po} valores positivos')
print(f'{ne} valores negativos')

