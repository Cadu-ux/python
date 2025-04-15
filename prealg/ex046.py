import random
palpites = 0
random = random.randint(1,100)
num = int(input('Insira um numero: '))
while num != random:
    if num > random:
        palpites += 1
        print ('O numero digitado eh maior que o numero sorteado')
    else:
        palpites += 1
        print ('O numero digitado eh menor que o numero sorteado')
    num = int(input('Tente novamente: '))
print (f'Parabens, voce acertou em {palpites} tentativas!')
