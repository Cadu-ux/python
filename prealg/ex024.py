import random

numero = random.randrange(1,101)
meu_palpite = int(input('Adivinhe um numero entre 1 e 100: '))
for palpites in range (1,101):
    if meu_palpite > numero:
        print ( meu_palpite,'eh maior que o numero')
    elif meu_palpite < numero:
        print (meu_palpite,'eh menor que o numero')
    elif meu_palpite == numero:
        break
    meu_palpite = int(input('Tente novamente: '))

print (f'\nÓtimo, voce acertou em {palpites} tentativas')