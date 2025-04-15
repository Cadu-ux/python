digitado = False
entrada = input('Insira uma palavra: ')
maior = entrada
menor = entrada
contador = 0

while entrada != '':
    contador += 1
    if len(entrada) > len(maior):
        maior = entrada
    elif len(entrada) < len(menor):
        menor = entrada
    entrada = input('Insira uma palavra: ')
    
if contador > 0:
    print (f'Foram digitadas {contador} palavras')
    print (f'A maior palavra digitada foi {maior} e a menor foi {menor}')
else:
    print ('Nenhuma palavra digitada')