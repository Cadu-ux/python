n = int(input('Insira o valor de N: '))
if n > 0 and n <= 50:
    nomes = []*n
    for i in range (n):
        nomes[i] = input('Insira um nome: ')
        
        
        print('Ordem inversa')
        for i in range(len(nomes)-1, -1, -1):
            print(nomes[i])
else:
    print ('N deve estar entre 1 e 50')