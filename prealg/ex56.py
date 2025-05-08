tamanho = int(input('Insira o tamanho do vetor: '))
vetor = []
soma = 0
for i in range (tamanho):
    n = int(input('Insira o numero desejado: '))
    vetor.append(n)
    
for i in vetor:
    soma += i
    
media = soma / tamanho
print (f'O somatorio dos seus numeros eh {soma} e a media dos seus numeros eh {media}')