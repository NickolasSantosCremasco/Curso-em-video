num = (int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')))
print(f'OS valores digitados forma {num}')
nove = num.count(9)
if nove == 1:
    print('O nove apareceu 1 vez')
else:
    print(f'O nove apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O numero 3 apareceu pela primeira vez no {num.index(3) + 1}° Lugar')
else:
    print('Valor 3 não encontrado')
print('Forma digitados esse numero de valores pares: ',end='')
for n in num:
    if n % 2 == 0:
        print(n, end=', ')