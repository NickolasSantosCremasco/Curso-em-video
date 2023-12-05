print('Digite 3 numeros: ')
num1 = int(input('N1:'))
num2 = int(input('N2:'))
num3 = int(input('N3:'))
maior = num1
if num2>num1 and num2>num3:
    maior = num2
elif num3> num1 and num3>num2:
    maior = num3
menor = num1
if num2<num1 and num2<num3:
    menor = num2

elif num3<num1 and num3<num2:
    menor = num3
print('O menor é {}'.format(menor))
print('O maior é {}'.format(maior))
