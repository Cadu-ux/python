soma = 0
quant = 0
while True:
    num = input('Insira um numero(pressione enter para parar): ')
    if num == '':
        break
    num = float(num)
    quant += 1
    soma += num
if quant == 0:
    print ('Nenhum numero foi digitado')
else:
    print (f'Foram digitados {quant} numeros e a media deles eh {soma / quant}')
