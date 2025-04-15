# Solicita ao usuário que digite um número inteiro
num = int(input('Insira um número: '))

# Guarda o número original para exibir depois (ex: 5!)
original = num

# Inicializa o fatorial e a string de saída
fat = 1
expressao = ""

# Enquanto o número for maior que 0
while num > 0:
    fat *= num  # Multiplica o acumulador pelo número atual

    # Adiciona o número atual na expressão, seguido de " x " se não for o último
    if num == 1:
        expressao += f"{num}"
    else:
        expressao += f"{num} x "

    num -= 1  # Decrementa o número

# Exibe a expressão e o resultado
print(f"{original}! = {expressao}")
print(f"Resultado: {fat}")

# 5! = 5 x 4 x 3 x 2 x 1