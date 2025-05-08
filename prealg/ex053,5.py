n = int(input('Insira o valor de N: '))
if n > 0 and n <= 50:
    nomes = []
    for i in range(n):
        nome = input('Insira um nome: ')
        nomes.append(nome)
        
    print('Ordem inversa:')
    for i in range(len(nomes) - 1, -1, -1):
        print(nomes[i])
else:
    print('N deve estar entre 1 e 50')
