lista  = []
impares = []
pares = []
continuar = str(input('Digite para iniciar o programa [S/N]: ').strip().upper()[0])
while continuar not in 'SN':
    continuar = str(input('Digite corretamente [S/N]: ').strip().upper()[0])
while continuar in 'S':
    valor = int(input('Digite um numero: '))
    lista.append(valor)
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
    continuar = str(input('Quer continuar [S/N]: ').strip().upper()[0])
    while continuar not in 'SN':
        continuar = str(input('Digite corretamente [S/N]: ').strip().upper()[0])

print('-='*20)
print(f'Os valores digitados foram {lista}')
print(f'''Os valores pares foram {pares}
Os valores impares foram {impares}''')
