import random
pedra = 0
papel = 1
tesoura = 2
computador = random.randint(0,2)
entrada = ''
while entrada != 'N' or entrada != 'n':
    print ('[0] Pedra')
    print ('[1] Papel')
    print ('[2] Tesoura')
    jogador = int(input('Escolha uma opcao: '))
    if jogador == 0 and computador == 2:
        print ('Parabens, voce ganhou!')
    elif jogador == 1 and computador == 0:
        print ('Parabens, voce ganhou!')
    elif jogador == 2 and computador == 1:
        print ('Parabens, voce ganhou!')
    elif jogador == computador:
        print ('Empate!')
    else:
        print ('Que pena, voce perdeu!')
        entrada = input('Deseja jogar novamente? [S/N] ')