n1 = int(input('Insira a quantidade de elementos do primeiro vetor: '))
n2 = int(input('Insira a quantidade de elementos do segundo vetor: '))
if n1 > 0 and n1 <= 50 and n2 > 0 and n2 <= 50:
    v1 = [0] * n1
    v2 = [0] * n2
    for i in range(len(v1)):
        v1[i] = int(input('Insira um valor para o primeiro vetor: '))
    for i in range (n2):
        v2[i] = int(input('Insira um valor para o segundo vetor: '))
    print('Vetor 1')
    print(v1)
    print('Vetor 2')
    print(v2)
    if n1==n2:
        v3 = [0] * n1
        for i in range (n1):
            v3[i] = v1[i] + v2[i]
        print('Vetor 3')
        print(v3)
    
    
else:
    print ('N deve estar entre 1 e 50')