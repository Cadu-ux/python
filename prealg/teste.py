menor = 0
maior = 0
n = int(input('Insira um numero: '))
menor = n
maior = n

for i in range (9):
    n = int(input('Insira um numero: '))
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
        
print (f'O maior numero digitado foi {maior} e o menor foi {menor}')