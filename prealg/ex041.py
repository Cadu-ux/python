op = int(input('Escolha uma opção: 1 - Somar, 2 - Subtrair, 3 - Multiplicar, 4 - Dividir, 0 - Sair: '))
while op < 0 or op > 4:
    op = int(input('Opçao invalida. Escolha uma opção: 1 - Somar, 2 - Subtrair, 3 - Multiplicar, 4 - Dividir, 0 - Sair: '))
if op == 0:
    print ('Saindo...')
    exit()
    
n1 = int(input('Insira um numero: '))
n2 = int(input('Insira outro numero: '))
if op == 1:
    print (n1 + n2)
elif op == 2:
    print (n1 - n2)
elif op == 3:
    print (n1 * n2)
elif op == 4:
    print (n1 / n2)
    
breakpoint
    

