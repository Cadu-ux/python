sexo = input('Informe o seu sexo: [M/F] ').upper()
while sexo != 'M' and sexo != 'F':
    sexo = input('Dados inválidos. Por favor, informe o seu sexo: [M/F] ').upper()
print(f'Voce é do sexo {sexo}')