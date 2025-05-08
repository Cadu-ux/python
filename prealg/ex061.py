palavra = input('Insira uma palavra: ')
while True:
    sair = 0
    letraTroca = input('Insira a letra que deve ser substituida: ')
    
    for letra in palavra:
        if letra == letraTroca:
            sair = 1
            break
    if sair == 1:
        break
novaLetra = input('Insira a letra substituta: ')
novaPalavra = ''
for letra in palavra:
    if letra == letraTroca:
        novaPalavra += letraTroca
    else:
        novaPalavra += letra
        
print (f'Palavra original: {palavra}\nPalavra nova: {novaPalavra}')