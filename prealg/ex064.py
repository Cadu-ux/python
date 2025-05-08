n1 = int(input('Insira a quantidade de elementos do vetor: '))
v1 = [0] * n1

for i in range (n1):
    v1[i] = int(input('Insira um numero: '))
for i in range((len(v1)//2)):
    aux = v1[i]
    v1[i] = v1[len(v1) - 1 - i]
    v1[len(v1) - 1 - i] = aux
print (v1)