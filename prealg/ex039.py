#fibonacci
n = int(input('Insira um numero: '))
x = 1
y = 1
for i in range (n):
    print (x)
    aux = x
    x = y
    y = aux + y
    
