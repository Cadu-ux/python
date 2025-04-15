fat = 1
num = int(input('Insira um numero: '))
while num != 0:
    fat = fat * num
    num -= 1
print (f"O fatorial do numero eh {fat}")