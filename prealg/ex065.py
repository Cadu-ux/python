n1 = int(input('Insira a quantidade de elementos do vetor: '))
v1 = [0] * n1
maior = v1 [0]
cont = 1
while cont < n1:
    v1[cont] = int(input('Insira um numero: '))
    if v1[cont] > maior:
        maior = v1[cont]
    cont += 1
for i in range (n1):
    if v1[i] == maior:
        print (f'{v1[i]} eh o maior numero do vetor')