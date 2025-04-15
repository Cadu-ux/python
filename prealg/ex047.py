c1 = 0
c2 = 0
letras = input('Insira uma palavra: ')
for letra in letras:
    if letra in 'aAeEiIoOuU':
        c1 += 1
    elif letra not in '':
        c2 += 1
print (f'{c1} vogais e {c2} consoantes')
    
    