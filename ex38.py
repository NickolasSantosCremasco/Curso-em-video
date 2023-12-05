print('Digite dois valores')
num1 = float(input('primeiro valor: '))
num2 = float(input('Segundo valor: '))

if num1 > num2:
    print('o {} é maior que o {}'.format(num1,num2))
elif num2 > num1:
    print('o {} é maior que {}'.format(num2,num1))
elif num1 == num2:
    print('Os dois valores são iguais')
else:
    print('Digite os valores corretamente')