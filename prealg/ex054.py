n = int(input('Insira o valor de N: '))
if n > 0 and n <= 50:
    nomes = []*n
    for i in range (n):
        nomes[i] = input('Insira um nome: ')
        
        print('Ordem inversa')
        cont = n - 1
        while cont >= 0:
            print(nomes[cont])
            cont -= 1
else:
    print ('N deve estar entre 1 e 50')