l1 = float(input('Insira um lado do triangulo: '))
l2 = float(input('Insira outro lado do triangulo: '))
l3 = float(input('Insira outro lado do triangulo: '))
if l1 == l2 == l3:
    print ('O triangulo eh equilatero')
elif l1 == l2 or l1 == l3 or l2 == l3:
    print ('O triangulo eh isosceles')
else:
    print ('O triangulo eh escaleno')