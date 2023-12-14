valores = [[], []]

for x in range(0,7):
    valor = int(input(f'Digite o {x + 1}º Valor: '))
    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)
valores[0].sort()
valores[1].sort()
print(f'Os valores ímpares foram: {valores[1]}')
print(f'Os valores pares foram: {valores[0]}')

