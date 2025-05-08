n1 = int(input('Insira a quantidade de elementos dos vetores: '))
v1 = [0] * n1
v2 = [0] * n1

for i in range (n1):
    v1[i] = int(input('Insira um numero do primeiro vetor: '))
for i in range (n1):
    v2[i] = int(input('Insira um numero do segundo vetor: '))
v3 = [0] * (n1 * 2)
for i in range (n1):
    v3[i*2] = v1[i]
    v3[i*2+1] = v2[i]
print(v1)
print(v2)
print(v3)