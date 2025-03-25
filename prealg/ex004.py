salariob = float(input('Insira o salario bruto: '))
quantfilhos = int(input('Insira a quantidade de filhos: '))
quantfilhos2 = (quantfilhos / 100) + 1
s1 = salariob * 0.8
s2 = s1 * quantfilhos2
if quantfilhos > 0:
    print (f'O salario liquido eh: {s1} ')
else:
    print (f'O salario liquido eh: {s2} ') 