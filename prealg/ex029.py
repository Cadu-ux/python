soma = 0
total = 0
for i in range (5):
    numero = float(input('Insira um numero: '))
    if numero % 2 == 0:
        soma += numero
        total += 1
if total != 0:
    print (f'A media dos seus numeros pares eh: {soma / total}')
else:
    print ('Nenhum numero par foi digitado')
        