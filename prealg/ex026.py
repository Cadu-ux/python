c = 0
for n in range(10):
    numero = int(input('Insira um numero: '))
    if numero >= 10 and numero <= 150:
        c += 1
print (f'{c} numeros estao entre 10 e 150')