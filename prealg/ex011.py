idade = int(input('Insira sua idade: '))
if idade < 16:
    print ('Sua classe eleitoral é não eleitor')
elif idade == 16 or idade == 17:
    print ('Sua classe eleitoral é eleitor facultativo')
elif idade >= 18 and idade <= 65:
    print ('Sua classe eleitoral é eleitor obrigatorio')
else:
    print ('Sua classe eleitoral é eleitor facultativo')