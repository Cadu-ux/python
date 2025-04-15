
num = int(input('Insira um numero: '))
razao = int(input('Insira a razao: '))
termo = num
cont = 1
while cont <= 10:
    termo = termo + razao
    print (f'{termo}', end=' → ' if cont < 10 else ' ✅\n')
    cont += 1