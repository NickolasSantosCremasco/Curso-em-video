salario = float(input('Digite seu salário: '))
if salario >= 1250:
    desconto = (salario*10)/100
    aumento = desconto+salario
    print('o aumento foi de {}'.format(aumento))
else:
    desconto = (salario * 15) / 100
    aumento = desconto + salario
    print('o aumento foi de {}'.format(aumento))
