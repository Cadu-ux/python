num = int(input('Insira um numero: '))
maior = num
while True:
    num = int(input('Insira um numero: '))
    if num == 0:
        break
    if num > maior:
        maior = num
print(f"O maior numero digitado foi {maior}")