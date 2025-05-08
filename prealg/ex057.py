n = int(input('Insira o numero de elementos: '))
vetor = []
par = 0
impar = 0
for i in range(n):
    num = int(input('Insira um numero: '))
    vetor.append(num)
for i in vetor:
    if i % 2 == 0:
        par += 1
    else:
        impar += 1
print (f'Foram digitados {par} numeros pares e {impar} numeros impares')