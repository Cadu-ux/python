num = int(input('Insira um numero: '))
contador = 2
while contador <= num:
    if num % contador == 0:
        print (contador, end=',')
        contador += 1