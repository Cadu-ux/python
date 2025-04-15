c100 = 0
c50 = 0
c20 = 0
c10 = 0
c5 = 0
c2 = 0
c1 = 0
valor = int(input('Insira um valor: '))
while valor >= 100:
    valor -= 100
    c100 += 1

while valor >= 50:
    valor -= 50
    c50 += 1

while valor >= 20:
    valor -= 20
    c20 += 1

while valor >= 10:    
    valor -= 10
    c10 += 1

while valor >= 5:
    valor -= 5
    c5 += 1

while valor >= 2:    
    valor -= 2
    c2 += 1

while valor >= 1:
    valor -= 1
    c1 += 1

print (f'{c100} cedulas de 100')
print (f'{c50} cedulas de 50')
print (f'{c20} cedulas de 20')
print (f'{c10} cedulas de 10')
print (f'{c5} cedulas de 5')
print (f'{c2} cedulas de 2')
print (f'{c1} cedulas de 1')
    