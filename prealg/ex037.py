cont = 0
soma = 0
while True:
    x = int(input('Insira um numero: '))
    if (x >= 0):
        cont += 1
        soma += x
    else:
        break
print (f'media: {soma / cont}')