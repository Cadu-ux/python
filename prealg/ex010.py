nome = (input('Insira seu nome: '))
n1 = float(input('Insira a nota da primeira prova: '))
n2 = float(input('Insira a nota da segunda prova: '))
if (n1 + n2) / 2 >= 7:
    print (f'O aluno {nome} tirou nota {n1} e {n2}, teve media {(n1 + n2) / 2} e foi aprovado')
elif (n1 + n2) / 2 <= 3:
    print (f'O aluno {nome} tirou nota {n1} e {n2}, teve media {(n1 + n2) / 2} e foi reprovado')
else:
    print (f'O aluno {nome} tirou nota {n1} e {n2}, teve media {(n1 + n2) / 2} e ficou de recuperacao final')