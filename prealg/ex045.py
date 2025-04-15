operador = '+'
while (operador in{'+', '-', '*', '/'}):
    operador = input('Insira um operador: ')
    num1 = int(input('Insira um numero: '))
    num2 = int(input('Insira outro numero: '))
    if operador == '+':
        print (f'{num1} + {num2} = {num1 + num2}')
    elif operador == '-':
        print (f'{num1} - {num2} = {num1 - num2}')
    elif operador == '*':
        print (f'{num1} * {num2} = {num1 * num2}')
    elif operador == '/':
        print (f'{num1} / {num2} = {num1 / num2}')
    else:
        print ('Operador invalido')
        break
print ('Deseja continuar?')
continuar = input('S/N: ')
if continuar == 'S' or continuar == 's':
    ex045()
    