n1 = int(input('Insira a quantidade de elementos do vetor: '))
v1 = [0] * n1
soma = 0
for i in range (n1):
    v1[1] = int(input('Insira um numero: '))
    soma += v1[i]
media = soma / n1
print (f'A media dos seus numeros eh: {media}')
for i in range (n1):
    if v1(i) > media:
        print (v1[i])