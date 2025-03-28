nome = input('Insira seu nome: ')
idade = int(input('Insira sua idade: '))
if idade < 10:
    print (f'{nome} devera pagar R$ 130,00')
elif idade < 29:
    print (f'{nome} devera pagar R$ 160,00')
elif idade < 45:
    print (f'{nome} devera pagar R$ 220,00')
elif idade < 59:
    print (f'{nome} devera pagar R$ 250,00')
elif idade < 65:
    print (f'{nome} devera pagar R$ 350,00')
else:
    print (f'{nome} devera pagar R$ 600,00')


