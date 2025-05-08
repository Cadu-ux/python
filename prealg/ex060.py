palavra = input('Insira uma palavra: ')
contador = 0
for letra in palavra:
    if letra in 'abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        contador += 1
print (f'Foram digitadas {contador} caracteres')