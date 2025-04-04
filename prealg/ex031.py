total = int(input('Insira um numero de jogadores: '))
alt = 0
for i in range (total):
    altura = float(input('Insira a altura do jogador: '))
    alt += altura
print (f'A media das alturas eh: {alt / total:.2f}')