n = int(input('Insira o valor de n: '))
acumuladora = 0
for numero in range (n):
    aux = int(input('Insira um numero: '))
    acumuladora = acumuladora + aux
print (f'A soma dos seus numeros eh: {acumuladora}')