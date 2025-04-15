opcao = int(input('Escolha uma opção: 1 - Somar, 2 - Subtrair, 3 - Multiplicar, 4 - Dividir, 0 - Sair: '))
while opcao > 4 or opcao < 0:
    opcao = input('Opçao invalida. Escolha uma opção: 1 - Somar, 2 - Subtrair, 3 - Multiplicar, 4 - Dividir, 0 - Sair: ')
if opcao ==1:
    n1 = int(input('Insira um numero: '))
    n2 = int(input('Insira outro numero: '))
    print (n1 + n2)
elif opcao == 2:
    n1 = int(input('Insira um numero: '))
    n2 = int(input('Insira outro numero: '))
    print (n1 - n2)
elif opcao == 3:
    n1 = int(input('Insira um numero: '))
    n2 = int(input('Insira outro numero: '))
    print (n1 * n2)
elif opcao == 4:
    n1 = int(input('Insira um numero: '))
    n2 = int(input('Insira outro numero: '))
    print (n1 / n2)
    
elif opcao == 0:
    print ('Saindo...')
    exit()